---
wave: 3
depends_on:
  - 16-PLAN-01
files_modified:
  - src/glma/index/progress.py
  - src/glma/summarize/pipeline.py
  - src/glma/cli.py
requirements_addressed:
  - PIPE-06
---

# Plan 06: Summarization Progress Display (PIPE-06)

## Objective
Create a `SummarizeProgress` class (following the `IndexProgress` pattern) that shows a Rich progress bar during the summarization pass with per-chunk status, current file+chunk name, and running counts of done/skipped/failed.

## Tasks

### Task 6.1: Create SummarizeProgress class

<read_first>
- 02-worktrees/glma/src/glma/index/progress.py — `IndexProgress` class (111 lines, full file)
- 02-worktrees/glma/src/glma/summarize/pipeline.py — `summarize_chunks()` function to understand the counting variables (summarized_count, skipped_count, failed_count)
</read_first>

<action>
Create `SummarizeProgress` in `src/glma/index/progress.py` (same module as `IndexProgress`):

```python
class SummarizeProgress:
    """Manages progress display for the summarization pipeline.

    Shows a Rich progress bar with:
    - Spinner
    - Current file and chunk name in description
    - Progress bar
    - Running counts of done/skipped/failed
    """

    def __init__(self, quiet: bool = False, console: Optional[Console] = None):
        self.quiet = quiet
        self.console = console or Console()
        self._progress: Optional[Progress] = None
        self._task: Optional[TaskID] = None
        self._done: int = 0
        self._skipped: int = 0
        self._failed: int = 0

    def start(self, total_chunks: int, description: str = "Summarizing") -> None:
        if self.quiet:
            return
        self._progress = Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("({task.completed}/{task.total} chunks)"),
            TimeElapsedColumn(),
            console=self.console,
        )
        self._progress.start()
        self._task = self._progress.add_task(description, total=total_chunks)

    def advance(self, file_path: str = "", chunk_name: str = "", status: str = "done") -> None:
        """Advance progress by one chunk.

        Args:
            file_path: Current file path for description.
            chunk_name: Current chunk name for description.
            status: One of 'done', 'skipped', 'failed'.
        """
        if status == "done":
            self._done += 1
        elif status == "skipped":
            self._skipped += 1
        elif status == "failed":
            self._failed += 1

        if self._progress and self._task is not None:
            short_path = file_path.split("/")[-1] if "/" in file_path else file_path
            desc = f"Summarizing: {short_path} → {chunk_name}  ✓{self._done} ⊘{self._skipped} ✗{self._failed}"
            self._progress.update(self._task, description=desc)
            self._progress.advance(self._task)

    def finish(self, message: str = "Summarization complete") -> None:
        if self._progress:
            self._progress.stop()
        if not self.quiet:
            self.console.print(f"[bold green]✓[/bold green] {message}")

    def print_summary(
        self,
        summarized: int = 0,
        decomposed: int = 0,
        skipped: int = 0,
        failed: int = 0,
    ) -> None:
        if self.quiet:
            return
        self.console.print()
        self.console.print(f"  Summarized:    {summarized}")
        if decomposed:
            self.console.print(f"  Decomposed:    {decomposed}")
        self.console.print(f"  Skipped:       {skipped}")
        self.console.print(f"  Failed:        {failed}")
```

No changes to `IndexProgress` — just add the new class in the same file.
</action>

<acceptance_criteria>
- `progress.py` contains `class SummarizeProgress:` with methods `start()`, `advance()`, `finish()`, `print_summary()`
- `SummarizeProgress.advance()` accepts `file_path`, `chunk_name`, and `status` parameters
- Progress description shows format like `Summarizing: auth.py → verify_token  ✓28 ⊘5 ✗1`
- Uses Rich `Progress` with `SpinnerColumn`, `TextColumn`, `BarColumn`, `TimeElapsedColumn`
- `IndexProgress` class is unchanged
</acceptance_criteria>

---

### Task 6.2: Integrate SummarizeProgress into summarize_chunks()

<read_first>
- 02-worktrees/glma/src/glma/summarize/pipeline.py — `summarize_chunks()` function (full function, ~50 lines of main logic)
</read_first>

