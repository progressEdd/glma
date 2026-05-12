# 2026-05-11: Embedding Dimension Mismatch — Hardcoded FLOAT[768] in DB Schema

## Problem

Running `glma embed` against an indexed repo (ag2-framework) resulted in **all 5264 chunks failing**:

```
Embedded:  0
Skipped:   0
Failed:    5264
```

LM Studio was successfully receiving requests and returning 1024-dimensional vectors for the model `text-embedding-qwen3-embedding-0.6b`, but the store threw a runtime error:

```
RuntimeError: Conversion exception: Unsupported casting LIST with incorrect list entry to ARRAY.
Expected: 768, Actual: 1024.
```

## Root Cause

The `LadybugStore` class had the embedding vector dimension **hardcoded as `FLOAT[768]`** in three places:

1. `SCHEMA_CHUNKS` — the `CREATE NODE TABLE` DDL
2. `_migrate_schema()` — the `ALTER TABLE ADD embedding FLOAT[768]` migration
3. `create_vector_index()` — default parameter `dimensions: int = 768`

KuzuDB (LadybugDB) requires array dimensions to be specified at table creation time and does not allow mismatched dimensions in SET operations. The `.glma.toml` config correctly specified `vector_dimensions = 1024`, but the store never consulted it.

## Changes Made

### `src/glma/db/ladybug_store.py`

1. **Dynamic schema generation**: Replaced the static `SCHEMA_CHUNKS` string with a `_build_chunk_schema(dims)` static method that generates the DDL with the correct dimension.

2. **Constructor accepts `vector_dimensions`**:
   ```python
   def __init__(self, db_path: Path, vector_dimensions: int = 0)
   ```
   Defaults to `DEFAULT_VECTOR_DIMS = 768` when not provided (backward compatible).

3. **Auto-rebuild on dimension mismatch**: Added `_rebuild_chunk_table_if_needed()` which inspects the actual schema via `CALL TABLE_INFO('Chunk') RETURN *`, extracts the dimension from the type string (e.g. `FLOAT[768]`), and if it doesn't match the config:
   - Preserves all chunk data (id, content, summary, etc.) minus embeddings
   - Drops and recreates the Chunk table with correct dimensions
   - Re-inserts preserved chunks
   - Rebuilds `CONTAINS` edges from File→Chunk

4. **`_migrate_schema()`** now uses `self._vector_dims` instead of hardcoded 768.

5. **`create_vector_index()`** default changed from `768` to `0` (falls back to instance default).

### `src/glma/cli.py`

Updated two `LadybugStore()` instantiations to pass `vector_dimensions` from the loaded `SearchConfig`:

- `embed` command (line ~499)
- `search` command (line ~729)

## State / Follow-up Needed

- The ag2-framework index was wiped during debugging (`.glma-index` deleted). A full re-index + summarize is needed before embed can be re-run:
  ```bash
  rm -rf <repo>/.glma-index
  uv run glma index <repo> --summarize
  uv run glma embed <repo>
  ```

- The re-index was started but timed out (600s). The summarize pass over 648 files with a local LLM takes a long time.

- The `_rebuild_chunk_table()` auto-migration should be tested end-to-end: index at 768, then change config to 1024, then run embed — verify chunks and summaries are preserved while embeddings are cleared for re-generation.

- Other `LadybugStore()` callers in `cli.py` (index, query, export) don't pass `vector_dimensions` — this is fine since they don't need to write embeddings, but if they ever need to, they should be updated too.
