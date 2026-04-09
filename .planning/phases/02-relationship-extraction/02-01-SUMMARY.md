---
plan: 02-01
phase: 02-relationship-extraction
status: complete
started: "2026-04-09T12:00:00Z"
completed: "2026-04-09T12:30:00Z"
---

# SUMMARY: Plan 02-01

## Objective
Add relationship data model, Ladybug RELATES_TO edge table, and C relationship extraction from tree-sitter ASTs.

## What was built
- **RelType enum**: CALLS, IMPORTS, INHERITS, INCLUDES (4 relationship types)
- **Confidence enum**: DIRECT, INFERRED (2 confidence levels)
- **Relationship Pydantic model**: source_id, target_id, target_name, rel_type, confidence, source_line
- **RELATES_TO edge table** in LadybugStore with full CRUD: upsert_relationships, delete_relationships, get_outgoing_relationships, get_incoming_relationships, get_file_relationships
- **LanguageConfig extensions**: call_node_type, import_node_type, inherit_node_type fields for both C and Python
- **C relationship extraction**: function call resolution (DIRECT for same-file, INFERRED for unresolved), #include resolution (DIRECT for local indexed headers, INFERRED for system headers)

## Key Decisions
- Unresolved targets stored as self-referential edges (source → source) with target_name capturing the unresolved callee name
- Module-level calls (no enclosing function) are skipped
- C has no inheritance, so inherit_node_type is empty string

## Files Modified
- `src/glma/models.py` — Added RelType, Confidence, Relationship
- `src/glma/db/ladybug_store.py` — Added RELATES_TO schema + 5 CRUD methods
- `src/glma/index/parser.py` — Extended LanguageConfig with 3 new fields
- `src/glma/index/relationships.py` — New: C relationship extraction module

## Files Created
- `src/glma/index/relationships.py`
- `tests/test_relationships_c.py` — 5 tests for C relationship extraction
- `tests/test_store_rels.py` — 5 tests for relationship CRUD

## Test Results
- 126 tests passing (116 existing + 10 new)
- All acceptance criteria met

## key-files
### created
- src/glma/index/relationships.py
- tests/test_relationships_c.py
- tests/test_store_rels.py

### modified
- src/glma/models.py
- src/glma/db/ladybug_store.py
- src/glma/index/parser.py
