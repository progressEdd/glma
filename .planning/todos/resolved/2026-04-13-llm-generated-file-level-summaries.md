---
created: 2026-04-13T00:00:00Z
title: LLM-generated file-level summaries in export
area: api
status: resolved
files:
  - src/glma/models.py
  - src/glma/db/ladybug_store.py
  - src/glma/cli.py
  - src/glma/export.py
  - src/glma/index/writer.py
  - tests/integration/test_full_index.py
---

## Problem

The per-file Summary section in exports used a rule-based summary (e.g., `"8 function(s): version_callback, main, index,..."`) which described the file structure but not what it actually does. INDEX.md had the same issue when no AI summaries were available.

## Solution

Added LLM-generated file-level summaries:

1. **New `file_summary` field** on `FileRecord` model and in the LadybugStore DB schema
2. **`update_file_summary()`** method on LadybugStore for targeted field updates
3. **File-level summarization pass** in `cli.py` — after per-chunk summaries are generated, a second pass sends all chunk summaries to the LLM and asks for a 1-2 sentence file summary
4. **Export uses `file_summary`** — both INDEX.md and per-file exports show the LLM-generated file summary as the primary Summary, falling back to rule-based when no LLM summary exists

### Before (rule-based)
```
## Summary
8 function(s): version_callback, main, index, _write_output, _group_rels_by_chunk, query, watch, export. Imports: asyncio, glma, glma.config, ...
```

### After (LLM-generated)
```
## Summary
Provides a command-line interface for indexing repositories into a database, managing AI-driven summarization, and exporting documentation as static Markdown. It supports repository monitoring for incremental updates and allows users to query indexed file relationships via JSON or Markdown outputs.
```

### Also fixed
- Pre-existing broken `test_docstrings_in_markdown` integration test (docstrings in `attached_comments` aren't stored in DB, so they don't survive the write_markdown path)

## Resolved

2026-04-13 — Commit `4c71474`, 274/274 tests passing. Ran `glma index --summarize` with Gemma 4 31B on glma itself — all 28 files got both chunk and file-level summaries.
