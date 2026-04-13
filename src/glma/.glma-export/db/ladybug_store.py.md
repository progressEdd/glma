---
file_path: db/ladybug_store.py
language: python
last_indexed: 2026-04-13T20:15:23.395466+00:00
chunk_count: 20
content_hash: 52a262f91535245515590a26a3e5d11f61bc3c13f120113c36ac240f7d888376
---

# db/ladybug_store.py

## Summary

Provides a graph database interface for indexing code files and chunks, managing their metadata, AI summaries, and inter-relationships via Cypher queries. It supports CRUD operations for file/chunk records and implements complex relationship retrieval through BFS traversals.

**AI Chunk Summaries:**
- **LadybugStore**: Manages a graph database for storing and querying code index data, including files, chunks, and their inter-relationships. It provides methods to upsert records, update AI-generated summaries, and perform BFS traversals of relationships between code chunks.
- **__init__**: Initializes the database store by ensuring the target directory exists and establishing a connection to the provided `db_path`. It concludes by executing `_init_schema()` to ensure all required tables and structures are present.
- **_init_schema**: Initializes the database by executing predefined schema SQL statements to create necessary tables if they do not already exist. It takes no inputs and produces no return value, modifying the connected database state.
- **upsert_file**: Updates or inserts a `FileRecord` into the database by first performing a detach delete of all associated chunks and the existing file node. It then serializes the record's data to create a fresh `File` node with updated metadata.
- **upsert_chunks**: Replaces existing chunks for a given file path with a new list of `Chunk` objects while preserving AI-generated summaries based on content hashes. It deletes old nodes and edges in the database, inserts the updated chunk data, and restores the `:CONTAINS` relationships between the file and its chunks.
- **get_file_hash**: Retrieves the stored `content_hash` for a specific file path from the database. It queries the graph using the provided path and returns the hash string if found, otherwise returning `None`.
- **get_indexed_files**: Retrieves all indexed files from the database using a Cypher query. It returns a dictionary mapping file paths to their corresponding content hashes.
- **delete_file**: Removes a file and all its associated chunks from the database using the provided `file_path`. It executes two Cypher queries to detach and delete related `Chunk` nodes before deleting the corresponding `File` node.
- **update_chunk_summary**: Updates the `summary` property of a specific `Chunk` node in the database using its unique ID. It performs a targeted field update via a Cypher query without modifying other node properties.
- **update_file_summary**: Updates the `file_summary` property of a specific `File` node in the database using its relative path. It takes a file path and a summary string as input and executes a Cypher `SET` operation via the database connection.
- **delete_relationships**: Removes all outgoing `RELATES_TO` relationships from graph nodes labeled as `Chunk` that match the provided `file_path`. It takes a file path string as input and executes a Cypher query to delete these edges.
- **upsert_relationships**: Replaces all existing outgoing relationships for a given file path with a new list of `Relationship` objects. It creates Neo4j edges between chunks if a target ID exists, otherwise it creates a self-referencing edge to mark the relationship as unresolved.
- **get_outgoing_relationships**: Retrieves all outgoing `RELATES_TO` relationships for a given `chunk_id` from the Neo4j database. It returns a list of dictionaries containing relationship metadata (type, confidence, source line) and target chunk details.
- **get_incoming_relationships**: Retrieves all incoming `RELATES_TO` relationships for a specific chunk ID from the Neo4j database. It returns a list of dictionaries containing relationship metadata and source chunk details.
- **get_file_relationships**: Retrieves all outgoing `RELATES_TO` relationships for chunks associated with a given file path from the Neo4j database. It returns a list of dictionaries containing source and target chunk metadata, relationship types, confidence scores, and line numbers.
- **get_file_record**: Retrieves a `FileRecord` from the database using a provided file path. It queries Neo4j for specific file metadata and returns a populated data object if found, otherwise returning `None`.
- **get_chunks_for_file**: Retrieves all `Chunk` objects associated with a given file path from the database. It returns a list of chunks ordered by their starting line number.
- **get_all_relationships_for_file**: Retrieves all outgoing and incoming relationships for every chunk associated with a given file path. It returns a dictionary keyed by `chunk_id` containing lists of edges, specifically filtering out internal file references from the incoming set to avoid duplication.
- **traverse_relationships**: Performs a breadth-first search (BFS) to retrieve all incoming and outgoing relationships starting from a list of chunk IDs up to a specified maximum depth. It returns a list of relationship dictionaries, each augmented with its traversal depth and source/target identifiers.
- **close**: Terminates the database session by deleting the connection and database object references. It takes no inputs and returns nothing.

## Key Exports

