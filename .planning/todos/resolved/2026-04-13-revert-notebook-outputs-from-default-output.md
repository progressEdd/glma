---
created: 2026-04-13T00:00:00Z
title: Revert notebook cell outputs from default compaction output
area: api
status: resolved
files:
  - src/glma/query/notebook.py
  - src/glma/cli.py
  - tests/test_notebook.py
---

## Problem

After adding cell outputs to the default notebook compaction output (commit `fef0ed4`), the rendered markdown became cluttered. The outputs are valuable for LLM summarization context but not needed in the final human-readable output by default.

## Solution

Reverted the default: `include_outputs` now defaults to `False` in both `compact_notebook()` and the `--include-outputs` CLI flag. Outputs are still:

1. **Passed to the LLM** during summarization via `_format_outputs_for_context()` → `# Output:` block appended to source
2. **Cached** with output-aware hashing (`_cell_content_hash_with_outputs`)
3. **Available on request** via `--include-outputs` CLI flag

### Changes

- `notebook.py`: `include_outputs` default `True` → `False`, docstring updated
- `cli.py`: `--include-outputs` default `True` → `False`, help text updated
- `test_notebook.py`: renamed `test_outputs_included_by_default` → `test_outputs_excluded_by_default`, flipped assertion

## Resolved

2026-04-13 — Commit `56cd9cd`, 21/21 notebook tests passing.
