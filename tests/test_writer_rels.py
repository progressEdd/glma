"""Tests for markdown relationship output."""

from pathlib import Path

import pytest

from glma.models import Chunk, ChunkType
from glma.index.writer import format_file_markdown, write_markdown


@pytest.fixture
def sample_chunks():
    return [
        Chunk(
            id="src/main.py::function::foo::1",
            file_path="src/main.py",
            chunk_type=ChunkType.FUNCTION,
            name="foo",
            content="def foo():\n    pass",
            summary=None,
            start_line=1,
            end_line=2,
            content_hash="hash1",
            parent_id=None,
        ),
        Chunk(
            id="src/main.py::function::bar::4",
            file_path="src/main.py",
            chunk_type=ChunkType.FUNCTION,
            name="bar",
            content="def bar():\n    foo()",
            summary=None,
            start_line=4,
            end_line=5,
            content_hash="hash2",
            parent_id=None,
        ),
    ]


class TestMarkdownNoRelationships:
    """Test that no-relationships output matches Phase 1 format."""

    def test_markdown_no_relationships(self, sample_chunks):
        md = format_file_markdown("src/main.py", sample_chunks, relationships=None)
        assert "## Relationships" not in md
        assert "**Calls:**" not in md
        assert "**Called by:**" not in md
        # Should still have the Phase 1 format
        assert "## Key Exports" in md
        assert "## Chunks" in md


class TestMarkdownInlineCalls:
    """Test inline call display."""

    def test_markdown_inline_calls(self, sample_chunks):
        rels = [
            {
                "source_id": "src/main.py::function::bar::4",
                "source_name": "bar",
                "rel_type": "calls",
                "confidence": "DIRECT",
                "source_line": 5,
                "target_name": "foo",
                "target_id": "src/main.py::function::foo::1",
                "target_name_resolved": "foo",
            },
        ]
        md = format_file_markdown("src/main.py", sample_chunks, relationships=rels)
        assert "**Calls:**" in md
        assert "foo (DIRECT)" in md


class TestMarkdownInlineCalledBy:
    """Test inline called-by display."""

    def test_markdown_inline_called_by(self, sample_chunks):
        rels = [
            {
                "source_id": "src/other.py::function::baz::3",
                "source_name": "baz",
                "rel_type": "calls",
                "confidence": "DIRECT",
                "source_line": 3,
                "target_name": "foo",
                "target_id": "src/main.py::function::foo::1",
                "direction": "incoming",
            },
        ]
        md = format_file_markdown("src/main.py", sample_chunks, relationships=rels)
        assert "**Called by:**" in md
        assert "baz (DIRECT)" in md


class TestMarkdownSummaryOutgoingTable:
    """Test outgoing calls summary table."""

    def test_markdown_summary_outgoing_calls_table(self, sample_chunks):
        rels = [
            {
                "source_id": "src/main.py::function::bar::4",
                "source_name": "bar",
                "rel_type": "calls",
                "confidence": "DIRECT",
                "source_line": 5,
                "target_name": "foo",
                "target_id": "src/main.py::function::foo::1",
                "target_name_resolved": "foo",
            },
        ]
        md = format_file_markdown("src/main.py", sample_chunks, relationships=rels)
        assert "## Relationships" in md
        assert "### Outgoing Calls" in md
        assert "| From | To | Confidence | Line |" in md
        assert "| bar | foo | DIRECT | L5 |" in md


class TestMarkdownSummaryInherits:
    """Test inheritance summary table."""

    def test_markdown_summary_inherits_table(self):
        chunks = [
            Chunk(
                id="animal.py::class::Animal::1",
                file_path="animal.py",
                chunk_type=ChunkType.CLASS,
                name="Animal",
                content="class Animal: pass",
                summary=None,
                start_line=1,
                end_line=1,
                content_hash="h1",
                parent_id=None,
            ),
            Chunk(
                id="animal.py::class::Dog::3",
                file_path="animal.py",
                chunk_type=ChunkType.CLASS,
                name="Dog",
                content="class Dog(Animal): pass",
                summary=None,
                start_line=3,
                end_line=3,
                content_hash="h2",
                parent_id=None,
            ),
        ]
        rels = [
            {
                "source_id": "animal.py::class::Dog::3",
                "source_name": "Dog",
                "rel_type": "inherits",
                "confidence": "DIRECT",
                "source_line": 3,
                "target_name": "Animal",
                "target_id": "animal.py::class::Animal::1",
            },
        ]
        md = format_file_markdown("animal.py", chunks, relationships=rels)
        assert "### Inherits" in md
        assert "| Dog | Animal | DIRECT |" in md


class TestMarkdownUnresolvedTarget:
    """Test unresolved target display."""

    def test_markdown_unresolved_target_display(self, sample_chunks):
        rels = [
            {
                "source_id": "src/main.py::function::bar::4",
                "source_name": "bar",
                "rel_type": "calls",
                "confidence": "INFERRED",
                "source_line": 5,
                "target_name": "unknown",
                "target_id": "",
            },
        ]
        md = format_file_markdown("src/main.py", sample_chunks, relationships=rels)
        # Both inline and summary should show ? (unknown)
        assert "? (unknown)" in md


class TestMarkdownEmptySectionsOmitted:
    """Test that empty relationship sections are omitted."""

    def test_markdown_empty_sections_omitted(self, sample_chunks):
        rels = [
            {
                "source_id": "src/main.py::function::bar::4",
                "source_name": "bar",
                "rel_type": "calls",
                "confidence": "DIRECT",
                "source_line": 5,
                "target_name": "foo",
                "target_id": "src/main.py::function::foo::1",
                "target_name_resolved": "foo",
            },
        ]
        md = format_file_markdown("src/main.py", sample_chunks, relationships=rels)
        assert "### Imports" not in md
        assert "### Inherits" not in md
        assert "### Includes" not in md


class TestWriteMarkdownWithRelationships:
    """Test full write_markdown with relationships."""

    def test_write_markdown_with_relationships(self, sample_chunks, tmp_path):
        rels = [
            {
                "source_id": "src/main.py::function::bar::4",
                "source_name": "bar",
                "rel_type": "calls",
                "confidence": "DIRECT",
                "source_line": 5,
                "target_name": "foo",
                "target_id": "src/main.py::function::foo::1",
                "target_name_resolved": "foo",
            },
        ]
        md_path = write_markdown(sample_chunks, tmp_path, ".glma-index", relationships=rels)
        assert md_path.exists()
        content = md_path.read_text()
        assert "## Relationships" in content
        assert "### Outgoing Calls" in content
