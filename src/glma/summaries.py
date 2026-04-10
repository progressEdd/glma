"""Shared summary generation for file-level summaries."""

from glma.models import Chunk, ChunkType


def generate_rule_summary(
    file_path: str,
    chunks: list[Chunk],
    relationships: list[dict],
) -> str:
    """Generate deterministic file summary from chunk + relationship data.

    No LLM needed. Lists top-level exports and imports.

    Args:
        file_path: Relative file path.
        chunks: All chunks for the file.
        relationships: All relationships for the file.

    Returns:
        Human-readable summary string.
    """
    functions = [c for c in chunks if c.chunk_type == ChunkType.FUNCTION]
    classes = [c for c in chunks if c.chunk_type == ChunkType.CLASS]
    methods = [c for c in chunks if c.chunk_type == ChunkType.METHOD]

    parts: list[str] = []

    if functions:
        names = ", ".join(f.name for f in functions[:10])
        suffix = f" and {len(functions) - 10} more" if len(functions) > 10 else ""
        parts.append(f"{len(functions)} function(s): {names}{suffix}")

    if classes:
        names = ", ".join(c.name for c in classes)
        parts.append(f"{len(classes)} class(es): {names}")

    if methods:
        parts.append(f"{len(methods)} method(s)")

    # Extract unique import/include targets
    imports = sorted({r.get("target_name", "") for r in relationships if r.get("rel_type") == "imports" and r.get("target_name")})
    includes = sorted({r.get("target_name", "") for r in relationships if r.get("rel_type") == "includes" and r.get("target_name")})

    if imports:
        imp_str = ", ".join(imports[:15])
        suffix = f" and {len(imports) - 15} more" if len(imports) > 15 else ""
        parts.append(f"Imports: {imp_str}{suffix}")

    if includes:
        inc_str = ", ".join(includes[:15])
        parts.append(f"Includes: {inc_str}")

    return ". ".join(parts) + "." if parts else f"File with {len(chunks)} chunk(s)."
