"""Tree-sitter parsing pipeline for C and Python source files."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import tree_sitter_c as tsc
import tree_sitter_cpp as tscpp
import tree_sitter_typescript as tsts
import tree_sitter_rust as tsrust
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

    # NEW: Node types relevant to relationship extraction
    call_node_type: str  # The AST node type for function calls
    import_node_type: str  # The AST node type for imports/includes
    inherit_node_type: str  # The AST node type for inheritance/base classes


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
            call_node_type="call_expression",
            import_node_type="preproc_include",
            inherit_node_type="",  # C has no class inheritance
        ),
        Language.PYTHON: LanguageConfig(
            language=Language.PYTHON,
            ts_language=TSLanguage(tspython.language()),
            chunk_types={
                "function_definition": "function",
                "class_definition": "class",
            },
            container_types={"module", "class_definition"},
            call_node_type="call",
            import_node_type="import_statement",
            inherit_node_type="class_definition",
        ),
        Language.CPP: LanguageConfig(
            language=Language.CPP,
            ts_language=TSLanguage(tscpp.language()),
            chunk_types={
                "function_definition": "function",
                "class_specifier": "class",
                "struct_specifier": "class",
                "enum_specifier": "class",
                "type_definition": "class",
                "namespace_definition": "class",
                "template_declaration": "function",
                "constructor_definition": "function",
                "destructor_definition": "function",
            },
            container_types={"translation_unit", "namespace_definition", "class_specifier"},
            call_node_type="call_expression",
            import_node_type="preproc_include",
            inherit_node_type="class_specifier",
        ),
        Language.TYPESCRIPT: LanguageConfig(
            language=Language.TYPESCRIPT,
            ts_language=TSLanguage(tsts.language_typescript()),
            chunk_types={
                "function_declaration": "function",
                "class_declaration": "class",
                "interface_declaration": "class",
                "type_alias_declaration": "class",
                "enum_declaration": "class",
                "method_definition": "method",
                "arrow_function": "function",
                "lexical_declaration": "function",
            },
            container_types={"program", "class_declaration", "module"},
            call_node_type="call_expression",
            import_node_type="import_statement",
            inherit_node_type="class_declaration",
        ),
        Language.TSX: LanguageConfig(
            language=Language.TSX,
            ts_language=TSLanguage(tsts.language_tsx()),
            chunk_types={
                "function_declaration": "function",
                "class_declaration": "class",
                "interface_declaration": "class",
                "type_alias_declaration": "class",
                "enum_declaration": "class",
                "method_definition": "method",
                "arrow_function": "function",
                "lexical_declaration": "function",
            },
            container_types={"program", "class_declaration", "module"},
            call_node_type="call_expression",
            import_node_type="import_statement",
            inherit_node_type="class_declaration",
        ),
        Language.RUST: LanguageConfig(
            language=Language.RUST,
            ts_language=TSLanguage(tsrust.language()),
            chunk_types={
                "function_item": "function",
                "struct_item": "class",
                "enum_item": "class",
                "trait_item": "class",
                "type_item": "class",
                "impl_item": "class",
                "function_signature_item": "function",
            },
            container_types={"source_file", "impl_item", "trait_item"},
            call_node_type="call_expression",
            import_node_type="use_declaration",
            inherit_node_type="impl_item",
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
