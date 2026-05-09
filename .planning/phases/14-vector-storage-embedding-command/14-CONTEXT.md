# Phase 14: Vector Storage & Embedding Command - Context

**Gathered:** 2026-05-09
**Status:** Ready for planning

<domain>
## Phase Boundary

Store chunk summary embeddings in the Ladybug graph database and provide a `glma embed` CLI command to generate/update them. This phase connects the Phase 13 embedding infrastructure (provider protocol, config, presets) to actual persisted vectors in the database, ready for Phase 15 hybrid search to query.

No CLI query integration (Phase 15). No auto-embedding during indexing (deferred). Purely vector persistence and the standalone embed command.

</domain>

<decisions>
## Implementation Decisions

### Embedding Storage Model
- **D-01:** Add `embedding FLOAT[N]`, `summary_hash STRING`, and `vector_dimensions INT64` columns directly to the existing `Chunk` node table in LadybugStore. No separate table.
- **D-02:** `embedding` column initialized as NULL (no vector) or a FLOAT array. Chunks start without embeddings — they're added only when `glma embed` runs.
- **D-03:** `summary_hash` stores the hash of the summary text at the time it was embedded. Used for incremental change detection.
- **D-04:** `vector_dimensions` stores the configured dimension count at embed time. Used to detect model/dimension mismatches on re-runs.
- **D-05:** Schema migration: `SCHEMA_CHUNKS` in LadybugStore gets the three new columns. Existing databases will need the columns added (handle gracefully — the `CREATE NODE TABLE IF NOT EXISTS` pattern means schema changes need an ALTER or re-creation strategy).

### `glma embed` CLI Design
- **D-06:** Standalone `embed` command in `cli.py` using Typer, following the same pattern as `index` and `query` commands.
- **D-07:** Auto-detects provider config from `.glma.toml` `[search]` section via `load_search_config()`. CLI flags override config file values.
- **D-08:** CLI flags: `--embedding-provider <name>`, `--embedding-model <name>`, `--embedding-base-url <url>`, `--vector-dimensions <int>`, `--force`, `--quiet`.
- **D-09:** `--force` re-embeds chunks where the summary has changed (ignores summary_hash match check). Does NOT re-embed chunks with unchanged summaries. Still only embeds chunks that have non-empty summaries.
- **D-10:** Progress display uses Rich progress bar, consistent with the `IndexProgress` pattern from `index/progress.py`. Shows files → chunks → embedding status.
- **D-11:** Requires an existing index (fails with clear error if no database found). Does NOT trigger re-indexing or re-summarization.

### Incremental Embedding Logic
- **D-12:** For each chunk in the database:
  1. Skip if `summary` is NULL or empty (nothing to embed)
  2. Skip if `embedding` exists AND `summary_hash` matches current summary AND `vector_dimensions` matches config
  3. Embed the summary text, store vector + update `summary_hash` + update `vector_dimensions`
- **D-13:** Dimension mismatch detection: if `vector_dimensions` on a chunk ≠ `vector_dimensions` from config, re-embed regardless of hash match. Prevents cosine similarity errors from mismatched-length vectors at query time.
- **D-14:** `--force` overrides the summary_hash check only — still skips chunks with no summary, still checks dimension mismatch.

### Batching & Error Handling
- **D-15:** Dynamic batch size based on total text length in the batch. Shorter summaries → larger batches. Longer summaries → smaller batches. Target a character budget per API call (e.g., cap at ~32K chars per batch) rather than a fixed chunk count.
- **D-16:** Skip failed batches, continue to next batch. Log warnings with chunk IDs that failed. No retry.
- **D-17:** Exit code 0 if all eligible chunks embedded successfully (or nothing to embed). Exit code 1 if any failures occurred.
- **D-18:** Final progress summary shows: embedded count / skipped count / failed count / total chunks.

### Agent's Discretion
- Exact dynamic batching formula/character budget threshold
- Summary hash algorithm (BLAKE2b to match content_hash pattern, or simpler)
- How to handle the schema migration for existing databases (ALTER TABLE vs. detect-and-recreate)
- Error message wording
- Test structure and coverage specifics
- Whether to create a separate `embedding/pipeline.py` or add embed logic to existing module

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Existing embedding infrastructure (built in Phase 13)
- `02-worktrees/glma/src/glma/embedding/providers.py` — `EmbeddingProvider` protocol, `OpenAIEmbeddingProvider` implementation. The `embed(texts: list[str]) -> list[list[float]]` method is the API surface.
- `02-worktrees/glma/src/glma/models.py` — `SearchConfig` model with `vector_dimensions`, `similarity_threshold`, `hybrid_keyword_weight`, `hybrid_vector_weight`, `EMBEDDING_PROVIDER_PRESETS` dict
- `02-worktrees/glma/src/glma/config.py` — `load_search_config()` for provider preset resolution, config file loading, CLI override merging

