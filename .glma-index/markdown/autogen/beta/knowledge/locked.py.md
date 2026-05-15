# autogen/beta/knowledge/locked.py

1 class(es): LockedKnowledgeStore. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LockedKnowledgeStore | class |  |

## Chunks

### LockedKnowledgeStore (class, L10-L61)

> *Summary: This wrapper ensures thread-safe access to an underlying `KnowledgeStore` by using a provided lock mechanism. It allows concurrent reads but serializes all write, delete, and append operations by acquiring specific locks before execution.*


### __init__ (method, L17-L19, parent: LockedKnowledgeStore)

> *Summary: Initializes the object by storing a reference to a `KnowledgeStore` and an external synchronization `lock`. This sets up the necessary components for thread-safe knowledge management operations.*


### read (method, L21-L22, parent: LockedKnowledgeStore)

> *Summary: Retrieves the content of a file specified by `path` from the underlying store asynchronously. It returns the file's content as a string or `None` if not found.*


### write (method, L24-L31, parent: LockedKnowledgeStore)

> *Summary: This method ensures exclusive access to a storage location before writing data. It attempts to acquire a time-limited lock for the given path and content; if successful, it writes the content using the underlying store and guarantees the lock is released afterward.*


### list (method, L33-L34, parent: LockedKnowledgeStore)

> *Summary: Retrieves a list of file or directory names from the underlying storage at a specified path. It asynchronously calls the store's listing method and returns the resulting list of strings.*


### delete (method, L36-L43, parent: LockedKnowledgeStore)

> *Summary: This method safely removes a specified path from the store by first acquiring an exclusive write lock on that path for 30 seconds. It executes the deletion operation within a `try...finally` block to guarantee the lock is released afterward, even if errors occur.*


### exists (method, L45-L46, parent: LockedKnowledgeStore)

> *Summary: Checks for the existence of a given file path within the underlying storage mechanism and returns a boolean indicating its presence.*


### append (method, L48-L55, parent: LockedKnowledgeStore)

> *Summary: This method safely appends content to a specified path within the store by first acquiring an exclusive lock for that path. It returns the result of the append operation only after ensuring the lock is released, even if errors occur.*


### read_range (method, L57-L58, parent: LockedKnowledgeStore)

> *Summary: Retrieves a segment of data from a specified file path within the knowledge store. It accepts the path and optional start/end indices to return the requested string content.*


### on_change (method, L60-L61, parent: LockedKnowledgeStore)

> *Summary: This method subscribes to changes within a specified file path by delegating the request to an underlying store object. It returns a subscription handle that allows for later cancellation of the change notification.*

