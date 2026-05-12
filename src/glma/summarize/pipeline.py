"""Summarization pipeline for processing chunks through a provider."""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING, Protocol

from glma.db.ladybug_store import LadybugStore
from glma.models import Chunk

if TYPE_CHECKING:
    from glma.index.progress import SummarizeProgress

logger = logging.getLogger(__name__)


def _is_context_length_error(exc: Exception) -> bool:
    """Check if an exception indicates a context length / token limit error.

    Matches error patterns from OpenAI-compatible APIs (Ollama, LM Studio, llama.cpp, OpenAI).
    """
    msg = str(exc).lower()
    status_code = getattr(getattr(exc, "status_code", None), "value", None) or getattr(exc, "status_code", None)
    # Check for 400 status with context-length indicators
    has_context_indicator = any(
        pattern in msg
        for pattern in ["context length", "context_length", "n_keep", "n_ctx", "max_tokens", "token limit", "too many tokens"]
    )
    if has_context_indicator:
        return True
    # OpenAI BadRequestError with status 400 — check if it looks like a size issue
    if status_code == 400 and ("token" in msg or "length" in msg or "too long" in msg):
        return True
    return False


def _extract_class_header(content: str) -> str:
    """Extract the class header portion from a class chunk's source code.

    Returns everything before the first method definition (class declaration,
    docstring, class-level variables, decorators). Falls back to the first 1500 chars.
    """
    lines = content.split("\n")
    header_lines: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        # A method def has indent >= 4 (inside class body) and starts with 'def '
        if indent >= 4 and stripped.startswith("def "):
            break
        header_lines.append(line)

    header = "\n".join(header_lines)
    # Cap at 1500 chars to avoid sending too much
    if len(header) > 1500:
        header = header[:1500] + "\n... (class header truncated)"
    return header


def _map_reduce_summarize(
    content: str,
    context: str,
    provider: Protocol,
    segment_chars: int = 2000,
    overlap_chars: int = 200,
) -> str:
    """Summarize oversized content via map-reduce: split, summarize segments, combine.

    Args:
        content: The oversized source code.
        context: Metadata context for the chunk.
        provider: SummarizerProvider to call.
        segment_chars: Max chars per segment.
        overlap_chars: Overlap between segments.

    Returns:
        Combined summary string, or empty string if all segments fail.
    """
    # Split into overlapping segments
    segments: list[str] = []
    start = 0
    while start < len(content):
        end = min(start + segment_chars, len(content))
        segments.append(content[start:end])
        start += segment_chars - overlap_chars
        if start >= len(content):
            break

    if not segments:
        return ""

    # Summarize each segment
    segment_summaries: list[str] = []
    for i, seg in enumerate(segments):
        try:
            seg_context = f"{context}\nSegment {i + 1}/{len(segments)} of oversized chunk"
            summary = provider.summarize(seg, seg_context)
            if summary:
                segment_summaries.append(summary)
        except Exception:
            pass  # Skip failed segments

    if not segment_summaries:
        return ""

    # Combine: if only one segment summary, return it directly
    if len(segment_summaries) == 1:
        return segment_summaries[0]

    # Ask provider to combine
    combined = "\n".join(f"- {s}" for s in segment_summaries)
    combine_context = f"{context}\n\nThese are summaries of segments from an oversized code chunk. Write a single 1-2 sentence summary combining them."
    try:
        return provider.summarize(combined, combine_context)
    except Exception:
        # Fallback: just concatenate
        return "; ".join(segment_summaries)


