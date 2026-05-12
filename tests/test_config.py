"""Tests for configuration loading."""

import tempfile
from pathlib import Path

import pytest

from glma.config import load_config, _resolve_config_path
from glma.models import Language


@pytest.fixture
def config_dir(tmp_path):
    """Create .glma-index/ directory for config file placement."""
    config_path = tmp_path / ".glma-index"
    config_path.mkdir()
    return config_path


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
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text(
            '[index]\nlanguages = ["c"]\noutput_dir = "my-output"\n'
        )
        cfg = load_config(tmp_path)
        assert cfg.languages == [Language.C]
        assert cfg.output_dir == "my-output"

    def test_load_python_only(self, tmp_path):
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[index]\nlanguages = ["python"]\n')
        cfg = load_config(tmp_path)
        assert cfg.languages == [Language.PYTHON]
        assert Language.C not in cfg.languages


class TestCliOverrides:
    """Test CLI overrides take precedence over file config."""

    def test_cli_overrides_file(self, tmp_path):
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[index]\noutput_dir = "from-file"\n')
        cfg = load_config(tmp_path, {"output_dir": "from-cli"})
        assert cfg.output_dir == "from-cli"

    def test_cli_overrides_quiet(self, tmp_path):
        cfg = load_config(tmp_path, {"quiet": True})
        assert cfg.quiet is True

    def test_none_override_ignored(self, tmp_path):
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[index]\noutput_dir = "from-file"\n')
        cfg = load_config(tmp_path, {"output_dir": None})
        assert cfg.output_dir == "from-file"


class TestInvalidConfig:
    """Test invalid configuration raises errors."""

    def test_invalid_language(self, tmp_path):
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[index]\nlanguages = ["fortran"]\n')
        with pytest.raises(Exception):
            load_config(tmp_path)


class TestSummarizeConfig:
    """Test load_summarize_config()."""

    def test_defaults(self, tmp_path):
        from glma.config import load_summarize_config
        cfg = load_summarize_config(tmp_path)
        assert cfg.enabled is False
        assert cfg.provider.value == "local"
        assert cfg.model == "default"
        assert cfg.base_url == "http://localhost:1234/v1"

    def test_load_from_file(self, tmp_path):
        from glma.config import load_summarize_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text(
            '[summarize]\nenabled = true\nprovider = "local"\nmodel = "llama3"\nbase_url = "http://ollama:11434/v1"\n'
        )
        cfg = load_summarize_config(tmp_path)
        assert cfg.enabled is True
        assert cfg.model == "llama3"
        assert cfg.base_url == "http://ollama:11434/v1"

    def test_cli_overrides_file(self, tmp_path):
        from glma.config import load_summarize_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[summarize]\nmodel = "from-file"\n')
        cfg = load_summarize_config(tmp_path, {"model": "from-cli"})
        assert cfg.model == "from-cli"

    def test_none_override_ignored(self, tmp_path):
        from glma.config import load_summarize_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[summarize]\nmodel = "from-file"\n')
        cfg = load_summarize_config(tmp_path, {"model": None})
        assert cfg.model == "from-file"

    def test_cli_enabled_flag(self, tmp_path):
        from glma.config import load_summarize_config
        cfg = load_summarize_config(tmp_path, {"enabled": True})
        assert cfg.enabled is True


