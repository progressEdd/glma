"""Tests for the air-gapped export module."""

import tarfile
import io
from pathlib import Path

import pytest

from glma.models import Chunk, ChunkType, ExportConfig
from glma.export import (
    generate_rule_summary,
    generate_index_md,
    generate_relationships_md,
    generate_architecture_md,
    _format_export_file,
    _write_files_to_dir,
)


def _make_chunk(
    name: str = "test_func",
    chunk_type: ChunkType = ChunkType.FUNCTION,
    file_path: str = "src/test.py",
    start_line: int = 1,
    end_line: int = 10,
) -> Chunk:
    """Helper to create a test chunk."""
    return Chunk(
        id=f"{file_path}::{chunk_type.value}::{name}::{start_line}",
        file_path=file_path,
        chunk_type=chunk_type,
        name=name,
        content=f"def {name}(): pass",
        summary=None,
        start_line=start_line,
        end_line=end_line,
        content_hash="abc123",
        parent_id=None,
    )


class TestRuleSummary:
    """Tests for generate_rule_summary."""

    def test_function_summary(self):
        chunks = [_make_chunk("authenticate"), _make_chunk("verify_token")]
        summary = generate_rule_summary("src/auth.py", chunks, [])
        assert "2 function(s)" in summary
        assert "authenticate" in summary
        assert "verify_token" in summary

    def test_class_summary(self):
        chunks = [_make_chunk("TokenStore", ChunkType.CLASS)]
        summary = generate_rule_summary("src/store.py", chunks, [])
        assert "1 class(es)" in summary
        assert "TokenStore" in summary

    def test_import_summary(self):
        chunks = [_make_chunk()]
        rels = [{"rel_type": "imports", "target_name": "jwt"}, {"rel_type": "imports", "target_name": "os"}]
        summary = generate_rule_summary("src/auth.py", chunks, rels)
        assert "Imports:" in summary
        assert "jwt" in summary

    def test_empty_file(self):
        summary = generate_rule_summary("empty.py", [], [])
        assert "0 chunk" in summary

    def test_many_functions_truncation(self):
        chunks = [_make_chunk(f"func_{i}") for i in range(15)]
        summary = generate_rule_summary("big.py", chunks, [])
        assert "15 function(s)" in summary
        assert "more" in summary  # Truncation indicator

    def test_shared_module_identical(self):
        """Verify shared module produces same result as old location."""
        from glma.summaries import generate_rule_summary as shared_summary
        chunks = [_make_chunk("hello")]
        assert generate_rule_summary("test.py", chunks, []) == shared_summary("test.py", chunks, [])


class TestFormatExportFile:
    """Tests for _format_export_file."""

    def test_metadata_header(self):
        chunks = [_make_chunk()]
        config = ExportConfig()
        from glma.models import FileRecord, Language
        record = FileRecord(
            path="src/test.py",
            language=Language.PYTHON,
            content_hash="abc",
            last_indexed="2026-04-09T12:00:00Z",
            chunk_count=1,
        )
        md = _format_export_file("src/test.py", record, chunks, [], config)
        assert "---" in md
        assert "file_path: src/test.py" in md
        assert "language: python" in md
        assert "chunk_count: 1" in md

    def test_summary_section(self):
        chunks = [_make_chunk("hello")]
        config = ExportConfig()
        md = _format_export_file("src/test.py", None, chunks, [], config)
        assert "## Summary" in md
        assert "hello" in md

    def test_code_included_when_requested(self):
        chunks = [_make_chunk("my_func")]
        config = ExportConfig(include_code=True)
        md = _format_export_file("src/test.py", None, chunks, [], config)
        assert "```python" in md
        assert "def my_func(): pass" in md

    def test_code_excluded(self):
        chunks = [_make_chunk("my_func")]
        config = ExportConfig(include_code=False)
        md = _format_export_file("src/test.py", None, chunks, [], config)
        assert "Code omitted" in md
        assert "```python" not in md

    def test_relationships_section(self):
        chunks = [_make_chunk("caller")]
        rels = [{
            "source_id": chunks[0].id,
            "source_name": "caller",
            "rel_type": "calls",
            "confidence": "DIRECT",
            "source_line": 5,
            "target_name": "callee",
            "target_id": "other::function::callee::1",
        }]
        config = ExportConfig()
        md = _format_export_file("src/test.py", None, chunks, rels, config)
        assert "## Relationships" in md
        assert "Outgoing Calls" in md
        assert "caller" in md
        assert "callee" in md