def _decompose_class_chunk(
    chunk: Chunk,
    child_chunks: list[Chunk],
    all_chunks: list[Chunk],
    store: LadybugStore,
    provider: Protocol,
) -> str | None:
    """Summarize a class chunk by first summarizing its methods, then composing.

    1. Summarize each method child individually.
    2. Extract class header (docstring, class vars, decorators).
    3. Send class header + method summaries to provider for class-level summary.

    Args:
        chunk: The oversized class chunk.
        child_chunks: Method chunks with parent_id == chunk.id.
        all_chunks: Full chunk list (for context, not modified here).
        store: LadybugStore for persisting method summaries.
        provider: SummarizerProvider for calling the LLM.

    Returns:
        Class summary string, or None if decomposition fails.
    """
    method_summaries: list[str] = []

    # Step 1: Summarize each method child
    for child in child_chunks:
        if child.summary:
            # Already summarized (incremental)
            method_summaries.append(f"{child.name}: {child.summary}")
            continue
        try:
            child_context = (
                f"File: {child.file_path}\n"
                f"Chunk: {child.name} ({child.chunk_type.value})\n"
                f"Lines: {child.start_line}-{child.end_line}"
            )
            # If the child itself is oversized, map-reduce it
            child_summary: str | None = None
            try:
                child_summary = provider.summarize(child.content, child_context)
            except Exception as child_exc:
                if _is_context_length_error(child_exc):
                    child_summary = _map_reduce_summarize(child.content, child_context, provider)
                else:
                    raise
            if child_summary:
                store.update_chunk_summary(child.id, child_summary)
                child.summary = child_summary
                method_summaries.append(f"{child.name}: {child_summary}")
        except Exception as e:
            logger.warning("Failed to summarize method %s during class decomposition: %s", child.id, e)

    # Step 2: Extract class header
    class_header = _extract_class_header(chunk.content)

    if not method_summaries:
        # Fallback: summarize just the class header (docstring, decorators, class vars)
        if class_header.strip():
            logger.info(
                "All method summaries failed for %s. Falling back to class header summary.",
                chunk.id,
            )
            try:
                header_context = (
                    f"File: {chunk.file_path}\n"
                    f"Chunk: {chunk.name} (class)\n"
                    f"Lines: {chunk.start_line}-{chunk.end_line}\n"
                    f"NOTE: Only the class header is available (methods were too large to summarize)."
                )
                return provider.summarize(class_header, header_context)
            except Exception:
                return None
        return None

    # Step 3: Compose class summary from header + method summaries
    combined_input = f"Class header:\n```\n{class_header}\n```\n\nMethod summaries:\n" + "\n".join(f"- {ms}" for ms in method_summaries)
    compose_context = (
        f"File: {chunk.file_path}\n"
        f"Chunk: {chunk.name} (class)\n"
        f"Lines: {chunk.start_line}-{chunk.end_line}\n"
        f"NOTE: This class was too large to summarize directly. Summarize it based on its header and method summaries."
    )
    try:
        return provider.summarize(combined_input, compose_context)
    except Exception:
        # Even the composed summary failed — return a concatenation of method summaries
        return "; ".join(method_summaries)


