---
created: 2026-04-10T00:00:00Z
title: Default markdown export to summaries only
area: api
files:
  - 02-worktrees/glma/src/glma/models.py:102
  - 02-worktrees/glma/src/glma/export.py:196
  - 02-worktrees/glma/src/glma/cli.py:317
---

## Problem

The markdown export (`ExportConfig.include_code`) defaults to `True` in models.py:102. This means exported markdown files include full source code in every chunk by default. For air-gapped exports meant to give agents a quick overview, this bloats the output significantly. The current CLI only sets `include_code = False` via a `--no-code` flag (cli.py:317), but the default should be summaries-only, with code included only when explicitly requested via a `--include-code` flag.

## Solution

1. Flip `ExportConfig.include_code` default from `True` to `False` in models.py:102
2. Invert the CLI flag logic: change `--no-code` to `--include-code` (or add `--include-code` as opt-in) in cli.py:317
3. Update any tests that assume code is included by default
