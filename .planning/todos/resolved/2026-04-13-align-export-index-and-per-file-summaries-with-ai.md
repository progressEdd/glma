---
created: 2026-04-13T00:00:00Z
title: Align export INDEX.md and per-file summaries with AI summaries
area: api
status: resolved
files:
  - src/glma/export.py
  - tests/test_export.py
---

## Problem

Two consistency issues with AI summaries in `glma export`:

1. **INDEX.md used AI summaries, per-file exports didn't** — INDEX.md showed LLM-generated text (joined chunk summaries) while per-file `.md` files still showed the old rule-based `"8 function(s): version_callback, main,..."` summary. Clicking through from INDEX.md to a file showed a different summary.

2. **Per-file exports had a separate "AI Chunk Summaries" subsection** — When `--ai-summaries` was enabled, the file showed the rule-based summary first, then repeated all AI chunk summaries below under `**AI Chunk Summaries:**`. Redundant and inconsistent.

## Solution

Unified both INDEX.md and per-file exports to use the same AI summaries from the DB:

- **`export_index()`** — composes file-level summary by joining per-chunk AI summaries (falls back to `generate_rule_summary()` when no AI summaries exist)
- **`_format_export_file()`** — now accepts `file_summary` param; Summary section lists each chunk's AI summary as bullet points directly, with no separate subsection
- **INDEX.md** — truncated view of the same joined AI summaries in the table

### Before
```
## Summary
8 function(s): version_callback, main, index, _write_output,...

**AI Chunk Summaries:**
- **version_callback**: Prints the current application version...
```

### After
```
## Summary
- **version_callback**: Prints the current application version...
- **main**: Defines the CLI entry point using Typer...
```

## Resolved

2026-04-13 — Commit `0fca96d` (INDEX.md uses AI summaries), `1b50260` (reverted per-file export, INDEX.md reads AI summaries directly from DB chunks). INDEX.md now shows full joined AI summaries (no truncation). Per-file exports keep rule-based summary + AI Chunk Summaries section. Both use the same AI data from the DB. 64/64 tests passing.
