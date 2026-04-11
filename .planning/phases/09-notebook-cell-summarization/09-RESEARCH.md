# Phase 9 Research: Notebook Cell Summarization

**Researched:** 2026-04-11
**Status:** Complete

## Research Question

What do I need to know to PLAN notebook cell summarization well?

## 1. Current Notebook Query Flow

The notebook query path is entirely bypass-based — no LadybugStore involved:

```
cli.py:query()
  → filepath.endswith('.ipynb') → dispatches to compact_notebook()
  → compact_notebook(filepath, include_outputs, include_code) → returns markdown string
  → _write_output(result_text, output)
```

Key observations:
- `compact_notebook()` has exactly 3 parameters: `filepath`, `include_outputs`, `include_code`
- No provider, no cache dir, no repo_root passed in currently
- The early return in cli.py means query flags like `--verbose`, `--depth`, `--no-relationships` are ignored for notebooks
- `_write_output()` is a shared helper for file/stdout output

## 2. Integration Point: compact_notebook()

The function signature needs to expand to accept optional summarization parameters. Based on CONTEXT.md decisions:

```python
def compact_notebook(
    filepath: str | Path,
    include_outputs: bool = False,
    include_code: bool = False,
    # NEW parameters for summarization:
    provider: SummarizerProvider | None = None,
    cache_dir: Path | None = None,
) -> str:
```

When `provider` is None → current behavior, zero changes to output.

The internal flow needs modification:
1. After parsing notebook and extracting cell_infos → iterate code cells
2. For each code cell with ≥3 non-empty lines → check cache → call provider if uncached
3. Pass summary to `_format_cell()` which renders it as a blockquote

## 3. Integration Point: _format_cell()

Currently `_format_cell()` has this signature:
```python
def _format_cell(
    index: int,
    cell_info: CellVariableInfo,
    variable_flow: dict,
    include_outputs: bool,
    outputs: list,
    include_code: bool = True,
) -> list[str]:
```

Needs to add an optional `summary: str | None = None` parameter. When present, render before the code/annotations block:
```
> *Summary: <LLM-generated text>*
```

This aligns with D-07 from CONTEXT.md.

## 4. Cache Design Analysis

### Schema (from D-09, D-10):
```json
{
  "cells": [
    {"index": 0, "content_hash": "blake2b_hex", "summary": "..."},
    {"index": 1, "content_hash": "blake2b_hex", "summary": "..."}
  ]
}
```

Location: `<repo_root>/.glma-index/notebook-cache/<notebook-stem>-<file-hash>.json`

### Content hashing:
- `file_content_hash()` in `index/pipeline.py` uses `hashlib.blake2b(content, digest_size=32).hexdigest()` — 64-char hex
- For cells, we hash individual cell source: `hashlib.blake2b(cell.source.encode(), digest_size=32).hexdigest()`

### Cache invalidation:
- Per-cell: if `content_hash` differs → regenerate summary
- Per-notebook: file hash in filename → if notebook changes, new cache file created (old ones orphaned)
- Actually, looking at D-09 more carefully: `<notebook-stem>-<file-hash>.json` means a new file per notebook version. But the cell-level hashes handle incremental updates. This is slightly redundant — the file hash in the filename means if ANY cell changes, you get a new cache file. But the cell hashes mean you only re-summarize changed cells.

### Implementation approach:
- Create a `NotebookCache` helper class (can live in notebook.py or a separate cache module)
- `load_cache(cache_dir, notebook_path) -> dict[int, tuple[str, str]]` (cell_index → (content_hash, summary))
- `save_cache(cache_dir, notebook_path, cells_data) -> None`
- Cache dir is lazy-created on first save

### File hash for cache filename:
We need the whole-notebook hash for the filename. Use `file_content_hash()` pattern from index/pipeline.py.

## 5. CLI Flag Integration

Current `query` command flags (relevant subset):
```python
@app.command()
def query(
    filepath: str = ...,
    include_outputs: bool = ...,
    include_code: bool = ...,
    repo_root: Optional[Path] = ...,
    ...
)
```

