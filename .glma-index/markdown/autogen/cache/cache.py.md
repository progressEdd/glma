# autogen/cache/cache.py

1 class(es): Cache. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Cache | class |  |

## Chunks

### Cache (class, L19-L203)

> *Summary: This class acts as a unified wrapper for managing various underlying cache implementations (Redis, Disk, Cosmos DB). It initializes the appropriate cache instance based on configuration provided via static factory methods and exposes standard `get`/`set` operations while supporting context management.*


### redis (method, L41-L51, parent: Cache)

> *Summary: Instantiates a `Cache` object specifically configured to use Redis as its backend. It accepts an optional seed and the connection URL for the Redis server.*


### disk (method, L54-L64, parent: Cache)

> *Summary: Instantiates a `Cache` object specifically designed for disk storage by accepting an optional seed and a root directory path. It returns the configured `Cache` instance ready to use file-based caching.*


### cosmos_db (method, L67-L90, parent: Cache)

> *Summary: This function initializes and returns a `Cache` object configured to use Cosmos DB for storage. It accepts connection details, container ID, a cache seed, and an optional pre-existing client to establish the database connection.*


### __init__ (method, L92-L117, parent: Cache)

> *Summary: Initializes a cache object by validating an input configuration dictionary against allowed keys and ensuring the `cache_seed` is stored as a string. It then constructs and assigns the actual cache instance using a factory based on the provided configuration parameters like Redis URL or file paths.*


### __enter__ (method, L119-L130, parent: Cache)

> *Summary: When entering a context, it saves the existing global cache state and sets the current instance as the active one within the system's registry. It then delegates to the underlying cache object's entry logic and returns itself for use inside the `with` block.*


### __exit__ (method, L132-L160, parent: Cache)

> *Summary: When exiting its runtime context, this method first calls the underlying cache's exit logic and then attempts to restore a global context variable using a stored token or previous state if an error occurs during restoration. It propagates any exceptions encountered within the managed block.*


### get (method, L162-L173, parent: Cache)

> *Summary: Retrieves a cached item using a specified string key; it returns the stored value or an optional provided default if the key is absent.*


### set (method, L175-L182, parent: Cache)

> *Summary: Stores a given `value` associated with a specific string `key` within the internal cache structure. This method directly delegates the storage operation to the underlying cache object.*


### close (method, L184-L189, parent: Cache)

> *Summary: This method ensures proper resource management by calling the `close()` method on the internal cache object. It performs necessary cleanup operations to release held resources when the cache instance is shut down.*


### get_current_cache (method, L192-L203, parent: Cache)

> *Summary: Retrieves the active cache object, either by accepting a provided `Cache` instance or by attempting to fetch it from a thread-local storage mechanism (`cls._current_cache`). If fetching fails due to no registered cache, it returns `None`.*

