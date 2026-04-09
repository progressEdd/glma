---
plan: 03-02
phase: 03-query-tool-notebook-compaction
status: complete
completed: 2026-04-09
---

# Plan 03-02: Jupyter Notebook Parsing, Variable Tracking, Notebook Compaction

## Result

Built Jupyter notebook compaction: parse .ipynb files, track per-statement variables, and generate compacted markdown with cross-cell variable flow.

## What was built

- **Variable extraction** (`glma/query/variables.py`): Per-statement AST analysis tracking `defines` and `references`. Handles all Python statement types (assign, function_def, class_def, import, for_loop, with_stmt, aug_assign, etc.)
- **Notebook compaction** (`glma/query/notebook.py`): nbformat-based .ipynb parser with per-cell code blocks, per-statement annotations, cross-cell variable origin tracking, and Variable Flow summary table
- **Graceful degradation**: Unparseable cells return empty statements instead of crashing

## Key files created/modified

- `src/glma/query/variables.py` — StatementInfo, CellVariableInfo dataclasses, extract_cell_variables(), build_variable_flow()
- `src/glma/query/notebook.py` — compact_notebook() with cell formatting, variable flow table, output handling
- `pyproject.toml` — added nbformat>=5.10 dependency
- `tests/test_variables.py` — 8 variable extraction tests
- `tests/test_notebook.py` — 4 notebook compaction tests

## Decisions

- Per-statement granularity (not per-cell) for better agent debugging
- Markdown cells rendered as blockquotes to preserve narrative context
- Cell outputs stripped by default (D-08)
- _extract_name_refs checks the node itself (not just children) for correct Name detection
- Function arg names included in references per plan spec

## Self-Check: PASSED