class TestGenerateIndexMd:
    """Tests for generate_index_md."""

    def test_basic_index(self):
        indexed_files = {"src/a.py": "hash1", "src/b.c": "hash2"}
        file_data = {
            "src/a.py": {
                "chunks": [_make_chunk("func_a", file_path="src/a.py")],
                "summary": "1 function.",
                "record": None,
            },
            "src/b.c": {
                "chunks": [_make_chunk("main_c", file_path="src/b.c")],
                "summary": "Entry point.",
                "record": None,
            },
        }
        md = generate_index_md(indexed_files, file_data)
        assert "# Codebase Index" in md
        assert "**Total Files:** 2" in md
        assert "**Total Chunks:** 2" in md
        assert "[src/a.py](src/a.py.md)" in md
        assert "[src/b.c](src/b.c.md)" in md

    def test_statistics(self):
        file_data = {
            "test.py": {
                "chunks": [
                    _make_chunk("f1", ChunkType.FUNCTION),
                    _make_chunk("C1", ChunkType.CLASS),
                ],
                "summary": "",
                "record": None,
            },
        }
        md = generate_index_md({"test.py": "h"}, file_data)
        assert "Total functions: 1" in md
        assert "Total classes: 1" in md


class TestDirectoryOutput:
    """Tests for _write_files_to_dir."""

    def test_creates_nested_structure(self, tmp_path):
        file_exports = {
            "src/auth/login.py": "# login.py\n",
            "src/main.c": "# main.c\n",
        }
        _write_files_to_dir(tmp_path, file_exports, "# Index", "# Rels", "# Arch")

        assert (tmp_path / "src" / "auth" / "login.py.md").exists()
        assert (tmp_path / "src" / "main.c.md").exists()
        assert (tmp_path / "INDEX.md").exists()
        assert (tmp_path / "RELATIONSHIPS.md").exists()
        assert (tmp_path / "ARCHITECTURE.md").exists()

    def test_file_content_correct(self, tmp_path):
        file_exports = {"test.py": "# Hello World\n"}
        _write_files_to_dir(tmp_path, file_exports, "# Index", "# Rels", "# Arch")

        content = (tmp_path / "test.py.md").read_text()
        assert "# Hello World" in content

        index_content = (tmp_path / "INDEX.md").read_text()
        assert "# Index" in index_content

        arch_content = (tmp_path / "ARCHITECTURE.md").read_text()
        assert "# Arch" in arch_content


class TestExportCLI:
    """Integration tests for the export CLI command."""

    def test_export_requires_index(self, tmp_path):
        """Export command should fail if no index exists."""
        from typer.testing import CliRunner
        from glma.cli import app

        runner = CliRunner()
        result = runner.invoke(app, ["export", str(tmp_path)])
        assert result.exit_code == 4

    def test_export_in_help(self):
        """Export command appears in CLI help."""
        from typer.testing import CliRunner
        from glma.cli import app

        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        assert "export" in result.output.lower()


class TestChunkSummaryRendering:
    """Tests for AI chunk summary rendering in export output."""

    def test_chunk_summary_rendered_in_export(self):
        """Chunks with summary show blockquote when code is omitted."""
        chunk = _make_chunk("my_func")
        chunk.summary = "AI-generated summary of this chunk"
        config = ExportConfig(include_code=False)
        md = _format_export_file("src/test.py", None, [chunk], [], config)
        assert "> *Summary: AI-generated summary of this chunk*" in md
        assert "*(Code omitted" not in md

    def test_chunk_summary_with_code_included(self):
        """Chunks with summary AND code both appear."""
        chunk = _make_chunk("my_func")
        chunk.summary = "Test summary"
        config = ExportConfig(include_code=True)
        md = _format_export_file("src/test.py", None, [chunk], [], config)
        assert "> *Summary: Test summary*" in md
        assert "```python" in md

    def test_chunk_without_summary_shows_omitted(self):
        """Chunks without summary show code omitted when include_code=False."""
        chunk = _make_chunk("my_func")
        config = ExportConfig(include_code=False)
        md = _format_export_file("src/test.py", None, [chunk], [], config)
        assert "*(Code omitted" in md

    def test_ai_summaries_shows_chunk_overview(self):
        """Files with AI summaries show AI Chunk Summaries section."""
        chunk1 = _make_chunk("func_a")
        chunk1.summary = "Summary A"
        chunk2 = _make_chunk("func_b")
        chunk2.summary = "Summary B"
        config = ExportConfig(ai_summaries=True)
        md = _format_export_file("src/test.py", None, [chunk1, chunk2], [], config)
        assert "**AI Chunk Summaries:**" in md
        assert "- **func_a**: Summary A" in md
        assert "- **func_b**: Summary B" in md


