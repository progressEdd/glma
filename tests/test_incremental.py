"""Tests for incremental re-indexing behavior."""

from pathlib import Path

from glma.db.ladybug_store import LadybugStore
from glma.index.pipeline import run_index
from glma.models import IndexConfig, Language


class TestColdStart:
    """Test first index on a fresh directory."""

    def test_all_files_new(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        result = run_index(tmp_path, cfg)
        assert result.new_files == 2
        assert result.skipped_files == 0
        assert result.total_files == 2

    def test_db_has_both_records(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)
        # Verify DB has records
        db_path = tmp_path / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        files = store.get_indexed_files()
        assert "main.c" in files
        assert "lib.py" in files
        store.close()

    def test_markdown_generated(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)
        assert (tmp_path / ".glma-index" / "markdown" / "main.c.md").exists()
        assert (tmp_path / ".glma-index" / "markdown" / "lib.py.md").exists()


class TestNoChanges:
    """Test re-index with no file changes."""

    def test_all_files_skipped(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)

        result = run_index(tmp_path, cfg)
        assert result.skipped_files == 2
        assert result.new_files == 0
        assert result.updated_files == 0

    def test_db_records_preserved(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)
        db_path = tmp_path / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        hash_before = store.get_file_hash("main.c")
        run_index(tmp_path, cfg)
        hash_after = store.get_file_hash("main.c")
        assert hash_before == hash_after
        store.close()


class TestFileModified:
    """Test re-index after modifying a file."""

    def test_updated_file_count(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)

        # Modify main.c
        (tmp_path / "main.c").write_text("int main() { return 1; }\n")
        result = run_index(tmp_path, cfg)
        assert result.updated_files == 1
        assert result.skipped_files == 1

    def test_hash_updated(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)
        db_path = tmp_path / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        hash_before = store.get_file_hash("main.c")
        store.close()  # Close before modifying

        (tmp_path / "main.c").write_text("int main() { return 1; }\n")
        run_index(tmp_path, cfg)

        store2 = LadybugStore(db_path)
        hash_after = store2.get_file_hash("main.c")
        assert hash_before != hash_after
        store2.close()


class TestFileDeleted:
    """Test re-index after deleting a file."""

    def test_deleted_file_cleaned(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)

        # Delete lib.py
        (tmp_path / "lib.py").unlink()
        result = run_index(tmp_path, cfg)
        assert result.deleted_files == 1

    def test_db_record_removed(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        (tmp_path / "lib.py").write_text("def hello(): pass\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)

        (tmp_path / "lib.py").unlink()
        run_index(tmp_path, cfg)
        db_path = tmp_path / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        assert store.get_file_hash("lib.py") is None
        store.close()


class TestFileAdded:
    """Test re-index after adding a new file."""

    def test_new_file_indexed(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)

        # Add new file
        (tmp_path / "new_module.py").write_text("def new_func(): pass\n")
        result = run_index(tmp_path, cfg)
        assert result.new_files == 1
        assert result.skipped_files == 1

    def test_new_file_in_db(self, tmp_path):
        (tmp_path / "main.c").write_text("int main() { return 0; }\n")
        cfg = IndexConfig(quiet=True)
        run_index(tmp_path, cfg)

        (tmp_path / "new_module.py").write_text("def new_func(): pass\n")
        run_index(tmp_path, cfg)
        db_path = tmp_path / ".glma-index" / "db" / "index.lbug"
        store = LadybugStore(db_path)
        assert store.get_file_hash("new_module.py") is not None
        store.close()
