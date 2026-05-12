---
status: resolved
trigger: "glma embed fails all 5264 chunks — hardcoded FLOAT[768] in schema rejects 1024-dim embeddings"
created: 2026-05-11T00:00:00.000Z
updated: 2026-05-11T00:00:00.000Z
---

## Current Focus

hypothesis: LadybugStore schema hardcodes embedding dimension as FLOAT[768] in three places, ignoring the vector_dimensions config in .glma.toml
test: `glma embed` with `--embedding-provider embed-lmstudio` (1024-dim model) against DB created with 768 dims
expecting: Embeddings stored successfully, schema adapted to model dimensions
next_action: N/A — all fixed and verified

## Symptoms

expected: `glma embed` generates and stores 1024-dim embeddings for all chunks
actual: All 5264 chunks fail with `RuntimeError: Conversion exception: Unsupported casting LIST with incorrect list entry to ARRAY. Expected: 768, Actual: 1024.`
errors: `RuntimeError: Expected: 768, Actual: 1024` on every SET operation
reproduction: Configure `vector_dimensions = 1024` in `.glma.toml`, run `glma embed` against DB created at 768 dims
started: First discovered during v1.3 Phase 14 testing

## Eliminated

- hypothesis: LM Studio is returning wrong-dimension vectors
  evidence: LM Studio returns correct 1024-dim vectors for the `text-embedding-qhen3-embedding-0.6b` model. The error is in LadybugStore's schema, not the provider.
  timestamp: 2026-05-11T00:00:00Z

## Evidence

- timestamp: 2026-05-11T00:00:00Z
  checked: `LadybugStore` schema definition in `ladybug_store.py`
  found: `SCHEMA_CHUNKS` DDL hardcoded `FLOAT[768]`, `_migrate_schema()` hardcoded `FLOAT[768]`, `create_vector_index()` defaulted to `768`. Config `vector_dimensions = 1024` never consulted.
  implication: Replace static schema with dynamic dimension-aware generation

- timestamp: 2026-05-11T00:00:00Z
  checked: KuzuDB (LadybugDB) array type requirements
  found: Array dimensions fixed at table creation time; no runtime casting between different array sizes
  implication: Must get dimensions right at schema creation, or rebuild table on mismatch

## Resolution

root_cause: `LadybugStore` hardcoded embedding vector dimension as `FLOAT[768]` in three places (DDL, migration, vector index). The `.glma.toml` `vector_dimensions` config was never read by the store.

fix: (1) Replaced static `SCHEMA_CHUNKS` with `_build_chunk_schema(dims)` static method. (2) Constructor now accepts `vector_dimensions` parameter (defaults to 768 for backward compat). (3) Added `_rebuild_chunk_table_if_needed()` — inspects actual schema via `CALL TABLE_INFO('Chunk')`, auto-rebuilds with correct dimensions on mismatch (preserving chunk data, clearing embeddings). (4) `_migrate_schema()` and `create_vector_index()` use instance dimension. (5) Updated `LadybugStore()` calls in `cli.py` embed and search commands to pass `vector_dimensions` from config.

verification: `glma embed` successfully stores 1024-dim embeddings. Auto-migration from 768→1024 preserves chunk data and summaries. All tests pass.

files_changed:
  - 02-worktrees/glma/src/glma/db/ladybug_store.py
  - 02-worktrees/glma/src/glma/cli.py
