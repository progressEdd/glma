# Phase 8: ARCHITECTURE.md & Export Polish - Context

**Gathered:** 2026-04-10
**Status:** Ready for planning

<domain>
## Phase Boundary

Generate a codebase-level `ARCHITECTURE.md` derived from relationship data and summaries already in the Ladybug DB, and include it in all export outputs. This file gives consuming agents instant high-level understanding of the indexed codebase without needing to piece it together from INDEX.md + RELATIONSHIPS.md + individual per-file markdown. No new LLM calls at export time — compose from what's already stored. No new CLI flags — ARCHITECTURE.md is always generated alongside INDEX.md and RELATIONSHIPS.md.

</domain>

<decisions>
## Implementation Decisions

### ARCHITECTURE.md Content Structure
- **D-01:** Narrative + tables format — structured sections with descriptive text assembled from DB data, not pure data tables (which RELATIONSHIPS.md already provides).
- **D-02:** Sections: project structure overview, module dependency graph, entry points, key interfaces. These are the four required sections derived from DB data.
- **D-03:** Reuse existing `chunk.summary` from DB (populated by `glma index --summarize`). No new LLM generation at export time. If no AI summaries exist, fall back to rule-based summaries via `generate_rule_summary()` — same pattern as existing export.
- **D-04:** Per-module narrative descriptions are assembled from the summaries of chunks within that module. Not free-text LLM output — composed from structured data.

### Module Grouping Strategy
- **D-05:** Top-level directory segments as base grouping (e.g., `src/glma/db/` → module "db", `src/glma/index/` → module "index").
- **D-06:** Merge tightly-coupled directories into single modules based on cross-relationship density. If two directory groups have high inter-module relationship counts, they're treated as one conceptual module. The exact merge threshold is agent's discretion.

### Entry Point Detection
- **D-07:** Hybrid approach: convention checks first, then fan-in analysis to supplement.
- **D-08:** Convention checks: `__main__.py` files, `if __name__ == "__main__"` blocks, `cli.py` / `main.py` filenames.
- **D-09:** Fan-in analysis: files with zero incoming imports that have outgoing relationships → likely entry points.
- **D-10:** Convention-based entries flagged as "detected entry point", fan-in entries flagged as "likely entry point" in the output.

### Export Pipeline Integration
- **D-11:** ARCHITECTURE.md generated unconditionally alongside INDEX.md and RELATIONSHIPS.md — always present in export output, no CLI flag.
- **D-12:** New `generate_architecture_md()` function in `export.py`, following the same pattern as `generate_index_md()` and `generate_relationships_md()`.
- **D-13:** Wired into both `_write_files_to_dir()` and `_write_tar_to_stream()` — all three export modes (directory, tar.gz, stdout) include ARCHITECTURE.md.

### Folded Todos
- **Generate codebase architecture summary file** — core Phase 8 deliverable: ARCHITECTURE.md with project structure, module grouping, entry points, key interfaces

### Agent's Discretion
- Exact merge threshold for directory + relationship density grouping
- The algorithm for computing relationship density between directory groups
- Exact formatting and section ordering within ARCHITECTURE.md
- How to represent the module dependency graph (adjacency table, Mermaid diagram, bullet lists)
- What counts as a "key interface" (top-level exports? classes with many dependents?)
- How to handle flat file structures (no subdirectories — single module?)
- Edge cases: circular dependencies, orphaned files, very large codebases

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Export pipeline (modification targets)
- `02-worktrees/glma/src/glma/export.py` — Full export module: `export_index()` orchestrator, `generate_index_md()`, `generate_relationships_md()`, `_write_files_to_dir()`, `_write_tar_to_stream()`. New `generate_architecture_md()` goes here alongside the existing root file generators.
- `02-worktrees/glma/src/glma/cli.py` — Export command registration. No flag changes needed for this phase, but reference for how export is invoked.

### Data sources (what ARCHITECTURE.md derives from)
- `02-worktrees/glma/src/glma/db/ladybug_store.py` — `get_indexed_files()`, `get_file_record()`, `get_chunks_for_file()`, `get_file_relationships()` — all the read queries needed to assemble architecture data.
- `02-worktrees/glma/src/glma/models.py` — `Chunk`, `FileRecord`, `ChunkType`, `ExportConfig` models.
- `02-worktrees/glma/src/glma/summaries.py` — `generate_rule_summary()` for fallback summaries when no AI summaries exist.

