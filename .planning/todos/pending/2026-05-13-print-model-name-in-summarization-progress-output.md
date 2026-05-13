---
created: "2026-05-13T03:10:00.000Z"
title: Print model name in summarization progress output
area: cli
files:
  - 02-worktrees/glma/src/glma/cli.py
  - 02-worktrees/glma/src/glma/index/progress.py
---

## Problem

When running `glma index --summarize`, the output shows "Summarizing chunks with local provider..." but doesn't indicate which model is being used. When switching between models (e.g., `unsloth/gemma-4-26b-a4b-it` vs `unsloth/gemma-4-E4B-it-GGUF`), there's no way to confirm from the terminal output which model actually ran. This is especially confusing during re-summarization passes on large codebases like the Linux kernel (72K+ chunks).

## Solution

Print the model name after "Summarizing chunks with local provider..." line, e.g.:

```
Summarizing chunks with local provider (unsloth/gemma-4-E4B-it-GGUF)...
```

The model name is already loaded in `SummarizeConfig.model` and available in the `index` command function in `cli.py`. Just append it to the Rich console output that precedes the summarization loop.
