"""Relationship extraction from tree-sitter ASTs.

Extracts structural relationships (calls, imports/includes, inheritance) from
parsed ASTs and resolves them against chunks stored in the database.
"""

from pathlib import Path
from typing import Optional

from tree_sitter import Node

from glma.models import Chunk, Language, Relationship, RelType, Confidence
from glma.index.parser import PARSER_CONFIGS, get_root_node
from glma.db.ladybug_store import LadybugStore


def _find_enclosing_chunk(node: Node, chunks: list[Chunk]) -> Optional[Chunk]:
    """Walk up the node's parent chain to find the nearest enclosing chunk.

    Matches by start_line (1-indexed) to find the corresponding Chunk object.
    Returns None if no enclosing chunk found (module-level code).
    """
    current = node.parent
    while current is not None:
        start_line = current.start_point[0] + 1
        for chunk in chunks:
            if chunk.start_line == start_line:
                return chunk
        current = current.parent
    return None


def _extract_c_calls(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract C function call relationships from an AST.

    Walks AST looking for call_expression nodes. For each one, extracts the
    callee name and resolves it against source_chunks.
    """
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "call_expression":
            # First child is the callee
            callee = n.child_by_field_name("function")
            if callee is None and len(n.children) > 0:
                callee = n.children[0]

            if callee is not None and callee.type == "identifier":
                callee_name = callee.text.decode("utf-8")
                source_line = n.start_point[0] + 1

                # Find enclosing function chunk
                enclosing = _find_enclosing_chunk(n, source_chunks)
                if enclosing is None:
                    # Module-level call — skip or use first chunk
                    _walk_children(n)
                    return

                # Look up callee in source chunks
                target_chunk = None
                for chunk in source_chunks:
                    if chunk.name == callee_name:
                        target_chunk = chunk
                        break

                if target_chunk is not None:
                    relationships.append(Relationship(
                        source_id=enclosing.id,
                        target_id=target_chunk.id,
                        target_name=callee_name,
                        rel_type=RelType.CALLS,
                        confidence=Confidence.DIRECT,
                        source_line=source_line,
                    ))
                else:
                    relationships.append(Relationship(
                        source_id=enclosing.id,
                        target_id="",
                        target_name=callee_name,
                        rel_type=RelType.CALLS,
                        confidence=Confidence.INFERRED,
                        source_line=source_line,
                    ))

        _walk_children(n)

    def _walk_children(n: Node) -> None:
        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_c_includes(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
    indexed_files: dict[str, str],
) -> list[Relationship]:
    """Extract C #include relationships from an AST.

    Handles both local includes ("myheader.h") and system includes (<stdio.h>).
    """
    relationships: list[Relationship] = []
    source_id = source_chunks[0].id if source_chunks else ""

    def _walk(n: Node) -> None:
        if n.type == "preproc_include":
            source_line = n.start_point[0] + 1

            # Check for string_literal (local include) or system_lib_string (system header)
            for child in n.children:
                if child.type == "string_literal":
                    # Local include like "utils.h"
                    # Get the string_content child
                    content_child = child.child_by_field_name("content")
                    if content_child is None:
                        # Fallback: decode and strip quotes
                        text = child.text.decode("utf-8")
                        include_path = text.strip('"')
                    else:
                        include_path = content_child.text.decode("utf-8")

                    # Resolve against indexed files
                    resolved = False
                    for idx_path in indexed_files:
                        if idx_path.endswith(include_path):
                            relationships.append(Relationship(
                                source_id=source_id,
                                target_id="",  # Will be resolved later if needed
                                target_name=include_path,
                                rel_type=RelType.INCLUDES,
                                confidence=Confidence.DIRECT,
                                source_line=source_line,
                            ))
                            resolved = True
                            break

                    if not resolved:
                        relationships.append(Relationship(
                            source_id=source_id,
                            target_id="",
                            target_name=include_path,
                            rel_type=RelType.INCLUDES,
                            confidence=Confidence.INFERRED,
                            source_line=source_line,
                        ))

                elif child.type == "system_lib_string":
                    # System header like <stdio.h>
                    text = child.text.decode("utf-8")
                    include_name = text.strip("<>")
                    relationships.append(Relationship(
                        source_id=source_id,
                        target_id="",
                        target_name=include_name,
                        rel_type=RelType.INCLUDES,
                        confidence=Confidence.INFERRED,
                        source_line=source_line,
                    ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def extract_c_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Extract all relationships from a C source file.

    Args:
        filepath: Absolute path to the C source file.
        language: Must be Language.C.
        repo_root: Absolute path to repository root.
        source_chunks: Chunks extracted from this file.
        store: LadybugStore for resolving cross-file references.

    Returns:
        List of Relationship objects.
    """
    root = get_root_node(filepath, language)
    if root is None:
        return []

    indexed_files = store.get_indexed_files()

    calls = _extract_c_calls(root, source_chunks, str(filepath.relative_to(repo_root)))
    includes = _extract_c_includes(root, source_chunks, str(filepath.relative_to(repo_root)), indexed_files)

    return calls + includes


def extract_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Dispatcher: extract relationships based on language.

    Args:
        filepath: Absolute path to the source file.
        language: Programming language.
        repo_root: Absolute path to repository root.
        source_chunks: Chunks extracted from this file.
        store: LadybugStore for resolving cross-file references.

    Returns:
        List of Relationship objects. Empty list for unsupported languages.
    """
    if language == Language.C:
        return extract_c_relationships(filepath, language, repo_root, source_chunks, store)

    # Python handled in Plan 02-02
    return []