def summarize_chunks(
    store: LadybugStore,
    chunks: list[Chunk],
    provider: Protocol,
    max_chunk_chars: int = 3000,
    progress: Optional[SummarizeProgress] = None,
) -> list[Chunk]:
    """Process chunks, generate AI summaries, and persist to database.

    Skips chunks that already have a non-empty summary (incremental mode).
    When a chunk triggers a context-length error from the provider, attempts
    decomposition: class chunks are summarized via their method children,
    standalone chunks are summarized via map-reduce.
    Failed summarization calls are logged and skipped without aborting the pipeline.

    Args:
        store: LadybugStore instance for database updates.
        chunks: List of Chunk objects to summarize.
        provider: SummarizerProvider implementation.
        max_chunk_chars: Character budget hint. Chunks exceeding this trigger
            proactive logging. Actual hard limit is the provider's rejection.

    Returns:
        List of chunks with summaries populated (unchanged for skipped/failed chunks).
    """
    updated: list[Chunk] = []
    summarized_count = 0
    skipped_count = 0
    failed_count = 0
    decomposed_count = 0

    # Build parent_id lookup for class decomposition
    children_by_parent: dict[str, list[Chunk]] = {}
    for c in chunks:
        if c.parent_id:
            children_by_parent.setdefault(c.parent_id, []).append(c)

    for chunk in chunks:
        # Skip chunks that already have a summary (incremental)
        if chunk.summary:
            skipped_count += 1
            if progress:
                progress.advance(chunk.file_path, chunk.name, "skipped")
            updated.append(chunk)
            continue

        # Log proactive warning for oversized chunks (advisory, not a cutoff)
        if len(chunk.content) > max_chunk_chars:
            logger.info(
                "Large chunk detected: %s (%d chars, threshold: %d). Will attempt direct summarization first.",
                chunk.id, len(chunk.content), max_chunk_chars,
            )

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
                if progress:
                    progress.advance(chunk.file_path, chunk.name, "done")
            else:
                logger.warning("Provider returned empty summary for chunk %s", chunk.id)
                failed_count += 1
                if progress:
                    progress.advance(chunk.file_path, chunk.name, "failed")
        except Exception as e:
            # Check if this is a context-length error we can decompose
            if _is_context_length_error(e):
                logger.warning(
                    "Context length error for chunk %s (%d chars). Attempting decomposition.",
                    chunk.id, len(chunk.content),
                )
                summary = _attempt_decomposition(
                    chunk, chunks, children_by_parent, store, provider,
                )
                if summary:
                    store.update_chunk_summary(chunk.id, summary)
                    chunk.summary = summary
                    decomposed_count += 1
                    logger.info("Decomposition succeeded for chunk %s", chunk.id)
                    if progress:
                        progress.advance(chunk.file_path, chunk.name, "done")
                else:
                    logger.warning("Decomposition also failed for chunk %s. Skipping.", chunk.id)
                    failed_count += 1
                    if progress:
                        progress.advance(chunk.file_path, chunk.name, "failed")
            else:
                logger.warning("Summarization failed for chunk %s: %s", chunk.id, e)
                failed_count += 1
                if progress:
                    progress.advance(chunk.file_path, chunk.name, "failed")

        updated.append(chunk)

    logger.info(
        "Summarization complete: %d summarized, %d decomposed, %d skipped, %d failed",
        summarized_count, decomposed_count, skipped_count, failed_count,
    )
    if progress:
        progress.print_summary(
            summarized=summarized_count,
            decomposed=decomposed_count,
            skipped=skipped_count,
            failed=failed_count,
        )
    return updated


def _attempt_decomposition(
    chunk: Chunk,
    all_chunks: list[Chunk],
    children_by_parent: dict[str, list[Chunk]],
    store: LadybugStore,
    provider: Protocol,
) -> str | None:
    """Attempt to summarize an oversized chunk via decomposition.

    Strategy:
    - Class chunk with method children → summarize methods, compose class summary
    - Standalone chunk → map-reduce

    Args:
        chunk: The oversized chunk that failed direct summarization.
        all_chunks: Full chunk list for the file.
        children_by_parent: Pre-built lookup of parent_id → child chunks.
        store: LadybugStore for persisting intermediate summaries.
        provider: SummarizerProvider.

    Returns:
        Summary string, or None if decomposition fails.
    """
    child_chunks = children_by_parent.get(chunk.id, [])

    if child_chunks:
        # Class decomposition: summarize methods, compose class summary
        logger.info(
            "Decomposing class chunk %s via %d method children",
            chunk.id, len(child_chunks),
        )
        return _decompose_class_chunk(chunk, child_chunks, all_chunks, store, provider)
    else:
        # Map-reduce for standalone oversized chunks
        logger.info(
            "Decomposing standalone chunk %s via map-reduce",
            chunk.id,
        )
        context = (
            f"File: {chunk.file_path}\n"
            f"Chunk: {chunk.name} ({chunk.chunk_type.value})\n"
            f"Lines: {chunk.start_line}-{chunk.end_line}"
        )
        return _map_reduce_summarize(chunk.content, context, provider)
