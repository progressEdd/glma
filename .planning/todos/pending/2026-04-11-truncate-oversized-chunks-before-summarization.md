---
created: 2026-04-11T00:00:00Z
title: Truncate oversized chunks before sending to summarization provider
area: api
status: open
files:
  - src/glma/summarize/pipeline.py
  - src/glma/summarize/providers.py
---

## Problem

When running `glma index --summarize` against the ag2-framework repo (648 files, 5,264 chunks) with `gemma-4-31b-it` via LM Studio (4096 context window), large chunks exceed the model's context length and fail with:

```
Summarization failed for chunk autogen/agentchat/contrib/captainagent/agent_builder.py::class::AgentBuilder::53:
  Error code: 400 - {'error': 'The number of tokens to keep from the initial prompt is greater
  than the context length (n_keep: 8312>= n_ctx: 4096). Try to load the model with a larger
  context length, or provide a shorter input.'}
```

3 out of 363 summarized chunks failed for this reason. The remaining ~4,900 chunks weren't attempted before timeout, but many more would likely hit the same limit.

## Root Cause

Tree-sitter chunking produces some very large chunks (e.g., `AgentBuilder` is ~400 lines). When combined with the system prompt and context metadata, the total token count exceeds the model's context window.

## Solution

Add chunk truncation in `summarize_chunks()` or in `OpenAICompatibleProvider.summarize()` before sending to the API:

1. **Character-based truncation**: If chunk source exceeds N characters (e.g., 3000 chars ≈ 750 tokens), truncate and append `... (truncated from {original_len} chars)`.
2. **Or token estimation**: Rough estimate at ~4 chars/token. Truncate at `max_context_tokens - buffer` where buffer accounts for system prompt + context metadata (~200 tokens).
3. **Log a warning** when truncation occurs so the user knows the summary covers only a portion of the chunk.

### Alternative approach
- Make truncation threshold configurable via `.glma.toml` `[summarize]` section
- Default to a safe value that works with 4K context models

## Acceptance Criteria

- Chunks exceeding context limits are truncated, not failed
- Truncated chunks still receive a summary (covering their first N tokens)
- A warning is logged when truncation occurs
- The full summarization run completes without 400 errors

## Evidence

Encountered during Phase 9 execution testing against ag2-framework:
```
Summarization failed for chunk autogen/agentchat/contrib/captainagent/agent_builder.py::class::AgentBuilder::53
Summarization failed for chunk autogen/agentchat/contrib/gpt_assistant_agent.py::class::GPTAssistantAgent::24
```
Both are large class chunks (400+ lines) that exceed 4096 tokens.