class TestProviderPresets:
    """Test provider preset resolution in load_summarize_config()."""

    def test_ollama_preset_resolves(self, tmp_path):
        """--summarize-provider ollama resolves to correct base_url and model."""
        from glma.config import load_summarize_config
        cfg = load_summarize_config(tmp_path, cli_overrides={"provider": "ollama"})
        assert cfg.base_url == "http://localhost:11434/v1"
        assert cfg.model == "llama3"

    def test_lmstudio_preset_resolves(self, tmp_path):
        """--summarize-provider lmstudio resolves to correct base_url and model."""
        from glma.config import load_summarize_config
        cfg = load_summarize_config(tmp_path, cli_overrides={"provider": "lmstudio"})
        assert cfg.base_url == "http://localhost:1234/v1"
        assert cfg.model == "default"

    def test_preset_url_override(self, tmp_path):
        """Explicit base_url overrides preset base_url."""
        from glma.config import load_summarize_config
        cfg = load_summarize_config(tmp_path, cli_overrides={
            "provider": "ollama",
            "base_url": "http://custom:9999/v1",
        })
        assert cfg.base_url == "http://custom:9999/v1"
        assert cfg.model == "llama3"  # model from preset still applies

    def test_preset_model_override(self, tmp_path):
        """Explicit model overrides preset default model."""
        from glma.config import load_summarize_config
        cfg = load_summarize_config(tmp_path, cli_overrides={
            "provider": "ollama",
            "model": "codellama",
        })
        assert cfg.base_url == "http://localhost:11434/v1"  # URL from preset
        assert cfg.model == "codellama"

    def test_local_preset_backward_compat(self, tmp_path):
        """'local' preset still resolves to LM Studio defaults."""
        from glma.config import load_summarize_config
        cfg = load_summarize_config(tmp_path, cli_overrides={"provider": "local"})
        assert cfg.base_url == "http://localhost:1234/v1"
        assert cfg.model == "default"

    def test_custom_provider_from_toml(self, tmp_path):
        """Custom providers from [summarize.providers] override built-in presets."""
        from glma.config import load_summarize_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text(
            '[summarize.providers.ollama]\nbase_url = "http://my-server:11434/v1"\nmodel = "mistral"\n'
        )
        cfg = load_summarize_config(tmp_path, cli_overrides={"provider": "ollama"})
        assert cfg.base_url == "http://my-server:11434/v1"
        assert cfg.model == "mistral"

    def test_new_custom_provider(self, tmp_path):
        """Entirely new custom provider can be added via config."""
        from glma.config import load_summarize_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text(
            '[summarize.providers.myprovider]\nbase_url = "http://custom:5555/v1"\nmodel = "mymodel"\n'
        )
        cfg = load_summarize_config(tmp_path, cli_overrides={"provider": "myprovider"})
        assert cfg.base_url == "http://custom:5555/v1"
        assert cfg.model == "mymodel"


class TestSearchConfigDefaults:
    """Test load_search_config() defaults."""

    def test_defaults(self, tmp_path):
        from glma.config import load_search_config
        cfg = load_search_config(tmp_path)
        assert cfg.enabled is False
        assert cfg.embedding_provider == "embed-local"
        assert cfg.embedding_model == "default"
        assert cfg.embedding_base_url == "http://localhost:1234/v1"
        assert cfg.vector_dimensions == 768
        assert cfg.similarity_threshold == 0.5
        assert cfg.hybrid_keyword_weight == 0.5
        assert cfg.hybrid_vector_weight == 0.5


class TestSearchConfigValidation:
    """Test SearchConfig model validation."""

    def test_dimensions_must_be_positive(self, tmp_path):
        from glma.models import SearchConfig
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            SearchConfig(vector_dimensions=0)

    def test_threshold_zero_to_one(self, tmp_path):
        from glma.models import SearchConfig
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            SearchConfig(similarity_threshold=1.5)
        SearchConfig(similarity_threshold=0.0)
        SearchConfig(similarity_threshold=1.0)

    def test_weights_must_sum_to_one(self, tmp_path):
        from glma.models import SearchConfig
        from pydantic import ValidationError
        with pytest.raises(ValidationError):
            SearchConfig(hybrid_keyword_weight=0.3, hybrid_vector_weight=0.3)

    def test_weights_default_valid(self, tmp_path):
        from glma.models import SearchConfig
        cfg = SearchConfig()
        assert abs(cfg.hybrid_keyword_weight + cfg.hybrid_vector_weight - 1.0) < 0.01


class TestSearchConfigFile:
    """Test load_search_config() from .glma.toml."""

    def test_load_from_file(self, tmp_path):
        from glma.config import load_search_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text(
            '[search]\nenabled = true\nembedding_provider = "embed-ollama"\n'
        )
        cfg = load_search_config(tmp_path)
        assert cfg.enabled is True
        assert cfg.embedding_base_url == "http://localhost:11434/v1"
        assert cfg.embedding_model == "qwen3-embedding"

    def test_cli_overrides_file(self, tmp_path):
        from glma.config import load_search_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[search]\nembedding_model = "from-file"\n')
        cfg = load_search_config(tmp_path, {"embedding_model": "from-cli"})
        assert cfg.embedding_model == "from-cli"

    def test_none_override_ignored(self, tmp_path):
        from glma.config import load_search_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text('[search]\nembedding_model = "from-file"\n')
        cfg = load_search_config(tmp_path, {"embedding_model": None})
        assert cfg.embedding_model == "from-file"


