---
phase: 04-file-watching-air-gapped-export
plan: 01
subsystem: watch
tags: [watchfiles, async, file-watching, incremental-indexing, event-batching]

requires:
  - phase: 03-query-tool-notebook-compaction
    provides: Indexing pipeline, LadybugStore, CLI framework
provides:
  - File watching with watchfiles async loop
  - Incremental re-indexing (changed_files/deleted_paths pipeline params)
  - Event classification and rename detection
  - WatchConfig model and config loading
  - glma watch CLI command
affects: [export, pipeline]

tech-stack:
  added: [watchfiles>=1.0]
  patterns: [async-watcher-loop, event-batching, basename-rename-heuristic]

key-files:
  created:
    - 02-worktrees/glma/src/glma/watch.py
    - 02-worktrees/glma/tests/test_watch.py
  modified:
    - 02-worktrees/glma/src/glma/models.py
    - 02-worktrees/glma/src/glma/config.py
    - 02-worktrees/glma/src/glma/index/pipeline.py
    - 02-worktrees/glma/src/glma/cli.py
    - 02-worktrees/glma/pyproject.toml

key-decisions:
  - "watchfiles for async file watching (awatch batches events at OS level)"
  - "Same-basename heuristic for rename detection in batch window"
  - "Pipeline accepts changed_files/deleted_paths to skip full directory walk"
  - "Pass 3 processes dependent files (files whose chunks reference changed file chunks)"

patterns-established:
  - "Incremental pipeline: run_index() with changed_files parameter skips walk_source_files()"
  - "Config pattern: WatchConfig/ExportConfig models with load_*_config() functions"

requirements-completed: [WTCH-01, WTCH-02, WTCH-03, CLIF-03]

duration: 10min
completed: 2026-04-09
---

# Plan 04-01: File Watcher with Incremental Re-Indexing Summary

**Async file watcher with watchfiles, event batching, rename detection, and incremental pipeline re-indexing**

## Performance

- **Duration:** 10 min
- **Tasks:** 4
- **Files modified:** 5 created/modified

## Accomplishments
- `glma watch /path/to/repo` starts async file watching loop
- File changes (create, modify, delete) trigger incremental re-indexing of only affected files
- Rename detection via same-basename heuristic in batch window
- Extended run_index() with changed_files and deleted_paths parameters for incremental mode

## Task Commits

1. **Task 1: Add watchfiles dep and config models** - `3dfbde4` (feat)
2. **Task 2: Create watch module** - `6351426` (feat)
3. **Task 3: Register glma watch CLI command** - `0a149b2` (feat)
4. **Task 4: Write tests** - `86ef485` (test)

## Files Created/Modified
- `src/glma/watch.py` - Async file watching with event batching and rename detection
- `tests/test_watch.py` - 15 unit tests for event classification, rename detection, CLI
- `src/glma/models.py` - Added WatchConfig model
- `src/glma/config.py` - Added load_watch_config() function
- `src/glma/index/pipeline.py` - Extended run_index() with changed_files/deleted_paths, changed_relative_paths tracking
- `src/glma/cli.py` - Added watch CLI command with asyncio.run()
- `pyproject.toml` - Added watchfiles>=1.0 dependency

## Decisions Made
- watchfiles provides awatch async generator that naturally batches events at OS level
- Rename detection uses same-basename heuristic (fast, good for most IDE/file-manager renames)
- Pipeline tracks changed_relative_paths set for targeted Pass 2/3 processing
- Pass 3 also processes dependent files that reference changed file chunks

## Deviations from Plan
None - plan executed exactly as written.

## Issues Encountered
None.

## Next Phase Readiness
- Watch infrastructure complete, ready for export feature (Plan 04-02)
- WatchConfig model pattern established for ExportConfig to follow

---
*Phase: 04-file-watching-air-gapped-export*
*Completed: 2026-04-09*
