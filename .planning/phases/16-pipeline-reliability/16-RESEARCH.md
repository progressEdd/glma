# Phase 16: Pipeline Reliability - Research

**Researched:** 2026-05-12
**Status:** Complete

## Research Question

What do I need to know to PLAN Phase 16 well?

---

## 1. Chunk ID Collision Analysis (PIPE-01)

### Current Format
`{file_path}::{chunk_type}::{name}::{start_line}` (in `chunks.py:_chunk_id()`)

### Collision Scenarios
The `chunk_type` field is already in the ID. The actual collision risk from the ROADMAP comes from:
- **C forward declarations:** `int foo(int x);` at line 10 and `int foo(int x) { ... }` at line 50 — same name, same chunk_type, different lines. The line number already disambiguates these, BUT if the file is re-indexed and lines shift, old IDs become orphaned.
- **C macros:** `#define FOO(x)` producing multiple expansions that result in the same function name at different lines — already handled by line number.
- **The real risk:** Two different chunks in the same file with the same name and chunk_type at different lines. E.g., C static functions with the same name in different scopes, or inline functions in headers included multiple times.

### Proposed Format
`{file_path}::{name}::{line}::{hash8}` — note: `chunk_type` is dropped per CONTEXT D-01.

### Impact Analysis
- `_chunk_id()` is called once in `_walk_chunks()` — single point of change.
- The `_content_hash()` function already exists (BLAKE2b, 64-char hex). We need a truncated 8-char version.
- **All downstream consumers:** Chunk.id is the primary key in the Ladybug Chunk node table. Relationship source_id/target_id reference it. CONTAINS edges connect File→Chunk. All of these use the string ID.
- **Force re-index:** Since the ID format changes, old DBs are incompatible. No migration needed — just re-index.
- **Summary/embedding preservation:** `upsert_chunks()` matches by `content_hash`, not by `id`. So summaries ARE preserved for same-content chunks even with new IDs, BUT the old chunks with old-format IDs are deleted and new ones with new-format IDs are created. The summary_map in `upsert_chunks()` is keyed by content_hash, so as long as the content hasn't changed, summaries survive. ✓

### Key Insight
The `chunk_type` field is currently used in the ID but CONTEXT D-01 says to drop it. This simplifies the ID but we need to verify that `chunk_type` is never needed to disambiguate two chunks with the same name at the same line (unlikely but worth noting — only possible with AST edge cases).

---

## 2. Pipeline Stage Tracking (PIPE-02)

### Current File Node Schema
```sql
CREATE NODE TABLE IF NOT EXISTS File (
    path STRING,
    language STRING,
    content_hash STRING,
    last_indexed STRING,
    chunk_count INT64,
    file_summary STRING,
    PRIMARY KEY (path)
)
```

### Adding `pipeline_stage`
- New `pipeline_stage STRING` column in SCHEMA_FILES
- Values: `discovered`, `chunked`, `relationships_extracted`, `complete`
- CONTEXT D-06: Summarization is NOT a pipeline stage — post-indexing pass only.
- Migration: `_migrate_schema()` already handles `ALTER TABLE ... ADD` gracefully (catches "already exists" exceptions). Same pattern.

### Stage Transitions
Current pipeline in `run_index()`:
1. **Walk source files** → `discovered` (new: set when file first found)
2. **Chunk extraction + attach comments** → `chunked`
3. **Relationship extraction** → `relationships_extracted`
4. **Cross-file relationships + final markdown** → `complete`

### Key Insight
The current pipeline processes ALL files in each pass sequentially (Pass 1: all files chunked, Pass 2: all files get relationships, Pass 3: cross-file). Stage tracking needs to be set PER-FILE within each pass, not per-pass.

### Stage Storage Pattern
- Set stage via `SET f.pipeline_stage = $stage` on the File node after each stage completes.
- Or embed in `upsert_file()` — add `pipeline_stage` to `FileRecord` model.
- QUERY pattern needed: `MATCH (f:File) WHERE f.pipeline_stage <> 'complete' RETURN f.path ORDER BY f.path` for resume logic.

---

## 3. Resume Logic (PIPE-03)

### Current Behavior
`run_index()` already has incremental logic: it checks `file_content_hash` and skips unchanged files. But there's no resume-from-interrupt — if you Ctrl+C during Pass 2, the next run starts from scratch on all passes.

### Resume Strategy
1. On `glma index` start: query all File nodes for `pipeline_stage`.
2. If ALL files are `complete` or `discovered` (with no mid-pipeline states) → normal fresh run.
3. If some files are `chunked` or `relationships_extracted` → resume from the first incomplete stage.
4. Files at `complete` are skipped entirely (content hash check still applies for staleness).

