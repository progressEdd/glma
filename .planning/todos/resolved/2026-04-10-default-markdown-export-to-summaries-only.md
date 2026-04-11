---
created: 2026-04-10T00:00:00Z
title: Default markdown export to summaries only
area: api
status: done
files:
  - 02-worktrees/glma/src/glma/models.py:102
  - 02-worktrees/glma/src/glma/export.py:196
  - 02-worktrees/glma/src/glma/cli.py:317
  - 02-worktrees/glma/src/glma/query/notebook.py
---

## Problem

The markdown export (`ExportConfig.include_code`) defaults to `True` in models.py:102. This means exported markdown files include full source code in every chunk by default. For air-gapped exports meant to give agents a quick overview, this bloats the output significantly. The current CLI only sets `include_code = False` via a `--no-code` flag (cli.py:317), but the default should be summaries-only, with code included only when explicitly requested via a `--include-code` flag.

Similarly, `compact_notebook()` in `query/notebook.py` defaulted `include_code=True`, causing `develop-compacted.md` to dump full source instead of compact summaries.

## Solution

1. Flip `ExportConfig.include_code` default from `True` to `False` in models.py:102
2. Invert the CLI flag logic: change `--no-code` to `--include-code` (or add `--include-code` as opt-in) in cli.py:317
3. Update any tests that assume code is included by default

## Done (2026-04-10)

- Flipped `compact_notebook()` default from `include_code=True` to `include_code=False` in `query/notebook.py`
- Added `--include-code` flag to CLI `query` command (opt-in, default off)
- Updated `test_comprehension_source_preserved` to pass `include_code=True`
- Added `test_code_hidden_by_default` and `test_code_shown_when_requested` tests
- 257 tests passing

**Note:** The `ExportConfig.include_code` default for `glma export` was already fixed in a prior session. This update covers the notebook query path specifically.
