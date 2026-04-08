"""Markdown output writer for indexed files.

Produces per-file markdown in layered summary format:
  # filename
  (file summary — empty in Phase 1)
  ## Key Exports
  (table: name, type, description)
  ## Chunks
  ### chunk_name (type, Lstart-Lend)
  (chunk content in code block)
"""

from pathlib import Path

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


def format_file_markdown(file_path: str, chunks: list[Chunk]) -> str:
    """Generate layered summary markdown for an indexed file.

    Args:
        file_path: Relative path from repo root.
        chunks: List of extracted chunks for this file.

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
        lines.append("")

    return "\n".join(lines)


def write_markdown(
    chunks: list[Chunk],
    repo_root: Path,
    output_dir: str,
) -> Path:
    """Write markdown file for a single indexed file.

    Creates the output directory structure mirroring the source file path.

    Args:
        chunks: All chunks for this file (must share same file_path).
        repo_root: Absolute path to repo root.
        output_dir: Output directory name (relative to repo root).

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

    content = format_file_markdown(file_path, chunks)
    md_path.write_text(content, encoding="utf-8")

    return md_path
