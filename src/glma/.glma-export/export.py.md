---
file_path: export.py
language: python
last_indexed: 2026-04-13T20:15:23.199108+00:00
chunk_count: 13
content_hash: 3901c85cd7eab84a70bd5790e67ddf28bde862231964fef3c70e7818a58583e9
---

# export.py

## Summary

Exports project metadata and relationship data from a `LadybugStore` into structured Markdown documentation. It generates detailed per-file summaries, dependency graphs, and an overall `ARCHITECTURE.md` overview, outputting the results as a directory, a compressed archive, or a stdout stream.

**AI Chunk Summaries:**
- **_format_export_file**: Generates an enriched Markdown representation of a single source file using its path, metadata record, code chunks, and relationship data. It constructs a structured document containing YAML frontmatter, AI-generated summaries, a table of key exports, detailed chunk content (optionally including raw code), and categorized relationship tables (calls, imports, etc.).
- **_format_rel_path**: Appends a `.md` extension to a given file path string to create an export-relative link. It takes a file path as input and returns the modified string.
- **generate_index_md**: Creates a markdown-formatted index file from indexed file paths and their associated metadata. It outputs a string containing a summary table of all files (including language, chunk counts, and AI summaries) and aggregate codebase statistics.
- **generate_relationships_md**: Processes a dictionary of file data to generate a markdown string representing a cross-file dependency graph. It filters for external relationships and outputs both a detailed dependency table and per-file summaries of imports and calls.
- **_get_module_name**: Extracts a module name from a relative file path by returning the immediate parent directory name if it exists, otherwise falling back to the filename stem. It takes a `file_path` string and returns a corresponding module name string.
- **_module_from_import_name**: Resolves a dotted import path to a module name by matching the last segment of the import against file stems in the provided `file_data` dictionary. It returns the resolved module name via `_get_module_name` or `None` if no match is found.
- **_group_by_module**: Organizes a dictionary of file data into a mapping of module names to sorted lists of associated file paths. It extracts the module name for each path and returns the final collection sorted alphabetically by module.
- **_detect_entry_points**: Identifies potential project entry points from a dictionary of file data using filename conventions, `__main__` block detection, and fan-in analysis (files with outgoing dependencies but no incoming imports). It returns a list of detected files along with their identification method and top-level chunk names.
- **_compute_key_interfaces**: Identifies the top 10 most critical code interfaces by counting unique cross-file incoming imports and calls from `file_data`. It returns a sorted list of metadata dictionaries containing the chunk's name, type, file path, usage count, and summary.
- **generate_architecture_md**: Transforms a dictionary of file metadata, summaries, and relationships into a comprehensive `ARCHITECTURE.md` markdown string. It aggregates data to generate a high-level codebase overview featuring module structures, a dependency graph, detected entry points, and key interfaces.
- **export_index**: Exports the full project index from a `LadybugStore` into static markdown files, including summaries and relationship maps. Based on the `ExportConfig`, it outputs these files as a directory, a compressed archive, or a stream to stdout.
- **_write_files_to_dir**: Writes a set of markdown files and three specific metadata documents (`INDEX`, `RELATIONSHIPS`, and `ARCHITECTURE`) to a target directory. It mirrors the original file structure for individual exports by creating necessary parent directories before writing UTF-8 encoded text.
- **_write_tar_to_stream**: Writes a collection of markdown content and metadata files into a `.tar.gz` archive streamed to a binary output. It takes a writable stream and several strings/dictionaries as input, encoding the text to UTF-8 before adding them as individual files to the compressed archive.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| _format_export_file | function | L19-L214 |  |
| _format_rel_path | function | L217-L222 |  |
| generate_index_md | function | L225-L296 |  |
| generate_relationships_md | function | L299-L405 |  |
| _get_module_name | function | L408-L427 |  |
| _module_from_import_name | function | L430-L463 |  |
| _group_by_module | function | L466-L482 |  |
| _detect_entry_points | function | L485-L574 |  |
| _compute_key_interfaces | function | L577-L655 |  |
| generate_architecture_md | function | L658-L813 |  |
| export_index | function | L816-L903 |  |
| _write_files_to_dir | function | L906-L936 |  |
| _write_tar_to_stream | function | L939-L979 |  |

## Chunks

### _format_export_file (function, L19-L214)

> *Summary: Generates an enriched Markdown representation of a single source file using its path, metadata record, code chunks, and relationship data. It constructs a structured document containing YAML frontmatter, AI-generated summaries, a table of key exports, detailed chunk content (optionally including raw code), and categorized relationship tables (calls, imports, etc.).*

