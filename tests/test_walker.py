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


class TestWalkerNewLanguages:
    def test_discovers_cpp_files(self, tmp_path):
        (tmp_path / "main.cpp").write_text("int main() { return 0; }")
        config = IndexConfig(languages=[Language.CPP])
        files = list(walk_source_files(tmp_path, config))
        assert len(files) == 1
        assert files[0][1] == "cpp"

    def test_discovers_typescript_files(self, tmp_path):
        (tmp_path / "app.ts").write_text("function main() {}")
        config = IndexConfig(languages=[Language.TYPESCRIPT])
        files = list(walk_source_files(tmp_path, config))
        assert len(files) == 1
        assert files[0][1] == "typescript"

    def test_discovers_tsx_files(self, tmp_path):
        (tmp_path / "app.tsx").write_text("export default function App() { return null; }")
        config = IndexConfig(languages=[Language.TSX])
        files = list(walk_source_files(tmp_path, config))
        assert len(files) == 1
        assert files[0][1] == "tsx"

    def test_discovers_rust_files(self, tmp_path):
        (tmp_path / "main.rs").write_text("fn main() {}")
        config = IndexConfig(languages=[Language.RUST])
        files = list(walk_source_files(tmp_path, config))
        assert len(files) == 1
        assert files[0][1] == "rust"

    def test_h_file_not_discovered_with_c_only(self, tmp_path):
        """When only C is selected, .h files should NOT be discovered (they map to CPP)."""
        (tmp_path / "header.h").write_text("#ifndef H\n#define H\n#endif")
        (tmp_path / "main.c").write_text('#include "header.h"\nint main() { return 0; }')
        config = IndexConfig(languages=[Language.C])
        files = list(walk_source_files(tmp_path, config))
        extensions = [Path(f[0]).suffix for f in files]
        assert ".h" not in extensions
        assert ".c" in extensions

    def test_h_file_discovered_with_cpp(self, tmp_path):
        """When CPP is selected, .h files should be discovered."""
        (tmp_path / "header.h").write_text("#pragma once")
        config = IndexConfig(languages=[Language.CPP])
        files = list(walk_source_files(tmp_path, config))
        assert len(files) == 1
        assert files[0][1] == "cpp"

    def test_default_languages_excludes_new(self, tmp_path):
        """Default language list [c, python] should not discover .rs or .ts files."""
        (tmp_path / "main.rs").write_text("fn main() {}")
        (tmp_path / "app.ts").write_text("function main() {}")
        (tmp_path / "main.c").write_text("int main() { return 0; }")
        config = IndexConfig()  # default: [C, PYTHON]
        files = list(walk_source_files(tmp_path, config))
        extensions = [Path(f[0]).suffix for f in files]
        assert ".rs" not in extensions
        assert ".ts" not in extensions
        assert ".c" in extensions
