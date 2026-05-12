"""Tests for variable extraction module."""

import pytest

from glma.query.variables import (
    CellVariableInfo,
    StatementInfo,
    build_variable_flow,
    extract_cell_variables,
)


def test_simple_assignment():
    """Test basic assignment tracking."""
    info = extract_cell_variables("x = 42\ny = x + 1", 0)
    assert len(info.statements) == 2
    assert info.statements[0].defines == ["x"]
    assert info.statements[0].references == []
    assert info.statements[1].defines == ["y"]
    assert "x" in info.statements[1].references


def test_function_definition():
    """Test function definition tracking."""
    info = extract_cell_variables("def foo(a, b):\n    return a + b", 0)
    assert len(info.statements) == 1
    stmt = info.statements[0]
    assert stmt.statement_type == "function_def"
    assert stmt.defines == ["foo"]
    assert "a" in stmt.references
    assert "b" in stmt.references


def test_import_tracking():
    """Test import tracking."""
    info = extract_cell_variables("import os\nfrom pathlib import Path", 0)
    assert len(info.statements) == 2
    assert info.statements[0].defines == ["os"]
    assert info.statements[1].defines == ["Path"]
    assert info.all_defines == ["os", "Path"]


def test_augmented_assignment():
    """Test augmented assignment reads the variable too."""
    info = extract_cell_variables("x = 10\nx += 5", 0)
    assert len(info.statements) == 2
    assert info.statements[0].defines == ["x"]
    assert info.statements[1].defines == ["x"]
    assert "x" in info.statements[1].references


def test_for_loop_target():
    """Test for-loop target variable extraction."""
    info = extract_cell_variables("for item in items:\n    pass", 0)
    assert len(info.statements) == 1
    stmt = info.statements[0]
    assert stmt.statement_type == "for_loop"
    assert stmt.defines == ["item"]
    assert "items" in stmt.references


def test_class_definition():
    """Test class definition with base class."""
    info = extract_cell_variables("class MyClass(Base):\n    pass", 0)
    assert len(info.statements) == 1
    stmt = info.statements[0]
    assert stmt.statement_type == "class_def"
    assert stmt.defines == ["MyClass"]
    assert "Base" in stmt.references


def test_build_variable_flow():
    """Test cross-cell variable flow mapping."""
    cells = [
        CellVariableInfo(
            cell_index=0,
            cell_type="code",
            source="x = 42\ny = 10",
            statements=[
                StatementInfo(line_number=1, statement_type="assign", defines=["x"], references=[]),
                StatementInfo(line_number=2, statement_type="assign", defines=["y"], references=[]),
            ],
            all_defines=["x", "y"],
            all_references=[],
        ),
        CellVariableInfo(
            cell_index=1,
            cell_type="code",
            source="z = x + 1",
            statements=[
                StatementInfo(line_number=1, statement_type="assign", defines=["z"], references=["x"]),
            ],
            all_defines=["z"],
            all_references=["x"],
        ),
    ]
    flow = build_variable_flow(cells)

    assert "x" in flow
    assert flow["x"]["defined_in"] == [{"cell": 0, "line": 1}]
    assert {"cell": 1, "line": 1} in flow["x"]["used_in"]

    assert "z" in flow
    assert flow["z"]["defined_in"] == [{"cell": 1, "line": 1}]


def test_syntax_error_graceful():
    """Test graceful handling of unparseable code."""
    info = extract_cell_variables("def foo(:\n    pass", 0)
    assert info.statements == []
    assert info.all_defines == []
    assert info.all_references == []
