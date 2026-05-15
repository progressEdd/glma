# autogen/beta/knowledge/redis.py

1 class(es): RedisKnowledgeStore. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RedisKnowledgeStore | class |  |

## Chunks

### RedisKnowledgeStore (class, L18-L172)

> *Summary: This class implements a knowledge store backed by Redis, using string keys for data and a sorted set to maintain version rankings across paths. It provides asynchronous methods to read, write, delete, and list content under specific paths, while also supporting change notifications via polling.*


### __init__ (method, L37-L55, parent: RedisKnowledgeStore)

> *Summary: Initializes a Redis knowledge store by establishing a connection either from a provided URL string or an existing client object. It configures the storage with a specific key prefix, polling interval, and sets up an asynchronous lock for thread safety.*


### _key (method, L57-L58, parent: RedisKnowledgeStore)

> *Summary: Constructs a unique Redis key by prepending a configured prefix to the normalized input path. This method ensures all stored data is namespaced under the instance's defined key prefix.*


### _index_add (method, L60-L61, parent: RedisKnowledgeStore)

> *Summary: Adds a member to a sorted set within Redis using the provided string and integer score. This operation updates or inserts an entry into the index key based on its normalized form and version number.*


### _index_remove (method, L63-L65, parent: RedisKnowledgeStore)

> *Summary: Removes specified paths from a Redis sorted set index using the client's `zrem` command. It accepts a variable number of path strings as input and returns nothing upon successful execution.*


### _index_scan (method, L67-L75, parent: RedisKnowledgeStore)

> *Summary: Retrieves all members and their associated scores from a Redis sorted set identified by `self._index_key`. It decodes byte paths to strings and returns a dictionary mapping each path to its integer score.*


### read (method, L77-L81, parent: RedisKnowledgeStore)

> *Summary: Retrieves a stored string value from Redis using a provided path key. It queries the underlying client and decodes the retrieved byte value to UTF-8 before returning it or `None` if no data is found.*


### write (method, L83-L88, parent: RedisKnowledgeStore)

> *Summary: This method persists string content to a Redis key identified by the provided path after normalizing the path and acquiring a lock. It atomically increments a global version counter before storing the encoded content and updating an index with the new version.*


### list (method, L90-L102, parent: RedisKnowledgeStore)

> *Summary: Retrieves a list of immediate children for a given path by scanning the entire index snapshot. It filters entries matching the specified prefix and extracts the first-level directory names or keys under that path, returning them as a sorted list of strings.*


### delete (method, L104-L115, parent: RedisKnowledgeStore)

> *Summary: Removes an entry and all its descendants from the knowledge base by first scanning the current index, identifying matching paths, deleting the corresponding keys from Redis, and finally removing the path entries from the internal index. It takes a string `path` as input and returns nothing upon successful deletion.*


### exists (method, L117-L123, parent: RedisKnowledgeStore)

> *Summary: Checks if a given path exists within the knowledge store by first querying Redis; if not found, it scans an index to see if any stored paths begin with the specified prefix. Returns `True` if the path or any related entry is present, and `False` otherwise.*


### append (method, L125-L138, parent: RedisKnowledgeStore)

> *Summary: This method appends new content to an existing string stored in Redis under a specified path. It retrieves the current content, calculates the starting offset, combines it with the input payload, updates the value in Redis, and increments a global version counter before returning the original length of the stored data.*


### read_range (method, L140-L148, parent: RedisKnowledgeStore)

> *Summary: Retrieves a substring from stored data identified by a path. It fetches the entire value associated with the key, handles byte/string encoding, and returns the slice between the specified start and end indices as a UTF-8 string.*


### list_versions_under (method, L150-L156, parent: RedisKnowledgeStore)

> *Summary: Retrieves version counts from an index scan based on a provided prefix. It filters the entire snapshot to return only entries matching the exact prefix or those starting with it.*


### on_change (method, L158-L166, parent: RedisKnowledgeStore)

> *Summary: Initiates a background polling mechanism to monitor changes within a specified file path. It returns a subscription object that manages the ongoing change watching process using a provided callback function.*


### close (method, L168-L172, parent: RedisKnowledgeStore)

> *Summary: This method asynchronously closes the internal Redis client if this object is responsible for managing it. It safely attempts to call `aclose()` on the underlying client, suppressing any exceptions during the process.*

