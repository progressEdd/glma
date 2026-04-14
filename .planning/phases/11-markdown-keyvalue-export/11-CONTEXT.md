# Phase 11: Markdown Key-Value Export Format - Context

**Gathered:** 2026-04-14
**Status:** Ready for planning

<domain>
## Phase Boundary

`glma export` outputs a compact, LLM-friendly key-value markdown format by default, with option to select other formats (markdown tables, json, yaml). Adds `ExportFormat` enum, shared `--format` flag across export and query commands, and a `FormatRenderer` strategy pattern for format routing. All output files respect the selected format. No new CLI commands, no schema changes, no new data — purely a formatting layer on top of existing export data.

</domain>

<decisions>
## Implementation Decisions

### KV Format Structure
- **D-01:** Flat inline style matching the todo reference — chunk name as `## heading`, followed by `key: value` lines for metadata (type, lines, summary, calls, imports, etc.).
- **D-02:** Relationships rendered as comma-separated target names under single keys: `calls: load_config, run_index, summarize_chunks`. No confidence levels, no line numbers, no sub-headings in KV per-file output.
- **D-03:** Full relationship detail (confidence, line numbers, direction) stays in the consolidated root file (CODEBASE.md in KV mode) or RELATIONSHIPS.md (in markdown mode). Per-file KV is maximally compact.

### Root File Rendering
- **D-04:** In KV format, consolidate INDEX.md + ARCHITECTURE.md + RELATIONSHIPS.md into a single `CODEBASE.md`. These three files overlap significantly (all describe files, modules, and their relationships). One file eliminates duplication.
- **D-05:** In markdown format (existing), keep INDEX.md + ARCHITECTURE.md + RELATIONSHIPS.md unchanged — backward compatible.
- **D-06:** In json/yaml formats, root file structure is agent's discretion (single object or separate keys).

### Backward Compatibility
- **D-07:** Shared `--format` / `-f` flag across both `glma export` and `glma query` commands, backed by a single `ExportFormat` enum with values: `markdown_kv`, `markdown`, `json`, `yaml`.
- **D-08:** `glma export` defaults to `markdown_kv`. `glma query` defaults to `markdown` (preserving current behavior).
- **D-09:** `glma query` gains `yaml` as a new format option alongside existing `markdown`/`json`.

### Format Routing Architecture
- **D-10:** Strategy pattern — a `FormatRenderer` protocol (or abstract base) with per-format implementations. Each format has its own renderer class implementing methods for per-file rendering and root file rendering.
- **D-11:** `export_index()` selects the appropriate renderer based on `ExportConfig.format` and delegates all formatting to it.
- **D-12:** Existing `_format_export_file()` logic becomes the markdown renderer implementation. No duplication.

### Folded Todos
- **Add markdown key-value export format as default with multi-format support** — core Phase 11 deliverable: ExportFormat enum, KV formatter, strategy routing, consolidated CODEBASE.md

### Agent's Discretion
- Exact `FormatRenderer` method signatures and protocol shape
- How to render ARCHITECTURE.md data (module groupings, entry points) in KV form inside CODEBASE.md
- JSON and YAML output structure (flat vs nested, field naming conventions)
- File extension for json/yaml exports (e.g., `.json` files instead of `.md`?)
- Whether CODEBASE.md includes per-chunk detail or stops at file-level summary
- Error handling for invalid format values
- Test organization for new format renderers

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Source todo (requirements and acceptance criteria)
- `.planning/todos/pending/2026-04-13-add-markdown-key-value-export-format.md` — Original problem description, concrete KV examples, multi-format table, implementation steps

### Export pipeline (primary modification targets)
- `02-worktrees/glma/src/glma/export.py` — Full export module: `export_index()` orchestrator, `_format_export_file()`, `generate_index_md()`, `generate_relationships_md()`, `generate_architecture_md()`, `_write_files_to_dir()`, `_write_tar_to_stream()`. Strategy pattern routes through here.
- `02-worktrees/glma/src/glma/cli.py` — Export command (line ~418, no `--format` flag yet) and query command (line ~216, has existing `--format` with `markdown`/`json`). Both need updating.
- `02-worktrees/glma/src/glma/models.py` — `ExportConfig` class (line ~128, needs `format` field), `QueryConfig` class (line ~78, has `output_format` field). New `ExportFormat` enum goes here.