### Database layer (must modify)
- `02-worktrees/glma/src/glma/db/ladybug_store.py` — `LadybugStore` class, `SCHEMA_CHUNKS` definition, `upsert_chunks()`, `update_chunk_summary()`. This is where embedding columns and storage methods go.

### CLI patterns (must follow)
- `02-worktrees/glma/src/glma/cli.py` — Typer command pattern, config loading in CLI context, provider instantiation, Rich progress display
- `02-worktrees/glma/src/glma/index/progress.py` — `IndexProgress` class for Rich progress bar pattern

### Summarization pipeline (reference for incremental pattern)
- `02-worktrees/glma/src/glma/summarize/pipeline.py` — `summarize_chunks()` function showing incremental processing (skip already-summarized), batch error handling, progress reporting pattern

### Prior phase decisions (constraints)
- `.planning/phases/13-embedding-infrastructure/13-CONTEXT.md` — Embedding provider protocol shape, config structure, preset naming, field decisions
- `.planning/phases/07-cli-integration-providers/07-CONTEXT.md` — Established provider protocol pattern, config loading, CLI flags

### Project conventions
- `.planning/codebase/CONVENTIONS.md` — Typer CLI pattern, Pydantic config models
- `.planning/codebase/STACK.md` — Python 3.13, Typer, Rich, Pydantic

### Requirements
- `.planning/REQUIREMENTS.md` — VEC-01 through VEC-05 (vector storage and embed command requirements)
- `.planning/ROADMAP.md` — Phase 14 success criteria

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`OpenAIEmbeddingProvider`** (`embedding/providers.py`): Batch `embed()` method ready to call. Takes `list[str]`, returns `list[list[float]]`.
- **`load_search_config()`** (`config.py`): Fully working config loader for `[search]` section with preset resolution. Returns `SearchConfig` with all needed fields.
- **`LadybugStore`** (`db/ladybug_store.py`): Chunk table schema, `update_chunk_summary()` method for targeted field updates, `get_chunks_for_file()` for chunk retrieval. Pattern for SET-based updates.
- **`IndexProgress`** (`index/progress.py`): Rich progress bar class. Should be followed for `glma embed` progress display.
- **`summarize_chunks()`** (`summarize/pipeline.py`): Reference for incremental processing pattern — skip already-done items, log failures, report counts.

### Established Patterns
- **Ladybug FLOAT[N] columns**: Confirmed working. `embedding FLOAT[768]` in CREATE TABLE works. Parameterized SET with list values works. `array_cosine_similarity(col, $query)` works for vector search queries.
- **No native vector index**: real_ladybug 0.15.3 does NOT support `CREATE VECTOR INDEX`. Similarity is brute-force via `array_cosine_similarity()` in Cypher. Fine for codebase scale.
- **SET updates**: `MATCH (c:Chunk {id: $id}) SET c.embedding = $emb` with parameterized float list works. SET to NULL also works.
- **Targeted field update**: `update_chunk_summary()` pattern: single MATCH + SET, no delete/recreate. Should be followed for `update_chunk_embedding()`.
- **CLI command pattern**: Typer `@app.command()`, resolve repo root, load config, instantiate provider, iterate files/chunks, Rich progress, error handling.

### Integration Points
- **`LadybugStore`**: Add `embedding`, `summary_hash`, `vector_dimensions` to `SCHEMA_CHUNKS`. Add `update_chunk_embedding()` method. Add method to query chunks needing embedding (no embedding, or stale hash, or dimension mismatch).
- **`cli.py`**: Add `embed` command. Follow `index` command pattern for repo root resolution and config loading.
- **`models.py`**: No changes needed — `SearchConfig` already has `vector_dimensions`.
- **`config.py`**: No changes needed — `load_search_config()` already works.

</code_context>

<specifics>
## Specific Ideas

- Dynamic batching should target a character budget (~32K chars per batch) rather than fixed count — local embedding providers are memory-bound on input text length, not chunk count
- The progress bar should show per-file granularity like `glma index` does, with chunk-level embedding status within each file
- Failed chunks should be identifiable in the output so users can investigate (file path + chunk name)

</specifics>

<deferred>
## Deferred Ideas

- **Auto-embedding during `glma index --summarize --embed`** — generating embeddings at the same time as summaries during indexing. Future feature, would require an `--embed` flag on the `index` command.
- **Hugging Face embedding provider** — in-process via `sentence-transformers`. Noted in Phase 13 context.
- **LLM-based query rewriting** (SRCH-07) — noted in REQUIREMENTS.md deferred section
- **Graph relationship traversal + semantic search** (SRCH-08) — 3-way hybrid, future capability

### Reviewed Todos (not folded)
The following todos matched Phase 14 but were already completed in prior phases:
- **Pi/agent integration for code summarization** — completed in Phase 12
- **Truncate oversized chunks before summarization** — completed in Phase 10
- **Add markdown key-value export format** — completed in Phase 11

</deferred>

---

*Phase: 14-vector-storage-embedding-command*
*Context gathered: 2026-05-09*
