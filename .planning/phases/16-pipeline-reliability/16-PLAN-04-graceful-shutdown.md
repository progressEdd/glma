---
wave: 2
depends_on:
  - 16-PLAN-02
  - 16-PLAN-03
files_modified:
  - src/glma/index/pipeline.py
  - src/glma/cli.py
requirements_addressed:
  - PIPE-04
---

# Plan 04: Graceful Shutdown on SIGINT/SIGTERM (PIPE-04)

## Objective
Register signal handlers at CLI entry that set a `threading.Event`. The pipeline checks this event between files in each pass — if set, it finishes the current file and exits cleanly with no partial writes.

## Tasks

### Task 4.1: Add shutdown_event parameter to run_index()

<read_first>
- 02-worktrees/glma/src/glma/index/pipeline.py — `run_index()` function signature and all three pass loops
</read_first>

<action>
1. Add `shutdown_event` parameter to `run_index()`:
   ```python
   def run_index(
       repo_root: Path,
       config: IndexConfig,
       store: Optional[LadybugStore] = None,
       progress: Optional[IndexProgress] = None,
       changed_files: Optional[list[tuple[Path, str]]] = None,
       deleted_paths: Optional[list[str]] = None,
       shutdown_event: Optional[threading.Event] = None,
   ) -> IndexResult:
   ```

   Add `import threading` at the top of the file (if not already imported).

2. **In Pass 1**, add shutdown check at the START of the file loop (before processing):
   ```python
   for filepath, language_name in source_files:
       if shutdown_event and shutdown_event.is_set():
           if progress:
               progress.console.print("[yellow]Interrupted. Finishing current file...[/yellow]")
           break
       # ... existing per-file processing ...
   ```
   
   Place the check as the FIRST thing in the loop, before any processing. This ensures we don't start a new file after the signal.

3. **In Pass 2**, same pattern — check at the start of the loop:
   ```python
   for filepath, language_name in source_files:
       if shutdown_event and shutdown_event.is_set():
           break
       # ... existing processing ...
   ```

4. **In Pass 3**, same pattern — check at the start of the loop.

5. **After all passes**, if `shutdown_event.is_set()`, print a resume hint:
   ```python
   if shutdown_event and shutdown_event.is_set():
       remaining = store.get_incomplete_files()
       if progress:
           progress.console.print(f"[yellow]Interrupted. {len(remaining)} files remaining. Run 'glma index' to resume.[/yellow]")
   ```

6. Return the partial `result` — the counts will reflect only what was completed.
</action>

<acceptance_criteria>
- `pipeline.py` `run_index()` accepts `shutdown_event: Optional[threading.Event] = None` parameter
- Each of the 3 pass loops checks `shutdown_event.is_set()` at the top and breaks if set
- When interrupted, the current file in progress completes (no mid-file interruption)
- A message is printed showing how many files remain: contains `"files remaining"` and `"glma index"`
- The function returns normally (doesn't raise) — callers get a partial `IndexResult`
- When `shutdown_event` is None (not provided), behavior is identical to current code
</acceptance_criteria>

---

### Task 4.2: Register signal handlers in CLI index command

<read_first>
- 02-worktrees/glma/src/glma/cli.py — `index()` command function (starts around line 60)
</read_first>

<action>
1. Add imports at the top of `cli.py`:
   ```python
   import signal
   import threading
   ```

2. Inside the `index()` command, BEFORE calling `run_index()`, create the event and register handlers:
   ```python
   # Signal handling for graceful shutdown
   shutdown_event = threading.Event()

   def _handle_signal(signum, frame):
       if shutdown_event.is_set():
           # Second signal — force exit
           console.print("[red]Force exit.[/red]")
           raise typer.Exit(1)
       shutdown_event.set()
       console.print("[yellow]Interrupt received. Finishing current file...[/yellow]")

   signal.signal(signal.SIGINT, _handle_signal)
   signal.signal(signal.SIGTERM, _handle_signal)
   ```

3. Pass `shutdown_event` to `run_index()`:
   ```python
   result = run_index(repo_path, cfg, progress=progress, shutdown_event=shutdown_event)
   ```

4. After `run_index()` returns, check if we were interrupted and handle the summarization skip:
   ```python
   if shutdown_event.is_set():
       console.print("[yellow]Indexing interrupted. Skipping summarization. Run 'glma index' to resume.[/yellow]")
       raise typer.Exit(0)
   ```
   Place this BEFORE the `if summarize:` block so that interrupted runs don't attempt summarization.
</action>

<acceptance_criteria>
- `cli.py` imports `signal` and `threading`
- `cli.py` `index()` command creates a `threading.Event()` and registers SIGINT/SIGTERM handlers
- Signal handler sets the event on first signal, force-exits on second signal
- `shutdown_event` is passed to `run_index()` call
- On interrupt, summarization is skipped and a message tells user to re-run
- First Ctrl+C prints "Finishing current file..." and waits for current file to complete
- Second Ctrl+C force-exits immediately
- Normal (non-interrupted) flow is completely unchanged
</acceptance_criteria>

---
