# Phase 14: Vector Storage & Embedding Command - Research

**Researched:** 2026-05-09
**Phase:** 14-vector-storage-embedding-command
**Question:** What do I need to know to PLAN this phase well?

---

## 1. Ladybug FLOAT Array Support (Verified)

### Schema Definition
- `FLOAT[N]` columns work in `CREATE NODE TABLE` — tested with `FLOAT[768]`
- Parameterized inserts with Python `list[float]` work correctly
- `INT64` columns work for scalar integer fields
- `STRING` columns for hash fields work as expected

### INSERT and SET Operations
- **CREATE with float array**: Works via parameterized query (`$emb` → Python `list[float]`)
- **SET float array**: `SET c.embedding = $vec` works with parameterized values
- **SET to NULL**: `SET c.embedding = NULL` works — resets to NULL
- **Read back**: `RETURN c.embedding` returns the float list correctly
- **NULL check**: `c.embedding IS NULL` returns `True`/`False` correctly
- **COALESCE**: `COALESCE(c.summary_hash, "")` works for handling NULL → empty string

### Schema Migration (ALTER TABLE)
- `ALTER TABLE Chunk ADD embedding FLOAT[768]` works ✓
- `ALTER TABLE Chunk ADD summary_hash STRING` works ✓
- `ALTER TABLE Chunk ADD vector_dimensions INT64` works ✓
- **Important**: Syntax is `ALTER TABLE`, NOT `ALTER NODE TABLE` (the latter fails with parser error)
- After ALTER TABLE, existing rows have NULL for new columns (confirmed)
- `CREATE NODE TABLE IF NOT EXISTS` with the full schema (including new columns) silently succeeds on an already-migrated table — no conflict

### Critical: Re-indexing Destroys Embeddings
- `upsert_chunks()` uses `DETACH DELETE + CREATE` pattern
- When a file is re-indexed, ALL existing chunk data is deleted and recreated
- Currently `upsert_chunks()` preserves `summary` via `summary_map` (keyed on `content_hash`)
- **Embedding data WILL be lost** on re-index unless the same preservation pattern is extended
- **Solution**: Extend the `summary_map` pattern to also preserve `embedding`, `summary_hash`, and `vector_dimensions` when `content_hash` matches
- This must be implemented in `upsert_chunks()` as part of this phase

### FLOAT Array Dimension Enforcement
- Ladybug enforces the declared dimension: inserting `[1.0, 2.0]` into `FLOAT[4]` raises `Conversion exception: Unsupported casting LIST with incorrect list entry to ARRAY. Expected: 4, Actual: 2`
- This means the dimension in `SCHEMA_CHUNKS` must match the provider's actual output dimension
- **Problem**: Different embedding models produce different dimensions (384, 768, 1024, etc.)
- **Solution options**:
  1. Use a fixed dimension in schema (e.g., `FLOAT[768]`) — requires DB rebuild when changing models
  2. Use `LIST` instead of `FLOAT[N]` — loses type safety but allows variable dimensions
  3. Store dimension from config, let the schema match it — but schema is hardcoded

**Recommended**: Use `FLOAT[768]` as default but rebuild schema when dimensions change. The `vector_dimensions` column tracks what dimension was actually used. If mismatch detected, user must re-create DB or use `--force` (which would need to handle this).

Actually, **better approach**: Use the `LIST` type instead of `FLOAT[N]` to avoid dimension-locking the schema. Testing needed.

### LIST vs FLOAT[N] Test (Not Yet Done)
- Need to verify if `LIST` type works for storing float vectors and if `array_cosine_similarity` works with `LIST` type
- If `LIST` works with cosine similarity, use that instead of `FLOAT[N]` to avoid dimension locking

---

## 2. Existing Code Patterns to Follow

### LadybugStore Methods
- **`update_chunk_summary(chunk_id, summary)`**: Single MATCH + SET pattern. This is the pattern for `update_chunk_embedding()`.
- **`upsert_chunks(file_path, chunks)`**: DELETE + CREATE pattern with `summary_map` preservation. Must be extended to preserve embeddings.
- **`get_chunks_for_file(file_path)`**: Returns `list[Chunk]` ordered by `start_line`. Pattern for querying chunks needing embedding.
- **`get_indexed_files()`**: Returns `dict[str, str]` of path → hash. Pattern for iterating all files.