| Name | Type | Line Range | Description |
| ---- | ---- | ---------- | ----------- |
| LadybugStore | class | L11-L430 |  |

## Chunks

### LadybugStore (class, L11-L430)

> *Summary: Manages a graph database for storing and querying code index data, including files, chunks, and their inter-relationships. It provides methods to upsert records, update AI-generated summaries, and perform BFS traversals of relationships between code chunks.*

> **Calls:** ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (glma.models) (INFERRED), ? (real_ladybug) (INFERRED), ? (real_ladybug) (INFERRED), ? (typing) (INFERRED), ? (pathlib) (INFERRED)

### __init__ (method, L50-L59)

> *Summary: Initializes the database store by ensuring the target directory exists and establishing a connection to the provided `db_path`. It concludes by executing `_init_schema()` to ensure all required tables and structures are present.*

> **Calls:** ? (Connection) (INFERRED), ? (str) (INFERRED), ? (Database) (INFERRED), ? (db_path.parent.mkdir) (INFERRED), self._init_schema (DIRECT)

### _init_schema (method, L61-L66)

> *Summary: Initializes the database by executing predefined schema SQL statements to create necessary tables if they do not already exist. It takes no inputs and produces no return value, modifying the connected database state.*

> **Calls:** ? (self.conn.execute) (INFERRED), ? (self.conn.execute) (INFERRED), ? (self.conn.execute) (INFERRED), ? (self.conn.execute) (INFERRED)

### upsert_file (method, L68-L93)

> *Summary: Updates or inserts a `FileRecord` into the database by first performing a detach delete of all associated chunks and the existing file node. It then serializes the record's data to create a fresh `File` node with updated metadata.*

> **Calls:** ? (self.conn.execute) (INFERRED), ? (data.get) (INFERRED), ? (record.model_dump) (INFERRED), ? (self.conn.execute) (INFERRED), ? (self.conn.execute) (INFERRED)

### upsert_chunks (method, L95-L144)

> *Summary: Replaces existing chunks for a given file path with a new list of `Chunk` objects while preserving AI-generated summaries based on content hashes. It deletes old nodes and edges in the database, inserts the updated chunk data, and restores the `:CONTAINS` relationships between the file and its chunks.*

> **Calls:** ? (self.conn.execute) (INFERRED), ? (self.conn.execute) (INFERRED), ? (data.get) (INFERRED), ? (data.get) (INFERRED), ? (chunk.model_dump) (INFERRED), ? (self.conn.execute) (INFERRED), self.get_chunks_for_file (DIRECT)

### get_file_hash (method, L146-L153)

> *Summary: Retrieves the stored `content_hash` for a specific file path from the database. It queries the graph using the provided path and returns the hash string if found, otherwise returning `None`.*

> **Calls:** ? (list) (INFERRED), ? (self.conn.execute) (INFERRED)

### get_indexed_files (method, L155-L159)

> *Summary: Retrieves all indexed files from the database using a Cypher query. It returns a dictionary mapping file paths to their corresponding content hashes.*

> **Calls:** ? (list) (INFERRED), ? (self.conn.execute) (INFERRED)

### delete_file (method, L161-L170)

> *Summary: Removes a file and all its associated chunks from the database using the provided `file_path`. It executes two Cypher queries to detach and delete related `Chunk` nodes before deleting the corresponding `File` node.*

> **Calls:** ? (self.conn.execute) (INFERRED), ? (self.conn.execute) (INFERRED)

### update_chunk_summary (method, L172-L184)

> *Summary: Updates the `summary` property of a specific `Chunk` node in the database using its unique ID. It performs a targeted field update via a Cypher query without modifying other node properties.*

> **Calls:** ? (self.conn.execute) (INFERRED)

### update_file_summary (method, L186-L196)

> *Summary: Updates the `file_summary` property of a specific `File` node in the database using its relative path. It takes a file path and a summary string as input and executes a Cypher `SET` operation via the database connection.*

> **Calls:** ? (self.conn.execute) (INFERRED)

### delete_relationships (method, L198-L203)

> *Summary: Removes all outgoing `RELATES_TO` relationships from graph nodes labeled as `Chunk` that match the provided `file_path`. It takes a file path string as input and executes a Cypher query to delete these edges.*

> **Calls:** ? (self.conn.execute) (INFERRED)

### upsert_relationships (method, L205-L234)

> *Summary: Replaces all existing outgoing relationships for a given file path with a new list of `Relationship` objects. It creates Neo4j edges between chunks if a target ID exists, otherwise it creates a self-referencing edge to mark the relationship as unresolved.*

> **Calls:** self.delete_relationships (DIRECT), ? (self.conn.execute) (INFERRED), ? (self.conn.execute) (INFERRED)

