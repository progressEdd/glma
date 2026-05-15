# autogen/beta/knowledge/sqlite.py

1 class(es): SqliteKnowledgeStore. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SqliteKnowledgeStore | class |  |

## Chunks

### SqliteKnowledgeStore (class, L18-L229)

> *Summary: This class provides a persistent, file-backed knowledge store using SQLite to manage path content and versions. It exposes asynchronous methods for reading, writing, listing, deleting, and appending data, ensuring thread safety by running blocking database operations in an executor. Change detection is implemented via polling at a configurable interval.*


### __init__ (method, L41-L51, parent: SqliteKnowledgeStore)

> *Summary: Initializes a SQLite database handler, storing the file path and a polling interval for monitoring changes. It sets up internal state including an asynchronous lock and a version counter to manage concurrent access and data integrity.*


### _ensure_connected (method, L53-L72, parent: SqliteKnowledgeStore)

> *Summary: This method establishes or retrieves an existing SQLite database connection, ensuring the necessary `entries` table exists upon first use. It also initializes and returns the connection object along with setting an internal version counter based on the maximum version found in the table.*


### _next_version (method, L74-L76, parent: SqliteKnowledgeStore)

> *Summary: Increments an internal version counter and returns the new value. This method is used to generate a sequential, unique identifier for knowledge artifacts.*


### _run (method, L78-L80, parent: SqliteKnowledgeStore)

> *Summary: Executes a synchronous callable function in a separate thread using the current event loop's executor. This allows blocking operations to run without stalling the main asynchronous flow.*


### _sync_read (method, L82-L88, parent: SqliteKnowledgeStore)

> *Summary: Retrieves the stored text content from an SQLite database given a normalized file path string. It establishes a connection, executes a `SELECT` query against the `entries` table, and returns the decoded content or `None` if no matching entry is found.*


### _sync_write (method, L90-L96, parent: SqliteKnowledgeStore)

> *Summary: This method synchronously writes or updates a knowledge entry in the SQLite database. It takes a normalized path string, byte payload, and an integer version as input, persisting them to the `entries` table upon successful execution.*


### _sync_list (method, L98-L111, parent: SqliteKnowledgeStore)

> *Summary: Retrieves and returns a sorted list of immediate children paths from the SQLite database, given a specified prefix. It queries entries matching the prefix and extracts the first segment following that prefix to determine the child names.*


### _sync_delete (method, L113-L117, parent: SqliteKnowledgeStore)

> *Summary: This method removes database entries matching a specific normalized path and any paths starting with a given prefix. It ensures the connection is active, executes two `DELETE` queries against the `entries` table, and commits the changes.*


### _sync_exists (method, L119-L128, parent: SqliteKnowledgeStore)

> *Summary: Checks if a given normalized path exists in the database, first by exact match and then by prefix matching against existing entries. Returns `True` if either an exact or prefixed entry is found, otherwise returns `False`.*


### _sync_append (method, L130-L142, parent: SqliteKnowledgeStore)

> *Summary: This method retrieves the current content for a given normalized path from SQLite, appends new payload data to it, and then atomically updates or inserts the combined content back into the database. It returns the original length of the existing content before appending.*


### _sync_read_range (method, L144-L154, parent: SqliteKnowledgeStore)

> *Summary: Retrieves a specific byte range from an SQLite entry identified by its normalized path. It queries the database for the content, and if found, returns the requested substring decoded as UTF-8, respecting provided start and end indices.*


### _sync_list_versions (method, L156-L165, parent: SqliteKnowledgeStore)

> *Summary: Retrieves the versions associated with a given file path from an SQLite database connection. It queries entries matching the exact path or any subpaths if the input is not empty or just a slash.*


### read (method, L167-L169, parent: SqliteKnowledgeStore)

> *Summary: Retrieves the content of a file specified by `path` after normalizing it. It executes the synchronous read operation asynchronously and returns the file's content as a string or `None`.*


### write (method, L171-L176, parent: SqliteKnowledgeStore)

> *Summary: This method asynchronously writes string content to a specified file path after normalizing the path and encoding the content to UTF-8 bytes. It acquires an internal lock before executing a synchronous write operation with an incremented version number.*


### list (method, L178-L180, parent: SqliteKnowledgeStore)

> *Summary: Retrieves a list of directory entries starting from the specified `path`. It normalizes the input path and asynchronously executes a synchronous listing operation to return a list of strings.*


### delete (method, L182-L186, parent: SqliteKnowledgeStore)

> *Summary: Removes a specified directory and its contents from the knowledge base using an asynchronous lock to ensure thread safety. It first normalizes the input path and constructs a directory prefix before executing the deletion operation.*


### exists (method, L188-L191, parent: SqliteKnowledgeStore)

> *Summary: Checks for the existence of a given file or directory path by first normalizing it and then querying the underlying SQLite database asynchronously. It returns `True` if the path exists according to the stored knowledge, otherwise `False`.*


### append (method, L193-L198, parent: SqliteKnowledgeStore)

> *Summary: This method asynchronously appends string content to a specified file path after normalizing the path and encoding the content. It acquires a lock, generates a new version number, and then executes a synchronous append operation in the background.*


### read_range (method, L200-L202, parent: SqliteKnowledgeStore)

> *Summary: Asynchronously reads a specified range of content from a SQLite database file path. It takes the file path and optional start/end indices as input and returns the requested string segment.*


### list_versions_under (method, L204-L213, parent: SqliteKnowledgeStore)

> *Summary: Retrieves a dictionary mapping paths to their version numbers for all keys located under a specified prefix. This method is designed to efficiently calculate differences between data snapshots by returning the current monotonic version for each relevant key.*


### on_change (method, L215-L223, parent: SqliteKnowledgeStore)

> *Summary: Initiates file system monitoring for a given path using a polling mechanism. It returns a subscription object that allows the caller to manage the ongoing change detection process.*


### close (method, L225-L229, parent: SqliteKnowledgeStore)

> *Summary: Safely terminates the underlying SQLite database connection if it exists, ensuring the operation is idempotent and handles potential closing errors gracefully.*

