---
created: 2026-04-13T00:00:00Z
title: Exclude code from static markdown output, regenerate after summarization
area: api
status: resolved
files:
  - src/glma/index/writer.py
  - src/glma/cli.py
  - tests/test_writer.py
---

## Problem

Two issues with the static markdown files in `.glma-index/markdown/`:

1. **Code bloat** — Full source code was included in every chunk's markdown output. For AI-summarized files this is redundant — the summary already captures what the code does.

2. **Stale markdown after summarization** — The `index --summarize` pass wrote AI summaries to the DB but never regenerated the static markdown files. Since all files were "unchanged" (same content hash), the pipeline skipped markdown regeneration. Summaries appeared in `glma query` (reads from DB) but not in the exported `.md` files.

## Solution

### 1. Code excluded from static markdown by default

Added `include_code` parameter to `format_file_markdown()` and `write_markdown()`:
- **Default `False`** — static markdown shows summaries, signatures, relationships, and first-line hints (for chunks without summaries/comments)
- **`True`** — includes full code blocks (used by tests, available for export command)

When code is excluded and a chunk has no summary or comments, a truncated first-line hint is shown:
```
`def another_function():`
```

### 2. Markdown regenerated after summarization

After the `summarize_chunks()` loop in `cli.py`, the CLI now iterates all indexed files and calls `write_markdown()` with fresh chunks (including AI summaries from the DB) and their relationships.

### Changes

- `writer.py`: added `include_code` param to `format_file_markdown()` and `write_markdown()`, default `False`
- `cli.py`: added post-summarization markdown regeneration loop
- `test_writer.py`: updated `test_python_code_block_hint` and `test_c_code_block_hint` to use `include_code=True`, added `test_code_excluded_by_default`

## Resolved

2026-04-13 — Commit `6eeeaf2`, 72/72 tests passing. Ran `glma index --summarize` on glma itself with Gemma 4 31B via LM Studio — all 28 files indexed, AI summaries generated, static markdown regenerated without code blocks.

2026-04-13 — Commit `0fca96d`, export INDEX.md now uses AI chunk summaries from DB instead of rule-based "N function(s): ..." summaries.
