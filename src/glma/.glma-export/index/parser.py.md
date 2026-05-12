---
file_path: index/parser.py
language: python
last_indexed: 2026-04-13T20:15:23.580863+00:00
chunk_count: 4
content_hash: 730fc4fbd4be3b5819047c63b93799df8d2de0195a6e39bffbd2a1558c245d6a
---

# index/parser.py

## Summary

Provides a framework for parsing source files into Tree-sitter ASTs using language-specific configuration schemas. It maps AST node types to extractable code chunks, enabling the identification of functions, classes, and dependencies across multiple supported languages.

**AI Chunk Summaries:**
- **LanguageConfig**: Defines a configuration schema for language-specific parsing, mapping tree-sitter node types to extractable chunks and container nodes. It specifies the required AST node types used to identify function calls, imports, and inheritance relationships.
- **_build_parsers**: Initializes a mapping of supported languages to their respective `LanguageConfig` objects. It defines language-specific Tree-sitter configurations, including node type mappings for functions, classes, calls, and imports.
- **parse_file**: Parses a source file into a tree-sitter `Tree` using a language-specific configuration. It reads the file bytes from the provided path and returns the resulting parse tree or `None` if the language is unsupported or the file is inaccessible.
- **get_root_node**: Parses a source file based on the provided language and returns its root AST node. It returns `None` if the parsing process fails.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| LanguageConfig | class | L16-L29 |  |
| _build_parsers | function | L32-L61 |  |
| parse_file | function | L67-L87 |  |
| get_root_node | function | L90-L103 |  |

## Chunks

### LanguageConfig (class, L16-L29)

> *Summary: Defines a configuration schema for language-specific parsing, mapping tree-sitter node types to extractable chunks and container nodes. It specifies the required AST node types used to identify function calls, imports, and inheritance relationships.*

> **Calls:** ? (glma.models) (INFERRED), ? (tree_sitter) (INFERRED), ? (tree_sitter) (INFERRED), ? (tree_sitter) (INFERRED), ? (tree_sitter) (INFERRED), ? (tree_sitter_python) (INFERRED), ? (tree_sitter_c) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (dataclasses) (INFERRED)

### _build_parsers (function, L32-L61)

> *Summary: Initializes a mapping of supported languages to their respective `LanguageConfig` objects. It defines language-specific Tree-sitter configurations, including node type mappings for functions, classes, calls, and imports.*

> **Calls:** LanguageConfig (DIRECT), LanguageConfig (DIRECT), ? (language) (INFERRED), ? (Language) (INFERRED), ? (language) (INFERRED), ? (Language) (INFERRED)

### parse_file (function, L67-L87)

> *Summary: Parses a source file into a tree-sitter `Tree` using a language-specific configuration. It reads the file bytes from the provided path and returns the resulting parse tree or `None` if the language is unsupported or the file is inaccessible.*

> **Calls:** ? (parser.parse) (INFERRED), ? (Parser) (INFERRED), ? (filepath.read_bytes) (INFERRED), ? (PARSER_CONFIGS.get) (INFERRED)

### get_root_node (function, L90-L103)

> *Summary: Parses a source file based on the provided language and returns its root AST node. It returns `None` if the parsing process fails.*

> **Calls:** parse_file (DIRECT)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| _build_parsers | LanguageConfig | DIRECT | L49 |
| _build_parsers | LanguageConfig | DIRECT | L35 |
| _build_parsers | ? (language) | INFERRED | L51 |
| _build_parsers | ? (Language) | INFERRED | L51 |
| _build_parsers | ? (language) | INFERRED | L37 |
| _build_parsers | ? (Language) | INFERRED | L37 |
| get_root_node | parse_file | DIRECT | L100 |
| parse_file | ? (parser.parse) | INFERRED | L87 |
| parse_file | ? (Parser) | INFERRED | L86 |
| parse_file | ? (filepath.read_bytes) | INFERRED | L82 |
| parse_file | ? (PARSER_CONFIGS.get) | INFERRED | L77 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| tree_sitter | INFERRED |
| tree_sitter | INFERRED |
| tree_sitter | INFERRED |
| tree_sitter | INFERRED |
| tree_sitter_python | INFERRED |
| tree_sitter_c | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| dataclasses | INFERRED |
