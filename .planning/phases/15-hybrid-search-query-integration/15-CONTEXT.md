# Phase 15: Hybrid Search & Query Integration - Context

**Gathered:** 2026-05-09
**Status:** Ready for planning

<domain>
## Phase Boundary

Add `glma search "natural language query"` as a new top-level CLI command that performs hybrid keyword + vector search across all chunk summaries in the database. Results are ranked by combined fuzzy keyword similarity and vector cosine similarity with configurable weights. Includes `--search-mode hybrid|vector|keyword` for strategy control.

This phase delivers: `glma search` command, hybrid search engine (fuzzy + vector), result formatting across all output formats, search mode flag, threshold filtering.

No changes to existing `glma query` command. No auto-embedding during search. No query rewriting.

</domain>

<decisions>
## Implementation Decisions

### Command Structure
- **D-01:** New top-level `glma search "text"` command — completely separate from file-scoped `glma query`. Different input (NL string vs file path), different output (ranked cross-file chunks vs structured single-file view), different scope (whole codebase vs one file).
- **D-02:** `glma search` inherits the same flag pattern as `glma query` where it makes sense: `--format` (markdown-kv, markdown, json, yaml), `--output`, `--repo`, `--verbose`. Exact flag mapping left to planning.
- **D-03:** Embedding-related CLI flags follow the same pattern as `glma embed`: `--embedding-provider`, `--embedding-model`, `--embedding-base-url`, `--vector-dimensions` for overriding search config.

### Result Format
- **D-04:** Search results are maximally lean: file path as heading (`# src/auth/login.py`), then code blocks with their matching summaries. No line numbers, chunk names, scores, or other metadata in the output.
- **D-05:** Consumers who need metadata (line range, chunk name, relationships) can follow up with `glma query <file>` on the relevant file path.
- **D-06:** Code blocks are the primary content — the summaries that got matched are shown alongside the code so consumers see why the result is relevant.

### Scoring & Threshold
- **D-07:** Unified scoring framework: `keyword_weight × fuzzy_score + vector_weight × vector_score`. Both components are always computed when in hybrid mode.
- **D-08:** Search modes just shift the weights:
  - `hybrid` (default): both weights from config (default 0.5/0.5)
  - `vector`: vector only (weights effectively 0.0/1.0)
  - `keyword`: fuzzy keyword only (weights effectively 1.0/0.0)
- **D-09:** Results below `similarity_threshold` are filtered out entirely.
- **D-10:** When no results pass the threshold: empty output with actionable message telling user to try lowering `--similarity-threshold`. No silent fallback to low-quality results.

### Keyword Fuzzy Matching
- **D-11:** Keyword component uses **fuzzywuzzy** for fuzzy string similarity between the query and chunk summaries. Exact fuzzy function (token_sort_ratio, partial_ratio, etc.) left to planning/research.
- **D-12:** All chunks with summaries are compared against the query string using fuzzy matching. No pre-filtering or indexing for keyword mode — brute-force comparison.

### Search Mode Fallbacks
- **D-13:** `--search-mode vector` when no embeddings exist in the database: explicit error with actionable message ("No embeddings found. Run `glma embed` first."). No silent fallback to keyword mode.
- **D-14:** `--search-mode keyword` works without embeddings — only needs summaries, which are always present after indexing + summarization.
- **D-15:** `--search-mode hybrid` when no embeddings exist: same error as vector mode, since hybrid requires vector scoring.

### Agent's Discretion
- Exact fuzzywuzzy similarity function (token_sort_ratio, partial_ratio, etc.)
- How to structure the search module (new `search/` directory, or extend existing modules)
- Exact result format for each output type (json, yaml, markdown, markdown-kv)
- Whether to add `--similarity-threshold` and `--search-mode` flags or only support them via config
- How many results to return by default (top N, or all above threshold)
- Test structure and coverage specifics
- Whether fuzzy matching is done in Python or pushed to Cypher

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Embedding infrastructure (built in Phase 13)
- `02-worktrees/glma/src/glma/embedding/providers.py` — `EmbeddingProvider` protocol, `OpenAIEmbeddingProvider` with `embed(texts: list[str]) -> list[list[float]]`
- `02-worktrees/glma/src/glma/models.py` — `SearchConfig` model with `similarity_threshold`, `hybrid_keyword_weight`, `hybrid_vector_weight`, `vector_dimensions`, `EMBEDDING_PROVIDER_PRESETS`
- `02-worktrees/glma/src/glma/config.py` — `load_search_config()` for provider preset resolution, config file loading, CLI override merging

