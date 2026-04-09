# Phase 3: Query Tool & Notebook Compaction - Context

**Gathered:** 2026-04-09
**Status:** Ready for planning

<domain>
## Phase Boundary

Agents can call `glma query <filepath>` and get compacted, relevant context as markdown — including Jupyter notebooks flattened into readable form. Query output uses layered format by default (summary → signatures with relationship hints) and includes full code with `--verbose` flag. Jupyter notebooks are compacted into markdown with per-statement variable tracking and cross-cell dependency flow. Query results show index metadata (last indexed timestamp, number of chunks in file).

This phase delivers: CLI query command, file lookup from LadybugStore, layered markdown formatting, Jupyter notebook parsing via nbformat, per-statement variable tracking, cross-cell variable flow, dependency inclusion in output, verbose mode, extended CLI flags, and structured error handling.

</domain>

<decisions>
## Implementation Decisions

### Query Output Format
- **D-01:** Default output is compact: file summary → function/class signatures with docstrings → relationship hints per signature. No code bodies in default mode.
- **D-02:** Each signature includes a compact relationship hint line (e.g., `→ calls: authenticate(), create_session()`). Gives dependency context without `--verbose`.
- **D-03:** `--verbose` flag adds full code bodies for each chunk. Transforms compact summary into full detail view.
- **D-04:** Query output is generated fresh from DB queries, not by slicing the existing per-file markdown from writer.py. The query output is a different, more compact view than the full markdown.

### Notebook Compaction
- **D-05:** Variable tracking is per-statement, not per-cell. Each assignment within a cell is tracked individually (e.g., "Cell 3 L1: defines `model` | references `Sequential`" and "Cell 3 L5: defines `accuracy` | references `model`, `score`").
- **D-06:** Variable flow displayed two ways: (1) inline per-cell `defines:` and `references:` with cross-cell origin annotations (e.g., `references: X_train (defined cell 1)`), and (2) a `## Variable Flow` summary table at the end: `| Variable | Defined (Cell) | Used (Cells) |`.
- **D-07:** Markdown cells in notebooks are included as-is, rendered as blockquotes between code cells. Preserves narrative context (explanations, headings, observations).
- **D-08:** Cell outputs stripped by default per ROADMAP spec. Configurable to include them.
- **D-09:** Notebook compaction uses nbformat for .ipynb parsing.

### Dependency Depth
- **D-10:** Default query shows direct (1-hop) relationships only — what the file directly calls/imports/inherits.
- **D-11:** `--depth N` flag enables deeper traversal. Power users and agents can trace multi-hop call chains.
- **D-12:** All relationship types shown by default: calls, imports, inherits, includes. No filtering by default.

### CLI Interface
- **D-13:** Extended flag set:
  - `--verbose` — add full code bodies
  - `--depth N` — relationship traversal depth (default 1)
  - `--no-relationships` — skip dependency section entirely
  - `--format json` — machine-readable JSON output for programmatic use
  - `--output -` — explicit stdout (useful for piping)
  - `--rel-types calls,imports` — filter which relationship types to show
  - `--summary-only` — just the file summary, skip signatures
- **D-14:** `glma query <filepath>` is the primary command. Filepath is relative to the indexed repo root.

### Error Handling
- **D-15:** Structured errors with semantic exit codes:
  - Exit 1: file not found on disk
  - Exit 2: file not indexed (exists but never indexed)
  - Exit 3: stale index (file modified since last index)
  - Exit 4: query error (DB error, parse error, etc.)
- **D-16:** Stderr gets human-readable error messages. Stdout stays clean for piping and programmatic use.

### Agent's Discretion
- Exact layout/spacing of the compact query output (signature block formatting, relationship hint styling)
- How to render the `## Variable Flow` table (column order, sort order)
- nbformat parsing implementation details (AST approach for variable extraction per statement)
- JSON output schema for `--format json`
- Whether `--depth N` has a hard cap (e.g., max depth 10) to prevent runaway traversals
- How stale index detection works (compare file mtime vs indexed timestamp, or re-hash the file)
- Index metadata display format (last indexed, chunk count, file hash)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project-level context
- `.planning/codebase/ARCHITECTURE.md` - Repository architecture, worktree pattern, data flow
- `.planning/codebase/STRUCTURE.md` - Directory layout, glma code lives in `02-worktrees/glma/src/glma/`
- `.planning/codebase/CONVENTIONS.md` - Code style, naming patterns, uv for package management
- `.planning/codebase/STACK.md` - Technology stack (tree-sitter, Ladybug, Python 3.13, uv)

