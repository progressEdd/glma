---
file_path: watch.py
language: python
last_indexed: 2026-04-13T20:15:23.083140+00:00
chunk_count: 4
content_hash: a6d0048177e6951a17872ec2477fb4ed46a0b40322d3581b7569644b71f43d05
---

# watch.py

## Summary

Monitors a repository for filesystem changes using `watchfiles` to trigger incremental re-indexing of supported language files. It processes event tuples to detect creations, modifications, deletions, and renames, updating the index accordingly based on provided configuration.

**AI Chunk Summaries:**
- **_classify_events**: Categorizes a set of `watchfiles` event tuples into three distinct sets based on the change type. It takes `(Change, str)` pairs as input and returns a tuple containing sets of `Path` objects for created, modified, and deleted files.
- **_detect_renames**: Identifies file renames by matching the basenames of newly created and recently deleted paths. It returns a list of mapped rename pairs along with the sets of unmatched created and deleted files.
- **_is_supported_file**: Determines if a file should be indexed by detecting its language and validating it against the `Language` model. It returns `True` if the file's detected language is supported, otherwise returning `False`.
- **watch_and_index**: Monitors a repository for file system changes and triggers incremental re-indexing based on provided configuration. It filters events by supported file types, detects renames, and calls `run_index` to update the database with modified or deleted paths.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| _classify_events | function | L21-L43 |  |
| _detect_renames | function | L46-L82 |  |
| _is_supported_file | function | L85-L105 |  |
| watch_and_index | function | L108-L236 |  |

## Chunks

### _classify_events (function, L21-L43)

> *Summary: Categorizes a set of `watchfiles` event tuples into three distinct sets based on the change type. It takes `(Change, str)` pairs as input and returns a tuple containing sets of `Path` objects for created, modified, and deleted files.*

> **Calls:** ? (glma.index.progress) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.index.pipeline) (INFERRED), ? (glma.index.detector) (INFERRED), ? (glma.db.ladybug_store) (INFERRED), ? (glma.config) (INFERRED), ? (watchfiles) (INFERRED), ? (watchfiles) (INFERRED), ? (rich.console) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED), ? (datetime) (INFERRED), ? (datetime) (INFERRED), ? (logging) (INFERRED), ? (asyncio) (INFERRED), ? (deleted.add) (INFERRED), ? (modified.add) (INFERRED), ? (created.add) (INFERRED), ? (Path) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED)

### _detect_renames (function, L46-L82)

> *Summary: Identifies file renames by matching the basenames of newly created and recently deleted paths. It returns a list of mapped rename pairs along with the sets of unmatched created and deleted files.*

> **Calls:** ? (used_deleted.add) (INFERRED), ? (used_created.add) (INFERRED), ? (renames.append) (INFERRED), ? (set) (INFERRED), ? (set) (INFERRED)

### _is_supported_file (function, L85-L105)

> *Summary: Determines if a file should be indexed by detecting its language and validating it against the `Language` model. It returns `True` if the file's detected language is supported, otherwise returning `False`.*

> **Calls:** ? (Language) (INFERRED), ? (detect_language) (INFERRED)

### watch_and_index (function, L108-L236)

> *Summary: Monitors a repository for file system changes and triggers incremental re-indexing based on provided configuration. It filters events by supported file types, detects renames, and calls `run_index` to update the database with modified or deleted paths.*

> **Calls:** _classify_events (DIRECT), _detect_renames (DIRECT), _is_supported_file (DIRECT), ? (console.print) (INFERRED), ? (logger.exception) (INFERRED), ? (console.print) (INFERRED), ? (console.print) (INFERRED), ? (run_index) (INFERRED), ? (IndexProgress) (INFERRED), ? (console.print) (INFERRED), ? (len) (INFERRED), ? (len) (INFERRED), ? (now) (INFERRED), ? (datetime.now().strftime) (INFERRED), ? (deleted_rel_paths.extend) (INFERRED), ? (now) (INFERRED), ? (datetime.now().strftime) (INFERRED), ? (console.print) (INFERRED), ? (deleted_rel_paths.append) (INFERRED), ? (path.relative_to) (INFERRED), ? (str) (INFERRED), ? (path.relative_to) (INFERRED), ? (now) (INFERRED), ? (datetime.now().strftime) (INFERRED), ? (console.print) (INFERRED), ? (changed_files.append) (INFERRED), ? (detect_language) (INFERRED), ? (path.relative_to) (INFERRED), ? (now) (INFERRED), ? (datetime.now().strftime) (INFERRED), ? (console.print) (INFERRED), ? (changed_files.append) (INFERRED), ? (detect_language) (INFERRED), ? (new_path.relative_to) (INFERRED), ? (now) (INFERRED), ? (datetime.now().strftime) (INFERRED), ? (console.print) (INFERRED), ? (changed_files.append) (INFERRED), ? (detect_language) (INFERRED), ? (rename_deleted_paths.append) (INFERRED), ? (old_path.relative_to) (INFERRED), ? (str) (INFERRED), ? (filtered_changes.add) (INFERRED), ? (any) (INFERRED), ? (path.relative_to) (INFERRED), ? (Path) (INFERRED), ? (set) (INFERRED), ? (awatch) (INFERRED), ? (console.print) (INFERRED), ? (console.print) (INFERRED), ? (console.print) (INFERRED), ? (console.print) (INFERRED), ? (LadybugStore) (INFERRED), ? (Console) (INFERRED)

## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| watch_and_index | _classify_events | DIRECT | L155 |
| _classify_events | ? (deleted.add) | INFERRED | L41 |
| _classify_events | ? (modified.add) | INFERRED | L39 |
| _classify_events | ? (created.add) | INFERRED | L37 |
| _classify_events | ? (Path) | INFERRED | L35 |
| _classify_events | ? (set) | INFERRED | L32 |
| _classify_events | ? (set) | INFERRED | L31 |
| _classify_events | ? (set) | INFERRED | L30 |
| watch_and_index | _detect_renames | DIRECT | L158 |
| _detect_renames | ? (used_deleted.add) | INFERRED | L75 |
| _detect_renames | ? (used_created.add) | INFERRED | L74 |
| _detect_renames | ? (renames.append) | INFERRED | L73 |
| _detect_renames | ? (set) | INFERRED | L65 |
| _detect_renames | ? (set) | INFERRED | L64 |
| watch_and_index | _is_supported_file | DIRECT | L148 |
| _is_supported_file | ? (Language) | INFERRED | L102 |
| _is_supported_file | ? (detect_language) | INFERRED | L98 |
| watch_and_index | ? (console.print) | INFERRED | L236 |
| watch_and_index | ? (logger.exception) | INFERRED | L233 |
| watch_and_index | ? (console.print) | INFERRED | L232 |
| watch_and_index | ? (console.print) | INFERRED | L230 |
| watch_and_index | ? (run_index) | INFERRED | L222 |
| watch_and_index | ? (IndexProgress) | INFERRED | L221 |
| watch_and_index | ? (console.print) | INFERRED | L217 |
| watch_and_index | ? (len) | INFERRED | L216 |
| watch_and_index | ? (len) | INFERRED | L216 |
| watch_and_index | ? (now) | INFERRED | L215 |
| watch_and_index | ? (datetime.now().strftime) | INFERRED | L215 |
| watch_and_index | ? (deleted_rel_paths.extend) | INFERRED | L209 |
| watch_and_index | ? (now) | INFERRED | L206 |
| watch_and_index | ? (datetime.now().strftime) | INFERRED | L206 |
| watch_and_index | ? (console.print) | INFERRED | L205 |
| watch_and_index | ? (deleted_rel_paths.append) | INFERRED | L203 |
| watch_and_index | ? (path.relative_to) | INFERRED | L202 |
| watch_and_index | ? (str) | INFERRED | L202 |
| watch_and_index | ? (path.relative_to) | INFERRED | L196 |
| watch_and_index | ? (now) | INFERRED | L195 |
| watch_and_index | ? (datetime.now().strftime) | INFERRED | L195 |
| watch_and_index | ? (console.print) | INFERRED | L194 |
| watch_and_index | ? (changed_files.append) | INFERRED | L192 |
| watch_and_index | ? (detect_language) | INFERRED | L190 |
| watch_and_index | ? (path.relative_to) | INFERRED | L185 |
| watch_and_index | ? (now) | INFERRED | L184 |
| watch_and_index | ? (datetime.now().strftime) | INFERRED | L184 |
| watch_and_index | ? (console.print) | INFERRED | L183 |
| watch_and_index | ? (changed_files.append) | INFERRED | L181 |
| watch_and_index | ? (detect_language) | INFERRED | L179 |
| watch_and_index | ? (new_path.relative_to) | INFERRED | L174 |
| watch_and_index | ? (now) | INFERRED | L173 |
| watch_and_index | ? (datetime.now().strftime) | INFERRED | L173 |
| watch_and_index | ? (console.print) | INFERRED | L172 |
| watch_and_index | ? (changed_files.append) | INFERRED | L170 |
| watch_and_index | ? (detect_language) | INFERRED | L168 |
| watch_and_index | ? (rename_deleted_paths.append) | INFERRED | L167 |
| watch_and_index | ? (old_path.relative_to) | INFERRED | L166 |
| watch_and_index | ? (str) | INFERRED | L166 |
| watch_and_index | ? (filtered_changes.add) | INFERRED | L150 |
| watch_and_index | ? (any) | INFERRED | L144 |
| watch_and_index | ? (path.relative_to) | INFERRED | L142 |
| watch_and_index | ? (Path) | INFERRED | L140 |
| watch_and_index | ? (set) | INFERRED | L138 |
| watch_and_index | ? (awatch) | INFERRED | L136 |
| watch_and_index | ? (console.print) | INFERRED | L133 |
| watch_and_index | ? (console.print) | INFERRED | L132 |
| watch_and_index | ? (console.print) | INFERRED | L131 |
| watch_and_index | ? (console.print) | INFERRED | L130 |
| watch_and_index | ? (LadybugStore) | INFERRED | L128 |
| watch_and_index | ? (Console) | INFERRED | L125 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.index.progress | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.index.pipeline | INFERRED |
| glma.index.detector | INFERRED |
| glma.db.ladybug_store | INFERRED |
| glma.config | INFERRED |
| watchfiles | INFERRED |
| watchfiles | INFERRED |
| rich.console | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
| datetime | INFERRED |
| datetime | INFERRED |
| logging | INFERRED |
| asyncio | INFERRED |
