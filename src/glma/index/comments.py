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
    Language.CPP: {"comment"},
    Language.TYPESCRIPT: {"comment"},
    Language.TSX: {"comment"},
    Language.RUST: {"line_comment"},
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


def _extract_doc_comment(node: Node, language: Language) -> Optional[str]:
    """Extract doc comment from a comment node.

    Handles:
    - TypeScript JSDoc: /** ... */
    - Rust outer doc: /// ...
    - Rust inner doc: //! ...
    """
    if node.type != "comment" and node.type != "line_comment":
        return None

    text = node.text.decode("utf-8")

    if language in (Language.TYPESCRIPT, Language.TSX):
        # JSDoc: starts with /**
        if text.startswith("/**"):
            content = text
            if content.endswith("*/"):
                content = content[:-2]
            if content.startswith("/**"):
                content = content[3:]
            elif content.startswith("/*"):
                content = content[2:]
            return content.strip(" \n\t*")

    elif language == Language.RUST:
        # Outer doc: starts with ///
        if text.startswith("///"):
            content = text[3:]
            return content.strip()
        # Inner doc: starts with //!
        if text.startswith("//!"):
            content = text[3:]
            return content.strip()

    return None


def _attach_doc_comments(
    comments: list[tuple[int, int, str, Node]],
    chunks: list[Chunk],
    language: Language,
) -> None:
    """Attach doc comments (JSDoc, Rust ///) to the following chunk."""
    for comment_start, comment_end, comment_text, comment_node in comments:
        doc_text = _extract_doc_comment(comment_node, language)
        if doc_text is None:
            continue

        best_chunk: Optional[Chunk] = None
        best_distance = float("inf")

        for chunk in chunks:
            if comment_end >= chunk.start_line:
                continue
            gap = chunk.start_line - comment_end
            if gap <= 2 and gap < best_distance:
                best_distance = gap
                best_chunk = chunk

        if best_chunk is not None:
            best_chunk.attached_comments.append(doc_text)


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

    # Extract doc comments for TypeScript/TSX/Rust
    if language in (Language.TYPESCRIPT, Language.TSX, Language.RUST):
        root = get_root_node(filepath, language)
        if root is not None:
            comment_types = COMMENT_TYPES.get(language, set())
            doc_comments: list[tuple[int, int, str, Node]] = []

            def _collect_doc_comments(n: Node) -> None:
                types = COMMENT_TYPES.get(language, set())
                if n.type in types:
                    text = n.text.decode("utf-8")
                    is_doc = False
                    if language in (Language.TYPESCRIPT, Language.TSX) and text.startswith("/**"):
                        is_doc = True
                    elif language == Language.RUST and text.startswith("///"):
                        is_doc = True
                    if is_doc:
                        start = n.start_point[0] + 1
                        end = n.end_point[0] + 1
                        doc_comments.append((start, end, text, n))
                for child in n.children:
                    _collect_doc_comments(child)

            _collect_doc_comments(root)
            _attach_doc_comments(doc_comments, chunks, language)

        # Handle Rust inner doc comments (//!) — attach to first chunk
        if language == Language.RUST:
            root = get_root_node(filepath, language)
            if root is not None:
                comment_types = COMMENT_TYPES.get(language, set())
                inner_docs: list[str] = []
                for child in root.children:
                    if child.type in comment_types:
                        text = child.text.decode("utf-8")
                        if text.startswith("//!"):
                            content = text[3:].strip()
                            inner_docs.append(content)
                if inner_docs and chunks:
                    first_top = None
                    for c in chunks:
                        if c.parent_id is None:
                            first_top = c
                            break
                    if first_top is None:
                        first_top = chunks[0]
                    for doc in inner_docs:
                        if doc not in first_top.attached_comments:
                            first_top.attached_comments.append(doc)

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
