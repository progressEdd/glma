---
file_path: index/relationships.py
language: python
last_indexed: 2026-04-13T20:15:23.907786+00:00
chunk_count: 9
content_hash: 9fe0e995ff4c5af69fb36c341e8ce66fd15ed81730fe405fad889c739c4d0a92
---

# index/relationships.py

## Summary

Extracts structural dependencies—such as function calls, imports, and class inheritance—from C and Python source files using AST traversal. It maps these connections into `Relationship` objects with associated confidence levels based on whether the targets are resolved within the indexed store.

**AI Chunk Summaries:**
- **_find_enclosing_chunk**: Traverses a node's parent hierarchy to locate the nearest `Chunk` that shares the same starting line. It takes a `Node` and a list of `Chunk` objects, returning the matching `Chunk` or `None` if no match is found.
- **_extract_c_calls**: Traverses a C AST to identify function call expressions and map them as `Relationship` objects between source and target chunks. It outputs a list of calls, assigning a direct confidence level if the callee is found in the provided `source_chunks` or an inferred level otherwise.
- **_extract_c_includes**: Parses an AST node to identify C `#include` directives and returns a list of `Relationship` objects. It resolves include paths against a dictionary of indexed files to assign either `DIRECT` or `INFERRED` confidence levels based on whether the target file is known.
- **extract_c_relationships**: Extracts function calls and include directives from a C source file using its AST root and provided source chunks. It returns a combined list of `Relationship` objects derived from these call and include dependencies.
- **_extract_python_calls**: Traverses an AST to identify function call relationships by resolving callees using an import map and store. It returns a list of `Relationship` objects linking the enclosing function to the target function with associated confidence levels.
- **_extract_python_imports**: Parses a syntax tree to identify Python import statements and resolve them into `Relationship` objects. It attempts to map imported modules to existing files in the `LadybugStore`, assigning a direct confidence level if found or an inferred level otherwise.
- **_extract_python_inheritance**: Parses a Tree-sitter AST node to identify Python class inheritance and returns a list of `Relationship` objects. It resolves base classes by searching local source chunks first, then querying the global store for cross-file references, falling back to inferred relationships if no target ID is found.
- **extract_python_relationships**: Parses a Python source file to identify and extract call, import, and inheritance relationships. It utilizes a root AST node and an import map to return a combined list of `Relationship` objects based on the provided file path and source chunks.
- **extract_relationships**: Acts as a dispatcher that routes the extraction of code relationships to language-specific handlers (C or Python). It takes file metadata and source chunks as input and returns a list of identified `Relationship` objects.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| _find_enclosing_chunk | function | L21-L34 |  |
| _extract_c_calls | function | L37-L92 |  |
| _extract_c_includes | function | L95-L158 |  |
| extract_c_relationships | function | L161-L178 |  |
| _extract_python_calls | function | L181-L231 |  |
| _extract_python_imports | function | L234-L293 |  |
| _extract_python_inheritance | function | L296-L394 |  |
| extract_python_relationships | function | L397-L416 |  |
| extract_relationships | function | L419-L432 |  |

## Chunks

### _find_enclosing_chunk (function, L21-L34)

> *Summary: Traverses a node's parent hierarchy to locate the nearest `Chunk` that shares the same starting line. It takes a `Node` and a list of `Chunk` objects, returning the matching `Chunk` or `None` if no match is found.*

> **Calls:** ? (glma.db.ladybug_store) (INFERRED), ? (glma.index.resolver) (INFERRED), ? (glma.index.resolver) (INFERRED), ? (glma.index.resolver) (INFERRED), ? (glma.index.resolver) (INFERRED), ? (glma.index.resolver) (INFERRED), ? (glma.index.parser) (INFERRED), ? (glma.index.parser) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (tree_sitter) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED)

### _extract_c_calls (function, L37-L92)

> *Summary: Traverses a C AST to identify function call expressions and map them as `Relationship` objects between source and target chunks. It outputs a list of calls, assigning a direct confidence level if the callee is found in the provided `source_chunks` or an inferred level otherwise.*

> **Calls:** _find_enclosing_chunk (DIRECT), ? (_walk) (INFERRED), ? (_walk) (INFERRED), ? (_walk_children) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (_walk_children) (INFERRED), ? (callee.text.decode) (INFERRED), ? (len) (INFERRED), ? (n.child_by_field_name) (INFERRED)

### _extract_c_includes (function, L95-L158)

> *Summary: Parses an AST node to identify C `#include` directives and returns a list of `Relationship` objects. It resolves include paths against a dictionary of indexed files to assign either `DIRECT` or `INFERRED` confidence levels based on whether the target file is known.*

> **Calls:** ? (_walk) (INFERRED), ? (_walk) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (text.strip) (INFERRED), ? (child.text.decode) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (idx_path.endswith) (INFERRED), ? (content_child.text.decode) (INFERRED), ? (text.strip) (INFERRED), ? (child.text.decode) (INFERRED), ? (child.child_by_field_name) (INFERRED)

### extract_c_relationships (function, L161-L178)

