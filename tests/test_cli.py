"""Tests for CLI interface."""

import subprocess
import sys


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
