# Phase 7: CLI Integration & Providers - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in 07-CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-10
**Phase:** 7-cli-integration-providers
**Areas discussed:** Provider config & CLI flags, Pi provider, Summaries in output paths, Optional dependency handling

---

## Provider Config & CLI Flags

| Option | Description | Selected |
| ------ | ----------- | -------- |
| A: Unified [summarize] config, both commands use it | Single `[summarize]` section; `index --summarize` and `export --ai-summaries` both pull from it; export's `--ai-url` becomes alias |   |
| B: Separate configs | New `[summarize]` for index-time only; export keeps own `ai_*` fields |   |
| C: Unified config, export reuses index summaries | One `[summarize]` config; export reads from DB instead of generating on-the-fly | ✓ |

**User's choice:** A/C hybrid — unified `[summarize]` config, export reads from DB. Motivated by wanting a consistent model across summaries, future query rewriting, and future vector/hybrid search. Export becomes "read from DB" not "generate now."

**Notes:** One model for everything — chunk summaries now, future query rewriting and embedding later. Same provider that wrote summaries will be used for query rephrasing in semantic search.

---

## Pi Provider Implementation

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Subprocess call to pi's CLI | Spawn pi with a prompt, capture stdout |   |
| Pi's API/library (SDK) | Import pi's SDK directly, call programmatically | ✓ |
| HTTP endpoint | Call pi's local HTTP API like OpenAI-compatible |   |

**User's choice:** Option 1/2 hybrid — it's primarily a pi extension. Uses pi's SDK when running inside pi. The pi provider is an ecosystem integration: "glma works standalone with local LLMs, works even better inside pi."

**Notes:** Optional — glma works fine without pi. The extension registers pi as a SummarizerProvider backend. No separate pip extras group for pi.

---

## Summaries in Output Paths

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Summary above code block (with code) | Italic blockquote: `> *Summary: ...*` | ✓ |
| Summary in heading section (summaries-only) | Appears where "Code omitted" / signature line is | ✓ |
| Same pattern across all three formats | export, query, writer all render the same way | ✓ |

**User's choice:** Both rendering modes, depending on output mode. DB `summary` field is source of truth. With code: summary above code block. Summaries-only: summary in heading section. Same pattern in export, query, and writer.

**Notes:** User clarified that the DB field is separate (already exists from Phase 6), and markdown rendering varies by output mode.

---

## Optional Dependency Handling

| Option | Description | Selected |
| ------ | ----------- | -------- |
| `[ai]` group = openai only, clear error if missing | `"Install with: pip install glma[ai]"` + exit 1 | ✓ |
| `[pi]` separate extras group | Extra pip install for pi provider | ✗ (rejected) |
| Graceful degradation (skip silently) | Don't error, just skip summarization | ✗ (not discussed) |

**User's choice:** `[ai]` = `openai` package only. Clear error + install hint + exit 1 when used without it. No `[pi]` group — pi extension handles its own deps.

**Notes:** Follows existing ImportError pattern in `export.py`.

---

## Agent's Discretion

- Exact prompt template for chunk summarization
- Exact `[summarize]` config field names and defaults
- How to handle deprecated export flags (`--ai-summaries`, `--ai-url`, `--ai-model`)
- Error retry logic for individual chunk failures
- Progress display during summarization pass

## Deferred Ideas

None — all discussion stayed within Phase 7 scope.
