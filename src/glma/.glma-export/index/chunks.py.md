---
file_path: index/chunks.py
language: python
last_indexed: 2026-04-13T20:15:23.612989+00:00
chunk_count: 5
content_hash: 4c82f757b97d16f01ef30913feffe346e9202d7d4882f6417935dd10ed8632a5
---

# index/chunks.py

## Summary

Parses source files into semantic code chunks by traversing AST nodes based on language-specific configurations. It generates unique identifiers and content hashes for each extracted segment, supporting nested structures like methods within classes.

**AI Chunk Summaries:**
- **_content_hash**: Generates a 32-byte BLAKE2b hexadecimal hash from a UTF-8 encoded input string. It takes a string as input and returns its corresponding content hash.
- **_chunk_id**: Generates a unique identifier string by concatenating the file path, chunk type, name, and starting line number using double-colon delimiters.
- **_extract_node_name**: Extracts a human-readable identifier from an AST node based on the specified language, targeting function or class names. It returns the decoded name string if found via field lookups (Python/C), otherwise falling back to a truncated version of the node's first line.
- **_walk_chunks**: Recursively traverses AST nodes to extract code segments as `Chunk` objects based on language-specific configurations. It maps node types to chunk categories and handles Python-specific logic to nest methods within class definitions via `parent_id`.
- **extract_chunks**: Parses a source file into a list of semantic `Chunk` objects using a language-specific parser configuration. It validates the file's root node and computes a relative path before recursively walking the AST to extract code segments.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| _content_hash | function | L13-L15 |  |
| _chunk_id | function | L18-L20 |  |
| _extract_node_name | function | L23-L56 |  |
| _walk_chunks | function | L59-L124 |  |
| extract_chunks | function | L127-L155 |  |

## Chunks

### _content_hash (function, L13-L15)

> *Summary: Generates a 32-byte BLAKE2b hexadecimal hash from a UTF-8 encoded input string. It takes a string as input and returns its corresponding content hash.*

> **Calls:** ? (glma.index.parser) (INFERRED), ? (glma.index.parser) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (tree_sitter) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (hashlib) (INFERRED), ? (content.encode) (INFERRED), ? (blake2b) (INFERRED), ? (hashlib.blake2b(content.encode("utf-8"), digest_size=32).hexdigest) (INFERRED)

### _chunk_id (function, L18-L20)

> *Summary: Generates a unique identifier string by concatenating the file path, chunk type, name, and starting line number using double-colon delimiters.*


### _extract_node_name (function, L23-L56)

> *Summary: Extracts a human-readable identifier from an AST node based on the specified language, targeting function or class names. It returns the decoded name string if found via field lookups (Python/C), otherwise falling back to a truncated version of the node's first line.*

> **Calls:** ? (text.split) (INFERRED), ? (text.split("\n")[0].strip) (INFERRED), ? (node.text.decode) (INFERRED), ? (name_node.text.decode) (INFERRED), ? (node.child_by_field_name) (INFERRED), ? (child.text.decode) (INFERRED), ? (name_node.text.decode) (INFERRED), ? (declarator.child_by_field_name) (INFERRED), ? (node.child_by_field_name) (INFERRED), ? (name_node.text.decode) (INFERRED), ? (node.child_by_field_name) (INFERRED)

### _walk_chunks (function, L59-L124)

> *Summary: Recursively traverses AST nodes to extract code segments as `Chunk` objects based on language-specific configurations. It maps node types to chunk categories and handles Python-specific logic to nest methods within class definitions via `parent_id`.*

> **Calls:** _content_hash (DIRECT), _chunk_id (DIRECT), _extract_node_name (DIRECT), ? (_walk_chunks) (DIRECT), ? (chunks.extend) (INFERRED), ? (_walk_chunks) (DIRECT), ? (chunks.extend) (INFERRED), ? (chunks.append) (INFERRED), ? (Chunk) (INFERRED), ? (ChunkType) (INFERRED), ? (child.text.decode) (INFERRED), ? (config.chunk_types.get) (INFERRED), ? (get) (INFERRED)

### extract_chunks (function, L127-L155)

> *Summary: Parses a source file into a list of semantic `Chunk` objects using a language-specific parser configuration. It validates the file's root node and computes a relative path before recursively walking the AST to extract code segments.*

> **Calls:** _walk_chunks (DIRECT), ? (get) (INFERRED), ? (filepath.relative_to) (INFERRED), ? (str) (INFERRED), ? (filepath.read_bytes) (INFERRED), ? (get_root_node) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| _walk_chunks | _content_hash | DIRECT | L106 |
| _content_hash | ? (content.encode) | INFERRED | L15 |
| _content_hash | ? (blake2b) | INFERRED | L15 |
| _content_hash | ? (hashlib.blake2b(content.encode("utf-8"), digest_size=32).hexdigest) | INFERRED | L15 |
| _walk_chunks | _chunk_id | DIRECT | L88 |
| _walk_chunks | _extract_node_name | DIRECT | L85 |
| _extract_node_name | ? (text.split) | INFERRED | L55 |
| _extract_node_name | ? (text.split("\n")[0].strip) | INFERRED | L55 |
| _extract_node_name | ? (node.text.decode) | INFERRED | L54 |
| _extract_node_name | ? (name_node.text.decode) | INFERRED | L51 |
| _extract_node_name | ? (node.child_by_field_name) | INFERRED | L49 |
| _extract_node_name | ? (child.text.decode) | INFERRED | L47 |
| _extract_node_name | ? (name_node.text.decode) | INFERRED | L43 |
| _extract_node_name | ? (declarator.child_by_field_name) | INFERRED | L41 |
| _extract_node_name | ? (node.child_by_field_name) | INFERRED | L37 |
| _extract_node_name | ? (name_node.text.decode) | INFERRED | L33 |
| _extract_node_name | ? (node.child_by_field_name) | INFERRED | L31 |
| extract_chunks | _walk_chunks | DIRECT | L153 |
| _walk_chunks | ? (_walk_chunks) | DIRECT | L120 |
| _walk_chunks | ? (chunks.extend) | INFERRED | L120 |
| _walk_chunks | ? (_walk_chunks) | DIRECT | L113 |
| _walk_chunks | ? (chunks.extend) | INFERRED | L113 |
| _walk_chunks | ? (chunks.append) | INFERRED | L109 |
| _walk_chunks | ? (Chunk) | INFERRED | L97 |
| _walk_chunks | ? (ChunkType) | INFERRED | L87 |
| _walk_chunks | ? (child.text.decode) | INFERRED | L82 |
| _walk_chunks | ? (config.chunk_types.get) | INFERRED | L78 |
| _walk_chunks | ? (get) | INFERRED | L71 |
| extract_chunks | ? (get) | INFERRED | L149 |
| extract_chunks | ? (filepath.relative_to) | INFERRED | L147 |
| extract_chunks | ? (str) | INFERRED | L147 |
| extract_chunks | ? (filepath.read_bytes) | INFERRED | L146 |
| extract_chunks | ? (get_root_node) | INFERRED | L138 |

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
| hashlib | INFERRED |
