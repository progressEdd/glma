"""Tests for notebook compaction module."""

import tempfile
import os

import nbformat
import pytest

from glma.query.notebook import compact_notebook


@pytest.fixture
def simple_notebook(tmp_path):
    """Create a minimal .ipynb file."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_code_cell("x = 42"),
        nbformat.v4.new_code_cell("y = x + 1"),
        nbformat.v4.new_markdown_cell("# Results\nGood stuff"),
    ]
    path = tmp_path / "test.ipynb"
    nbformat.write(nb, str(path))
    return path


def test_compact_simple_notebook(simple_notebook):
    """Test basic notebook compaction output."""
    result = compact_notebook(simple_notebook)
    assert "## Cells" in result
    assert "## Variable Flow" in result
    assert "### Cell 0 [code]" in result
    assert "### Cell 1 [code]" in result
    assert "### Cell 2 [markdown]" in result
    # Markdown cell rendered as blockquote
    assert "> # Results" in result
    assert "> Good stuff" in result


def test_outputs_stripped_by_default(tmp_path):
    """Test that cell outputs are not included by default."""
    nb = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell("print('hello')")
    cell.outputs = [nbformat.v4.new_output(output_type="stream", text="hello\n")]
    nb.cells = [cell]
    path = tmp_path / "test.ipynb"
    nbformat.write(nb, str(path))

    result = compact_notebook(path)
    # Output section should not appear
    assert "**Output:**" not in result


def test_outputs_included_when_requested(tmp_path):
    """Test that cell outputs are included with include_outputs=True."""
    nb = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell("print('hello')")
    cell.outputs = [nbformat.v4.new_output(output_type="stream", text="hello\n")]
    nb.cells = [cell]
    path = tmp_path / "test.ipynb"
    nbformat.write(nb, str(path))

    result = compact_notebook(path, include_outputs=True)
    assert "**Output:**" in result
    assert "hello" in result


def test_cross_cell_reference(simple_notebook):
    """Test variable flow shows cross-cell references."""
    result = compact_notebook(simple_notebook)

    # Variable flow should show x defined in cell 0, used in cell 1
    assert "x" in result
    assert "Cell 0" in result
    assert "Cell 1" in result

    # Cell 1 annotation should show x referenced with defined cell 0
    assert "defined cell 0" in result or "(defined cell 0)" in result


@pytest.fixture
def comprehension_notebook(tmp_path):
    """Create a notebook with list/dict/set comprehensions."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_code_cell("result = [x * 2 for x in range(10) if x > 3]"),
        nbformat.v4.new_code_cell("mapping = {k: v for k, v in zip(keys, values)}"),
        nbformat.v4.new_code_cell("unique = {x for x in items if x > 0}"),
        nbformat.v4.new_code_cell("""matrix = [
    [i * j for j in range(5)]
    for i in range(5)
]"""),
    ]
    path = tmp_path / "comprehension.ipynb"
    nbformat.write(nb, str(path))
    return path


def test_comprehension_source_preserved(comprehension_notebook):
    """List/dict/set comprehensions appear in full in cell source output."""
    result = compact_notebook(comprehension_notebook)
    # List comprehension — full expression must appear
    assert "[x * 2 for x in range(10) if x > 3]" in result
    # Dict comprehension — full expression must appear
    assert "{k: v for k, v in zip(keys, values)}" in result
    # Set comprehension — full expression must appear
    assert "{x for x in items if x > 0}" in result
    # Multi-line comprehension — both lines must appear
    assert "[i * j for j in range(5)]" in result
    assert "for i in range(5)" in result


def test_comprehension_variable_tracking(comprehension_notebook):
    """Comprehension statements are tracked in variable analysis."""
    result = compact_notebook(comprehension_notebook)
    # The variables assigned by comprehensions should appear in variable flow
    assert "result" in result
    assert "mapping" in result
    assert "unique" in result
    assert "matrix" in result
