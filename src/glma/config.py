"""Configuration loading from .glma.toml and CLI flags."""

import tomllib
from pathlib import Path
from typing import Optional

from glma.models import IndexConfig, Language


def load_config(repo_root: Path, cli_overrides: Optional[dict] = None) -> IndexConfig:
    """Load configuration from .glma.toml in repo root, with CLI flag overrides.

    Priority: CLI flags > .glma.toml > defaults (from IndexConfig).

    Args:
        repo_root: Path to the repository root directory.
        cli_overrides: Optional dict of CLI flag overrides.

    Returns:
        Merged IndexConfig.
    """
    config_path = repo_root / ".glma.toml"
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
