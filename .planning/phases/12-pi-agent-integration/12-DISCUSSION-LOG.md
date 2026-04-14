# Phase 12: Pi Agent Integration - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-14
**Phase:** 12-pi-agent-integration
**Areas discussed:** Extension architecture, model_hint resolution, provider presets, fallback chain behavior, extension location

---

## Extension Architecture

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| A: Direct model call (command) | Extension calls `complete()` directly, loops over chunks, writes to DB | |
| B: Agent loop (tool) | `glma_summarize` tool returns batches, agent summarizes, tool writes back | |
| C: Hybrid | Command does batch processing, tool is thin trigger | ✓ |

**User's choice:** Option C (hybrid) — command handles real batch summarization with a cheap model, tool gives agent a way to request it without leaving the conversation.

### Follow-up: How does the command write summaries back?

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| 1: Shell out to glma CLI | Reuses entire Python pipeline via subprocess | ✓ |
| 2: Direct DB writes from extension | Extension reads/writes Ladybug DB directly | |
| 3: Python helper script | Small script shipped with glma, middle ground | |

**User's choice:** Option 1 (shell out to glma CLI) — no duplicated logic, reuses decomposition, incremental summarization, error handling.

### Follow-up: API key routing for cloud vs local models

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| 1: Extension bridges the call | Cloud models via `complete()`, local models via CLI subprocess | ✓ |
| 2: Always shell out, pass credentials via env | Only works for OpenAI-compatible endpoints | |

**User's choice:** Option 1 — two code paths. Cloud models (Claude, GPT, Gemini) use `complete()` with pi's auth. Local models shell out to `glma index --summarize`.

---

## model_hint Resolution

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| 1: Cost-based sorting | `fast` = cheapest, `capable` = most expensive | |
| 2: Hardcoded preference order | Known families ranked, fallback to cost | ✓ |
| 3: User-configured aliases | Explicit mapping in `.glma.toml` | |

**User's choice:** Option 2 with insight that pi already owns model management — no need for glma-side aliases. `model_hint` resolves against pi's registry only. Empty hint = pi's active model.

**Notes:** User pointed out that pi already provides model selection infrastructure (`models.json`, `/model`, `ctx.modelRegistry`). The hint resolution should leverage pi's existing registry, not duplicate model config in glma.

---

## Provider Presets for Standalone

### Flag naming

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| 1: New `--ai-provider` flag | Separate from `--summarize-provider` | |
| 2: Extend `--summarize-provider` | Accept preset names (ollama, lmstudio, etc.) | ✓ |

**User's choice:** Option 2 — `--summarize-provider` accepts both backend types (`local`, `pi`) and preset names (`ollama`, `lmstudio`, `llamacpp`, `vllm`, `aphrodite`). Fewer flags to remember.

### Which presets to ship

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| 1: All 5 from todo | lmstudio, ollama, llamacpp, vllm, aphrodite | |
| 2: Top 3 | lmstudio, ollama, llamacpp | |
| 3: All 5 + extensible | Ship all 5, plus `.glma.toml` custom presets | ✓ |

**User's choice:** Option 3 — all 5 built-in presets plus `[summarize.providers]` config section for custom/overridden presets.

---

## Fallback Chain Behavior

| Option | Description | Selected |
| ---------- | ---------------------------------- | -------- |
| 1: Explicit only | No auto-detection, user picks provider | |
| 2: Auto-detect + explicit override | Detect pi environment, user can override, clear errors | ✓ |
| 3: Full cascade | Try pi → local → rule-based silently | |

**User's choice:** Option 2 — auto-detect pi environment for convenience, explicit override available, no silent cascading (fail clearly).

---

## Extension Location

| Question | Answer |
| ---------- | ------- |
| Where does the extension live? | `.pi/extensions/` in the glma repo (pi auto-discovery) |
| Command namespace? | `/glma` — currently `/glma-summarize`, extensible for future commands |
| File structure? | Start as single file (`.pi/extensions/glma-summarize.ts`), migrate to subdirectory if it grows |

**Notes:** User asked about adding pi agent commands (specifically `/glma`). Decided to ship the extension at `.pi/extensions/` so it's auto-discovered by pi. Commands registered under `/glma` namespace for future extensibility.

---

## Agent's Discretion

- Exact model family preference list for fast/capable heuristics
- How to read from glma's Ladybug DB from the extension
- Whether to keep or remove Python PiProvider stub
- Extension file structure (single file vs subdirectory)
- Progress display during batch summarization
- How the extension discovers the glma DB path
- Test strategy for the TypeScript extension

## Deferred Ideas

- Full `/glma` command suite (`/glma-index`, `/glma-query`, `/glma-export`) — out of scope, extension structure supports adding later
- SDK headless session for background summarization — alternative approach, deferred
- Streaming progress in pi's TUI — nice-to-have, not essential
