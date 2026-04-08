"""Comment attachment to code chunks via AST post-processing.

Two strategies:
1. Python docstrings: first statement in function/class body that is a string literal.
2. C/Python standalone comments: preceding comment nodes that are within 2 lines of the chunk.
"""

from pathlib import Path
from typing import Optional

from tree_sitter import Node

from glma.models import Chunk, ChunkType, Language
from glma.index.parser import PARSER_CONFIGS, get_root_node


# Comment node types per language
COMMENT_TYPES = {
    Language.C: {"comment"},
    Language.PYTHON: {"comment"},
}


def _extract_python_docstring(node: Node) -> Optional[str]:
    """Extract docstring from a Python function_definition or class_definition node.

    A docstring is the first expression_statement in the body whose child is a string.
    """
    body = node.child_by_field_name("body")
    if body is None or not body.children:
        return None

    first_child = body.children[0]
    if first_child.type == "expression_statement" and first_child.children:
        inner = first_child.children[0]
        if inner.type == "string":
            text = inner.text.decode("utf-8")
            # Strip triple-quote delimiters
            for quote in ('"""', "'''"):
                if text.startswith(quote) and text.endswith(quote):
                    text = text[len(quote):-len(quote)]
                    break
            return text.strip()

    return None


def _collect_comments(root: Node, language: Language) -> list[tuple[int, int, str]]:
    """Collect all comment nodes from the AST.

    Returns:
        List of (start_line, end_line, comment_text) tuples. Lines are 1-indexed.
    """
    comment_types = COMMENT_TYPES.get(language, set())
    comments: list[tuple[int, int, str]] = []

    def _walk(node: Node) -> None:
        if node.type in comment_types:
            start = node.start_point[0] + 1
            end = node.end_point[0] + 1
            text = node.text.decode("utf-8")
            comments.append((start, end, text))
        for child in node.children:
            _walk(child)

    _walk(root)
    return sorted(comments, key=lambda c: c[0])


def _find_docstrings_for_chunks(
    node: Node,
    chunks: list[Chunk],
    config,
) -> None:
    """Walk AST and extract docstrings, attaching them to matching chunks."""
    chunk_type_str = config.chunk_types.get(node.type)
    if chunk_type_str:
        start_line = node.start_point[0] + 1
        # Find matching chunk by start_line and type
        for chunk in chunks:
            if (chunk.start_line == start_line
                and chunk.chunk_type in (ChunkType.FUNCTION, ChunkType.CLASS, ChunkType.METHOD)):
                docstring = _extract_python_docstring(node)
                if docstring:
                    chunk.attached_comments = [docstring]
                break
    # Always recurse into all children to find nested docstrings
    for child in node.children:
        _find_docstrings_for_chunks(child, chunks, config)


def attach_comments(
    chunks: list[Chunk],
    filepath: Path,
    language: Language,
    repo_root: Path,
) -> list[Chunk]:
    """Attach comments to their associated code chunks.

    Strategy:
    1. For Python: extract docstrings from function/class bodies.
    2. For all languages: find preceding comments within 2 lines of each chunk's start.

    Args:
        chunks: List of already-extracted chunks.
        filepath: Path to the source file.
        language: Programming language.
        repo_root: Repo root path.

    Returns:
        The same chunks with attached_comments populated.
    """
    if not chunks:
        return chunks

    config = PARSER_CONFIGS.get(language)
    if config is None:
        return chunks

    # Extract Python docstrings
    if language == Language.PYTHON:
        root = get_root_node(filepath, language)
        if root is not None:
            _find_docstrings_for_chunks(root, chunks, config)

    # Collect standalone comments and attach by proximity
    root = get_root_node(filepath, language)
    if root is not None:
        comments = _collect_comments(root, language)

        for comment_start, comment_end, comment_text in comments:
            # Find the nearest chunk starting within 2 lines after the comment
            best_chunk: Optional[Chunk] = None
            best_distance = float("inf")

            for chunk in chunks:
                # Comment must be BEFORE the chunk (comment_end < chunk.start_line)
                if comment_end > chunk.start_line:
                    continue

                gap = chunk.start_line - comment_end
                if gap <= 2 and gap < best_distance:
                    best_distance = gap
                    best_chunk = chunk

            if best_chunk is not None:
                # Only add if not already captured as docstring
                if comment_text not in best_chunk.attached_comments:
                    best_chunk.attached_comments.append(comment_text)

    return chunks
