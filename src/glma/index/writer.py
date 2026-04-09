"""Markdown output writer for indexed files.

Produces per-file markdown in layered summary format:
  # filename
  (file summary — empty in Phase 1)
  ## Key Exports
  (table: name, type, description)
  ## Chunks
  ### chunk_name (type, Lstart-Lend)
  (chunk content in code block)
  > **Calls:** foo (DIRECT), bar (INFERRED → ?)
  ## Relationships
  ### Outgoing Calls / Imports / Inherits / Incoming
"""

from pathlib import Path
from typing import Optional

from glma.models import Chunk, ChunkType


def _chunk_display_type(chunk: Chunk) -> str:
    """Get display-friendly chunk type string."""
    type_map = {
        ChunkType.FUNCTION: "function",
        ChunkType.CLASS: "class",
        ChunkType.METHOD: "method",
        ChunkType.MODULE: "module",
    }
    return type_map.get(chunk.chunk_type, str(chunk.chunk_type))


def _format_chunk_heading(chunk: Chunk) -> str:
    """Format the markdown heading for a chunk."""
    type_str = _chunk_display_type(chunk)
    suffix = ""
    if chunk.parent_id:
        # Extract parent name from parent_id (format: path::type::name::line)
        parts = chunk.parent_id.split("::")
        if len(parts) >= 3:
            suffix = f", parent: {parts[2]}"

    return f"### {chunk.name} ({type_str}, L{chunk.start_line}-L{chunk.end_line}{suffix})"


def _get_lang_hint(file_path: str) -> str:
    """Get language hint for markdown code block."""
    if file_path.endswith(".py"):
        return "python"
    elif file_path.endswith(".c") or file_path.endswith(".h"):
        return "c"
    return ""


def _clean_description(comment: str) -> str:
    """Clean a comment for use as description in the exports table."""
    desc = comment.strip()
    # Strip Python docstring markers
    for quote in ('"""', "'''"):
        if desc.startswith(quote) and desc.endswith(quote):
            desc = desc[len(quote):-len(quote)]
            break
    # Strip # comment markers
    if desc.startswith("#"):
        desc = desc.lstrip("#").strip()
    # Strip C block comment markers
    elif desc.startswith("/*"):
        desc = desc.strip("/*").strip("*/").strip()
    return desc[:80]


def _resolve_target_display(rel: dict) -> str:
    """Format the target display for a relationship.

    Handles self-referential edges (source→source for unresolved targets)
    by checking if source_id == target_id.

    Args:
        rel: Relationship dict with target_name, target_name_resolved, confidence, target_id.

    Returns:
        Display string for the target.
    """
    # Self-referential edge = unresolved target stored as source→source
    if rel.get("source_id") == rel.get("target_id") and rel.get("source_id"):
        return f"? ({rel.get('target_name', 'unknown')})"

    if rel.get("target_name_resolved") and rel.get("target_id"):
        return rel["target_name_resolved"]
    if rel.get("confidence") == "INFERRED" and not rel.get("target_id"):
        return f"? ({rel.get('target_name', 'unknown')})"
    return rel.get("target_name", "unknown")


def _format_inline_relationships(chunk_id: str, relationships: list[dict]) -> list[str]:
    """Format inline relationship lines for a chunk.

    Args:
        chunk_id: The chunk ID to filter relationships for.
        relationships: All relationship dicts for the file.

    Returns:
        List of markdown lines starting with '> '.
    """
    if not relationships:
        return []

    lines: list[str] = []

    # Outgoing calls from this chunk
    outgoing = [r for r in relationships
                if r.get("source_id") == chunk_id
                and r.get("rel_type") in ("calls", "includes")]
    # Self-referential edges (source→source) represent unresolved targets
    if outgoing:
        parts = []
        for r in outgoing:
            target = _resolve_target_display(r)
            conf = r.get("confidence", "INFERRED")
            parts.append(f"{target} ({conf})")
        lines.append(f"> **Calls:** {', '.join(parts)}")

    # Incoming calls to this chunk (skip self-referential unresolved)
    incoming = [r for r in relationships
                if r.get("target_id") == chunk_id
                and r.get("source_id") != chunk_id
                and r.get("direction") == "incoming"]
    if incoming:
        parts = []
        for r in incoming:
            source = r.get("source_name", "unknown")
            conf = r.get("confidence", "INFERRED")
            parts.append(f"{source} ({conf})")
        lines.append(f"> **Called by:** {', '.join(parts)}")

    return lines


