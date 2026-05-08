# Phase 13: Embedding Infrastructure - Context

**Gathered:** 2026-05-08
**Status:** Ready for planning

<domain>
## Phase Boundary

Build the embedding provider protocol, OpenAI-compatible provider implementation, and `[search]` configuration infrastructure so that any local embedding model can generate vectors from text through a unified interface. No CLI commands (Phase 14's `glma embed`), no search (Phase 15). Purely the provider/config plumbing that downstream phases consume.

This phase delivers: EmbeddingProvider protocol, OpenAIEmbeddingProvider, SearchConfig model, `[search]` config loading, and provider presets.

</domain>

<decisions>
## Implementation Decisions

### Overall Architecture
- **D-01:** Summarization and embedding are separate pipeline steps. The architecture is:
  - **Index path:** Code chunks → summarizer model → chunk summaries → embed summaries → store vectors
  - **Query path:** User question → summarizer model → embed summary → hybrid search → ranked chunks
- **D-02:** The summarizer model generates both chunk summaries (index) and query summaries (search). The embedding model only embeds the resulting text.
- **D-03:** Only OpenAI-compatible provider (`/v1/embeddings` endpoint) for now. Hugging Face deferred.

### Protocol Shape
- **D-04:** `EmbeddingProvider` protocol with single method: `embed(texts: list[str]) -> list[list[float]]` — batch-only, no single-text convenience method. Callers wrap single text in `[text]`.
- **D-05:** No partial batch failure handling. Local providers either process the whole batch or fail entirely. Raise on error, let the caller handle retry.

### Provider Implementation
- **D-06:** `OpenAIEmbeddingProvider` class hits `/v1/embeddings` endpoint. Same pattern as `OpenAICompatibleProvider` for summarization but targeting the embeddings API instead of chat completions.
- **D-07:** Provider follows same constructor pattern: `(base_url: str, model: str)`. Optional `openai` package dependency (same `pip install glma[ai]` extra).

### Config Structure
- **D-08:** Single flat `[search]` section in `.glma.toml`. All fields at one level — no nesting.
- **D-09:** Phase 13 implements these fields: `enabled`, `embedding_provider`, `embedding_model`, `embedding_base_url`, `vector_dimensions`
- **D-10:** Phase 15 will add: `similarity_threshold`, `hybrid_keyword_weight`, `hybrid_vector_weight`. Pydantic model has sensible defaults so unused fields don't cause issues.
- **D-11:** `SearchConfig` Pydantic model in `models.py` with validation: dimensions > 0, threshold 0-1 (when used), weights sum to ~1.0 (when used).
- **D-12:** `load_search_config()` in `config.py` follows exact same pattern as `load_summarize_config()` — file config + CLI overrides + provider preset resolution.

### Provider Presets
- **D-13:** Embedding presets use prefixed names to distinguish from summarization presets: `embed-ollama`, `embed-lmstudio`, `embed-vllm`, `embed-llamacpp`, `embed-local`
- **D-14:** Embedding-specific model defaults:
  - `embed-ollama`: `http://localhost:11434/v1`, model `qwen3-embedding`
  - `embed-lmstudio`: `http://localhost:1234/v1`, model `default`
  - `embed-vllm`: `http://localhost:8000/v1`, model `default`
  - `embed-llamacpp`: `http://localhost:8080/v1`, model `default`
  - `embed-local`: `http://localhost:1234/v1`, model `default` (raw/manual, same as lmstudio)
- **D-15:** Custom embedding presets configurable in `[search.providers]` section of `.glma.toml`. Same merge pattern as `[summarize.providers]`.
- **D-16:** Preset resolution priority: `--embedding-provider <preset>` fills defaults → `--embedding-base-url` overrides URL → `--embedding-model` overrides model name. Explicit flags always win.

### Agent's Discretion
- Exact `OpenAIEmbeddingProvider` implementation details (request format, timeout, max_retries)
- Whether to create a separate `EMBEDDING_PROVIDER_PRESETS` dict or extend existing `PROVIDER_PRESETS`
- Error message wording for missing `openai` package
- Exact field names in SearchConfig (as long as they match the pattern)
- Test structure and coverage specifics

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Existing provider pattern (MUST follow)
- `02-worktrees/glma/src/glma/summarize/providers.py` — `SummarizerProvider` protocol, `OpenAICompatibleProvider` implementation pattern (constructor, error handling, optional dep import)
- `02-worktrees/glma/src/glma/models.py` — `SummarizeConfig`, `SummarizeProvider` enum, `PROVIDER_PRESETS` dict structure, `ExportConfig` for config model pattern
- `02-worktrees/glma/src/glma/config.py` — `load_summarize_config()` for preset resolution pattern, `load_config()` for file+CLI merge pattern
- `02-worktrees/glma/src/glma/cli.py` — CLI flag pattern with `typer.Option()`, summarize flags as reference for embedding flags

### Prior phase decisions (constraints)
- `.planning/phases/07-cli-integration-providers/07-CONTEXT.md` — Established provider protocol pattern, config loading, CLI flags
- `.planning/phases/12-pi-agent-integration/12-CONTEXT.md` — Provider presets, custom providers, preset resolution priority

### Project conventions
- `.planning/codebase/CONVENTIONS.md` — Typer CLI pattern, Pydantic config models
- `.planning/codebase/STACK.md` — Python 3.13, Typer, Rich, Pydantic

### Requirements
- `.planning/REQUIREMENTS.md` — EMB-01 through EMB-07 (embedding infrastructure requirements)
- `.planning/ROADMAP.md` — Phase 13 success criteria

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`OpenAICompatibleProvider`** (`summarize/providers.py`): Exact pattern to follow for `OpenAIEmbeddingProvider`. Constructor takes `base_url` + `model`, uses `from openai import OpenAI` with optional dep handling.
- **`PROVIDER_PRESETS`** (`models.py`): Dict of `{name: {base_url, model}}`. Embedding needs its own `EMBEDDING_PROVIDER_PRESETS` with prefixed names.
- **`SummarizeConfig`** (`models.py`): Pydantic model pattern — `SearchConfig` follows same shape with embedding-specific fields.
- **`load_summarize_config()`** (`config.py`): Full preset resolution logic — read `[summarize]` section, load custom providers from `[summarize.providers]`, resolve preset to base_url/model, merge with CLI overrides. `load_search_config()` mirrors this.
- **CLI flag pattern** (`cli.py`): `--summarize-provider`, `--summarize-model` → `--embedding-provider`, `--embedding-model`.

### Established Patterns
- **Config loading**: `tomllib` → `.glma.toml` section → merge with CLI overrides → Pydantic model → preset resolution. `load_search_config()` follows this exactly.
- **Provider protocol**: Protocol class with single method, concrete implementation class, optional dependency import. `EmbeddingProvider` mirrors `SummarizerProvider`.
- **Preset resolution**: Preset fills defaults → explicit flags override. Same priority chain for embedding presets.

### Integration Points
- **`models.py`**: Add `SearchConfig`, `EMBEDDING_PROVIDER_PRESETS`, embedding-related enums/models
- **`config.py`**: Add `load_search_config()` function
- **`providers.py`** (or new `embedding/providers.py`): Add `EmbeddingProvider` protocol + `OpenAIEmbeddingProvider`
- **`cli.py`**: Phase 14 will add embedding flags, but Phase 13 config loading needs to be ready for CLI override dict

</code_context>

<specifics>
## Specific Ideas

- Ollama's default embedding model should be `qwen3-embedding` — specific and modern
- Hugging Face model noted for future: `ENOSYS/Octen-Embedding-8B-750-v1-GGUF` — will use `sentence-transformers` integration
- Embedding presets are prefixed (`embed-*`) to explicitly distinguish from summarization presets even though they hit the same servers

</specifics>

<deferred>
## Deferred Ideas

- **Hugging Face embedding provider** — in-process via `sentence-transformers`, model `ENOSYS/Octen-Embedding-8B-750-v1-GGUF`. Belongs in a future phase after OpenAI-compatible provider is proven.
- **LLM-based query rewriting** (SRCH-07) — noted in REQUIREMENTS.md deferred section
- **Graph relationship traversal + semantic search** (SRCH-08) — 3-way hybrid, future capability

### Reviewed Todos (not folded)
The following todos matched Phase 13 but were already completed in prior phases:
- **Pi/agent integration for code summarization** — completed in Phase 12
- **Truncate oversized chunks before summarization** — completed in Phase 10
- **Add markdown key-value export format** — completed in Phase 11

</deferred>

---

*Phase: 13-embedding-infrastructure*
*Context gathered: 2026-05-08*