### Data sources (what formatters consume)
- `02-worktrees/glma/src/glma/db/ladybug_store.py` — `get_indexed_files()`, `get_file_record()`, `get_chunks_for_file()`, `get_file_relationships()` — data loading for export.
- `02-worktrees/glma/src/glma/models.py` — `Chunk`, `FileRecord`, `ChunkType` models consumed by formatters.
- `02-worktrees/glma/src/glma/summaries.py` — `generate_rule_summary()` for fallback summaries.

### Existing patterns (consistency reference)
- `02-worktrees/glma/src/glma/export.py` §`_format_export_file()` — Current markdown formatter: YAML frontmatter + structured sections + tables. Becomes the `markdown` renderer.
- `02-worktrees/glma/src/glma/export.py` §`generate_index_md()` / `generate_relationships_md()` / `generate_architecture_md()` — Root file generators. KV renderer needs equivalent for CODEBASE.md.

### Tests
- `02-worktrees/glma/tests/test_export.py` — Existing export tests. New format tests follow this pattern.

### Prior phase decisions
- `.planning/phases/04-file-watching-air-gapped-export/04-CONTEXT.md` — Original export design: three output modes, rule-based summaries
- `.planning/phases/08-architecture-md-export-polish/08-CONTEXT.md` — ARCHITECTURE.md structure, module grouping, entry point detection, root file generator pattern

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`_format_export_file()`** (`export.py`): The complete markdown formatter — becomes the `markdown` renderer with minimal changes. Contains all the data extraction logic (chunks, relationships, summaries, code blocks) that other renderers need the same data from.
- **`generate_index_md()` / `generate_relationships_md()` / `generate_architecture_md()`** (`export.py`): Root file generators. The markdown renderer continues using these; the KV renderer needs a `generate_codebase_md()` equivalent.
- **`file_data` dict** (built in `export_index()`): Central data structure `{path: {"record", "chunks", "relationships", "summary"}}` — already assembled before formatting. All renderers receive this same dict.
- **`ExportConfig`** (`models.py`): Already has `output_path`, `include_code`, `ai_summaries`. Adding `format` field is a one-line addition.
- **`QueryConfig.output_format`** (`models.py` line ~78): Already has `--format` on query command. Renaming/aligning with shared `ExportFormat` enum is straightforward.

### Established Patterns
- **Root file generators**: `generate_*_md()` functions take data dicts and return strings. Called from `export_index()`, passed to writers. Renderers follow this pattern.
- **Three output modes**: directory, tar.gz, stdout. `_write_files_to_dir()` and `_write_tar_to_stream()` handle serialization. These need to know which root files to write (INDEX/ARCH/RELS vs CODEBASE).
- **CLI flag overrides**: `export_overrides` dict in `cli.py` built from CLI flags, passed to `load_export_config()`. New `--format` flag follows same pattern.
- **Typer CLI pattern**: Options defined as function parameters with `typer.Option()`. `--format` / `-f` follows existing `--output` / `-o` pattern.

### Integration Points
- **`export_index()`** (`export.py` line ~816): Orchestration point — currently builds `file_data`, calls formatters, routes to writers. Strategy selection happens here.
- **`cli.py` export command** (line ~418): Add `--format` / `-f` parameter, pass to `ExportConfig`.
- **`cli.py` query command** (line ~216): Update existing `--format` to accept `ExportFormat` enum values including `yaml`.
- **`_write_files_to_dir()` / `_write_tar_to_stream()`**: Need to handle variable root file sets (3 files for markdown, 1 file for KV, TBD for json/yaml).

</code_context>

<specifics>
## Specific Ideas

- The todo's KV example for glma data is the canonical reference:
  ```markdown
  # cli.py

  language: python
  last_indexed: 2026-04-13T20:15:23
  chunk_count: 8

  ## version_callback

  type: function
  lines: L21-L24
  summary: Prints the current application version to the console...
  calls: []
  ```
- CODEBASE.md in KV format should feel like "the one file an agent reads to understand the entire codebase" — consolidating what's currently spread across 3 root files.
- JSON and YAML exports can serialize the `file_data` dict directly — they don't need elaborate formatting, just structured serialization.

</specifics>

<deferred>
## Deferred Ideas

### Reviewed Todos (not folded)
- **Pi/agent integration for code summarization** (matched Phase 11 on keywords) — belongs to Phase 12, not this phase
- **Truncate oversized chunks before summarization** (matched Phase 11 on keywords) — completed in Phase 10, not this phase

</deferred>

---

*Phase: 11-markdown-keyvalue-export*
*Context gathered: 2026-04-14*
