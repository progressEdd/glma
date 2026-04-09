---
plan: 02-03
phase: 02-relationship-extraction
status: complete
started: "2026-04-09T13:00:00Z"
completed: "2026-04-09T13:45:00Z"
---

# SUMMARY: Plan 02-03

## Objective
Integrate relationship extraction into the pipeline, add confidence tagging, update markdown output with relationship sections, and handle cross-file resolution.

## What was built
- **Pipeline 3-pass architecture**: Pass 1 (chunk extraction + store), Pass 2 (relationship extraction for changed files + markdown with relationships), Pass 3 (cross-file incoming relationships + final markdown rewrite)
- **Markdown relationship output**: Inline per-chunk `> **Calls:**` and `> **Called by:**` annotations, plus `## Relationships` summary section with tables for Outgoing Calls, Incoming Calls, Imports, Includes, and Inherits
- **Cross-file resolution**: Pass 3 queries incoming relationships from other files and includes them in markdown
- **Incremental re-indexing**: Changed files get relationship refresh, unchanged files skipped, deleted files cleaned up
- **IndexResult.total_relationships**: Tracks total relationships extracted

## Key Decisions
- Three-pass pipeline ensures cross-file resolution works (all chunks must be in DB first)
- Empty relationship sections omitted from markdown (no empty ### Inherits heading)
- Unresolved targets display as `? (name)` in both inline and summary
- Deleted files have relationships cleaned via delete_relationships before delete_file

## Files Modified
- `src/glma/index/pipeline.py` — Added Pass 2 (relationships), Pass 3 (cross-file), _load_chunks_from_store
- `src/glma/index/writer.py` — Added relationships parameter, inline formatting, summary tables

## Files Created
- `tests/test_writer_rels.py` — 8 tests for markdown relationship output
- `tests/integration/test_full_index.py` — 6 new integration tests

## Test Results
- 157 tests passing (143 previous + 14 new)

## key-files
### created
- tests/test_writer_rels.py

### modified
- src/glma/index/pipeline.py
- src/glma/index/writer.py
- tests/integration/test_full_index.py
