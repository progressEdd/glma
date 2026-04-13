---
file_path: index/pipeline.py
language: python
last_indexed: 2026-04-13T20:15:23.814410+00:00
chunk_count: 4
content_hash: 345423d3c6efa68c800642d50a66393b1999b6093e673262b1b4f3f666cfc2c3
---

# index/pipeline.py

## Summary

Implements an incremental indexing pipeline that extracts code chunks and relationships from source files, persisting them to a `LadybugStore`. It utilizes BLAKE2b content hashing to track changes and automatically generates updated markdown documentation for modified files.

**AI Chunk Summaries:**
- **file_content_hash**: Generates a 64-character hex digest of a file's content using the BLAKE2b algorithm. It takes a `Path` object as input and returns the resulting hash string.
- **IndexResult**: Acts as a data transfer object to track indexing statistics. It stores integer counts for processed files (new, updated, skipped, deleted), total chunks, and relationships generated during a run.
- **run_index**: Executes a multi-pass indexing pipeline that discovers source files, extracts code chunks and relationships, and persists them to a `LadybugStore`. It performs incremental updates via content hashing and generates corresponding markdown documentation for all modified or dependent files.
- **_load_chunks_from_store**: Retrieves all `Chunk` records associated with a specific file path from the `LadybugStore` using a Cypher query. It maps the database result rows into a list of `Chunk` objects.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| file_content_hash | function | L19-L29 |  |
| IndexResult | class | L32-L40 |  |
| run_index | function | L43-L257 |  |
| _load_chunks_from_store | function | L260-L282 |  |

## Chunks

### file_content_hash (function, L19-L29)

> *Summary: Generates a 64-character hex digest of a file's content using the BLAKE2b algorithm. It takes a `Path` object as input and returns the resulting hash string.*

> **Calls:** ? (glma.index.writer) (INFERRED), ? (glma.index.walker) (INFERRED), ? (glma.index.relationships) (INFERRED), ? (glma.index.progress) (INFERRED), ? (glma.index.detector) (INFERRED), ? (glma.index.comments) (INFERRED), ? (glma.index.chunks) (INFERRED), ? (glma.db.ladybug_store) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (datetime) (INFERRED), ? (datetime) (INFERRED), ? (hashlib) (INFERRED), ? (blake2b) (INFERRED), ? (hashlib.blake2b(content, digest_size=32).hexdigest) (INFERRED), ? (filepath.read_bytes) (INFERRED)

### IndexResult (class, L32-L40)

> *Summary: Acts as a data transfer object to track indexing statistics. It stores integer counts for processed files (new, updated, skipped, deleted), total chunks, and relationships generated during a run.*


### run_index (function, L43-L257)

> *Summary: Executes a multi-pass indexing pipeline that discovers source files, extracts code chunks and relationships, and persists them to a `LadybugStore`. It performs incremental updates via content hashing and generates corresponding markdown documentation for all modified or dependent files.*

