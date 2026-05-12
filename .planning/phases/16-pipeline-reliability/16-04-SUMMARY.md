---
phase: 16-pipeline-reliability
plan: 04
subsystem: cli
tags: [signal-handling, graceful-shutdown, SIGINT, SIGTERM]

requires:
  - plan: 16-02
    provides: Pipeline stage tracking
  - plan: 16-03
    provides: shutdown_event parameter in pipeline
provides:
  - Graceful shutdown on SIGINT/SIGTERM — finishes current file, exits cleanly
affects: [pipeline, cli]

tech-stack:
  added: []
  patterns: ["threading.Event for shutdown signaling", "Double-signal force exit"]

key-files:
  created: []
  modified:
    - src/glma/cli.py
    - src/glma/index/pipeline.py

key-decisions:
  - "First Ctrl+C waits for current file, second Ctrl+C force-exits"
  - "Summarization skipped on interrupt — avoids partial LLM calls"

patterns-established:
  - "Signal handler pattern: threading.Event checked at loop boundaries"

requirements-completed: [PIPE-04]

duration: 5min
completed: 2026-05-12
---

# Phase 16 Plan 04: Graceful Shutdown Summary

**SIGINT/SIGTERM handlers enable clean shutdown — finishes current file, prints resume hint**

## Performance

- **Duration:** 5 min
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments
- Signal handlers registered at CLI entry using threading.Event
- First Ctrl+C sets event, prints "Finishing current file..."
- Second Ctrl+C force-exits with code 1
- Pipeline checks shutdown_event at start of each pass loop
- On interrupt, prints count of remaining files with resume hint
- Summarization skipped if interrupted during indexing

## Task Commits

1. **Task 4.1: Add shutdown_event to run_index()** - `7a81fca` (feat)
2. **Task 4.2: Register signal handlers in CLI** - `25e34be` (feat)

## Files Created/Modified
- `src/glma/index/pipeline.py` - Shutdown checks in all 3 pass loops
- `src/glma/cli.py` - Signal handler registration, interrupt check before summarization

## Decisions Made
- threading.Event over direct flag — thread-safe, no race conditions
- Skip summarization on interrupt — avoids wasted LLM API calls for incomplete data

## Deviations from Plan
None — plan executed exactly as written.

## Issues Encountered
None.

## Next Phase Readiness
- Shutdown event also checked in summarization loop (Plan 05)
- Clean shutdown ensures no partial DB writes

---
*Phase: 16-pipeline-reliability*
*Completed: 2026-05-12*
