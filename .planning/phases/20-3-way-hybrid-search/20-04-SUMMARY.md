---
phase: 20
plan: 04
status: complete
started: "2026-05-12"
completed: "2026-05-12"
tasks_total: 1
tasks_complete: 1
requirements: [HYBR-05]
key-files:
  created: []
  modified:
    - src/glma/cli.py
---

# Plan 04 — CLI Flags for Graph Search

## What Was Built

Added three new CLI flags to the `search` command: `--graph` (boolean toggle for 3-way hybrid), `--graph-depth` (max BFS traversal depth, default 2), `--graph-fanout` (number of seed chunks, default 10). Graph depth and fanout are wired through config overrides. The `--graph` flag is threaded to both `engine.search(graph=graph)` and `format_search_output(graph_enabled=graph)`.

## Task Summary

| Task | Description | Status |
|------|-------------|--------|
| 1 | Add graph CLI flags and wire them through | ✓ Complete |

## Decisions

- `--graph` is a boolean toggle, not a weight setter — weights come from config file defaults
- `--graph-depth` and `--graph-fanout` are optional overrides (None by default, uses config values)
- No `--graph-weight` CLI flag — weight tuning is intentionally config-file only to prevent CLI overload

## Self-Check: PASSED
