# Phase 4: File Watching & Air-Gapped Export - Context

**Gathered:** 2026-04-09
**Status:** Ready for planning

<domain>
## Phase Boundary

The index stays in sync as code changes, and the full index can be exported as static markdown for zero-runtime environments. Two CLI commands: `glma watch` for live file watching with incremental re-indexing (keeps Ladybug DB and markdown in sync), and `glma export` for generating a complete static markdown export that shell-only agents can consume with just `cat`. This phase does NOT add new analysis capabilities — it operationalizes the existing indexing pipeline for continuous use and offline consumption.

</domain>

<decisions>
## Implementation Decisions

### Watch Behavior
- **D-01:** `glma watch` runs as a foreground process. User stops with Ctrl+C. No daemon mode.
- **D-02:** Batch window for change processing — collect all file change events over a fixed time window, then process them all at once. Handles bulk operations like `git checkout` or `git pull` cleanly.
- **D-03:** Track all file event types: create, modify, delete, and rename. Explicit rename tracking allows single-operation path updates instead of delete+re-parse.
- **D-04:** Minimal output by default: `[12:34:56] Re-indexing 3 files... Done.` Otherwise silent. `--verbose` flag logs every file event: `[12:34:56] MODIFIED src/auth.py`.

### Dual Output Sync
- **D-05:** Reuse existing `run_index` pipeline with a file filter for changed files. Don't write a separate incremental pipeline — the existing one already handles upserts, relationship extraction, and cross-file markdown rewrites.
- **D-06:** Atomic-ish write pattern: buffer all changes, write DB + markdown, verify both succeeded. If markdown write fails, roll back DB changes. Guarantees consistency between DB and markdown outputs.

### Export Format & Structure
- **D-07:** Export uses nested mirror structure matching source repo (`export/src/auth/login.py.md`). Plus a root `INDEX.md` with file listing, chunk counts, and relationship summaries. Plus a root `RELATIONSHIPS.md` showing full cross-file dependency graph as a table.
- **D-08:** Cross-file references: keep inline relationship sections per file (existing format from writer.py), add relative path links in relationship tables (`[src/auth.py](../auth/auth.py.md)`), plus dedicated root `RELATIONSHIPS.md` with `| Source File | Target File | Type | Details |` table.
- **D-09:** Each exported file gets a metadata header block: file path, language, last indexed timestamp, chunk count, content hash. Then file summary. Then existing chunk/relationship content.

### Export Completeness
- **D-10:** File summaries generated rule-based by default: auto-generate from existing data (list top-level exports, count functions/classes, note primary imports). Deterministic, no LLM needed, works offline. Example: "3 functions (authenticate, verify_token, refresh), 1 class (TokenStore). Imports: jwt, datetime, os."
- **D-11:** Optional AI summaries via `--ai-summaries` flag. Must support local model providers: LM Studio, llama.cpp, Ollama, etc. No cloud dependency required. User provides base URL and optional model name via config or CLI flags.
- **D-12:** Export output supports three modes: directory path (`--output ./dir`), compressed archive (`--output export.tar.gz`), or stdout pipe (`--output -` for streaming tar to stdout, enables `glma export . | ssh remote 'tar -x'`).

### the agent's Discretion
- Exact batch window duration (e.g., 3s, 5s, configurable via `.glma.toml`)
- File watching library choice (watchfiles, watchdog, or inotify-based)
- Rule-based summary format and detail level
- Local model API integration details (OpenAI-compatible endpoint assumption for LM Studio/Ollama/llama.cpp?)
- How to handle the atomic rollback on partial failure
- Archive format details (tar.gz vs zip)
- Exact INDEX.md and RELATIONSHIPS.md schema/formatting

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project-level context
- `.planning/codebase/ARCHITECTURE.md` - Repository architecture, worktree pattern, data flow
- `.planning/codebase/STRUCTURE.md` - Directory layout, glma code lives in `02-worktrees/glma/src/glma/`
- `.planning/codebase/CONVENTIONS.md` - Code style, naming patterns, uv for package management
- `.planning/codebase/STACK.md` - Technology stack (tree-sitter, Ladybug, Python 3.13, uv)

### Phase 1-3 implementation (directly extends this code)
- `02-worktrees/glma/src/glma/cli.py` - Existing Typer CLI with `glma index` and `glma query` commands. New `watch` and `export` commands go here.
- `02-worktrees/glma/src/glma/index/pipeline.py` - Main indexing orchestrator with `run_index()`. Watch reuses this with a file filter. Contains `file_content_hash()`, `IndexResult`, and the 3-pass pipeline.
- `02-worktrees/glma/src/glma/index/writer.py` - Markdown output writer with `format_file_markdown()` and `write_markdown()`. Export builds on this format with metadata headers and summaries.
- `02-worktrees/glma/src/glma/db/ladybug_store.py` - LadybugStore with all CRUD operations. Watch and export both read from this. Key methods: `get_indexed_files()`, `get_file_record()`, `get_chunks_for_file()`, `get_file_relationships()`, `get_all_relationships_for_file()`.
- `02-worktrees/glma/src/glma/config.py` - Config loading from `.glma.toml` + CLI overrides. Watch and export may need config extensions.
- `02-worktrees/glma/src/glma/models.py` - Chunk, FileRecord, Relationship, IndexConfig, QueryConfig models. May need ExportConfig, WatchConfig, or local model provider config.

