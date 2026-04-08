"""Tree-sitter parsing pipeline for C and Python source files."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import tree_sitter_c as tsc
import tree_sitter_python as tspython
from tree_sitter import Language as TSLanguage
from tree_sitter import Node, Parser, Tree

from glma.models import Language


@dataclass
class LanguageConfig:
    """Configuration for parsing a specific language."""
    language: Language
    ts_language: TSLanguage
    # Node types that represent extractable chunks
    chunk_types: dict[str, str]  # tree-sitter node type → ChunkType value

    # Node types whose children should be checked for nested chunks
    container_types: set[str]


def _build_parsers() -> dict[Language, LanguageConfig]:
    """Build parser configurations for all supported languages."""
    return {
        Language.C: LanguageConfig(
            language=Language.C,
            ts_language=TSLanguage(tsc.language()),
            chunk_types={
                "function_definition": "function",
                "struct_specifier": "class",   # closest C equivalent
                "enum_specifier": "class",     # closest C equivalent
                "type_definition": "class",    # typedef
            },
            container_types={"translation_unit"},
        ),
        Language.PYTHON: LanguageConfig(
            language=Language.PYTHON,
            ts_language=TSLanguage(tspython.language()),
            chunk_types={
                "function_definition": "function",
                "class_definition": "class",
            },
            container_types={"module", "class_definition"},
        ),
    }


PARSER_CONFIGS = _build_parsers()


def parse_file(filepath: Path, language: Language) -> Optional[Tree]:
    """Parse a source file with tree-sitter.

    Args:
        filepath: Path to the source file.
        language: Programming language to parse as.

    Returns:
        Tree-sitter Tree, or None if file cannot be read.
    """
    config = PARSER_CONFIGS.get(language)
    if config is None:
        return None

    try:
        source = filepath.read_bytes()
    except (OSError, IOError):
        return None

    parser = Parser(config.ts_language)
    return parser.parse(source)


def get_root_node(filepath: Path, language: Language) -> Optional[Node]:
    """Parse a file and return the root AST node.

    Args:
        filepath: Path to the source file.
        language: Programming language.

    Returns:
        Root node, or None on parse failure.
    """
    tree = parse_file(filepath, language)
    if tree is None:
        return None
    return tree.root_node
