# autogen/agentchat/contrib/vectordb/couchbase.py

1 class(es): CouchbaseVectorDB. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CouchbaseVectorDB | class |  |

## Chunks

### CouchbaseVectorDB (class, L39-L405)

> *Summary: This class provides a vector database implementation using Couchbase as the backend storage and indexing engine. It initializes by connecting to a specified Couchbase cluster, allowing users to create collections and vector search indexes based on an provided embedding function. Key operations include inserting, updating, deleting documents, retrieving by ID, and performing similarity searches against query vectors.*


### __init__ (method, L42-L89, parent: CouchbaseVectorDB)

> *Summary: Establishes a connection to a Couchbase cluster using provided credentials and configuration parameters like bucket, scope, and collection names. It initializes the necessary database objects and determines the vector dimension size based on an optional embedding function.*


### search_index_exists (method, L91-L98, parent: CouchbaseVectorDB)

> *Summary: Determines if a Couchbase search index is ready by attempting to retrieve and validate the specified index name from the scope's search indexes manager, returning `True` only if validation succeeds.*


### _get_embedding_size (method, L100-L101, parent: CouchbaseVectorDB)

> *Summary: Determines the dimensionality of vector embeddings by calculating the length of the embedding produced for a predefined sample sentence using the instance's embedding function. This value is crucial for configuring vector database operations.*


### create_collection (method, L103-L132, parent: CouchbaseVectorDB)

> *Summary: This method initializes a vector database collection by creating the specified collection and an associated primary index within it. It handles existing collections based on `overwrite` and `get_or_create` flags, returning the configured collection object.*


### create_index_if_not_exists (method, L134-L144, parent: CouchbaseVectorDB)

> *Summary: Checks for an existing vector search index and creates it in Couchbase if one with the given name is not found on the specified collection. This ensures a necessary indexing structure is present before further operations.*


### get_collection (method, L146-L165, parent: CouchbaseVectorDB)

> *Summary: Retrieves a Couchbase collection object, either by explicitly providing a `collection_name` or by defaulting to the instance's currently active collection if one is set. It raises an error if no collection is specified and none is actively configured.*


### delete_collection (method, L167-L177, parent: CouchbaseVectorDB)

> *Summary: Removes a specified collection from the vector database by calling `drop_collection` on the bucket's collection manager. It accepts a collection name string and logs any exceptions encountered during the deletion process.*


### create_vector_search_index (method, L179-L270, parent: CouchbaseVectorDB)

> *Summary: Configures and creates a vector search index within a Couchbase collection, using the provided collection name and an optional index name. It defines the schema to support vector embeddings (using L2 norm or dot product) and text content for efficient similarity searches.*


### upsert_docs (method, L272-L295, parent: CouchbaseVectorDB)

> *Summary: This method takes a list of `Document` objects and updates or inserts them into a Couchbase collection in batches. It first validates that each document has content and an ID, then generates embeddings for the content before performing a bulk upsert operation on the specified collection.*


### insert_docs (method, L297-L311, parent: CouchbaseVectorDB)

> *Summary: This method inserts a list of `Document` objects and their associated vector embeddings into the configured Couchbase collection. It handles upserts by calling an internal function with the provided documents and specified batch size.*


### update_docs (method, L313-L318, parent: CouchbaseVectorDB)

> *Summary: This method updates existing or inserts new documents and their associated embeddings into a specified Couchbase collection. It takes a list of `Document` objects as input and delegates the actual upserting operation to an internal helper function.*


### delete_docs (method, L320-L328, parent: CouchbaseVectorDB)

> *Summary: Removes specified documents from a Couchbase collection by iterating through the provided IDs in batches. It uses `remove_multi` on the retrieved collection object to perform the deletion operation.*


### get_docs_by_ids (method, L330-L355, parent: CouchbaseVectorDB)

> *Summary: Retrieves documents from a Couchbase collection using either a list of specific IDs or by querying all documents. It accepts optional parameters to specify the collection name and which fields should be returned, ultimately outputting a list of filtered document dictionaries.*


### retrieve_docs (method, L357-L377, parent: CouchbaseVectorDB)

> *Summary: This method fetches documents from a Couchbase vector database using a list of text queries. It converts each query into an embedding vector and then performs a vector search to return the top $N$ matching results for every input query.*


### _vector_search (method, L379-L405, parent: CouchbaseVectorDB)

> *Summary: Performs a core vector search against the Couchbase index using a provided embedding vector and desired result count. It constructs a `VectorSearch` request, executes it via the scope's search method, and returns a list of tuples containing the matching document data and its associated similarity score.*