### Resume Per-Stage
- `discovered`: Re-chunk (Pass 1 from this file).
- `chunked`: Skip chunking, start relationships (Pass 2 from this file).
- `relationships_extracted`: Skip chunking + relationships, do cross-file (Pass 3).
- `complete`: Skip entirely (unless content hash changed).

### CONTENT HASH INTERACTION
If a file's content hash changed but its stage is `chunked` or later → the file MUST be re-processed from scratch. The content hash check must override the stage — stale intermediate results are worse than re-doing work.

### Summarization Resume (CONTEXT D-08)
- `summarize_chunks()` already skips chunks with existing summaries (incremental).
- On re-run with `--summarize`, chunks that already have summaries are preserved via content_hash matching.
- Per CONTEXT D-08: regenerate markdown for already-summarized files first, then continue with remaining.

---

## 4. Graceful Shutdown (PIPE-04)

### Signal Handling in Python
- `signal.signal(signal.SIGINT, handler)` — works in main thread.
- `signal.signal(signal.SIGTERM, handler)` — works in main thread.
- Handler sets a `threading.Event` (or `asyncio.Event` for async).
- Pipeline checks `shutdown_event.is_set()` between files (not during a file).

### Integration Points
- **CLI layer (`cli.py`):** Register signal handlers at the start of the `index` command. Create `threading.Event` named `shutdown_event`.
- **Pipeline layer (`pipeline.py`):** Accept `shutdown_event` parameter. Check between files in the Pass 1/2/3 loops. If set: finish current file, update its stage, then exit.
- **Per CONTEXT D-10:** Finish current file's pipeline to consistent state, then exit. Do NOT finish all files at current stage.

### Implementation Pattern
```python
import signal, threading

shutdown_event = threading.Event()

def _signal_handler(signum, frame):
    shutdown_event.set()

signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)
```

### Exit Behavior
- Print a message: "Interrupted. N files remaining. Run `glma index` to resume."
- Return the partial IndexResult.
- Exit code: 0 (not an error — intentional interrupt).

### Key Insight
The current `run_index()` processes files in 3 separate loops (Pass 1, Pass 2, Pass 3). For graceful shutdown to work per-file, we'd need to either:
- **Option A (recommended):** Merge the 3 passes into a single per-file loop. Process each file through all 3 stages before moving to the next. This makes shutdown between files natural and eliminates the need to track "which pass was I in".
- **Option B:** Keep 3 passes but check shutdown_event at the top of each file iteration in each pass. Less ideal because interrupting during Pass 1 means Passes 2 and 3 never run for any file — all files are at `chunked` stage.

CONTEXT D-10 says "finish the current file's pipeline" — this strongly implies Option A (merge into single per-file loop). This is a significant refactor of `run_index()`.

---

## 5. Per-File Markdown Output (PIPE-05)

### Current Behavior
In `cli.py` (lines ~120-170), the summarization pass:
1. Iterates all files, calls `summarize_chunks()` per file.
2. Generates file-level summaries.
3. **Then** loops over all files again to `write_markdown()` — this is the batch-at-end behavior.

The indexing pipeline in `pipeline.py` already writes markdown per-file (3 times per file: after Pass 1, Pass 2, Pass 3). The problem is specifically in the **summarization** flow in `cli.py`.

### Fix Location
Move the `write_markdown()` call into the per-file summarization loop in `cli.py`, immediately after `summarize_chunks()` and file-level summary generation for that file. Remove the final batch loop.

### Impact
- Minimal code change — just moving a loop body.
- Per CONTEXT D-13: the summarization pass currently regenerates all markdown at the end. Moving the write into the per-file loop makes it immediate.

---

## 6. Summarization Progress Display (PIPE-06)

### Current Behavior
`summarize_chunks()` in `summarize/pipeline.py` has no progress display at all. It just logs counts at the end via `logger.info()`.

### Pattern to Follow
`IndexProgress` in `index/progress.py`:
- Uses Rich `Progress` with `SpinnerColumn`, `TextColumn`, `BarColumn`, etc.
- Methods: `start()`, `advance()`, `finish()`, `print_summary()`

### SummarizeProgress Design (CONTEXT D-14)
- Show: spinner + `Summarizing: {file_path} → {chunk_name} ({current}/{total} chunks) ✓{done} ⊘{skipped} ✗{failed}`
- Need: per-chunk advancement (not per-file like IndexProgress).
- Track counts: done, skipped, failed (already tracked in `summarize_chunks()`).

### Integration
- Pass `SummarizeProgress` into `summarize_chunks()` as optional parameter (same pattern as `IndexProgress` into `run_index()`).
- In `cli.py`, instantiate `SummarizeProgress` and pass it through.
- `summarize_chunks()` updates progress per-chunk: advance for each chunk, update description with current file+chunk name.

---

## 7. Single Per-File Pipeline Refactor (Critical Cross-Cutting)

