# autogen/cache/redis_cache.py

1 class(es): RedisCache. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RedisCache | class |  |

## Chunks

### RedisCache (class, L21-L119)

> *Summary: This class implements a caching mechanism using Redis, requiring a seed/namespace and a Redis connection URL upon initialization. It provides methods to retrieve (`get`) or store (`set`) data, automatically prefixing keys with the provided seed and serializing values using pickle for storage in Redis. The object also supports context management for automatic resource cleanup.*


### __init__ (method, L41-L50, parent: RedisCache)

> *Summary: Initializes a caching mechanism by setting a unique key prefix (`seed`) and establishing a connection to a specified Redis instance via its URL. This object then uses the configured Redis client for all subsequent cache operations.*


### _prefixed_key (method, L52-L61, parent: RedisCache)

> *Summary: This method prepends a namespace, incorporating the system's seed and "autogen:", to an input string. It returns this fully qualified, namespaced key suitable for cache storage.*


### get (method, L63-L77, parent: RedisCache)

> *Summary: Retrieves a cached item using a provided key from Redis, applying a prefix to the key before lookup. If found, it deserializes and returns the stored value; otherwise, it returns the specified default or `None`.*


### set (method, L79-L90, parent: RedisCache)

> *Summary: Stores a given Python object into the Redis cache by first serializing it using `pickle`. It uses a prefixed version of the provided key for storage within the underlying cache instance.*


### close (method, L92-L97, parent: RedisCache)

> *Summary: This method ensures proper resource management by calling `close()` on the underlying Redis client instance. It handles the cleanup of network connections associated with the cache.*


### __enter__ (method, L99-L105, parent: RedisCache)

> *Summary: When entering a `with` block, this method returns the current cache instance, allowing it to be used within the context manager. This enables resource management for Redis caching operations.*


### __exit__ (method, L107-L119, parent: RedisCache)

> *Summary: When exiting a runtime context, this method ensures proper cleanup by calling `self.close()` on the object. It accepts standard exception details (`exc_type`, `exc_val`, `exc_tb`) to handle potential errors during shutdown.*

