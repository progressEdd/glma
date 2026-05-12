---
plan: 19-02
phase: 19-llm-query-rewriting
status: complete
started: "2026-05-12"
completed: "2026-05-12"
requirements: [REWR-04]
key-files:
  modified:
    - src/glma/search/formatter.py
    - tests/test_search.py
---

# Plan 02 Summary — Formatter Query Header Support

## What Was Built

- Added `original_query` and `rewritten_query` optional parameters to all 5 formatter functions:
  - `format_search_markdown`, `format_search_kv`, `format_search_json`, `format_search_yaml`, `format_search_output`
- Markdown/KV: display `# Query: "..."` and `# Rewritten: "..."` header when params provided
- JSON/YAML: include `original_query` and `rewritten_query` fields in output data
- Raw mode shows `(raw)` label when only original_query provided
- 8 new tests covering headers for all formats plus backward compatibility

## Deviations

None. All tasks implemented as planned.

## Verification

```
52 tests pass in test_search.py (8 new)
All existing formatter tests pass unchanged
```
