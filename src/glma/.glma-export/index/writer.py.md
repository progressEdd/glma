---
file_path: index/writer.py
language: python
last_indexed: 2026-04-13T20:15:23.691353+00:00
chunk_count: 9
content_hash: 3ff3ef148a76e2db8c4fd6090c03c775a09abc3e768c25da49de02cd15726b9d
---

# index/writer.py

## Summary

Generates structured Markdown reports from indexed code chunks and their relationships, including source summaries and dependency tables. It processes chunk metadata and relationship data to write these formatted documents into a mirrored directory structure.

**AI Chunk Summaries:**
- **_chunk_display_type**: Maps a `Chunk` object's type to a human-readable string using a predefined mapping. It returns the corresponding display name or falls back to the string representation of the chunk type if no map entry exists.
- **_format_chunk_heading**: Generates a Markdown H3 heading for a `Chunk` object, incorporating its name, display type, and line range. If a `parent_id` is present, it extracts and appends the parent's name to the heading suffix.
- **_get_lang_hint**: Determines the appropriate markdown language identifier based on a given file extension. It returns `"python"` for `.py` files, `"c"` for `.c` or `.h` files, and an empty string otherwise.
- **_clean_description**: Sanitizes a string by removing Python docstring quotes, `#` prefixes, or C-style block comment markers. It returns the trimmed result truncated to a maximum of 80 characters.
- **_resolve_target_display**: Determines the display string for a relationship target based on a relationship dictionary. It prioritizes resolved names but returns a formatted placeholder (e.g., `? (name)`) if the target is self-referential, inferred without an ID, or otherwise unresolved.
- **_format_inline_relationships**: Filters a list of relationship dictionaries for a specific chunk ID to generate markdown-formatted strings. It outputs lists of "Calls" (outgoing) and "Called by" (incoming) references, including their confidence levels.
- **_format_relationships_summary**: Generates a list of Markdown strings summarizing code relationships (calls, includes, imports, and inheritance) based on provided relationship data and file chunks. It filters and groups these relationships by type and direction to produce formatted tables for outgoing and incoming dependencies.
- **format_file_markdown**: Generates a layered markdown report for an indexed file using its path, extracted chunks, and optional relationships. It produces a structured document containing a rule-based summary, a table of key exports, detailed chunk breakdowns (with optional source code), and a relationship summary.
- **write_markdown**: Generates a markdown representation of indexed file chunks and writes it to a mirrored directory structure within the specified output directory. It takes a list of chunks and configuration paths as input and returns the `Path` to the resulting `.md` file.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| _chunk_display_type | function | L23-L31 |  |
| _format_chunk_heading | function | L34-L44 |  |
| _get_lang_hint | function | L47-L53 |  |
| _clean_description | function | L56-L70 |  |
| _resolve_target_display | function | L73-L93 |  |
| _format_inline_relationships | function | L96-L137 |  |
| _format_relationships_summary | function | L140-L250 |  |
| format_file_markdown | function | L253-L346 |  |
| write_markdown | function | L349-L386 |  |

## Chunks

### _chunk_display_type (function, L23-L31)

> *Summary: Maps a `Chunk` object's type to a human-readable string using a predefined mapping. It returns the corresponding display name or falls back to the string representation of the chunk type if no map entry exists.*

> **Calls:** ? (glma.summaries) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (str) (INFERRED), ? (type_map.get) (INFERRED)

### _format_chunk_heading (function, L34-L44)

> *Summary: Generates a Markdown H3 heading for a `Chunk` object, incorporating its name, display type, and line range. If a `parent_id` is present, it extracts and appends the parent's name to the heading suffix.*

> **Calls:** _chunk_display_type (DIRECT), ? (len) (INFERRED), ? (chunk.parent_id.split) (INFERRED)

### _get_lang_hint (function, L47-L53)

> *Summary: Determines the appropriate markdown language identifier based on a given file extension. It returns `"python"` for `.py` files, `"c"` for `.c` or `.h` files, and an empty string otherwise.*

> **Calls:** ? (file_path.endswith) (INFERRED), ? (file_path.endswith) (INFERRED), ? (file_path.endswith) (INFERRED)

### _clean_description (function, L56-L70)

> *Summary: Sanitizes a string by removing Python docstring quotes, `#` prefixes, or C-style block comment markers. It returns the trimmed result truncated to a maximum of 80 characters.*

