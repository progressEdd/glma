---
file_path: query/notebook.py
language: python
last_indexed: 2026-04-13T20:15:24.171413+00:00
chunk_count: 13
content_hash: 1e4b250051ae2c3633cc0714aeda8503038dcbd3d76246462b3b11dea233f55a
---

# query/notebook.py

## Summary

Processes Jupyter notebooks into structured Markdown summaries by analyzing variable flow, grouping cells into logical sections, and optionally using an AI provider with BLAKE2b-based caching for cell descriptions. It outputs a comprehensive report including section overviews, detailed cell breakdowns, and variable dependency tables.

**AI Chunk Summaries:**
- **CachedCell**: Defines a data structure for storing cached notebook cell summaries. It tracks the cell's index, a content hash for change detection, and the resulting summary text.
- **_cell_content_hash**: Generates a 32-byte BLAKE2b hexadecimal hash from a UTF-8 encoded string of cell source content. It takes a string as input and returns its unique cryptographic digest.
- **_cell_content_hash_with_outputs**: Generates a BLAKE2b hash from a cell's source code and its associated outputs to facilitate cache invalidation. It processes stream, execute result, and error output types into UTF-8 encoded bytes to produce a unique 32-byte hexadecimal digest.
- **_format_outputs_for_context**: Converts a list of notebook cell output objects into a single formatted string for LLM context. It extracts text from streams and execution results, formats errors, and truncates the final result to a specified character limit.
- **_notebook_file_hash**: Computes a 32-byte BLAKE2b hexadecimal hash of a notebook file's raw bytes. It takes a `Path` object as input and returns the resulting hash string.
- **_load_cache**: Retrieves cached cell summaries from a JSON file based on the notebook's path and content hash. It returns a dictionary mapping cell indices to their corresponding content hashes and summaries, returning an empty dictionary if the cache is missing or invalid.
- **_save_cache**: Persists a list of `CachedCell` objects to a JSON file within the specified directory. It generates a unique filename using the notebook's stem and a content hash to ensure cache integrity.
- **_extract_heading**: Parses a markdown string to find the first occurrence of an ATX-style heading. It returns a tuple containing the heading level (1-6) and the trimmed text, or `None` if no match is found.
- **_group_sections**: Organizes a list of notebook cells into logical sections based on markdown headings. It returns a list of section metadata objects containing the heading title, level, and the range of cell indices belonging to each group.
- **_generate_section_summary**: Produces a rule-based summary string for a notebook section by analyzing imports, function/class definitions, and variables that flow into other cells. It processes section metadata, cell variable information, and data flow to return a concise description of the section's primary programmatic contributions.
- **_format_variable_flow_table**: Generates a Markdown table summarizing variable definitions and usages from a flow dictionary. It maps each variable to its definition locations (cell and line) and a deduplicated list of cells where it is used.
- **_format_cell**: Converts notebook cell metadata, variable flow, and execution outputs into a list of formatted Markdown strings. It handles markdown cells as blockquotes and code cells by optionally including source code, AI summaries, per-statement variable definitions/references, and processed output values.
- **compact_notebook**: Converts a Jupyter notebook file into a structured markdown summary, optionally using an AI provider to generate cell summaries with caching support. It analyzes variable flow and section groupings to produce a layered report containing a sections overview, detailed cell breakdowns (with configurable code/output visibility), and a variable dependency table.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| CachedCell | class | L26-L30 |  |
| _cell_content_hash | function | L33-L35 |  |
| _cell_content_hash_with_outputs | function | L38-L58 |  |
| _format_outputs_for_context | function | L61-L94 |  |
| _notebook_file_hash | function | L97-L100 |  |
| _load_cache | function | L103-L124 |  |
| _save_cache | function | L127-L141 |  |
| _extract_heading | function | L144-L153 |  |
| _group_sections | function | L156-L208 |  |
| _generate_section_summary | function | L211-L281 |  |
| _format_variable_flow_table | function | L284-L303 |  |
| _format_cell | function | L306-L409 |  |
| compact_notebook | function | L412-L559 |  |

## Chunks

### CachedCell (class, L26-L30)

> *Summary: Defines a data structure for storing cached notebook cell summaries. It tracks the cell's index, a content hash for change detection, and the resulting summary text.*

