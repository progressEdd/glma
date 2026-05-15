# autogen/agentchat/contrib/vectordb/qdrant.py

3 class(es): EmbeddingFunction, FastEmbedEmbeddingFunction, QdrantVectorDB. 19 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| EmbeddingFunction | class |  |
| FastEmbedEmbeddingFunction | class |  |
| QdrantVectorDB | class |  |

## Chunks

### EmbeddingFunction (class, L26-L29)

> *Summary: Defines an abstract interface requiring any implementing class to accept a list of strings and return a corresponding list of embedding vectors. This structure enforces that all concrete implementations must provide a method for converting text into numerical representations.*


### __call__ (method, L28-L29, parent: EmbeddingFunction)

> *Summary: This method is intended to be implemented by subclasses to process a list of string inputs. It must return a corresponding list of `Embeddings` objects.*


### FastEmbedEmbeddingFunction (class, L33-L69)

> *Summary: This class implements an embedding function using FastEmbed to convert a list of text strings into numerical vector representations. It accepts configuration parameters like the model name and batch size during initialization, and its call method returns a list of lists, where each inner list is the embedding vector for the corresponding input string.*


### __init__ (method, L36-L64, parent: FastEmbedEmbeddingFunction)

> *Summary: Initializes an embedding utility by creating a `TextEmbedding` instance using specified parameters like model name and batch size. It configures the underlying embedding process based on provided arguments for caching, threading, and parallel execution.*


### __call__ (method, L66-L69, parent: FastEmbedEmbeddingFunction)

> *Summary: This method takes a list of strings as input and uses an internal model to generate vector embeddings for each string. It returns these embeddings as a list of lists, where each inner list represents the numerical vector for the corresponding input text.*


### QdrantVectorDB (class, L73-L320)

> *Summary: This class implements a vector database interface using Qdrant as the backend, handling initialization with embedding functions and collection configurations. It provides methods to create, retrieve, insert, update, and delete documents by ID or via similarity search against provided queries.*


### __init__ (method, L76-L102, parent: QdrantVectorDB)

> *Summary: Initializes a Qdrant vector database instance, setting up the connection client (defaulting to in-memory), the embedding function, and payload keys for content and metadata. It accepts configuration options for collection creation and allows customization of these parameters upon instantiation.*


### create_collection (method, L104-L131, parent: QdrantVectorDB)

> *Summary: This method initializes a vector database collection based on specified parameters. It checks for the collection's existence and either creates it with appropriate embedding dimensions, overwrites an existing one if requested, or raises an error if it exists and no overwrite/get-or-create logic is permitted.*


### get_collection (method, L133-L145, parent: QdrantVectorDB)

> *Summary: Retrieves a specific vector database collection using its provided name. It validates that a `collection_name` string is supplied before calling the underlying client's retrieval method and returns the corresponding collection object.*


### delete_collection (method, L147-L156, parent: QdrantVectorDB)

> *Summary: Removes a specified collection from the underlying Qdrant vector database client. It accepts the collection's name as input and returns nothing upon successful deletion.*


### insert_docs (method, L158-L180, parent: QdrantVectorDB)

> *Summary: This method adds a list of `Document` objects to the specified vector database collection. It validates that all documents contain both content and an ID before performing an upsert operation on the client.*


### update_docs (method, L182-L192, parent: QdrantVectorDB)

> *Summary: This method updates existing documents within a specified Qdrant collection using provided `Document` objects. It validates that all input documents have non-null IDs and content, then performs an upsert operation only if the document IDs are found in the target collection.*


### delete_docs (method, L194-L205, parent: QdrantVectorDB)

> *Summary: Removes specified documents from a Qdrant vector database collection using a list of document IDs. It delegates the deletion operation to the underlying client instance.*


### retrieve_docs (method, L207-L242, parent: QdrantVectorDB)

> *Summary: This method queries a Qdrant vector database using provided text strings to find relevant documents. It converts the input queries into embeddings, executes a batched search request specifying result limits and distance thresholds, and returns structured query results containing the retrieved documents and their associated distances.*


### get_docs_by_ids (method, L244-L263, parent: QdrantVectorDB)

> *Summary: Retrieves documents from a Qdrant vector database using either a list of specific IDs or by fetching all documents in a collection. It accepts optional parameters to specify the collection name and which fields (payloads) should be returned alongside the vectors.*


### _point_to_document (method, L265-L271, parent: QdrantVectorDB)

> *Summary: Transforms a vector database point object into a structured `Document` format. It extracts the ID, content (using a specified key), metadata, and the embedding vector from the input point.*


### _points_to_documents (method, L273-L274, parent: QdrantVectorDB)

> *Summary: Transforms a list of vector database points into a corresponding list of `Document` objects by applying a point-to-document conversion function to each input point.*


### _scored_point_to_document (method, L276-L277, parent: QdrantVectorDB)

> *Summary: Converts a `ScoredPoint` object into a tuple containing the corresponding `Document` and its associated score. It delegates the document retrieval to another internal method while returning the point's score directly.*


### _documents_to_points (method, L279-L293, parent: QdrantVectorDB)

> *Summary: Converts a list of `Document` objects into Qdrant-compatible `PointStruct` representations. It extracts content, generates embeddings using an internal function, and structures the data with IDs, vectors, and associated metadata/content payloads.*


### _scored_points_to_documents (method, L295-L296, parent: QdrantVectorDB)

> *Summary: Transforms a list of `ScoredPoint` objects into a list of tuples, where each tuple pairs a `Document` with its associated score. It iterates over the input points and applies a helper method to convert each one individually.*


### _validate_update_ids (method, L298-L308, parent: QdrantVectorDB)

> *Summary: Checks if a provided list of IDs exists within a specified Qdrant collection by attempting to retrieve them. Returns `True` if all IDs are found, or logs a warning and returns `False` if any IDs are missing.*


### _validate_upsert_ids (method, L310-L320, parent: QdrantVectorDB)

> *Summary: Checks if any provided IDs already exist within a specified Qdrant collection by querying the database for those IDs. Returns `True` if none of the input IDs are found, and `False` otherwise, logging a warning upon detection.*

