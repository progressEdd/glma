---
file_path: index/comments.py
language: python
last_indexed: 2026-04-13T20:15:23.650677+00:00
chunk_count: 4
content_hash: 91e89edcb258bb3d370f9d69ac9d08a81367fe2f9097a2b73f23c3785f6764dd
---

# index/comments.py

## Summary

Extracts and associates Python docstrings and source code comments with their corresponding code chunks using AST traversal. It processes raw files into structured data by matching comment line ranges to specific functions or classes based on proximity and node type.

**AI Chunk Summaries:**
- **_extract_python_docstring**: Extracts the docstring from a Python class or function node by identifying the first string expression in the body. It returns the decoded, stripped string content with triple-quote delimiters removed, or `None` if no docstring is present.
- **_collect_comments**: Recursively traverses an AST starting from a root node to extract all comment nodes based on the specified language's defined types. It returns a list of 1-indexed line ranges and decoded text, sorted by start line.
- **_find_docstrings_for_chunks**: Recursively traverses an AST to extract Python docstrings and attach them to corresponding `Chunk` objects based on line number and type. It matches nodes against a provided configuration and updates the `attached_comments` list of compatible function, class, or method chunks.
- **attach_comments**: Populates the `attached_comments` field of a list of code chunks by extracting Python docstrings and associating preceding comments based on line proximity (within 2 lines). It takes a list of chunks, file metadata, and language configuration to return the updated chunks.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| _extract_python_docstring | function | L24-L45 |  |
| _collect_comments | function | L48-L67 |  |
| _find_docstrings_for_chunks | function | L70-L89 |  |
| attach_comments | function | L92-L151 |  |

## Chunks

### _extract_python_docstring (function, L24-L45)

> *Summary: Extracts the docstring from a Python class or function node by identifying the first string expression in the body. It returns the decoded, stripped string content with triple-quote delimiters removed, or `None` if no docstring is present.*

> **Calls:** ? (glma.index.parser) (INFERRED), ? (glma.index.parser) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (tree_sitter) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (text.strip) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (text.endswith) (INFERRED), ? (text.startswith) (INFERRED), ? (inner.text.decode) (INFERRED), ? (node.child_by_field_name) (INFERRED)

### _collect_comments (function, L48-L67)

> *Summary: Recursively traverses an AST starting from a root node to extract all comment nodes based on the specified language's defined types. It returns a list of 1-indexed line ranges and decoded text, sorted by start line.*

> **Calls:** ? (sorted) (INFERRED), ? (_walk) (INFERRED), ? (_walk) (INFERRED), ? (comments.append) (INFERRED), ? (node.text.decode) (INFERRED), ? (set) (INFERRED), ? (COMMENT_TYPES.get) (INFERRED)

### _find_docstrings_for_chunks (function, L70-L89)

> *Summary: Recursively traverses an AST to extract Python docstrings and attach them to corresponding `Chunk` objects based on line number and type. It matches nodes against a provided configuration and updates the `attached_comments` list of compatible function, class, or method chunks.*

> **Calls:** _extract_python_docstring (DIRECT), ? (_find_docstrings_for_chunks) (DIRECT), ? (config.chunk_types.get) (INFERRED)

### attach_comments (function, L92-L151)

> *Summary: Populates the `attached_comments` field of a list of code chunks by extracting Python docstrings and associating preceding comments based on line proximity (within 2 lines). It takes a list of chunks, file metadata, and language configuration to return the updated chunks.*

> **Calls:** _collect_comments (DIRECT), _find_docstrings_for_chunks (DIRECT), ? (best_chunk.attached_comments.append) (INFERRED), ? (float) (INFERRED), ? (get_root_node) (INFERRED), ? (get_root_node) (INFERRED), ? (get) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| _find_docstrings_for_chunks | _extract_python_docstring | DIRECT | L83 |
| _extract_python_docstring | ? (text.strip) | INFERRED | L43 |
| _extract_python_docstring | ? (len) | INFERRED | L41 |
| _extract_python_docstring | ? (len) | INFERRED | L41 |
| _extract_python_docstring | ? (text.endswith) | INFERRED | L40 |
| _extract_python_docstring | ? (text.startswith) | INFERRED | L40 |
| _extract_python_docstring | ? (inner.text.decode) | INFERRED | L37 |
| _extract_python_docstring | ? (node.child_by_field_name) | INFERRED | L29 |
| attach_comments | _collect_comments | DIRECT | L129 |
| _collect_comments | ? (sorted) | INFERRED | L67 |
| _collect_comments | ? (_walk) | INFERRED | L66 |
| _collect_comments | ? (_walk) | INFERRED | L64 |
| _collect_comments | ? (comments.append) | INFERRED | L62 |
| _collect_comments | ? (node.text.decode) | INFERRED | L61 |
| _collect_comments | ? (set) | INFERRED | L54 |
| _collect_comments | ? (COMMENT_TYPES.get) | INFERRED | L54 |
| attach_comments | _find_docstrings_for_chunks | DIRECT | L124 |
| _find_docstrings_for_chunks | ? (_find_docstrings_for_chunks) | DIRECT | L89 |
| _find_docstrings_for_chunks | ? (config.chunk_types.get) | INFERRED | L76 |
| attach_comments | ? (best_chunk.attached_comments.append) | INFERRED | L149 |
| attach_comments | ? (float) | INFERRED | L134 |
| attach_comments | ? (get_root_node) | INFERRED | L127 |
| attach_comments | ? (get_root_node) | INFERRED | L122 |
| attach_comments | ? (get) | INFERRED | L116 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.index.parser | INFERRED |
| glma.index.parser | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| tree_sitter | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