> **Calls:** ? (glma.summarize.providers) (INFERRED), ? (glma.query.variables) (INFERRED), ? (glma.query.variables) (INFERRED), ? (glma.query.variables) (INFERRED), ? (nbformat) (INFERRED), ? (typing) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (dataclasses) (INFERRED), ? (re) (INFERRED), ? (json) (INFERRED), ? (hashlib) (INFERRED)

### _cell_content_hash (function, L33-L35)

> *Summary: Generates a 32-byte BLAKE2b hexadecimal hash from a UTF-8 encoded string of cell source content. It takes a string as input and returns its unique cryptographic digest.*

> **Calls:** ? (source.encode) (INFERRED), ? (blake2b) (INFERRED), ? (hashlib.blake2b(source.encode("utf-8"), digest_size=32).hexdigest) (INFERRED)

### _cell_content_hash_with_outputs (function, L38-L58)

> *Summary: Generates a BLAKE2b hash from a cell's source code and its associated outputs to facilitate cache invalidation. It processes stream, execute result, and error output types into UTF-8 encoded bytes to produce a unique 32-byte hexadecimal digest.*

> **Calls:** ? (hasher.hexdigest) (INFERRED), ? (output.get) (INFERRED), ? (output.get("evalue", "").encode) (INFERRED), ? (hasher.update) (INFERRED), ? (output.get) (INFERRED), ? (output.get("ename", "").encode) (INFERRED), ? (hasher.update) (INFERRED), ? (text.encode) (INFERRED), ? (hasher.update) (INFERRED), ? ("".join) (INFERRED), ? (isinstance) (INFERRED), ? (data.get) (INFERRED), ? (output.get) (INFERRED), ? (text.encode) (INFERRED), ? (hasher.update) (INFERRED), ? ("".join) (INFERRED), ? (isinstance) (INFERRED), ? (output.get) (INFERRED), ? (output.get) (INFERRED), ? (source.encode) (INFERRED), ? (hasher.update) (INFERRED), ? (blake2b) (INFERRED)

### _format_outputs_for_context (function, L61-L94)

> *Summary: Converts a list of notebook cell output objects into a single formatted string for LLM context. It extracts text from streams and execution results, formats errors, and truncates the final result to a specified character limit.*

> **Calls:** ? (len) (INFERRED), ? (len) (INFERRED), ? ("\n".join) (INFERRED), ? (parts.append) (INFERRED), ? (parts.append) (INFERRED), ? (output.get) (INFERRED), ? (output.get) (INFERRED), ? (text.rstrip) (INFERRED), ? (parts.append) (INFERRED), ? ("".join) (INFERRED), ? (isinstance) (INFERRED), ? (data.get) (INFERRED), ? (output.get) (INFERRED), ? (text.rstrip) (INFERRED), ? (parts.append) (INFERRED), ? ("".join) (INFERRED), ? (isinstance) (INFERRED), ? (output.get) (INFERRED), ? (output.get) (INFERRED)

### _notebook_file_hash (function, L97-L100)

> *Summary: Computes a 32-byte BLAKE2b hexadecimal hash of a notebook file's raw bytes. It takes a `Path` object as input and returns the resulting hash string.*

> **Calls:** ? (blake2b) (INFERRED), ? (hashlib.blake2b(content, digest_size=32).hexdigest) (INFERRED), ? (filepath.read_bytes) (INFERRED)

### _load_cache (function, L103-L124)

> *Summary: Retrieves cached cell summaries from a JSON file based on the notebook's path and content hash. It returns a dictionary mapping cell indices to their corresponding content hashes and summaries, returning an empty dictionary if the cache is missing or invalid.*

> **Calls:** _notebook_file_hash (DIRECT), ? (cell_entry.get) (INFERRED), ? (cell_entry.get) (INFERRED), ? (cell_entry.get) (INFERRED), ? (data.get) (INFERRED), ? (cache_file.read_text) (INFERRED), ? (loads) (INFERRED), ? (cache_file.exists) (INFERRED)

### _save_cache (function, L127-L141)

> *Summary: Persists a list of `CachedCell` objects to a JSON file within the specified directory. It generates a unique filename using the notebook's stem and a content hash to ensure cache integrity.*

> **Calls:** _notebook_file_hash (DIRECT), ? (dumps) (INFERRED), ? (cache_file.write_text) (INFERRED), ? (cache_dir.mkdir) (INFERRED)

### _extract_heading (function, L144-L153)

