---
plan: "14-02"
phase: "14"
status: complete
wave: 1
gap_closure: false
started: "2026-05-09"
completed: "2026-05-09"
---

# Summary: Embedding Pipeline & CLI Command

## Objective
Create the embedding/pipeline.py module with core embedding logic (batching, incremental detection, error handling) and the glma embed CLI command connecting Phase 13 embedding providers to Phase 14 vector storage.

## What Was Built
- Created embedding/pipeline.py with:
  - embed_chunks() main pipeline: DB query → filter → batch → embed → store
  - _batch_chunks_by_char_budget() splits by cumulative summary text length (32K chars/batch)
  - _compute_summary_hash() using BLAKE2b for change detection
  - EmbeddingProgress dataclass tracking embedded/skipped/failed counts and failed chunk IDs
  - Incremental logic: skip chunks where embedding exists and summary hash + dims match
  - Force mode: re-embed all chunks with summaries regardless of current state
  - Error resilience: failed batches are logged and skipped, pipeline continues
- Added 'glma embed' CLI command with:
  - --embedding-provider, --embedding-model, --embedding-base-url, --vector-dimensions, --force, --quiet options
  - Config loading with CLI overrides merged with .glma.toml [search] section
  - Rich progress display with spinner
  - Exit codes: 0 success, 1 failures, 4 no index
- Updated embedding/__init__.py exports

## Files Modified
- `src/glma/embedding/pipeline.py` — New file (core pipeline logic)
- `src/glma/embedding/__init__.py` — Updated exports
- `src/glma/cli.py` — Added embed command
- `tests/test_embedding_pipeline.py` — New file (13 tests)

## Test Results
- 13 pipeline tests pass (hash, batching, embed, skip, force, failure, dim mismatch)
- 333 total tests pass, 0 regressions

## Deviations
- Used typing.Callable instead of `callable | None` syntax for Python 3.9 compatibility
- Force mode uses separate get_all_chunks_with_summaries() DB query
- Test dimension values use 768 to match Ladybug FLOAT[768] schema constraint

## key-files
- created: ["src/glma/embedding/pipeline.py", "tests/test_embedding_pipeline.py"]
- modified: ["src/glma/embedding/__init__.py", "src/glma/cli.py"]
