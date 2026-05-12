"""Tests for query formatter."""

import pytest

from glma.models import Chunk, ChunkType, FileRecord, Language
from glma.query.formatter import format_compact_output


@pytest.fixture
def sample_file_record() -> FileRecord:
    return FileRecord(
        path="test_file.py",
        language=Language.PYTHON,
        content_hash="abc123def456",
        last_indexed="2026-04-09T10:00:00+00:00",
        chunk_count=2,
    )


@pytest.fixture
def sample_chunks() -> list[Chunk]:
    return [
        Chunk(
            id="test_file.py::function::hello::1",
            file_path="test_file.py",
            chunk_type=ChunkType.FUNCTION,
            name="hello",
            content='def hello():\n    """Say hello."""\n    pass',
            start_line=1,
            end_line=3,
            content_hash="hash1",
            attached_comments=['"""Say hello."""'],
        ),
        Chunk(
            id="test_file.py::class::Greeter::5",
            file_path="test_file.py",
            chunk_type=ChunkType.CLASS,
            name="Greeter",
            content="class Greeter:\n    pass",
            start_line=5,
            end_line=6,
            content_hash="hash2",
        ),
    ]


def test_format_compact_basic(sample_file_record, sample_chunks):
    """Test basic compact output has expected sections."""
    result = format_compact_output(
        "test_file.py", sample_file_record, sample_chunks, {}
    )
    assert "# test_file.py" in result
    assert "## Summary" in result
    assert "## Signatures" in result
    assert "**hello** (function)" in result
    assert "**Greeter** (class)" in result
    assert "## Full Code" not in result


def test_format_compact_with_relationships(sample_file_record, sample_chunks):
    """Test relationship hints in signature blocks."""
    relationships = {
        "test_file.py::function::hello::1": {
            "outgoing": [
                {
                    "rel_type": "calls",
                    "target_name": "print_greeting",
                    "target_id": "other.py::function::print_greeting::1",
                    "target_name_resolved": "print_greeting",
                    "source_id": "test_file.py::function::hello::1",
                },
            ],
            "incoming": [
                {
                    "rel_type": "calls",
                    "source_id": "main.py::function::main::1",
                    "source_chunk_name": "main",
                    "source_name": "main",
                },
            ],
        },
    }
    result = format_compact_output(
        "test_file.py", sample_file_record, sample_chunks, relationships
    )
    assert "→ calls: print_greeting" in result
    assert "→ calls from: main" in result


def test_format_verbose_includes_code(sample_file_record, sample_chunks):
    """Test verbose mode includes full code section."""
    result = format_compact_output(
        "test_file.py", sample_file_record, sample_chunks, {}, verbose=True
    )
    assert "## Full Code" in result
    assert "```python" in result
    assert "def hello():" in result


def test_format_empty_chunks(sample_file_record):
    """Test output with no chunks doesn't crash."""
    record = FileRecord(
        path="empty.py",
        language=Language.PYTHON,
        content_hash="abc",
        last_indexed="2026-04-09T10:00:00+00:00",
        chunk_count=0,
    )
    result = format_compact_output("empty.py", record, [], {})
    assert "# empty.py" in result
    assert "## Summary" in result
    assert "*(no top-level chunks found)*" in result


class TestChunkSummaryInFormatter:
    """Tests for AI chunk summary rendering in query output."""

    def test_signature_block_shows_chunk_summary(self, sample_file_record):
        """Signature block renders chunk summary blockquote."""
        chunk = Chunk(
            id="test.py::function::do_thing::1",
            file_path="test.py",
            chunk_type=ChunkType.FUNCTION,
            name="do_thing",
            content="def do_thing(): pass",
            start_line=1,
            end_line=1,
            content_hash="hash1",
            summary="Does the thing",
        )
        result = format_compact_output("test.py", sample_file_record, [chunk], {})
        assert "> *Summary: Does the thing*" in result

    def test_verbose_code_shows_chunk_summary(self, sample_file_record):
        """Verbose mode renders chunk summary before code block."""
        chunk = Chunk(
            id="test.py::function::do_thing::1",
            file_path="test.py",
            chunk_type=ChunkType.FUNCTION,
            name="do_thing",
            content="def do_thing(): pass",
            start_line=1,
            end_line=1,
            content_hash="hash1",
            summary="Verbose summary",
        )
        result = format_compact_output(
            "test.py", sample_file_record, [chunk], {}, verbose=True
        )
        assert "> *Summary: Verbose summary*" in result
        assert "## Full Code" in result

    def test_json_output_includes_summary(self, sample_file_record):
        """JSON output includes summary field."""
        import json
        from glma.query.formatter import format_json_output

        chunk = Chunk(
            id="test.py::function::do_thing::1",
            file_path="test.py",
            chunk_type=ChunkType.FUNCTION,
            name="do_thing",
            content="def do_thing(): pass",
            start_line=1,
            end_line=1,
            content_hash="hash1",
            summary="JSON summary",
        )
        output = format_json_output("test.py", sample_file_record, [chunk], [])
        data = json.loads(output)
        assert data["chunks"][0]["summary"] == "JSON summary"

    def test_no_summary_no_extra_output(self, sample_file_record):
        """Chunks without summary don't produce summary-related output."""
        chunk = Chunk(
            id="test.py::function::do_thing::1",
            file_path="test.py",
            chunk_type=ChunkType.FUNCTION,
            name="do_thing",
            content="def do_thing(): pass",
            start_line=1,
            end_line=1,
            content_hash="hash1",
        )
        result = format_compact_output("test.py", sample_file_record, [chunk], {})
        assert "Summary:" not in result
        assert "> *Summary:" not in result
