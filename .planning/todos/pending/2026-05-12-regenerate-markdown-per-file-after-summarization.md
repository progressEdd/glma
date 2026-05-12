---
created: 2026-05-12T00:00:00Z
title: Regenerate markdown per-file after summarization instead of batching at end
area: cli
status: open
files:
  - src/glma/cli.py
---

## Problem

When running `glma index --summarize`, the markdown rewrite for all files happens in a single batch at the very end of the run (after both chunk summarization AND file-level summary generation). If the process is interrupted or canceled before that final loop, no markdown files get updated — even though chunk summaries were already persisted to the DB.

This means interrupted runs leave stale markdown with no summaries, making it appear as if summarization never ran.

## Solution

Move the markdown regeneration into the per-file summarization loop so each file's markdown is updated immediately after its chunks are summarized — before moving on to the next file.

### Current flow in `cli.py`

```
for file in indexed_files:
    summarize_chunks(...)          # chunk summaries → DB
    generate file-level summary    # file summary → DB
# AFTER ALL FILES:
for file in indexed_files:         # ← only reached if not interrupted
    write_markdown(...)            # DB summaries → markdown
```

### Proposed flow

```
for file in indexed_files:
    summarize_chunks(...)          # chunk summaries → DB
    generate file-level summary    # file summary → DB
    write_markdown(...)            # ← regenerate markdown immediately
```

This way, an interrupt only loses markdown for files not yet processed, not for all files.

## Acceptance Criteria

- Markdown is regenerated per-file immediately after its summarization completes
- Interrupting the run preserves markdown for all already-summarized files
- No change to the DB persistence behavior (summaries are still saved incrementally)
- Final summary counts still displayed at the end
