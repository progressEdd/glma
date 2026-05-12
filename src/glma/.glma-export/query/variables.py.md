---
file_path: query/variables.py
language: python
last_indexed: 2026-04-13T20:15:24.124666+00:00
chunk_count: 6
content_hash: 569d26f63451195ca357351be0ef7ebfd68840cb168eddfd725cfc602984ded0
---

# query/variables.py

## Summary

Analyzes notebook cell source code using AST parsing to identify variable definitions and references at the statement level. It aggregates this metadata into a flow dictionary that maps variables to their specific definition and usage locations across multiple cells.

**AI Chunk Summaries:**
- **StatementInfo**: Defines a data structure to track variable metadata for a single cell statement, including its line number and type. It maps which names are defined or referenced within that specific statement.
- **CellVariableInfo**: Stores metadata and analysis results for a single notebook cell, including its index, type, source code, and lists of identified statements, variable definitions, and references.
- **_extract_name_refs**: Recursively extracts all variable identifiers used in a `Load` context from an AST subtree. It returns a list of name strings while explicitly skipping nested function and class definitions to avoid capturing inner-scope references.
- **_extract_definition_names**: Recursively extracts variable identifiers from an AST assignment target node (supporting `Name`, `Tuple`, `List`, and `Starred` types). It returns a list of strings containing all identified variable names being stored.
- **extract_cell_variables**: Parses a cell's source code using the `ast` module to identify variable definitions and references for every statement. It returns a `CellVariableInfo` object containing per-statement analysis and aggregated lists of all defined and referenced variables.
- **build_variable_flow**: Maps variable definitions and references across multiple cells into a flow dictionary. It processes a list of `CellVariableInfo` objects to output a mapping of each variable name to its specific definition and usage locations (cell index and line number).

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| StatementInfo | class | L12-L17 |  |
| CellVariableInfo | class | L21-L28 |  |
| _extract_name_refs | function | L31-L45 |  |
| _extract_definition_names | function | L48-L59 |  |
| extract_cell_variables | function | L62-L193 |  |
| build_variable_flow | function | L196-L236 |  |

## Chunks

### StatementInfo (class, L12-L17)

> *Summary: Defines a data structure to track variable metadata for a single cell statement, including its line number and type. It maps which names are defined or referenced within that specific statement.*

> **Calls:** ? (dataclasses) (INFERRED), ? (dataclasses) (INFERRED), ? (ast) (INFERRED)

### CellVariableInfo (class, L21-L28)

> *Summary: Stores metadata and analysis results for a single notebook cell, including its index, type, source code, and lists of identified statements, variable definitions, and references.*


### _extract_name_refs (function, L31-L45)

> *Summary: Recursively extracts all variable identifiers used in a `Load` context from an AST subtree. It returns a list of name strings while explicitly skipping nested function and class definitions to avoid capturing inner-scope references.*

> **Calls:** ? (_extract_name_refs) (DIRECT), ? (names.extend) (INFERRED), ? (isinstance) (INFERRED), ? (iter_child_nodes) (INFERRED), ? (isinstance) (INFERRED), ? (isinstance) (INFERRED)

### _extract_definition_names (function, L48-L59)

> *Summary: Recursively extracts variable identifiers from an AST assignment target node (supporting `Name`, `Tuple`, `List`, and `Starred` types). It returns a list of strings containing all identified variable names being stored.*

> **Calls:** ? (_extract_definition_names) (DIRECT), ? (isinstance) (INFERRED), ? (_extract_definition_names) (DIRECT), ? (names.extend) (INFERRED), ? (isinstance) (INFERRED), ? (isinstance) (INFERRED), ? (isinstance) (INFERRED)

### extract_cell_variables (function, L62-L193)

> *Summary: Parses a cell's source code using the `ast` module to identify variable definitions and references for every statement. It returns a `CellVariableInfo` object containing per-statement analysis and aggregated lists of all defined and referenced variables.*

