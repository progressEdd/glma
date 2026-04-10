---
created: 2026-04-10T00:00:00Z
title: Fix notebook cell source truncation in compaction
area: api
files:
  - 02-worktrees/glma/src/glma/query/notebook.py:1
  - 02-worktrees/glma/src/glma/query/variables.py
---

## Problem

When compacting notebooks via `compact_notebook()`, some code cells have their source truncated or incorrectly rendered. Observed example: Cell 7 in a "develop" notebook had actual source:

```python
files = [file.name for file in Path(supporting_files).iterdir()]
files
```

But the compacted markdown output rendered it as:

```python
files = 
files
```

The list comprehension `[file.name for file in Path(supporting_files).iterdir()]` was completely dropped. This suggests a bug in how `cell_info.source` is populated — possibly the variable extraction (`extract_cell_variables`) or source reconstruction is stripping or truncating multi-line expressions that span assignments.

## Solution

1. Investigate `extract_cell_variables()` in `glma/query/variables.py` — check if AST processing modifies or reconstructs source incorrectly
2. Verify that `cell_info.source` in `_format_cell()` uses the original `cell.source` from nbformat, not a reconstructed version
3. Add a test case with a cell containing `var = [list comprehension]\nvar` to catch this regression
4. The fix likely ensures `_format_cell()` uses the raw `cell.source` string directly rather than any AST-derived source
