---
file_path: index/resolver.py
language: python
last_indexed: 2026-04-13T20:15:23.856982+00:00
chunk_count: 7
content_hash: 785cb4b455ee7bb59dfe7bdf3bd7fd7b7a722aee0741dbfe86e6f8fdbbd0ec9c
---

# index/resolver.py

## Summary

Analyzes Python ASTs to resolve function calls and import statements to specific code chunks within a `LadybugStore`. It maps local identifiers and module paths to their source definitions by tracking imports and traversing class/function scopes.

**AI Chunk Summaries:**
- **ImportInfo**: Defines a data structure to track import metadata, mapping a local alias or name to its source module and specific imported member. It stores the `local_name`, `source_module` path, and an optional `imported_name`.
- **build_import_map**: Traverses a root AST node to extract all Python import statements and their aliases. It returns a dictionary mapping local identifiers to `ImportInfo` objects containing the source module and original imported name.
- **find_enclosing_class**: Traverses up the AST parent chain from a given node to locate the nearest `class_definition`. Returns the decoded string of the class's identifier if found, otherwise returns `None`.
- **find_enclosing_function**: Traverses the AST parent chain from a given node to identify the ID of the enclosing function or method. It matches the first encountered `function_definition` node against a list of file chunks based on the starting line number.
- **resolve_callee**: Resolves a call expression's callee node to a target chunk ID and display name by analyzing identifiers and attributes. It searches through the import map, current file chunks, and class memberships (e.g., `self` methods) to determine the destination of the function call.
- **_resolve_imported_name**: Resolves a `from X import Y` statement to a specific chunk ID by querying the `LadybugStore` for the imported name within potential `.py` or `__init__.py` file paths. It returns a tuple containing the discovered chunk ID (or an empty string if not found) and the original imported name.
- **_resolve_module**: Maps a Python module path and optional attribute name to a specific chunk ID by querying the `LadybugStore` database. It checks for both `.py` and `__init__.py` file paths, returning a tuple of the resolved chunk ID and the original identifier.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| ImportInfo | class | L18-L22 |  |
| build_import_map | function | L25-L126 |  |
| find_enclosing_class | function | L129-L146 |  |
| find_enclosing_function | function | L149-L167 |  |
| resolve_callee | function | L170-L256 |  |
| _resolve_imported_name | function | L259-L281 |  |
| _resolve_module | function | L284-L317 |  |

## Chunks

### ImportInfo (class, L18-L22)

> *Summary: Defines a data structure to track import metadata, mapping a local alias or name to its source module and specific imported member. It stores the `local_name`, `source_module` path, and an optional `imported_name`.*

> **Calls:** ? (glma.db.ladybug_store) (INFERRED), ? (glma.models) (INFERRED), ? (tree_sitter) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (dataclasses) (INFERRED)

### build_import_map (function, L25-L126)

> *Summary: Traverses a root AST node to extract all Python import statements and their aliases. It returns a dictionary mapping local identifiers to `ImportInfo` objects containing the source module and original imported name.*

> **Calls:** ImportInfo (DIRECT), ImportInfo (DIRECT), ImportInfo (DIRECT), ? (_walk) (INFERRED), ? (imported_names.append) (INFERRED), ? (child.text.decode) (INFERRED), ? (child.text.decode) (INFERRED), ? (child.text.decode) (INFERRED), ? (imported_names.append) (INFERRED), ? (imported_names.append) (INFERRED), ? (alias_node.text.decode) (INFERRED), ? (name_node.text.decode) (INFERRED), ? (child.child_by_field_name) (INFERRED), ? (child.child_by_field_name) (INFERRED), ? (child.text.decode) (INFERRED), ? (module_path.split) (INFERRED), ? (child.text.decode) (INFERRED), ? (alias_node.text.decode) (INFERRED), ? (dotted_name_node.text.decode) (INFERRED), ? (child.child_by_field_name) (INFERRED), ? (child.child_by_field_name) (INFERRED), ? (_walk) (INFERRED), ? (_handle_import_from_statement) (INFERRED), ? (_handle_import_statement) (INFERRED)

### find_enclosing_class (function, L129-L146)

> *Summary: Traverses up the AST parent chain from a given node to locate the nearest `class_definition`. Returns the decoded string of the class's identifier if found, otherwise returns `None`.*

> **Calls:** ? (child.text.decode) (INFERRED)

### find_enclosing_function (function, L149-L167)

> *Summary: Traverses the AST parent chain from a given node to identify the ID of the enclosing function or method. It matches the first encountered `function_definition` node against a list of file chunks based on the starting line number.*


### resolve_callee (function, L170-L256)

> *Summary: Resolves a call expression's callee node to a target chunk ID and display name by analyzing identifiers and attributes. It searches through the import map, current file chunks, and class memberships (e.g., `self` methods) to determine the destination of the function call.*