### CLI Command Pattern (from `cli.py`)
1. Optional `path` argument with `Path.resolve()` default
2. `load_config()` / `load_search_config()` for config resolution
3. Provider instantiation with error handling
4. `LadybugStore` creation from `db_path`
5. Iterate files → iterate chunks → process
6. Rich progress display
7. Exit codes (0 success, 1 error, 4 config/state error)

### Progress Display Pattern (from `index/progress.py`)
- `IndexProgress` class: `start(total)`, `advance(filename)`, `finish(message)`, `print_summary(...)`
- Uses Rich `Progress` with `SpinnerColumn`, `BarColumn`, `TextColumn`, `TimeElapsedColumn`
- For embedding: similar class (`EmbedProgress`) or reuse pattern

### Incremental Processing Pattern (from `summarize/pipeline.py`)
- `summarize_chunks()` iterates chunks, skips those with existing summary
- Counts: summarized, skipped, failed, decomposed
- Error handling: log and skip, never abort pipeline
- This is the exact pattern for the embedding pipeline

### Chunk Model (from `models.py`)
- `Chunk` Pydantic model has: id, file_path, chunk_type, name, content, summary, start_line, end_line, content_hash, parent_id
- **No embedding fields yet** — will need `embedding: Optional[list[float]]`, `summary_hash: Optional[str]`, `vector_dimensions: Optional[int]` added

### Config Pattern (from `config.py`)
- `load_search_config()` already works: resolves presets, merges CLI overrides, returns `SearchConfig`
- `SearchConfig` has: `embedding_provider`, `embedding_model`, `embedding_base_url`, `vector_dimensions`
- No changes needed to config loading — Phase 13 built everything needed

---

## 3. Architecture Decisions from Research

### Embedding Pipeline Location
- **Create `glma/embedding/pipeline.py`** — parallel to `glma/summarize/pipeline.py`
- Keep embedding logic separate from summarization — different providers, different data shapes
- `embedding/` directory already exists with `providers.py` and `__init__.py`

### Schema Migration Strategy
1. `_init_schema()` runs on every `LadybugStore.__init__()`
2. Add `ALTER TABLE` statements after the `CREATE TABLE IF NOT EXISTS` for Chunk
3. Use try/except to handle the case where columns already exist (ALTER TABLE on existing column is an error)
4. **OR**: Check column existence first, then ALTER TABLE if missing
5. The `CREATE IF NOT EXISTS` with full schema (including new columns) will silently succeed, so it's safe to include the full schema in `SCHEMA_CHUNKS`

**Recommended approach**:
- Update `SCHEMA_CHUNKS` to include new columns
- Add `_migrate_schema()` method that runs `ALTER TABLE` for each new column, catching "already exists" errors
- Call `_migrate_schema()` after `_init_schema()` in `__init__`
- This handles both fresh databases (full schema) and existing databases (migration)

### Embedding Preservation During Re-index
- Extend `upsert_chunks()` to build an `embedding_map` alongside `summary_map`
- Key on `content_hash` (same key — if content unchanged, embedding is still valid)
- When recreating chunks, restore `embedding`, `summary_hash`, `vector_dimensions` from map
- This mirrors the existing `summary_map` pattern exactly

### Chunk Model Extension
- Add `embedding: Optional[list[float]] = None` to `Chunk` model
- Add `summary_hash: Optional[str] = None` to `Chunk` model  
- Add `vector_dimensions: Optional[int] = None` to `Chunk` model
- These need to be serialized/deserialized in `get_chunks_for_file()` and `upsert_chunks()`

### CLI `embed` Command Structure
```
@app.command()
def embed(
    path: Optional[Path] = Argument(None),
    embedding_provider: Optional[str] = Option(None),
    embedding_model: Optional[str] = Option(None),
    embedding_base_url: Optional[str] = Option(None),
    vector_dimensions: Optional[int] = Option(None),
    force: bool = Option(False),
    quiet: bool = Option(False, "--quiet", "-q"),
) -> None:
```

