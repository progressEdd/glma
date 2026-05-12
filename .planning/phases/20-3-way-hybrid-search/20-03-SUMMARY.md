---
phase: 20
plan: 03
status: complete
started: "2026-05-12"
completed: "2026-05-12"
tasks_total: 1
tasks_complete: 1
requirements: [HYBR-06]
key-files:
  created: []
  modified:
    - src/glma/search/formatter.py
---

# Plan 03 — Score Breakdown in Search Output

## What Was Built

Added `graph_enabled: bool = False` parameter to all four format functions (markdown, kv, json, yaml) and the dispatch function. When `graph_enabled=True`: markdown adds `> *Scores: graph=X.XX, keyword=X.XX, vector=X.XX, combined=X.XX*` annotation; kv adds `graph_score:`, `keyword_score:`, `vector_score:` lines; JSON/YAML conditionally include `graph` key in scores dict. When `graph_enabled=False`, output matches v1.3 format exactly.

## Task Summary

| Task | Description | Status |
|------|-------------|--------|
| 1 | Add graph_enabled parameter to format functions | ✓ Complete |

## Decisions

- Backward-compatible: default `graph_enabled=False` preserves v1.3 output format
- JSON/YAML use conditional dict merge `**({"graph": ...} if graph_enabled else {})` for clean key insertion
- All five functions consistently use the same parameter name and default

## Self-Check: PASSED
