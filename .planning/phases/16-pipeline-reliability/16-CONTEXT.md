# Phase 16: Pipeline Reliability - Context

**Gathered:** 2026-05-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Fix chunk ID collisions, add per-file pipeline stage tracking, resume-from-interrupt, graceful shutdown, per-file markdown output, and summarization progress display. This phase establishes the durable indexing foundation that all subsequent features depend on.

Requirements: PIPE-01 through PIPE-06.

No changes to `glma search`, `glma query`, `glma export`, or `glma embed` commands. No new CLI commands. No changes to user-facing output formats.

</domain>

<decisions>
## Implementation Decisions

### Chunk ID Format (PIPE-01)
- **D-01:** Chunk ID format changes from `{file_path}::{chunk_type}::{name}::{start_line}` to `{file_path}::{name}::{line}::{hash8}` — 8-character hex suffix from BLAKE2b hash of chunk content. Note: `chunk_type` is dropped from the ID string (matches ROADMAP spec format).
- **D-02:** Force re-index — no migration script. Just change the format; next `glma index` rebuilds everything. Old DBs are incompatible.
- **D-03:** Existing summaries and embeddings are preserved automatically via the existing `upsert_chunks` logic, which matches by `content_hash` (BLAKE2b of chunk content, separate from the ID hash).
- **D-04:** This is a backend data change only — chunk IDs are internal plumbing. Users never see chunk IDs in any output (search, query, export all show chunk name, type, line range, but not the raw ID).

### Pipeline Stage Tracking (PIPE-02)
- **D-05:** 4 stages tracked per file as a `pipeline_stage` property on the Ladybug File node: `discovered → chunked → relationships_extracted → complete`.
- **D-06:** Summarization is NOT a pipeline stage — it's a post-indexing pass triggered by `--summarize`. Keeps indexing and summarization decoupled.

### Resume from Interrupt (PIPE-03)
- **D-07:** `glma index` resumes from the first file with `pipeline_stage != complete`, continuing from that file's incomplete stage. Files at `complete` are skipped entirely.
- **D-08:** Summarization resume: on re-run with `--summarize`, skip chunks that already have summaries (preserved via `content_hash` matching in `upsert_chunks`). Regenerate markdown for already-summarized files first to ensure markdown is current, then continue summarizing remaining chunks.
- **D-09:** Interrupt during summarization is safe — completed summaries are persisted to DB per-chunk. Next run picks up where it left off.

### Graceful Shutdown (PIPE-04)
- **D-10:** On SIGINT/SIGTERM: finish the current file's pipeline to a consistent state, then exit. Do NOT finish the entire current stage across all files.
- **D-11:** No rollback logic needed — the current file is completed before exit, so no partial writes exist.
- **D-12:** Signal handlers register at CLI entry, use a shared `shutdown_event` (asyncio.Event or threading.Event) that pipeline stages check between files (not during a file).

### Per-File Markdown Output (PIPE-05)
- **D-13:** Markdown is regenerated per-file immediately after that file's summarization completes — not batched at end. Already partially how it works (markdown is written per-file in the indexing pipeline), but the summarization pass currently regenerates all markdown at the end. Move the per-file markdown write into the per-file summarization loop.

### Summarization Progress Display (PIPE-06)
- **D-14:** Per-chunk Rich progress bar showing: spinner + current file and chunk name in description + progress bar + running counts of done/skipped/failed. Example: `Summarizing: auth/login.py → verify_token (34/120 chunks) ✓28 ⊘5 ✗1`.
- **D-15:** Follows the same pattern as `IndexProgress` — Rich progress with spinner, description, bar, and counts. May extend `IndexProgress` or create a parallel `SummarizeProgress` class.

### Agent's Discretion
- Exact Rich progress bar layout and column selection for summarization display
- Where to put `SummarizeProgress` (same module as `IndexProgress`, or separate)
- Whether `pipeline_stage` uses a string enum or plain string in the File node
- How to handle the `discovered` stage (set when file is first found by walker, before chunking)
- Whether to add a `--force-reindex` flag to ignore pipeline stages and reprocess everything
- Exact signal handler implementation (signal.signal vs asyncio signal handlers)
- How to communicate shutdown_event between signal handler and pipeline (threading.Event is simplest)
- Whether to print a summary of "interrupted, X files remaining" on SIGINT before exit

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Pipeline internals
- `02-worktrees/glma/src/glma/index/pipeline.py` — `run_index()` function, 3-pass pipeline (chunk → relationships → cross-file), `IndexResult` tracking, per-file processing loop. THIS IS THE PRIMARY FILE for this phase.
- `02-worktrees/glma/src/glma/index/chunks.py` — `_chunk_id()` function on line 18 generates current format. Must change to include content hash.
- `02-worktrees/glma/src/glma/index/writer.py` — `write_markdown()` function, per-file markdown generation. Currently called 3 times per file (Pass 1, 2, 3). PIPE-05 changes when markdown is written during summarization.
- `02-worktrees/glma/src/glma/index/progress.py` — `IndexProgress` class. Pattern to follow for summarization progress.