def _make_arch_file_data() -> dict[str, dict]:
    """Helper to create sample file_data for architecture tests."""
    return {
        "src/app/db/store.py": {
            "chunks": [
                _make_chunk("Database", ChunkType.CLASS, "src/app/db/store.py"),
                _make_chunk("connect", file_path="src/app/db/store.py"),
            ],
            "relationships": [],
            "summary": "Database connection manager.",
            "record": None,
        },
        "src/app/db/migrate.py": {
            "chunks": [
                _make_chunk("run_migrations", file_path="src/app/db/migrate.py"),
            ],
            "relationships": [],
            "summary": "Database migration runner.",
            "record": None,
        },
        "src/app/cli.py": {
            "chunks": [
                _make_chunk("main", file_path="src/app/cli.py"),
                _make_chunk("parse_args", file_path="src/app/cli.py"),
            ],
            "relationships": [
                {
                    "source_id": "src/app/cli.py::function::main::1",
                    "source_name": "main",
                    "rel_type": "imports",
                    "target_name": "store",
                    "target_id": "src/app/db/store.py::class::Database::1",
                    "direction": "outgoing",
                },
            ],
            "summary": "CLI entry point.",
            "record": None,
        },
        "src/app/__main__.py": {
            "chunks": [
                Chunk(
                    id="src/app/__main__.py::function::_run::1",
                    file_path="src/app/__main__.py",
                    chunk_type=ChunkType.FUNCTION,
                    name="_run",
                    content='if __name__ == "__main__": main()',
                    summary=None,
                    start_line=1,
                    end_line=3,
                    content_hash="main123",
                    parent_id=None,
                ),
            ],
            "relationships": [
                {
                    "source_id": "src/app/__main__.py::function::_run::1",
                    "source_name": "_run",
                    "rel_type": "imports",
                    "target_name": "cli",
                    "target_id": "src/app/cli.py::function::main::1",
                    "direction": "outgoing",
                },
            ],
            "summary": "Package entry point.",
            "record": None,
        },
    }


class TestGenerateArchitectureMd:
    """Tests for generate_architecture_md."""

    def test_basic_architecture_generation(self):
        """All 4 sections present in generated output."""
        file_data = _make_arch_file_data()
        md = generate_architecture_md(file_data)

        assert "# Architecture Overview" in md
        assert "**Generated:**" in md
        assert "**Total Modules:**" in md
        assert "## Project Structure Overview" in md
        assert "## Module Dependencies" in md
        assert "## Entry Points" in md
        assert "## Key Interfaces" in md

    def test_entry_point_detection(self):
        """Entry points detected via convention and fan-in."""
        file_data = _make_arch_file_data()
        md = generate_architecture_md(file_data)

        # __main__.py is a convention-based entry point
        assert "__main__.py" in md
        assert "detected entry point" in md

        # cli.py is detected by convention (filename)
        assert "cli.py" in md

    def test_module_grouping(self):
        """Files grouped by directory into modules."""
        file_data = {
            "src/app/db/store.py": {
                "chunks": [_make_chunk("Database", ChunkType.CLASS, "src/app/db/store.py")],
                "relationships": [],
                "summary": "DB store.",
                "record": None,
            },
            "src/app/db/migrate.py": {
                "chunks": [_make_chunk("run_migrations", file_path="src/app/db/migrate.py")],
                "relationships": [],
                "summary": "DB migrate.",
                "record": None,
            },
            "src/app/api/routes.py": {
                "chunks": [_make_chunk("Router", ChunkType.CLASS, "src/app/api/routes.py")],
                "relationships": [],
                "summary": "API routes.",
                "record": None,
            },
            "src/app/api/auth.py": {
                "chunks": [_make_chunk("authenticate", file_path="src/app/api/auth.py")],
                "relationships": [],
                "summary": "API auth.",
                "record": None,
            },
        }
        md = generate_architecture_md(file_data)

        # Two module groupings: db and api
        assert "### Module: db" in md
        assert "### Module: api" in md
        # Both db files under same module
        assert "store.py" in md
        assert "migrate.py" in md
        # Both api files under same module
        assert "routes.py" in md
        assert "auth.py" in md

    def test_chunk_summaries_used_in_narrative(self):
        """AI chunk summaries appear in module narratives."""
        chunk1 = _make_chunk("Database", ChunkType.CLASS, "src/app/db/store.py")
        chunk1.summary = "Manages database connections and queries"
        chunk2 = _make_chunk("connect", file_path="src/app/db/store.py")
        chunk2.summary = "Establishes connection to the database"

        file_data = {
            "src/app/db/store.py": {
                "chunks": [chunk1, chunk2],
                "relationships": [],
                "summary": "Database module.",
                "record": None,
            },
        }
        md = generate_architecture_md(file_data)

        assert "Manages database connections" in md
        assert "Establishes connection" in md

    def test_single_file_codebase(self):
        """Single file does not crash and produces valid output."""
        file_data = {
            "main.py": {
                "chunks": [_make_chunk("main", file_path="main.py")],
                "relationships": [],
                "summary": "Entry point.",
                "record": None,
            },
        }
        md = generate_architecture_md(file_data)

        assert "# Architecture Overview" in md
        assert "**Total Modules:** 1" in md
        assert "*(no external dependencies)*" in md

    def test_architecture_md_in_directory_output(self, tmp_path):
        """ARCHITECTURE.md is written to directory output."""
        file_exports = {"test.py": "# Hello\n"}
        _write_files_to_dir(tmp_path, file_exports, "# Index", "# Rels", "# Arch")

        assert (tmp_path / "ARCHITECTURE.md").exists()
        assert (tmp_path / "ARCHITECTURE.md").read_text() == "# Arch"