class TestSearchProviderPresets:
    """Test embedding provider preset resolution in load_search_config()."""

    def test_ollama_preset_resolves(self, tmp_path):
        from glma.config import load_search_config
        cfg = load_search_config(tmp_path, cli_overrides={"embedding_provider": "embed-ollama"})
        assert cfg.embedding_base_url == "http://localhost:11434/v1"
        assert cfg.embedding_model == "qwen3-embedding"

    def test_preset_url_override(self, tmp_path):
        """Explicit embedding_base_url overrides preset base_url."""
        from glma.config import load_search_config
        cfg = load_search_config(tmp_path, cli_overrides={
            "embedding_provider": "embed-ollama",
            "embedding_base_url": "http://custom:9999/v1",
        })
        assert cfg.embedding_base_url == "http://custom:9999/v1"
        assert cfg.embedding_model == "qwen3-embedding"

    def test_preset_model_override(self, tmp_path):
        """Explicit embedding_model overrides preset default model."""
        from glma.config import load_search_config
        cfg = load_search_config(tmp_path, cli_overrides={
            "embedding_provider": "embed-ollama",
            "embedding_model": "custom-model",
        })
        assert cfg.embedding_base_url == "http://localhost:11434/v1"
        assert cfg.embedding_model == "custom-model"

    def test_custom_provider_from_toml(self, tmp_path):
        """Custom providers from [search.providers] override built-in presets."""
        from glma.config import load_search_config
        (tmp_path / ".glma-index").mkdir(exist_ok=True)
        config_file = tmp_path / ".glma-index" / ".glma.toml"
        config_file.write_text(
            '[search.providers.mycustom]\nbase_url = "http://my-server:5555/v1"\nmodel = "mymodel"\n'
        )
        cfg = load_search_config(tmp_path, cli_overrides={"embedding_provider": "mycustom"})
        assert cfg.embedding_base_url == "http://my-server:5555/v1"
        assert cfg.embedding_model == "mymodel"

    def test_embed_local_preset(self, tmp_path):
        """'embed-local' preset resolves to LM Studio defaults."""
        from glma.config import load_search_config
        cfg = load_search_config(tmp_path, cli_overrides={"embedding_provider": "embed-local"})
        assert cfg.embedding_base_url == "http://localhost:1234/v1"
        assert cfg.embedding_model == "default"


class TestConfigMigration:
    """Test auto-migration from root .glma.toml to .glma-index/.glma.toml."""

    def test_auto_migrate_root_config(self, tmp_path):
        """Root .glma.toml is auto-moved to .glma-index/.glma.toml."""
        (tmp_path / ".glma.toml").write_text('[index]\noutput_dir = "custom-out"\n')
        cfg = load_config(tmp_path)
        assert cfg.output_dir == "custom-out"
        # File should now be in new location
        assert (tmp_path / ".glma-index" / ".glma.toml").exists()
        # Old file should be gone
        assert not (tmp_path / ".glma.toml").exists()

    def test_new_location_takes_priority(self, tmp_path):
        """If both locations exist, new location wins."""
        (tmp_path / ".glma-index").mkdir()
        (tmp_path / ".glma.toml").write_text('[index]\noutput_dir = "old-location"\n')
        (tmp_path / ".glma-index" / ".glma.toml").write_text('[index]\noutput_dir = "new-location"\n')
        cfg = load_config(tmp_path)
        assert cfg.output_dir == "new-location"
        # Old file should still exist (not deleted in dual-location case)
        assert (tmp_path / ".glma.toml").exists()

    def test_no_config_no_error(self, tmp_path):
        """No config anywhere returns defaults without error."""
        cfg = load_config(tmp_path)
        assert cfg.output_dir == ".glma-index"

    def test_explicit_config_skips_migration(self, tmp_path):
        """--config flag uses exact path, no migration logic."""
        custom = tmp_path / "custom-config.toml"
        custom.write_text('[index]\noutput_dir = "explicit"\n')
        result = _resolve_config_path(tmp_path, explicit_config=custom)
        assert result == custom

    def test_migration_creates_index_dir(self, tmp_path):
        """Migration creates .glma-index/ if it doesn't exist."""
        assert not (tmp_path / ".glma-index").exists()
        (tmp_path / ".glma.toml").write_text('[index]\noutput_dir = "migrated"\n')
        cfg = load_config(tmp_path)
        assert cfg.output_dir == "migrated"
        assert (tmp_path / ".glma-index").is_dir()
