"""Progress display for indexing operations."""

from typing import Optional

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)


class IndexProgress:
    """Manages progress display for the indexing pipeline.

    Uses Rich progress bar showing:
    - Spinner
    - Description text
    - Progress bar
    - Percentage
    - Elapsed time
    - Remaining time estimate
    """

    def __init__(self, quiet: bool = False, console: Optional[Console] = None):
        """Initialize progress display.

        Args:
            quiet: If True, suppress all output.
            console: Optional Rich console (creates one if not provided).
        """
        self.quiet = quiet
        self.console = console or Console()
        self._progress: Optional[Progress] = None
        self._task: Optional[TaskID] = None

    def start(self, total_files: int, description: str = "Indexing") -> None:
        """Start progress tracking.

        Args:
            total_files: Total number of files to process.
            description: Description text for the progress bar.
        """
        if self.quiet:
            return

        self._progress = Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("({task.completed}/{task.total} files)"),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=self.console,
        )
        self._progress.start()
        self._task = self._progress.add_task(description, total=total_files)

    def advance(self, filename: str = "") -> None:
        """Advance progress by one file.

        Args:
            filename: Optional filename to show in description.
        """
        if self._progress and self._task is not None:
            if filename:
                self._progress.update(self._task, description=f"Indexing: {filename}")
            self._progress.advance(self._task)

    def finish(self, message: str = "Indexing complete") -> None:
        """Stop progress and show completion message.

        Args:
            message: Completion message to display.
        """
        if self._progress:
            self._progress.stop()
        if not self.quiet:
            self.console.print(f"[bold green]✓[/bold green] {message}")

    def print_summary(
        self,
        total_files: int,
        total_chunks: int,
        new_files: int,
        updated_files: int,
        skipped_files: int,
    ) -> None:
        """Print indexing summary.

        Args:
            total_files: Total source files found.
            total_chunks: Total chunks extracted.
            new_files: Newly indexed files.
            updated_files: Re-indexed (changed) files.
            skipped_files: Unchanged files skipped.
        """
        if self.quiet:
            return

        self.console.print()
        self.console.print(f"  Files scanned:   {total_files}")
        self.console.print(f"  New:             {new_files}")
        self.console.print(f"  Updated:         {updated_files}")
        self.console.print(f"  Unchanged:       {skipped_files}")
        self.console.print(f"  Total chunks:    {total_chunks}")