> **Calls:** StatementInfo (DIRECT), CellVariableInfo (DIRECT), CellVariableInfo (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_name_refs (DIRECT), _extract_definition_names (DIRECT), _extract_definition_names (DIRECT), _extract_definition_names (DIRECT), _extract_definition_names (DIRECT), ? (seen_ref.add) (INFERRED), ? (all_references.append) (INFERRED), ? (seen_def.add) (INFERRED), ? (all_defines.append) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED), ? (statements.append) (INFERRED), ? (isinstance) (INFERRED), ? (isinstance) (INFERRED), ? (defines.extend) (INFERRED), ? (references.extend) (INFERRED), ? (isinstance) (INFERRED), ? (isinstance) (INFERRED), ? (defines.append) (INFERRED), ? (isinstance) (INFERRED), ? (alias.name.split) (INFERRED), ? (defines.append) (INFERRED), ? (isinstance) (INFERRED), ? (references.extend) (INFERRED), ? (references.extend) (INFERRED), ? (references.extend) (INFERRED), ? (isinstance) (INFERRED), ? (refs.extend) (INFERRED), ? (refs.extend) (INFERRED), ? (refs.extend) (INFERRED), ? (refs.append) (INFERRED), ? (refs.append) (INFERRED), ? (refs.extend) (INFERRED), ? (refs.append) (INFERRED), ? (isinstance) (INFERRED), ? (isinstance) (INFERRED), ? (defines.extend) (INFERRED), ? (isinstance) (INFERRED), ? (parse) (INFERRED)

### build_variable_flow (function, L196-L236)

> *Summary: Maps variable definitions and references across multiple cells into a flow dictionary. It processes a list of `CellVariableInfo` objects to output a mapping of each variable name to its specific definition and usage locations (cell index and line number).*

