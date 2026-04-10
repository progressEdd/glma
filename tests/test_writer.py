"""Tests for markdown output writer."""

from pathlib import Path

import pytest

from glma.index.chunks import extract_chunks
from glma.index.comments import attach_comments
from glma.index.writer import format_file_markdown, write_markdown
from glma.models import Language

FIXTURES = Path(__file__).parent / "fixtures"


class TestFormatFileMarkdown:
    """Test markdown generation."""

    @pytest.fixture
    def py_chunks(self, tmp_path):
        src = tmp_path / "sample.py"
        src.write_text((FIXTURES / "sample.py").read_text())
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        chunks = attach_comments(chunks, src, Language.PYTHON, tmp_path)
        return chunks

    @pytest.fixture
    def c_chunks(self, tmp_path):
        src = tmp_path / "sample.c"
        src.write_text((FIXTURES / "sample.c").read_text())
        chunks = extract_chunks(src, Language.C, tmp_path)
        chunks = attach_comments(chunks, src, Language.C, tmp_path)
        return chunks

    def test_file_heading(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        assert md.startswith("# sample.py")

    def test_key_exports_heading(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        assert "## Key Exports" in md

    def test_chunks_heading(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        assert "## Chunks" in md

    def test_chunk_headings(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        # Should have headings like ### standalone_function (function, L7-L9)
        assert "### standalone_function (function" in md
        assert "### MyClass (class" in md

    def test_python_code_block_hint(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        assert "```python" in md

    def test_c_code_block_hint(self, c_chunks):
        md = format_file_markdown("sample.c", c_chunks)
        assert "```c" in md

    def test_exports_table_top_level_only(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        # Methods should NOT appear in the exports table (they have parent_id)
        lines = md.split("\n")
        in_exports = False
        exports_names = []
        for line in lines:
            if "## Key Exports" in line:
                in_exports = True
            elif line.startswith("## "):
                in_exports = False
            elif in_exports and line.startswith("|") and "Name" not in line and "----" not in line:
                parts = [p.strip() for p in line.split("|") if p.strip()]
                if parts:
                    exports_names.append(parts[0])

        assert "MyClass" in exports_names
        assert "standalone_function" in exports_names
        assert "__init__" not in exports_names
        assert "greet" not in exports_names

    def test_method_parent_shown(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        # Method headings should show "parent: MyClass"
        assert "parent: MyClass" in md

    def test_attached_comments_rendered(self, py_chunks):
        md = format_file_markdown("sample.py", py_chunks)
        # Docstrings should appear above code blocks
        assert "standalone function" in md.lower() or "A standalone function" in md

    def test_file_summary_not_placeholder(self, py_chunks):
        """Writer output shows actual summary, not Phase 3 placeholder."""
        md = format_file_markdown("sample.py", py_chunks)
        assert "*(File summary not yet generated — available after Phase 3.)*" not in md
        # Should contain some actual summary content
        assert "function" in md or "class" in md or "chunk" in md


class TestWriteMarkdown:
    """Test writing markdown to disk."""

    def test_write_creates_file(self, tmp_path):
        src = tmp_path / "src" / "app.py"
        src.parent.mkdir(parents=True)
        src.write_text("def hello(): pass\n")

        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        md_path = write_markdown(chunks, tmp_path, ".glma-index")

        assert md_path.exists()
        assert md_path.parent.name == "src"

    def test_write_content_readable(self, tmp_path):
        src = tmp_path / "app.py"
        src.write_text("def hello(): pass\n")

        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        md_path = write_markdown(chunks, tmp_path, ".glma-index")

        content = md_path.read_text()
        assert "hello" in content

    def test_write_empty_chunks_raises(self, tmp_path):
        with pytest.raises(ValueError, match="No chunks"):
            write_markdown([], tmp_path, ".glma-index")
