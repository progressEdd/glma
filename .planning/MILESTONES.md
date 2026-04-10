# Milestones

## v1.0 — Initial Release

**Completed:** 2026-04-10
**Duration:** ~3.5 hours execution across 4 phases, 12 plans
**Status:** tech_debt (all requirements satisfied, accumulated tech debt tracked)

### What Shipped

A CLI tool that indexes codebases (C + Python) into a Ladybug graph database, extracts structural relationships, and outputs agent-readable markdown — both as a live queryable index and as static air-gapped exports.

### Key Accomplishments

- **4 CLI commands:** `glma index`, `glma query`, `glma watch`, `glma export`
- **Core indexing pipeline:** Tree-sitter parsing → chunk extraction → comment attachment → Ladybug store → markdown output
- **Relationship extraction:** Function calls, imports, inheritance, includes with confidence tagging (DIRECT/INFERRED)
- **Cross-file resolution:** 3-pass pipeline for incoming relationships, import alias resolution, self.method() resolution
- **Query tool:** Layered markdown (summary → signatures → full code), BFS depth traversal, JSON output
- **Notebook compaction:** Per-statement variable tracking, cross-cell flow table, nbformat-based .ipynb parsing
- **File watching:** watchfiles async loop, incremental re-indexing, rename detection
- **Air-gapped export:** Per-file markdown + INDEX.md + RELATIONSHIPS.md, directory/tar.gz/stdout modes
- **211 tests passing**, all integration flows verified

### Stats

| Metric | Value |
|--------|-------|
| Phases | 4 |
| Plans | 12 |
| Tests | 211 |
| Requirements | 42/42 satisfied |
| CLI commands | 4 |
| Languages supported | 2 (C, Python) |
| Export modes | 3 (directory, tar.gz, stdout) |

### Known Tech Debt

1. Stale "Phase 3 placeholder" in writer.py:274 — file summaries show "not yet generated"
2. ExportConfig.include_code defaults to True (should be False)
3. Notebook cell source truncation (list comprehensions stripped)
4. No VERIFICATION.md for phases 2-4
5. AI summaries only at file level, not per-chunk
6. No architecture summary file in exports
7. REQUIREMENTS.md checkboxes never updated

### Files Archived

- `.planning/milestones/v1.0-ROADMAP.md`
- `.planning/milestones/v1.0-REQUIREMENTS.md`
