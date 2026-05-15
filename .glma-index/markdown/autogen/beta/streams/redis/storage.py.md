# autogen/beta/streams/redis/storage.py

1 class(es): RedisStorage. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RedisStorage | class |  |

## Chunks

### RedisStorage (class, L17-L53)

> *Summary: This class provides persistence for chat history by using Redis as a backend storage mechanism. It accepts a Redis URL and manages saving, retrieving, setting, and deleting event streams based on a provided `StreamId`.*


### __init__ (method, L20-L28, parent: RedisStorage)

> *Summary: Initializes a Redis storage handler by establishing an asynchronous connection to the specified `redis_url`, setting a default key `prefix`, and configuring the data serialization method. It prepares the necessary components for stream persistence operations using these inputs.*


### _key (method, L30-L31, parent: RedisStorage)

> *Summary: Generates a unique Redis key string by prepending the instance's prefix to the provided `StreamId`. This method serves as a standardized identifier for accessing stream data within Redis.*


### save_event (method, L33-L35, parent: RedisStorage)

> *Summary: This method appends a serialized `BaseEvent` to a Redis stream identified by the provided `Context`. It uses the internal Redis client to perform an RPUSH operation on the appropriate key.*


### get_history (method, L37-L39, parent: RedisStorage)

> *Summary: Retrieves all stored events from a specified stream ID by fetching the entire list range from Redis. It then deserializes each raw byte array into a `BaseEvent` object before returning them as an iterable.*


### set_history (method, L41-L47, parent: RedisStorage)

> *Summary: This method overwrites the stored history for a given stream ID by first deleting any existing data associated with its key. It then atomically pushes all provided events onto that key using Redis pipeline operations.*


### drop_history (method, L49-L50, parent: RedisStorage)

> *Summary: Removes the entire history associated with a given `StreamId` by deleting its corresponding key from Redis. This operation is asynchronous and returns nothing upon successful execution.*


### close (method, L52-L53, parent: RedisStorage)

> *Summary: This method asynchronously closes the underlying Redis connection managed by the instance. It ensures proper resource cleanup by calling `aclose()` on the internal Redis client object.*

