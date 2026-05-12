"""Tests for the file watching module."""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from watchfiles import Change

from glma.models import IndexConfig, WatchConfig
from glma.watch import _classify_events, _detect_renames, _is_supported_file


class TestClassifyEvents:
    """Tests for _classify_events."""

    def test_created_files(self):
        changes = {(Change.added, "/repo/src/new.py")}
        created, modified, deleted = _classify_events(changes)
        assert created == {Path("/repo/src/new.py")}
        assert modified == set()
        assert deleted == set()

    def test_modified_files(self):
        changes = {(Change.modified, "/repo/src/existing.py")}
        created, modified, deleted = _classify_events(changes)
        assert created == set()
        assert modified == {Path("/repo/src/existing.py")}
        assert deleted == set()

    def test_deleted_files(self):
        changes = {(Change.deleted, "/repo/src/old.py")}
        created, modified, deleted = _classify_events(changes)
        assert created == set()
        assert modified == set()
        assert deleted == {Path("/repo/src/old.py")}

    def test_mixed_events(self):
        changes = {
            (Change.added, "/repo/src/a.py"),
            (Change.modified, "/repo/src/b.py"),
            (Change.deleted, "/repo/src/c.py"),
        }
        created, modified, deleted = _classify_events(changes)
        assert len(created) == 1
        assert len(modified) == 1
        assert len(deleted) == 1

    def test_duplicate_paths_latest_wins(self):
        """If same path appears as both added and modified, both sets contain it."""
        changes = {
            (Change.added, "/repo/src/x.py"),
            (Change.modified, "/repo/src/x.py"),
        }
        created, modified, deleted = _classify_events(changes)
        assert Path("/repo/src/x.py") in created
        assert Path("/repo/src/x.py") in modified


class TestDetectRenames:
    """Tests for _detect_renames."""

    def test_rename_detected_by_same_basename(self):
        created = {Path("/repo/src/new_auth.py")}
        deleted = {Path("/repo/src/old_auth.py")}
        # Different basenames — no rename
        renames, rem_created, rem_deleted = _detect_renames(created, deleted)
        assert renames == []
        assert len(rem_created) == 1
        assert len(rem_deleted) == 1

    def test_rename_same_basename_different_dir(self):
        created = {Path("/repo/src/utils/helpers.py")}
        deleted = {Path("/repo/lib/helpers.py")}
        renames, rem_created, rem_deleted = _detect_renames(created, deleted)
        assert len(renames) == 1
        assert renames[0] == (Path("/repo/lib/helpers.py"), Path("/repo/src/utils/helpers.py"))
        assert len(rem_created) == 0
        assert len(rem_deleted) == 0

    def test_no_renames_when_empty(self):
        renames, rem_created, rem_deleted = _detect_renames(set(), set())
        assert renames == []
        assert rem_created == set()
        assert rem_deleted == set()

    def test_multiple_events_no_match(self):
        created = {Path("/repo/a.py"), Path("/repo/b.py")}
        deleted = {Path("/repo/c.py"), Path("/repo/d.py")}
        renames, rem_created, rem_deleted = _detect_renames(created, deleted)
        assert renames == []
        assert len(rem_created) == 2
        assert len(rem_deleted) == 2


class TestIsSupportedFile:
    """Tests for _is_supported_file."""

    def test_python_file_supported(self, tmp_path):
        config = IndexConfig()
        py_file = tmp_path / "test.py"
        py_file.write_text("def hello(): pass")
        assert _is_supported_file(py_file, config) is True

    def test_c_file_supported(self, tmp_path):
        config = IndexConfig()
        c_file = tmp_path / "test.c"
        c_file.write_text("int main() { return 0; }")
        assert _is_supported_file(c_file, config) is True

    def test_non_source_file_not_supported(self, tmp_path):
        config = IndexConfig()
        txt_file = tmp_path / "readme.txt"
        txt_file.write_text("hello")
        assert _is_supported_file(txt_file, config) is False

    def test_markdown_file_not_supported(self, tmp_path):
        config = IndexConfig()
        md_file = tmp_path / "doc.md"
        md_file.write_text("# Hello")
        assert _is_supported_file(md_file, config) is False


class TestWatchCLI:
    """Integration tests for the watch CLI command."""

    def test_watch_requires_index(self, tmp_path):
        """Watch command should fail if no index exists."""
        from typer.testing import CliRunner
        from glma.cli import app

        runner = CliRunner()
        result = runner.invoke(app, ["watch", str(tmp_path)])
        assert result.exit_code == 4

    def test_watch_in_help(self):
        """Watch command appears in CLI help."""
        from typer.testing import CliRunner
        from glma.cli import app

        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        assert "watch" in result.output.lower()
