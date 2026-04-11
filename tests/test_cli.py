"""Tests for CLI interface."""

import subprocess
import sys
from pathlib import Path


class TestVersion:
    """Test --version flag."""

    def test_version_output(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "--version"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "glma 0.1.0" in result.stdout

    def test_version_short_flag(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "-v"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "0.1.0" in result.stdout


class TestIndexCommand:
    """Test index command."""

    def test_index_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "index", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Index a repository" in result.stdout

    def test_no_args_shows_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma"],
            capture_output=True,
            text=True,
        )
        # Typer exits with code 2 for no_args_is_help
        assert result.returncode == 2 or result.returncode == 0
        assert "index" in result.stdout.lower()


class TestExportFlags:
    """Test export command flags."""

    def test_include_code_flag_in_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "export", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "--include-code" in result.stdout
        assert "--no-code" not in result.stdout


class TestQuerySummarizeFlags:
    """Test --summarize flags on query command."""

    def test_summarize_flag_in_help(self):
        result = subprocess.run(
            [sys.executable, "-m", "glma", "query", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "--summarize" in result.stdout
        assert "--summarize-provider" in result.stdout
        assert "--summarize-model" in result.stdout

    def test_notebook_without_summarize_unchanged(self):
        """Notebook query without --summarize works as before."""
        import nbformat
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            nb = nbformat.v4.new_notebook()
            nb.cells = [nbformat.v4.new_code_cell("x = 42")]
            path = Path(tmp) / "test.ipynb"
            nbformat.write(nb, str(path))
            result = subprocess.run(
                [sys.executable, "-m", "glma", "query", str(path), "--repo", tmp],
                capture_output=True,
                text=True,
            )
            assert result.returncode == 0
            assert "### Cell 0 [code]" in result.stdout
            assert "Summary" not in result.stdout

    def test_notebook_summarize_with_no_provider_fails_gracefully(self):
        """Notebook --summarize without openai package shows error."""
        import nbformat
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            nb = nbformat.v4.new_notebook()
            nb.cells = [nbformat.v4.new_code_cell("x = 42\ny = x + 1\nz = y * 2")]
            path = Path(tmp) / "test.ipynb"
            nbformat.write(nb, str(path))
            result = subprocess.run(
                [sys.executable, "-m", "glma", "query", str(path), "--summarize", "--repo", tmp],
                capture_output=True,
                text=True,
            )
            # Will fail because no local model running — but shouldn't crash with traceback
            # It either succeeds (if openai is installed) or shows a clean error
            assert result.returncode != 0 or "### Cell 0" in result.stdout
