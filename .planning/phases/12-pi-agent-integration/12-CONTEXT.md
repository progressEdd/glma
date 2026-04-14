# Phase 12: Pi Agent Integration - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary

A pi extension that lets pi generate glma chunk summaries using pi's model registry — no separate LLM server needed. Includes named provider presets for standalone mode (Ollama, LM Studio, etc.) and model_hint resolution (fast/capable/exact ID). The extension lives in the project at `.pi/extensions/` and registers `/glma` commands. No new chunking logic, no schema changes, no export format changes. Purely integrating glma's existing summarization pipeline with pi's model and extension infrastructure.

</domain>

<decisions>
## Implementation Decisions

### Pi Extension Architecture
- **D-01:** Hybrid command + tool approach. `/glma-summarize` command does the batch summarization (resolves model, loops over chunks, writes summaries to DB). `glma_summarize` tool is a thin trigger that queues the command as a follow-up message — lets the agent request summarization without leaving the conversation.
- **D-02:** Two code paths for model invocation based on model type:
  - **Cloud models (Claude, GPT, Gemini):** Extension reads chunks from glma DB → calls `complete()` with resolved model and API key from pi's registry → writes summaries back to DB directly.
  - **Local models (Ollama, LM Studio):** Extension resolves model hint to a base_url → shells out to `glma index --summarize` with provider flags → reuses the entire Python pipeline (decomposition, incremental summarization, error logging, DB writes).
- **D-03:** The existing `PiProvider` class in `providers.py` (Python, uses `from pi import Agent`) is a stub that doesn't match pi's actual extension API. Phase 12 replaces it with the real TypeScript extension. The Python `PiProvider` can be kept as a fallback for programmatic use or removed.
- **D-04:** Extension registers commands under the `/glma` namespace. Currently `/glma-summarize`; future commands (`/glma-index`, `/glma-query`, `/glma-export`) can be added without changing the extension structure.

### model_hint Resolution
- **D-05:** `model_hint` in `.glma.toml` `[summarize]` section resolves against pi's existing model registry only. No glma-side model config duplication — pi owns all model/API key management via `models.json` and `auth.json`.
- **D-06:** Resolution rules:
  - `fast` → heuristic selection from pi's available models (prefer haiku, flash, mini — cheapest/fastest known families)
  - `capable` → heuristic selection (prefer opus, sonnet, gpt-4o — strongest known families)
  - exact model ID (e.g., `claude-sonnet-4-20250514`) → `ctx.modelRegistry.find(provider, id)`
  - empty / unset → pi's currently active model (`ctx.model`)
- **D-07:** Heuristic for `fast`/`capable` uses a built-in preference order of known model families, falling back to cost if no known models are found. No separate alias config needed — pi's registry is the source of truth.

### Provider Presets for Standalone Mode
- **D-08:** `--summarize-provider` accepts preset names that auto-fill base_url and model defaults. No separate `--ai-provider` flag. Values: `local` (raw/manual), `pi`, `ollama`, `lmstudio`, `llamacpp`, `vllm`, `aphrodite`.
- **D-09:** Built-in presets (from todo):
  - `lmstudio`: `http://localhost:1234/v1`, model `default`
  - `ollama`: `http://localhost:11434/v1`, model `llama3`
  - `llamacpp`: `http://localhost:8080/v1`, model `default`
  - `vllm`: `http://localhost:8000/v1`, model `default`
  - `aphrodite`: `http://localhost:7860/v1`, model `default`
- **D-10:** Custom presets configurable in `.glma.toml` `[summarize.providers]` section. Users can override URLs/models for built-in presets or add entirely new provider definitions.
- **D-11:** Preset resolution priority: `--summarize-provider <preset>` fills defaults → `--ai-url` overrides base_url → `--summarize-model` overrides model name. Explicit flags always win over preset defaults.

