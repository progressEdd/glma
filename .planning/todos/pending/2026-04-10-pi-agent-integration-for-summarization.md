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

1. Add an agent-based summarization backend alongside the existing OpenAI-compatible one
2. Could work as:
   - A pi extension/skill that hooks into the glma export pipeline
   - A `--summarize-via agent` CLI flag that delegates to whatever agent is running
   - Or a simple stdin/stdout protocol where glma pipes chunk data out and the agent pipes summaries back
3. Fallback chain: agent (if available) → local LLM (if running) → rule-based summaries (current default)
4. Would also solve the per-chunk summary problem (related todo) since the agent can batch-summarize efficiently
