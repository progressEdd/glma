"""Tests for Python relationship extraction."""

from datetime import datetime, timezone
from pathlib import Path

import pytest

from glma.db.ladybug_store import LadybugStore
from glma.index.chunks import extract_chunks
from glma.index.relationships import extract_relationships
from glma.models import Chunk, ChunkType, FileRecord, Language, Relationship, RelType, Confidence


@pytest.fixture
def store(tmp_path):
    """Create a LadybugStore in a temp directory."""
    db_path = tmp_path / "db" / "test.lbug"
    s = LadybugStore(db_path)
    yield s
    s.close()


def _make_py_file(tmp_path, filename, content):
    """Write a Python source file and return its path."""
    src = tmp_path / filename
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text(content)
    return src


def _index_file(store, tmp_path, filename, content):
    """Create, parse, and store a Python file. Returns (path, chunks)."""
    src = _make_py_file(tmp_path, filename, content)
    chunks = extract_chunks(src, Language.PYTHON, tmp_path)
    store.upsert_file(FileRecord(
        path=filename,
        language=Language.PYTHON,
        content_hash="abc123",
        last_indexed=datetime.now(timezone.utc).isoformat(),
        chunk_count=len(chunks),
    ))
    store.upsert_chunks(filename, chunks)
    return src, chunks


class TestPythonDirectCall:
    """Test direct function call extraction in Python."""

    def test_python_direct_call_same_file(self, tmp_path, store):
        src, chunks = _index_file(store, tmp_path, "sample.py", """\
def bar():
    return 42

def foo():
    return bar()
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1
        direct = [r for r in calls if r.confidence == Confidence.DIRECT]
        assert len(direct) >= 1
        bar_calls = [r for r in direct if r.target_name == "bar"]
        assert len(bar_calls) >= 1
        assert bar_calls[0].target_id != ""  # Resolved

    def test_python_self_method_call(self, tmp_path, store):
        src, chunks = _index_file(store, tmp_path, "animal.py", """\
class Animal:
    def speak(self):
        return "hello"

    def greet(self):
        return self.speak()
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        self_calls = [r for r in calls if "self.speak" in r.target_name]
        assert len(self_calls) >= 1
        # Should resolve to the speak method
        assert self_calls[0].confidence == Confidence.DIRECT
        assert self_calls[0].target_id != ""

    def test_python_unresolved_call(self, tmp_path, store):
        src, chunks = _index_file(store, tmp_path, "main.py", """\
def run():
    unknown_func()
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        unresolved = [r for r in calls if r.target_id == "" and r.confidence == Confidence.INFERRED]
        assert len(unresolved) >= 1
        assert unresolved[0].target_name == "unknown_func"

    def test_python_import_from(self, tmp_path, store):
        # Create an imported module
        _index_file(store, tmp_path, "pathlib.py", """\
class Path:
    pass
""")

        src, chunks = _index_file(store, tmp_path, "main.py", """\
from pathlib import Path

def run():
    p = Path()
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        imports = [r for r in rels if r.rel_type == RelType.IMPORTS]
        assert len(imports) >= 1
        # pathlib is INFERRED since it's not actually indexed as pathlib.py
        # (unless the test module happens to match)

    def test_python_import_alias(self, tmp_path, store):
        src, chunks = _index_file(store, tmp_path, "main.py", """\
import foo.bar as baz

def run():
    baz.something()
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        # Check import is extracted (INFERRED since foo.bar not indexed)
        imports = [r for r in rels if r.rel_type == RelType.IMPORTS]
        assert len(imports) >= 1

        # Check call extraction
        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1

    def test_python_inheritance(self, tmp_path, store):
        src, chunks = _index_file(store, tmp_path, "animals.py", """\
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof"
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        inherits = [r for r in rels if r.rel_type == RelType.INHERITS]
        assert len(inherits) >= 1
        dog_inherits = [r for r in inherits if r.target_name == "Animal"]
        assert len(dog_inherits) >= 1
        assert dog_inherits[0].confidence == Confidence.DIRECT
        assert dog_inherits[0].target_id != ""

    def test_python_multiple_inheritance(self, tmp_path, store):
        src, chunks = _index_file(store, tmp_path, "multi.py", """\
class A:
    pass

class B:
    pass

class C(A, B):
    pass
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        inherits = [r for r in rels if r.rel_type == RelType.INHERITS]
        assert len(inherits) >= 2
        target_names = {r.target_name for r in inherits}
        assert "A" in target_names
        assert "B" in target_names

    def test_python_attribute_call_unknown_object(self, tmp_path, store):
        src, chunks = _index_file(store, tmp_path, "main.py", """\
def run():
    obj.method()
""")
        rels = extract_relationships(src, Language.PYTHON, tmp_path, chunks, store)

        calls = [r for r in rels if r.rel_type == RelType.CALLS]
        assert len(calls) >= 1
        obj_calls = [r for r in calls if "obj.method" in r.target_name]
        assert len(obj_calls) >= 1
        assert obj_calls[0].confidence == Confidence.INFERRED