### Requirements
- `.planning/REQUIREMENTS.md` - Phase 4 covers: WTCH-01, WTCH-02, WTCH-03, AIRG-01, AIRG-02, AIRG-03, CLIF-03, CLIF-04
- `.planning/ROADMAP.md` §Phase 4 - Success criteria, plan breakdown (04-01 through 04-02)

### Prior phase decisions
- `.planning/phases/01-core-indexing-pipeline/01-CONTEXT.md` - Phase 1 decisions: Ladybug schema, layered markdown structure, content hashing, upsert patterns, dual output (DB + markdown)
- `.planning/phases/02-relationship-extraction/02-CONTEXT.md` - Phase 2 decisions: RELATES_TO edge schema, 3-pass pipeline, cross-file resolution
- `.planning/phases/03-query-tool-notebook-compaction/03-CONTEXT.md` - Phase 3 decisions: query output format, error handling, CLI flag patterns

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`run_index()` pipeline** (`index/pipeline.py`): Full indexing orchestrator that does walk → hash → skip-if-unchanged → parse → store → write markdown → extract relationships → cross-file rewrite. Watch calls this with a subset of files.
- **`file_content_hash()`** (`index/pipeline.py`): BLAKE2b hashing already works for incremental re-index detection.
- **`IndexResult`** (`index/pipeline.py`): Summary stats (total_files, new_files, updated_files, etc.). Reusable for watch batch results.
- **LadybugStore** (`db/ladybug_store.py`): Full CRUD for files, chunks, relationships. `get_indexed_files()` returns all indexed file paths with hashes — needed for export and watch sync. `get_file_relationships()` and `get_all_relationships_for_file()` needed for export relationship tables.
- **`format_file_markdown()`** (`index/writer.py`): Generates per-file markdown with chunks and relationships. Export enriches this format with metadata headers and summaries.
- **`write_markdown()`** (`index/writer.py`): Writes markdown to `.glma-index/markdown/` directory. Export writes to a different output directory using similar logic.
- **Typer CLI** (`cli.py`): `app = typer.Typer()` with `index` and `query` commands. `watch` and `export` register on the same app. Rich console already imported.
- **IndexConfig** (`models.py`): Pydantic config model. Pattern to follow for WatchConfig/ExportConfig.

### Established Patterns
- **Typer CLI with Rich**: Commands decorated with `@app.command()`, Rich console for formatted output, `typer.Option()` for flags.
- **Ladybug Cypher queries**: `store.conn.execute("MATCH ...", {params})` pattern for all graph queries.
- **Chunk ID format**: `{file_path}::{chunk_type}::{name}::{start_line}` — used for joining chunks to relationships.
- **Config pattern**: Pydantic BaseModel loaded from `.glma.toml` with CLI overrides via `load_config()`.
- **Dual output**: Every index operation writes to both Ladybug DB and markdown files. Watch must maintain this contract.
- **3-pass pipeline**: Pass 1 = chunks, Pass 2 = relationships, Pass 3 = cross-file incoming rewrite. Watch must run all 3 passes for affected files.
- **Upsert = delete + recreate**: File/chunk upserts delete first, then insert. This pattern is what makes re-indexing safe.

### Integration Points
- **CLI registration**: Two new commands: `@app.command()` for `watch` and `export` in `cli.py`.
- **Pipeline reuse**: `run_index()` needs to accept a file filter parameter (list of changed files) so watch can call it with only affected files instead of a full directory walk.
- **Config extensions**: `.glma.toml` may need `[watch]` and `[export]` sections for debounce timing, batch window, local model URL, etc.
- **Export directory**: Different from `.glma-index/`. User specifies output path. Must create nested mirror structure + INDEX.md + RELATIONSHIPS.md.
- **Local model API**: Likely OpenAI-compatible API (most local providers — LM Studio, Ollama, llama.cpp server — expose this). Config needs `base_url` and optional `model` field. Use `openai` Python client pointed at local URL.

</code_context>

<specifics>
## Specific Ideas

- The batch window approach is key for `glma watch`. When a user does `git checkout main` and 200 files change, you don't want 200 individual re-indexes. Collect everything in the window, then call `run_index` once with the batch of changed files.
- The export's `RELATIONSHIPS.md` is the killer feature for air-gapped agents. A single file that shows the entire cross-file dependency graph means an agent can understand the codebase architecture without reading every file.
- Rule-based summaries should be good enough for most cases. "3 functions (auth, verify, refresh), 1 class (TokenStore). Imports: jwt, datetime" tells an agent a lot. AI summaries are for when users want natural language like "This file implements JWT authentication with refresh token rotation."
- Local model support via OpenAI-compatible API is the right abstraction. LM Studio, Ollama, llama.cpp server all expose `/v1/chat/completions`. One integration covers all of them.
- Stdout export mode (`--output -`) enables powerful workflows like `glma export . | ssh airgapped 'cd /project && tar -x'` — pipe directly to an air-gapped machine.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 04-file-watching-air-gapped-export*
*Context gathered: 2026-04-09*
