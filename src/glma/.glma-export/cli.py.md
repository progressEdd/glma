---
file_path: cli.py
language: python
last_indexed: 2026-04-13T20:15:23.141218+00:00
chunk_count: 8
content_hash: e9dde70d4355a25963f90e95842e05f13062b2d737d2ea1dfaf951f1600fa230
---

# cli.py

## Summary

Provides a command-line interface for indexing repositories into a database, managing AI-driven summarization, and exporting documentation as static Markdown. It supports repository monitoring for incremental updates and allows users to query indexed file relationships via JSON or Markdown outputs.

**AI Chunk Summaries:**
- **version_callback**: Prints the current application version to the console and terminates execution if the provided boolean flag is true.
- **main**: Defines the CLI entry point using Typer to handle command-line arguments. It currently supports a `--version` flag that triggers a callback to display the application version.
- **index**: Processes a repository's source files into a database using configurable language filters and output paths. Optionally performs an AI-driven summarization pass to generate per-chunk and file-level summaries, updating the database and regenerating markdown documentation.
- **_write_output**: Writes a string to a specified file path using UTF-8 encoding or prints it to the console if no path is provided. It handles output routing based on whether `output_path` is defined.
- **_group_rels_by_chunk**: Organizes a list of relationship dictionaries into a map keyed by chunk IDs. It categorizes each relationship as either "incoming" or "outgoing" based on its direction and associated ID, provided the ID exists in the specified `chunk_ids` list.
- **query**: Processes a request to retrieve and format information about an indexed file or notebook from a repository. It resolves the repository root, handles specialized notebook summarization via AI providers, or queries a `LadybugStore` database to extract file records, chunks, and relationship dependencies for output in Markdown or JSON.
- **watch**: Monitors a repository for file changes to trigger incremental re-indexing. It validates the existence of an existing index and executes an asynchronous watcher using provided path, verbosity, and debounce configurations.
- **export**: Exports a repository index as static markdown for air-gapped use, taking an optional repo path and output destination. It validates the existence of the Ladybug database and applies configuration overrides to determine whether AI summaries and full source code are included in the final export.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| version_callback | function | L21-L24 |  |
| main | function | L28-L34 |  |
| index | function | L38-L174 |  |
| _write_output | function | L177-L182 |  |
| _group_rels_by_chunk | function | L185-L200 |  |
| query | function | L204-L371 |  |
| watch | function | L375-L407 |  |
| export | function | L411-L465 |  |

## Chunks

### version_callback (function, L21-L24)

> *Summary: Prints the current application version to the console and terminates execution if the provided boolean flag is true.*

> **Calls:** ? (glma.export) (INFERRED), ? (glma.db.ladybug_store) (INFERRED), ? (glma.config) (INFERRED), ? (glma.config) (INFERRED), ? (glma.watch) (INFERRED), ? (glma.config) (INFERRED), ? (glma.config) (INFERRED), ? (glma.query.formatter) (INFERRED), ? (glma.query.formatter) (INFERRED), ? (glma.models) (INFERRED), ? (glma.index.pipeline) (INFERRED), ? (glma.db.ladybug_store) (INFERRED), ? (glma.query.notebook) (INFERRED), ? (glma.summarize.providers) (INFERRED), ? (glma.summarize.providers) (INFERRED), ? (glma.config) (INFERRED), ? (glma.index.writer) (INFERRED), ? (glma.db.ladybug_store) (INFERRED), ? (glma.summarize.providers) (INFERRED), ? (glma.summarize.providers) (INFERRED), ? (glma.summarize) (INFERRED), ? (glma.config) (INFERRED), ? (glma.index.progress) (INFERRED), ? (glma.index.pipeline) (INFERRED), ? (glma.models) (INFERRED), ? (glma.config) (INFERRED), ? (glma) (INFERRED), ? (rich.console) (INFERRED), ? (typer) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (sys) (INFERRED), ? (asyncio) (INFERRED), ? (Exit) (INFERRED), ? (console.print) (INFERRED)

### main (function, L28-L34)

> *Summary: Defines the CLI entry point using Typer to handle command-line arguments. It currently supports a `--version` flag that triggers a callback to display the application version.*

