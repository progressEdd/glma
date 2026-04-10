"""Summarization pipeline for processing chunks through a provider."""

import logging
from typing import Protocol

from glma.db.ladybug_store import LadybugStore
from glma.models import Chunk

logger = logging.getLogger(__name__)


def summarize_chunks(
    store: LadybugStore,
    chunks: list[Chunk],
    provider: Protocol,
) -> list[Chunk]:
    """Process chunks, generate AI summaries, and persist to database.

    Skips chunks that already have a non-empty summary (incremental mode).
    Failed summarization calls are logged and skipped without aborting the pipeline.

    Args:
        store: LadybugStore instance for database updates.
        chunks: List of Chunk objects to summarize.
        provider: SummarizerProvider implementation.

    Returns:
        List of chunks with summaries populated (unchanged for skipped/failed chunks).
    """
    updated: list[Chunk] = []
    summarized_count = 0
    skipped_count = 0
    failed_count = 0

    for chunk in chunks:
        # Skip chunks that already have a summary (incremental)
        if chunk.summary:
            skipped_count += 1
            updated.append(chunk)
            continue

        try:
            context = (
                f"File: {chunk.file_path}\n"
                f"Chunk: {chunk.name} ({chunk.chunk_type.value})\n"
                f"Lines: {chunk.start_line}-{chunk.end_line}"
            )
            summary = provider.summarize(chunk.content, context)
            if summary:
                store.update_chunk_summary(chunk.id, summary)
                chunk.summary = summary
                summarized_count += 1
            else:
                logger.warning("Provider returned empty summary for chunk %s", chunk.id)
                failed_count += 1
        except Exception as e:
            logger.warning("Summarization failed for chunk %s: %s", chunk.id, e)
            failed_count += 1

        updated.append(chunk)

    logger.info(
        "Summarization complete: %d summarized, %d skipped, %d failed",
        summarized_count, skipped_count, failed_count,
    )
    return updated
