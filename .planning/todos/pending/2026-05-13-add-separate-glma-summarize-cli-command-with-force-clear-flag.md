---
created: "2026-05-13T02:46:27.142Z"
title: Add separate glma summarize CLI command with force-clear flag
area: cli
files:
  - 02-worktrees/glma/src/glma/cli.py
  - 02-worktrees/glma/src/glma/summarize/pipeline.py
  - 02-worktrees/glma/src/glma/db/ladybug_store.py
---

## Problem

Currently `--summarize` is a flag on `glma index`. This means:
1. To re-summarize after changing the LLM model, you have to manually clear summaries via a Python script (`MATCH (c:Chunk) SET c.summary = NULL, c.summary_hash = NULL`) — not user-friendly.
2. Summarization is tightly coupled to indexing. If all files are unchanged, it still runs through the index logic before reaching summarization.
3. There's no `--force` or `--clear` flag to re-summarize chunks that already have summaries (e.g., after switching LLM models).
4. The `--summarize` flag on index doesn't support clearing existing summaries.

Users should be able to run `glma summarize` as a standalone command, similar to how `glma search` and `glma embed` are separate commands.

## Solution

Create a new `glma summarize` CLI command that:
- Runs the summarization pass on an already-indexed repo
- Accepts a `--force` flag to clear all existing summaries and re-summarize from scratch
- Accepts `--summarize-provider`, `--summarize-model`, `--ai-url` overrides (same as current index flags)
- Works with the existing `LadybugStore.get_indexed_files()` and `summarize_chunks()` infrastructure
- Can be run independently without re-running the full index pipeline

The `--summarize` flag on `glma index` remains for convenience (index + summarize in one pass).

Also add a `--force` flag to `glma index --summarize` that clears existing summaries before summarizing.

Example usage:
```
glma summarize --force                          # re-summarize everything
glma summarize --summarize-model llama3         # use different model
glma index . --summarize --force                # index + force re-summarize
```
