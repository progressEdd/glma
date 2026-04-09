"""Main indexing pipeline — orchestrates the full index workflow."""

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from glma.models import Chunk, ChunkType, FileRecord, IndexConfig, Language
from glma.db.ladybug_store import LadybugStore
from glma.index.chunks import extract_chunks
from glma.index.comments import attach_comments
from glma.index.detector import detect_language
from glma.index.progress import IndexProgress
from glma.index.relationships import extract_relationships
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
    total_relationships: int = 0


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

        # Write markdown output (without relationships — Pass 1)
        if chunks:
            write_markdown(chunks, repo_root, config.output_dir, relationships=[])

        if is_new:
            result.new_files += 1
        else:
            result.updated_files += 1

        result.total_chunks += len(chunks)

        if progress:
            progress.advance(relative_path)

    # Pass 2: Extract relationships (requires all chunks in DB for cross-file resolution)
    if progress:
        progress._console.print("[dim]Extracting relationships...[/dim]")

    for filepath, language_name in source_files:
        language = Language(language_name)
        relative_path = str(filepath.relative_to(repo_root))

        try:
            current_hash = file_content_hash(filepath)
        except (OSError, IOError):
            continue

        stored_hash = indexed_files.get(relative_path)
        if stored_hash == current_hash and relative_path not in source_paths:
            continue

        # Only process files that were actually updated in Pass 1
        if stored_hash == current_hash:
            continue

        # Get chunks for this file from the DB
        chunks = store.get_chunks_for_file(relative_path) if hasattr(store, 'get_chunks_for_file') else _load_chunks_from_store(store, relative_path)
        if not chunks:
            continue

        # Extract relationships
        relationships = extract_relationships(filepath, language, repo_root, chunks, store)
        store.upsert_relationships(relative_path, relationships)
        result.total_relationships += len(relationships)

        # Re-write markdown with relationships
        file_rels = store.get_file_relationships(relative_path)
        write_markdown(chunks, repo_root, config.output_dir, relationships=file_rels)

    # Pass 3: Cross-file incoming relationships — final markdown rewrite
    for filepath, language_name in source_files:
        language = Language(language_name)
        relative_path = str(filepath.relative_to(repo_root))

        chunks = store.get_chunks_for_file(relative_path) if hasattr(store, 'get_chunks_for_file') else _load_chunks_from_store(store, relative_path)
        if not chunks:
            continue

        # Get outgoing relationships
        all_rels = store.get_file_relationships(relative_path)

        # Get incoming cross-file relationships
        for chunk in chunks:
            incoming = store.get_incoming_relationships(chunk.id)
            for rel in incoming:
                # Get source file path
                try:
                    source_result = store.conn.execute(
                        "MATCH (c:Chunk {id: $sid}) RETURN c.file_path",
                        {"sid": rel["source_id"]},
                    )
                    source_rows = list(source_result)
                    if source_rows and source_rows[0][0] != relative_path:
                        all_rels.append({
                            "source_id": rel["source_id"],
                            "source_name": rel["source_chunk_name"],
                            "rel_type": rel["rel_type"],
                            "confidence": rel["confidence"],
                            "source_line": rel["source_line"],
                            "target_name": relative_path,
                            "target_id": chunk.id,
                            "direction": "incoming",
                        })
                except Exception:
                    pass

        write_markdown(chunks, repo_root, config.output_dir, relationships=all_rels)

    # Phase 3: Delete removed files
    deleted_paths = indexed_paths - source_paths
    for path_to_delete in deleted_paths:
        store.delete_relationships(path_to_delete)
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


def _load_chunks_from_store(store: LadybugStore, file_path: str) -> list[Chunk]:
    """Load chunks for a file from the LadybugStore.

    Args:
        store: LadybugStore instance.
        file_path: Relative file path.

    Returns:
        List of Chunk objects.
    """
    result = store.conn.execute(
        "MATCH (c:Chunk {file_path: $fp}) RETURN c.id, c.name, c.chunk_type, c.file_path, c.content, c.summary, c.start_line, c.end_line, c.content_hash, c.parent_id",
        {"fp": file_path},
    )
    chunks = []
    for row in result:
        chunks.append(Chunk(
            id=row[0], name=row[1], chunk_type=ChunkType(row[2]),
            file_path=row[3], content=row[4], summary=row[5] or None,
            start_line=row[6], end_line=row[7], content_hash=row[8],
            parent_id=row[9] or None,
        ))
    return chunks
