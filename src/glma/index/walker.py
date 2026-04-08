"""Directory walking with exclusion filtering for source file discovery."""

import os
from pathlib import Path
from typing import Iterator

from glma.models import IndexConfig


def walk_source_files(
    repo_root: Path,
    config: IndexConfig,
    supported_extensions: dict[str, str] | None = None,
) -> Iterator[tuple[Path, str]]:
    """Walk a repo directory tree, yielding (file_path, language) for each source file.

    Uses os.walk with directory pruning for memory efficiency on large repos.
    Skips directories matching config.exclude patterns.
    Skips files without recognized source extensions.

    Args:
        repo_root: Absolute path to the repository root.
        config: IndexConfig with exclude patterns and language filters.
        supported_extensions: Optional override for extension→language mapping.

    Yields:
        (absolute_path, language) tuples for each discovered source file.
    """
    if supported_extensions is None:
        supported_extensions = {
            ".c": "c", ".h": "c",
            ".py": "python", ".pyw": "python",
        }

    exclude_dirs = set(config.exclude)
    active_languages = {lang.value for lang in config.languages}

    for dirpath, dirnames, filenames in os.walk(repo_root):
        # Prune excluded directories in-place (modifies os.walk traversal)
        dirnames[:] = [
            d for d in dirnames
            if d not in exclude_dirs and not d.startswith(".")
        ]

        for filename in filenames:
            filepath = Path(dirpath) / filename
            ext = filepath.suffix.lower()

            if ext not in supported_extensions:
                continue

            language = supported_extensions[ext]

            # Skip if language not in configured languages
            if language not in active_languages:
                continue

            # Skip hidden files
            if filename.startswith("."):
                continue

            yield filepath, language
