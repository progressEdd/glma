---
file_path: query/formatter.py
language: python
last_indexed: 2026-04-13T20:15:23.982230+00:00
chunk_count: 7
content_hash: 39c342459be993ef94372d8149b745456135ac2d4c559d2a0fcf8f7bc6a3f3d6
---

# query/formatter.py

## Summary

Provides utilities to format code chunks, index metadata, and relationship mappings into structured Markdown reports or JSON strings. It transforms raw file records and chunk data into human-readable summaries or machine-readable exports based on a provided configuration.

**AI Chunk Summaries:**
- **_get_lang_hint**: Determines the markdown language identifier based on a given file path's extension. It returns `"python"` for `.py` files, `"c"` for `.c` or `.h` files, and an empty string otherwise.
- **_format_summary**: Generates a list of formatted summary strings for top-level chunks, including their names and types. It extracts and cleans the first attached comment to append as a brief description (up to 80 characters) for each entry.
- **_format_signature_block**: Generates a formatted Markdown list of strings representing a code chunk's header, docstrings, AI summaries, and filtered relationship hints. It takes a `Chunk` object, a dictionary of relationships, and an optional `QueryConfig` to determine which metadata and relationship types to include in the output.
- **_format_verbose_code**: Generates a Markdown-formatted list of strings representing the full code section, taking a list of `Chunk` objects and a file path as input. It iterates through each chunk to append its name, optional AI summary, and content wrapped in language-specific code blocks.
- **_format_index_metadata**: Generates a Markdown-formatted list of strings representing index metadata from a `FileRecord` object. It extracts and formats the content hash (truncated if necessary), indexing timestamp, chunk count, and language value.
- **format_compact_output**: Generates a layered markdown report for a specific file using its metadata, extracted chunks, and relationship mappings. It outputs a string containing index metadata, summaries, and optionally function signatures or full code bodies based on the provided `QueryConfig`.
- **format_json_output**: Generates a formatted JSON string representing a file's index data, including metadata, chunk details, and categorized relationships. It takes file paths, records, chunks, and relationship lists as input, optionally including full chunk content if `verbose` is enabled.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| _get_lang_hint | function | L25-L31 |  |
| _format_summary | function | L34-L53 |  |
| _format_signature_block | function | L56-L122 |  |
| _format_verbose_code | function | L125-L142 |  |
| _format_index_metadata | function | L145-L156 |  |
| format_compact_output | function | L159-L226 |  |
| format_json_output | function | L229-L273 |  |

## Chunks

### _get_lang_hint (function, L25-L31)

> *Summary: Determines the markdown language identifier based on a given file path's extension. It returns `"python"` for `.py` files, `"c"` for `.c` or `.h` files, and an empty string otherwise.*

> **Calls:** ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (typing) (INFERRED), ? (datetime) (INFERRED), ? (json) (INFERRED), ? (file_path.endswith) (INFERRED), ? (file_path.endswith) (INFERRED), ? (file_path.endswith) (INFERRED)

### _format_summary (function, L34-L53)

> *Summary: Generates a list of formatted summary strings for top-level chunks, including their names and types. It extracts and cleans the first attached comment to append as a brief description (up to 80 characters) for each entry.*

> **Calls:** ? (lines.append) (INFERRED), ? (comment.lstrip) (INFERRED), ? (comment.lstrip("#").strip) (INFERRED), ? (comment.startswith) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (comment[len(quote):-len(quote)].strip) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (comment.endswith) (INFERRED), ? (comment.startswith) (INFERRED), ? (chunk.attached_comments[0].strip) (INFERRED)

### _format_signature_block (function, L56-L122)

> *Summary: Generates a formatted Markdown list of strings representing a code chunk's header, docstrings, AI summaries, and filtered relationship hints. It takes a `Chunk` object, a dictionary of relationships, and an optional `QueryConfig` to determine which metadata and relationship types to include in the output.*

