# Phase 5: Bug Fixes — Research

**Researched:** 2026-04-10
**Status:** Research complete

## Research Question

What do I need to know to PLAN Phase 5 (Bug Fixes) well?

Three targeted bugs, all with known file locations and clear success criteria. Research focused on understanding the exact code paths, confirming root causes, and identifying safe fix strategies that preserve the 211 existing tests.

---

## BUG-1: Export defaults to summaries-only (FIX-01)

### Current Behavior
- `ExportConfig.include_code` defaults to `True` in `models.py:108`
- CLI has `--no-code` flag that sets `include_code=False` (`cli.py:318-321`)
- Default export output includes full source code in every chunk

### Desired Behavior
- `ExportConfig.include_code` defaults to `False`
- CLI flag becomes `--include-code` (positive opt-in to include source)
- `glma export` without flags → signatures/summaries only

### Root Cause Analysis
This is a **design oversight**, not a code bug. The default was set to `True` during Phase 4 implementation before the UX direction was clarified. The fix is straightforward:

1. **`models.py:108`** — Change `default=True` to `default=False` in `ExportConfig.include_code`
2. **`cli.py:318-321`** — Replace `--no-code` with `--include-code` flag that sets `include_code=True`
3. **`cli.py` export command** — Update the `export_overrides` dict to handle the new flag semantics

### Affected Code Paths

| File | Lines | Change |
| ---- | ----- | ------ |
| `models.py` | L108 | `default=True` → `default=False` |
| `cli.py` | L318-321 | Replace `--no-code` flag with `--include-code` |
| `cli.py` | L330-331 | Update `export_overrides` logic for new flag |

### Test Impact
- `test_export.py::TestFormatExportFile::test_code_included_by_default` — This test creates `ExportConfig()` and asserts `python` code blocks appear. After the fix, `ExportConfig()` will have `include_code=False`, so this test will FAIL. Must update to `ExportConfig(include_code=True)`.
- `test_export.py::TestFormatExportFile::test_code_excluded` — Creates `ExportConfig(include_code=False)`. This still works, just redundant with new default. Can leave as-is for clarity.
- `test_export.py::TestExportCLI::test_export_in_help` — Just checks help text, no impact.
- No other tests assert on `include_code` default.

### Risk Assessment
**Low risk.** One test needs updating. The config-loading pipeline (`config.py:load_export_config`) merges `.glma.toml [export]` with CLI overrides, so existing `.glma.toml` files with explicit `include_code=true` will still work.

---

## BUG-2: Notebook cell source truncation for comprehensions (FIX-02)

### Current Behavior
Per CONTEXT.md, comprehensions (list/dict/set) are reportedly truncated in notebook cell output. The query path for notebooks is:

1. User runs `glma query <file.ipynb>`
2. `cli.py:query()` dispatches to `compact_notebook()` in `notebook.py`
3. `compact_notebook()` reads cells with `nbformat`, calls `extract_cell_variables()` for each code cell
4. Output uses `cell_info.source` (the raw cell source from nbformat) in the markdown code block

### Code Path Analysis

**`notebook.py:compact_notebook()`** (L155-200):
- Reads `nb.cells` via nbformat
- For code cells: calls `extract_cell_variables(cell.source, index)`
- Stores `source=cell.source` in `CellVariableInfo`
- `_format_cell()` renders `cell_info.source` in a ` ```python ``` ` block

**`variables.py:extract_cell_variables()`** (L73-170):
- Parses `cell_source` with `ast.parse(cell_source)`
- Iterates `tree.body` for top-level statements
- Handles: `Assign`, `AugAssign`, `FunctionDef`, `ClassDef`, `Import`, `ImportFrom`, `For`, `With`, `Return`, `Expr`
- **NOT handled:** `ListComp`, `SetComp`, `DictComp`, `GeneratorExp` as top-level statements

### Root Cause Analysis

The `source` field in `CellVariableInfo` stores the **complete raw cell source** from nbformat. The markdown output at `_format_cell()` line 101-103 renders:

```python
lines.append("```python")
lines.append(cell_info.source)
lines.append("```")
```

This should output the **full cell source** without truncation. **The `cell.source` from nbformat is the authoritative source text.**

**However**, the `variables.py` statement extraction walks `tree.body` (top-level statements only). If a comprehension is the *sole* content of a cell, it would be an `ast.Expr` wrapping a `ListComp`/`DictComp`/`SetComp`. The `Expr` handler at line 158:

```python
elif isinstance(node, ast.Expr):
    stmt_type = "expr"
    references = _extract_name_refs(node.value)
```

This correctly identifies the comprehension as an expression and extracts references. But the **variable tracking annotation** might show nothing was defined (comprehensions don't assign unless wrapped in `x = [...]`).

**Actual truncation hypothesis:** If the issue is that comprehension *content* is truncated in the *per-statement annotations* (not the source code block), the problem would be in how the statement info is displayed — but `_format_cell()` only shows `defines` and `references` lists, not the source text of individual statements.

**Alternative hypothesis:** The issue might be that `cell.source` in nbformat sometimes contains newlines that aren't properly joined. nbformat v4 stores source as either a string or a list of strings. Let me verify:

```python
# nbformat v4 cell source can be either:
# cell.source = "x = [i*2 for i in items]\n"  (string)
# OR
# cell.source = ["x = [i*2 for i in items]\n"]  (list of strings)
```

If the source is stored as a list of strings and not properly joined, multi-line comprehensions could appear truncated. But `extract_cell_variables` passes `cell_source: str` to `ast.parse()`, and nbformat normally handles this transparently.

**Recommended fix strategy:** Create a test notebook with multi-line comprehensions first, run through `compact_notebook()`, and observe the actual output before fixing. The test should include:

```python
# Cell 1: list comprehension
result = [x * 2 for x in range(10) if x > 3]

# Cell 2: dict comprehension  
mapping = {k: v for k, v in zip(keys, values)}

# Cell 3: nested/multi-line comprehension
matrix = [
    [i * j for j in range(5)]
    for i in range(5)
]
```

### Test Impact
- `test_notebook.py` — Only 4 tests currently, none test comprehension cells. Need to add test cases.
- `test_variables.py` — Tests `extract_cell_variables` directly. May need a comprehension test case.

### Risk Assessment
**Low-medium risk.** Depends on whether truncation is in the source rendering (unlikely given nbformat's `cell.source` usage) or in the statement annotation display. The test-first approach is critical here.

---

## BUG-3: Stale Phase 3 placeholder in writer output (FIX-03)

### Current Behavior
- `writer.py:274` has hardcoded: `"*(File summary not yet generated — available after Phase 3.)*"`
- This string appears in ALL per-file markdown output from `glma index`
- The `generate_rule_summary()` function in `export.py` already produces correct summaries

### Desired Behavior
- Writer output shows the actual rule-based summary (same function as exports)
- Placeholder string removed entirely

### Root Cause Analysis
The placeholder was added in Phase 1 as a known gap, with the intent to fill it after the summary system was built. Phase 4 built `generate_rule_summary()` in `export.py`, but `writer.py` was never updated to use it.

### Fix Strategy

**Step 1: Move `generate_rule_summary()` to a shared module**

Per CONTEXT.md decision D-03, move from `export.py` to a shared location. Options:
- `glma/summaries.py` — New dedicated module (cleanest)
- `glma/index/summaries.py` — Inside index subpackage (writer is in index/)
- Keep in `export.py` and import from there (creates coupling writer → export)

**Recommended: `glma/summaries.py`** — A new top-level module. Both `export.py` and `writer.py` import from it. This avoids circular dependencies and keeps the function discoverable.

**Step 2: Update `writer.py:format_file_markdown()`**

Replace lines 273-274:
```python
# Before:
# File summary (placeholder for Phase 3 LLM generation)
lines.append("*(File summary not yet generated — available after Phase 3.)*")

