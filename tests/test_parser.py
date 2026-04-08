"""Tests for tree-sitter parsing pipeline."""

from pathlib import Path

import pytest

from glma.index.parser import PARSER_CONFIGS, get_root_node, parse_file
from glma.models import Language

FIXTURES = Path(__file__).parent / "fixtures"


class TestCParsing:
    def test_parse_sample_c(self):
        root = get_root_node(FIXTURES / "sample.c", Language.C)
        assert root is not None
        assert root.type == "translation_unit"
        assert len(root.children) > 0

    def test_c_has_functions(self):
        root = get_root_node(FIXTURES / "sample.c", Language.C)
        types = [c.type for c in root.children]
        assert "function_definition" in types

    def test_c_nonexistent_file(self):
        root = get_root_node(Path("/nonexistent/file.c"), Language.C)
        assert root is None


class TestPythonParsing:
    def test_parse_sample_py(self):
        root = get_root_node(FIXTURES / "sample.py", Language.PYTHON)
        assert root is not None
        assert root.type == "module"
        assert len(root.children) > 0

    def test_python_has_functions_and_classes(self):
        root = get_root_node(FIXTURES / "sample.py", Language.PYTHON)
        types = [c.type for c in root.children if c.is_named]
        assert "function_definition" in types
        assert "class_definition" in types

    def test_empty_file(self):
        root = get_root_node(FIXTURES / "empty.py", Language.PYTHON)
        assert root is not None
        assert root.type == "module"
        named_children = [c for c in root.children if c.is_named]
        assert len(named_children) == 0


class TestParserConfigs:
    def test_c_config_exists(self):
        assert Language.C in PARSER_CONFIGS

    def test_python_config_exists(self):
        assert Language.PYTHON in PARSER_CONFIGS

    def test_c_chunk_types(self):
        config = PARSER_CONFIGS[Language.C]
        assert "function_definition" in config.chunk_types
        assert "struct_specifier" in config.chunk_types

    def test_python_chunk_types(self):
        config = PARSER_CONFIGS[Language.PYTHON]
        assert "function_definition" in config.chunk_types
        assert "class_definition" in config.chunk_types