def _format_relationships_summary(file_path: str, relationships: list[dict], chunks: list[Chunk]) -> list[str]:
    """Format the relationships summary section.

    Args:
        file_path: File path (unused currently, for future context).
        relationships: All relationship dicts for the file.
        chunks: Chunks for the file (for resolving names).

    Returns:
        List of markdown lines for the relationships summary.
    """
    if not relationships:
        return []

    lines: list[str] = []
    chunk_ids = {c.id for c in chunks}

    # Group by rel_type
    by_type: dict[str, list[dict]] = {}
    for r in relationships:
        rt = r.get("rel_type", "unknown")
        if rt not in by_type:
            by_type[rt] = []
        by_type[rt].append(r)

    # Helper: get chunk name by id
    def _chunk_name(cid: str) -> str:
        for c in chunks:
            if c.id == cid:
                return c.name
        return cid.split("::")[2] if "::" in cid else cid

    # Outgoing calls
    if "calls" in by_type:
        out_calls = [r for r in by_type["calls"] if r.get("source_id") in chunk_ids]
        if out_calls:
            lines.append("### Outgoing Calls")
            lines.append("")
            lines.append("| From | To | Confidence | Line |")
            lines.append("| ---- | -- | ---------- | ---- |")
            for r in out_calls:
                from_name = r.get("source_name", _chunk_name(r.get("source_id", "")))
                to_name = _resolve_target_display(r)
                lines.append(f"| {from_name} | {to_name} | {r.get('confidence', '')} | L{r.get('source_line', '')} |")
            lines.append("")

    # Incoming calls (cross-file)
    incoming_calls = [r for r in relationships
                      if r.get("rel_type") == "calls"
                      and r.get("direction") == "incoming"
                      and r.get("target_id") in chunk_ids]
    if incoming_calls:
        lines.append("### Incoming Calls")
        lines.append("")
        lines.append("| From | To | Confidence |")
        lines.append("| ---- | -- | ---------- |")
        for r in incoming_calls:
            from_name = r.get("source_name", "unknown")
            to_name = _chunk_name(r.get("target_id", ""))
            lines.append(f"| {from_name} | {to_name} | {r.get('confidence', '')} |")
        lines.append("")

    # Includes (C)
    if "includes" in by_type:
        includes = [r for r in by_type["includes"] if r.get("source_id") in chunk_ids]
        if includes:
            lines.append("### Includes")
            lines.append("")
            lines.append("| Include | Confidence |")
            lines.append("| ------- | ---------- |")
            for r in includes:
                lines.append(f"| {r.get('target_name', '')} | {r.get('confidence', '')} |")
            lines.append("")

    # Imports (Python)
    if "imports" in by_type:
        imports = [r for r in by_type["imports"] if r.get("source_id") in chunk_ids]
        if imports:
            lines.append("### Imports")
            lines.append("")
            lines.append("| Import | Source | Confidence |")
            lines.append("| ------ | ------ | ---------- |")
            for r in imports:
                lines.append(f"| {r.get('target_name', '')} | {r.get('target_name', '')} | {r.get('confidence', '')} |")
            lines.append("")

    # Imported By (cross-file)
    incoming_imports = [r for r in relationships
                        if r.get("rel_type") == "imports"
                        and r.get("direction") == "incoming"]
    if incoming_imports:
        lines.append("### Imported By")
        lines.append("")
        lines.append("*(cross-file — populated when other files import this file's chunks)*")
        lines.append("")

    # Inherits
    if "inherits" in by_type:
        inherits = [r for r in by_type["inherits"] if r.get("source_id") in chunk_ids]
        if inherits:
            lines.append("### Inherits")
            lines.append("")
            lines.append("| Class | Base | Confidence |")
            lines.append("| ----- | ---- | ---------- |")
            for r in inherits:
                from_name = r.get("source_name", _chunk_name(r.get("source_id", "")))
                to_name = _resolve_target_display(r)
                lines.append(f"| {from_name} | {to_name} | {r.get('confidence', '')} |")
            lines.append("")

    return lines


