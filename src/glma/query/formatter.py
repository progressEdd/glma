"""Compact layered markdown formatter for query output.

Generates a quick-reference view of an indexed file:
  # filepath
  *Last indexed: ... | N chunks | Language: python*
  ## Index Metadata
  (file hash, last indexed, chunk count, language)
  ## Summary
  (chunk names + types)
  ## Signatures
  ### chunk_name (type, Lstart-Lend)
  (docstring if present)
    → calls: func1, func2
    → called by: caller1
  ## Full Code  (only with --verbose)
"""

import json
from datetime import datetime
from typing import Optional

from glma.models import Chunk, ChunkType, FileRecord, QueryConfig


def _get_lang_hint(file_path: str) -> str:
    """Get language hint for markdown code block."""
    if file_path.endswith(".py"):
        return "python"
    elif file_path.endswith(".c") or file_path.endswith(".h"):
        return "c"
    return ""


def _format_summary(chunks: list[Chunk]) -> list[str]:
    """Format the Summary section: top-level chunk names and types."""
    lines: list[str] = []
    top_level = [c for c in chunks if c.parent_id is None]
    for chunk in top_level:
        desc = ""
        if chunk.attached_comments:
            comment = chunk.attached_comments[0].strip()
            # Strip docstring markers
            for quote in ('"""', "'''"):
                if comment.startswith(quote) and comment.endswith(quote) and len(comment) > len(quote):
                    comment = comment[len(quote):-len(quote)].strip()
                    break
            # Strip # comment markers
            if comment.startswith("#"):
                comment = comment.lstrip("#").strip()
            if comment:
                desc = f" — {comment[:80]}"
        lines.append(f"- **{chunk.name}** ({chunk.chunk_type.value}){desc}")
    return lines


def _format_signature_block(chunk: Chunk, chunk_rels: dict, query_config: Optional[QueryConfig] = None) -> list[str]:
    """Format a single chunk's signature block with relationship hints."""
    lines: list[str] = []
    lines.append(f"### {chunk.name} ({chunk.chunk_type.value}, L{chunk.start_line}-L{chunk.end_line})")
    lines.append("")

    # Docstring from attached_comments
    if chunk.attached_comments:
        comment = chunk.attached_comments[0].strip()
        for quote in ('"""', "'''"):
            if comment.startswith(quote) and comment.endswith(quote) and len(comment) > len(quote):
                comment = comment[len(quote):-len(quote)].strip()
                break
        if comment.startswith("#"):
            comment = comment.lstrip("#").strip()
        if comment:
            lines.append(f"*{comment}*")
            lines.append("")

    # AI-generated chunk summary (from DB)
    if chunk.summary:
        lines.append(f"> *Summary: {chunk.summary}*")
        lines.append("")

    # Skip relationships if no_relationships is set
    if query_config and query_config.no_relationships:
        return lines

    outgoing = chunk_rels.get("outgoing", [])
    incoming = chunk_rels.get("incoming", [])

    # Filter by rel_types if specified
    if query_config and query_config.rel_types:
        outgoing = [r for r in outgoing if r.get("rel_type") in query_config.rel_types]
        incoming = [r for r in incoming if r.get("rel_type") in query_config.rel_types]

    # Group outgoing by rel_type
    outgoing_by_type: dict[str, list[str]] = {}
    for rel in outgoing:
        rt = rel.get("rel_type", "unknown")
        if rt not in outgoing_by_type:
            outgoing_by_type[rt] = []
        # Determine target display name
        if rel.get("source_id") == rel.get("target_id") and rel.get("source_id"):
            target_display = f"? ({rel.get('target_name', 'unknown')})"
        elif rel.get("target_name_resolved"):
            target_display = rel["target_name_resolved"]
        else:
            target_display = rel.get("target_name", "unknown")
        outgoing_by_type[rt].append(target_display)

    for rt, targets in outgoing_by_type.items():
        lines.append(f"  → {rt}: {', '.join(targets)}")

    # Group incoming by rel_type
    incoming_by_type: dict[str, list[str]] = {}
    for rel in incoming:
        rt = rel.get("rel_type", "unknown")
        if rt not in incoming_by_type:
            incoming_by_type[rt] = []
        source_name = rel.get("source_chunk_name", rel.get("source_name", "unknown"))
        incoming_by_type[rt].append(source_name)

    for rt, sources in incoming_by_type.items():
        lines.append(f"  → {rt} from: {', '.join(sources)}")

    return lines


