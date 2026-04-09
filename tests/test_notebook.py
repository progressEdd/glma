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
