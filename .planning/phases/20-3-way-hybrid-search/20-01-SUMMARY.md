---
phase: 20
plan: 01
status: complete
started: "2026-05-12"
completed: "2026-05-12"
tasks_total: 3
tasks_complete: 3
requirements: [HYBR-04]
key-files:
  created: []
  modified:
    - src/glma/models.py
    - src/glma/db/ladybug_store.py
---

# Plan 01 — Config & Data Layer for 3-Way Hybrid Search

## What Was Built

Extended `SearchConfig` with three new graph search fields (`graph_weight`, `graph_depth`, `graph_fanout`) and updated the hybrid weight validator to enforce 3-way summing to ~1.0. Added `get_chunks_by_ids()` batch lookup method to `LadybugStore` for fetching graph-discovered chunk metadata. Verified config loader already handles the new fields via generic merge pattern.

## Task Summary

| Task | Description | Status |
|------|-------------|--------|
| 1 | Extend SearchConfig with graph fields and 3-way weight validator | ✓ Complete |
| 2 | Add batch chunk lookup method to LadybugStore | ✓ Complete |
| 3 | Update config loader to pass through graph CLI overrides | ✓ Complete (no changes needed) |

## Decisions

- Default weights: 0.3 keyword + 0.3 vector + 0.4 graph = 1.0 (graph gets highest weight as differentiator)
- `get_chunks_by_ids` uses MATCH query with parameterized IN clause for batch efficiency
- Config merge pattern already handles new fields — no config.py changes needed

## Self-Check: PASSED