> *Summary: Extracts function calls and include directives from a C source file using its AST root and provided source chunks. It returns a combined list of `Relationship` objects derived from these call and include dependencies.*

> **Calls:** _extract_c_calls (DIRECT), _extract_c_includes (DIRECT), ? (filepath.relative_to) (INFERRED), ? (str) (INFERRED), ? (filepath.relative_to) (INFERRED), ? (str) (INFERRED), ? (store.get_indexed_files) (INFERRED), ? (get_root_node) (INFERRED)

### _extract_python_calls (function, L181-L231)

> *Summary: Traverses an AST to identify function call relationships by resolving callees using an import map and store. It returns a list of `Relationship` objects linking the enclosing function to the target function with associated confidence levels.*

> **Calls:** ? (_walk) (INFERRED), ? (_walk) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (callee.child_by_field_name) (INFERRED), ? (callee.child_by_field_name("object").text.decode) (INFERRED), ? (callee.child_by_field_name) (INFERRED), ? (resolve_callee) (INFERRED), ? (find_enclosing_class) (INFERRED), ? (_walk) (INFERRED), ? (find_enclosing_function) (INFERRED)

### _extract_python_imports (function, L234-L293)

> *Summary: Parses a syntax tree to identify Python import statements and resolve them into `Relationship` objects. It attempts to map imported modules to existing files in the `LadybugStore`, assigning a direct confidence level if found or an inferred level otherwise.*

> **Calls:** ? (_walk) (INFERRED), ? (_walk) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (list) (INFERRED), ? (store.conn.execute) (INFERRED), ? (info.source_module.replace) (INFERRED), ? (local_imports.items) (INFERRED), ? (build_import_map) (INFERRED)

### _extract_python_inheritance (function, L296-L394)

> *Summary: Parses a Tree-sitter AST node to identify Python class inheritance and returns a list of `Relationship` objects. It resolves base classes by searching local source chunks first, then querying the global store for cross-file references, falling back to inferred relationships if no target ID is found.*

> **Calls:** ? (_walk) (INFERRED), ? (_walk) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (arg.text.decode) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (list) (INFERRED), ? (store.conn.execute) (INFERRED), ? (Relationship) (INFERRED), ? (relationships.append) (INFERRED), ? (arg.text.decode) (INFERRED), ? (_walk) (INFERRED), ? (class_name_node.text.decode) (INFERRED), ? (_walk) (INFERRED), ? (n.child_by_field_name) (INFERRED)

### extract_python_relationships (function, L397-L416)

> *Summary: Parses a Python source file to identify and extract call, import, and inheritance relationships. It utilizes a root AST node and an import map to return a combined list of `Relationship` objects based on the provided file path and source chunks.*

> **Calls:** _extract_python_calls (DIRECT), _extract_python_imports (DIRECT), _extract_python_inheritance (DIRECT), ? (build_import_map) (INFERRED), ? (filepath.relative_to) (INFERRED), ? (str) (INFERRED), ? (get_root_node) (INFERRED)

### extract_relationships (function, L419-L432)

> *Summary: Acts as a dispatcher that routes the extraction of code relationships to language-specific handlers (C or Python). It takes file metadata and source chunks as input and returns a list of identified `Relationship` objects.*