### get_outgoing_relationships (method, L236-L248)

> *Summary: Retrieves all outgoing `RELATES_TO` relationships for a given `chunk_id` from the Neo4j database. It returns a list of dictionaries containing relationship metadata (type, confidence, source line) and target chunk details.*

> **Calls:** ? (rows.append) (INFERRED), ? (self.conn.execute) (INFERRED)

### get_incoming_relationships (method, L250-L262)

> *Summary: Retrieves all incoming `RELATES_TO` relationships for a specific chunk ID from the Neo4j database. It returns a list of dictionaries containing relationship metadata and source chunk details.*

> **Calls:** ? (rows.append) (INFERRED), ? (self.conn.execute) (INFERRED)

### get_file_relationships (method, L264-L277)

> *Summary: Retrieves all outgoing `RELATES_TO` relationships for chunks associated with a given file path from the Neo4j database. It returns a list of dictionaries containing source and target chunk metadata, relationship types, confidence scores, and line numbers.*

> **Calls:** ? (rows.append) (INFERRED), ? (self.conn.execute) (INFERRED)

### get_file_record (method, L279-L296)

> *Summary: Retrieves a `FileRecord` from the database using a provided file path. It queries Neo4j for specific file metadata and returns a populated data object if found, otherwise returning `None`.*

> **Calls:** ? (Language) (INFERRED), ? (FileRecord) (INFERRED), ? (list) (INFERRED), ? (self.conn.execute) (INFERRED)

### get_chunks_for_file (method, L298-L315)

> *Summary: Retrieves all `Chunk` objects associated with a given file path from the database. It returns a list of chunks ordered by their starting line number.*

> **Calls:** ? (ChunkType) (INFERRED), ? (Chunk) (INFERRED), ? (chunks.append) (INFERRED), ? (self.conn.execute) (INFERRED)

### get_all_relationships_for_file (method, L317-L371)

> *Summary: Retrieves all outgoing and incoming relationships for every chunk associated with a given file path. It returns a dictionary keyed by `chunk_id` containing lists of edges, specifically filtering out internal file references from the incoming set to avoid duplication.*

> **Calls:** self.get_incoming_relationships (DIRECT), self.get_file_relationships (DIRECT), self.get_chunks_for_file (DIRECT), ? (relationships[chunk.id]["incoming"].append) (INFERRED), ? (list) (INFERRED), ? (self.conn.execute) (INFERRED), ? (relationships[source_id]["outgoing"].append) (INFERRED), ? (relationships[source_id]["outgoing"].append) (INFERRED)

### traverse_relationships (method, L373-L425)

> *Summary: Performs a breadth-first search (BFS) to retrieve all incoming and outgoing relationships starting from a list of chunk IDs up to a specified maximum depth. It returns a list of relationship dictionaries, each augmented with its traversal depth and source/target identifiers.*

> **Calls:** self.get_outgoing_relationships (DIRECT), self.get_incoming_relationships (DIRECT), ? (queue.append) (INFERRED), ? (visited.add) (INFERRED), ? (results.append) (INFERRED), ? (dict) (INFERRED), ? (rel.get) (INFERRED), ? (queue.append) (INFERRED), ? (visited.add) (INFERRED), ? (results.append) (INFERRED), ? (dict) (INFERRED), ? (results.append) (INFERRED), ? (dict) (INFERRED), ? (rel.get) (INFERRED), ? (queue.pop) (INFERRED), ? (set) (INFERRED)

### close (method, L427-L430)

> *Summary: Terminates the database session by deleting the connection and database object references. It takes no inputs and returns nothing.*


## Relationships

### Outgoing Calls