> **Calls:** file_content_hash (DIRECT), IndexResult (DIRECT), ? (progress.print_summary) (INFERRED), ? (progress.finish) (INFERRED), ? (md_path.unlink) (INFERRED), ? (md_path.exists) (INFERRED), ? (Path) (INFERRED), ? (Path(path_to_delete).with_suffix) (INFERRED), ? (store.delete_file) (INFERRED), ? (store.delete_relationships) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED), ? (write_markdown) (INFERRED), ? (all_rels.append) (INFERRED), ? (list) (INFERRED), ? (store.conn.execute) (INFERRED), ? (store.get_incoming_relationships) (INFERRED), ? (store.get_file_relationships) (INFERRED), ? (hasattr) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (filepath.relative_to) (INFERRED), ? (str) (INFERRED), ? (Language) (INFERRED), ? (dependent_paths.add) (INFERRED), ? (list) (INFERRED), ? (store.conn.execute) (INFERRED), ? (store.get_incoming_relationships) (INFERRED), ? (hasattr) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (set) (INFERRED), ? (write_markdown) (INFERRED), ? (store.get_file_relationships) (INFERRED), ? (len) (INFERRED), ? (store.upsert_relationships) (INFERRED), ? (extract_relationships) (INFERRED), ? (hasattr) (INFERRED), ? (store.get_chunks_for_file) (INFERRED), ? (filepath.relative_to) (INFERRED), ? (str) (INFERRED), ? (Language) (INFERRED), ? (progress.console.print) (INFERRED), ? (progress.advance) (INFERRED), ? (len) (INFERRED), ? (write_markdown) (INFERRED), ? (store.upsert_chunks) (INFERRED), ? (store.upsert_file) (INFERRED), ? (len) (INFERRED), ? (now) (INFERRED), ? (datetime.now(timezone.utc).isoformat) (INFERRED), ? (FileRecord) (INFERRED), ? (attach_comments) (INFERRED), ? (extract_chunks) (INFERRED), ? (changed_relative_paths.add) (INFERRED), ? (progress.advance) (INFERRED), ? (indexed_files.get) (INFERRED), ? (progress.advance) (INFERRED), ? (filepath.relative_to) (INFERRED), ? (str) (INFERRED), ? (Language) (INFERRED), ? (set) (INFERRED), ? (f.relative_to) (INFERRED), ? (str) (INFERRED), ? (indexed_files.keys) (INFERRED), ? (set) (INFERRED), ? (store.get_indexed_files) (INFERRED), ? (progress.start) (INFERRED), ? (len) (INFERRED), ? (walk_source_files) (INFERRED), ? (list) (INFERRED), ? (LadybugStore) (INFERRED), ? (repo_root.resolve) (INFERRED), _load_chunks_from_store (DIRECT), _load_chunks_from_store (DIRECT), _load_chunks_from_store (DIRECT)

### _load_chunks_from_store (function, L260-L282)

> *Summary: Retrieves all `Chunk` records associated with a specific file path from the `LadybugStore` using a Cypher query. It maps the database result rows into a list of `Chunk` objects.*

