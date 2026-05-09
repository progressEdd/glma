---
plan: "14-01"
phase: "14"
status: complete
wave: 1
gap_closure: false
started: "2026-05-09"
completed: "2026-05-09"
---

# Summary: Schema & Data Model — Embedding Columns on Chunk Table

## Objective
Add embedding, summary_hash, and vector_dimensions fields to the Chunk node table schema, extend the Chunk Pydantic model, implement schema migration for existing databases, and extend upsert_chunks() to preserve embedding data across re-indexing operations.

## What Was Built
- Extended Chunk Pydantic model with 3 optional fields: embedding (list[float]), summary_hash (str), vector_dimensions (int)
- Updated SCHEMA_CHUNKS with FLOAT[768] embedding column, summary_hash STRING, vector_dimensions INT64
- Added _migrate_schema() method for ALTER TABLE migration on existing databases
- Added update_chunk_embedding() for targeted field updates
- Added get_chunks_needing_embedding() for incremental embedding detection (NULL embedding, dim mismatch)
- Added get_all_chunks_with_summaries() for force-embed mode
- Extended upsert_chunks() to preserve embedding data via embedding_map across re-indexing
- Updated get_chunks_for_file() to return embedding fields (rows 10-12)

## Files Modified
- `src/glma/models.py` — Added 3 optional fields to Chunk model
- `src/glma/db/ladybug_store.py` — Schema, migration, new methods, upsert preservation
- `tests/test_store.py` — Added TestEmbeddingFields (4 new tests)

## Test Results
- 15 store tests pass (11 existing + 4 new)
- 333 total tests pass, 0 regressions

## Deviations
- Added get_all_chunks_with_summaries() method (not in original plan) to support force-embed mode

## key-files
- created: []
- modified: ["src/glma/models.py", "src/glma/db/ladybug_store.py", "tests/test_store.py"]
