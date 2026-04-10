---
status: resolved
trigger: "glma query notebook.ipynb --summary-only still shows full code"
created: 2026-04-10T23:20:00.000Z
updated: 2026-04-10T23:22:00.000Z
---

## Current Focus

hypothesis: Notebook dispatch in cli.py ignores summary_only flag
test: Run glma query with --summary-only on a notebook
expecting: Code cells show only first line + line count, not full source
next_action: N/A — fixed and verified

## Symptoms

expected: `glma query develop.ipynb --summary-only` produces compact output without source code
actual: Full source code included in every cell despite --summary-only flag
errors: None — flag silently ignored
reproduction: `glma query ../linux_kernel/develop.ipynb --repo ../linux_kernel --summary-only`
started: Always broken — notebook code path never supported the flag

## Eliminated

- hypothesis: The formatter's format_compact_output() should handle notebooks
  evidence: Notebooks have their own code path (compact_notebook) that bypasses the formatter entirely. The issue is upstream in the dispatch.
  timestamp: 2026-04-10T23:20:30Z

## Evidence

- timestamp: 2026-04-10T23:20:00Z
  checked: cli.py notebook dispatch (line ~213)
  found: `compact_notebook(disk_path, include_outputs=include_outputs)` — no summary_only parameter passed
  implication: Need to add include_code param to compact_notebook

- timestamp: 2026-04-10T23:21:00Z
  checked: compact_notebook() signature in notebook.py
  found: Only accepts `filepath` and `include_outputs`. No code visibility control.
  implication: Add `include_code` parameter, thread through to _format_cell

## Resolution

root_cause: Notebook query path was implemented as a standalone feature (Phase 3) before --summary-only existed (added in Phase 4 for regular files). The two were never connected.

fix: (1) Added `include_code: bool = True` parameter to `compact_notebook()` and `_format_cell()`. (2) When `include_code=False`, code cells show `*N lines* — \`first line...\`` instead of full source. (3) Wired `--summary-only` → `include_code=not summary_only` in cli.py notebook dispatch.

verification: `glma query develop.ipynb --summary-only` produces 774 lines (vs 1802 with code). Each code cell shows line count and first line preview. Variable flow annotations preserved. 255/255 tests pass.

files_changed:
  - 02-worktrees/glma/src/glma/query/notebook.py
  - 02-worktrees/glma/src/glma/cli.py