### Phase 1-2 implementation (directly extends this code)
- `02-worktrees/glma/src/glma/cli.py` - Existing Typer CLI with `glma index` command. New `query` command goes here.
- `02-worktrees/glma/src/glma/db/ladybug_store.py` - LadybugStore with Chunk/File nodes, RELATES_TO edges. Query methods already exist: `get_outgoing_relationships`, `get_incoming_relationships`, `get_file_relationships`. May need new query-specific methods.
- `02-worktrees/glma/src/glma/models.py` - Chunk, FileRecord, Relationship, IndexConfig models. May need QueryConfig or query result models.
- `02-worktrees/glma/src/glma/index/writer.py` - Existing markdown output writer with `format_file_markdown()`. Query output is a different, more compact format — separate formatter, not reusing writer.py.
- `02-worktrees/glma/src/glma/index/pipeline.py` - Main indexing orchestrator. Query tool reads from the DB that pipeline creates.

### Requirements
- `.planning/REQUIREMENTS.md` - Phase 3 covers: QURY-01 through QURY-05, JNTP-01 through JNTP-04, CLIF-02, CLIF-05
- `.planning/ROADMAP.md` §Phase 3 - Success criteria, plan breakdown (03-01 through 03-03)

### Prior phase decisions
- `.planning/phases/01-core-indexing-pipeline/01-CONTEXT.md` - Phase 1 decisions: Ladybug schema, layered markdown structure, content hashing, upsert patterns
- `.planning/phases/02-relationship-extraction/02-CONTEXT.md` - Phase 2 decisions: RELATES_TO edge schema, relationship markdown output (inline + summary), confidence tagging, cross-file resolution

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **LadybugStore** (`db/ladybug_store.py`): Already has `get_outgoing_relationships(chunk_id)`, `get_incoming_relationships(chunk_id)`, `get_file_relationships(file_path)`. Query tool calls these directly. May need a few new methods: `get_file_by_path()`, `get_chunks_for_file()`, `get_index_metadata()`.
- **Typer CLI** (`cli.py`): Existing `app` Typer instance with `index` command. New `query` command registers on the same app. Rich console already imported.
- **Models** (`models.py`): Chunk, FileRecord, Relationship models with full field definitions. Query results may reuse Chunk for signature display.
- **Writer** (`index/writer.py`): `_format_chunk_heading()`, `_resolve_target_display()`, `_format_relationships_summary()` contain reusable formatting helpers for relationship display. Don't reuse the full `format_file_markdown()` — query output is a different compact format.
- **Pipeline** (`index/pipeline.py`): `_load_chunks_from_store()` loads chunks from DB given a file path. Query tool needs the same pattern.

### Established Patterns
- **Typer CLI with Rich**: `app = typer.Typer()`, commands decorated with `@app.command()`, Rich console for formatted output.
- **Ladybug Cypher queries**: `store.conn.execute("MATCH ...", {params})` pattern. All graph queries use parameterized Cypher.
- **Chunk ID format**: `{file_path}::{chunk_type}::{name}::{start_line}` — used throughout for joining chunks to relationships.
- **Upsert = delete + recreate**: File/chunk upserts delete first, then insert. Query tool is read-only — no upsert patterns needed.
- **Config via IndexConfig**: Pydantic model loaded from `.glma.toml` + CLI overrides. Query may need a lighter QueryConfig.

### Integration Points
- **CLI registration**: New `@app.command()` for `query` in `cli.py`. Takes filepath argument plus extended flags.
- **LadybugStore**: Query tool opens the same `.glma-index/db/index.lbug` database in read-only mode. May want a read-only connection to avoid accidental writes.
- **Markdown output dir**: `.glma-index/markdown/` contains the full per-file markdown. Query tool does NOT read these files — it queries the DB directly and generates fresh compact output.
- **Notebook pipeline**: New `.ipynb` parsing module. Notebooks go through a different pipeline than source files (nbformat → cell extraction → variable tracking → compacted markdown). May or may not use LadybugStore depending on whether notebooks are also indexed as chunks.

</code_context>

<specifics>
## Specific Ideas

- The query output should feel like a quick-reference card, not a full document. An agent should be able to glance at it and know: what this file does, what's in it, what it depends on, and what depends on it. That's the compact default. `--verbose` is for when they need to see implementation.
- Per-statement variable tracking in notebooks is more complex than per-cell but gives much better results for agents trying to debug or understand data flow. The Variable Flow summary table is the key deliverable — it's what makes notebooks actually navigable.
- The relationship hints on signatures (e.g., `→ calls: authenticate(), create_session()`) are the killer feature for agents. They get dependency context without needing a separate call or `--verbose`.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 03-query-tool-notebook-compaction*
*Context gathered: 2026-04-09*
