"""Tests for chunk extraction."""

from pathlib import Path

import pytest

from glma.index.chunks import extract_chunks
from glma.models import ChunkType, Language

FIXTURES = Path(__file__).parent / "fixtures"


class TestPythonChunkExtraction:
    """Test chunk extraction from Python files."""

    @pytest.fixture
    def py_chunks(self, tmp_path):
        """Extract chunks from sample.py with tmp_path as repo root."""
        # Copy fixture to tmp_path to get clean relative paths
        src = tmp_path / "sample.py"
        src.write_text((FIXTURES / "sample.py").read_text())
        return extract_chunks(src, Language.PYTHON, tmp_path)

    def test_finds_standalone_function(self, py_chunks):
        names = [c.name for c in py_chunks]
        assert "standalone_function" in names

    def test_finds_class(self, py_chunks):
        classes = [c for c in py_chunks if c.chunk_type == ChunkType.CLASS]
        assert len(classes) == 1
        assert classes[0].name == "MyClass"

    def test_finds_methods(self, py_chunks):
        methods = [c for c in py_chunks if c.chunk_type == ChunkType.METHOD]
        method_names = [m.name for m in methods]
        assert "__init__" in method_names
        assert "greet" in method_names

    def test_methods_have_parent_id(self, py_chunks):
        class_chunk = [c for c in py_chunks if c.name == "MyClass"][0]
        methods = [c for c in py_chunks if c.chunk_type == ChunkType.METHOD]
        for m in methods:
            assert m.parent_id == class_chunk.id

    def test_standalone_no_parent(self, py_chunks):
        standalone = [c for c in py_chunks if c.name == "standalone_function"]
        assert len(standalone) == 1
        assert standalone[0].parent_id is None

    def test_another_function(self, py_chunks):
        names = [c.name for c in py_chunks]
        assert "another_function" in names

    def test_total_chunk_count(self, py_chunks):
        # 3 functions + 1 class + 2 methods = 6
        assert len(py_chunks) >= 5

    def test_content_hash_valid(self, py_chunks):
        for chunk in py_chunks:
            assert len(chunk.content_hash) == 64  # BLAKE2b-32 → 64 hex chars
            assert all(c in "0123456789abcdef" for c in chunk.content_hash)

    def test_line_numbers_1_indexed(self, py_chunks):
        for chunk in py_chunks:
            assert chunk.start_line >= 1
            assert chunk.end_line >= 1
            assert chunk.end_line >= chunk.start_line

    def test_chunk_id_format(self, py_chunks):
        for chunk in py_chunks:
            assert "::" in chunk.id
            parts = chunk.id.split("::")
            assert len(parts) == 4  # path::type::name::line


class TestCChunkExtraction:
    """Test chunk extraction from C files."""

    @pytest.fixture
    def c_chunks(self, tmp_path):
        src = tmp_path / "sample.c"
        src.write_text((FIXTURES / "sample.c").read_text())
        return extract_chunks(src, Language.C, tmp_path)

    def test_finds_add_function(self, c_chunks):
        names = [c.name for c in c_chunks]
        assert "add" in names

    def test_finds_main_function(self, c_chunks):
        names = [c.name for c in c_chunks]
        assert "main" in names

    def test_finds_struct(self, c_chunks):
        structs = [c for c in c_chunks if c.chunk_type == ChunkType.CLASS]
        names = [s.name for s in structs]
        assert "Point" in names

    def test_total_chunk_count(self, c_chunks):
        # add + Point + main + possibly typedef/Rectangle
        assert len(c_chunks) >= 3

    def test_c_functions_are_function_type(self, c_chunks):
        functions = [c for c in c_chunks if c.name in ("add", "main")]
        for f in functions:
            assert f.chunk_type == ChunkType.FUNCTION


class TestEdgeCases:
    """Test edge cases for chunk extraction."""

    def test_empty_file(self, tmp_path):
        src = tmp_path / "empty.py"
        src.write_text("")
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        assert chunks == []

    def test_nonexistent_file(self, tmp_path):
        src = tmp_path / "nonexistent.py"
        chunks = extract_chunks(src, Language.PYTHON, tmp_path)
        assert chunks == []


class TestCppChunkExtraction:
    @pytest.fixture
    def cpp_chunks(self, tmp_path):
        src = tmp_path / "sample.cpp"
        src.write_text((FIXTURES / "sample.cpp").read_text())
        return extract_chunks(src, Language.CPP, tmp_path)

    def test_finds_add_function(self, cpp_chunks):
        names = [c.name for c in cpp_chunks]
        assert "add" in names

    def test_finds_class(self, cpp_chunks):
        classes = [c for c in cpp_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Shape" in class_names

    def test_finds_struct(self, cpp_chunks):
        classes = [c for c in cpp_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Point" in class_names

    def test_finds_namespace(self, cpp_chunks):
        classes = [c for c in cpp_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "MyApp" in class_names


class TestTypescriptChunkExtraction:
    @pytest.fixture
    def ts_chunks(self, tmp_path):
        src = tmp_path / "sample.ts"
        src.write_text((FIXTURES / "sample.ts").read_text())
        return extract_chunks(src, Language.TYPESCRIPT, tmp_path)

    def test_finds_function(self, ts_chunks):
        names = [c.name for c in ts_chunks]
        assert "greet" in names

    def test_finds_class(self, ts_chunks):
        classes = [c for c in ts_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Circle" in class_names

    def test_finds_interface(self, ts_chunks):
        classes = [c for c in ts_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Shape" in class_names

    def test_finds_enum(self, ts_chunks):
        classes = [c for c in ts_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Color" in class_names

    def test_finds_type_alias(self, ts_chunks):
        classes = [c for c in ts_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Point" in class_names


class TestRustChunkExtraction:
    @pytest.fixture
    def rs_chunks(self, tmp_path):
        src = tmp_path / "sample.rs"
        src.write_text((FIXTURES / "sample.rs").read_text())
        return extract_chunks(src, Language.RUST, tmp_path)

    def test_finds_main_function(self, rs_chunks):
        names = [c.name for c in rs_chunks]
        assert "main" in names

    def test_finds_struct(self, rs_chunks):
        classes = [c for c in rs_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Point" in class_names

    def test_finds_enum(self, rs_chunks):
        classes = [c for c in rs_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Shape" in class_names

    def test_finds_trait(self, rs_chunks):
        classes = [c for c in rs_chunks if c.chunk_type == ChunkType.CLASS]
        class_names = [c.name for c in classes]
        assert "Describe" in class_names
