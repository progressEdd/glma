---
phase: 16-pipeline-reliability
plan: 03
subsystem: pipeline
tags: [resume, stage-tracking, incremental-indexing]

requires:
  - plan: 16-01
    provides: New chunk ID format with content hash
  - plan: 16-02
    provides: Pipeline stage tracking on File nodes
provides:
  - Resume-safe pipeline that skips completed stages on re-run
  - Per-file stage updates after each processing pass
affects: [cli]

tech-stack:
  added: []
  patterns: ["Resume: query file stages, include incomplete files in appropriate pass"]

key-files:
  created: []
  modified:
    - src/glma/index/pipeline.py

key-decisions:
  - "Content hash changes override stage — changed files always re-processed from scratch"
  - "Resume files aggregated from DB stage query, not in-memory state"

patterns-established:
  - "Resume from interrupt: files at 'chunked' stage join Pass 2, files at 'relationships_extracted' join Pass 3"

requirements-completed: [PIPE-02, PIPE-03]

duration: 10min
completed: 2026-05-12
---

# Phase 16 Plan 03: Resume-Safe Pipeline Summary

**Pipeline now resumes from first incomplete stage — re-running glma index skips completed work**

## Performance

- **Duration:** 10 min
- **Tasks:** 1
- **Files modified:** 1

## Accomplishments
- Added file_stages dict from DB query at pipeline start
- Pass 1 sets "chunked" stage after processing each file
- Pass 2 sets "relationships_extracted" after processing each file
- Pass 3 sets "complete" after final markdown write
- Resume logic includes files at "chunked" stage in Pass 2 and "relationships_extracted" in Pass 3
- Content hash changes override stage — changed files always start from scratch

## Task Commits

1. **Task 3.1: Add resume logic to run_index()** - `7a81fca` (feat)

## Files Created/Modified
- `src/glma/index/pipeline.py` - Resume logic, stage tracking, shutdown_event parameter

## Decisions Made
- Content hash comparison takes priority over stage — ensures stale data is never served
- File stages queried once at start, not per-file (reduces DB queries)

## Deviations from Plan
None — plan executed exactly as written.

## Issues Encountered
None.

## Next Phase Readiness
- Pipeline stages are set correctly for resume
- shutdown_event parameter added for Plan 04 (graceful shutdown)

---
*Phase: 16-pipeline-reliability*
*Completed: 2026-05-12*
