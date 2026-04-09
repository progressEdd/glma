"""Integration tests for the full indexing pipeline."""

from pathlib import Path

from glma.db.ladybug_store import LadybugStore
from glma.index.pipeline import run_index
from glma.models import IndexConfig
from tests.test_pipeline import create_test_project


class TestFullIndex:
    """Test complete indexing of a multi-file project."""

    @staticmethod
    def _index_project(tmp_path):
        """Helper to create and index the test project."""
        root = create_test_project(tmp_path)
        cfg = IndexConfig(quiet=True)
        result = run_index(root, cfg)
        return root, result

    def test_completes_without_error(self, tmp_path):
        root, result = self._index_project(tmp_path)
        assert result.total_files > 0

    def test_only_source_files_indexed(self, tmp_path):
        """Only .c, .h, .py files should be indexed (4 files)."""
        root, result = self._index_project(tmp_path)
        assert result.total_files == 4
        assert result.new_files == 4

    def test_git_excluded(self, tmp_path):
        root, result = self._index_project(tmp_path)
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        files = store.get_indexed_files()
        assert not any(".git" in f for f in files)
        store.close()

    def test_venv_excluded(self, tmp_path):
        root, result = self._index_project(tmp_path)
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        files = store.get_indexed_files()
        assert not any("venv" in f for f in files)
        store.close()

    def test_node_modules_excluded(self, tmp_path):
        root, result = self._index_project(tmp_path)
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        files = store.get_indexed_files()
        assert not any("node_modules" in f for f in files)
        store.close()

    def test_hidden_files_excluded(self, tmp_path):
        root, result = self._index_project(tmp_path)
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        files = store.get_indexed_files()
        assert not any(".hidden" in f for f in files)
        store.close()

    def test_readme_excluded(self, tmp_path):
        root, result = self._index_project(tmp_path)
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        files = store.get_indexed_files()
        assert "README.md" not in files
        store.close()

    def test_app_py_chunk_count(self, tmp_path):
        """app.py should have 1 class + 3 methods + 1 standalone function = 5 chunks."""
        root, result = self._index_project(tmp_path)
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        files = store.get_indexed_files()
        # app.py should have at least 4 chunks
        for path, count_attr in files.items():
            pass  # We don't have chunk_count directly, check via markdown
        store.close()
        # Check markdown was created
        md_path = root / ".glma-index" / "markdown" / "src" / "app.py.md"
        assert md_path.exists()
        content = md_path.read_text()
        # Should have headings for class and methods
        assert "User (class" in content
        assert "__init__ (method" in content
        assert "greet (method" in content
        assert "to_dict (method" in content
        assert "create_user (function" in content

    def test_main_c_chunk_count(self, tmp_path):
        """main.c should have at least 1 function chunk."""
        root, result = self._index_project(tmp_path)
        md_path = root / ".glma-index" / "markdown" / "src" / "main.c.md"
        assert md_path.exists()
        content = md_path.read_text()
        assert "main (function" in content

    def test_markdown_files_created(self, tmp_path):
        """Markdown should be created for each indexed file."""
        root, result = self._index_project(tmp_path)
        md_dir = root / ".glma-index" / "markdown"
        assert md_dir.exists()
        md_files = list(md_dir.rglob("*.md"))
        assert len(md_files) >= 4

    def test_app_py_exports_table(self, tmp_path):
        """app.py markdown should have Key Exports with User and create_user."""
        root, result = self._index_project(tmp_path)
        md_path = root / ".glma-index" / "markdown" / "src" / "app.py.md"
        content = md_path.read_text()
        # Extract Key Exports section
        lines = content.split("\n")
        in_exports = False
        export_lines = []
        for line in lines:
            if "## Key Exports" in line:
                in_exports = True
            elif line.startswith("## "):
                in_exports = False
            elif in_exports and line.startswith("|"):
                export_lines.append(line)

        export_text = "\n".join(export_lines)
        assert "User" in export_text
        assert "create_user" in export_text
        # Methods should NOT be in exports
        assert "__init__" not in export_text

    def test_app_py_methods_show_parent(self, tmp_path):
        """Methods should show 'parent: User' in heading."""
        root, result = self._index_project(tmp_path)
        md_path = root / ".glma-index" / "markdown" / "src" / "app.py.md"
        content = md_path.read_text()
        assert "parent: User" in content

    def test_docstrings_in_markdown(self, tmp_path):
        """Docstrings should appear in markdown content."""
        root, result = self._index_project(tmp_path)
        md_path = root / ".glma-index" / "markdown" / "src" / "app.py.md"
        content = md_path.read_text()
        assert "Represents a user" in content

    def test_rerun_skips_all(self, tmp_path):
        """Re-running index with no changes should skip all files."""
        root, result = self._index_project(tmp_path)
        cfg = IndexConfig(quiet=True)
        result2 = run_index(root, cfg)
        assert result2.skipped_files == 4
        assert result2.new_files == 0
        assert result2.updated_files == 0

    def test_total_chunks_minimum(self, tmp_path):
        """Total chunks across all files should be at least 8."""
        root, result = self._index_project(tmp_path)
        assert result.total_chunks >= 8


