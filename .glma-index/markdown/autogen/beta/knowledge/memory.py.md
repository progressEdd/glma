# autogen/beta/knowledge/memory.py

2 class(es): _MemoryChangeSubscription, MemoryKnowledgeStore. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _MemoryChangeSubscription | class |  |
| MemoryKnowledgeStore | class |  |

## Chunks

### _MemoryChangeSubscription (class, L11-L26)

> *Summary: This class manages a subscription to changes within a knowledge store for a specific key. It allows an asynchronous `close` method to safely unsubscribe the associated callback from the relevant subscriber list and clean up the key's entry if necessary.*


### __init__ (method, L14-L17, parent: _MemoryChangeSubscription)

> *Summary: Initializes a memory object by storing a dictionary of change subscribers, a unique string key, and a specific callback function. This sets up the necessary components for tracking changes associated with the given key.*


### close (method, L19-L26, parent: _MemoryChangeSubscription)

> *Summary: This method unsubscribes the instance's callback from its associated subscriber bucket within the internal subscription map. It safely removes the callback and cleans up the entry in the subscribers dictionary if the bucket becomes empty.*


### MemoryKnowledgeStore (class, L29-L112)

> *Summary: This class implements an in-memory key-value store using a dictionary to manage knowledge paths and their content. It provides asynchronous methods for reading, writing, listing directory contents, deleting entries, checking existence, appending data, and subscribing callbacks to path changes.*


### __init__ (method, L36-L39, parent: MemoryKnowledgeStore)

> *Summary: Initializes a memory object by setting up an internal dictionary for storing key-value data, an `asyncio.Lock` to manage concurrent access, and a structure to track subscribers interested in data changes.*


### read (method, L41-L42, parent: MemoryKnowledgeStore)

> *Summary: Retrieves stored data associated with a given file path key from the internal data store. It returns the corresponding string value or `None` if no entry exists for that normalized path.*


### write (method, L44-L47, parent: MemoryKnowledgeStore)

> *Summary: Stores provided string content under a normalized file path within the internal data structure and then asynchronously notifies listeners about the update.*


### list (method, L49-L61, parent: MemoryKnowledgeStore)

> *Summary: Retrieves a list of immediate subdirectories or files located under a specified path within the stored data structure. It processes all keys in the internal data, filters those matching the given prefix, and returns a sorted set of the first-level components found beneath that path.*


### delete (method, L63-L74, parent: MemoryKnowledgeStore)

> *Summary: Removes a specified knowledge path and all its descendants from the internal data store. It normalizes the input path, deletes the entry if it exists, then iterates through and removes any keys starting with that path's prefix before notifying listeners of all affected keys.*


### exists (method, L76-L81, parent: MemoryKnowledgeStore)

> *Summary: Checks if a given file path exists within the stored data by first checking for an exact match, and then iterating through all keys to see if any start with the path as a prefix. Returns `True` if the path or any descendant is present, otherwise returns `False`.*


### append (method, L83-L90, parent: MemoryKnowledgeStore)

> *Summary: This method asynchronously appends new string content to an existing stored value associated with a given path, returning the byte offset of the original data. It ensures thread safety using a lock before modifying the internal data structure and notifies listeners upon completion.*


### read_range (method, L92-L101, parent: MemoryKnowledgeStore)

> *Summary: Retrieves a substring from stored data identified by a path. It takes the file path, a starting index, and an optional ending index as input, returning the requested segment as a UTF-8 decoded string or an empty string if not found or invalid.*


### on_change (method, L103-L106, parent: MemoryKnowledgeStore)

> *Summary: Registers a callback function to be notified when changes occur at a specific file path. It normalizes the input path and returns a subscription object allowing the caller to later unsubscribe from notifications.*


### _notify (method, L108-L112, parent: MemoryKnowledgeStore)

> *Summary: This method asynchronously notifies all registered subscribers when a specific file path changes. It iterates through subscriptions, triggering callbacks for any paths that exactly match or are descendants of the reported `changed_path`.*

