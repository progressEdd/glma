# autogen/agentchat/contrib/vectordb/mongodb.py

2 function(s): with_id_rename, _vector_search. 1 class(es): MongoDBAtlasVectorDB. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| with_id_rename | function |  |
| MongoDBAtlasVectorDB | class |  |
| _vector_search | function |  |

## Chunks

### with_id_rename (function, L31-L33)

> *Summary: Transforms an iterable of documents by renaming the internal `_id` field to a standard `id` field while excluding the original `_id`. It accepts any iterable of dictionaries and returns a list of modified dictionaries.*


### MongoDBAtlasVectorDB (class, L37-L500)

> *Summary: This class provides a comprehensive interface to interact with MongoDB Atlas as a vector database. It initializes connections, manages collections and vector search indexes using specified embedding functions, and supports CRUD operations like inserting, updating, retrieving documents by ID, and performing similarity searches based on text queries.*


### __init__ (method, L40-L86, parent: MongoDBAtlasVectorDB)

> *Summary: Establishes a connection to MongoDB using provided credentials and initializes the vector database configuration. It sets up an embedding function, determines the required vector dimensions, and prepares the active collection based on input parameters.*


### _is_index_ready (method, L88-L102, parent: MongoDBAtlasVectorDB)

> *Summary: Determines if a specified vector search index within a MongoDB collection is fully operational. It iterates through the collection's search indexes, returning `True` only if an index matching the name exists and has a status of "READY".*


### _wait_for_index (method, L104-L119, parent: MongoDBAtlasVectorDB)

> *Summary: This method polls a MongoDB collection to ensure an index creation or deletion operation has finished within a predefined timeout period. It repeatedly checks the index status, sleeping briefly between attempts until the condition is met or a `TimeoutError` is raised.*


### _wait_for_document (method, L121-L134, parent: MongoDBAtlasVectorDB)

> *Summary: This method polls a MongoDB collection using vector search until a specific document ID appears in the results or a timeout occurs. It continuously queries the database with the document's embedding, pausing briefly between checks to confirm readiness.*


### _get_embedding_size (method, L136-L137, parent: MongoDBAtlasVectorDB)

> *Summary: Determines the dimensionality of the vector embeddings by calculating the length of the embedding produced for a predefined sample sentence using the instance's embedding function. This value is crucial for configuring vector database operations.*


### list_collections (method, L139-L145, parent: MongoDBAtlasVectorDB)

> *Summary: Retrieves all collection names from the underlying MongoDB instance. It takes no arguments and returns a list of strings representing the existing database collections.*


### create_collection (method, L147-L176, parent: MongoDBAtlasVectorDB)

> *Summary: This method initializes a MongoDB collection, optionally deleting it first if `overwrite` is true. It either creates the specified collection with a vector search index or retrieves the existing one, raising an error if retrieval is disallowed and the collection is present.*


### create_index_if_not_exists (method, L178-L186, parent: MongoDBAtlasVectorDB)

> *Summary: Checks if a vector search index already exists for a given collection and name; if it doesn't exist, it proceeds to create the specified MongoDB vector search index.*


### get_collection (method, L188-L208, parent: MongoDBAtlasVectorDB)

> *Summary: Retrieves a specific MongoDB collection or defaults to the currently active one if no name is provided. It raises an error if no collection has been set and none is specified as input.*


### delete_collection (method, L210-L220, parent: MongoDBAtlasVectorDB)

> *Summary: Removes all search indexes associated with a specified collection before deleting the entire collection from the MongoDB vector database. It accepts a collection name string and returns nothing upon successful deletion.*


### create_vector_search_index (method, L222-L266, parent: MongoDBAtlasVectorDB)

> *Summary: This method configures and creates a vector search index within a specified MongoDB collection. It takes the collection, an optional index name, and a similarity metric as input to define how vector embeddings will be searched.*


### insert_docs (method, L268-L336, parent: MongoDBAtlasVectorDB)

> *Summary: Inserts a list of `Document` objects into the vector database collection, handling large inputs by processing them in batches. It supports optional upserting and performs validation checks on required document fields before insertion.*


### _insert_batch (method, L338-L369, parent: MongoDBAtlasVectorDB)

> *Summary: This method computes embeddings for a batch of text inputs and then inserts the resulting documents, along with their associated metadata and unique IDs, into a specified MongoDB collection. It returns the set of IDs that were successfully inserted into the database.*


### update_docs (method, L371-L408, parent: MongoDBAtlasVectorDB)

> *Summary: Takes a list of `Document` objects and an optional collection name to embed their content and update corresponding records in MongoDB. It performs a bulk write operation, optionally enabling upserts based on the provided keyword arguments.*


### delete_docs (method, L410-L419, parent: MongoDBAtlasVectorDB)

> *Summary: Removes specified documents from a MongoDB collection using a list of document IDs. It takes the IDs and an optional collection name as input, returning the result of the deletion operation.*


### get_docs_by_ids (method, L421-L449, parent: MongoDBAtlasVectorDB)

> *Summary: Retrieves documents from a MongoDB collection using specified IDs, or all documents if no IDs are provided. It allows filtering which fields to return and maps the database's `_id` field to the `Document` object's `id`.*


### retrieve_docs (method, L451-L500, parent: MongoDBAtlasVectorDB)

> *Summary: Retrieves documents from a MongoDB vector database based on a list of text queries. It converts each query to an embedding, performs a similarity search using the configured index and parameters like result count and distance threshold, and returns structured results containing the matching documents and their scores for every input query.*


### _vector_search (function, L503-L551)

> *Summary: Executes a MongoDB `$vectorSearch` aggregation to find nearest neighbors based on an input embedding vector within a specified collection and index. It returns a list of tuples containing the matching document and its calculated similarity score, optionally filtering by distance or excluding the embedded vector from the output.*

