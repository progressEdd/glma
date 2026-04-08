"""Tests for configuration loading."""

import tempfile
from pathlib import Path

import pytest

from glma.config import load_config
from glma.models import Language


class TestDefaultConfig:
    """Test default config when no .glma.toml exists."""

    def test_defaults_applied(self, tmp_path):
        cfg = load_config(tmp_path)
        assert cfg.languages == [Language.C, Language.PYTHON]
        assert cfg.output_dir == ".glma-index"
        assert cfg.quiet is False
        assert ".git" in cfg.exclude
        assert "node_modules" in cfg.exclude

    def test_default_exclude_list(self, tmp_path):
        cfg = load_config(tmp_path)
        assert "venv" in cfg.exclude
        assert "__pycache__" in cfg.exclude
        assert "build" in cfg.exclude


class TestFileConfig:
    """Test config loaded from .glma.toml."""

    def test_load_languages(self, tmp_path):
        config_file = tmp_path / ".glma.toml"
        config_file.write_text(
            '[index]\nlanguages = ["c"]\noutput_dir = "my-output"\n'
        )
        cfg = load_config(tmp_path)
        assert cfg.languages == [Language.C]
        assert cfg.output_dir == "my-output"

    def test_load_python_only(self, tmp_path):
        config_file = tmp_path / ".glma.toml"
        config_file.write_text('[index]\nlanguages = ["python"]\n')
        cfg = load_config(tmp_path)
        assert cfg.languages == [Language.PYTHON]
        assert Language.C not in cfg.languages


class TestCliOverrides:
    """Test CLI overrides take precedence over file config."""

    def test_cli_overrides_file(self, tmp_path):
        config_file = tmp_path / ".glma.toml"
        config_file.write_text('[index]\noutput_dir = "from-file"\n')
        cfg = load_config(tmp_path, {"output_dir": "from-cli"})
        assert cfg.output_dir == "from-cli"

    def test_cli_overrides_quiet(self, tmp_path):
        cfg = load_config(tmp_path, {"quiet": True})
        assert cfg.quiet is True

    def test_none_override_ignored(self, tmp_path):
        config_file = tmp_path / ".glma.toml"
        config_file.write_text('[index]\noutput_dir = "from-file"\n')
        cfg = load_config(tmp_path, {"output_dir": None})
        assert cfg.output_dir == "from-file"


class TestInvalidConfig:
    """Test invalid configuration raises errors."""

    def test_invalid_language(self, tmp_path):
        config_file = tmp_path / ".glma.toml"
        config_file.write_text('[index]\nlanguages = ["rust"]\n')
        with pytest.raises(Exception):
            load_config(tmp_path)