### Database layer (query patterns)
- `02-worktrees/glma/src/glma/db/ladybug_store.py` — `LadybugStore` class with `get_all_chunks_with_summaries()`, `get_chunks_for_file()`, embedding columns on Chunk table. `array_cosine_similarity()` confirmed working in Cypher. **No native vector index** — brute-force similarity.

### CLI patterns (must follow)
- `02-worktrees/glma/src/glma/cli.py` — Typer command pattern, `@app.command()`, config loading in CLI context, provider instantiation, `glma embed` command as closest reference for new `glma search` command
- `02-worktrees/glma/src/glma/query/formatter.py` — Existing output formatters (compact, KV, JSON, YAML). Search results need new formatting but follow same output modes.

### Prior phase decisions (constraints)
- `.planning/phases/13-embedding-infrastructure/13-CONTEXT.md` — Embedding provider protocol, config structure, preset naming
- `.planning/phases/14-vector-storage-embedding-command/14-CONTEXT.md` — Vector storage model, Ladybug schema with embedding columns, confirmed no native vector index in real_ladybug 0.15.3

### Project conventions
- `.planning/codebase/CONVENTIONS.md` — Typer CLI pattern, Pydantic config models
- `.planning/codebase/STACK.md` — Python 3.13, Typer, Rich, Pydantic

### Requirements
- `.planning/REQUIREMENTS.md` — SRCH-01 through SRCH-06 (hybrid search and query integration requirements)
- `.planning/ROADMAP.md` — Phase 15 success criteria

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`OpenAIEmbeddingProvider`** (`embedding/providers.py`): `embed()` method ready to use for query embedding. Takes `list[str]`, returns `list[list[float]]`.
- **`load_search_config()`** (`config.py`): Fully working config loader for `[search]` section. Returns `SearchConfig` with weights, threshold, provider settings.
- **`LadybugStore`** (`db/ladybug_store.py`): `get_all_chunks_with_summaries()` returns all chunks with non-empty summaries including their embeddings. This is the primary data source for search.
- **`SearchConfig`** (`models.py`): Already has `similarity_threshold`, `hybrid_keyword_weight`, `hybrid_vector_weight`, `vector_dimensions`.
- **Output formatters** (`query/formatter.py`): `format_json_output()`, `format_kv_output()`, `format_compact_output()`, `format_yaml_output()` — patterns to follow for search result formatting.

### Established Patterns
- **Cypher vector similarity**: `array_cosine_similarity(c.embedding, $query_vector)` works in real_ladybug. Brute-force — no index needed at codebase scale.
- **CLI command pattern**: Typer `@app.command()`, resolve repo root, load config, instantiate provider, Rich progress/error handling.
- **Config loading**: `load_search_config()` resolves provider presets, merges file config with CLI overrides. Same pattern for search command.
- **Output dispatch**: `--format` flag selects formatter. Same dispatch for search results.

### Integration Points
- **`cli.py`**: Add new `search` command. Follow `embed` command pattern for provider instantiation and config loading.
- **`ladybug_store.py`**: May need a new method for vector similarity query (Cypher with `array_cosine_similarity` + ORDER BY + LIMIT). Or the search engine can use `get_all_chunks_with_summaries()` and compute in Python.
- **New `search/` module** (or extend existing): Hybrid search engine — embed query, compute vector similarity, compute fuzzy similarity, combine scores, filter by threshold, rank results, format output.

</code_context>

<specifics>
## Specific Ideas

- fuzzywuzzy for keyword fuzzy matching — proven library for fuzzy string similarity
- Search results should be maximally lean: code + summary only, file path as heading
- The "keyword" component is fuzzy matching (not exact substring), which makes it more useful for natural language queries that don't exactly match summary text
- Consumers (agents) can always follow up with `glma query <file>` for detailed metadata — search is for discovery, query is for detail

</specifics>

<deferred>
## Deferred Ideas

- **LLM-based query rewriting** (SRCH-07) — noted in REQUIREMENTS.md deferred section
- **Graph relationship traversal + semantic search** (SRCH-08) — 3-way hybrid, future capability
- **Ladybug FTS index for keyword search** — proper full-text search index instead of fuzzy matching. Future phase if needed.
- **Auto-embedding during `glma index`** — generating embeddings at the same time as summaries. Future feature.

### Reviewed Todos (not folded)
The following todos matched Phase 15 but were already completed in prior phases:
- **Pi/agent integration for code summarization** — completed in Phase 12
- **Truncate oversized chunks before summarization** — completed in Phase 10
- **Add markdown key-value export format** — completed in Phase 11

</deferred>

---

*Phase: 15-hybrid-search-query-integration*
*Context gathered: 2026-05-09*
