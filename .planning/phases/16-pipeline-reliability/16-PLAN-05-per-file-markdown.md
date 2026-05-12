---
wave: 2
depends_on:
  - 16-PLAN-03
  - 16-PLAN-04
files_modified:
  - src/glma/cli.py
requirements_addressed:
  - PIPE-05
---

# Plan 05: Per-File Markdown Output During Summarization (PIPE-05)

## Objective
Move markdown generation from a batch-at-end loop into the per-file summarization loop, so each file's markdown is written immediately after its summarization completes — not after all files are processed.

## Tasks

### Task 5.1: Move write_markdown into per-file summarization loop

<read_first>
- 02-worktrees/glma/src/glma/cli.py — `index()` command, specifically the summarization section (search for `# Summarization pass` and `# Regenerate static markdown files`)
- 02-worktrees/glma/src/glma/index/writer.py — `write_markdown()` function signature
</read_first>

<action>
1. In `cli.py`, find the summarization section. It currently has this structure:
   ```python
   # 1. Per-file summarization loop
   for file_path in sorted(indexed_files.keys()):
       chunks = store.get_chunks_for_file(file_path)
       if chunks:
           summarize_chunks(store, chunks, provider, max_chunk_chars=summ_cfg.max_chunk_chars)

   # 2. File-level summary generation loop
   for file_path in sorted(indexed_files.keys()):
       # ... generate file_summary ...
       store.update_file_summary(file_path, file_summary)

   # 3. Batch markdown regeneration loop
   for file_path in sorted(indexed_files.keys()):
       chunks = store.get_chunks_for_file(file_path)
       if chunks:
           file_rels = store.get_file_relationships(file_path)
           write_markdown(chunks, repo_path, cfg.output_dir, relationships=file_rels)
   ```

2. **Merge loops 2 and 3 into loop 1.** The new structure:
   ```python
   from glma.index.writer import write_markdown

   for file_path in sorted(indexed_files.keys()):
       chunks = store.get_chunks_for_file(file_path)
       if not chunks:
           continue

       # Summarize chunks
       summarize_chunks(store, chunks, provider, max_chunk_chars=summ_cfg.max_chunk_chars)

       # Generate file-level summary
       record = store.get_file_record(file_path)
       if not (record and record.file_summary):
           chunk_summaries = [c.summary for c in chunks if c.summary]
           if chunk_summaries:
               try:
                   context = f"File: {file_path}"
                   chunk_text = "\n".join(f"- {s}" for s in chunk_summaries)
                   prompt = (
                       f"Based on these per-function/class summaries, write a single 1-2 sentence summary of what this file does as a whole.\n"
                       f"\n{chunk_text}"
                   )
                   file_summary = provider.summarize(prompt, context)
                   if file_summary:
                       store.update_file_summary(file_path, file_summary)
               except Exception:
                   pass

       # Write markdown IMMEDIATELY after this file is summarized
       file_rels = store.get_file_relationships(file_path)
       write_markdown(chunks, repo_path, cfg.output_dir, relationships=file_rels)
   ```

3. **Delete the old separate loops** (file-level summary loop and batch markdown loop). They are now merged into the single loop above.

4. **Remove the duplicate `from glma.index.writer import write_markdown`** that was inside the old batch loop — it's now imported at the top of the summarization block (the import is already inside the `if summarize:` block).

5. **Update the completion message** — it can now say "Summarization complete: {N} files processed" without changing (already accurate).

6. **Add shutdown_event check** between files in the summarization loop:
   ```python
   for file_path in sorted(indexed_files.keys()):
       if shutdown_event and shutdown_event.is_set():
           console.print("[yellow]Summarization interrupted. Run 'glma index --summarize' to resume.[/yellow]")
           break
       # ... per-file processing ...
   ```
   Note: This works with the shutdown_event from Plan 04. If that plan hasn't been executed yet, the `shutdown_event` variable won't exist — use a safe check:
   ```python
   if 'shutdown_event' in dir() and shutdown_event and shutdown_event.is_set():
   ```
   Actually, better: just define `shutdown_event = None` at the top of the function before the signal handler setup, so it's always available:
   ```python
   shutdown_event = None  # Will be set if signal handlers are registered
   ```
   Then check `if shutdown_event and shutdown_event.is_set():`.
</action>

<acceptance_criteria>
- `cli.py` has a SINGLE loop in the summarization section (not 3 separate loops)
- `write_markdown()` is called inside the per-file loop, AFTER `summarize_chunks()` and file-level summary generation for that file
- The old batch-at-end markdown regeneration loop is REMOVED
- After summarizing file A but before file B, file A's markdown file exists on disk
- Shutdown check is present between files in the summarization loop
- Completion message unchanged: contains `"Summarization complete"`
</acceptance_criteria>

---
