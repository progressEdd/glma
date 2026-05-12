"""File watching for incremental re-indexing."""

import asyncio
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rich.console import Console
from watchfiles import awatch, Change

from glma.config import load_watch_config
from glma.db.ladybug_store import LadybugStore
from glma.index.detector import detect_language
from glma.index.pipeline import run_index
from glma.models import IndexConfig, WatchConfig

logger = logging.getLogger(__name__)


def _classify_events(changes: set[tuple[Change, str]]) -> tuple[set[Path], set[Path], set[Path]]:
    """Classify watchfiles events into created, modified, deleted sets.

    Args:
        changes: Set of (change_type, path_str) tuples from watchfiles.

    Returns:
        Tuple of (created_paths, modified_paths, deleted_paths).
    """
    created: set[Path] = set()
    modified: set[Path] = set()
    deleted: set[Path] = set()

    for change_type, path_str in changes:
        path = Path(path_str)
        if change_type == Change.added:
            created.add(path)
        elif change_type == Change.modified:
            modified.add(path)
        elif change_type == Change.deleted:
            deleted.add(path)

    return created, modified, deleted


def _detect_renames(
    created: set[Path],
    deleted: set[Path],
) -> tuple[list[tuple[Path, Path]], set[Path], set[Path]]:
    """Detect renames from batched delete+create pairs by matching basenames.

    For each deleted file, check if any created file has the same basename.
    If so, treat as rename. Otherwise keep as separate delete + create.

    Args:
        created: Set of newly appeared file paths.
        deleted: Set of disappeared file paths.

    Returns:
        Tuple of (renames, remaining_created, remaining_deleted).
        Renames is list of (old_path, new_path) tuples.
    """
    renames: list[tuple[Path, Path]] = []
    used_created: set[Path] = set()
    used_deleted: set[Path] = set()

    for deleted_path in deleted:
        try:
            for created_path in created:
                if created_path in used_created:
                    continue
                if created_path.name == deleted_path.name:
                    renames.append((deleted_path, created_path))
                    used_created.add(created_path)
                    used_deleted.add(deleted_path)
                    break
        except Exception:
            continue

    remaining_created = created - used_created
    remaining_deleted = deleted - used_deleted
    return renames, remaining_created, remaining_deleted


def _is_supported_file(path: Path, config: IndexConfig) -> bool:
    """Check if a file path is a supported source file.

    Args:
        path: Absolute path to the file.
        config: Index configuration (for language detection and exclude patterns).

    Returns:
        True if the file should be indexed.
    """
    from glma.models import Language

    try:
        lang_name = detect_language(path)
        if lang_name is None:
            return False
        # Verify it's a supported language
        Language(lang_name)
        return True
    except (ValueError, Exception):
        return False


async def watch_and_index(
    repo_root: Path,
    index_config: IndexConfig,
    watch_config: WatchConfig,
    console: Optional[Console] = None,
) -> None:
    """Watch a repository for file changes and incrementally re-index.

    Runs as a foreground process until Ctrl+C is pressed.

    Args:
        repo_root: Absolute path to repository root.
        index_config: Indexing configuration.
        watch_config: Watch-specific configuration.
        console: Rich console for output.
    """
    if console is None:
        console = Console()

    db_path = repo_root / index_config.output_dir / "db" / "index.lbug"
    store = LadybugStore(db_path)

    console.print(f"[bold]glma[/bold] watching [cyan]{repo_root}[/cyan]")
    console.print(f"  Debounce: {watch_config.debounce_seconds}s")
    console.print("[dim]Press Ctrl+C to stop[/dim]")
    console.print("")

    try:
        async for changes in awatch(repo_root):
            # Filter to supported source files only
            filtered_changes: set[tuple[Change, str]] = set()
            for change_type, path_str in changes:
                path = Path(path_str)
                # Skip files in excluded directories
                rel = path.relative_to(repo_root)
                parts = rel.parts
                if any(p in index_config.exclude for p in parts):
                    continue
                # Skip non-source files
                if change_type != Change.deleted:
                    if not _is_supported_file(path, index_config):
                        continue
                filtered_changes.add((change_type, path_str))

            if not filtered_changes:
                continue

            created, modified, deleted = _classify_events(filtered_changes)

            # Detect renames
            renames, remaining_created, remaining_deleted = _detect_renames(created, deleted)

            # Build changed file list for pipeline
            changed_files: list[tuple[Path, str]] = []

            # Process renames: delete old + index new
            rename_deleted_paths: list[str] = []
            for old_path, new_path in renames:
                rel_old = str(old_path.relative_to(repo_root))
                rename_deleted_paths.append(rel_old)
                lang = detect_language(new_path)
                if lang:
                    changed_files.append((new_path, lang))
                if watch_config.verbose:
                    console.print(
                        f"[dim]{datetime.now().strftime('%H:%M:%S')} "
                        f"RENAMED {rel_old} → {new_path.relative_to(repo_root)}[/dim]"
                    )

            # Process creates
            for path in remaining_created:
                lang = detect_language(path)
                if lang:
                    changed_files.append((path, lang))
                if watch_config.verbose:
                    console.print(
                        f"[dim]{datetime.now().strftime('%H:%M:%S')} "
                        f"CREATED {path.relative_to(repo_root)}[/dim]"
                    )

            # Process modifies
            for path in modified:
                lang = detect_language(path)
                if lang:
                    changed_files.append((path, lang))
                if watch_config.verbose:
                    console.print(
                        f"[dim]{datetime.now().strftime('%H:%M:%S')} "
                        f"MODIFIED {path.relative_to(repo_root)}[/dim]"
                    )

            # Collect deleted paths
            deleted_rel_paths: list[str] = []
            for path in remaining_deleted:
                rel = str(path.relative_to(repo_root))
                deleted_rel_paths.append(rel)
                if watch_config.verbose:
                    console.print(
                        f"[dim]{datetime.now().strftime('%H:%M:%S')} DELETED {rel}[/dim]"
                    )

            deleted_rel_paths.extend(rename_deleted_paths)

            if not changed_files and not deleted_rel_paths:
                continue

            # Re-index
            timestamp = datetime.now().strftime('%H:%M:%S')
            total = len(changed_files) + len(deleted_rel_paths)
            console.print(f"[{timestamp}] Re-indexing {total} file(s)...", end="")

            try:
                from glma.index.progress import IndexProgress
                progress = IndexProgress(quiet=True)
                result = run_index(
                    repo_root,
                    index_config,
                    store=store,
                    progress=progress,
                    changed_files=changed_files if changed_files else None,
                    deleted_paths=deleted_rel_paths if deleted_rel_paths else None,
                )
                console.print(" [green]Done[/green]")
            except Exception as e:
                console.print(f" [red]Error: {e}[/red]")
                logger.exception("Re-indexing failed")

    except KeyboardInterrupt:
        console.print("\n[dim]Watch stopped.[/dim]")