> **Calls:** ? (', '.join) (INFERRED), ? (lines.append) (INFERRED), ? (incoming_by_type.items) (INFERRED), ? (incoming_by_type[rt].append) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (', '.join) (INFERRED), ? (lines.append) (INFERRED), ? (outgoing_by_type.items) (INFERRED), ? (outgoing_by_type[rt].append) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (chunk_rels.get) (INFERRED), ? (chunk_rels.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (comment.lstrip) (INFERRED), ? (comment.lstrip("#").strip) (INFERRED), ? (comment.startswith) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (comment[len(quote):-len(quote)].strip) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (comment.endswith) (INFERRED), ? (comment.startswith) (INFERRED), ? (chunk.attached_comments[0].strip) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### _format_verbose_code (function, L125-L142)

> *Summary: Generates a Markdown-formatted list of strings representing the full code section, taking a list of `Chunk` objects and a file path as input. It iterates through each chunk to append its name, optional AI summary, and content wrapped in language-specific code blocks.*

> **Calls:** _get_lang_hint (DIRECT), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### _format_index_metadata (function, L145-L156)

> *Summary: Generates a Markdown-formatted list of strings representing index metadata from a `FileRecord` object. It extracts and formats the content hash (truncated if necessary), indexing timestamp, chunk count, and language value.*

> **Calls:** ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### format_compact_output (function, L159-L226)

> *Summary: Generates a layered markdown report for a specific file using its metadata, extracted chunks, and relationship mappings. It outputs a string containing index metadata, summaries, and optionally function signatures or full code bodies based on the provided `QueryConfig`.*

> **Calls:** _format_summary (DIRECT), _format_signature_block (DIRECT), _format_verbose_code (DIRECT), _format_index_metadata (DIRECT), ? ("\n".join) (INFERRED), ? (lines.extend) (INFERRED), ? (lines.append) (INFERRED), ? (lines.extend) (INFERRED), ? (relationships.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.extend) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.extend) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (dt.strftime) (INFERRED), ? (fromisoformat) (INFERRED), ? (QueryConfig) (INFERRED)

### format_json_output (function, L229-L273)

> *Summary: Generates a formatted JSON string representing a file's index data, including metadata, chunk details, and categorized relationships. It takes file paths, records, chunks, and relationship lists as input, optionally including full chunk content if `verbose` is enabled.*