> **Calls:** ? (Option) (INFERRED)

### index (function, L38-L174)

> *Summary: Processes a repository's source files into a database using configurable language filters and output paths. Optionally performs an AI-driven summarization pass to generate per-chunk and file-level summaries, updating the database and regenerating markdown documentation.*

> **Calls:** ? (len) (INFERRED), ? (console.print) (INFERRED), ? (write_markdown) (INFERRED), ? (store.get_file_relationships) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (indexed_files.keys) (INFERRED), ? (sorted) (INFERRED), ? (store.update_file_summary) (INFERRED), ? (provider.summarize) (INFERRED), ? ("\n".join) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (store.get_file_record) (INFERRED), ? (indexed_files.keys) (INFERRED), ? (sorted) (INFERRED), ? (console.print) (INFERRED), ? (summarize_chunks) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (indexed_files.keys) (INFERRED), ? (sorted) (INFERRED), ? (console.print) (INFERRED), ? (store.get_indexed_files) (INFERRED), ? (LadybugStore) (INFERRED), ? (Exit) (INFERRED), ? (console.print) (INFERRED), ? (OpenAICompatibleProvider) (INFERRED), ? (PiProvider) (INFERRED), ? (load_summarize_config) (INFERRED), ? (Exit) (INFERRED), ? (console.print) (INFERRED), ? (run_index) (INFERRED), ? (IndexProgress) (INFERRED), ? (console.print) (INFERRED), ? (', '.join) (INFERRED), ? (console.print) (INFERRED), ? (console.print) (INFERRED), ? (load_config) (INFERRED), ? (Language) (INFERRED), ? (cwd) (INFERRED), ? (path.resolve) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Argument) (INFERRED)

### _write_output (function, L177-L182)

> *Summary: Writes a string to a specified file path using UTF-8 encoding or prints it to the console if no path is provided. It handles output routing based on whether `output_path` is defined.*

> **Calls:** ? (console.print) (INFERRED), ? (Path) (INFERRED), ? (Path(output_path).write_text) (INFERRED)

### _group_rels_by_chunk (function, L185-L200)

> *Summary: Organizes a list of relationship dictionaries into a map keyed by chunk IDs. It categorizes each relationship as either "incoming" or "outgoing" based on its direction and associated ID, provided the ID exists in the specified `chunk_ids` list.*

> **Calls:** ? (result[source_id]["outgoing"].append) (INFERRED), ? (rel.get) (INFERRED), ? (result[target_id]["incoming"].append) (INFERRED), ? (rel.get) (INFERRED), ? (rel.get) (INFERRED)

### query (function, L204-L371)

> *Summary: Processes a request to retrieve and format information about an indexed file or notebook from a repository. It resolves the repository root, handles specialized notebook summarization via AI providers, or queries a `LadybugStore` database to extract file records, chunks, and relationship dependencies for output in Markdown or JSON.*

> **Calls:** _write_output (DIRECT), _write_output (DIRECT), _group_rels_by_chunk (DIRECT), ? (Exit) (INFERRED), ? (format_compact_output) (INFERRED), ? (format_json_output) (INFERRED), ? (rels.get) (INFERRED), ? (flat_rels.extend) (INFERRED), ? (rels.get) (INFERRED), ? (flat_rels.extend) (INFERRED), ? (relationships.items) (INFERRED), ? (store.get_all_relationships_for_file) (INFERRED), ? (store.get_file_relationships) (INFERRED), ? (store.traverse_relationships) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (rel_types.split) (INFERRED), ? (min) (INFERRED), ? (QueryConfig) (INFERRED), ? (sys.stderr.write) (INFERRED), ? (file_content_hash) (INFERRED), ? (Exit) (INFERRED), ? (sys.stderr.write) (INFERRED), ? (store.get_file_record) (INFERRED), ? (LadybugStore) (INFERRED), ? (Exit) (INFERRED), ? (sys.stderr.write) (INFERRED), ? (disk_path.exists) (INFERRED), ? (Exit) (INFERRED), ? (sys.stderr.write) (INFERRED), ? (db_path.exists) (INFERRED), ? (compact_notebook) (INFERRED), ? (Exit) (INFERRED), ? (console.print) (INFERRED), ? (OpenAICompatibleProvider) (INFERRED), ? (PiProvider) (INFERRED), ? (load_summarize_config) (INFERRED), ? (Exit) (INFERRED), ? (sys.stderr.write) (INFERRED), ? (disk_path.exists) (INFERRED), ? (filepath.endswith) (INFERRED), ? (Exit) (INFERRED), ? (sys.stderr.write) (INFERRED), ? ((parent / ".glma.toml").is_file) (INFERRED), ? ((parent / ".glma-index").is_dir) (INFERRED), ? (list) (INFERRED), ? (cwd) (INFERRED), ? (repo_root.resolve) (INFERRED), ? (Exit) (INFERRED), ? (sys.stderr.write) (INFERRED), ? (Exit) (INFERRED), ? (sys.stderr.write) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Argument) (INFERRED)