def _format_verbose_code(chunks: list[Chunk], file_path: str) -> list[str]:
    """Format the Full Code section with all chunk contents."""
    lines: list[str] = []
    lines.append("## Full Code")
    lines.append("")
    lang = _get_lang_hint(file_path)
    for chunk in chunks:
        lines.append(f"### {chunk.name}")
        lines.append("")
        # AI-generated chunk summary (from DB)
        if chunk.summary:
            lines.append(f"> *Summary: {chunk.summary}*")
            lines.append("")
        lines.append(f"```{lang}")
        lines.append(chunk.content)
        lines.append("```")
        lines.append("")
    return lines


def _format_index_metadata(file_record: FileRecord) -> list[str]:
    """Format the Index Metadata section."""
    lines: list[str] = []
    lines.append("## Index Metadata")
    lines.append("")
    truncated_hash = file_record.content_hash[:12] + "..." if len(file_record.content_hash) > 12 else file_record.content_hash
    lines.append(f"- **File hash:** `{truncated_hash}`")
    lines.append(f"- **Last indexed:** {file_record.last_indexed}")
    lines.append(f"- **Chunks:** {file_record.chunk_count}")
    lines.append(f"- **Language:** {file_record.language.value}")
    lines.append("")
    return lines


def format_compact_output(
    file_path: str,
    file_record: FileRecord,
    chunks: list[Chunk],
    relationships: dict,
    verbose: bool = False,
    query_config: Optional[QueryConfig] = None,
) -> str:
    """Generate compact layered markdown for a queried file.

    Args:
        file_path: Relative path from repo root.
        file_record: File metadata from the index.
        chunks: Extracted chunks for this file.
        relationships: Dict keyed by chunk_id with 'outgoing'/'incoming' lists.
        verbose: If True, include full code bodies (overridden by query_config).
        query_config: Optional query configuration.

    Returns:
        Complete markdown string.
    """
    if query_config is None:
        query_config = QueryConfig(verbose=verbose)

    lines: list[str] = []

    # File heading with metadata
    try:
        dt = datetime.fromisoformat(file_record.last_indexed)
        human_time = dt.strftime("%Y-%m-%d %H:%M UTC")
    except (ValueError, TypeError):
        human_time = file_record.last_indexed

    lines.append(f"# {file_path}")
    lines.append(f"*Last indexed: {human_time} | {file_record.chunk_count} chunks | "
                 f"Language: {file_record.language.value}*")
    lines.append("")

    # Index Metadata section (always shown, even in summary_only)
    lines.extend(_format_index_metadata(file_record))

    # Summary section
    lines.append("## Summary")
    lines.append("")
    summary_lines = _format_summary(chunks)
    if summary_lines:
        lines.extend(summary_lines)
    else:
        lines.append("*(no top-level chunks found)*")
    lines.append("")

    # Signatures section (skip if summary_only)
    if not query_config.summary_only:
        lines.append("## Signatures")
        lines.append("")
        for chunk in chunks:
            if chunk.parent_id is not None:
                continue  # Only top-level chunks in signatures
            chunk_rels = relationships.get(chunk.id, {"outgoing": [], "incoming": []})
            sig_lines = _format_signature_block(chunk, chunk_rels, query_config=query_config)
            lines.extend(sig_lines)
            lines.append("")

    # Verbose: full code section
    if query_config.verbose:
        lines.extend(_format_verbose_code(chunks, file_path))

    return "\n".join(lines)


def format_json_output(
    file_path: str,
    file_record: FileRecord,
    chunks: list[Chunk],
    relationships: list[dict],
    verbose: bool = False,
) -> str:
    """Generate JSON output for programmatic consumption.

    Args:
        file_path: Relative path from repo root.
        file_record: File metadata from the index.
        chunks: Extracted chunks for this file.
        relationships: Flat list of relationship dicts (from traverse_relationships or get_file_relationships).
        verbose: If True, include chunk content.

    Returns:
        JSON string.
    """
    result = {
        "file": file_path,
        "metadata": {
            "language": file_record.language.value,
            "last_indexed": file_record.last_indexed,
            "chunk_count": file_record.chunk_count,
            "content_hash": file_record.content_hash,
        },
        "chunks": [
            {
                "name": chunk.name,
                "type": chunk.chunk_type.value,
                "start_line": chunk.start_line,
                "end_line": chunk.end_line,
                "docstring": chunk.attached_comments[0] if chunk.attached_comments else None,
                "summary": chunk.summary,
                "content": chunk.content if verbose else None,
            }
            for chunk in chunks
        ],
        "relationships": {
            "outgoing": [r for r in relationships if r.get("direction") != "incoming"],
            "incoming": [r for r in relationships if r.get("direction") == "incoming"],
        },
    }
    return json.dumps(result, indent=2)
