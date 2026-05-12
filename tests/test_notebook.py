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


def test_outputs_excluded_by_default(tmp_path):
    """Test that cell outputs are excluded from output by default."""
    nb = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell("print('hello')")
    cell.outputs = [nbformat.v4.new_output(output_type="stream", text="hello\n")]
    nb.cells = [cell]
    path = tmp_path / "test.ipynb"
    nbformat.write(nb, str(path))

    result = compact_notebook(path)
    # Output section should NOT appear by default
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
    result = compact_notebook(comprehension_notebook, include_code=True)
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


def test_code_hidden_by_default(simple_notebook):
    """Code blocks are hidden by default in compacted output."""
    result = compact_notebook(simple_notebook)
    # Should NOT contain a full code block with the source
    assert "```python" not in result
    # The first-line preview is OK — just no full code blocks
    # Should still contain cell annotations
    assert "### Cell 0 [code]" in result


def test_code_shown_when_requested(simple_notebook):
    """Code blocks appear when include_code=True."""
    result = compact_notebook(simple_notebook, include_code=True)
    assert "```python" in result
    assert "x = 42" in result


# --- Summarization & Cache Tests ---


class MockNotebookProvider:
    """Mock SummarizerProvider for notebook tests."""

    def __init__(self, response_prefix="AI summary for cell"):
        self.calls: list[tuple[str, str]] = []
        self.response_prefix = response_prefix

    def summarize(self, code: str, context: str) -> str:
        self.calls.append((code, context))
        return f"{self.response_prefix}: {context.splitlines()[1] if len(context.splitlines()) > 1 else 'unknown'}"


class FailingNotebookProvider:
    """Provider that always raises."""

    def summarize(self, code: str, context: str) -> str:
        raise RuntimeError("Provider unavailable")


def test_cell_content_hash():
    """Cell content hash is deterministic BLAKE2b hex string."""
    from glma.query.notebook import _cell_content_hash
    h1 = _cell_content_hash("x = 42")
    h2 = _cell_content_hash("x = 42")
    h3 = _cell_content_hash("y = 99")
    assert h1 == h2
    assert h1 != h3
    assert len(h1) == 64  # BLAKE2b digest_size=32 → 64 hex chars


def test_cache_roundtrip(tmp_path):
    """Cache save and load preserves cell summaries."""
    from glma.query.notebook import _save_cache, _load_cache, CachedCell
    nb_path = tmp_path / "test.ipynb"
    nb_path.write_text('{"cells":[]}', encoding="utf-8")
    cache_dir = tmp_path / "cache"

    cells = [
        CachedCell(index=0, content_hash="abc", summary="First cell summary"),
        CachedCell(index=2, content_hash="def", summary="Third cell summary"),
    ]
    _save_cache(cache_dir, nb_path, cells)

    loaded = _load_cache(cache_dir, nb_path)
    assert 0 in loaded
    assert loaded[0] == ("abc", "First cell summary")
    assert 2 in loaded
    assert loaded[2] == ("def", "Third cell summary")
    assert 1 not in loaded


def test_cache_empty_when_missing(tmp_path):
    """Loading cache from nonexistent path returns empty dict."""
    from glma.query.notebook import _load_cache
    nb_path = tmp_path / "ghost.ipynb"
    nb_path.write_text('{}', encoding="utf-8")
    loaded = _load_cache(tmp_path / "nope", nb_path)
    assert loaded == {}


def test_summarize_appears_in_output(tmp_path):
    """Summarized cells show blockquote summary in output."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_code_cell("x = 42\ny = x + 1\nz = y * 2"),
        nbformat.v4.new_code_cell("a = 1\nb = 2\nc = a + b"),
    ]
    path = tmp_path / "summ.ipynb"
    nbformat.write(nb, str(path))

    provider = MockNotebookProvider()
    cache_dir = tmp_path / "cache"
    result = compact_notebook(path, provider=provider, cache_dir=cache_dir)

    assert "> *Summary:" in result
    assert len(provider.calls) == 2  # Both cells ≥ 3 lines


def test_summarize_skips_trivial_cells(tmp_path):
    """Cells with < 3 non-empty lines are not summarized."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_code_cell("x = 42"),  # 1 line — skip
        nbformat.v4.new_code_cell("a = 1\nb = 2\nc = a + b"),  # 3 lines — summarize
    ]
    path = tmp_path / "trivial.ipynb"
    nbformat.write(nb, str(path))

    provider = MockNotebookProvider()
    cache_dir = tmp_path / "cache"
    result = compact_notebook(path, provider=provider, cache_dir=cache_dir)

    assert len(provider.calls) == 1  # Only the 3-line cell
    assert "> *Summary:" in result


