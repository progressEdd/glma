# Phase 8: ARCHITECTURE.md & Export Polish - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-10
**Phase:** 08-architecture-md-export-polish
**Areas discussed:** Content structure, Module grouping, Entry point detection, Export integration

---

## Content Structure

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Narrative + tables | Sections with prose summaries assembled from DB data: project overview, directory tree, module descriptions, entry points, key interfaces, dependency adjacency | ✓ |
| Structured data only | Pure tables and lists — directory tree, file→module mapping, chunk counts, dependency matrix | |
| Layered (like query output) | Summary → module overview → details, mirroring glma's layered markdown pattern | |

**User's choice:** Narrative + tables
**Notes:** Reuse existing `chunk.summary` from DB — no new LLM calls at export time. If no AI summaries, fall back to `generate_rule_summary()`. User explicitly said "if the DB is already doing the generated summaries, there's no point to duplicate it, just reuse the already generated ones."

---

## Module Grouping Strategy

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Top-level directory | Group by first directory segment | |
| Directory + relationship density | Start with directory grouping, merge tightly-coupled dirs by cross-relationship count | ✓ |
| Import cluster analysis | Graph clustering on import/call relationships | |

**User's choice:** Directory + relationship density
**Notes:** Base grouping by directory segment, then merge groups with high inter-relationship density. Exact threshold left to agent's discretion.

---

## Entry Point Detection

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Convention-based | Detect `__main__.py`, `if __name__`, `cli.py`/`main.py` filenames | |
| Fan-in analysis | Files with zero incoming imports + outgoing relationships | |
| Convention + fan-in hybrid | Convention first, supplement with fan-in | ✓ |

**User's choice:** Convention + fan-in hybrid
**Notes:** Convention-based entries flagged as "detected entry point", fan-in entries flagged as "likely entry point".

---

## Export Integration

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Parallel to INDEX/RELATIONSHIPS | New `generate_architecture_md()`, always generated, no flag | ✓ |
| Behind a flag | New `--architecture` flag, only when requested | |

**User's choice:** Parallel to INDEX/RELATIONSHIPS
**Notes:** Consistent with existing pattern — INDEX.md and RELATIONSHIPS.md are always generated. No new CLI flags.

---

## Agent's Discretion

- Exact merge threshold for relationship density grouping
- Algorithm for computing relationship density between directory groups
- Exact formatting and section ordering within ARCHITECTURE.md
- Module dependency graph representation (adjacency table, Mermaid, bullet lists)
- What counts as a "key interface"
- Edge cases: flat structures, circular deps, orphaned files, very large codebases

## Deferred Ideas

None — discussion stayed within phase scope.
