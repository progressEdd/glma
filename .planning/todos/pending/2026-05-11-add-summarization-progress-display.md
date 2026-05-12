---
created: 2026-05-11T00:00:00Z
title: Add summarization progress display to CLI
area: cli
status: open
files:
  - src/glma/cli.py
  - src/glma/summarize/pipeline.py
---

## Problem

When running `glma index --summarize` on a large repo (648 files), the summarization pass shows no progress — just a long silence followed by context-length warnings. The user has no visibility into which chunks are being processed, how many are done, or how many remain.

By contrast, the indexing phase shows a nice progress bar:

```
Extracting relationships...
  Indexing: website/mkdocs/docs_src/__init__.py ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% (648/648 files) 0:00:00 0:00:00
✓ Indexing complete
```

## Solution

Add a Rich progress display to the summarization pass, similar to the indexing progress bar. Show:

1. **Overall progress**: `Summarizing: autogen/browser_utils.py::SimpleTextBrowser ━━━━ 142/5264 ━━━━ 0:01:23`
2. **Per-chunk status**: which chunk is currently being summarized (file, name, type)
3. **Counts**: summarized, decomposed, skipped, failed — updated in real-time

### Approach

- Add a `progress_callback` parameter to `summarize_chunks()` (same pattern as `embed_chunks()`)
- In `cli.py`, create a Rich `Progress` widget and pass the callback
- Update counts after each chunk (summarized / decomposed / skipped / failed)
- Show the current chunk name in the description (e.g., `from_dict (method, L189-L211, parent: ThinkNode)`)

### Example output

```
Summarizing chunks with local provider...
  Summarizing: autogen/agentchat/contrib/captainagent/agent_factory.py::AgentFactory ━━━━ 142/5264 ━━━━ 0:01:23

  Summarized:    128
  Decomposed:    8
  Skipped:       0
  Failed:        6
```

## Acceptance Criteria

- Summarization pass shows a live progress bar with chunk counts
- Current chunk name/type is displayed during processing
- Final counts are shown on completion (matching existing embed output style)
- `--quiet` flag suppresses the progress display