> **Calls:** ? (desc.strip) (INFERRED), ? (desc.strip("/*").strip) (INFERRED), ? (desc.strip("/*").strip("*/").strip) (INFERRED), ? (desc.startswith) (INFERRED), ? (desc.lstrip) (INFERRED), ? (desc.lstrip("#").strip) (INFERRED), ? (desc.startswith) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (desc.endswith) (INFERRED), ? (desc.startswith) (INFERRED), ? (comment.strip) (INFERRED)

### _resolve_target_display (function, L73-L93)

> *Summary: Determines the display string for a relationship target based on a relationship dictionary. It prioritizes resolved names but returns a formatted placeholder (e.g., `? (name)`) if the target is self-referential, inferred without an ID, or otherwise unresolved.*

> **Calls:** ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED)

### _format_inline_relationships (function, L96-L137)

> *Summary: Filters a list of relationship dictionaries for a specific chunk ID to generate markdown-formatted strings. It outputs lists of "Calls" (outgoing) and "Called by" (incoming) references, including their confidence levels.*

> **Calls:** _resolve_target_display (DIRECT), ? (', '.join) (INFERRED), ? (lines.append) (INFERRED), ? (parts.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (', '.join) (INFERRED), ? (lines.append) (INFERRED), ? (parts.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED)

### _format_relationships_summary (function, L140-L250)

> *Summary: Generates a list of Markdown strings summarizing code relationships (calls, includes, imports, and inheritance) based on provided relationship data and file chunks. It filters and groups these relationships by type and direction to produce formatted tables for outgoing and incoming dependencies.*

> **Calls:** _resolve_target_display (DIRECT), _resolve_target_display (DIRECT), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (_chunk_name) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (_chunk_name) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (_chunk_name) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (cid.split) (INFERRED), ? (by_type[rt].append) (INFERRED), ? (r.get) (INFERRED)

### format_file_markdown (function, L253-L346)

> *Summary: Generates a layered markdown report for an indexed file using its path, extracted chunks, and optional relationships. It produces a structured document containing a rule-based summary, a table of key exports, detailed chunk breakdowns (with optional source code), and a relationship summary.*

> **Calls:** _chunk_display_type (DIRECT), _format_chunk_heading (DIRECT), _get_lang_hint (DIRECT), _clean_description (DIRECT), _format_inline_relationships (DIRECT), _format_relationships_summary (DIRECT), ? ("\n".join) (INFERRED), ? (lines.extend) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.extend) (INFERRED), ? (lines.append) (INFERRED), ? (chunk.content.strip) (INFERRED), ? (chunk.content.strip().splitlines) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (chunk.content.strip) (INFERRED), ? (chunk.content.strip) (INFERRED), ? (chunk.content.strip().splitlines) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (generate_rule_summary) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### write_markdown (function, L349-L386)

> *Summary: Generates a markdown representation of indexed file chunks and writes it to a mirrored directory structure within the specified output directory. It takes a list of chunks and configuration paths as input and returns the `Path` to the resulting `.md` file.*