### Fallback Chain Behavior
- **D-12:** Auto-detect environment: if running inside pi (extension detected), use pi provider. Otherwise fall back to local/preset. User can override with explicit `--summarize-provider`.
- **D-13:** No silent cascading. If the detected or selected provider fails, error out with a clear message. Rule-based summaries are the default when `--summarize` isn't used at all — not a fallback tier.
- **D-14:** Auto-detection check: `--summarize` used without explicit `--summarize-provider` → detect if pi extension is available → use pi provider if yes, use `local` (lmstudio defaults) if no.

### Extension Location & Structure
- **D-15:** Extension lives at `.pi/extensions/` in the glma repo for pi auto-discovery. Hot-reloadable with `/reload`.
- **D-16:** Extension file: `.pi/extensions/glma-summarize.ts` (single file) or `.pi/extensions/glma/index.ts` (subdirectory if it grows). Start as single file, migrate to subdirectory if commands grow.
- **D-17:** Extension uses `@mariozechner/pi-coding-agent` for `ExtensionAPI`, `defineTool`, `registerCommand`. Uses `@mariozechner/pi-ai` for `complete`, `getModel`, `Type`. Uses `@mariozechner/pi-tui` for any UI components.

### Agent's Discretion
- Exact model family preference list for `fast`/`capable` heuristics
- How to read from glma's Ladybug DB from the extension (shell out to a query command? direct file access? Python helper script?)
- Exact `.pi/extensions/` file structure (single file vs subdirectory)
- Progress display during batch summarization (status line, notifications)
- Error message wording for failed provider detection
- Whether to keep or remove the Python `PiProvider` stub in `providers.py`
- How the extension discovers the glma DB path (config file, convention, CLI arg)
- Test strategy for the TypeScript extension

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Source todo (requirements and acceptance criteria)
- `.Complete/todos/Complete/2026-04-10-pi-agent-integration-for-summarization.md` — Original problem description, fallback chain, model_hint design, provider presets, CLI usage examples, proposed `AIProvider` enum

### Pi extension documentation (MUST read — this is the implementation target)
- `pi-coding-agent/docs/extensions.md` — Full extension API: `registerTool`, `registerCommand`, `ExtensionAPI`, `ctx.modelRegistry`, `ctx.model`, `complete()`, events, state management
- `pi-coding-agent/docs/models.md` — How pi configures models via `models.json`, provider structure, custom providers
- `pi-coding-agent/examples/extensions/hello.ts` — Minimal tool registration pattern
- `pi-coding-agent/examples/extensions/summarize.ts` — Direct model call pattern (`getModel()` → `getApiKeyAndHeaders()` → `complete()`), closest reference for the command implementation
- `pi-coding-agent/examples/extensions/tools.ts` — Stateful extension with session events, `appendEntry`, command registration

### Glma summarization pipeline (the backend being integrated)
- `02-worktrees/glma/src/glma/summarize/providers.py` — `SummarizerProvider` protocol, `OpenAICompatibleProvider`, `PiProvider` stub
- `02-worktrees/glma/src/glma/summarize/pipeline.py` — `summarize_chunks()` function, decomposition logic, incremental summarization
- `02-worktrees/glma/src/glma/cli.py` — CLI `index` command with `--summarize`, `--summarize-provider`, `--summarize-model`, `--max-chunk-chars` flags
- `02-worktrees/glma/src/glma/config.py` — `load_summarize_config()` pattern
- `02-worktrees/glma/src/glma/models.py` — `SummarizeConfig`, `SummarizeProvider` enum, `ExportConfig`
- `02-worktrees/glma/src/glma/db/ladybug_store.py` — `update_chunk_summary()`, `get_chunks_for_file()`, DB access methods

### Prior phase decisions (constraints and patterns)
- `.planning/phases/07-cli-integration-providers/07-CONTEXT.md` — Established `[summarize]` config section, `SummarizerProvider` protocol, `PiProvider` as optional, one model/provider for everything
- `.planning/phases/10-chunk-truncation-summarization/10-CONTEXT.md` — Decomposition logic, `max_chunk_chars` config, try-first/decompose-on-failure pattern
- `.planning/phases/11-markdown-keyvalue-export/11-CONTEXT.md` — `ExportFormat` enum, strategy pattern

