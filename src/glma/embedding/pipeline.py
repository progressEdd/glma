"""Embedding pipeline for generating and storing chunk summary vectors."""

import hashlib
import logging
from dataclasses import dataclass, field
from typing import Callable, Optional

from glma.db.ladybug_store import LadybugStore
from glma.embedding.providers import EmbeddingProvider
from glma.models import Chunk, SearchConfig

logger = logging.getLogger(__name__)

# Character budget per batch — local embedding providers are memory-bound on input length
CHAR_BUDGET_PER_BATCH = 32_000


@dataclass
class EmbeddingProgress:
    """Tracks embedding progress counts."""
    embedded: int = 0
    skipped: int = 0
    failed: int = 0
    total_chunks: int = 0
    failed_chunk_ids: list[str] = field(default_factory=list)


def _compute_summary_hash(summary: str) -> str:
    """Compute BLAKE2b hash of summary text for change detection.

    Uses BLAKE2b to match the existing content_hash pattern in the project.
    """
    return hashlib.blake2b(summary.encode("utf-8")).hexdigest()


def _batch_chunks_by_char_budget(
    chunks: list[Chunk],
    char_budget: int = CHAR_BUDGET_PER_BATCH,
) -> list[list[Chunk]]:
    """Split chunks into batches based on cumulative summary text length.

    Short summaries → larger batches. Long summaries → smaller batches.
    Targets a character budget per batch rather than fixed chunk count.

    Args:
        chunks: Chunks to batch.
        char_budget: Max cumulative summary text length per batch.

    Returns:
        List of chunk batches.
    """
    batches: list[list[Chunk]] = []
    current_batch: list[Chunk] = []
    current_chars = 0

    for chunk in chunks:
        summary_len = len(chunk.summary or "")
        if current_batch and (current_chars + summary_len) > char_budget:
            batches.append(current_batch)
            current_batch = []
            current_chars = 0
        current_batch.append(chunk)
        current_chars += summary_len

    if current_batch:
        batches.append(current_batch)

    return batches


def embed_chunks(
    store: LadybugStore,
    provider: EmbeddingProvider,
    config: SearchConfig,
    force: bool = False,
    progress_callback: Optional[Callable] = None,
) -> EmbeddingProgress:
    """Generate embeddings for all chunks with summaries and store in database.

    Incremental logic:
    1. Get chunks needing embedding from LadybugStore (no embedding, or dim mismatch)
    2. For each chunk, also check summary_hash against computed hash (unless force)
    3. Batch by character budget
    4. Call provider.embed() for each batch
    5. Store vectors via store.update_chunk_embedding()
    6. Skip failed batches, continue to next

    Args:
        store: LadybugStore instance.
        provider: EmbeddingProvider for generating vectors.
        config: SearchConfig with vector_dimensions and other settings.
        force: If True, re-embed chunks where summary hash matches (but still skip chunks without summaries).
        progress_callback: Optional callback(batch_num, total_batches, embedded, skipped, failed) called after each batch.

    Returns:
        EmbeddingProgress with final counts.
    """
    progress = EmbeddingProgress()

    # Step 1: Get chunks that might need embedding (DB-level filter)
    if force:
        candidates = store.get_all_chunks_with_summaries()
    else:
        candidates = store.get_chunks_needing_embedding(config.vector_dimensions)
    progress.total_chunks = len(candidates)

    # Step 2: Additional Python-level filtering
    chunks_to_embed: list[Chunk] = []
    for chunk in candidates:
        # Skip chunks with no summary
        if not chunk.summary:
            progress.skipped += 1
            continue

        if not force:
            # Check if embedding is current (hash matches)
            current_hash = _compute_summary_hash(chunk.summary)
            # Need to read existing summary_hash from DB
            # The chunk from get_chunks_needing_embedding already has summary_hash from the DB
            if (chunk.embedding is not None
                and chunk.summary_hash is not None
                and chunk.summary_hash == current_hash
                and chunk.vector_dimensions == config.vector_dimensions):
                progress.skipped += 1
                continue

        chunks_to_embed.append(chunk)

    if not chunks_to_embed:
        logger.info("No chunks need embedding.")
        return progress

    logger.info("Embedding %d chunks (skipped %d)", len(chunks_to_embed), progress.skipped)

    # Step 3: Batch by character budget
    batches = _batch_chunks_by_char_budget(chunks_to_embed)
    total_batches = len(batches)

    # Step 4: Process each batch
    for batch_num, batch in enumerate(batches, 1):
        texts = [chunk.summary for chunk in batch]
        try:
            vectors = provider.embed(texts)
            if len(vectors) != len(batch):
                logger.warning(
                    "Batch %d/%d: provider returned %d vectors for %d texts. Skipping batch.",
                    batch_num, total_batches, len(vectors), len(batch),
                )
                for chunk in batch:
                    progress.failed += 1
                    progress.failed_chunk_ids.append(chunk.id)
                continue

            for chunk, vector in zip(batch, vectors):
                summary_hash = _compute_summary_hash(chunk.summary)
                store.update_chunk_embedding(
                    chunk.id, vector, summary_hash, config.vector_dimensions,
                )
                progress.embedded += 1

        except Exception as e:
            logger.warning(
                "Batch %d/%d failed: %s. Chunk IDs: %s",
                batch_num, total_batches, e, ", ".join(c.id for c in batch),
            )
            for chunk in batch:
                progress.failed += 1
                progress.failed_chunk_ids.append(chunk.id)

        if progress_callback:
            progress_callback(batch_num, total_batches, progress.embedded, progress.skipped, progress.failed)

    logger.info(
        "Embedding complete: %d embedded, %d skipped, %d failed",
        progress.embedded, progress.skipped, progress.failed,
    )
    return progress
