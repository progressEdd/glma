---
file_path: index/progress.py
language: python
last_indexed: 2026-04-13T20:15:23.740453+00:00
chunk_count: 6
content_hash: 4ec8d60808259ae78f0c925ba90e90377f93636585fb3db829723f64bdf21a0f
---

# index/progress.py

## Summary

Provides a Rich-based progress tracking system for the indexing pipeline, managing real-time status bars and final summaries. It tracks processing milestones via start/advance/finish methods while supporting a quiet mode to suppress all console output.

**AI Chunk Summaries:**
- **IndexProgress**: Manages a Rich-based progress bar and summary display for the indexing pipeline. It tracks file processing via `start`, `advance`, and `finish` methods, optionally suppressing all output if initialized in quiet mode.
- **__init__**: Initializes the progress display by configuring output suppression and setting up a Rich console instance. It initializes internal state trackers for the progress bar and task ID to `None`.
- **start**: Initializes and starts a Rich-based progress bar with custom columns for tracking file indexing. It takes the total file count and an optional description to create a task, provided quiet mode is disabled.
- **advance**: Increments the progress of a specific indexing task and optionally updates its display description with the provided filename. It requires both an active progress tracker and an assigned task to execute.
- **finish**: Stops the active progress tracker and prints a success message to the console if quiet mode is disabled. It accepts an optional custom completion string as input.
- **print_summary**: Outputs a formatted indexing summary to the console using provided file and chunk counts. It suppresses all output if the `quiet` flag is enabled.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| IndexProgress | class | L17-L111 |  |

## Chunks

### IndexProgress (class, L17-L111)

> *Summary: Manages a Rich-based progress bar and summary display for the indexing pipeline. It tracks file processing via `start`, `advance`, and `finish` methods, optionally suppressing all output if initialized in quiet mode.*

> **Calls:** ? (rich.progress) (INFERRED), ? (rich.progress) (INFERRED), ? (rich.progress) (INFERRED), ? (rich.progress) (INFERRED), ? (rich.progress) (INFERRED), ? (rich.progress) (INFERRED), ? (rich.progress) (INFERRED), ? (rich.console) (INFERRED), ? (typing) (INFERRED)

### __init__ (method, L29-L39)

> *Summary: Initializes the progress display by configuring output suppression and setting up a Rich console instance. It initializes internal state trackers for the progress bar and task ID to `None`.*

> **Calls:** ? (Console) (INFERRED)

### start (method, L41-L62)

> *Summary: Initializes and starts a Rich-based progress bar with custom columns for tracking file indexing. It takes the total file count and an optional description to create a task, provided quiet mode is disabled.*

> **Calls:** ? (self._progress.add_task) (INFERRED), ? (self._progress.start) (INFERRED), ? (TimeRemainingColumn) (INFERRED), ? (TimeElapsedColumn) (INFERRED), ? (TextColumn) (INFERRED), ? (TextColumn) (INFERRED), ? (BarColumn) (INFERRED), ? (TextColumn) (INFERRED), ? (SpinnerColumn) (INFERRED), ? (Progress) (INFERRED)

### advance (method, L64-L73)

> *Summary: Increments the progress of a specific indexing task and optionally updates its display description with the provided filename. It requires both an active progress tracker and an assigned task to execute.*

> **Calls:** ? (self._progress.advance) (INFERRED), ? (self._progress.update) (INFERRED)

### finish (method, L75-L84)

> *Summary: Stops the active progress tracker and prints a success message to the console if quiet mode is disabled. It accepts an optional custom completion string as input.*

> **Calls:** ? (self.console.print) (INFERRED), ? (self._progress.stop) (INFERRED)

### print_summary (method, L86-L111)

> *Summary: Outputs a formatted indexing summary to the console using provided file and chunk counts. It suppresses all output if the `quiet` flag is enabled.*

> **Calls:** ? (self.console.print) (INFERRED), ? (self.console.print) (INFERRED), ? (self.console.print) (INFERRED), ? (self.console.print) (INFERRED), ? (self.console.print) (INFERRED), ? (self.console.print) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| __init__ | ? (Console) | INFERRED | L37 |
| start | ? (self._progress.add_task) | INFERRED | L62 |
| start | ? (self._progress.start) | INFERRED | L61 |
| start | ? (TimeRemainingColumn) | INFERRED | L58 |
| start | ? (TimeElapsedColumn) | INFERRED | L57 |
| start | ? (TextColumn) | INFERRED | L56 |
| start | ? (TextColumn) | INFERRED | L55 |
| start | ? (BarColumn) | INFERRED | L54 |
| start | ? (TextColumn) | INFERRED | L53 |
| start | ? (SpinnerColumn) | INFERRED | L52 |
| start | ? (Progress) | INFERRED | L51 |
| advance | ? (self._progress.advance) | INFERRED | L73 |
| advance | ? (self._progress.update) | INFERRED | L72 |
| finish | ? (self.console.print) | INFERRED | L84 |
| finish | ? (self._progress.stop) | INFERRED | L82 |
| print_summary | ? (self.console.print) | INFERRED | L111 |
| print_summary | ? (self.console.print) | INFERRED | L110 |
| print_summary | ? (self.console.print) | INFERRED | L109 |
| print_summary | ? (self.console.print) | INFERRED | L108 |
| print_summary | ? (self.console.print) | INFERRED | L107 |
| print_summary | ? (self.console.print) | INFERRED | L106 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| rich.progress | INFERRED |
| rich.progress | INFERRED |
| rich.progress | INFERRED |
| rich.progress | INFERRED |
| rich.progress | INFERRED |
| rich.progress | INFERRED |
| rich.progress | INFERRED |
| rich.console | INFERRED |
| typing | INFERRED |