The biggest architectural decision is whether to merge the 3-pass pipeline into a single per-file loop. This affects PIPE-02, PIPE-03, PIPE-04, and PIPE-05.

### Current 3-Pass Architecture
```
Pass 1: For each file → chunk, attach comments, store, write markdown
Pass 2: For each changed file → extract relationships, store, rewrite markdown
Pass 3: For each affected file → get cross-file relationships, rewrite markdown
```

### Proposed Single-Pass Architecture
```
For each file:
  1. Chunk extraction + comment attachment
  2. Store chunks, set stage = chunked
  3. Extract relationships (requires other files' chunks in DB)
  4. Store relationships, set stage = relationships_extracted
  5. Write markdown with relationships
  Set stage = complete
```

### Dependency Problem
Pass 2 (relationship extraction) calls `extract_relationships()` which resolves cross-references by looking up chunks in the DB. If we process file A before file B, file A's relationships to file B won't resolve because file B isn't in the DB yet.

**However:** The current code already handles unresolved targets (stores with source pointing to itself, `target_name` captures what was called). So single-pass is viable — unresolved targets are stored and can be resolved later.

**BUT:** The ROADMAP says "3-pass pipeline" and the existing code's Pass 3 specifically handles incoming cross-file relationships. If we go single-pass, we lose the ability to resolve cross-file references in a single run.

### Recommended Approach (from CONTEXT)
Keep 2 passes, not 3:
1. **Pass 1 (per-file loop):** For each file: chunk → store → set `chunked` → extract relationships → store → set `relationships_extracted` → write markdown → set `complete`. Check `shutdown_event` between files.
2. **Pass 2 (cross-file):** For each newly-completed file, resolve incoming cross-file relationships and rewrite markdown.

This keeps cross-file resolution working while making per-file shutdown natural.

### Actually: Keep 3 Passes, Add Stage + Shutdown
After deeper analysis, the 3-pass architecture is fine for stage tracking and shutdown:
- **Pass 1:** For each file: chunk → store → set `chunked`. Check shutdown between files.
- **Pass 2:** For each chunked file: extract relationships → store → set `relationships_extracted`. Check shutdown between files.
- **Pass 3:** For each relationships_extracted file: cross-file → write markdown → set `complete`. Check shutdown between files.

Resume picks up from the right stage. Shutdown finishes current file within the current pass. This avoids the cross-file resolution problem entirely.

**Verdict:** Keep the 3-pass architecture but add per-file stage tracking and shutdown checks. This is less risky than restructuring the pipeline.

---

## 8. Database Schema Changes Summary

### File Node (SCHEMA_FILES)
Add: `pipeline_stage STRING` with default `discovered`

### New Methods on LadybugStore
- `set_pipeline_stage(file_path: str, stage: str)` — update File node stage
- `get_files_by_stage(stage: str) -> list[str]` — query files at a given stage
- `get_incomplete_files() -> list[tuple[str, str]]` — files where stage != complete, returns (path, stage)

### FileRecord Model
Add: `pipeline_stage: Optional[str]` field, default `None` (not set until indexing starts)

### Chunk Schema
No changes needed — chunk ID format changes but schema is unchanged (id is already a STRING).

---

## 9. Testing Strategy

### Test Files to Create/Modify
- `tests/test_chunk_id.py` — test new chunk ID format with hash suffix
- `tests/test_pipeline_stages.py` — test stage transitions and resume
- `tests/test_graceful_shutdown.py` — test SIGINT handling
- `tests/test_summarize_progress.py` — test progress display

### Key Test Scenarios
1. **Chunk ID uniqueness:** Two chunks with same name/line in different files → different IDs. Two chunks with same name but different content → different IDs (hash differs).
2. **Resume after interrupt:** Set some files to `chunked` stage, run `run_index()` → only Pass 2 and Pass 3 run for those files.
3. **Content hash overrides stage:** File at `chunked` stage but content changed → re-process from scratch.
4. **Signal handling:** Set `shutdown_event`, verify current file completes but next file is skipped.
5. **Per-file markdown:** Summarize file A → file A's markdown exists before file B is summarized.

---

## RESEARCH COMPLETE

### Summary of Key Findings

1. **Chunk ID change is low-risk** — single function to modify, summary/embedding preservation works via content_hash matching.
2. **Pipeline stage tracking is additive** — new column + new methods, no existing code breaks.
3. **Keep 3-pass architecture** — less risky than restructuring. Add stage tracking and shutdown checks at per-file boundaries.
4. **Graceful shutdown uses `threading.Event`** — check between files in each pass.
5. **Per-file markdown is a CLI-layer fix** — move `write_markdown()` call into the per-file summarization loop.
6. **SummarizeProgress follows IndexProgress pattern** — Rich progress, per-chunk advancement.
7. **Force re-index is implicit** — new chunk ID format means old DBs are incompatible. Next `glma index` rebuilds.