<action>
1. Add `progress` parameter to `summarize_chunks()`:
   ```python
   def summarize_chunks(
       store: LadybugStore,
       chunks: list[Chunk],
       provider: Protocol,
       max_chunk_chars: int = 3000,
       progress: Optional['SummarizeProgress'] = None,
   ) -> list[Chunk]:
   ```
   Add the import for type hinting at the top or use `TYPE_CHECKING`:
   ```python
   from __future__ import annotations
   from typing import TYPE_CHECKING
   if TYPE_CHECKING:
       from glma.index.progress import SummarizeProgress
   ```

2. After the initial skip counting, start progress:
   ```python
   # Count chunks needing summarization for progress total
   needs_summary = sum(1 for c in chunks if not c.summary)
   if progress:
       progress.start(len(chunks))
   ```

3. In the chunk loop, update progress for each outcome:
   - **Skip** (already has summary): `if progress: progress.advance(chunk.file_path, chunk.name, "skipped")`
   - **Success**: `if progress: progress.advance(chunk.file_path, chunk.name, "done")`
   - **Failed**: `if progress: progress.advance(chunk.file_path, chunk.name, "failed")`
   - **Decomposed** (success via decomposition): `if progress: progress.advance(chunk.file_path, chunk.name, "done")`

4. After the loop, call `finish()` and `print_summary()`:
   ```python
   if progress:
       progress.finish()
       progress.print_summary(
           summarized=summarized_count,
           decomposed=decomposed_count,
           skipped=skipped_count,
           failed=failed_count,
       )
   ```
</action>

<acceptance_criteria>
- `summarize/pipeline.py` `summarize_chunks()` accepts `progress` parameter (optional, default None)
- Progress is started with total chunk count before the loop
- Progress is advanced for each chunk with correct status (done/skipped/failed)
- Progress is finished and summary printed after the loop
- When `progress` is None, behavior is identical to current code (no changes to output)
- Existing logging is unchanged (logger.info still fires)
</acceptance_criteria>

---

### Task 6.3: Wire SummarizeProgress in CLI

<read_first>
- 02-worktrees/glma/src/glma/cli.py — `index()` command, the `if summarize:` block
</read_first>

<action>
1. Import `SummarizeProgress` alongside `IndexProgress`:
   ```python
   from glma.index.progress import IndexProgress, SummarizeProgress
   ```

2. In the summarization section, create a `SummarizeProgress` instance:
   ```python
   summ_progress = SummarizeProgress(quiet=cfg.quiet, console=console)
   ```

3. Pass it to `summarize_chunks()`:
   ```python
   for file_path in sorted(indexed_files.keys()):
       chunks = store.get_chunks_for_file(file_path)
       if chunks:
           summarize_chunks(store, chunks, provider, max_chunk_chars=summ_cfg.max_chunk_chars, progress=summ_progress)
           # ... file-level summary + markdown write (from Plan 05) ...
   ```
   
   Note: Progress will be started/stopped for each file's chunk batch. This is fine — each file's summarization gets its own progress bar.

   **ALTERNATIVE (better UX):** Create a single progress bar for the entire summarization pass. Pre-count total chunks across all files, start progress once, and advance across all files. This avoids the progress bar flickering between files.

   Implementation:
   ```python
   # Pre-count total chunks
   total_chunks = 0
   for file_path in sorted(indexed_files.keys()):
       chunks = store.get_chunks_for_file(file_path)
       total_chunks += len(chunks)
   
   summ_progress = SummarizeProgress(quiet=cfg.quiet, console=console)
   summ_progress.start(total_chunks)
   
   for file_path in sorted(indexed_files.keys()):
       chunks = store.get_chunks_for_file(file_path)
       if chunks:
           summarize_chunks(store, chunks, provider, max_chunk_chars=summ_cfg.max_chunk_chars, progress=summ_progress)
           # ... file-level summary + markdown write ...
   
   summ_progress.print_summary(...)
   ```
   
   But this means `summarize_chunks()` shouldn't call `start()`/`finish()` — only `advance()`. Adjust the contract: if `progress` is already started (has a task), `summarize_chunks()` only calls `advance()`, not `start()`/`finish()`.

   Simplest approach: let the CLI manage `start()`/`finish()` and have `summarize_chunks()` only call `advance()`. This is cleaner.
</action>

<acceptance_criteria>
- `cli.py` imports `SummarizeProgress`
- `cli.py` creates `SummarizeProgress` instance and passes it to `summarize_chunks()`
- Progress bar is visible during `glma index --summarize`
- Progress shows current file and chunk name with counts like `✓28 ⊘5 ✗1`
- When `--quiet` is set, no progress output is shown
</acceptance_criteria>

---