Need to add (matching `index` command's flags):
```python
    summarize: bool = typer.Option(False, "--summarize", ...),
    summarize_provider: Optional[str] = typer.Option(None, "--summarize-provider", ...),
    summarize_model: Optional[str] = typer.Option(None, "--summarize-model", ...),
```

The notebook dispatch block needs to:
1. Check `--summarize` flag
2. If set, load `SummarizeConfig` via `load_summarize_config(repo_root, overrides)`
3. Instantiate provider (same pattern as `index` command)
4. Determine cache_dir = `repo_root / ".glma-index" / "notebook-cache"`
5. Pass `provider` and `cache_dir` to `compact_notebook()`

## 6. Cell Filtering Logic

From success criteria #6 and CONTEXT.md specifics:
- Skip cells with < 3 non-empty lines
- Skip markdown cells (they're already prose)
- Only summarize code cells

Filter: `len([line for line in cell.source.splitlines() if line.strip()]) >= 3`

## 7. Error Handling Strategy

When provider is unavailable:
- CONTEXT.md marks this as "agent's Discretion"
- Recommended: **fail open** — if provider raises, log warning, skip that cell's summary, continue with rule-based output
- This matches the pattern in `summarize_chunks()` pipeline which catches exceptions and continues
- A cell without a summary just doesn't show the blockquote line — no regression

## 8. System Prompt for Cell Summarization

The existing `OpenAICompatibleProvider.SYSTEM_PROMPT` is:
```
"Summarize this code chunk in 1-2 concise sentences for a developer. 
Focus on purpose, inputs, outputs, and key behavior. 
Do not repeat the function/class name as the first word."
```

For notebook cells, the context string should include (from CONTEXT.md specifics):
- Notebook filename
- Cell index
- Cell type
- Section heading the cell belongs to

This means we need a different system prompt or context builder for cells vs chunks. The provider's `summarize()` method takes `code` and `context` — we can customize the `context` parameter per cell without changing the system prompt.

Recommended cell context format:
```
Notebook: analysis.ipynb
Cell: 5 [code]
Section: "Data Cleaning"
```

## 9. Test Strategy

### Existing tests to not break:
- `test_notebook.py` has 9 tests — all call `compact_notebook()` without provider/cache
- These MUST continue to pass (success criteria #5: no regressions without --summarize)

### New tests needed (success criteria #7):
1. **Cache logic tests:**
   - Cache is created on first summarize call
   - Cache is loaded on subsequent calls
   - Changed cell content triggers re-summarization
   - Unchanged cells use cached summary
   - Trivial cells (< 3 lines) are not cached/summarized

2. **Provider integration tests:**
   - MockProvider returns summaries that appear in output
   - Blockquote format `> *Summary: ...*` in output
   - Provider failure = no summary line, no crash
   - Both code-visible and code-hidden modes show summaries

3. **CLI flag tests:**
   - `--summarize` flag triggers provider instantiation
   - `--summarize-provider` and `--summarize-model` are passed through
   - Without `--summarize`, notebook output is unchanged

### Test patterns from existing code:
- Use `MockProvider` from `test_summarize.py` pattern (simple class with `summarize()` method)
- Use `nbformat.v4.new_notebook()` / `new_code_cell()` / `new_markdown_cell()` for fixtures
- Use `tmp_path` fixture for cache directory

## 10. Files to Modify

| File | Change |
|------|--------|
| `src/glma/query/notebook.py` | Add cache helper, modify `compact_notebook()` and `_format_cell()`, add summarization logic |
| `src/glma/cli.py` | Add `--summarize`, `--summarize-provider`, `--summarize-model` flags to `query` command; wire provider in notebook dispatch |
| `tests/test_notebook.py` | Add tests for cache, provider integration, cell filtering |

Files NOT modified:
- `src/glma/summarize/providers.py` — providers work as-is
- `src/glma/config.py` — `load_summarize_config()` works as-is
- `src/glma/models.py` — no new models needed (no DB changes)
- `src/glma/summarize/pipeline.py` — we don't use `summarize_chunks()` (cells aren't Chunk objects)

## 11. Dependency Order

This phase depends on Phase 7 (summarization providers) — **confirmed complete**. All provider classes exist:
- `SummarizerProvider` protocol ✓
- `OpenAICompatibleProvider` ✓  
- `PiProvider` ✓
- `load_summarize_config()` ✓
- `SummarizeConfig` model ✓

## RESEARCH COMPLETE

All integration points identified, patterns documented, approach validated against existing codebase.