> **Calls:** extract_c_relationships (DIRECT), extract_python_relationships (DIRECT)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| _extract_c_calls | _find_enclosing_chunk | DIRECT | L55 |
| extract_c_relationships | _extract_c_calls | DIRECT | L175 |
| _extract_c_calls | ? (_walk) | INFERRED | L91 |
| _extract_c_calls | ? (_walk) | INFERRED | L89 |
| _extract_c_calls | ? (_walk_children) | INFERRED | L85 |
| _extract_c_calls | ? (Relationship) | INFERRED | L76 |
| _extract_c_calls | ? (relationships.append) | INFERRED | L76 |
| _extract_c_calls | ? (Relationship) | INFERRED | L67 |
| _extract_c_calls | ? (relationships.append) | INFERRED | L67 |
| _extract_c_calls | ? (_walk_children) | INFERRED | L57 |
| _extract_c_calls | ? (callee.text.decode) | INFERRED | L52 |
| _extract_c_calls | ? (len) | INFERRED | L48 |
| _extract_c_calls | ? (n.child_by_field_name) | INFERRED | L47 |
| extract_c_relationships | _extract_c_includes | DIRECT | L176 |
| _extract_c_includes | ? (_walk) | INFERRED | L157 |
| _extract_c_includes | ? (_walk) | INFERRED | L155 |
| _extract_c_includes | ? (Relationship) | INFERRED | L145 |
| _extract_c_includes | ? (relationships.append) | INFERRED | L145 |
| _extract_c_includes | ? (text.strip) | INFERRED | L144 |
| _extract_c_includes | ? (child.text.decode) | INFERRED | L143 |
| _extract_c_includes | ? (Relationship) | INFERRED | L133 |
| _extract_c_includes | ? (relationships.append) | INFERRED | L133 |
| _extract_c_includes | ? (Relationship) | INFERRED | L121 |
| _extract_c_includes | ? (relationships.append) | INFERRED | L121 |
| _extract_c_includes | ? (idx_path.endswith) | INFERRED | L120 |
| _extract_c_includes | ? (content_child.text.decode) | INFERRED | L116 |
| _extract_c_includes | ? (text.strip) | INFERRED | L114 |
| _extract_c_includes | ? (child.text.decode) | INFERRED | L113 |
| _extract_c_includes | ? (child.child_by_field_name) | INFERRED | L111 |
| extract_relationships | extract_c_relationships | DIRECT | L428 |
| extract_c_relationships | ? (filepath.relative_to) | INFERRED | L176 |
| extract_c_relationships | ? (str) | INFERRED | L176 |
| extract_c_relationships | ? (filepath.relative_to) | INFERRED | L175 |
| extract_c_relationships | ? (str) | INFERRED | L175 |
| extract_c_relationships | ? (store.get_indexed_files) | INFERRED | L173 |
| extract_c_relationships | ? (get_root_node) | INFERRED | L169 |
| extract_python_relationships | _extract_python_calls | DIRECT | L412 |
| _extract_python_calls | ? (_walk) | INFERRED | L230 |
| _extract_python_calls | ? (_walk) | INFERRED | L228 |
| _extract_python_calls | ? (Relationship) | INFERRED | L218 |
| _extract_python_calls | ? (relationships.append) | INFERRED | L218 |
| _extract_python_calls | ? (callee.child_by_field_name) | INFERRED | L213 |
| _extract_python_calls | ? (callee.child_by_field_name("object").text.decode) | INFERRED | L213 |
| _extract_python_calls | ? (callee.child_by_field_name) | INFERRED | L212 |
| _extract_python_calls | ? (resolve_callee) | INFERRED | L205 |
| _extract_python_calls | ? (find_enclosing_class) | INFERRED | L203 |
| _extract_python_calls | ? (_walk) | INFERRED | L200 |
| _extract_python_calls | ? (find_enclosing_function) | INFERRED | L197 |
| extract_python_relationships | _extract_python_imports | DIRECT | L413 |
| _extract_python_imports | ? (_walk) | INFERRED | L292 |
| _extract_python_imports | ? (_walk) | INFERRED | L290 |
| _extract_python_imports | ? (Relationship) | INFERRED | L280 |
| _extract_python_imports | ? (relationships.append) | INFERRED | L280 |
| _extract_python_imports | ? (Relationship) | INFERRED | L266 |
| _extract_python_imports | ? (relationships.append) | INFERRED | L266 |
| _extract_python_imports | ? (list) | INFERRED | L264 |
| _extract_python_imports | ? (store.conn.execute) | INFERRED | L260 |
| _extract_python_imports | ? (info.source_module.replace) | INFERRED | L251 |
| _extract_python_imports | ? (local_imports.items) | INFERRED | L250 |
| _extract_python_imports | ? (build_import_map) | INFERRED | L248 |
| extract_python_relationships | _extract_python_inheritance | DIRECT | L414 |
| _extract_python_inheritance | ? (_walk) | INFERRED | L393 |
| _extract_python_inheritance | ? (_walk) | INFERRED | L391 |
| _extract_python_inheritance | ? (Relationship) | INFERRED | L381 |
| _extract_python_inheritance | ? (relationships.append) | INFERRED | L381 |
| _extract_python_inheritance | ? (arg.text.decode) | INFERRED | L380 |
| _extract_python_inheritance | ? (Relationship) | INFERRED | L370 |
| _extract_python_inheritance | ? (relationships.append) | INFERRED | L370 |
| _extract_python_inheritance | ? (Relationship) | INFERRED | L357 |
| _extract_python_inheritance | ? (relationships.append) | INFERRED | L357 |
| _extract_python_inheritance | ? (list) | INFERRED | L355 |
| _extract_python_inheritance | ? (store.conn.execute) | INFERRED | L351 |
| _extract_python_inheritance | ? (Relationship) | INFERRED | L339 |
| _extract_python_inheritance | ? (relationships.append) | INFERRED | L339 |
| _extract_python_inheritance | ? (arg.text.decode) | INFERRED | L329 |
| _extract_python_inheritance | ? (_walk) | INFERRED | L322 |
| _extract_python_inheritance | ? (class_name_node.text.decode) | INFERRED | L313 |
| _extract_python_inheritance | ? (_walk) | INFERRED | L310 |
| _extract_python_inheritance | ? (n.child_by_field_name) | INFERRED | L307 |
| extract_relationships | extract_python_relationships | DIRECT | L430 |
| extract_python_relationships | ? (build_import_map) | INFERRED | L410 |
| extract_python_relationships | ? (filepath.relative_to) | INFERRED | L409 |
| extract_python_relationships | ? (str) | INFERRED | L409 |
| extract_python_relationships | ? (get_root_node) | INFERRED | L405 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.db.ladybug_store | INFERRED |
| glma.index.resolver | INFERRED |
| glma.index.resolver | INFERRED |
| glma.index.resolver | INFERRED |
| glma.index.resolver | INFERRED |
| glma.index.resolver | INFERRED |
| glma.index.parser | INFERRED |
| glma.index.parser | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| tree_sitter | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
