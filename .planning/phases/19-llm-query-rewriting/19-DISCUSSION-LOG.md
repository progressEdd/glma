# Phase 19: LLM Query Rewriting - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-05-12
**Phase:** 19-llm-query-rewriting
**Areas discussed:** Rewrite Prompt Design, Output Transparency, Rewrite Failure Handling, CLI Flag Integration

---

## Rewrite Prompt Design

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Code-aware expansion | Single rewritten string, expands abbreviations, adds likely terms, preserves intent | ✓ |
| Multi-strategy rewrite | Produce 2-3 variants, run search against all, merge results | |
| Structured query output | LLM returns JSON with expanded_terms, likely_symbols, original_intent | |

**User's choice:** Code-aware expansion. Also requested that the prompt be aware of chunk summary style — how summaries are formed (1-2 concise sentences about purpose, inputs, outputs, behavior) — so the rewrite targets that same natural language pattern.

**Notes:** User specifically said to "look for the prompt for code summaries" — the summarization SYSTEM_PROMPT in `src/glma/summarize/providers.py` is the canonical reference for summary style.

---

## Output Transparency

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Header above results | Always-visible header showing original + rewritten query before result list | ✓ |
| Stderr header only | Show on stderr, keep stdout clean for piping | |
| Only in verbose/JSON mode | Markdown stays lean, JSON/YAML get machine-readable fields | |

**User's choice:** Header above results — always visible in all output formats.

**Notes:** JSON/YAML also get `original_query` and `rewritten_query` fields for machine readability. `--raw` shows only original query with "raw query" label.

---

## Rewrite Failure Handling

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Fall back to raw with warning | Stderr warning, proceed with original query | ✓ |
| Error out entirely | Whole command fails, forces --raw or fix | |
| Silent fallback | Use raw query with no indication | |

**User's choice:** Fall back to raw query with stderr warning.

**Notes:** User explicitly stated "same model/endpoint as the summarizer model" — reuse `[summarize]` config and `--summarize-provider`/`--summarize-model`/`--ai-url` flags.

---

## CLI Flag Integration

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Reuse summarizer flags | Same --summarize-provider/model/ai-url, only --raw is new | ✓ |
| Dedicated rewrite flags | New --rewrite-provider/model flags | |
| Search-section config | Add rewrite_provider/model to [search], defaulting to [summarize] | |

**User's choice:** Reuse summarizer flags. `--raw` is the only new CLI flag.

**Notes:** User clarified that `--raw` simply skips the rewriter entirely — no LLM call, query goes straight to hybrid search as-is. `rewrite_prompt` field added to `[search]` config for custom prompt overrides.

---

## Agent's Discretion

- Exact wording of the default rewrite prompt (constrained by summary-style targeting)
- Module structure for rewrite code (new file or extend existing)
- Provider instantiation strategy (new instance vs shared)
- Header formatting details
- LLM call parameters (max_tokens, timeout)

## Deferred Ideas

None - discussion stayed within phase scope.
