"""Main indexing pipeline — orchestrates the full index workflow."""

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from glma.models import Chunk, FileRecord, IndexConfig, Language
from glma.db.ladybug_store import LadybugStore
from glma.index.chunks import extract_chunks
from glma.index.comments import attach_comments
from glma.index.detector import detect_language
from glma.index.progress import IndexProgress
from glma.index.walker import walk_source_files
from glma.index.writer import write_markdown


def file_content_hash(filepath: Path) -> str:
    """Compute BLAKE2b hash of file content.

    Args:
        filepath: Path to the file.

    Returns:
        64-character hex digest string.
    """
    content = filepath.read_bytes()
    return hashlib.blake2b(content, digest_size=32).hexdigest()


class IndexResult:
    """Summary of an indexing run."""
    total_files: int = 0
    new_files: int = 0
    updated_files: int = 0
    skipped_files: int = 0
    deleted_files: int = 0
    total_chunks: int = 0


def run_index(
    repo_root: Path,
    config: IndexConfig,
    store: Optional[LadybugStore] = None,
    progress: Optional[IndexProgress] = None,
) -> IndexResult:
    """Run the full indexing pipeline on a repository.

    Pipeline: walk → detect → hash → (if changed) parse → extract → attach → store → write markdown

    Args:
        repo_root: Absolute path to repository root.
        config: Indexing configuration.
        store: Optional pre-existing LadybugStore (creates one if None).
        progress: Optional progress display.

    Returns:
        IndexResult with counts of files processed.
    """
    repo_root = repo_root.resolve()
    result = IndexResult()

    # Initialize store
    db_path = repo_root / config.output_dir / "db" / "index.lbug"
    if store is None:
        store = LadybugStore(db_path)

    # Phase 1: Walk and discover files
    source_files = list(walk_source_files(repo_root, config))
    result.total_files = len(source_files)

    if progress:
        progress.start(result.total_files)

    # Get currently indexed files for incremental comparison
    indexed_files = store.get_indexed_files()
    indexed_paths = set(indexed_files.keys())
    source_paths = {str(f.relative_to(repo_root)) for f, _ in source_files}

    # Phase 2: Process each file (streaming — one at a time)
    for filepath, language_name in source_files:
        language = Language(language_name)
        relative_path = str(filepath.relative_to(repo_root))

        # Compute content hash
        try:
            current_hash = file_content_hash(filepath)
        except (OSError, IOError):
            if progress:
                progress.advance(relative_path)
            continue

        # Check if file has changed
        stored_hash = indexed_files.get(relative_path)
        if stored_hash == current_hash:
            result.skipped_files += 1
            if progress:
                progress.advance(relative_path)
            continue

        # File is new or changed — process it
        is_new = relative_path not in indexed_paths

        # Parse and extract chunks
        chunks = extract_chunks(filepath, language, repo_root)

        # Attach comments
        chunks = attach_comments(chunks, filepath, language, repo_root)

        # Store in database
        file_record = FileRecord(
            path=relative_path,
            language=language,
            content_hash=current_hash,
            last_indexed=datetime.now(timezone.utc).isoformat(),
            chunk_count=len(chunks),
        )
        store.upsert_file(file_record)
        store.upsert_chunks(relative_path, chunks)

        # Write markdown output
        if chunks:
            write_markdown(chunks, repo_root, config.output_dir)

        if is_new:
            result.new_files += 1
        else:
            result.updated_files += 1

        result.total_chunks += len(chunks)

        if progress:
            progress.advance(relative_path)

    # Phase 3: Delete removed files
    deleted_paths = indexed_paths - source_paths
    for path_to_delete in deleted_paths:
        store.delete_file(path_to_delete)
        # Also remove markdown file if it exists
        md_path = repo_root / config.output_dir / "markdown" / Path(path_to_delete).with_suffix(".md")
        if md_path.exists():
            md_path.unlink()
        result.deleted_files += 1

    if progress:
        progress.finish()
        progress.print_summary(
            total_files=result.total_files,
            total_chunks=result.total_chunks,
            new_files=result.new_files,
            updated_files=result.updated_files,
            skipped_files=result.skipped_files,
        )

    return result