> **Calls:** ? (callee_node.text.decode) (INFERRED), ? (len) (INFERRED), ? (chunk.parent_id.split) (INFERRED), ? (attr_node.text.decode) (INFERRED), ? (obj_node.text.decode) (INFERRED), ? (callee_node.text.decode) (INFERRED), ? (callee_node.child_by_field_name) (INFERRED), ? (callee_node.child_by_field_name) (INFERRED), ? (import_info.source_module.replace) (INFERRED), ? (callee_node.text.decode) (INFERRED), _resolve_imported_name (DIRECT), _resolve_module (DIRECT), _resolve_module (DIRECT)

### _resolve_imported_name (function, L259-L281)

> *Summary: Resolves a `from X import Y` statement to a specific chunk ID by querying the `LadybugStore` for the imported name within potential `.py` or `__init__.py` file paths. It returns a tuple containing the discovered chunk ID (or an empty string if not found) and the original imported name.*

> **Calls:** ? (list) (INFERRED), ? (store.conn.execute) (INFERRED), ? (import_info.source_module.replace) (INFERRED)

### _resolve_module (function, L284-L317)

> *Summary: Maps a Python module path and optional attribute name to a specific chunk ID by querying the `LadybugStore` database. It checks for both `.py` and `__init__.py` file paths, returning a tuple of the resolved chunk ID and the original identifier.*

> **Calls:** ? (list) (INFERRED), ? (store.conn.execute) (INFERRED), ? (list) (INFERRED), ? (store.conn.execute) (INFERRED), ? (module.replace) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| build_import_map | ImportInfo | DIRECT | L119 |
| build_import_map | ImportInfo | DIRECT | L73 |
| build_import_map | ImportInfo | DIRECT | L63 |
| build_import_map | ? (_walk) | INFERRED | L125 |
| build_import_map | ? (imported_names.append) | INFERRED | L107 |
| build_import_map | ? (child.text.decode) | INFERRED | L106 |
| build_import_map | ? (child.text.decode) | INFERRED | L103 |
| build_import_map | ? (child.text.decode) | INFERRED | L103 |
| build_import_map | ? (imported_names.append) | INFERRED | L103 |
| build_import_map | ? (imported_names.append) | INFERRED | L101 |
| build_import_map | ? (alias_node.text.decode) | INFERRED | L100 |
| build_import_map | ? (name_node.text.decode) | INFERRED | L99 |
| build_import_map | ? (child.child_by_field_name) | INFERRED | L97 |
| build_import_map | ? (child.child_by_field_name) | INFERRED | L96 |
| build_import_map | ? (child.text.decode) | INFERRED | L92 |
| build_import_map | ? (module_path.split) | INFERRED | L72 |
| build_import_map | ? (child.text.decode) | INFERRED | L70 |
| build_import_map | ? (alias_node.text.decode) | INFERRED | L62 |
| build_import_map | ? (dotted_name_node.text.decode) | INFERRED | L61 |
| build_import_map | ? (child.child_by_field_name) | INFERRED | L58 |
| build_import_map | ? (child.child_by_field_name) | INFERRED | L57 |
| build_import_map | ? (_walk) | INFERRED | L50 |
| build_import_map | ? (_handle_import_from_statement) | INFERRED | L47 |
| build_import_map | ? (_handle_import_statement) | INFERRED | L45 |
| find_enclosing_class | ? (child.text.decode) | INFERRED | L144 |
| resolve_callee | ? (callee_node.text.decode) | INFERRED | L256 |
| resolve_callee | ? (len) | INFERRED | L241 |
| resolve_callee | ? (chunk.parent_id.split) | INFERRED | L240 |
| resolve_callee | ? (attr_node.text.decode) | INFERRED | L223 |
| resolve_callee | ? (obj_node.text.decode) | INFERRED | L222 |
| resolve_callee | ? (callee_node.text.decode) | INFERRED | L220 |
| resolve_callee | ? (callee_node.child_by_field_name) | INFERRED | L217 |
| resolve_callee | ? (callee_node.child_by_field_name) | INFERRED | L216 |
| resolve_callee | ? (import_info.source_module.replace) | INFERRED | L198 |
| resolve_callee | ? (callee_node.text.decode) | INFERRED | L192 |
| _resolve_imported_name | ? (list) | INFERRED | L274 |
| _resolve_imported_name | ? (store.conn.execute) | INFERRED | L270 |
| _resolve_imported_name | ? (import_info.source_module.replace) | INFERRED | L261 |
| resolve_callee | _resolve_imported_name | DIRECT | L201 |
| _resolve_module | ? (list) | INFERRED | L312 |
| _resolve_module | ? (store.conn.execute) | INFERRED | L308 |
| _resolve_module | ? (list) | INFERRED | L299 |
| _resolve_module | ? (store.conn.execute) | INFERRED | L295 |
| _resolve_module | ? (module.replace) | INFERRED | L286 |
| resolve_callee | _resolve_module | DIRECT | L249 |
| resolve_callee | _resolve_module | DIRECT | L204 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.db.ladybug_store | INFERRED |
| glma.models | INFERRED |
| tree_sitter | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| dataclasses | INFERRED |