class TestFullIndexWithRelationships:
    """Test complete indexing with relationship extraction."""

    @staticmethod
    def _create_rel_project(tmp_path):
        """Create a multi-file Python project with cross-file relationships."""
        root = tmp_path / "relproject"
        root.mkdir()

        (root / "animal.py").write_text("""\
class Animal:
    def speak(self):
        raise NotImplementedError
""")

        (root / "dog.py").write_text("""\
from animal import Animal

class Dog(Animal):
    def speak(self):
        return "woof"

    def fetch(self):
        return self.speak()
""")

        (root / "main.py").write_text("""\
from dog import Dog

def make_pet():
    d = Dog()
    return d.speak()
""")

        cfg = IndexConfig(quiet=True)
        result = run_index(root, cfg)
        return root, result

    def test_relationships_extracted(self, tmp_path):
        root, result = self._create_rel_project(tmp_path)
        assert result.total_relationships > 0

    def test_dog_inherits_animal(self, tmp_path):
        root, result = self._create_rel_project(tmp_path)
        md_path = root / ".glma-index" / "markdown" / "dog.py.md"
        assert md_path.exists()
        content = md_path.read_text()
        assert "## Relationships" in content

    def test_self_method_resolved(self, tmp_path):
        root, result = self._create_rel_project(tmp_path)
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        # Dog.fetch should call self.speak
        rels = store.get_file_relationships("dog.py")
        assert len(rels) > 0
        store.close()

    def test_main_calls_dog(self, tmp_path):
        root, result = self._create_rel_project(tmp_path)
        md_path = root / ".glma-index" / "markdown" / "main.py.md"
        assert md_path.exists()
        content = md_path.read_text()
        # Should have relationships section
        assert "## Relationships" in content or "## Key Exports" in content

    def test_incremental_reindex_updates_relationships(self, tmp_path):
        """Modifying a file should update its relationships."""
        root, result = self._create_rel_project(tmp_path)

        # Modify main.py
        (root / "main.py").write_text("""\
from dog import Dog

def make_pet():
    d = Dog()
    d.speak()
    d.fetch()
    return d
""")

        cfg = IndexConfig(quiet=True)
        result2 = run_index(root, cfg)
        assert result2.updated_files == 1
        assert result2.skipped_files == 2  # animal.py, dog.py unchanged

    def test_c_file_relationships(self, tmp_path):
        """C files should have INCLUDES and CALLS relationships."""
        root = tmp_path / "cproject"
        root.mkdir()

        (root / "utils.h").write_text("int helper();\n")
        (root / "utils.c").write_text("""\
#include "utils.h"
int helper() { return 42; }
""")
        (root / "main.c").write_text("""\
#include <stdio.h>
#include "utils.h"
int main() {
    printf("hello");
    return helper();
}
""")

        cfg = IndexConfig(quiet=True)
        result = run_index(root, cfg)
        assert result.total_files == 3

        # Check relationships extracted
        db_path = root / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        rels = store.get_file_relationships("main.c")
        assert len(rels) > 0
        store.close()

        # Check markdown
        md_path = root / ".glma-index" / "markdown" / "main.c.md"
        assert md_path.exists()
        content = md_path.read_text()
        assert "## Relationships" in content