### Querying Chunks Needing Embedding
- Can't do hash comparison in Cypher (summary hash is computed in Python)
- **Approach**: Load all chunks with non-empty summaries, filter in Python:
  1. Skip if `summary` is empty/None
  2. Skip if `embedding` exists AND `summary_hash` matches computed hash AND `vector_dimensions` matches config
  3. Otherwise: needs embedding
- Use a new `LadybugStore.get_all_chunks_with_summaries()` method that returns chunks across all files

### Dynamic Batching
- Target: ~32K chars per batch
- Collect chunks until cumulative text length exceeds threshold, then flush batch
- Call `provider.embed(batch_texts)` → get vectors
- Store each vector via `update_chunk_embedding()`
- Continue to next batch

### Summary Hash Algorithm
- Use BLAKE2b (matches existing `content_hash` pattern)
- `hashlib.blake2b(summary.encode()).hexdigest()`
- Fast, deterministic, consistent with project conventions

---

## 4. Test Coverage Needs

### New Tests Required
1. **`test_store.py`**: Test schema migration (ALTER TABLE), `update_chunk_embedding()`, `get_all_chunks_with_summaries()`, embedding preservation during `upsert_chunks()`
2. **New `test_embed_command.py`** (or extend `test_cli.py`): Test `embed` CLI command
3. **`test_embedding_pipeline.py`**: Test the embedding pipeline logic (batching, incremental, error handling)
4. **Config tests**: Verify `load_search_config()` works with embed command CLI overrides

### Test Patterns from Existing Tests
- Use `tmp_path` fixture for temporary databases
- Mock `EmbeddingProvider.embed()` to return test vectors
- Test incremental: insert chunks with/without embeddings, run embed, verify correct ones updated
- Test force flag: verify all chunks re-embedded regardless of hash
- Test error handling: mock provider to fail on specific batch, verify others succeed

---

## 5. Risks and Open Questions

### FLOAT[N] vs LIST for Embeddings
- FLOAT[N] enforces dimension at schema level — problematic if user changes models
- LIST type may not work with `array_cosine_similarity()` (needed in Phase 15)
- **Mitigation**: Use FLOAT[N] with the configured dimension. Document that changing dimensions requires DB rebuild. Store `vector_dimensions` to detect mismatches.
- **For this phase**: We only need to store embeddings, not search them. Can defer the `array_cosine_similarity` question to Phase 15.

### Large Embedding Vectors in Memory
- 768-dim float = ~6KB per vector
- 10K chunks = ~60MB of vectors in memory during batch embedding
- Acceptable for codebase scale

### Embedding Provider Availability
- `glma embed` requires a running embedding server
- Clear error messages needed when server is unreachable
- Should fail early with helpful message, not hang

### Concurrent Access
- If `glma embed` runs while `glma watch` is active, could have conflicts
- Ladybug is single-writer — will error on concurrent writes
- **Mitigation**: Document this limitation. Not a code fix for v1.3.

---

## RESEARCH COMPLETE

### Summary of Key Findings

1. **Ladybug FLOAT[N] works** for storing embedding vectors — parameterized INSERT/SET, NULL, IS NULL all verified
2. **ALTER TABLE works** for schema migration — `ALTER TABLE Chunk ADD embedding FLOAT[768]` adds column to existing tables
3. **Re-indexing destroys embeddings** — `upsert_chunks()` must be extended with embedding preservation map
4. **All existing patterns** (CLI, progress, incremental, config) have clear templates to follow
5. **No new dependencies** — everything needed (Ladybug, Rich, Typer, Pydantic) is already in the project
6. **Phase 13 infrastructure** (EmbeddingProvider, SearchConfig, load_search_config) is complete and ready to consume

### Files to Modify
- `glma/models.py` — Add embedding fields to Chunk model
- `glma/db/ladybug_store.py` — Schema migration, embedding methods, preservation during upsert
- `glma/cli.py` — Add `embed` command
- `glma/embedding/__init__.py` — Export new pipeline functions

### Files to Create
- `glma/embedding/pipeline.py` — Embedding pipeline (batching, incremental, error handling)
- `tests/test_embedding_pipeline.py` — Pipeline tests
- `tests/test_embed_cli.py` — CLI command tests (or extend test_cli.py)