> *Summary: Parses a markdown string to find the first occurrence of an ATX-style heading. It returns a tuple containing the heading level (1-6) and the trimmed text, or `None` if no match is found.*

> **Calls:** ? (m.group) (INFERRED), ? (m.group(2).strip) (INFERRED), ? (m.group) (INFERRED), ? (len) (INFERRED), ? (match) (INFERRED), ? (source.split) (INFERRED)

### _group_sections (function, L156-L208)

> *Summary: Organizes a list of notebook cells into logical sections based on markdown headings. It returns a list of section metadata objects containing the heading title, level, and the range of cell indices belonging to each group.*

> **Calls:** _extract_heading (DIRECT), ? (sections.append) (INFERRED), ? (current["cell_indices"].append) (INFERRED), ? (sections.append) (INFERRED)

### _generate_section_summary (function, L211-L281)

> *Summary: Produces a rule-based summary string for a notebook section by analyzing imports, function/class definitions, and variables that flow into other cells. It processes section metadata, cell variable information, and data flow to return a concise description of the section's primary programmatic contributions.*

> **Calls:** ? (". ".join) (INFERRED), ? (sum) (INFERRED), ? (sum) (INFERRED), ? (', '.join) (INFERRED), ? (parts.append) (INFERRED), ? (dict.fromkeys) (INFERRED), ? (list) (INFERRED), ? (', '.join) (INFERRED), ? (parts.append) (INFERRED), ? (dict.fromkeys) (INFERRED), ? (list) (INFERRED), ? (', '.join) (INFERRED), ? (parts.append) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (dict.fromkeys) (INFERRED), ? (list) (INFERRED), ? (', '.join) (INFERRED), ? (parts.append) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (dict.fromkeys) (INFERRED), ? (list) (INFERRED), ? (key_vars.append) (INFERRED), ? (flow[var].get) (INFERRED), ? (classes.extend) (INFERRED), ? (functions.extend) (INFERRED), ? (imports.extend) (INFERRED)

### _format_variable_flow_table (function, L284-L303)

> *Summary: Generates a Markdown table summarizing variable definitions and usages from a flow dictionary. It maps each variable to its definition locations (cell and line) and a deduplicated list of cells where it is used.*

> **Calls:** ? (', '.join) (INFERRED), ? (', '.join) (INFERRED), ? (lines.append) (INFERRED), ? (set) (INFERRED), ? (sorted) (INFERRED), ? (defined_strs.append) (INFERRED), ? (flow.items) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### _format_cell (function, L306-L409)

> *Summary: Converts notebook cell metadata, variable flow, and execution outputs into a list of formatted Markdown strings. It handles markdown cells as blockquotes and code cells by optionally including source code, AI summaries, per-statement variable definitions/references, and processed output values.*

