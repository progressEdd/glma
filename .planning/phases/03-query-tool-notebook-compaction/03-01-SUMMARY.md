---
plan: 03-01
phase: 03-query-tool-notebook-compaction
status: complete
completed: 2026-04-09
---

# Plan 03-01: CLI Query Command, File Lookup, Layered Markdown Formatting

## Result

Built the core `glma query <filepath>` command with compact layered markdown output.

## What was built

- **LadybugStore query methods**: `get_file_record()`, `get_chunks_for_file()`, `get_all_relationships_for_file()` — reusable read-only query methods on the store
- **Query formatter** (`glma/query/formatter.py`): Compact layered markdown with Summary → Signatures → Full Code sections. Relationship hints on signatures (`→ calls: func1, func2`)
- **CLI query command**: `glma query <filepath>` with `--verbose`, `--output`, `--repo` flags
- **Semantic exit codes**: 1=not found, 2=not indexed, 3=stale, 4=query error
- **Error handling**: Errors to stderr, output to stdout (pipe-friendly)

## Key files created/modified

- `src/glma/query/__init__.py` — new module
- `src/glma/query/formatter.py` — compact layered markdown formatter
- `src/glma/db/ladybug_store.py` — 3 new query methods
- `src/glma/cli.py` — query command with error handling
- `src/glma/index/pipeline.py` — delegate to store.get_chunks_for_file()
- `tests/test_query_formatter.py` — 4 formatter tests

## Decisions

- Query output is generated fresh from DB queries, not by slicing existing per-file markdown
- Relationship hints use `→ rel_type: target1, target2` format for compact readability
- Stale index is a warning (exit 3) not an error — still shows output

## Self-Check: PASSED