### Existing root files (consistency reference)
- `02-worktrees/glma/src/glma/export.py` §`generate_index_md()` — File listing + statistics format. ARCHITECTURE.md should complement, not duplicate.
- `02-worktrees/glma/src/glma/export.py` §`generate_relationships_md()` — Cross-file dependency table format. ARCHITECTURE.md adds higher-level module view on top of this.

### Tests
- `02-worktrees/glma/tests/test_export.py` — Existing export tests. New tests for ARCHITECTURE.md generation follow this pattern.

### Project context
- `.planning/codebase/CONVENTIONS.md` — Typer CLI pattern, Pydantic config models, Rich console
- `.planning/codebase/STRUCTURE.md` — Source in `02-worktrees/glma/src/glma/`

### Prior phase decisions
- `.planning/phases/04-file-watching-air-gapped-export/04-CONTEXT.md` — Export design: three output modes, INDEX.md + RELATIONSHIPS.md structure, rule-based summaries
- `.planning/phases/07-cli-integration-providers/07-CONTEXT.md` — Chunk summaries in DB as single source of truth, blockquote rendering pattern across all output paths

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`generate_index_md()`** (`export.py`): Already collects file data into `file_data` dict with `record`, `chunks`, `relationships`, `summary` per file. ARCHITECTURE.md generator receives this same dict — no new data loading needed.
- **`generate_relationships_md()`** (`export.py`): Already computes cross-file relationships and per-file dependency summaries (imports_from, imported_by, calls_to, called_by). The module grouping logic can reuse this cross-file relationship extraction.
- **`generate_rule_summary()`** (`summaries.py`): Fallback for modules/files without AI summaries. Lists functions, classes, imports deterministically.
- **`file_data` dict** (built in `export_index()`): The central data structure — `{path: {"record", "chunks", "relationships", "summary"}}` — already assembled before any root file generation. ARCHITECTURE.md generator gets this for free.

### Established Patterns
- **Root file generators**: `generate_*_md()` functions take data dicts and return markdown strings. Called from `export_index()`, passed to `_write_files_to_dir()` / `_write_tar_to_stream()`.
- **Timestamp headers**: Both INDEX.md and RELATIONSHIPS.md include `**Generated:** {ISO timestamp}`. ARCHITECTURE.md should follow this pattern.
- **Relationship resolution**: Self-referential edges (source_id == target_id) represent unresolved targets. Already handled in `_resolve_target_display()` in writer.py — same logic needed for entry point fan-in analysis.

### Integration Points
- **`export_index()`** (`export.py`): After building `file_data` and generating `index_md` + `rels_md`, add `arch_md = generate_architecture_md(file_data)` and pass to writers.
- **`_write_files_to_dir()`**: Add `(output_dir / "ARCHITECTURE.md").write_text(arch_md, encoding="utf-8")` alongside INDEX.md and RELATIONSHIPS.md writes.
- **`_write_tar_to_stream()`**: Add ARCHITECTURE.md tar entry alongside existing INDEX.md and RELATIONSHIPS.md entries.

</code_context>

<specifics>
## Specific Ideas

- ARCHITECTURE.md should feel like the "readme for agents" — the one file an AI agent reads first to understand how the codebase is organized before diving into specifics.
- The module dependency graph section is the key differentiator from RELATIONSHIPS.md. Where RELATIONSHIPS.md shows every edge, ARCHITECTURE.md shows "these 4 modules exist, here's how they depend on each other at a high level."
- Reusing existing summaries means: if a user ran `glma index --summarize`, ARCHITECTURE.md gets rich AI-powered module descriptions. If they didn't, it gets rule-based "3 functions, 1 class" summaries. Both are useful.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

### Reviewed Todos (not folded)
The following todos matched Phase 8 but belong to completed phases (5-7):
- **Default markdown export to summaries only** — completed in Phase 5 (FIX-01)
- **Fix notebook cell source truncation in compaction** — completed in Phase 5 (FIX-02)
- **Replace stale Phase 3 placeholder in writer markdown** — completed in Phase 5 (FIX-03)
- **Per-chunk AI summaries from local LLM** — completed in Phase 6-7 (SUMM-01, SUMM-02, SUMM-03)
- **Pi/agent integration for code summarization** — completed in Phase 7 (PROV-03)

</deferred>

---

*Phase: 08-architecture-md-export-polish*
*Context gathered: 2026-04-10*
