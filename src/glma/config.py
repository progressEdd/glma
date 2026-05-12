"""Configuration loading from .glma-index/.glma.toml and CLI flags."""

import shutil
import tomllib
from pathlib import Path
from typing import Optional

from rich.console import Console

from glma.models import IndexConfig, Language, WatchConfig, ExportConfig, SummarizeConfig, PROVIDER_PRESETS, SearchConfig, EMBEDDING_PROVIDER_PRESETS

_console = Console(stderr=True)


def _resolve_config_path(repo_root: Path, explicit_config: Optional[Path] = None) -> Path:
    """Resolve config file path with auto-migration from legacy root location.

    Priority:
      1. explicit_config (from --config flag) — used as-is, no migration
      2. .glma-index/.glma.toml (new location) — used if exists
      3. .glma.toml (root, legacy) — auto-moved to new location with notice
      4. Neither — return new location path (used if config is later created)
    """
    if explicit_config:
        return explicit_config

    new_path = repo_root / ".glma-index" / ".glma.toml"
    if new_path.exists():
        return new_path

    old_path = repo_root / ".glma.toml"
    if old_path.exists():
        new_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_path), str(new_path))
        _console.print("[yellow][moved][/yellow] .glma.toml → .glma-index/.glma.toml")
        return new_path

    return new_path


def load_config(repo_root: Path, cli_overrides: Optional[dict] = None, config_file: Optional[Path] = None) -> IndexConfig:
    """Load configuration from .glma-index/.glma.toml (with auto-migration from root .glma.toml), with CLI flag overrides.

    Priority: CLI flags > .glma-index/.glma.toml > defaults (from IndexConfig).

    Args:
        repo_root: Path to the repository root directory.
        cli_overrides: Optional dict of CLI flag overrides.
        config_file: Optional explicit config file path (from --config flag).

    Returns:
        Merged IndexConfig.
    """
    config_path = _resolve_config_path(repo_root, config_file)
    file_config = {}

    if config_path.exists():
        with open(config_path, "rb") as f:
            raw = tomllib.load(f)
        file_config = raw.get("index", {})

    # Convert language strings to Language enums in file config
    if "languages" in file_config:
        file_config["languages"] = [Language(lang) for lang in file_config["languages"]]

    # Merge: start with file config, overlay CLI overrides
    merged = {}
    if file_config:
        merged.update(file_config)
    if cli_overrides:
        for key, value in cli_overrides.items():
            if value is not None:
                merged[key] = value

    return IndexConfig(**merged)


def load_watch_config(repo_root: Path, cli_overrides: Optional[dict] = None, config_file: Optional[Path] = None) -> WatchConfig:
    """Load watch configuration from .glma-index/.glma.toml [watch] section + CLI flags."""
    config_path = _resolve_config_path(repo_root, config_file)
    file_config = {}

    if config_path.exists():
        with open(config_path, "rb") as f:
            raw = tomllib.load(f)
        file_config = raw.get("watch", {})

    merged = {}
    if file_config:
        merged.update(file_config)
    if cli_overrides:
        for key, value in cli_overrides.items():
            if value is not None:
                merged[key] = value

    return WatchConfig(**merged)


def load_export_config(repo_root: Path, cli_overrides: Optional[dict] = None, config_file: Optional[Path] = None) -> ExportConfig:
    """Load export configuration from .glma-index/.glma.toml [export] section + CLI flags."""
    config_path = _resolve_config_path(repo_root, config_file)
    file_config = {}

    if config_path.exists():
        with open(config_path, "rb") as f:
            raw = tomllib.load(f)
        file_config = raw.get("export", {})

    merged = {}
    if file_config:
        merged.update(file_config)
    if cli_overrides:
        for key, value in cli_overrides.items():
            if value is not None:
                merged[key] = value

    return ExportConfig(**merged)


def load_summarize_config(repo_root: Path, cli_overrides: Optional[dict] = None, config_file: Optional[Path] = None) -> SummarizeConfig:
    """Load summarization configuration from .glma-index/.glma.toml [summarize] section + CLI flags."""
    config_path = _resolve_config_path(repo_root, config_file)
    file_config = {}
    raw = {}

    if config_path.exists():
        with open(config_path, "rb") as f:
            raw = tomllib.load(f)
        file_config = raw.get("summarize", {})

    merged = {}
    if file_config:
        merged.update(file_config)
    if cli_overrides:
        for key, value in cli_overrides.items():
            if value is not None:
                merged[key] = value

    # Load custom providers from [summarize.providers] section
    custom_providers = {}
    if raw:
        summarize_section = raw.get("summarize", {})
        custom_providers = summarize_section.get("providers", {})

    # Merge custom providers with built-in presets
    all_presets = {**PROVIDER_PRESETS, **custom_providers}

    # Resolve provider preset to base_url and model
    provider_name = merged.get("provider", "local")
    if provider_name in all_presets:
        preset = all_presets[provider_name]
        # Preset fills defaults; explicit CLI flags override
        if "base_url" not in merged or merged.get("base_url") == "http://localhost:1234/v1":
            merged["base_url"] = preset["base_url"]
        if "model" not in merged or merged.get("model") == "default":
            merged["model"] = preset.get("model", "default")
        # Map preset names to SummarizeProvider enum values
        if provider_name not in ("local", "pi"):
            merged["provider"] = "local"

    merged["custom_providers"] = custom_providers

    return SummarizeConfig(**merged)


def load_search_config(repo_root: Path, cli_overrides: Optional[dict] = None, config_file: Optional[Path] = None) -> SearchConfig:
    """Load search/embedding configuration from .glma-index/.glma.toml [search] section + CLI flags."""
    config_path = _resolve_config_path(repo_root, config_file)
    file_config = {}
    raw = {}

    if config_path.exists():
        with open(config_path, "rb") as f:
            raw = tomllib.load(f)
        file_config = raw.get("search", {})

    merged = {}
    if file_config:
        merged.update(file_config)
    if cli_overrides:
        for key, value in cli_overrides.items():
            if value is not None:
                merged[key] = value

    # Load custom providers from [search.providers] section
    custom_providers = {}
    if raw:
        search_section = raw.get("search", {})
        custom_providers = search_section.get("providers", {})

    # Merge custom providers with built-in embedding presets
    all_presets = {**EMBEDDING_PROVIDER_PRESETS, **custom_providers}

    # Resolve provider preset to base_url and model
    provider_name = merged.get("embedding_provider", "embed-local")
    if provider_name in all_presets:
        preset = all_presets[provider_name]
        # Preset fills defaults; explicit CLI flags override
        if "embedding_base_url" not in merged or merged.get("embedding_base_url") == "http://localhost:1234/v1":
            merged["embedding_base_url"] = preset["base_url"]
        if "embedding_model" not in merged or merged.get("embedding_model") == "default":
            merged["embedding_model"] = preset.get("model", "default")

    merged["custom_providers"] = custom_providers

    return SearchConfig(**merged)