| From | To | Confidence | Line |
| ---- | -- | ---------- | ---- |
| __init__ | ? (Connection) | INFERRED | L58 |
| __init__ | ? (str) | INFERRED | L57 |
| __init__ | ? (Database) | INFERRED | L57 |
| __init__ | ? (db_path.parent.mkdir) | INFERRED | L56 |
| _init_schema | ? (self.conn.execute) | INFERRED | L66 |
| _init_schema | ? (self.conn.execute) | INFERRED | L65 |
| _init_schema | ? (self.conn.execute) | INFERRED | L64 |
| _init_schema | ? (self.conn.execute) | INFERRED | L63 |
| __init__ | _init_schema | DIRECT | L59 |
| upsert_file | ? (self.conn.execute) | INFERRED | L83 |
| upsert_file | ? (data.get) | INFERRED | L82 |
| upsert_file | ? (record.model_dump) | INFERRED | L80 |
| upsert_file | ? (self.conn.execute) | INFERRED | L76 |
| upsert_file | ? (self.conn.execute) | INFERRED | L71 |
| upsert_chunks | ? (self.conn.execute) | INFERRED | L140 |
| upsert_chunks | ? (self.conn.execute) | INFERRED | L123 |
| upsert_chunks | ? (data.get) | INFERRED | L122 |
| upsert_chunks | ? (data.get) | INFERRED | L121 |
| upsert_chunks | ? (chunk.model_dump) | INFERRED | L117 |
| upsert_chunks | ? (self.conn.execute) | INFERRED | L111 |
| get_file_hash | ? (list) | INFERRED | L152 |
| get_file_hash | ? (self.conn.execute) | INFERRED | L148 |
| get_indexed_files | ? (list) | INFERRED | L158 |
| get_indexed_files | ? (self.conn.execute) | INFERRED | L157 |
| delete_file | ? (self.conn.execute) | INFERRED | L167 |
| delete_file | ? (self.conn.execute) | INFERRED | L163 |
| update_chunk_summary | ? (self.conn.execute) | INFERRED | L181 |
| update_file_summary | ? (self.conn.execute) | INFERRED | L193 |
| upsert_relationships | delete_relationships | DIRECT | L207 |
| delete_relationships | ? (self.conn.execute) | INFERRED | L200 |
| upsert_relationships | ? (self.conn.execute) | INFERRED | L224 |
| upsert_relationships | ? (self.conn.execute) | INFERRED | L210 |
| traverse_relationships | get_outgoing_relationships | DIRECT | L393 |
| get_outgoing_relationships | ? (rows.append) | INFERRED | L244 |
| get_outgoing_relationships | ? (self.conn.execute) | INFERRED | L238 |
| traverse_relationships | get_incoming_relationships | DIRECT | L411 |
| get_all_relationships_for_file | get_incoming_relationships | DIRECT | L344 |
| get_incoming_relationships | ? (rows.append) | INFERRED | L258 |
| get_incoming_relationships | ? (self.conn.execute) | INFERRED | L252 |
| get_all_relationships_for_file | get_file_relationships | DIRECT | L326 |
| get_file_relationships | ? (rows.append) | INFERRED | L272 |
| get_file_relationships | ? (self.conn.execute) | INFERRED | L266 |
| get_file_record | ? (Language) | INFERRED | L291 |
| get_file_record | ? (FileRecord) | INFERRED | L289 |
| get_file_record | ? (list) | INFERRED | L285 |
| get_file_record | ? (self.conn.execute) | INFERRED | L281 |
| get_all_relationships_for_file | get_chunks_for_file | DIRECT | L339 |
| get_chunks_for_file | ? (ChunkType) | INFERRED | L310 |
| get_chunks_for_file | ? (Chunk) | INFERRED | L309 |
| get_chunks_for_file | ? (chunks.append) | INFERRED | L309 |
| get_chunks_for_file | ? (self.conn.execute) | INFERRED | L300 |
| upsert_chunks | get_chunks_for_file | DIRECT | L102 |
| get_all_relationships_for_file | ? (relationships[chunk.id]["incoming"].append) | INFERRED | L369 |
| get_all_relationships_for_file | ? (list) | INFERRED | L356 |
| get_all_relationships_for_file | ? (self.conn.execute) | INFERRED | L352 |
| get_all_relationships_for_file | ? (relationships[source_id]["outgoing"].append) | INFERRED | L336 |
| get_all_relationships_for_file | ? (relationships[source_id]["outgoing"].append) | INFERRED | L334 |
| traverse_relationships | ? (queue.append) | INFERRED | L423 |
| traverse_relationships | ? (visited.add) | INFERRED | L422 |
| traverse_relationships | ? (results.append) | INFERRED | L420 |
| traverse_relationships | ? (dict) | INFERRED | L416 |
| traverse_relationships | ? (rel.get) | INFERRED | L412 |
| traverse_relationships | ? (queue.append) | INFERRED | L408 |
| traverse_relationships | ? (visited.add) | INFERRED | L407 |
| traverse_relationships | ? (results.append) | INFERRED | L405 |
| traverse_relationships | ? (dict) | INFERRED | L402 |
| traverse_relationships | ? (results.append) | INFERRED | L400 |
| traverse_relationships | ? (dict) | INFERRED | L397 |
| traverse_relationships | ? (rel.get) | INFERRED | L394 |
| traverse_relationships | ? (queue.pop) | INFERRED | L388 |
| traverse_relationships | ? (set) | INFERRED | L383 |

### Imports

| Import | Confidence |
| ------ | ---------- |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| glma.models | INFERRED |
| real_ladybug | INFERRED |
| real_ladybug | INFERRED |
| typing | INFERRED |
| pathlib | INFERRED |
