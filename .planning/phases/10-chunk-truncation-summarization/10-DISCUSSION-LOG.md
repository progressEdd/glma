# Phase 10: Chunk Truncation for Summarization - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-14
**Phase:** 10-chunk-truncation-summarization
**Areas discussed:** Truncation location, Token estimation, Config surface, Decomposition strategy

---

## Truncation Location

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Pipeline level (`summarize_chunks()`) | Truncate before calling provider. All providers protected. | |
| Provider level (each `.summarize()`) | Each provider truncates independently. More control but duplicated. | |
| Both | Pipeline as safety net, providers can refine. | |

**User's choice:** Evolved beyond simple truncation — see Decomposition Strategy below.

---

## Token Estimation

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Character-based (~4 chars/token) | Simple, no dependency, works across all models | |
| Actual tokenizer (tiktoken) | Accurate but OpenAI-specific, adds dependency | |
| Configurable | User sets the limit. Char-based default. | |

**User's choice:** Both — auto mode uses tiktoken when available, manual mode uses char-based fallback. Auto mode detects provider max context and calculates budget.

---

## Config Surface

| Option | Description | Selected |
| ------ | ----------- | -------- |
| `.glma.toml` only | `max_chunk_chars` in `[summarize]` section | |
| CLI flag only | `--max-chunk-chars` per-run override | |
| Both | Config + CLI flag with CLI overriding config | ✓ |

**User's choice:** Both `.glma.toml` and CLI flag. Auto context sizing on by default when tiktoken installed.

---

## Decomposition Strategy

This emerged from discussion about the root cause of ag2-framework failures.

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Pre-sort + always decompose classes | Process methods first, always build class summary from method summaries | |
| Simple truncation | Cut at N chars, summarize the first portion | |
| Try-first, decompose on failure | Send as-is, catch context error, then decompose | ✓ |

**User's choice:** Try-first, decompose on failure. For classes: summarize methods individually, then send class header + method summaries to LLM for class summary. For standalone oversized chunks: map-reduce with overlapping segments.

**Notes:** User wanted to try classes first without upfront decomposition. Only trigger the expensive strategy when the provider rejects the request. This keeps the happy path fast for the majority of chunks that fit fine.

### Key insight from user

The reason ag2's AgentBuilder breaks is that the class chunk (32,475 chars) includes all method bodies as redundant content — but those methods are already extracted as separate chunks with their own IDs. The class-level string variables (prompt templates like `GROUP_CHAT_DESCRIPTION`) are also bloating the chunk but aren't code logic. Rather than truncating, decompose: summarize the parts, then compose a class summary from the parts.

---

## Agent's Discretion

- Exact overlap size for map-reduce segments
- How to extract "class header" content from a class chunk
- Whether to strip class-level string variables (prompt templates) as noise
- How to combine map-reduce segment summaries
- Whether to retry with simpler prompt before decomposing

## Deferred Ideas

- Pre-emptive token counting to skip oversized chunks before API call (optimization)
- Stripping class-level string variables as non-code noise (separate concern)
- Configurable decomposition strategy per chunk type (over-engineering)