> **Calls:** ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (output.get) (INFERRED), ? (output.get) (INFERRED), ? (lines.append) (INFERRED), ? (text.rstrip) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? ("".join) (INFERRED), ? (isinstance) (INFERRED), ? (data.get) (INFERRED), ? (output.get) (INFERRED), ? (lines.append) (INFERRED), ? (text.rstrip) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? ("".join) (INFERRED), ? (isinstance) (INFERRED), ? (output.get) (INFERRED), ? (output.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (' | '.join) (INFERRED), ? (lines.append) (INFERRED), ? (', '.join) (INFERRED), ? (parts.append) (INFERRED), ? (ref_parts.append) (INFERRED), ? (ref_parts.append) (INFERRED), ? (parts.append) (INFERRED), ? (', '.join) (INFERRED), ? (parts.append) (INFERRED), ? (variable_flow.items) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (cell_info.source.strip) (INFERRED), ? (cell_info.source.strip().splitlines) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (cell_info.source.split) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### compact_notebook (function, L412-L559)

> *Summary: Converts a Jupyter notebook file into a structured markdown summary, optionally using an AI provider to generate cell summaries with caching support. It analyzes variable flow and section groupings to produce a layered report containing a sections overview, detailed cell breakdowns (with configurable code/output visibility), and a variable dependency table.*

> **Calls:** CachedCell (DIRECT), CachedCell (DIRECT), _cell_content_hash_with_outputs (DIRECT), _format_outputs_for_context (DIRECT), _load_cache (DIRECT), _save_cache (DIRECT), _group_sections (DIRECT), _generate_section_summary (DIRECT), _format_variable_flow_table (DIRECT), _format_cell (DIRECT), ? ("\n".join) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.extend) (INFERRED), ? (lines.extend) (INFERRED), ? (cell_summaries.get) (INFERRED), ? (cell.get) (INFERRED), ? (enumerate) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (cache_updates.append) (INFERRED), ? (provider.summarize) (INFERRED), ? (cache_updates.append) (INFERRED), ? (cell.get) (INFERRED), ? (len) (INFERRED), ? (ln.strip) (INFERRED), ? (cell.source.splitlines) (INFERRED), ? (enumerate) (INFERRED), ? (cell_data_list.append) (INFERRED), ? (enumerate) (INFERRED), ? (len) (INFERRED), ? (sum) (INFERRED), ? (build_variable_flow) (INFERRED), ? (cell_infos.append) (INFERRED), ? (CellVariableInfo) (INFERRED), ? (extract_cell_variables) (INFERRED), ? (enumerate) (INFERRED), ? (str) (INFERRED), ? (read) (INFERRED), ? (Path) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| compact_notebook | CachedCell | DIRECT | L513 |
| compact_notebook | CachedCell | DIRECT | L488 |
| _cell_content_hash | ? (source.encode) | INFERRED | L35 |
| _cell_content_hash | ? (blake2b) | INFERRED | L35 |
| _cell_content_hash | ? (hashlib.blake2b(source.encode("utf-8"), digest_size=32).hexdigest) | INFERRED | L35 |
| compact_notebook | _cell_content_hash_with_outputs | DIRECT | L483 |
| _cell_content_hash_with_outputs | ? (hasher.hexdigest) | INFERRED | L58 |
| _cell_content_hash_with_outputs | ? (output.get) | INFERRED | L57 |
| _cell_content_hash_with_outputs | ? (output.get("evalue", "").encode) | INFERRED | L57 |
| _cell_content_hash_with_outputs | ? (hasher.update) | INFERRED | L57 |
| _cell_content_hash_with_outputs | ? (output.get) | INFERRED | L56 |
| _cell_content_hash_with_outputs | ? (output.get("ename", "").encode) | INFERRED | L56 |
| _cell_content_hash_with_outputs | ? (hasher.update) | INFERRED | L56 |
| _cell_content_hash_with_outputs | ? (text.encode) | INFERRED | L54 |
| _cell_content_hash_with_outputs | ? (hasher.update) | INFERRED | L54 |
| _cell_content_hash_with_outputs | ? ("".join) | INFERRED | L53 |
| _cell_content_hash_with_outputs | ? (isinstance) | INFERRED | L52 |
| _cell_content_hash_with_outputs | ? (data.get) | INFERRED | L51 |
| _cell_content_hash_with_outputs | ? (output.get) | INFERRED | L50 |
| _cell_content_hash_with_outputs | ? (text.encode) | INFERRED | L48 |
| _cell_content_hash_with_outputs | ? (hasher.update) | INFERRED | L48 |
| _cell_content_hash_with_outputs | ? ("".join) | INFERRED | L47 |
| _cell_content_hash_with_outputs | ? (isinstance) | INFERRED | L46 |
| _cell_content_hash_with_outputs | ? (output.get) | INFERRED | L45 |
| _cell_content_hash_with_outputs | ? (output.get) | INFERRED | L43 |
| _cell_content_hash_with_outputs | ? (source.encode) | INFERRED | L41 |
| _cell_content_hash_with_outputs | ? (hasher.update) | INFERRED | L41 |
| _cell_content_hash_with_outputs | ? (blake2b) | INFERRED | L40 |
| compact_notebook | _format_outputs_for_context | DIRECT | L506 |
| _format_outputs_for_context | ? (len) | INFERRED | L93 |
| _format_outputs_for_context | ? (len) | INFERRED | L92 |
| _format_outputs_for_context | ? ("\n".join) | INFERRED | L91 |
| _format_outputs_for_context | ? (parts.append) | INFERRED | L86 |
| _format_outputs_for_context | ? (parts.append) | INFERRED | L84 |
| _format_outputs_for_context | ? (output.get) | INFERRED | L83 |
| _format_outputs_for_context | ? (output.get) | INFERRED | L82 |
| _format_outputs_for_context | ? (text.rstrip) | INFERRED | L80 |
| _format_outputs_for_context | ? (parts.append) | INFERRED | L80 |
| _format_outputs_for_context | ? ("".join) | INFERRED | L79 |
| _format_outputs_for_context | ? (isinstance) | INFERRED | L78 |
| _format_outputs_for_context | ? (data.get) | INFERRED | L77 |
| _format_outputs_for_context | ? (output.get) | INFERRED | L76 |
| _format_outputs_for_context | ? (text.rstrip) | INFERRED | L74 |
| _format_outputs_for_context | ? (parts.append) | INFERRED | L74 |
| _format_outputs_for_context | ? ("".join) | INFERRED | L73 |
| _format_outputs_for_context | ? (isinstance) | INFERRED | L72 |
| _format_outputs_for_context | ? (output.get) | INFERRED | L71 |
| _format_outputs_for_context | ? (output.get) | INFERRED | L69 |
| _save_cache | _notebook_file_hash | DIRECT | L133 |
| _load_cache | _notebook_file_hash | DIRECT | L109 |
| _notebook_file_hash | ? (blake2b) | INFERRED | L100 |
| _notebook_file_hash | ? (hashlib.blake2b(content, digest_size=32).hexdigest) | INFERRED | L100 |
| _notebook_file_hash | ? (filepath.read_bytes) | INFERRED | L99 |
| compact_notebook | _load_cache | DIRECT | L470 |
| _load_cache | ? (cell_entry.get) | INFERRED | L119 |
| _load_cache | ? (cell_entry.get) | INFERRED | L118 |
| _load_cache | ? (cell_entry.get) | INFERRED | L117 |
| _load_cache | ? (data.get) | INFERRED | L116 |
| _load_cache | ? (cache_file.read_text) | INFERRED | L114 |
| _load_cache | ? (loads) | INFERRED | L114 |
| _load_cache | ? (cache_file.exists) | INFERRED | L111 |
| compact_notebook | _save_cache | DIRECT | L519 |
| _save_cache | ? (dumps) | INFERRED | L141 |
| _save_cache | ? (cache_file.write_text) | INFERRED | L141 |
| _save_cache | ? (cache_dir.mkdir) | INFERRED | L132 |
| _group_sections | _extract_heading | DIRECT | L178 |
| _extract_heading | ? (m.group) | INFERRED | L152 |
| _extract_heading | ? (m.group(2).strip) | INFERRED | L152 |
| _extract_heading | ? (m.group) | INFERRED | L152 |
| _extract_heading | ? (len) | INFERRED | L152 |
| _extract_heading | ? (match) | INFERRED | L150 |
| _extract_heading | ? (source.split) | INFERRED | L149 |
| compact_notebook | _group_sections | DIRECT | L465 |
| _group_sections | ? (sections.append) | INFERRED | L206 |
| _group_sections | ? (current["cell_indices"].append) | INFERRED | L202 |
| _group_sections | ? (sections.append) | INFERRED | L182 |
| compact_notebook | _generate_section_summary | DIRECT | L533 |
| _generate_section_summary | ? (". ".join) | INFERRED | L281 |
| _generate_section_summary | ? (sum) | INFERRED | L276 |
| _generate_section_summary | ? (sum) | INFERRED | L275 |
| _generate_section_summary | ? (', '.join) | INFERRED | L272 |
| _generate_section_summary | ? (parts.append) | INFERRED | L272 |
| _generate_section_summary | ? (dict.fromkeys) | INFERRED | L271 |
| _generate_section_summary | ? (list) | INFERRED | L271 |
| _generate_section_summary | ? (', '.join) | INFERRED | L268 |
| _generate_section_summary | ? (parts.append) | INFERRED | L268 |
| _generate_section_summary | ? (dict.fromkeys) | INFERRED | L267 |
| _generate_section_summary | ? (list) | INFERRED | L267 |
| _generate_section_summary | ? (', '.join) | INFERRED | L264 |
| _generate_section_summary | ? (parts.append) | INFERRED | L264 |
| _generate_section_summary | ? (len) | INFERRED | L263 |
| _generate_section_summary | ? (len) | INFERRED | L263 |
| _generate_section_summary | ? (len) | INFERRED | L263 |
| _generate_section_summary | ? (dict.fromkeys) | INFERRED | L262 |
| _generate_section_summary | ? (list) | INFERRED | L262 |
| _generate_section_summary | ? (', '.join) | INFERRED | L259 |
| _generate_section_summary | ? (parts.append) | INFERRED | L259 |
| _generate_section_summary | ? (len) | INFERRED | L258 |
| _generate_section_summary | ? (len) | INFERRED | L258 |
| _generate_section_summary | ? (len) | INFERRED | L258 |
| _generate_section_summary | ? (dict.fromkeys) | INFERRED | L257 |
| _generate_section_summary | ? (list) | INFERRED | L257 |
| _generate_section_summary | ? (key_vars.append) | INFERRED | L254 |
| _generate_section_summary | ? (flow[var].get) | INFERRED | L250 |
| _generate_section_summary | ? (classes.extend) | INFERRED | L245 |
| _generate_section_summary | ? (functions.extend) | INFERRED | L243 |
| _generate_section_summary | ? (imports.extend) | INFERRED | L241 |
| compact_notebook | _format_variable_flow_table | DIRECT | L553 |
| _format_variable_flow_table | ? (', '.join) | INFERRED | L301 |
| _format_variable_flow_table | ? (', '.join) | INFERRED | L301 |
| _format_variable_flow_table | ? (lines.append) | INFERRED | L301 |
| _format_variable_flow_table | ? (set) | INFERRED | L298 |
| _format_variable_flow_table | ? (sorted) | INFERRED | L298 |
| _format_variable_flow_table | ? (defined_strs.append) | INFERRED | L295 |
| _format_variable_flow_table | ? (flow.items) | INFERRED | L292 |
| _format_variable_flow_table | ? (lines.append) | INFERRED | L290 |
| _format_variable_flow_table | ? (lines.append) | INFERRED | L289 |
| _format_variable_flow_table | ? (lines.append) | INFERRED | L288 |
| _format_variable_flow_table | ? (lines.append) | INFERRED | L287 |
| compact_notebook | _format_cell | DIRECT | L544 |
| _format_cell | ? (lines.append) | INFERRED | L408 |
| _format_cell | ? (lines.append) | INFERRED | L406 |
| _format_cell | ? (lines.append) | INFERRED | L404 |
| _format_cell | ? (output.get) | INFERRED | L403 |
| _format_cell | ? (output.get) | INFERRED | L402 |
| _format_cell | ? (lines.append) | INFERRED | L400 |
| _format_cell | ? (text.rstrip) | INFERRED | L399 |
| _format_cell | ? (lines.append) | INFERRED | L399 |
| _format_cell | ? (lines.append) | INFERRED | L398 |
| _format_cell | ? ("".join) | INFERRED | L397 |
| _format_cell | ? (isinstance) | INFERRED | L396 |
| _format_cell | ? (data.get) | INFERRED | L395 |
| _format_cell | ? (output.get) | INFERRED | L394 |
| _format_cell | ? (lines.append) | INFERRED | L392 |
| _format_cell | ? (text.rstrip) | INFERRED | L391 |
| _format_cell | ? (lines.append) | INFERRED | L391 |
| _format_cell | ? (lines.append) | INFERRED | L390 |
| _format_cell | ? ("".join) | INFERRED | L389 |
| _format_cell | ? (isinstance) | INFERRED | L388 |
| _format_cell | ? (output.get) | INFERRED | L387 |
| _format_cell | ? (output.get) | INFERRED | L385 |
| _format_cell | ? (lines.append) | INFERRED | L383 |
| _format_cell | ? (lines.append) | INFERRED | L382 |
| _format_cell | ? (' | '.join) | INFERRED | L378 |
| _format_cell | ? (lines.append) | INFERRED | L378 |
| _format_cell | ? (', '.join) | INFERRED | L376 |
| _format_cell | ? (parts.append) | INFERRED | L376 |
| _format_cell | ? (ref_parts.append) | INFERRED | L375 |
| _format_cell | ? (ref_parts.append) | INFERRED | L373 |
| _format_cell | ? (parts.append) | INFERRED | L367 |
| _format_cell | ? (', '.join) | INFERRED | L365 |
| _format_cell | ? (parts.append) | INFERRED | L365 |
| _format_cell | ? (variable_flow.items) | INFERRED | L354 |
| _format_cell | ? (lines.append) | INFERRED | L351 |
| _format_cell | ? (lines.append) | INFERRED | L347 |
| _format_cell | ? (len) | INFERRED | L345 |
| _format_cell | ? (len) | INFERRED | L345 |
| _format_cell | ? (lines.append) | INFERRED | L345 |
| _format_cell | ? (cell_info.source.strip) | INFERRED | L342 |
| _format_cell | ? (cell_info.source.strip().splitlines) | INFERRED | L342 |
| _format_cell | ? (lines.append) | INFERRED | L339 |
| _format_cell | ? (lines.append) | INFERRED | L338 |
| _format_cell | ? (lines.append) | INFERRED | L337 |
| _format_cell | ? (lines.append) | INFERRED | L334 |
| _format_cell | ? (lines.append) | INFERRED | L333 |
| _format_cell | ? (lines.append) | INFERRED | L329 |
| _format_cell | ? (lines.append) | INFERRED | L328 |
| _format_cell | ? (lines.append) | INFERRED | L324 |
| _format_cell | ? (lines.append) | INFERRED | L323 |
| _format_cell | ? (cell_info.source.split) | INFERRED | L322 |
| _format_cell | ? (lines.append) | INFERRED | L320 |
| _format_cell | ? (lines.append) | INFERRED | L319 |
| compact_notebook | ? ("\n".join) | INFERRED | L559 |
| compact_notebook | ? (lines.append) | INFERRED | L557 |
| compact_notebook | ? (lines.append) | INFERRED | L556 |
| compact_notebook | ? (lines.append) | INFERRED | L555 |
| compact_notebook | ? (lines.extend) | INFERRED | L553 |
| compact_notebook | ? (lines.extend) | INFERRED | L549 |
| compact_notebook | ? (cell_summaries.get) | INFERRED | L547 |
| compact_notebook | ? (cell.get) | INFERRED | L543 |
| compact_notebook | ? (enumerate) | INFERRED | L541 |
| compact_notebook | ? (lines.append) | INFERRED | L539 |
| compact_notebook | ? (lines.append) | INFERRED | L538 |
| compact_notebook | ? (lines.append) | INFERRED | L535 |
| compact_notebook | ? (lines.append) | INFERRED | L534 |
| compact_notebook | ? (len) | INFERRED | L532 |
| compact_notebook | ? (lines.append) | INFERRED | L530 |
| compact_notebook | ? (lines.append) | INFERRED | L529 |
| compact_notebook | ? (lines.append) | INFERRED | L525 |
| compact_notebook | ? (len) | INFERRED | L524 |
| compact_notebook | ? (lines.append) | INFERRED | L524 |
| compact_notebook | ? (lines.append) | INFERRED | L523 |
| compact_notebook | ? (cache_updates.append) | INFERRED | L513 |
| compact_notebook | ? (provider.summarize) | INFERRED | L510 |
| compact_notebook | ? (cache_updates.append) | INFERRED | L488 |
| compact_notebook | ? (cell.get) | INFERRED | L482 |
| compact_notebook | ? (len) | INFERRED | L478 |
| compact_notebook | ? (ln.strip) | INFERRED | L477 |
| compact_notebook | ? (cell.source.splitlines) | INFERRED | L477 |
| compact_notebook | ? (enumerate) | INFERRED | L473 |
| compact_notebook | ? (cell_data_list.append) | INFERRED | L458 |
| compact_notebook | ? (enumerate) | INFERRED | L457 |
| compact_notebook | ? (len) | INFERRED | L453 |
| compact_notebook | ? (sum) | INFERRED | L452 |
| compact_notebook | ? (build_variable_flow) | INFERRED | L449 |
| compact_notebook | ? (cell_infos.append) | INFERRED | L446 |
| compact_notebook | ? (CellVariableInfo) | INFERRED | L441 |
| compact_notebook | ? (extract_cell_variables) | INFERRED | L439 |
| compact_notebook | ? (enumerate) | INFERRED | L437 |
| compact_notebook | ? (str) | INFERRED | L433 |
| compact_notebook | ? (read) | INFERRED | L433 |
| compact_notebook | ? (Path) | INFERRED | L432 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.summarize.providers | INFERRED |
| glma.query.variables | INFERRED |
| glma.query.variables | INFERRED |
| glma.query.variables | INFERRED |
| nbformat | INFERRED |
| typing | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| dataclasses | INFERRED |
| re | INFERRED |
| json | INFERRED |
| hashlib | INFERRED |
