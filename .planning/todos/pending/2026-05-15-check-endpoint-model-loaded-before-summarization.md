---
created: "2026-05-15T04:50:06.000Z"
title: Check endpoint model loaded before summarization
area: cli
files:
  - 02-worktrees/glma/src/glma/summarize/providers.py
  - 02-worktrees/glma/src/glma/summarize/pipeline.py
  - 02-worktrees/glma/src/glma/cli.py
---

## Problem

When running `glma index --summarize`, if the configured model isn't loaded at the local endpoint (e.g., LM Studio at `localhost:1234`), the summarization pipeline crashes with an OpenAI API error after already starting the indexing pass. On large codebases (Linux kernel 72K+ chunks), this wastes significant time — the user discovers the model isn't running only when the first chunk hits the summarizer.

There's currently no pre-flight check in `LocalProvider.__init__()` or `summarize_chunks()` that verifies the model is reachable and loaded before committing to the full pipeline.

## Solution

Add a pre-flight health check before summarization begins:

1. **Probe `/v1/models`** endpoint to see if the configured model is available
2. **If model not loaded**: warn the user and either (a) exit gracefully with a clear message, or (b) attempt to load the model via the provider's API if supported (e.g., LM Studio supports loading models via REST)
3. **If endpoint unreachable**: fail fast with a clear "is LM Studio running?" message instead of an opaque OpenAI exception

Implementation likely goes in `LocalProvider` as a `check_model_ready()` method, called from `cli.py` before entering the summarization loop. The existing `LocalProvider.__init__()` already creates the OpenAI client with the configured `base_url` and `model`.