> **Calls:** ? (glma.summaries) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.db.ladybug_store) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (datetime) (INFERRED), ? (datetime) (INFERRED), ? (logging) (INFERRED), ? (tarfile) (INFERRED), ? (sys) (INFERRED), ? (io) (INFERRED), ? ("\n".join) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (by_type.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (by_type.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (by_type.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (r.get) (INFERRED), ? (by_type.get) (INFERRED), ? (by_type.setdefault) (INFERRED), ? (by_type.setdefault(rt, []).append) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (', '.join) (INFERRED), ? (lines.append) (INFERRED), ? (parts.append) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (file_path.endswith) (INFERRED), ? (file_path.endswith) (INFERRED), ? (file_path.endswith) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (chunk.attached_comments[0].strip) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (generate_rule_summary) (INFERRED), ? (lines.append) (INFERRED), ? (hasattr) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (str) (INFERRED), ? (hasattr) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### _format_rel_path (function, L217-L222)

> *Summary: Appends a `.md` extension to a given file path string to create an export-relative link. It takes a file path as input and returns the modified string.*


### generate_index_md (function, L225-L296)

> *Summary: Creates a markdown-formatted index file from indexed file paths and their associated metadata. It outputs a string containing a summary table of all files (including language, chunk counts, and AI summaries) and aggregate codebase statistics.*

> **Calls:** _format_rel_path (DIRECT), ? ("\n".join) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (sum) (INFERRED), ? (sum) (INFERRED), ? (sum) (INFERRED), ? (d.get) (INFERRED), ? (all_chunks.extend) (INFERRED), ? (file_data.values) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (data.get) (INFERRED), ? ("; ".join) (INFERRED), ? (hasattr) (INFERRED), ? (len) (INFERRED), ? (hasattr) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (file_data.get) (INFERRED), ? (indexed_files.keys) (INFERRED), ? (sorted) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (file_data.values) (INFERRED), ? (d.get) (INFERRED), ? (len) (INFERRED), ? (sum) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (now) (INFERRED), ? (datetime.now(timezone.utc).isoformat) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### generate_relationships_md (function, L299-L405)

> *Summary: Processes a dictionary of file data to generate a markdown string representing a cross-file dependency graph. It filters for external relationships and outputs both a detailed dependency table and per-file summaries of imports and calls.*

> **Calls:** _format_rel_path (DIRECT), _format_rel_path (DIRECT), _format_rel_path (DIRECT), _format_rel_path (DIRECT), _format_rel_path (DIRECT), ? ("\n".join) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (sorted) (INFERRED), ? (", ".join) (INFERRED), ? (lines.append) (INFERRED), ? (sorted) (INFERRED), ? (", ".join) (INFERRED), ? (lines.append) (INFERRED), ? (sorted) (INFERRED), ? (", ".join) (INFERRED), ? (lines.append) (INFERRED), ? (sorted) (INFERRED), ? (", ".join) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (calls_to.add) (INFERRED), ? (rel.get) (INFERRED), ? (imports_from.add) (INFERRED), ? (rel.get) (INFERRED), ? (target_id.split) (INFERRED), ? (rel.get) (INFERRED), ? (called_by.add) (INFERRED), ? (rel.get) (INFERRED), ? (imported_by.add) (INFERRED), ? (rel.get) (INFERRED), ? (src_id.split) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED), ? (file_data[path].get) (INFERRED), ? (file_data[path].get) (INFERRED), ? (file_data.keys) (INFERRED), ? (sorted) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (sorted) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (cross_file_rels.append) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (file_data.items) (INFERRED), ? (lines.append) (INFERRED), ? (now) (INFERRED), ? (datetime.now(timezone.utc).isoformat) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### _get_module_name (function, L408-L427)

> *Summary: Extracts a module name from a relative file path by returning the immediate parent directory name if it exists, otherwise falling back to the filename stem. It takes a `file_path` string and returns a corresponding module name string.*

> **Calls:** ? (Path) (INFERRED), ? (len) (INFERRED), ? (Path) (INFERRED)

### _module_from_import_name (function, L430-L463)

> *Summary: Resolves a dotted import path to a module name by matching the last segment of the import against file stems in the provided `file_data` dictionary. It returns the resolved module name via `_get_module_name` or `None` if no match is found.*

> **Calls:** _get_module_name (DIRECT), _get_module_name (DIRECT), ? (Path) (INFERRED), ? (len) (INFERRED), ? (Path) (INFERRED), ? (len) (INFERRED), ? (import_name.split) (INFERRED)

### _group_by_module (function, L466-L482)

> *Summary: Organizes a dictionary of file data into a mapping of module names to sorted lists of associated file paths. It extracts the module name for each path and returns the final collection sorted alphabetically by module.*

> **Calls:** _get_module_name (DIRECT), ? (modules.items) (INFERRED), ? (sorted) (INFERRED), ? (dict) (INFERRED), ? (modules[mod].sort) (INFERRED), ? (modules.setdefault) (INFERRED), ? (modules.setdefault(module, []).append) (INFERRED)

### _detect_entry_points (function, L485-L574)

> *Summary: Identifies potential project entry points from a dictionary of file data using filename conventions, `__main__` block detection, and fan-in analysis (files with outgoing dependencies but no incoming imports). It returns a list of detected files along with their identification method and top-level chunk names.*

> **Calls:** ? (entry_points.append) (INFERRED), ? (data.get) (INFERRED), ? (r.get) (INFERRED), ? (r.get) (INFERRED), ? (any) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (file_data.items) (INFERRED), ? (imported_files.add) (INFERRED), ? (Path) (INFERRED), ? (file_data.items) (INFERRED), ? (target_name.split) (INFERRED), ? (rel.get) (INFERRED), ? (imported_files.add) (INFERRED), ? (target_id.split) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (file_data.items) (INFERRED), ? (set) (INFERRED), ? (entry_points.append) (INFERRED), ? (data.get) (INFERRED), ? (convention_files.add) (INFERRED), ? (data.get) (INFERRED), ? (entry_points.append) (INFERRED), ? (data.get) (INFERRED), ? (convention_files.add) (INFERRED), ? (Path) (INFERRED), ? (file_data.items) (INFERRED), ? (set) (INFERRED)

### _compute_key_interfaces (function, L577-L655)

> *Summary: Identifies the top 10 most critical code interfaces by counting unique cross-file incoming imports and calls from `file_data`. It returns a sorted list of metadata dictionaries containing the chunk's name, type, file path, usage count, and summary.*

> **Calls:** ? (info.get) (INFERRED), ? (set) (INFERRED), ? (source_files.get) (INFERRED), ? (len) (INFERRED), ? (info.get) (INFERRED), ? (info.get) (INFERRED), ? (info.get) (INFERRED), ? (result.append) (INFERRED), ? (chunk_info.get) (INFERRED), ? (incoming_counts.get) (INFERRED), ? (incoming_counts.keys) (INFERRED), ? (sorted) (INFERRED), ? (set) (INFERRED), ? (source_files.setdefault) (INFERRED), ? (source_files.setdefault(matched_cid, set()).add) (INFERRED), ? (incoming_counts.get) (INFERRED), ? (chunk_info[matched_cid].get) (INFERRED), ? (import_to_chunk.get) (INFERRED), ? (target_name.split) (INFERRED), ? (rel.get) (INFERRED), ? (set) (INFERRED), ? (source_files.setdefault) (INFERRED), ? (source_files.setdefault(target_id, set()).add) (INFERRED), ? (incoming_counts.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (file_data.items) (INFERRED), ? (import_to_chunk.setdefault) (INFERRED), ? (import_to_chunk.setdefault(name, []).append) (INFERRED), ? (info.get) (INFERRED), ? (chunk_info.items) (INFERRED), ? (data.get) (INFERRED), ? (file_data.items) (INFERRED)

### generate_architecture_md (function, L658-L813)

> *Summary: Transforms a dictionary of file metadata, summaries, and relationships into a comprehensive `ARCHITECTURE.md` markdown string. It aggregates data to generate a high-level codebase overview featuring module structures, a dependency graph, detected entry points, and key interfaces.*

> **Calls:** _get_module_name (DIRECT), _get_module_name (DIRECT), _module_from_import_name (DIRECT), _group_by_module (DIRECT), _detect_entry_points (DIRECT), _compute_key_interfaces (DIRECT), ? ("\n".join) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (", ".join) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (sorted) (INFERRED), ? (', '.join) (INFERRED), ? (lines.append) (INFERRED), ? (set) (INFERRED), ? (module_deps.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (module_deps.values) (INFERRED), ? (module_deps.keys) (INFERRED), ? (set) (INFERRED), ? (modules.keys) (INFERRED), ? (set) (INFERRED), ? (sorted) (INFERRED), ? (set) (INFERRED), ? (module_deps.setdefault) (INFERRED), ? (module_deps.setdefault(my_module, set()).add) (INFERRED), ? (rel.get) (INFERRED), ? (target_id.split) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (file_data.items) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? ("; ".join) (INFERRED), ? (Path) (INFERRED), ? (narrative_parts.append) (INFERRED), ? (generate_rule_summary) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (narrative_parts.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (data.get) (INFERRED), ? (module_chunks.extend) (INFERRED), ? (data.get) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (modules.items) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (len) (INFERRED), ? (lines.append) (INFERRED), ? (now) (INFERRED), ? (datetime.now(timezone.utc).isoformat) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED), ? (lines.append) (INFERRED)

### export_index (function, L816-L903)

> *Summary: Exports the full project index from a `LadybugStore` into static markdown files, including summaries and relationship maps. Based on the `ExportConfig`, it outputs these files as a directory, a compressed archive, or a stream to stdout.*

> **Calls:** _format_export_file (DIRECT), generate_index_md (DIRECT), generate_relationships_md (DIRECT), generate_architecture_md (DIRECT), ? (console.print) (INFERRED), ? (output_dir.mkdir) (INFERRED), ? (Path) (INFERRED), ? (console.print) (INFERRED), ? (open) (INFERRED), ? (Path) (INFERRED), ? (output.endswith) (INFERRED), ? (output.endswith) (INFERRED), ? (Path) (INFERRED), ? (file_data.items) (INFERRED), ? (generate_rule_summary) (INFERRED), ? ("; ".join) (INFERRED), ? (store.get_file_relationships) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (store.get_file_record) (INFERRED), ? (indexed_files.keys) (INFERRED), ? (sorted) (INFERRED), ? (len) (INFERRED), ? (console.print) (INFERRED), ? (store.get_indexed_files) (INFERRED), _write_files_to_dir (DIRECT), _write_tar_to_stream (DIRECT), _write_tar_to_stream (DIRECT)

### _write_files_to_dir (function, L906-L936)

> *Summary: Writes a set of markdown files and three specific metadata documents (`INDEX`, `RELATIONSHIPS`, and `ARCHITECTURE`) to a target directory. It mirrors the original file structure for individual exports by creating necessary parent directories before writing UTF-8 encoded text.*

> **Calls:** ? ((output_dir / "ARCHITECTURE.md").write_text) (INFERRED), ? ((output_dir / "RELATIONSHIPS.md").write_text) (INFERRED), ? ((output_dir / "INDEX.md").write_text) (INFERRED), ? (md_path.write_text) (INFERRED), ? (md_path.parent.mkdir) (INFERRED), ? (file_exports.items) (INFERRED)

### _write_tar_to_stream (function, L939-L979)

> *Summary: Writes a collection of markdown content and metadata files into a `.tar.gz` archive streamed to a binary output. It takes a writable stream and several strings/dictionaries as input, encoding the text to UTF-8 before adding them as individual files to the compressed archive.*

> **Calls:** ? (BytesIO) (INFERRED), ? (tar.addfile) (INFERRED), ? (len) (INFERRED), ? (TarInfo) (INFERRED), ? (arch_md.encode) (INFERRED), ? (BytesIO) (INFERRED), ? (tar.addfile) (INFERRED), ? (len) (INFERRED), ? (TarInfo) (INFERRED), ? (rels_md.encode) (INFERRED), ? (BytesIO) (INFERRED), ? (tar.addfile) (INFERRED), ? (len) (INFERRED), ? (TarInfo) (INFERRED), ? (index_md.encode) (INFERRED), ? (BytesIO) (INFERRED), ? (tar.addfile) (INFERRED), ? (len) (INFERRED), ? (TarInfo) (INFERRED), ? (content.encode) (INFERRED), ? (file_exports.items) (INFERRED), ? (open) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| export_index | _format_export_file | DIRECT | L867 |
| _format_export_file | ? ("\n".join) | INFERRED | L214 |
| _format_export_file | ? (lines.append) | INFERRED | L212 |
| _format_export_file | ? (r.get) | INFERRED | L211 |
| _format_export_file | ? (lines.append) | INFERRED | L211 |
| _format_export_file | ? (r.get) | INFERRED | L210 |
| _format_export_file | ? (r.get) | INFERRED | L210 |
| _format_export_file | ? (r.get) | INFERRED | L209 |
| _format_export_file | ? (lines.append) | INFERRED | L207 |
| _format_export_file | ? (lines.append) | INFERRED | L206 |
| _format_export_file | ? (lines.append) | INFERRED | L205 |
| _format_export_file | ? (lines.append) | INFERRED | L204 |
| _format_export_file | ? (r.get) | INFERRED | L202 |
| _format_export_file | ? (by_type.get) | INFERRED | L202 |
| _format_export_file | ? (lines.append) | INFERRED | L199 |
| _format_export_file | ? (r.get) | INFERRED | L198 |
| _format_export_file | ? (r.get) | INFERRED | L198 |
| _format_export_file | ? (lines.append) | INFERRED | L198 |
| _format_export_file | ? (lines.append) | INFERRED | L196 |
| _format_export_file | ? (lines.append) | INFERRED | L195 |
| _format_export_file | ? (lines.append) | INFERRED | L194 |
| _format_export_file | ? (lines.append) | INFERRED | L193 |
| _format_export_file | ? (r.get) | INFERRED | L191 |
| _format_export_file | ? (by_type.get) | INFERRED | L191 |
| _format_export_file | ? (lines.append) | INFERRED | L188 |
| _format_export_file | ? (r.get) | INFERRED | L187 |
| _format_export_file | ? (r.get) | INFERRED | L187 |
| _format_export_file | ? (lines.append) | INFERRED | L187 |
| _format_export_file | ? (lines.append) | INFERRED | L185 |
| _format_export_file | ? (lines.append) | INFERRED | L184 |
| _format_export_file | ? (lines.append) | INFERRED | L183 |
| _format_export_file | ? (lines.append) | INFERRED | L182 |
| _format_export_file | ? (r.get) | INFERRED | L180 |
| _format_export_file | ? (by_type.get) | INFERRED | L180 |
| _format_export_file | ? (lines.append) | INFERRED | L177 |
| _format_export_file | ? (r.get) | INFERRED | L176 |
| _format_export_file | ? (r.get) | INFERRED | L176 |
| _format_export_file | ? (r.get) | INFERRED | L176 |
| _format_export_file | ? (lines.append) | INFERRED | L176 |
| _format_export_file | ? (lines.append) | INFERRED | L174 |
| _format_export_file | ? (lines.append) | INFERRED | L173 |
| _format_export_file | ? (lines.append) | INFERRED | L172 |
| _format_export_file | ? (lines.append) | INFERRED | L171 |
| _format_export_file | ? (r.get) | INFERRED | L169 |
| _format_export_file | ? (r.get) | INFERRED | L169 |
| _format_export_file | ? (lines.append) | INFERRED | L166 |
| _format_export_file | ? (r.get) | INFERRED | L165 |
| _format_export_file | ? (r.get) | INFERRED | L165 |
| _format_export_file | ? (lines.append) | INFERRED | L165 |
| _format_export_file | ? (r.get) | INFERRED | L164 |
| _format_export_file | ? (r.get) | INFERRED | L163 |
| _format_export_file | ? (r.get) | INFERRED | L163 |
| _format_export_file | ? (r.get) | INFERRED | L162 |
| _format_export_file | ? (r.get) | INFERRED | L162 |
| _format_export_file | ? (r.get) | INFERRED | L161 |
| _format_export_file | ? (lines.append) | INFERRED | L159 |
| _format_export_file | ? (lines.append) | INFERRED | L158 |
| _format_export_file | ? (lines.append) | INFERRED | L157 |
| _format_export_file | ? (lines.append) | INFERRED | L156 |
| _format_export_file | ? (r.get) | INFERRED | L154 |
| _format_export_file | ? (by_type.get) | INFERRED | L154 |
| _format_export_file | ? (by_type.setdefault) | INFERRED | L149 |
| _format_export_file | ? (by_type.setdefault(rt, []).append) | INFERRED | L149 |
| _format_export_file | ? (r.get) | INFERRED | L148 |
| _format_export_file | ? (lines.append) | INFERRED | L143 |
| _format_export_file | ? (lines.append) | INFERRED | L142 |
| _format_export_file | ? (lines.append) | INFERRED | L138 |
| _format_export_file | ? (', '.join) | INFERRED | L136 |
| _format_export_file | ? (lines.append) | INFERRED | L136 |
| _format_export_file | ? (parts.append) | INFERRED | L134 |
| _format_export_file | ? (r.get) | INFERRED | L133 |
| _format_export_file | ? (r.get) | INFERRED | L132 |
| _format_export_file | ? (r.get) | INFERRED | L131 |
| _format_export_file | ? (r.get) | INFERRED | L131 |
| _format_export_file | ? (r.get) | INFERRED | L130 |
| _format_export_file | ? (r.get) | INFERRED | L126 |
| _format_export_file | ? (lines.append) | INFERRED | L123 |
| _format_export_file | ? (lines.append) | INFERRED | L117 |
| _format_export_file | ? (lines.append) | INFERRED | L116 |
| _format_export_file | ? (lines.append) | INFERRED | L115 |
| _format_export_file | ? (file_path.endswith) | INFERRED | L113 |
| _format_export_file | ? (file_path.endswith) | INFERRED | L113 |
| _format_export_file | ? (file_path.endswith) | INFERRED | L111 |
| _format_export_file | ? (lines.append) | INFERRED | L106 |
| _format_export_file | ? (lines.append) | INFERRED | L105 |
| _format_export_file | ? (lines.append) | INFERRED | L101 |
| _format_export_file | ? (lines.append) | INFERRED | L100 |
| _format_export_file | ? (lines.append) | INFERRED | L97 |
| _format_export_file | ? (lines.append) | INFERRED | L96 |
| _format_export_file | ? (lines.append) | INFERRED | L93 |
| _format_export_file | ? (lines.append) | INFERRED | L92 |
| _format_export_file | ? (lines.append) | INFERRED | L90 |
| _format_export_file | ? (chunk.attached_comments[0].strip) | INFERRED | L89 |
| _format_export_file | ? (lines.append) | INFERRED | L82 |
| _format_export_file | ? (lines.append) | INFERRED | L81 |
| _format_export_file | ? (lines.append) | INFERRED | L80 |
| _format_export_file | ? (lines.append) | INFERRED | L79 |
| _format_export_file | ? (lines.append) | INFERRED | L76 |
| _format_export_file | ? (lines.append) | INFERRED | L75 |
| _format_export_file | ? (lines.append) | INFERRED | L73 |
| _format_export_file | ? (lines.append) | INFERRED | L72 |
| _format_export_file | ? (lines.append) | INFERRED | L67 |
| _format_export_file | ? (generate_rule_summary) | INFERRED | L66 |
| _format_export_file | ? (lines.append) | INFERRED | L64 |
| _format_export_file | ? (hasattr) | INFERRED | L63 |
| _format_export_file | ? (lines.append) | INFERRED | L60 |
| _format_export_file | ? (lines.append) | INFERRED | L59 |
| _format_export_file | ? (lines.append) | INFERRED | L56 |
| _format_export_file | ? (lines.append) | INFERRED | L55 |
| _format_export_file | ? (lines.append) | INFERRED | L52 |
| _format_export_file | ? (lines.append) | INFERRED | L51 |
| _format_export_file | ? (lines.append) | INFERRED | L50 |
| _format_export_file | ? (lines.append) | INFERRED | L49 |
| _format_export_file | ? (lines.append) | INFERRED | L48 |
| _format_export_file | ? (lines.append) | INFERRED | L47 |
| _format_export_file | ? (str) | INFERRED | L46 |
| _format_export_file | ? (hasattr) | INFERRED | L46 |
| _format_export_file | ? (lines.append) | INFERRED | L44 |
| _format_export_file | ? (lines.append) | INFERRED | L43 |
| generate_relationships_md | _format_rel_path | DIRECT | L401 |
| generate_relationships_md | _format_rel_path | DIRECT | L398 |
| generate_relationships_md | _format_rel_path | DIRECT | L395 |
| generate_relationships_md | _format_rel_path | DIRECT | L392 |
| generate_relationships_md | _format_rel_path | DIRECT | L351 |
| generate_index_md | _format_rel_path | DIRECT | L262 |
| export_index | generate_index_md | DIRECT | L877 |
| generate_index_md | ? ("\n".join) | INFERRED | L296 |
| generate_index_md | ? (lines.append) | INFERRED | L294 |
| generate_index_md | ? (len) | INFERRED | L293 |
| generate_index_md | ? (lines.append) | INFERRED | L293 |
| generate_index_md | ? (lines.append) | INFERRED | L292 |
| generate_index_md | ? (lines.append) | INFERRED | L291 |
| generate_index_md | ? (lines.append) | INFERRED | L290 |
| generate_index_md | ? (sum) | INFERRED | L288 |
| generate_index_md | ? (sum) | INFERRED | L287 |
| generate_index_md | ? (sum) | INFERRED | L286 |
| generate_index_md | ? (d.get) | INFERRED | L284 |
| generate_index_md | ? (all_chunks.extend) | INFERRED | L284 |
| generate_index_md | ? (file_data.values) | INFERRED | L283 |
| generate_index_md | ? (lines.append) | INFERRED | L280 |
| generate_index_md | ? (lines.append) | INFERRED | L279 |
| generate_index_md | ? (lines.append) | INFERRED | L276 |
| generate_index_md | ? (lines.append) | INFERRED | L274 |
| generate_index_md | ? (data.get) | INFERRED | L272 |
| generate_index_md | ? ("; ".join) | INFERRED | L270 |
| generate_index_md | ? (hasattr) | INFERRED | L265 |
| generate_index_md | ? (len) | INFERRED | L261 |
| generate_index_md | ? (hasattr) | INFERRED | L260 |
| generate_index_md | ? (data.get) | INFERRED | L258 |
| generate_index_md | ? (data.get) | INFERRED | L257 |
| generate_index_md | ? (file_data.get) | INFERRED | L256 |
| generate_index_md | ? (indexed_files.keys) | INFERRED | L255 |
| generate_index_md | ? (sorted) | INFERRED | L255 |
| generate_index_md | ? (lines.append) | INFERRED | L253 |
| generate_index_md | ? (lines.append) | INFERRED | L252 |
| generate_index_md | ? (lines.append) | INFERRED | L251 |
| generate_index_md | ? (lines.append) | INFERRED | L250 |
| generate_index_md | ? (lines.append) | INFERRED | L247 |
| generate_index_md | ? (lines.append) | INFERRED | L246 |
| generate_index_md | ? (file_data.values) | INFERRED | L245 |
| generate_index_md | ? (d.get) | INFERRED | L245 |
| generate_index_md | ? (len) | INFERRED | L245 |
| generate_index_md | ? (sum) | INFERRED | L245 |
| generate_index_md | ? (len) | INFERRED | L243 |
| generate_index_md | ? (lines.append) | INFERRED | L243 |
| generate_index_md | ? (now) | INFERRED | L242 |
| generate_index_md | ? (datetime.now(timezone.utc).isoformat) | INFERRED | L242 |
| generate_index_md | ? (lines.append) | INFERRED | L242 |
| generate_index_md | ? (lines.append) | INFERRED | L241 |
| generate_index_md | ? (lines.append) | INFERRED | L240 |
| export_index | generate_relationships_md | DIRECT | L878 |
| generate_relationships_md | ? ("\n".join) | INFERRED | L405 |
| generate_relationships_md | ? (lines.append) | INFERRED | L403 |
| generate_relationships_md | ? (lines.append) | INFERRED | L402 |
| generate_relationships_md | ? (sorted) | INFERRED | L401 |
| generate_relationships_md | ? (", ".join) | INFERRED | L401 |
| generate_relationships_md | ? (lines.append) | INFERRED | L399 |
| generate_relationships_md | ? (sorted) | INFERRED | L398 |
| generate_relationships_md | ? (", ".join) | INFERRED | L398 |
| generate_relationships_md | ? (lines.append) | INFERRED | L396 |
| generate_relationships_md | ? (sorted) | INFERRED | L395 |
| generate_relationships_md | ? (", ".join) | INFERRED | L395 |
| generate_relationships_md | ? (lines.append) | INFERRED | L393 |
| generate_relationships_md | ? (sorted) | INFERRED | L392 |
| generate_relationships_md | ? (", ".join) | INFERRED | L392 |
| generate_relationships_md | ? (lines.append) | INFERRED | L390 |
| generate_relationships_md | ? (lines.append) | INFERRED | L389 |
| generate_relationships_md | ? (calls_to.add) | INFERRED | L386 |
| generate_relationships_md | ? (rel.get) | INFERRED | L385 |
| generate_relationships_md | ? (imports_from.add) | INFERRED | L384 |
| generate_relationships_md | ? (rel.get) | INFERRED | L383 |
| generate_relationships_md | ? (target_id.split) | INFERRED | L381 |
| generate_relationships_md | ? (rel.get) | INFERRED | L380 |
| generate_relationships_md | ? (called_by.add) | INFERRED | L378 |
| generate_relationships_md | ? (rel.get) | INFERRED | L377 |
| generate_relationships_md | ? (imported_by.add) | INFERRED | L376 |
| generate_relationships_md | ? (rel.get) | INFERRED | L375 |
| generate_relationships_md | ? (src_id.split) | INFERRED | L373 |
| generate_relationships_md | ? (rel.get) | INFERRED | L372 |
| generate_relationships_md | ? (rel.get) | INFERRED | L371 |
| generate_relationships_md | ? (set) | INFERRED | L368 |
| generate_relationships_md | ? (set) | INFERRED | L367 |
| generate_relationships_md | ? (set) | INFERRED | L366 |
| generate_relationships_md | ? (set) | INFERRED | L365 |
| generate_relationships_md | ? (file_data[path].get) | INFERRED | L362 |
| generate_relationships_md | ? (file_data[path].get) | INFERRED | L361 |
| generate_relationships_md | ? (file_data.keys) | INFERRED | L360 |
| generate_relationships_md | ? (sorted) | INFERRED | L360 |
| generate_relationships_md | ? (lines.append) | INFERRED | L358 |
| generate_relationships_md | ? (lines.append) | INFERRED | L357 |
| generate_relationships_md | ? (lines.append) | INFERRED | L354 |
| generate_relationships_md | ? (lines.append) | INFERRED | L352 |
| generate_relationships_md | ? (sorted) | INFERRED | L350 |
| generate_relationships_md | ? (lines.append) | INFERRED | L348 |
| generate_relationships_md | ? (lines.append) | INFERRED | L347 |
| generate_relationships_md | ? (lines.append) | INFERRED | L346 |
| generate_relationships_md | ? (lines.append) | INFERRED | L345 |
| generate_relationships_md | ? (lines.append) | INFERRED | L342 |
| generate_relationships_md | ? (lines.append) | INFERRED | L341 |
| generate_relationships_md | ? (len) | INFERRED | L340 |
| generate_relationships_md | ? (rel.get) | INFERRED | L337 |
| generate_relationships_md | ? (rel.get) | INFERRED | L337 |
| generate_relationships_md | ? (rel.get) | INFERRED | L336 |
| generate_relationships_md | ? (rel.get) | INFERRED | L335 |
| generate_relationships_md | ? (cross_file_rels.append) | INFERRED | L333 |
| generate_relationships_md | ? (rel.get) | INFERRED | L326 |
| generate_relationships_md | ? (rel.get) | INFERRED | L325 |
| generate_relationships_md | ? (data.get) | INFERRED | L321 |
| generate_relationships_md | ? (data.get) | INFERRED | L320 |
| generate_relationships_md | ? (file_data.items) | INFERRED | L319 |
| generate_relationships_md | ? (lines.append) | INFERRED | L315 |
| generate_relationships_md | ? (now) | INFERRED | L314 |
| generate_relationships_md | ? (datetime.now(timezone.utc).isoformat) | INFERRED | L314 |
| generate_relationships_md | ? (lines.append) | INFERRED | L314 |
| generate_relationships_md | ? (lines.append) | INFERRED | L313 |
| generate_relationships_md | ? (lines.append) | INFERRED | L312 |
| generate_architecture_md | _get_module_name | DIRECT | L755 |
| generate_architecture_md | _get_module_name | DIRECT | L734 |
| _group_by_module | _get_module_name | DIRECT | L477 |
| _module_from_import_name | _get_module_name | DIRECT | L461 |
| _module_from_import_name | _get_module_name | DIRECT | L454 |
| _get_module_name | ? (Path) | INFERRED | L427 |
| _get_module_name | ? (len) | INFERRED | L421 |
| _get_module_name | ? (Path) | INFERRED | L420 |
| generate_architecture_md | _module_from_import_name | DIRECT | L760 |
| _module_from_import_name | ? (Path) | INFERRED | L459 |
| _module_from_import_name | ? (len) | INFERRED | L453 |
| _module_from_import_name | ? (Path) | INFERRED | L452 |
| _module_from_import_name | ? (len) | INFERRED | L448 |
| _module_from_import_name | ? (import_name.split) | INFERRED | L447 |
| generate_architecture_md | _group_by_module | DIRECT | L680 |
| _group_by_module | ? (modules.items) | INFERRED | L482 |
| _group_by_module | ? (sorted) | INFERRED | L482 |
| _group_by_module | ? (dict) | INFERRED | L482 |
| _group_by_module | ? (modules[mod].sort) | INFERRED | L481 |
| _group_by_module | ? (modules.setdefault) | INFERRED | L478 |
| _group_by_module | ? (modules.setdefault(module, []).append) | INFERRED | L478 |
| generate_architecture_md | _detect_entry_points | DIRECT | L784 |
| _detect_entry_points | ? (entry_points.append) | INFERRED | L568 |
| _detect_entry_points | ? (data.get) | INFERRED | L567 |
| _detect_entry_points | ? (r.get) | INFERRED | L562 |
| _detect_entry_points | ? (r.get) | INFERRED | L561 |
| _detect_entry_points | ? (any) | INFERRED | L560 |
| _detect_entry_points | ? (data.get) | INFERRED | L559 |
| _detect_entry_points | ? (data.get) | INFERRED | L558 |
| _detect_entry_points | ? (file_data.items) | INFERRED | L554 |
| _detect_entry_points | ? (imported_files.add) | INFERRED | L552 |
| _detect_entry_points | ? (Path) | INFERRED | L551 |
| _detect_entry_points | ? (file_data.items) | INFERRED | L548 |
| _detect_entry_points | ? (target_name.split) | INFERRED | L547 |
| _detect_entry_points | ? (rel.get) | INFERRED | L545 |
| _detect_entry_points | ? (imported_files.add) | INFERRED | L542 |
| _detect_entry_points | ? (target_id.split) | INFERRED | L540 |
| _detect_entry_points | ? (rel.get) | INFERRED | L535 |
| _detect_entry_points | ? (rel.get) | INFERRED | L534 |
| _detect_entry_points | ? (rel.get) | INFERRED | L533 |
| _detect_entry_points | ? (data.get) | INFERRED | L532 |
| _detect_entry_points | ? (data.get) | INFERRED | L530 |
| _detect_entry_points | ? (file_data.items) | INFERRED | L529 |
| _detect_entry_points | ? (set) | INFERRED | L528 |
| _detect_entry_points | ? (entry_points.append) | INFERRED | L519 |
| _detect_entry_points | ? (data.get) | INFERRED | L518 |
| _detect_entry_points | ? (convention_files.add) | INFERRED | L517 |
| _detect_entry_points | ? (data.get) | INFERRED | L515 |
| _detect_entry_points | ? (entry_points.append) | INFERRED | L508 |
| _detect_entry_points | ? (data.get) | INFERRED | L507 |
| _detect_entry_points | ? (convention_files.add) | INFERRED | L506 |
| _detect_entry_points | ? (Path) | INFERRED | L504 |
| _detect_entry_points | ? (file_data.items) | INFERRED | L503 |
| _detect_entry_points | ? (set) | INFERRED | L500 |
| generate_architecture_md | _compute_key_interfaces | DIRECT | L799 |
| _compute_key_interfaces | ? (info.get) | INFERRED | L652 |
| _compute_key_interfaces | ? (set) | INFERRED | L651 |
| _compute_key_interfaces | ? (source_files.get) | INFERRED | L651 |
| _compute_key_interfaces | ? (len) | INFERRED | L651 |
| _compute_key_interfaces | ? (info.get) | INFERRED | L650 |
| _compute_key_interfaces | ? (info.get) | INFERRED | L649 |
| _compute_key_interfaces | ? (info.get) | INFERRED | L648 |
| _compute_key_interfaces | ? (result.append) | INFERRED | L647 |
| _compute_key_interfaces | ? (chunk_info.get) | INFERRED | L646 |
| _compute_key_interfaces | ? (incoming_counts.get) | INFERRED | L642 |
| _compute_key_interfaces | ? (incoming_counts.keys) | INFERRED | L642 |
| _compute_key_interfaces | ? (sorted) | INFERRED | L642 |
| _compute_key_interfaces | ? (set) | INFERRED | L639 |
| _compute_key_interfaces | ? (source_files.setdefault) | INFERRED | L639 |
| _compute_key_interfaces | ? (source_files.setdefault(matched_cid, set()).add) | INFERRED | L639 |
| _compute_key_interfaces | ? (incoming_counts.get) | INFERRED | L638 |
| _compute_key_interfaces | ? (chunk_info[matched_cid].get) | INFERRED | L637 |
| _compute_key_interfaces | ? (import_to_chunk.get) | INFERRED | L635 |
| _compute_key_interfaces | ? (target_name.split) | INFERRED | L634 |
| _compute_key_interfaces | ? (rel.get) | INFERRED | L631 |
| _compute_key_interfaces | ? (set) | INFERRED | L628 |
| _compute_key_interfaces | ? (source_files.setdefault) | INFERRED | L628 |
| _compute_key_interfaces | ? (source_files.setdefault(target_id, set()).add) | INFERRED | L628 |
| _compute_key_interfaces | ? (incoming_counts.get) | INFERRED | L627 |
| _compute_key_interfaces | ? (rel.get) | INFERRED | L619 |
| _compute_key_interfaces | ? (rel.get) | INFERRED | L618 |
| _compute_key_interfaces | ? (rel.get) | INFERRED | L615 |
| _compute_key_interfaces | ? (data.get) | INFERRED | L614 |
| _compute_key_interfaces | ? (data.get) | INFERRED | L613 |
| _compute_key_interfaces | ? (file_data.items) | INFERRED | L612 |
| _compute_key_interfaces | ? (import_to_chunk.setdefault) | INFERRED | L610 |
| _compute_key_interfaces | ? (import_to_chunk.setdefault(name, []).append) | INFERRED | L610 |
| _compute_key_interfaces | ? (info.get) | INFERRED | L608 |
| _compute_key_interfaces | ? (chunk_info.items) | INFERRED | L607 |
| _compute_key_interfaces | ? (data.get) | INFERRED | L592 |
| _compute_key_interfaces | ? (file_data.items) | INFERRED | L591 |
| export_index | generate_architecture_md | DIRECT | L879 |
| generate_architecture_md | ? ("\n".join) | INFERRED | L813 |
| generate_architecture_md | ? (lines.append) | INFERRED | L811 |
| generate_architecture_md | ? (lines.append) | INFERRED | L810 |
| generate_architecture_md | ? (lines.append) | INFERRED | L808 |
| generate_architecture_md | ? (len) | INFERRED | L806 |
| generate_architecture_md | ? (lines.append) | INFERRED | L802 |
| generate_architecture_md | ? (lines.append) | INFERRED | L801 |
| generate_architecture_md | ? (lines.append) | INFERRED | L797 |
| generate_architecture_md | ? (lines.append) | INFERRED | L796 |
| generate_architecture_md | ? (lines.append) | INFERRED | L793 |
| generate_architecture_md | ? (lines.append) | INFERRED | L792 |
| generate_architecture_md | ? (lines.append) | INFERRED | L790 |
| generate_architecture_md | ? (", ".join) | INFERRED | L789 |
| generate_architecture_md | ? (lines.append) | INFERRED | L787 |
| generate_architecture_md | ? (lines.append) | INFERRED | L786 |
| generate_architecture_md | ? (lines.append) | INFERRED | L782 |
| generate_architecture_md | ? (lines.append) | INFERRED | L781 |
| generate_architecture_md | ? (lines.append) | INFERRED | L778 |
| generate_architecture_md | ? (lines.append) | INFERRED | L777 |
| generate_architecture_md | ? (sorted) | INFERRED | L775 |
| generate_architecture_md | ? (', '.join) | INFERRED | L775 |
| generate_architecture_md | ? (lines.append) | INFERRED | L775 |
| generate_architecture_md | ? (set) | INFERRED | L773 |
| generate_architecture_md | ? (module_deps.get) | INFERRED | L773 |
| generate_architecture_md | ? (lines.append) | INFERRED | L771 |
| generate_architecture_md | ? (lines.append) | INFERRED | L770 |
| generate_architecture_md | ? (module_deps.values) | INFERRED | L767 |
| generate_architecture_md | ? (module_deps.keys) | INFERRED | L767 |
| generate_architecture_md | ? (set) | INFERRED | L767 |
| generate_architecture_md | ? (modules.keys) | INFERRED | L767 |
| generate_architecture_md | ? (set) | INFERRED | L767 |
| generate_architecture_md | ? (sorted) | INFERRED | L766 |
| generate_architecture_md | ? (set) | INFERRED | L763 |
| generate_architecture_md | ? (module_deps.setdefault) | INFERRED | L763 |
| generate_architecture_md | ? (module_deps.setdefault(my_module, set()).add) | INFERRED | L763 |
| generate_architecture_md | ? (rel.get) | INFERRED | L758 |
| generate_architecture_md | ? (target_id.split) | INFERRED | L753 |
| generate_architecture_md | ? (rel.get) | INFERRED | L743 |
| generate_architecture_md | ? (rel.get) | INFERRED | L742 |
| generate_architecture_md | ? (rel.get) | INFERRED | L739 |
| generate_architecture_md | ? (data.get) | INFERRED | L738 |
| generate_architecture_md | ? (data.get) | INFERRED | L735 |
| generate_architecture_md | ? (file_data.items) | INFERRED | L733 |
| generate_architecture_md | ? (lines.append) | INFERRED | L729 |
| generate_architecture_md | ? (lines.append) | INFERRED | L728 |
| generate_architecture_md | ? (lines.append) | INFERRED | L725 |
| generate_architecture_md | ? (lines.append) | INFERRED | L724 |
| generate_architecture_md | ? (len) | INFERRED | L722 |
| generate_architecture_md | ? ("; ".join) | INFERRED | L721 |
| generate_architecture_md | ? (Path) | INFERRED | L718 |
| generate_architecture_md | ? (narrative_parts.append) | INFERRED | L718 |
| generate_architecture_md | ? (generate_rule_summary) | INFERRED | L717 |
| generate_architecture_md | ? (data.get) | INFERRED | L716 |
| generate_architecture_md | ? (data.get) | INFERRED | L715 |
| generate_architecture_md | ? (narrative_parts.append) | INFERRED | L709 |
| generate_architecture_md | ? (lines.append) | INFERRED | L703 |
| generate_architecture_md | ? (len) | INFERRED | L701 |
| generate_architecture_md | ? (lines.append) | INFERRED | L701 |
| generate_architecture_md | ? (len) | INFERRED | L700 |
| generate_architecture_md | ? (data.get) | INFERRED | L699 |
| generate_architecture_md | ? (module_chunks.extend) | INFERRED | L698 |
| generate_architecture_md | ? (data.get) | INFERRED | L697 |
| generate_architecture_md | ? (lines.append) | INFERRED | L692 |
| generate_architecture_md | ? (lines.append) | INFERRED | L691 |
| generate_architecture_md | ? (lines.append) | INFERRED | L690 |
| generate_architecture_md | ? (lines.append) | INFERRED | L689 |
| generate_architecture_md | ? (modules.items) | INFERRED | L688 |
| generate_architecture_md | ? (lines.append) | INFERRED | L686 |
| generate_architecture_md | ? (lines.append) | INFERRED | L685 |
| generate_architecture_md | ? (lines.append) | INFERRED | L682 |
| generate_architecture_md | ? (len) | INFERRED | L681 |
| generate_architecture_md | ? (lines.append) | INFERRED | L681 |
| generate_architecture_md | ? (now) | INFERRED | L677 |
| generate_architecture_md | ? (datetime.now(timezone.utc).isoformat) | INFERRED | L677 |
| generate_architecture_md | ? (lines.append) | INFERRED | L677 |
| generate_architecture_md | ? (lines.append) | INFERRED | L676 |
| generate_architecture_md | ? (lines.append) | INFERRED | L675 |
| export_index | ? (console.print) | INFERRED | L902 |
| export_index | ? (output_dir.mkdir) | INFERRED | L899 |
| export_index | ? (Path) | INFERRED | L898 |
| export_index | ? (console.print) | INFERRED | L894 |
| export_index | ? (open) | INFERRED | L891 |
| export_index | ? (Path) | INFERRED | L890 |
| export_index | ? (output.endswith) | INFERRED | L888 |
| export_index | ? (output.endswith) | INFERRED | L888 |
| export_index | ? (Path) | INFERRED | L887 |
| export_index | ? (file_data.items) | INFERRED | L866 |
| export_index | ? (generate_rule_summary) | INFERRED | L855 |
| export_index | ? ("; ".join) | INFERRED | L853 |
| export_index | ? (store.get_file_relationships) | INFERRED | L848 |
| export_index | ? (store.get_chunks_for_file) | INFERRED | L847 |
| export_index | ? (store.get_file_record) | INFERRED | L846 |
| export_index | ? (indexed_files.keys) | INFERRED | L845 |
| export_index | ? (sorted) | INFERRED | L845 |
| export_index | ? (len) | INFERRED | L841 |
| export_index | ? (console.print) | INFERRED | L841 |
| export_index | ? (store.get_indexed_files) | INFERRED | L838 |
| _write_files_to_dir | ? ((output_dir / "ARCHITECTURE.md").write_text) | INFERRED | L936 |
| _write_files_to_dir | ? ((output_dir / "RELATIONSHIPS.md").write_text) | INFERRED | L933 |
| _write_files_to_dir | ? ((output_dir / "INDEX.md").write_text) | INFERRED | L930 |
| _write_files_to_dir | ? (md_path.write_text) | INFERRED | L927 |
| _write_files_to_dir | ? (md_path.parent.mkdir) | INFERRED | L926 |
| _write_files_to_dir | ? (file_exports.items) | INFERRED | L923 |
| export_index | _write_files_to_dir | DIRECT | L900 |
| _write_tar_to_stream | ? (BytesIO) | INFERRED | L979 |
| _write_tar_to_stream | ? (tar.addfile) | INFERRED | L979 |
| _write_tar_to_stream | ? (len) | INFERRED | L978 |
| _write_tar_to_stream | ? (TarInfo) | INFERRED | L977 |
| _write_tar_to_stream | ? (arch_md.encode) | INFERRED | L976 |
| _write_tar_to_stream | ? (BytesIO) | INFERRED | L973 |
| _write_tar_to_stream | ? (tar.addfile) | INFERRED | L973 |
| _write_tar_to_stream | ? (len) | INFERRED | L972 |
| _write_tar_to_stream | ? (TarInfo) | INFERRED | L971 |
| _write_tar_to_stream | ? (rels_md.encode) | INFERRED | L970 |
| _write_tar_to_stream | ? (BytesIO) | INFERRED | L967 |
| _write_tar_to_stream | ? (tar.addfile) | INFERRED | L967 |
| _write_tar_to_stream | ? (len) | INFERRED | L966 |
| _write_tar_to_stream | ? (TarInfo) | INFERRED | L965 |
| _write_tar_to_stream | ? (index_md.encode) | INFERRED | L964 |
| _write_tar_to_stream | ? (BytesIO) | INFERRED | L961 |
| _write_tar_to_stream | ? (tar.addfile) | INFERRED | L961 |
| _write_tar_to_stream | ? (len) | INFERRED | L960 |
| _write_tar_to_stream | ? (TarInfo) | INFERRED | L959 |
| _write_tar_to_stream | ? (content.encode) | INFERRED | L958 |
| _write_tar_to_stream | ? (file_exports.items) | INFERRED | L957 |
| _write_tar_to_stream | ? (open) | INFERRED | L955 |
| export_index | _write_tar_to_stream | DIRECT | L892 |
| export_index | _write_tar_to_stream | DIRECT | L886 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.summaries | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.db.ladybug_store | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| datetime | INFERRED |
| datetime | INFERRED |
| logging | INFERRED |
| tarfile | INFERRED |
| sys | INFERRED |
| io | INFERRED |
