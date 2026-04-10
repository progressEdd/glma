---
status: resolved
trigger: "ARCHITECTURE.md module grouping wrong, dependency graph empty, key interfaces empty, too many entry points"
created: 2026-04-10T23:15:00.000Z
updated: 2026-04-10T23:25:00.000Z
---

## Current Focus

hypothesis: Multiple issues in generate_architecture_md() and helpers — module grouping off-by-one, dependency computation only handles resolved edges, key interfaces only counts incoming direction
test: Run glma export on glma codebase and inspect ARCHITECTURE.md output
expecting: Correct module names, non-empty dependency graph, correct entry points
next_action: N/A — all fixed and verified

## Symptoms

expected: ARCHITECTURE.md shows db as module, dependency edges between modules, ~3 entry points, key interfaces like LadybugStore
actual: 23 modules (each file its own module), all deps "no external dependencies", every file an entry point, no key interfaces
errors: No runtime errors — just wrong output
reproduction: `glma index src/glma --lang python && glma export src/glma -o /tmp/test`
started: Always broken — first implementation

## Eliminated

- hypothesis: Relationship resolver is broken and needs fixing
  evidence: Resolver works correctly — it marks unresolved imports with source_id==target_id by design. The bug was in ARCHITECTURE.md not handling unresolved edges.
  timestamp: 2026-04-10T23:17:00Z

## Evidence

- timestamp: 2026-04-10T23:16:00Z
  checked: `_get_module_name()` with `db/store.py`
  found: Returns `store` (stem) instead of `db` (directory). Threshold was `>= 3` segments, needs `>= 2`.
  implication: Fix threshold to `>= 2`

- timestamp: 2026-04-10T23:17:00Z
  checked: Relationship data for `cli.py` — 157 relationships
  found: All imports unresolved (source_id == target_id). target_name is dotted path like `glma.db.ladybug_store`.
  implication: Must resolve using target_name, not just target_id

- timestamp: 2026-04-10T23:18:00Z
  checked: `_compute_key_interfaces()` counting logic
  found: Only counts `direction == "incoming"` which doesn't exist for unresolved imports
  implication: Must count from source side and match target_name to chunk names

- timestamp: 2026-04-10T23:19:00Z
  checked: `_detect_entry_points()` fan-in logic
  found: `has_incoming_imports` checks `direction == "incoming"` — always False. Every file has zero incoming → every file is entry point.
  implication: Pre-compute imported_files set from outgoing import names

## Resolution

root_cause: Three functions in export.py assumed resolved cross-file relationships (where source_id != target_id), but Python imports are mostly unresolved in glma. The code skipped all self-referential edges, losing the actual dependency data encoded in target_name.

fix: (1) Fixed _get_module_name threshold from >=3 to >=2. (2) Added _module_from_import_name() to resolve dotted import names to modules. (3) Module dependency loop now handles both resolved and unresolved edges. (4) Key interfaces counts from source side using target_name matching. (5) Entry point fan-in pre-computes imported_files set from outgoing import names.

verification: `glma export` on glma codebase produces correct modules (12 including db, index, query, summarize), dependency graph showing db as core dependency, 3 entry points (__main__.py, cli.py, export.py), and key interfaces including LadybugStore (3 files) and Language (6 files). 255/255 tests pass.

files_changed:
  - 02-worktrees/glma/src/glma/export.py