### Project conventions
- `.planning/codebase/CONVENTIONS.md` — Typer CLI pattern, Pydantic config models
- `.planning/codebase/STACK.md` — Python 3.13, Typer, Rich, Pydantic

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`OpenAICompatibleProvider`** (`providers.py`): Working provider with configurable `base_url` + `model`. Presets just pre-fill these constructor args.
- **`summarize_chunks()`** (`pipeline.py`): Full pipeline — incremental, decomposition, error handling, logging. Local model path shells out to this.
- **`SummarizeConfig`** (`models.py`): Already has `provider`, `model`, `base_url`, `max_chunk_chars` fields. Needs `provider` enum expanded to accept preset names.
- **`load_summarize_config()`** (`config.py`): Config merge pattern — add `[summarize.providers]` section loading.
- **Pi's `complete()` API** (`@mariozechner/pi-ai`): Cloud model call pattern shown in `summarize.ts` example — `getModel()` → `getApiKeyAndHeaders()` → `complete(model, messages, options)`.

### Established Patterns
- **Config loading**: `tomllib` → `.glma.toml` section → merge with CLI overrides → Pydantic model. Add provider preset resolution before Pydantic validation.
- **CLI flags**: `typer.Option()` with defaults. `--summarize-provider` already exists, expanding its accepted values.
- **Pi extension pattern**: TypeScript file exporting a function `(pi: ExtensionAPI) => void`. Registers tools and commands. Uses `ctx.modelRegistry` for model access.
- **Pi model access**: `ctx.modelRegistry.find(provider, id)` for lookup, `ctx.modelRegistry.getApiKeyAndHeaders(model)` for auth, `complete(model, messages, opts)` for invocation.

### Integration Points
- **`--summarize-provider` flag** (`cli.py`): Expand `SummarizeProvider` enum to include preset names, or add a separate resolution layer that maps presets → local provider + URL/model.
- **`SummarizeProvider` enum** (`models.py`): Currently `LOCAL` / `PI`. Needs to accept preset names or be replaced with string-based resolution.
- **`.glma.toml [summarize.providers]`** (`config.py`): New config section for custom presets.
- **`.pi/extensions/`**: New directory for the pi extension file. Currently doesn't exist in the project.
- **`PiProvider` class** (`providers.py`): Stub that needs replacement — either removed or repurposed as a thin wrapper.

</code_context>

<specifics>
## Specific Ideas

- The `summarize.ts` pi example (`pi-coding-agent/examples/extensions/summarize.ts`) is the closest reference for the command implementation — it shows `getModel()` → `getApiKeyAndHeaders()` → `complete()` for calling a model from an extension.
- The extension reads chunks needing summaries from glma's Ladybug DB. For cloud models, it calls `complete()` directly and writes summaries back. For local models, it shells out to `glma index --summarize` and lets the Python pipeline handle everything.
- Model hint resolution should feel invisible — user sets `model_hint = "fast"` in `.glma.toml` or leaves it empty (uses pi's current model), and the extension figures out the rest.
- `/glma` as a command namespace means future commands can be added: `/glma-index`, `/glma-query`, `/glma-export` — the extension becomes the primary interface when running inside pi.
- Provider presets make standalone mode much more approachable: `glma index --summarize --summarize-provider ollama` instead of remembering port numbers.

</specifics>

<deferred>
## Deferred Ideas

- **Full `/glma` command suite** (`/glma-index`, `/glma-query`, `/glma-export`) — out of scope for this phase, but the extension structure supports adding them later
- **SDK headless session** (`createAgentSession()`) for background summarization — alternative approach from the todo, deferred in favor of direct model call pattern
- **Streaming progress from extension** — Rich progress bar equivalent in pi's TUI during batch summarization; nice-to-have, not essential

### Reviewed Todos (not folded)
The following todos matched Phase 12 but were already completed in prior phases:
- **Truncate oversized chunks before summarization** — completed in Phase 10
- **Add markdown key-value export format** — completed in Phase 11

</deferred>

---

*Phase: 12-pi-agent-integration*
*Context gathered: 2026-04-14*
