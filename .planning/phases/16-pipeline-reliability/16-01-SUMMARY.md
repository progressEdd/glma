---
phase: 16-pipeline-reliability
plan: 01
subsystem: indexing
tags: [chunks, content-hash, blake2b, collision-prevention]

requires: []
provides:
  - Chunk IDs with content hash suffix preventing collisions from C macros and forward declarations
affects: [pipeline, writer, store, embedding]

tech-stack:
  added: []
  patterns: ["Chunk ID format: {file_path}::{name}::{start_line}::{hash8}"]

key-files:
  created: []
  modified:
    - src/glma/index/chunks.py
    - src/glma/models.py
    - src/glma/index/writer.py
    - src/glma/db/ladybug_store.py

key-decisions:
  - "Drop chunk_type from ID — name+line+hash provides sufficient uniqueness"
  - "Compute content_hash once in _walk_chunks and reuse for both ID and Chunk model"

patterns-established:
  - "Content hash in chunk IDs: prevents collisions from C macros/forward declarations"

requirements-completed: [PIPE-01]

duration: 5min
completed: 2026-05-12
---

# Phase 16 Plan 01: Chunk ID Hash Suffix Summary

**Chunk IDs now include 8-char BLAKE2b content hash suffix — prevents collisions from C macros and forward declarations**

## Performance

- **Duration:** 5 min
- **Tasks:** 2
- **Files modified:** 4

## Accomplishments
- Changed chunk ID format from `{file_path}::{chunk_type}::{name}::{start_line}` to `{file_path}::{name}::{start_line}::{hash8}`
- Content hash computed once and reused for both ID and Chunk model field
- Fixed writer.py parent name extraction for new format (index 1 instead of 2)
- Updated all docstrings referencing old format

## Task Commits

1. **Task 1.1: Update _chunk_id()** - `f140f6b` (feat)
2. **Task 1.2: Verify SQL queries** - no changes needed (IDs are opaque strings in DB)

## Files Created/Modified
- `src/glma/index/chunks.py` - Changed _chunk_id() signature and _walk_chunks() call site
- `src/glma/models.py` - Updated Chunk.id field description
- `src/glma/index/writer.py` - Fixed parent name extraction from new ID format
- `src/glma/db/ladybug_store.py` - Updated docstrings

## Decisions Made
- Dropped chunk_type from ID — name+line+hash provides sufficient uniqueness without it
- Used 8-char hash prefix (64-bit entropy) — collision probability negligible for any codebase

## Deviations from Plan
None — plan executed exactly as written.

## Issues Encountered
- Writer extracted parent name at wrong index after format change — caught by test, fixed immediately.

## Next Phase Readiness
- New chunk ID format is backward-incompatible — requires re-index of existing databases
- All 393 tests pass with new format

---
*Phase: 16-pipeline-reliability*
*Completed: 2026-05-12*
