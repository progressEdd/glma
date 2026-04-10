---
created: 2026-04-10T00:00:00Z
title: Pi/agent integration for code summarization
area: api
files:
  - 02-worktrees/glma/src/glma/export.py:68
  - 02-worktrees/glma/src/glma/cli.py:276
  - 02-worktrees/glma/src/glma/models.py:106
---

## Problem

Currently AI summarization requires a running local LLM (LM Studio, Ollama, etc.) with an OpenAI-compatible endpoint. This means:
- User must have a separate model server running
- No fallback when no local LLM is available
- Can't leverage the coding agent (pi) that's already running and already has model access

Pi (or any coding agent) already has an LLM connection and understands code context. It could generate summaries during or after indexing without requiring a separate model server.

## Solution

**Preferred: pi extension with `glma_summarize` tool**

1. Create a pi extension (~/.pi/agent/extensions/glma-summarize.ts) that registers a tool:
   - Tool reads chunks needing summaries from glma DB (via `glma` CLI or direct DB access)
   - Agent loops: tool returns batch of chunks → agent summarizes each → tool writes summaries back
   - State tracked via `pi.appendEntry()` for crash recovery / resume
2. No separate LLM server needed — uses whatever model pi is already connected to
3. Fallback chain: pi extension (if running) → local LLM (--ai-summaries, existing) → rule-based (default)
4. Would also solve the per-chunk summary problem (related todo) since the agent can batch-summarize efficiently

**Alternative: SDK headless session**
- Use `createAgentSession()` with `SessionManager.inMemory()` to spin up a background session
- Pipe chunk data in, collect summary text from streaming events
- Works from any Node.js process, no TUI needed
- Could be triggered from glma CLI as `glma export --summarize-via agent`