> **Calls:** ? (ChunkType) (INFERRED), ? (Chunk) (INFERRED), ? (chunks.append) (INFERRED), ? (store.conn.execute) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| run_index | file_content_hash | DIRECT | L97 |
| file_content_hash | ? (blake2b) | INFERRED | L29 |
| file_content_hash | ? (hashlib.blake2b(content, digest_size=32).hexdigest) | INFERRED | L29 |
| file_content_hash | ? (filepath.read_bytes) | INFERRED | L28 |
| run_index | IndexResult | DIRECT | L65 |
| run_index | ? (progress.print_summary) | INFERRED | L249 |
| run_index | ? (progress.finish) | INFERRED | L248 |
| run_index | ? (md_path.unlink) | INFERRED | L244 |
| run_index | ? (md_path.exists) | INFERRED | L243 |
| run_index | ? (Path) | INFERRED | L242 |
| run_index | ? (Path(path_to_delete).with_suffix) | INFERRED | L242 |
| run_index | ? (store.delete_file) | INFERRED | L240 |
| run_index | ? (store.delete_relationships) | INFERRED | L239 |
| run_index | ? (set) | INFERRED | L235 |
| run_index | ? (set) | INFERRED | L235 |
| run_index | ? (write_markdown) | INFERRED | L232 |
| run_index | ? (all_rels.append) | INFERRED | L219 |
| run_index | ? (list) | INFERRED | L217 |
| run_index | ? (store.conn.execute) | INFERRED | L213 |
| run_index | ? (store.get_incoming_relationships) | INFERRED | L209 |
| run_index | ? (store.get_file_relationships) | INFERRED | L205 |
| run_index | ? (hasattr) | INFERRED | L200 |
| run_index | ? (store.get_chunks_for_file) | INFERRED | L200 |
| run_index | ? (filepath.relative_to) | INFERRED | L195 |
| run_index | ? (str) | INFERRED | L195 |
| run_index | ? (Language) | INFERRED | L194 |
| run_index | ? (dependent_paths.add) | INFERRED | L187 |
| run_index | ? (list) | INFERRED | L185 |
| run_index | ? (store.conn.execute) | INFERRED | L181 |
| run_index | ? (store.get_incoming_relationships) | INFERRED | L178 |
| run_index | ? (hasattr) | INFERRED | L176 |
| run_index | ? (store.get_chunks_for_file) | INFERRED | L176 |
| run_index | ? (set) | INFERRED | L174 |
| run_index | ? (write_markdown) | INFERRED | L170 |
| run_index | ? (store.get_file_relationships) | INFERRED | L169 |
| run_index | ? (len) | INFERRED | L166 |
| run_index | ? (store.upsert_relationships) | INFERRED | L165 |
| run_index | ? (extract_relationships) | INFERRED | L164 |
| run_index | ? (hasattr) | INFERRED | L159 |
| run_index | ? (store.get_chunks_for_file) | INFERRED | L159 |
| run_index | ? (filepath.relative_to) | INFERRED | L152 |
| run_index | ? (str) | INFERRED | L152 |
| run_index | ? (Language) | INFERRED | L151 |
| run_index | ? (progress.console.print) | INFERRED | L148 |
| run_index | ? (progress.advance) | INFERRED | L144 |
| run_index | ? (len) | INFERRED | L141 |
| run_index | ? (write_markdown) | INFERRED | L134 |
| run_index | ? (store.upsert_chunks) | INFERRED | L130 |
| run_index | ? (store.upsert_file) | INFERRED | L129 |
| run_index | ? (len) | INFERRED | L127 |
| run_index | ? (now) | INFERRED | L126 |
| run_index | ? (datetime.now(timezone.utc).isoformat) | INFERRED | L126 |
| run_index | ? (FileRecord) | INFERRED | L122 |
| run_index | ? (attach_comments) | INFERRED | L119 |
| run_index | ? (extract_chunks) | INFERRED | L116 |
| run_index | ? (changed_relative_paths.add) | INFERRED | L113 |
| run_index | ? (progress.advance) | INFERRED | L108 |
| run_index | ? (indexed_files.get) | INFERRED | L104 |
| run_index | ? (progress.advance) | INFERRED | L100 |
| run_index | ? (filepath.relative_to) | INFERRED | L93 |
| run_index | ? (str) | INFERRED | L93 |
| run_index | ? (Language) | INFERRED | L92 |
| run_index | ? (set) | INFERRED | L88 |
| run_index | ? (f.relative_to) | INFERRED | L85 |
| run_index | ? (str) | INFERRED | L85 |
| run_index | ? (indexed_files.keys) | INFERRED | L84 |
| run_index | ? (set) | INFERRED | L84 |
| run_index | ? (store.get_indexed_files) | INFERRED | L83 |
| run_index | ? (progress.start) | INFERRED | L80 |
| run_index | ? (len) | INFERRED | L77 |
| run_index | ? (walk_source_files) | INFERRED | L76 |
| run_index | ? (list) | INFERRED | L76 |
| run_index | ? (LadybugStore) | INFERRED | L70 |
| run_index | ? (repo_root.resolve) | INFERRED | L64 |
| _load_chunks_from_store | ? (ChunkType) | INFERRED | L277 |
| _load_chunks_from_store | ? (Chunk) | INFERRED | L276 |
| _load_chunks_from_store | ? (chunks.append) | INFERRED | L276 |
| _load_chunks_from_store | ? (store.conn.execute) | INFERRED | L270 |
| run_index | _load_chunks_from_store | DIRECT | L200 |
| run_index | _load_chunks_from_store | DIRECT | L176 |
| run_index | _load_chunks_from_store | DIRECT | L159 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.index.writer | INFERRED |
| glma.index.walker | INFERRED |
| glma.index.relationships | INFERRED |
| glma.index.progress | INFERRED |
| glma.index.detector | INFERRED |
| glma.index.comments | INFERRED |
| glma.index.chunks | INFERRED |
| glma.db.ladybug_store | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| datetime | INFERRED |
| datetime | INFERRED |
| hashlib | INFERRED |
