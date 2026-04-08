---
plan: "01-04"
phase: "01-core-indexing-pipeline"
status: complete
wave: 4
started: "2026-04-08T23:00:00Z"
completed: "2026-04-08T23:25:00Z"
---

# Summary: Plan 01-04 — Content Hashing, Incremental Re-Indexing, Integration

## Objective
Wire up the full indexing pipeline end-to-end: connect walker → detector → parser → chunk extractor → comment attacher → DB store → markdown writer. Add content hashing for incremental re-indexing. Update the CLI to invoke the pipeline. Write integration tests.

## What Was Built
- Full pipeline orchestration (`pipeline.py`) with `run_index()` function implementing: walk → hash → skip unchanged → parse → extract → attach → store → write markdown
- `IndexResult` class tracking: total_files, new_files, updated_files, skipped_files, deleted_files, total_chunks
- Content hashing with BLAKE2b (digest_size=32)
- Incremental re-indexing: unchanged files skipped, modified files re-parsed, deleted files cleaned from DB and markdown
- CLI wired to pipeline: `glma index /path` now runs the full pipeline
- 116 total tests passing including:
  - 11 incremental re-indexing tests (cold start, no-change skip, update, delete, add)
  - 15 integration tests with multi-file project

## Key Decisions
- **Markdown filename includes extension**: `sample.c.md` and `sample.py.md` to avoid collision when same-stem files exist in same directory
- **upsert_file uses DETACH DELETE on chunks first**: File nodes have CONTAINS edges to Chunks, so regular DELETE fails. Now deletes chunks first, then file.
- **DB path is file-based**: `index.lbug` inside `.glma-index/db/` directory, consistent with Ladybug requiring file path not directory
- **Streaming pipeline**: One file at a time, no accumulation of parse trees in memory

## Deviations
- Plan specified `stem + ".md"` for markdown filenames; changed to `name + ".md"` (includes extension) to prevent collisions
- Plan specified `.glma-index/db/` directory for DB; actual path is `.glma-index/db/index.lbug` file

## Bugs Fixed
- `upsert_file` originally used `DELETE` which failed with connected CONTAINS edges → fixed with chunk cleanup first
- `.gitignore` appended `.glma-index/` without proper separation → fixed

## key-files.created
- `02-worktrees/glma/src/glma/index/pipeline.py`
- `02-worktrees/glma/tests/test_incremental.py`
- `02-worktrees/glma/tests/test_pipeline.py`
- `02-worktrees/glma/tests/integration/__init__.py`
- `02-worktrees/glma/tests/integration/test_full_index.py`

## Self-Check: PASSED
- [x] All 5 tasks executed
- [x] Each task committed individually
- [x] 116/116 tests passing (full suite)
- [x] `glma index tests/fixtures/` runs without error
- [x] Re-running skips unchanged files
- [x] Modified files re-indexed with updated hash
- [x] Deleted files cleaned from DB and markdown
- [x] New files indexed and added to DB
- [x] Integration test covers multi-file project with .git, venv, node_modules exclusion