# After:
from glma.summaries import generate_rule_summary
# ...
summary = generate_rule_summary(file_path, chunks, relationships or [])
lines.append(summary)
```

Note: `format_file_markdown()` currently takes `relationships: Optional[list[dict]] = None`. The summary function needs relationships, so pass `relationships or []`.

**Step 3: Update `export.py` to import from shared module**

```python
# Before:
# generate_rule_summary defined in export.py

# After:
from glma.summaries import generate_rule_summary
```

Keep the function in `export.py` as a re-export for backward compatibility, or just replace the import everywhere.

### Affected Code Paths

| File | Lines | Change |
| ---- | ----- | ------ |
| NEW: `glma/summaries.py` | — | `generate_rule_summary()` function (moved from export.py) |
| `export.py` | L18-62 | Remove function, add `from glma.summaries import generate_rule_summary` |
| `writer.py` | L273-274 | Replace placeholder with `generate_rule_summary()` call |
| `writer.py` | L1-10 | Add import of `generate_rule_summary` |

### Import Chain Impact
- `writer.py` imports from `glma.summaries` — new dependency, no circular risk
- `export.py` imports from `glma.summaries` — replaces internal definition
- No other files import `generate_rule_summary` from export.py (it was only used internally in `export_index()` and `_format_export_file()`)

Wait — let me verify:

```bash
grep -rn "generate_rule_summary" 02-worktrees/glma/src/glma/
```

Results: Only referenced in `export.py` itself (definition + internal calls) and `test_export.py` (test import). The test imports `from glma.export import generate_rule_summary` — this will still work if export.py re-exports it.

### Test Impact
- `test_writer.py` — No test currently checks the file summary content. Should add a test that verifies the summary is NOT the placeholder string.
- `test_export.py` — Tests import `generate_rule_summary` from `glma.export`. Will still work if export.py re-exports, but should ideally import from `glma.summaries`.
- `test_writer.py::TestFormatFileMarkdown` — The `test_file_heading` test just checks the heading, not the summary. No breakage.

### Risk Assessment
**Low risk.** The function already works and is tested. Moving it is a simple refactor. The writer just needs to call it with the right arguments.

---

## Cross-Cutting Concerns

### Test Suite Integrity
- **211 tests must remain passing** after all three fixes
- Most impacted tests are in `test_export.py` (1-2 tests), `test_writer.py` (no breakage, add new test), and `test_notebook.py` (add new test)
- FIX-01 changes a default value — exactly 1 test asserts on that default

### File Structure (all paths relative to `02-worktrees/glma/`)

```
src/glma/
├── summaries.py          # NEW: shared generate_rule_summary()
├── cli.py                # FIX-01: --no-code → --include-code
├── export.py             # FIX-03: import from summaries.py instead of local def
├── models.py             # FIX-01: include_code default True → False
├── index/
│   └── writer.py         # FIX-03: replace placeholder with generate_rule_summary()
├── query/
│   ├── notebook.py       # FIX-02: investigate, likely no code change needed here
│   └── variables.py      # FIX-02: investigate, may need comprehension handling
└── config.py             # No changes needed
```

### Dependency Analysis
- FIX-01 is **independent** — touches models.py and cli.py only
- FIX-03 depends on creating `summaries.py` first, then updating both export.py and writer.py
- FIX-02 is **independent** — touches notebook.py and/or variables.py only
- No interdependencies between fixes — they can be implemented in any order or in parallel

### Execution Order Recommendation
1. **FIX-03 first** — Creates the shared module, unblocks future summarization work (Phase 6)
2. **FIX-01 second** — Simple default change + CLI flag swap, one test update
3. **FIX-02 last** — Requires investigation-first approach (write test, observe, fix)

This order ensures the shared `summaries.py` module is in place before other phases need it.

---

## RESEARCH COMPLETE

Three bugs analyzed. FIX-01 and FIX-03 have clear, low-risk fixes. FIX-02 needs a test-first investigation to confirm the truncation root cause before planning the fix. All fixes are independent and can be parallelized across plans if desired.