### Database layer
- `02-worktrees/glma/src/glma/db/ladybug_store.py` — `LadybugStore` class. `upsert_chunks()` (line ~235) preserves summaries/embeddings by `content_hash`. `SCHEMA_FILES` defines File node — needs `pipeline_stage` property added. `update_chunk_summary()` for per-chunk summary persistence.
- `02-worktrees/glma/src/glma/models.py` — `Chunk`, `FileRecord`, `IndexConfig` models. `FileRecord` may need `pipeline_stage` field. `Chunk.id` docstring references current format.

### Summarization
- `02-worktrees/glma/src/glma/summarize/pipeline.py` — `summarize_chunks()` function. Currently has no progress display. Skips chunks with existing summaries (line ~221). This is where `SummarizeProgress` integrates.
- `02-worktrees/glma/src/glma/summarize/providers.py` — `OpenAICompatibleProvider` used for summarization calls.
- `02-worktrees/glma/src/glma/cli.py` — `index` command (line ~60). Summarization pass is in `cli.py` lines ~120-170. This is where signal handlers register and where the summarization loop currently batches markdown regeneration at the end.

### Requirements
- `.planning/REQUIREMENTS.md` — PIPE-01 through PIPE-06
- `.planning/ROADMAP.md` — Phase 16 success criteria and key implementation notes

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`IndexProgress`** (`index/progress.py`): Rich progress bar pattern with start/advance/finish/print_summary. Same pattern for summarization progress.
- **`upsert_chunks()`** (`db/ladybug_store.py`): Already preserves summaries and embeddings by `content_hash`. The mechanism for safe re-indexing already exists — no changes needed for summary preservation.
- **`_content_hash()`** (`index/chunks.py`): BLAKE2b hash of chunk content — can reuse for the 8-char hash suffix in chunk IDs.
- **`file_content_hash()`** (`index/pipeline.py`): BLAKE2b hash of file content for incremental detection. Same pattern.

### Established Patterns
- **Ladybug File node schema**: defined in `SCHEMA_FILES` string in `ladybug_store.py`. New `pipeline_stage` property follows the same STRING column pattern as `content_hash`, `last_indexed`, etc.
- **3-pass pipeline**: chunk → relationships → cross-file. Each pass iterates files. Signal checking between files (not during) is natural since the loop already has per-file boundaries.
- **CLI command pattern**: Typer `@app.command()`, config loading, provider instantiation. Signal handlers register at command entry, before pipeline starts.
- **Markdown write timing**: currently called 3 times per file (once per pass). PIPE-05 moves the summarization-triggered write into the per-file loop instead of batching at end.

### Integration Points
- **`chunks.py` `_chunk_id()`**: Change format. All downstream consumers (DB primary key, relationship source_id/target_id, CONTAINS edges) use this string.
- **`pipeline.py` `run_index()`**: Add `pipeline_stage` updates between passes. Add shutdown_event checks between files.
- **`cli.py` `index` command**: Register signal handlers before pipeline start. Move summarization markdown writes from batch-at-end to per-file-during-summarization.
- **`ladybug_store.py` SCHEMA_FILES**: Add `pipeline_stage STRING` column. Add method to query files by stage for resume logic.
- **`summarize/pipeline.py` `summarize_chunks()`**: Add `SummarizeProgress` parameter and per-chunk progress updates.

</code_context>

<specifics>
## Specific Ideas

- Progress bar description updates with "file.py → chunk_name" to show what's currently being summarized — matches how indexing shows the current file
- The existing `upsert_chunks` content_hash matching is the key enabler for safe re-indexing without losing LLM work — no new logic needed for that concern

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 16-pipeline-reliability*
*Context gathered: 2026-05-12*