> **Calls:** ? (used_vars.get) (INFERRED), ? (defined_vars.get) (INFERRED), ? (used_vars.keys) (INFERRED), ? (set) (INFERRED), ? (defined_vars.keys) (INFERRED), ? (set) (INFERRED), ? (used_vars[name].append) (INFERRED), ? (defined_vars[name].append) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| extract_cell_variables | StatementInfo | DIRECT | L164 |
| extract_cell_variables | CellVariableInfo | DIRECT | L186 |
| extract_cell_variables | CellVariableInfo | DIRECT | L75 |
| extract_cell_variables | _extract_name_refs | DIRECT | L162 |
| extract_cell_variables | _extract_name_refs | DIRECT | L158 |
| extract_cell_variables | _extract_name_refs | DIRECT | L151 |
| extract_cell_variables | _extract_name_refs | DIRECT | L146 |
| extract_cell_variables | _extract_name_refs | DIRECT | L131 |
| extract_cell_variables | _extract_name_refs | DIRECT | L129 |
| extract_cell_variables | _extract_name_refs | DIRECT | L127 |
| extract_cell_variables | _extract_name_refs | DIRECT | L119 |
| extract_cell_variables | _extract_name_refs | DIRECT | L117 |
| extract_cell_variables | _extract_name_refs | DIRECT | L115 |
| extract_cell_variables | _extract_name_refs | DIRECT | L108 |
| extract_cell_variables | _extract_name_refs | DIRECT | L98 |
| extract_cell_variables | _extract_name_refs | DIRECT | L92 |
| _extract_name_refs | ? (_extract_name_refs) | DIRECT | L44 |
| _extract_name_refs | ? (names.extend) | INFERRED | L44 |
| _extract_name_refs | ? (isinstance) | INFERRED | L41 |
| _extract_name_refs | ? (iter_child_nodes) | INFERRED | L40 |
| _extract_name_refs | ? (isinstance) | INFERRED | L37 |
| _extract_name_refs | ? (isinstance) | INFERRED | L37 |
| extract_cell_variables | _extract_definition_names | DIRECT | L153 |
| extract_cell_variables | _extract_definition_names | DIRECT | L145 |
| extract_cell_variables | _extract_definition_names | DIRECT | L96 |
| extract_cell_variables | _extract_definition_names | DIRECT | L91 |
| _extract_definition_names | ? (_extract_definition_names) | DIRECT | L58 |
| _extract_definition_names | ? (isinstance) | INFERRED | L57 |
| _extract_definition_names | ? (_extract_definition_names) | DIRECT | L55 |
| _extract_definition_names | ? (names.extend) | INFERRED | L55 |
| _extract_definition_names | ? (isinstance) | INFERRED | L52 |
| _extract_definition_names | ? (isinstance) | INFERRED | L50 |
| _extract_definition_names | ? (isinstance) | INFERRED | L50 |
| extract_cell_variables | ? (seen_ref.add) | INFERRED | L184 |
| extract_cell_variables | ? (all_references.append) | INFERRED | L183 |
| extract_cell_variables | ? (seen_def.add) | INFERRED | L180 |
| extract_cell_variables | ? (all_defines.append) | INFERRED | L179 |
| extract_cell_variables | ? (set) | INFERRED | L175 |
| extract_cell_variables | ? (set) | INFERRED | L174 |
| extract_cell_variables | ? (statements.append) | INFERRED | L164 |
| extract_cell_variables | ? (isinstance) | INFERRED | L160 |
| extract_cell_variables | ? (isinstance) | INFERRED | L155 |
| extract_cell_variables | ? (defines.extend) | INFERRED | L153 |
| extract_cell_variables | ? (references.extend) | INFERRED | L151 |
| extract_cell_variables | ? (isinstance) | INFERRED | L148 |
| extract_cell_variables | ? (isinstance) | INFERRED | L143 |
| extract_cell_variables | ? (defines.append) | INFERRED | L141 |
| extract_cell_variables | ? (isinstance) | INFERRED | L138 |
| extract_cell_variables | ? (alias.name.split) | INFERRED | L136 |
| extract_cell_variables | ? (defines.append) | INFERRED | L136 |
| extract_cell_variables | ? (isinstance) | INFERRED | L133 |
| extract_cell_variables | ? (references.extend) | INFERRED | L131 |
| extract_cell_variables | ? (references.extend) | INFERRED | L129 |
| extract_cell_variables | ? (references.extend) | INFERRED | L127 |
| extract_cell_variables | ? (isinstance) | INFERRED | L122 |
| extract_cell_variables | ? (refs.extend) | INFERRED | L119 |
| extract_cell_variables | ? (refs.extend) | INFERRED | L117 |
| extract_cell_variables | ? (refs.extend) | INFERRED | L115 |
| extract_cell_variables | ? (refs.append) | INFERRED | L112 |
| extract_cell_variables | ? (refs.append) | INFERRED | L110 |
| extract_cell_variables | ? (refs.extend) | INFERRED | L108 |
| extract_cell_variables | ? (refs.append) | INFERRED | L106 |
| extract_cell_variables | ? (isinstance) | INFERRED | L100 |
| extract_cell_variables | ? (isinstance) | INFERRED | L94 |
| extract_cell_variables | ? (defines.extend) | INFERRED | L91 |
| extract_cell_variables | ? (isinstance) | INFERRED | L88 |
| extract_cell_variables | ? (parse) | INFERRED | L73 |
| build_variable_flow | ? (used_vars.get) | INFERRED | L233 |
| build_variable_flow | ? (defined_vars.get) | INFERRED | L232 |
| build_variable_flow | ? (used_vars.keys) | INFERRED | L229 |
| build_variable_flow | ? (set) | INFERRED | L229 |
| build_variable_flow | ? (defined_vars.keys) | INFERRED | L229 |
| build_variable_flow | ? (set) | INFERRED | L229 |
| build_variable_flow | ? (used_vars[name].append) | INFERRED | L225 |
| build_variable_flow | ? (defined_vars[name].append) | INFERRED | L215 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| dataclasses | INFERRED |
| dataclasses | INFERRED |
| ast | INFERRED |