### watch (function, L375-L407)

> *Summary: Monitors a repository for file changes to trigger incremental re-indexing. It validates the existence of an existing index and executes an asynchronous watcher using provided path, verbosity, and debounce configurations.*

> **Calls:** ? (watch_and_index) (INFERRED), ? (run) (INFERRED), ? (load_watch_config) (INFERRED), ? (Exit) (INFERRED), ? (console.print) (INFERRED), ? (db_path.exists) (INFERRED), ? (load_config) (INFERRED), ? (cwd) (INFERRED), ? (path.resolve) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Argument) (INFERRED)

### export (function, L411-L465)

> *Summary: Exports a repository index as static markdown for air-gapped use, taking an optional repo path and output destination. It validates the existence of the Ladybug database and applies configuration overrides to determine whether AI summaries and full source code are included in the final export.*

> **Calls:** ? (export_index) (INFERRED), ? (LadybugStore) (INFERRED), ? (load_export_config) (INFERRED), ? (Exit) (INFERRED), ? (console.print) (INFERRED), ? (db_path.exists) (INFERRED), ? (load_config) (INFERRED), ? (cwd) (INFERRED), ? (path.resolve) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Option) (INFERRED), ? (Argument) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| version_callback | ? (Exit) | INFERRED | L24 |
| version_callback | ? (console.print) | INFERRED | L23 |
| main | ? (Option) | INFERRED | L29 |
| index | ? (len) | INFERRED | L174 |
| index | ? (console.print) | INFERRED | L174 |
| index | ? (write_markdown) | INFERRED | L171 |
| index | ? (store.get_file_relationships) | INFERRED | L170 |
| index | ? (store.get_chunks_for_file) | INFERRED | L168 |
| index | ? (indexed_files.keys) | INFERRED | L167 |
| index | ? (sorted) | INFERRED | L167 |
| index | ? (store.update_file_summary) | INFERRED | L160 |
| index | ? (provider.summarize) | INFERRED | L158 |
| index | ? ("\n".join) | INFERRED | L153 |
| index | ? (store.get_chunks_for_file) | INFERRED | L147 |
| index | ? (store.get_file_record) | INFERRED | L144 |
| index | ? (indexed_files.keys) | INFERRED | L143 |
| index | ? (sorted) | INFERRED | L143 |
| index | ? (console.print) | INFERRED | L141 |
| index | ? (summarize_chunks) | INFERRED | L137 |
| index | ? (store.get_chunks_for_file) | INFERRED | L135 |
| index | ? (indexed_files.keys) | INFERRED | L134 |
| index | ? (sorted) | INFERRED | L134 |
| index | ? (console.print) | INFERRED | L132 |
| index | ? (store.get_indexed_files) | INFERRED | L129 |
| index | ? (LadybugStore) | INFERRED | L128 |
| index | ? (Exit) | INFERRED | L124 |
| index | ? (console.print) | INFERRED | L123 |
| index | ? (OpenAICompatibleProvider) | INFERRED | L118 |
| index | ? (PiProvider) | INFERRED | L116 |
| index | ? (load_summarize_config) | INFERRED | L111 |
| index | ? (Exit) | INFERRED | L95 |
| index | ? (console.print) | INFERRED | L94 |
| index | ? (run_index) | INFERRED | L91 |
| index | ? (IndexProgress) | INFERRED | L90 |
| index | ? (console.print) | INFERRED | L84 |
| index | ? (', '.join) | INFERRED | L83 |
| index | ? (console.print) | INFERRED | L83 |
| index | ? (console.print) | INFERRED | L82 |
| index | ? (load_config) | INFERRED | L79 |
| index | ? (Language) | INFERRED | L74 |
| index | ? (cwd) | INFERRED | L67 |
| index | ? (path.resolve) | INFERRED | L67 |
| index | ? (Option) | INFERRED | L57 |
| index | ? (Option) | INFERRED | L52 |
| index | ? (Option) | INFERRED | L47 |
| index | ? (Option) | INFERRED | L46 |
| index | ? (Option) | INFERRED | L45 |
| index | ? (Option) | INFERRED | L44 |
| index | ? (Option) | INFERRED | L43 |
| index | ? (Argument) | INFERRED | L39 |
| query | _write_output | DIRECT | L368 |
| query | _write_output | DIRECT | L301 |
| _write_output | ? (console.print) | INFERRED | L182 |
| _write_output | ? (Path) | INFERRED | L180 |
| _write_output | ? (Path(output_path).write_text) | INFERRED | L180 |
| query | _group_rels_by_chunk | DIRECT | L349 |
| _group_rels_by_chunk | ? (result[source_id]["outgoing"].append) | INFERRED | L199 |
| _group_rels_by_chunk | ? (rel.get) | INFERRED | L197 |
| _group_rels_by_chunk | ? (result[target_id]["incoming"].append) | INFERRED | L195 |
| _group_rels_by_chunk | ? (rel.get) | INFERRED | L193 |
| _group_rels_by_chunk | ? (rel.get) | INFERRED | L192 |
| query | ? (Exit) | INFERRED | L371 |
| query | ? (format_compact_output) | INFERRED | L366 |
| query | ? (format_json_output) | INFERRED | L363 |
| query | ? (rels.get) | INFERRED | L357 |
| query | ? (flat_rels.extend) | INFERRED | L357 |
| query | ? (rels.get) | INFERRED | L356 |
| query | ? (flat_rels.extend) | INFERRED | L356 |
| query | ? (relationships.items) | INFERRED | L355 |
| query | ? (store.get_all_relationships_for_file) | INFERRED | L352 |
| query | ? (store.get_file_relationships) | INFERRED | L351 |
| query | ? (store.traverse_relationships) | INFERRED | L348 |
| query | ? (store.get_chunks_for_file) | INFERRED | L343 |
| query | ? (rel_types.split) | INFERRED | L338 |
| query | ? (min) | INFERRED | L335 |
| query | ? (QueryConfig) | INFERRED | L333 |
| query | ? (sys.stderr.write) | INFERRED | L329 |
| query | ? (file_content_hash) | INFERRED | L326 |
| query | ? (Exit) | INFERRED | L322 |
| query | ? (sys.stderr.write) | INFERRED | L321 |
| query | ? (store.get_file_record) | INFERRED | L319 |
| query | ? (LadybugStore) | INFERRED | L318 |
| query | ? (Exit) | INFERRED | L314 |
| query | ? (sys.stderr.write) | INFERRED | L313 |
| query | ? (disk_path.exists) | INFERRED | L312 |
| query | ? (Exit) | INFERRED | L308 |
| query | ? (sys.stderr.write) | INFERRED | L307 |
| query | ? (db_path.exists) | INFERRED | L306 |
| query | ? (compact_notebook) | INFERRED | L294 |
| query | ? (Exit) | INFERRED | L289 |
| query | ? (console.print) | INFERRED | L288 |
| query | ? (OpenAICompatibleProvider) | INFERRED | L283 |
| query | ? (PiProvider) | INFERRED | L281 |
| query | ? (load_summarize_config) | INFERRED | L277 |
| query | ? (Exit) | INFERRED | L262 |
| query | ? (sys.stderr.write) | INFERRED | L261 |
| query | ? (disk_path.exists) | INFERRED | L260 |
| query | ? (filepath.endswith) | INFERRED | L258 |
| query | ? (Exit) | INFERRED | L255 |
| query | ? (sys.stderr.write) | INFERRED | L254 |
| query | ? ((parent / ".glma.toml").is_file) | INFERRED | L249 |
| query | ? ((parent / ".glma-index").is_dir) | INFERRED | L249 |
| query | ? (list) | INFERRED | L248 |
| query | ? (cwd) | INFERRED | L246 |
| query | ? (repo_root.resolve) | INFERRED | L243 |
| query | ? (Exit) | INFERRED | L239 |
| query | ? (sys.stderr.write) | INFERRED | L238 |
| query | ? (Exit) | INFERRED | L236 |
| query | ? (sys.stderr.write) | INFERRED | L235 |
| query | ? (Option) | INFERRED | L226 |
| query | ? (Option) | INFERRED | L221 |
| query | ? (Option) | INFERRED | L216 |
| query | ? (Option) | INFERRED | L215 |
| query | ? (Option) | INFERRED | L214 |
| query | ? (Option) | INFERRED | L213 |
| query | ? (Option) | INFERRED | L212 |
| query | ? (Option) | INFERRED | L211 |
| query | ? (Option) | INFERRED | L210 |
| query | ? (Option) | INFERRED | L209 |
| query | ? (Option) | INFERRED | L208 |
| query | ? (Option) | INFERRED | L207 |
| query | ? (Option) | INFERRED | L206 |
| query | ? (Argument) | INFERRED | L205 |
| watch | ? (watch_and_index) | INFERRED | L407 |
| watch | ? (run) | INFERRED | L407 |
| watch | ? (load_watch_config) | INFERRED | L403 |
| watch | ? (Exit) | INFERRED | L394 |
| watch | ? (console.print) | INFERRED | L393 |
| watch | ? (db_path.exists) | INFERRED | L392 |
| watch | ? (load_config) | INFERRED | L390 |
| watch | ? (cwd) | INFERRED | L387 |
| watch | ? (path.resolve) | INFERRED | L387 |
| watch | ? (Option) | INFERRED | L382 |
| watch | ? (Option) | INFERRED | L381 |
| watch | ? (Option) | INFERRED | L380 |
| watch | ? (Argument) | INFERRED | L376 |
| export | ? (export_index) | INFERRED | L465 |
| export | ? (LadybugStore) | INFERRED | L464 |
| export | ? (load_export_config) | INFERRED | L458 |
| export | ? (Exit) | INFERRED | L448 |
| export | ? (console.print) | INFERRED | L447 |
| export | ? (db_path.exists) | INFERRED | L446 |
| export | ? (load_config) | INFERRED | L444 |
| export | ? (cwd) | INFERRED | L441 |
| export | ? (path.resolve) | INFERRED | L441 |
| export | ? (Option) | INFERRED | L432 |
| export | ? (Option) | INFERRED | L427 |
| export | ? (Option) | INFERRED | L422 |
| export | ? (Option) | INFERRED | L416 |
| export | ? (Argument) | INFERRED | L412 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.export | INFERRED |
| glma.db.ladybug_store | INFERRED |
| glma.config | INFERRED |
| glma.config | INFERRED |
| glma.watch | INFERRED |
| glma.config | INFERRED |
| glma.config | INFERRED |
| glma.query.formatter | INFERRED |
| glma.query.formatter | INFERRED |
| glma.models | INFERRED |
| glma.index.pipeline | INFERRED |
| glma.db.ladybug_store | INFERRED |
| glma.query.notebook | INFERRED |
| glma.summarize.providers | INFERRED |
| glma.summarize.providers | INFERRED |
| glma.config | INFERRED |
| glma.index.writer | INFERRED |
| glma.db.ladybug_store | INFERRED |
| glma.summarize.providers | INFERRED |
| glma.summarize.providers | INFERRED |
| glma.summarize | INFERRED |
| glma.config | INFERRED |
| glma.index.progress | INFERRED |
| glma.index.pipeline | INFERRED |
| glma.models | INFERRED |
| glma.config | INFERRED |
| glma | INFERRED |
| rich.console | INFERRED |
| typer | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| sys | INFERRED |
| asyncio | INFERRED |