def test_summarize_skips_markdown_cells(tmp_path):
    """Markdown cells are never summarized even with provider."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_markdown_cell("# Introduction\nThis is a long intro\nwith multiple lines"),
    ]
    path = tmp_path / "md.ipynb"
    nbformat.write(nb, str(path))

    provider = MockNotebookProvider()
    cache_dir = tmp_path / "cache"
    result = compact_notebook(path, provider=provider, cache_dir=cache_dir)

    assert len(provider.calls) == 0  # No code cells
    assert "> *Summary:" not in result


def test_summarize_cache_avoids_duplicate_calls(tmp_path):
    """Cached cells are not re-summarized."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_code_cell("x = 42\ny = x + 1\nz = y * 2"),
    ]
    path = tmp_path / "cached.ipynb"
    nbformat.write(nb, str(path))

    cache_dir = tmp_path / "cache"

    # First call — summarizes and caches
    provider1 = MockNotebookProvider()
    result1 = compact_notebook(path, provider=provider1, cache_dir=cache_dir)
    assert len(provider1.calls) == 1

    # Second call — should use cache
    provider2 = MockNotebookProvider()
    result2 = compact_notebook(path, provider=provider2, cache_dir=cache_dir)
    assert len(provider2.calls) == 0  # Cached, no provider calls

    # Same summary in both outputs
    assert result1 == result2


def test_summarize_provider_failure_is_graceful(tmp_path):
    """Provider errors don't crash — cell just has no summary."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_code_cell("x = 42\ny = x + 1\nz = y * 2"),
    ]
    path = tmp_path / "fail.ipynb"
    nbformat.write(nb, str(path))

    provider = FailingNotebookProvider()
    cache_dir = tmp_path / "cache"
    result = compact_notebook(path, provider=provider, cache_dir=cache_dir)

    # Should not crash, and should not show a summary
    assert "### Cell 0 [code]" in result
    assert "> *Summary:" not in result


def test_summarize_works_in_both_code_modes(tmp_path):
    """Summary appears in both code-visible and code-hidden modes."""
    nb = nbformat.v4.new_notebook()
    nb.cells = [
        nbformat.v4.new_code_cell("x = 42\ny = x + 1\nz = y * 2"),
    ]
    path = tmp_path / "modes.ipynb"
    nbformat.write(nb, str(path))

    provider = MockNotebookProvider()
    cache_dir = tmp_path / "cache"

    result_code = compact_notebook(path, include_code=True, provider=provider, cache_dir=cache_dir)
    assert "> *Summary:" in result_code
    assert "```python" in result_code

    # Clear cache for second run
    import shutil
    shutil.rmtree(cache_dir, ignore_errors=True)

    result_nocode = compact_notebook(path, include_code=False, provider=provider, cache_dir=cache_dir)
    assert "> *Summary:" in result_nocode


def test_no_provider_identical_output(simple_notebook):
    """Without provider, output is identical to previous behavior."""
    result_no_provider = compact_notebook(simple_notebook)
    assert "> *Summary:" not in result_no_provider
    assert "## Cells" in result_no_provider
    assert "## Variable Flow" in result_no_provider


def test_hash_changes_when_outputs_change(tmp_path):
    """Cache invalidates when cell outputs change."""
    from glma.query.notebook import _cell_content_hash, _cell_content_hash_with_outputs
    source = "x = 42\ny = x + 1\nz = y * 2"
    hash_no_outputs = _cell_content_hash(source)

    outputs_v1 = [{"output_type": "stream", "text": "hello\n"}]
    outputs_v2 = [{"output_type": "stream", "text": "world\n"}]

    hash_v1 = _cell_content_hash_with_outputs(source, outputs_v1)
    hash_v2 = _cell_content_hash_with_outputs(source, outputs_v2)
    hash_empty = _cell_content_hash_with_outputs(source, [])

    assert hash_v1 != hash_v2  # Different outputs → different hash
    assert hash_v1 != hash_empty  # With outputs ≠ without outputs
    assert hash_empty == hash_no_outputs  # No outputs matches original hash


def test_format_outputs_truncation(tmp_path):
    """Large outputs are truncated for LLM context."""
    from glma.query.notebook import _format_outputs_for_context

    short = _format_outputs_for_context([{"output_type": "stream", "text": "hi\n"}])
    assert short == "hi"
    assert "... (truncated" not in short

    long_text = "x" * 2000
    truncated = _format_outputs_for_context([{"output_type": "stream", "text": long_text}], max_chars=500)
    assert len(truncated) < 600  # Truncated + marker
    assert "... (truncated" in truncated
    assert f"{len(long_text)} chars total" in truncated


def test_outputs_included_in_summarization_context(tmp_path):
    """Provider receives cell outputs appended to source code."""
    nb = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell("x = 42\ny = x + 1\nz = y * 2")
    cell.outputs = [nbformat.v4.new_output(output_type="stream", text="result: 86\n")]
    nb.cells = [cell]
    path = tmp_path / "with_output.ipynb"
    nbformat.write(nb, str(path))

    class SpyProvider:
        def __init__(self):
            self.calls = []
        def summarize(self, code, context):
            self.calls.append((code, context))
            return "Saw the output"

    provider = SpyProvider()
    cache_dir = tmp_path / "cache"
    result = compact_notebook(path, provider=provider, cache_dir=cache_dir)

    assert len(provider.calls) == 1
    code_arg = provider.calls[0][0]
    # Output should be appended to the code sent to the provider
    assert "# Output:" in code_arg
    assert "result: 86" in code_arg
    assert "x = 42" in code_arg  # Source code still present
    assert "> *Summary: Saw the output*" in result
