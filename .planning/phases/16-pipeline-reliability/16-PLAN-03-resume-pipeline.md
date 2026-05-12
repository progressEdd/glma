---
wave: 2
depends_on:
  - 16-PLAN-01
  - 16-PLAN-02
files_modified:
  - src/glma/index/pipeline.py
requirements_addressed:
  - PIPE-02
  - PIPE-03
---

# Plan 03: Resume-Safe Pipeline with Stage Updates (PIPE-02, PIPE-03)

## Objective
Modify `run_index()` to set pipeline stages per-file during each pass, and implement resume logic that skips already-completed stages. When `glma index` re-runs, it picks up from the first incomplete stage.

## Tasks

### Task 3.1: Add resume logic to `run_index()`

<read_first>
- 02-worktrees/glma/src/glma/index/pipeline.py — `run_index()` function (full file, 282 lines)
- 02-worktrees/glma/src/glma/db/ladybug_store.py — new `get_incomplete_files()` and `set_pipeline_stage()` methods (added by Plan 02)
- 02-worktrees/glma/src/glma/models.py — `FileRecord` model with `pipeline_stage` field
</read_first>

<action>
Refactor `run_index()` to add stage tracking and resume logic. The core changes:

1. **After store initialization**, query existing file stages:
   ```python
   # Resume: get existing file stages from DB
   file_stages: dict[str, str] = {}
   indexed_files = store.get_indexed_files()
   for fp, _ in indexed_files.items():
       record = store.get_file_record(fp)
       if record:
           file_stages[fp] = getattr(record, 'pipeline_stage', 'complete')
   ```

2. **In Pass 1 (chunk extraction loop)**, after storing a file's chunks and writing initial markdown, set stage:
   ```python
   store.set_pipeline_stage(relative_path, "chunked")
   ```
   This goes after the `store.upsert_chunks()` and `write_markdown()` calls for that file. Also set `file_record.pipeline_stage = "chunked"` before calling `store.upsert_file()`.

3. **In Pass 2 (relationship extraction loop)**, after storing relationships and rewriting markdown:
   ```python
   store.set_pipeline_stage(relative_path, "relationships_extracted")
   ```

4. **In Pass 3 (cross-file relationships loop)**, after the final markdown write:
   ```python
   store.set_pipeline_stage(relative_path, "complete")
   ```

5. **Content hash check overrides stage**: In Pass 1, the existing logic checks `stored_hash == current_hash` and skips unchanged files. Add a condition: if a file's content hash changed (new or updated), its stage should be reset. The current logic already handles this — it re-processes changed files from scratch. Just make sure the stage is set to `discovered` when a file is first seen or re-indexed.

   Specifically, in the `upsert_file()` call, set `pipeline_stage="discovered"` initially (this is the default in FileRecord). Then it gets updated to `chunked` after Pass 1, `relationships_extracted` after Pass 2, and `complete` after Pass 3.

6. **Resume in Pass 1**: Files where `file_stages.get(relative_path) == "complete"` AND content hash hasn't changed → skip entirely (existing behavior). Files where stage is `"chunked"` or later but content hash changed → re-process from scratch (existing hash check handles this).

7. **Resume in Pass 2**: Files that already have stage `"relationships_extracted"` or `"complete"` AND weren't re-chunked in Pass 1 → skip. Only process files that were newly chunked in this run.
   
   Update the skip condition in Pass 2. Currently it checks `if relative_path not in changed_relative_paths: continue`. Keep this but ALSO skip files whose stage is already `relationships_extracted` or `complete` (unless they were in `changed_relative_paths`):
   ```python
   # Skip files that weren't actually changed AND already have relationships
   if relative_path not in changed_relative_paths:
       current_stage = file_stages.get(relative_path, "")
       if current_stage in ("relationships_extracted", "complete"):
           continue
   ```
   
   Actually, the existing `changed_relative_paths` logic already handles this correctly — only changed files get relationships extracted. For resume, we need to handle the case where a file was chunked (stage=`chunked`) in a previous interrupted run but wasn't in `changed_relative_paths` for THIS run. Add:
   ```python
   # Resume: also process files from previous runs that are at 'chunked' stage
   resume_chunked = [fp for fp, stage in file_stages.items() if stage == "chunked"]
   ```
   Then in the Pass 2 loop, iterate over `changed_relative_paths | set(resume_chunked)` instead of just `changed_relative_paths`.

8. **Resume in Pass 3**: Similarly, include files at stage `relationships_extracted` that need their final markdown:
   ```python
   resume_rels_extracted = [fp for fp, stage in file_stages.items() if stage == "relationships_extracted"]
   ```
   Include these in Pass 3 processing.

9. **Update `pass3_paths`**: Currently `pass3_paths = changed_relative_paths | dependent_paths`. Also add `set(resume_rels_extracted)` so previously-interrupted files get their cross-file markdown.
</action>

<acceptance_criteria>
- `pipeline.py` `run_index()` calls `store.set_pipeline_stage()` after each pass stage
- Pass 1 sets `"chunked"` stage after processing each file
- Pass 2 sets `"relationships_extracted"` stage after processing each file  
- Pass 3 sets `"complete"` stage after processing each file
- Resume files (at `chunked` stage from previous run) are included in Pass 2 processing
- Resume files (at `relationships_extracted` stage from previous run) are included in Pass 3 processing
- Content hash changes override stage — changed files are re-processed from scratch regardless of stage
- Files at `complete` stage with unchanged content hash are skipped in all passes
- Running `glma index`, interrupting during Pass 2, then re-running `glma index` skips already-complete files and resumes from Pass 2 for chunked files
</acceptance_criteria>

---