> **Calls:** format_file_markdown (DIRECT), ? (md_path.write_text) (INFERRED), ? (Path) (INFERRED), ? (md_dir.mkdir) (INFERRED), ? (Path) (INFERRED), ? (ValueError) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| format_file_markdown | _chunk_display_type | DIRECT | L295 |
| _format_chunk_heading | _chunk_display_type | DIRECT | L36 |
| _chunk_display_type | ? (str) | INFERRED | L31 |
| _chunk_display_type | ? (type_map.get) | INFERRED | L31 |
| format_file_markdown | _format_chunk_heading | DIRECT | L305 |
| _format_chunk_heading | ? (len) | INFERRED | L41 |
| _format_chunk_heading | ? (chunk.parent_id.split) | INFERRED | L40 |
| format_file_markdown | _get_lang_hint | DIRECT | L321 |
| _get_lang_hint | ? (file_path.endswith) | INFERRED | L51 |
| _get_lang_hint | ? (file_path.endswith) | INFERRED | L51 |
| _get_lang_hint | ? (file_path.endswith) | INFERRED | L49 |
| format_file_markdown | _clean_description | DIRECT | L294 |
| _clean_description | ? (desc.strip) | INFERRED | L69 |
| _clean_description | ? (desc.strip("/*").strip) | INFERRED | L69 |
| _clean_description | ? (desc.strip("/*").strip("*/").strip) | INFERRED | L69 |
| _clean_description | ? (desc.startswith) | INFERRED | L68 |
| _clean_description | ? (desc.lstrip) | INFERRED | L66 |
| _clean_description | ? (desc.lstrip("#").strip) | INFERRED | L66 |
| _clean_description | ? (desc.startswith) | INFERRED | L65 |
| _clean_description | ? (len) | INFERRED | L62 |
| _clean_description | ? (len) | INFERRED | L62 |
| _clean_description | ? (desc.endswith) | INFERRED | L61 |
| _clean_description | ? (desc.startswith) | INFERRED | L61 |
| _clean_description | ? (comment.strip) | INFERRED | L58 |
| _format_relationships_summary | _resolve_target_display | DIRECT | L246 |
| _format_relationships_summary | _resolve_target_display | DIRECT | L182 |
| _format_inline_relationships | _resolve_target_display | DIRECT | L119 |
| _resolve_target_display | ? (rel.get) | INFERRED | L93 |
| _resolve_target_display | ? (rel.get) | INFERRED | L92 |
| _resolve_target_display | ? (rel.get) | INFERRED | L91 |
| _resolve_target_display | ? (rel.get) | INFERRED | L91 |
| _resolve_target_display | ? (rel.get) | INFERRED | L89 |
| _resolve_target_display | ? (rel.get) | INFERRED | L89 |
| _resolve_target_display | ? (rel.get) | INFERRED | L87 |
| _resolve_target_display | ? (rel.get) | INFERRED | L86 |
| _resolve_target_display | ? (rel.get) | INFERRED | L86 |
| _resolve_target_display | ? (rel.get) | INFERRED | L86 |
| format_file_markdown | _format_inline_relationships | DIRECT | L331 |
| _format_inline_relationships | ? (', '.join) | INFERRED | L135 |
| _format_inline_relationships | ? (lines.append) | INFERRED | L135 |
| _format_inline_relationships | ? (parts.append) | INFERRED | L134 |
| _format_inline_relationships | ? (r.get) | INFERRED | L133 |
| _format_inline_relationships | ? (r.get) | INFERRED | L132 |
| _format_inline_relationships | ? (r.get) | INFERRED | L128 |
| _format_inline_relationships | ? (r.get) | INFERRED | L127 |
| _format_inline_relationships | ? (r.get) | INFERRED | L126 |
| _format_inline_relationships | ? (', '.join) | INFERRED | L122 |
| _format_inline_relationships | ? (lines.append) | INFERRED | L122 |
| _format_inline_relationships | ? (parts.append) | INFERRED | L121 |
| _format_inline_relationships | ? (r.get) | INFERRED | L120 |
| _format_inline_relationships | ? (r.get) | INFERRED | L114 |
| _format_inline_relationships | ? (r.get) | INFERRED | L113 |
| format_file_markdown | _format_relationships_summary | DIRECT | L340 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L248 |
| _format_relationships_summary | ? (r.get) | INFERRED | L247 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L247 |
| _format_relationships_summary | ? (r.get) | INFERRED | L245 |
| _format_relationships_summary | ? (_chunk_name) | INFERRED | L245 |
| _format_relationships_summary | ? (r.get) | INFERRED | L245 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L243 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L242 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L241 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L240 |
| _format_relationships_summary | ? (r.get) | INFERRED | L238 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L234 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L233 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L232 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L231 |
| _format_relationships_summary | ? (r.get) | INFERRED | L229 |
| _format_relationships_summary | ? (r.get) | INFERRED | L228 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L224 |
| _format_relationships_summary | ? (r.get) | INFERRED | L223 |
| _format_relationships_summary | ? (r.get) | INFERRED | L223 |
| _format_relationships_summary | ? (r.get) | INFERRED | L223 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L223 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L221 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L220 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L219 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L218 |
| _format_relationships_summary | ? (r.get) | INFERRED | L216 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L212 |
| _format_relationships_summary | ? (r.get) | INFERRED | L211 |
| _format_relationships_summary | ? (r.get) | INFERRED | L211 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L211 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L209 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L208 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L207 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L206 |
| _format_relationships_summary | ? (r.get) | INFERRED | L204 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L200 |
| _format_relationships_summary | ? (r.get) | INFERRED | L199 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L199 |
| _format_relationships_summary | ? (r.get) | INFERRED | L198 |
| _format_relationships_summary | ? (_chunk_name) | INFERRED | L198 |
| _format_relationships_summary | ? (r.get) | INFERRED | L197 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L195 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L194 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L193 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L192 |
| _format_relationships_summary | ? (r.get) | INFERRED | L190 |
| _format_relationships_summary | ? (r.get) | INFERRED | L189 |
| _format_relationships_summary | ? (r.get) | INFERRED | L188 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L184 |
| _format_relationships_summary | ? (r.get) | INFERRED | L183 |
| _format_relationships_summary | ? (r.get) | INFERRED | L183 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L183 |
| _format_relationships_summary | ? (r.get) | INFERRED | L181 |
| _format_relationships_summary | ? (_chunk_name) | INFERRED | L181 |
| _format_relationships_summary | ? (r.get) | INFERRED | L181 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L179 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L178 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L177 |
| _format_relationships_summary | ? (lines.append) | INFERRED | L176 |
| _format_relationships_summary | ? (r.get) | INFERRED | L174 |
| _format_relationships_summary | ? (cid.split) | INFERRED | L170 |
| _format_relationships_summary | ? (by_type[rt].append) | INFERRED | L163 |
| _format_relationships_summary | ? (r.get) | INFERRED | L160 |
| write_markdown | format_file_markdown | DIRECT | L383 |
| format_file_markdown | ? ("\n".join) | INFERRED | L346 |
| format_file_markdown | ? (lines.extend) | INFERRED | L344 |
| format_file_markdown | ? (lines.append) | INFERRED | L343 |
| format_file_markdown | ? (lines.append) | INFERRED | L342 |
| format_file_markdown | ? (lines.append) | INFERRED | L336 |
| format_file_markdown | ? (lines.extend) | INFERRED | L334 |
| format_file_markdown | ? (lines.append) | INFERRED | L333 |
| format_file_markdown | ? (chunk.content.strip) | INFERRED | L327 |
| format_file_markdown | ? (chunk.content.strip().splitlines) | INFERRED | L327 |
| format_file_markdown | ? (len) | INFERRED | L327 |
| format_file_markdown | ? (lines.append) | INFERRED | L327 |
| format_file_markdown | ? (chunk.content.strip) | INFERRED | L326 |
| format_file_markdown | ? (chunk.content.strip) | INFERRED | L326 |
| format_file_markdown | ? (chunk.content.strip().splitlines) | INFERRED | L326 |
| format_file_markdown | ? (lines.append) | INFERRED | L323 |
| format_file_markdown | ? (lines.append) | INFERRED | L322 |
| format_file_markdown | ? (lines.append) | INFERRED | L321 |
| format_file_markdown | ? (lines.append) | INFERRED | L317 |
| format_file_markdown | ? (lines.append) | INFERRED | L316 |
| format_file_markdown | ? (lines.append) | INFERRED | L311 |
| format_file_markdown | ? (lines.append) | INFERRED | L310 |
| format_file_markdown | ? (lines.append) | INFERRED | L306 |
| format_file_markdown | ? (lines.append) | INFERRED | L305 |
| format_file_markdown | ? (lines.append) | INFERRED | L302 |
| format_file_markdown | ? (lines.append) | INFERRED | L301 |
| format_file_markdown | ? (lines.append) | INFERRED | L298 |
| format_file_markdown | ? (lines.append) | INFERRED | L297 |
| format_file_markdown | ? (lines.append) | INFERRED | L295 |
| format_file_markdown | ? (lines.append) | INFERRED | L286 |
| format_file_markdown | ? (lines.append) | INFERRED | L285 |
| format_file_markdown | ? (lines.append) | INFERRED | L284 |
| format_file_markdown | ? (lines.append) | INFERRED | L283 |
| format_file_markdown | ? (lines.append) | INFERRED | L280 |
| format_file_markdown | ? (lines.append) | INFERRED | L279 |
| format_file_markdown | ? (generate_rule_summary) | INFERRED | L278 |
| format_file_markdown | ? (lines.append) | INFERRED | L275 |
| format_file_markdown | ? (lines.append) | INFERRED | L274 |
| write_markdown | ? (md_path.write_text) | INFERRED | L384 |
| write_markdown | ? (Path) | INFERRED | L380 |
| write_markdown | ? (md_dir.mkdir) | INFERRED | L378 |
| write_markdown | ? (Path) | INFERRED | L377 |
| write_markdown | ? (ValueError) | INFERRED | L371 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.summaries | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
