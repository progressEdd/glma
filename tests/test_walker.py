"""Tests for directory walker."""

import os
from pathlib import Path

import pytest

from glma.index.walker import walk_source_files
from glma.models import IndexConfig, Language


@pytest.fixture
def sample_tree(tmp_path):
    """Create a sample directory tree for testing."""
    # Create directories
    (tmp_path / ".git").mkdir()
    (tmp_path / "venv").mkdir()
    (tmp_path / "src").mkdir()

    # Create files
    (tmp_path / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    (tmp_path / "venv" / "lib.py").write_text("# venv file\n")
    (tmp_path / "src" / "main.c").write_text("int main() { return 0; }\n")
    (tmp_path / "src" / "lib.py").write_text("def hello(): pass\n")
    (tmp_path / "README.md").write_text("# Readme\n")
    (tmp_path / ".hidden.py").write_text("# hidden\n")
    return tmp_path


class TestDefaultWalk:
    """Test walking with default config."""

    def test_finds_source_files(self, sample_tree):
        config = IndexConfig()
        files = list(walk_source_files(sample_tree, config))
        paths = [str(f.relative_to(sample_tree)) for f, _ in files]
        assert "src/main.c" in paths
        assert "src/lib.py" in paths

    def test_excludes_git(self, sample_tree):
        config = IndexConfig()
        files = list(walk_source_files(sample_tree, config))
        paths = [str(f.relative_to(sample_tree)) for f, _ in files]
        assert not any(".git" in p for p in paths)

    def test_excludes_venv(self, sample_tree):
        config = IndexConfig()
        files = list(walk_source_files(sample_tree, config))
        paths = [str(f.relative_to(sample_tree)) for f, _ in files]
        assert not any("venv" in p for p in paths)

    def test_excludes_hidden_files(self, sample_tree):
        config = IndexConfig()
        files = list(walk_source_files(sample_tree, config))
        paths = [str(f.relative_to(sample_tree)) for f, _ in files]
        assert not any(".hidden" in p for p in paths)

    def test_excludes_non_source(self, sample_tree):
        config = IndexConfig()
        files = list(walk_source_files(sample_tree, config))
        paths = [str(f.relative_to(sample_tree)) for f, _ in files]
        assert not any("README" in p for p in paths)

    def test_language_labels(self, sample_tree):
        config = IndexConfig()
        files = {str(f.relative_to(sample_tree)): lang for f, lang in walk_source_files(sample_tree, config)}
        assert files["src/main.c"] == "c"
        assert files["src/lib.py"] == "python"


class TestLanguageFiltering:
    """Test language-based filtering."""

    def test_c_only(self, sample_tree):
        config = IndexConfig(languages=[Language.C])
        files = list(walk_source_files(sample_tree, config))
        paths = [str(f.relative_to(sample_tree)) for f, _ in files]
        assert "src/main.c" in paths
        assert "src/lib.py" not in paths

    def test_python_only(self, sample_tree):
        config = IndexConfig(languages=[Language.PYTHON])
        files = list(walk_source_files(sample_tree, config))
        paths = [str(f.relative_to(sample_tree)) for f, _ in files]
        assert "src/lib.py" in paths
        assert "src/main.c" not in paths
