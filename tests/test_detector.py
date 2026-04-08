"""Tests for language detection."""

from pathlib import Path

from glma.index.detector import detect_language
from glma.models import Language


class TestDetectLanguage:
    def test_c_file(self):
        assert detect_language(Path("foo.c")) == Language.C

    def test_h_file(self):
        assert detect_language(Path("foo.h")) == Language.C

    def test_python_file(self):
        assert detect_language(Path("foo.py")) == Language.PYTHON

    def test_pythonw_file(self):
        assert detect_language(Path("foo.pyw")) == Language.PYTHON

    def test_unknown_extension(self):
        assert detect_language(Path("foo.rs")) is None

    def test_case_insensitive(self):
        assert detect_language(Path("FOO.PY")) == Language.PYTHON

    def test_no_extension(self):
        assert detect_language(Path("Makefile")) is None
