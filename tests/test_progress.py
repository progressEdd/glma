"""Tests for progress display."""

from io import StringIO

from rich.console import Console

from glma.index.progress import IndexProgress


class TestQuietMode:
    """Test that quiet mode suppresses output."""

    def test_quiet_start(self):
        progress = IndexProgress(quiet=True)
        progress.start(10)
        # Should not raise

    def test_quiet_advance(self):
        progress = IndexProgress(quiet=True)
        progress.start(10)
        progress.advance("test.py")
        # Should not raise

    def test_quiet_finish(self):
        progress = IndexProgress(quiet=True)
        progress.start(10)
        progress.finish()
        # Should not raise

    def test_quiet_summary(self):
        progress = IndexProgress(quiet=True)
        progress.print_summary(10, 50, 5, 2, 3)
        # Should not raise


class TestNonQuietMode:
    """Test non-quiet mode produces output."""

    def test_finish_shows_checkmark(self):
        output = StringIO()
        console = Console(file=output, force_terminal=True)
        progress = IndexProgress(quiet=False, console=console)
        progress.start(5)
        progress.finish("Done")
        assert "Done" in output.getvalue()

    def test_summary_shows_counts(self):
        output = StringIO()
        console = Console(file=output, force_terminal=True)
        progress = IndexProgress(quiet=False, console=console)
        progress.start(10)
        progress.finish()
        progress.print_summary(
            total_files=10,
            total_chunks=50,
            new_files=5,
            updated_files=2,
            skipped_files=3,
        )
        text = output.getvalue()
        assert "10" in text  # total files
        assert "50" in text  # total chunks
        assert "5" in text   # new files
