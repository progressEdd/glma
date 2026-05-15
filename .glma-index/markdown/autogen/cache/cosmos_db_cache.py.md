# autogen/cache/cosmos_db_cache.py

2 class(es): CosmosDBConfig, CosmosDBCache. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CosmosDBConfig | class |  |
| CosmosDBCache | class |  |

## Chunks

### CosmosDBConfig (class, L21-L26)

> *Summary: Defines a configuration structure for Cosmos DB interactions, holding necessary connection details like the string, database ID, and container ID. It optionally includes a cache seed and an initialized client object.*


### CosmosDBCache (class, L30-L144)

> *Summary: This class provides a synchronous caching mechanism backed by Azure Cosmos DB, using a specified seed as the partition key. It allows setting and retrieving serialized data items via `set` and `get`, handling connection setup through various factory methods based on configuration or existing clients.*


### __init__ (method, L42-L58, parent: CosmosDBCache)

> *Summary: Sets up a cache client by initializing connections to Cosmos DB using provided configuration and a unique seed/namespace. It ensures the necessary database and container exist for subsequent caching operations.*


### create_cache (method, L61-L68, parent: CosmosDBCache)

> *Summary: This factory method instantiates a cache object by checking the provided configuration for an existing `CosmosClient`. It either uses the pre-existing client via a specific class method or initializes a new connection based on the full configuration.*


### from_config (method, L71-L72, parent: CosmosDBCache)

> *Summary: Creates an instance of the class by accepting a seeding value and a configuration object. It ensures the seed is stored as a string before initializing the object.*


### from_connection_string (method, L75-L77, parent: CosmosDBCache)

> *Summary: Creates an instance of the cache class using provided configuration details. It accepts a seed (as string or int), connection string, database ID, and container ID to initialize the object.*


### from_existing_client (method, L80-L82, parent: CosmosDBCache)

> *Summary: Creates a cache instance from an already initialized CosmosDB client. It accepts the seed value, the existing client object, and the IDs for the target database and container to construct and return the configured class instance.*


### get (method, L84-L102, parent: CosmosDBCache)

> *Summary: Retrieves a cached item from Cosmos DB using a provided string key, deserializing the stored data upon success. If the key is not found in the database, it returns an optional default value instead of raising an error.*


### set (method, L104-L120, parent: CosmosDBCache)

> *Summary: Stores a given value under a specified string key in the Cosmos DB cache by first serializing the value using pickle. It then upserts an item into the container, using the provided key as the document ID and the instance's seed for the partition key.*


### close (method, L122-L129, parent: CosmosDBCache)

> *Summary: This method performs cleanup for the cached Cosmos DB client. Currently, it does nothing because the underlying SDK client does not require explicit closing.*


### __enter__ (method, L131-L137, parent: CosmosDBCache)

> *Summary: When entering the context, this method returns the current cache instance. This allows for direct access to the object's state within a `with` block.*


### __exit__ (method, L139-L144, parent: CosmosDBCache)

> *Summary: When exiting a context manager, this method ensures proper resource cleanup by calling the instance's `close()` method to shut down the Cosmos DB client connection. It handles any potential exceptions that occurred within the managed block.*