> **Calls:** ? (dumps) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| _format_verbose_code | _get_lang_hint | DIRECT | L130 |
| _get_lang_hint | ? (file_path.endswith) | INFERRED | L29 |
| _get_lang_hint | ? (file_path.endswith) | INFERRED | L29 |
| _get_lang_hint | ? (file_path.endswith) | INFERRED | L27 |
| format_compact_output | _format_summary | DIRECT | L203 |
| _format_summary | ? (lines.append) | INFERRED | L52 |
| _format_summary | ? (comment.lstrip) | INFERRED | L49 |
| _format_summary | ? (comment.lstrip("#").strip) | INFERRED | L49 |
| _format_summary | ? (comment.startswith) | INFERRED | L48 |
| _format_summary | ? (len) | INFERRED | L45 |
| _format_summary | ? (len) | INFERRED | L45 |
| _format_summary | ? (comment[len(quote):-len(quote)].strip) | INFERRED | L45 |
| _format_summary | ? (len) | INFERRED | L44 |
| _format_summary | ? (len) | INFERRED | L44 |
| _format_summary | ? (comment.endswith) | INFERRED | L44 |
| _format_summary | ? (comment.startswith) | INFERRED | L44 |
| _format_summary | ? (chunk.attached_comments[0].strip) | INFERRED | L41 |
| format_compact_output | _format_signature_block | DIRECT | L218 |
| _format_signature_block | ? (', '.join) | INFERRED | L120 |
| _format_signature_block | ? (lines.append) | INFERRED | L120 |
| _format_signature_block | ? (incoming_by_type.items) | INFERRED | L119 |
| _format_signature_block | ? (incoming_by_type[rt].append) | INFERRED | L117 |
| _format_signature_block | ? (rel.get) | INFERRED | L116 |
| _format_signature_block | ? (rel.get) | INFERRED | L116 |
| _format_signature_block | ? (rel.get) | INFERRED | L113 |
| _format_signature_block | ? (', '.join) | INFERRED | L108 |
| _format_signature_block | ? (lines.append) | INFERRED | L108 |
| _format_signature_block | ? (outgoing_by_type.items) | INFERRED | L107 |
| _format_signature_block | ? (outgoing_by_type[rt].append) | INFERRED | L105 |
| _format_signature_block | ? (rel.get) | INFERRED | L104 |
| _format_signature_block | ? (rel.get) | INFERRED | L101 |
| _format_signature_block | ? (rel.get) | INFERRED | L100 |
| _format_signature_block | ? (rel.get) | INFERRED | L99 |
| _format_signature_block | ? (rel.get) | INFERRED | L99 |
| _format_signature_block | ? (rel.get) | INFERRED | L99 |
| _format_signature_block | ? (rel.get) | INFERRED | L95 |
| _format_signature_block | ? (r.get) | INFERRED | L90 |
| _format_signature_block | ? (r.get) | INFERRED | L89 |
| _format_signature_block | ? (chunk_rels.get) | INFERRED | L85 |
| _format_signature_block | ? (chunk_rels.get) | INFERRED | L84 |
| _format_signature_block | ? (lines.append) | INFERRED | L78 |
| _format_signature_block | ? (lines.append) | INFERRED | L77 |
| _format_signature_block | ? (lines.append) | INFERRED | L73 |
| _format_signature_block | ? (lines.append) | INFERRED | L72 |
| _format_signature_block | ? (comment.lstrip) | INFERRED | L70 |
| _format_signature_block | ? (comment.lstrip("#").strip) | INFERRED | L70 |
| _format_signature_block | ? (comment.startswith) | INFERRED | L69 |
| _format_signature_block | ? (len) | INFERRED | L67 |
| _format_signature_block | ? (len) | INFERRED | L67 |
| _format_signature_block | ? (comment[len(quote):-len(quote)].strip) | INFERRED | L67 |
| _format_signature_block | ? (len) | INFERRED | L66 |
| _format_signature_block | ? (len) | INFERRED | L66 |
| _format_signature_block | ? (comment.endswith) | INFERRED | L66 |
| _format_signature_block | ? (comment.startswith) | INFERRED | L66 |
| _format_signature_block | ? (chunk.attached_comments[0].strip) | INFERRED | L64 |
| _format_signature_block | ? (lines.append) | INFERRED | L60 |
| _format_signature_block | ? (lines.append) | INFERRED | L59 |
| format_compact_output | _format_verbose_code | DIRECT | L224 |
| _format_verbose_code | ? (lines.append) | INFERRED | L141 |
| _format_verbose_code | ? (lines.append) | INFERRED | L140 |
| _format_verbose_code | ? (lines.append) | INFERRED | L139 |
| _format_verbose_code | ? (lines.append) | INFERRED | L138 |
| _format_verbose_code | ? (lines.append) | INFERRED | L137 |
| _format_verbose_code | ? (lines.append) | INFERRED | L136 |
| _format_verbose_code | ? (lines.append) | INFERRED | L133 |
| _format_verbose_code | ? (lines.append) | INFERRED | L132 |
| _format_verbose_code | ? (lines.append) | INFERRED | L129 |
| _format_verbose_code | ? (lines.append) | INFERRED | L128 |
| format_compact_output | _format_index_metadata | DIRECT | L198 |
| _format_index_metadata | ? (lines.append) | INFERRED | L155 |
| _format_index_metadata | ? (lines.append) | INFERRED | L154 |
| _format_index_metadata | ? (lines.append) | INFERRED | L153 |
| _format_index_metadata | ? (lines.append) | INFERRED | L152 |
| _format_index_metadata | ? (lines.append) | INFERRED | L151 |
| _format_index_metadata | ? (len) | INFERRED | L150 |
| _format_index_metadata | ? (lines.append) | INFERRED | L149 |
| _format_index_metadata | ? (lines.append) | INFERRED | L148 |
| format_compact_output | ? ("\n".join) | INFERRED | L226 |
| format_compact_output | ? (lines.extend) | INFERRED | L224 |
| format_compact_output | ? (lines.append) | INFERRED | L220 |
| format_compact_output | ? (lines.extend) | INFERRED | L219 |
| format_compact_output | ? (relationships.get) | INFERRED | L217 |
| format_compact_output | ? (lines.append) | INFERRED | L213 |
| format_compact_output | ? (lines.append) | INFERRED | L212 |
| format_compact_output | ? (lines.append) | INFERRED | L208 |
| format_compact_output | ? (lines.append) | INFERRED | L207 |
| format_compact_output | ? (lines.extend) | INFERRED | L205 |
| format_compact_output | ? (lines.append) | INFERRED | L202 |
| format_compact_output | ? (lines.append) | INFERRED | L201 |
| format_compact_output | ? (lines.extend) | INFERRED | L198 |
| format_compact_output | ? (lines.append) | INFERRED | L195 |
| format_compact_output | ? (lines.append) | INFERRED | L193 |
| format_compact_output | ? (lines.append) | INFERRED | L192 |
| format_compact_output | ? (dt.strftime) | INFERRED | L188 |
| format_compact_output | ? (fromisoformat) | INFERRED | L187 |
| format_compact_output | ? (QueryConfig) | INFERRED | L181 |
| format_json_output | ? (dumps) | INFERRED | L273 |
| format_json_output | ? (r.get) | INFERRED | L270 |
| format_json_output | ? (r.get) | INFERRED | L269 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| typing | INFERRED |
| datetime | INFERRED |
| json | INFERRED |
