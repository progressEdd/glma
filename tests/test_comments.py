"""Tests for comment attachment."""

from pathlib import Path

import pytest

from glma.index.chunks import extract_chunks
from glma.index.comments import attach_comments
from glma.models import Language

FIXTURES = Path(__file__).parent / "fixtures"


class TestPythonDocstrings:
    """Test Python docstring extraction."""

    def test_standalone_function_docstring(self, tmp_path):
        src = tmp_path / "sample.py"
        src.write_text((FIXTURES / "sample.py").read_text())
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        chunks = attach_comments(chunks, src, Language.PYTHON, tmp_path)

        func = [c for c in chunks if c.name == "standalone_function"][0]
        assert any("standalone function" in comment.lower() for comment in func.attached_comments)

    def test_class_docstring(self, tmp_path):
        src = tmp_path / "sample.py"
        src.write_text((FIXTURES / "sample.py").read_text())
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        chunks = attach_comments(chunks, src, Language.PYTHON, tmp_path)

        cls = [c for c in chunks if c.name == "MyClass"][0]
        assert any("sample class" in comment.lower() for comment in cls.attached_comments)

    def test_init_no_docstring(self, tmp_path):
        src = tmp_path / "sample.py"
        src.write_text((FIXTURES / "sample.py").read_text())
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        chunks = attach_comments(chunks, src, Language.PYTHON, tmp_path)

        init = [c for c in chunks if c.name == "__init__"][0]
        # __init__ has no docstring in sample.py
        assert not any("docstring" in comment.lower() for comment in init.attached_comments)


class TestCommentProximity:
    """Test standalone comment attachment via proximity."""

    def test_commented_func_has_both(self, tmp_path):
        src = tmp_path / "commented.py"
        src.write_text((FIXTURES / "commented.py").read_text())
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        chunks = attach_comments(chunks, src, Language.PYTHON, tmp_path)

        func = [c for c in chunks if c.name == "commented_func"][0]
        # Should have both the # comment and the docstring
        assert len(func.attached_comments) >= 1
        has_docstring = any("Has both" in c for c in func.attached_comments)
        has_comment = any("comment about" in c for c in func.attached_comments)
        assert has_docstring or has_comment

    def test_gap_func_has_comment(self, tmp_path):
        src = tmp_path / "commented.py"
        src.write_text((FIXTURES / "commented.py").read_text())
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        chunks = attach_comments(chunks, src, Language.PYTHON, tmp_path)

        func = [c for c in chunks if c.name == "gap_func"][0]
        # The # comment should be attached even with 1 blank line gap
        assert any("Comment about another" in c for c in func.attached_comments)


class TestCComments:
    """Test C block comment attachment."""

    def test_add_has_comment(self, tmp_path):
        src = tmp_path / "sample.c"
        src.write_text((FIXTURES / "sample.c").read_text())
        chunks = extract_chunks(src, Language.C, tmp_path)
        chunks = attach_comments(chunks, src, Language.C, tmp_path)

        add_func = [c for c in chunks if c.name == "add"][0]
        assert any("standalone function" in c.lower() for c in add_func.attached_comments)


class TestEdgeCases:
    """Test edge cases."""

    def test_empty_file_no_error(self, tmp_path):
        src = tmp_path / "empty.py"
        src.write_text("")
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        chunks = attach_comments(chunks, src, Language.PYTHON, tmp_path)
        assert chunks == []


class TestCppComments:
    def test_add_has_comment(self, tmp_path):
        src = tmp_path / "sample.cpp"
        src.write_text((FIXTURES / "sample.cpp").read_text())
        chunks = extract_chunks(src, Language.CPP, tmp_path)
        chunks = attach_comments(chunks, src, Language.CPP, tmp_path)

        add_func = [c for c in chunks if c.name == "add"]
        if add_func:
            assert any("standalone function" in c.lower() for c in add_func[0].attached_comments)


class TestTypescriptComments:
    def test_jsdoc_attached(self, tmp_path):
        src = tmp_path / "sample.ts"
        src.write_text((FIXTURES / "sample.ts").read_text())
        chunks = extract_chunks(src, Language.TYPESCRIPT, tmp_path)
        chunks = attach_comments(chunks, src, Language.TYPESCRIPT, tmp_path)

        all_comments = []
        for c in chunks:
            all_comments.extend(c.attached_comments)
        assert len(chunks) > 0

    def test_jsdoc_extraction(self, tmp_path):
        src = tmp_path / "doc.ts"
        src.write_text("""\
/** A documented function */
function greet(name: string): string {
    return `Hello, ${name}`;
}
""")
        chunks = extract_chunks(src, Language.TYPESCRIPT, tmp_path)
        chunks = attach_comments(chunks, src, Language.TYPESCRIPT, tmp_path)

        greet = [c for c in chunks if c.name == "greet"]
        assert len(greet) == 1
        assert any("documented function" in c.lower() for c in greet[0].attached_comments)


class TestRustComments:
    def test_outer_doc_comment(self, tmp_path):
        src = tmp_path / "sample.rs"
        src.write_text("""\
/// A documented function
fn documented() -> i32 {
    42
}

fn other() -> i32 {
    0
}
""")
        chunks = extract_chunks(src, Language.RUST, tmp_path)
        chunks = attach_comments(chunks, src, Language.RUST, tmp_path)

        doc = [c for c in chunks if c.name == "documented"]
        assert len(doc) == 1
        assert any("documented function" in c.lower() for c in doc[0].attached_comments)

    def test_inner_doc_comment(self, tmp_path):
        src = tmp_path / "sample.rs"
        src.write_text("""\
//! Module documentation

/// A function
fn foo() {}
""")
        chunks = extract_chunks(src, Language.RUST, tmp_path)
        chunks = attach_comments(chunks, src, Language.RUST, tmp_path)

        all_comments = []
        for c in chunks:
            all_comments.extend(c.attached_comments)
        assert any("Module documentation" in c for c in all_comments)
