"""Tests for import resolution and import map building."""

from pathlib import Path

import pytest

from glma.index.resolver import (
    build_import_map, find_enclosing_class, resolve_callee, ImportInfo,
)
from glma.index.parser import get_root_node
from glma.models import Language


def _parse_python(code: str, tmp_path):
    """Parse Python code and return root node."""
    src = tmp_path / "test.py"
    src.write_text(code)
    root = get_root_node(src, Language.PYTHON)
    return root


class TestBuildImportMap:
    """Test import map building from Python ASTs."""

    def test_build_import_map_simple(self, tmp_path):
        root = _parse_python("import os\n", tmp_path)
        imap = build_import_map(root)
        assert "os" in imap
        assert imap["os"] == ImportInfo("os", "os", None)

    def test_build_import_map_from_import(self, tmp_path):
        root = _parse_python("from pathlib import Path\n", tmp_path)
        imap = build_import_map(root)
        assert "Path" in imap
        assert imap["Path"] == ImportInfo("Path", "pathlib", "Path")

    def test_build_import_map_alias(self, tmp_path):
        root = _parse_python("import foo.bar as baz\n", tmp_path)
        imap = build_import_map(root)
        assert "baz" in imap
        assert imap["baz"] == ImportInfo("baz", "foo.bar", None)

    def test_build_import_map_multiple_names(self, tmp_path):
        root = _parse_python("from typing import Optional, List\n", tmp_path)
        imap = build_import_map(root)
        assert "Optional" in imap
        assert "List" in imap
        assert imap["Optional"] == ImportInfo("Optional", "typing", "Optional")
        assert imap["List"] == ImportInfo("List", "typing", "List")

    def test_build_import_map_dotted_no_alias(self, tmp_path):
        root = _parse_python("import os.path\n", tmp_path)
        imap = build_import_map(root)
        assert "os" in imap
        assert imap["os"].source_module == "os.path"

    def test_build_import_map_from_import_alias(self, tmp_path):
        root = _parse_python("from typing import List as L\n", tmp_path)
        imap = build_import_map(root)
        assert "L" in imap


class TestFindEnclosingClass:
    """Test finding the enclosing class for a node."""

    def test_find_enclosing_class(self, tmp_path):
        code = """\
class MyClass:
    def my_method(self):
        x = 1
"""
        root = _parse_python(code, tmp_path)

        # Find the 'x = 1' assignment node
        def _find_assignment(node):
            if node.type == "assignment" or node.type == "expression_statement":
                for child in node.children:
                    if child.type == "assignment":
                        return child
            for child in node.children:
                result = _find_assignment(child)
                if result is not None:
                    return result
            return None

        assignment = _find_assignment(root)
        assert assignment is not None

        class_name = find_enclosing_class(assignment)
        assert class_name == "MyClass"

    def test_find_enclosing_class_none(self, tmp_path):
        code = """\
def standalone():
    x = 1
"""
        root = _parse_python(code, tmp_path)

        def _find_first(node, node_type):
            if node.type == node_type:
                return node
            for child in node.children:
                result = _find_first(child, node_type)
                if result is not None:
                    return result
            return None

        assignment = _find_first(root, "assignment")
        if assignment is None:
            # tree-sitter might parse `x = 1` differently
            # Try finding the expression_statement containing x
            assignment = _find_first(root, "expression_statement")

        if assignment is not None:
            class_name = find_enclosing_class(assignment)
            assert class_name is None


class TestResolveCallee:
    """Test callee resolution with mock store."""

    def test_resolve_callee_self_method(self, tmp_path):
        from datetime import datetime, timezone
        from glma.db.ladybug_store import LadybugStore
        from glma.models import Chunk, ChunkType, FileRecord

        store = LadybugStore(tmp_path / "db" / "test.lbug")

        # Create a file with a class and method
        src = tmp_path / "test.py"
        src.write_text("class Foo:\n    def bar(self):\n        pass\n    def baz(self):\n        self.bar()\n")
        root = get_root_node(src, Language.PYTHON)

        # Find the 'self.bar()' call node
        def _find_call(node):
            if node.type == "call":
                return node
            for child in node.children:
                result = _find_call(child)
                if result is not None:
                    return result
            return None

        call_node = _find_call(root)
        assert call_node is not None
        callee = call_node.children[0]
        assert callee is not None

        # Build source chunks manually
        class_chunk = Chunk(
            id="test.py::class::Foo::1",
            file_path="test.py",
            chunk_type=ChunkType.CLASS,
            name="Foo",
            content="class Foo:\n    pass",
            summary=None,
            start_line=1,
            end_line=3,
            content_hash="hash1",
            parent_id=None,
        )
        bar_chunk = Chunk(
            id="test.py::method::bar::2",
            file_path="test.py",
            chunk_type=ChunkType.METHOD,
            name="bar",
            content="def bar(self):\n    pass",
            summary=None,
            start_line=2,
            end_line=3,
            content_hash="hash2",
            parent_id="test.py::class::Foo::1",
        )

        import_map = {}
        target_id, target_name = resolve_callee(
            callee, import_map, "Foo", store, "test.py", [class_chunk, bar_chunk]
        )

        assert target_id == bar_chunk.id
        assert "self.bar" in target_name

        store.close()
