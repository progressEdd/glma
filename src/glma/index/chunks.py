"""Semantic chunk extraction from tree-sitter ASTs."""

import hashlib
from pathlib import Path
from typing import Optional

from tree_sitter import Node

from glma.models import Chunk, ChunkType, Language
from glma.index.parser import PARSER_CONFIGS, get_root_node


def _content_hash(content: str) -> str:
    """Compute BLAKE2b hash of content."""
    return hashlib.blake2b(content.encode("utf-8"), digest_size=32).hexdigest()


def _chunk_id(file_path: str, chunk_type: str, name: str, start_line: int) -> str:
    """Generate a unique chunk ID."""
    return f"{file_path}::{chunk_type}::{name}::{start_line}"


def _extract_node_name(node: Node, source_bytes: bytes, language: Language) -> str:
    """Extract the name of a chunk from its AST node.

    For functions: the name is in the 'name' field or declarator.
    For classes/structs: the name is in the 'name' field.
    """
    if language == Language.PYTHON:
        # Python: function_definition and class_definition have 'name' child
        name_node = node.child_by_field_name("name")
        if name_node:
            return name_node.text.decode("utf-8")

    elif language == Language.C:
        # C: function_definition has a declarator with the name
        declarator = node.child_by_field_name("declarator")
        if declarator:
            # The declarator could be a function_declarator, pointer_declarator, etc.
            # Drill down to find the identifier
            name_node = declarator.child_by_field_name("declarator")
            if name_node:
                return name_node.text.decode("utf-8")
            # Direct identifier
            for child in declarator.children:
                if child.type == "identifier":
                    return child.text.decode("utf-8")
        # struct/enum: name field
        name_node = node.child_by_field_name("name")
        if name_node:
            return name_node.text.decode("utf-8")

    # Fallback: first line of content, truncated
    text = node.text.decode("utf-8")
    first_line = text.split("\n")[0].strip()[:50]
    return first_line


def _walk_chunks(
    node: Node,
    source_bytes: bytes,
    file_path: str,
    language: Language,
    parent_id: Optional[str] = None,
) -> list[Chunk]:
    """Recursively walk AST nodes and extract chunks.

    For Python class_definition nodes, also extract methods as separate chunks
    with parent_id pointing to the class chunk.
    """
    config = PARSER_CONFIGS.get(language)
    if config is None:
        return []

    chunks: list[Chunk] = []

    for child in node.children:
        chunk_type_str = config.chunk_types.get(child.type)

        if chunk_type_str is not None:
            # This node is an extractable chunk
            content = child.text.decode("utf-8")
            start_line = child.start_point[0] + 1  # Convert 0-indexed to 1-indexed
            end_line = child.end_point[0] + 1
            name = _extract_node_name(child, source_bytes, language)

            chunk_type = ChunkType(chunk_type_str)
            cid = _chunk_id(file_path, chunk_type_str, name, start_line)

            # Determine chunk_type: if inside a class_definition and it's a function, it's a method
            actual_type = chunk_type
            if (language == Language.PYTHON
                and chunk_type == ChunkType.FUNCTION
                and parent_id is not None):
                actual_type = ChunkType.METHOD

            chunk = Chunk(
                id=cid,
                file_path=file_path,
                chunk_type=actual_type,
                name=name,
                content=content,
                summary=None,
                start_line=start_line,
                end_line=end_line,
                content_hash=_content_hash(content),
                parent_id=parent_id,
            )
            chunks.append(chunk)

            # For Python class_definition: recurse into it to find methods
            if language == Language.PYTHON and child.type == "class_definition":
                chunks.extend(_walk_chunks(
                    child, source_bytes, file_path, language, parent_id=cid,
                ))

        else:
            # Recurse into ALL children to find nested chunks
            # (handles block nodes inside class_definition, etc.)
            chunks.extend(_walk_chunks(
                child, source_bytes, file_path, language, parent_id,
            ))

    return chunks


def extract_chunks(filepath: Path, language: Language, repo_root: Path) -> list[Chunk]:
    """Extract all semantic chunks from a source file.

    Args:
        filepath: Absolute path to the source file.
        language: Programming language of the file.
        repo_root: Absolute path to repo root (for computing relative paths).

    Returns:
        List of Chunk objects extracted from the file.
    """
    root = get_root_node(filepath, language)
    if root is None:
        return []

    # Skip files where root node has ERROR type (malformed source)
    if root.has_error and root.type == "ERROR":
        return []

    source_bytes = filepath.read_bytes()
    relative_path = str(filepath.relative_to(repo_root))

    config = PARSER_CONFIGS.get(language)
    if config is None:
        return []

    chunks = _walk_chunks(root, source_bytes, relative_path, language)

    return chunks