def format_file_markdown(
    file_path: str,
    chunks: list[Chunk],
    relationships: Optional[list[dict]] = None,
) -> str:
    """Generate layered summary markdown for an indexed file.

    Args:
        file_path: Relative path from repo root.
        chunks: List of extracted chunks for this file.
        relationships: Optional list of relationship dicts for the file.

    Returns:
        Complete markdown string.
    """
    lines: list[str] = []

    # File heading
    lines.append(f"# {file_path}")
    lines.append("")

    # File summary (placeholder for Phase 3 LLM generation)
    lines.append("*(File summary not yet generated — available after Phase 3.)*")
    lines.append("")

    # Key Exports table
    lines.append("## Key Exports")
    lines.append("")
    lines.append("| Name | Type | Description |")
    lines.append("| ---- | ---- | ----------- |")

    # Top-level chunks only (no parent_id) for the exports table
    exports = [c for c in chunks if c.parent_id is None]
    if exports:
        for chunk in exports:
            desc = ""
            if chunk.attached_comments:
                desc = _clean_description(chunk.attached_comments[0])
            lines.append(f"| {chunk.name} | {_chunk_display_type(chunk)} | {desc} |")
    else:
        lines.append("| *(no exports found)* | | |")
    lines.append("")

    # Chunks section
    lines.append("## Chunks")
    lines.append("")

    for chunk in chunks:
        lines.append(_format_chunk_heading(chunk))
        lines.append("")

        # Show attached comments above the code block
        if chunk.attached_comments:
            for comment in chunk.attached_comments:
                lines.append(comment)
                lines.append("")

        # Code block
        lines.append("```" + _get_lang_hint(file_path))
        lines.append(chunk.content)
        lines.append("```")

        # Inline relationships
        if relationships:
            inline = _format_inline_relationships(chunk.id, relationships)
            if inline:
                lines.append("")
                lines.extend(inline)

        lines.append("")

    # Relationships summary section
    if relationships:
        summary = _format_relationships_summary(file_path, relationships, chunks)
        if summary:
            lines.append("## Relationships")
            lines.append("")
            lines.extend(summary)

    return "\n".join(lines)


def write_markdown(
    chunks: list[Chunk],
    repo_root: Path,
    output_dir: str,
    relationships: Optional[list[dict]] = None,
) -> Path:
    """Write markdown file for a single indexed file.

    Creates the output directory structure mirroring the source file path.

    Args:
        chunks: All chunks for this file (must share same file_path).
        repo_root: Absolute path to repo root.
        output_dir: Output directory name (relative to repo root).
        relationships: Optional list of relationship dicts.

    Returns:
        Path to the written markdown file.
    """
    if not chunks:
        raise ValueError("No chunks to write")

    file_path = chunks[0].file_path

    # Output path: .glma-index/markdown/<relative-path-with-extension>.md
    # Use full filename (including extension) to avoid collisions like sample.c vs sample.py
    md_dir = repo_root / output_dir / "markdown" / Path(file_path).parent
    md_dir.mkdir(parents=True, exist_ok=True)

    md_filename = Path(file_path).name + ".md"
    md_path = md_dir / md_filename

    content = format_file_markdown(file_path, chunks, relationships=relationships)
    md_path.write_text(content, encoding="utf-8")

    return md_path
