---
status: investigating
trigger: "develop-compacted.md includes full codeblocks instead of hiding them by default; no AI summaries for notebook cells"
created: 2026-04-10T23:37:00.000Z
updated: 2026-04-10T23:37:00.000Z
---

## Current Focus

hypothesis: Two distinct bugs — (1) `compact_notebook()` defaults `include_code=True`, and (2) notebook path bypasses the entire summarization pipeline so no LLM summaries are ever generated for cell code
test: `glma query develop.ipynb -o develop-compacted.md` from linux_kernel worktree
expecting: Compacted output with code hidden and AI summaries visible
next_action: Decide whether to fix defaults in `compact_notebook()` / CLI, and design notebook-aware summarization path

## Symptoms

expected: `develop-compacted.md` shows collapsed/hidden code blocks with AI-generated summaries describing what each cell does
actual: Full Python source code is rendered in every code cell's ```python block; no summary text beyond rule-based variable tracking
errors: No errors — it's a design gap, not a crash
reproduction: `cd 02-worktrees/linux_kernel && glma query develop.ipynb -o develop-compacted.md`
started: Always been this way — notebook compaction was never wired to hide code by default or to use AI summarization

## Root Causes

### Bug 1: `include_code` defaults to `True`

In `src/glma/query/notebook.py`:
```python
def compact_notebook(filepath, include_outputs=False, include_code=True) -> str:
```

In `src/glma/cli.py` (query command):
```python
result_text = compact_notebook(disk_path, include_outputs=include_outputs, include_code=not summary_only)
```

Code is only hidden when `--summary-only` is passed. The default (no flags) dumps full source — the opposite of what "compacted" implies.

### Bug 2: Notebooks bypass the summarization pipeline entirely

In `src/glma/cli.py` (query command), notebooks short-circuit before touching LadybugStore:
```python
if filepath.endswith('.ipynb'):
    result_text = compact_notebook(disk_path, ...)
    _write_output(result_text, output)
    return  # <-- exits before any summarization
```

The `glma index --summarize` flow only works for regular source files (`.py`, `.c`) that go through `extract_chunks()` → `LadybugStore.upsert_chunks()` → `summarize_chunks()`. Notebook cells are never stored as chunks and never reach the LLM summarizer.

## Eliminated

- hypothesis: The summarization provider is broken
  evidence: AI summarization works for `.py` and `.c` files indexed through the normal pipeline. The issue is notebooks never enter that pipeline.
  timestamp: 2026-04-10T23:37:00Z

- hypothesis: The `--summary-only` flag is being ignored for notebooks
  evidence: Already fixed in a prior debug session (`2026-04-10-notebook-summary-only-ignored.md` in resolved/). The flag works; the problem is the default behavior when no flag is passed.
  timestamp: 2026-04-10T23:37:00Z

## Evidence

- timestamp: 2026-04-10T23:37:00Z
  checked: Read `develop-compacted.md` (60KB, 1823 lines) — every code cell has full source in ```python blocks
  found: No AI summary text anywhere in the file; only rule-based variable annotations
  implication: The "compacted" output is not compacted at all — it's a full dump with variable annotations

- timestamp: 2026-04-10T23:37:00Z
  checked: Traced CLI → `compact_notebook()` → `_format_cell()` in `src/glma/query/notebook.py`
  found: `_format_cell()` has `include_code` param that controls code block emission, defaults to `True`
  implication: Simple fix — flip the default or change the CLI wiring

- timestamp: 2026-04-10T23:37:00Z
  checked: Traced `glma index --summarize` → `summarize_chunks()` in `src/glma/summarize/pipeline.py`
  found: Pipeline operates on `Chunk` objects from LadybugStore. Notebook cells are `CellVariableInfo` objects — incompatible types, never stored in DB.
  implication: Significant design work needed to bridge notebook cells into the summarization pipeline

## Proposed Fixes

### Fix 1 (easy): Invert `include_code` default for "compacted" output

**DONE (2026-04-10):**
- Flipped `compact_notebook()` default to `include_code=False`
- Added `--include-code` CLI flag (opt-in)
- Added tests `test_code_hidden_by_default` and `test_code_shown_when_requested`
- 257 tests passing

### Fix 2 (medium): Wire notebook cells into summarization pipeline

Options:
- **Option A**: Convert notebook cells to `Chunk` objects, store in LadybugStore alongside regular file chunks, run through existing `summarize_chunks()` pipeline
- **Option B**: Add a notebook-specific summarization step in `compact_notebook()` that calls the provider directly per cell
- **Option C**: Add `--summarize` flag to `glma query` for notebooks only, using a lightweight cell-by-cell approach

### Affected Files

| File | Role |
| ---- | ---- |
| `src/glma/query/notebook.py` | `compact_notebook()`, `_format_cell()` — defaults and code emission |
| `src/glma/cli.py` | `query` command — notebook dispatch, flag wiring |
| `src/glma/summarize/pipeline.py` | `summarize_chunks()` — may need notebook-aware variant |
| `src/glma/summarize/providers.py` | Provider interface — reused as-is for notebook cells |

## Resolution

root_cause: Two-part — (1) `include_code=True` default ✅ FIXED, (2) notebooks excluded from summarization pipeline — still open
fix: Bug 1 fixed (default flipped, --include-code flag added). Bug 2 tracked in `.planning/todos/pending/2026-04-10-per-chunk-ai-summaries-from-local-llm.md`
verification: `glma query develop.ipynb` now hides code by default. AI summaries for notebooks still pending.
files_changed: [src/glma/query/notebook.py, src/glma/cli.py, tests/test_notebook.py]
