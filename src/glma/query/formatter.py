"""Compact layered markdown formatter for query output.

Generates a quick-reference view of an indexed file:
  # filepath
  *Last indexed: ... | N chunks | Language: python*
  ## Summary
  (chunk names + types)
  ## Signatures
  ### chunk_name (type, Lstart-Lend)
  (docstring if present)
    → calls: func1, func2
    → called by: caller1
  ## Full Code  (only with --verbose)
"""

from datetime import datetime
from typing import Optional

from glma.models import Chunk, ChunkType, FileRecord


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


def _format_signature_block(chunk: Chunk, chunk_rels: dict) -> list[str]:
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

    # Relationship hints
    outgoing = chunk_rels.get("outgoing", [])
    incoming = chunk_rels.get("incoming", [])

    # Group outgoing by rel_type
    outgoing_by_type: dict[str, list[str]] = {}
    for rel in outgoing:
        rt = rel.get("rel_type", "unknown")
        if rt not in outgoing_by_type:
            outgoing_by_type[rt] = []
        # Determine target display name
        if rel.get("source_id") == rel.get("target_id") and rel.get("source_id"):
            # Self-referential (unresolved)
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
        lines.append(f"```{lang}")
        lines.append(chunk.content)
        lines.append("```")
        lines.append("")
    return lines


def format_compact_output(
    file_path: str,
    file_record: FileRecord,
    chunks: list[Chunk],
    relationships: dict,
    verbose: bool = False,
) -> str:
    """Generate compact layered markdown for a queried file.

    Args:
        file_path: Relative path from repo root.
        file_record: File metadata from the index.
        chunks: Extracted chunks for this file.
        relationships: Dict keyed by chunk_id with 'outgoing'/'incoming' lists.
        verbose: If True, include full code bodies.

    Returns:
        Complete markdown string.
    """
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

    # Summary section
    lines.append("## Summary")
    lines.append("")
    summary_lines = _format_summary(chunks)
    if summary_lines:
        lines.extend(summary_lines)
    else:
        lines.append("*(no top-level chunks found)*")
    lines.append("")

    # Signatures section
    lines.append("## Signatures")
    lines.append("")
    for chunk in chunks:
        if chunk.parent_id is not None:
            continue  # Only top-level chunks in signatures
        chunk_rels = relationships.get(chunk.id, {"outgoing": [], "incoming": []})
        sig_lines = _format_signature_block(chunk, chunk_rels)
        lines.extend(sig_lines)
        lines.append("")

    # Verbose: full code section
    if verbose:
        lines.extend(_format_verbose_code(chunks, file_path))

    return "\n".join(lines)
