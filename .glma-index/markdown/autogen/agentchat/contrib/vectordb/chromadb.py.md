# autogen/agentchat/contrib/vectordb/chromadb.py

1 class(es): ChromaVectorDB. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ChromaVectorDB | class |  |

## Chunks

### ChromaVectorDB (class, L30-L316)

> *Summary: This class implements a vector database interface using ChromaDB as the backend, allowing initialization with specific client configurations or paths. It provides methods to manage collections (create, get, delete), insert/update/delete documents in batches, and perform similarity searches based on text queries or document IDs.*


### __init__ (method, L33-L68, parent: ChromaVectorDB)

> *Summary: Initializes a ChromaDB vector database instance, accepting an optional pre-configured client or path for persistence. It configures the embedding function (defaulting to SentenceTransformer), sets metadata parameters, and establishes the connection using either a provided client or by creating a persistent/in-memory client based on the input path.*


### create_collection (method, L70-L112, parent: ChromaVectorDB)

> *Summary: This method manages the creation or retrieval of a vector database collection based on specified parameters. It accepts a collection name and boolean flags for overwriting or ensuring existence, returning the corresponding `Collection` object or raising an error if conditions are not met.*


### get_collection (method, L114-L136, parent: ChromaVectorDB)

> *Summary: Retrieves a specific ChromaDB collection by name or defaults to the currently active one if no name is provided. It ensures the requested collection is loaded into `self.active_collection` if it's not already set and matches the input name.*


### delete_collection (method, L138-L149, parent: ChromaVectorDB)

> *Summary: Removes a specified collection from the underlying ChromaDB instance via the client. If the deleted collection was currently active, it also resets the internal active collection reference to `None`.*


### _batch_insert (method, L151-L166, parent: ChromaVectorDB)

> *Summary: This method iteratively inserts or updates documents into a ChromaDB collection in batches defined by `CHROMADB_MAX_BATCH_SIZE`. It accepts lists of documents, IDs, metadatas, and optional embeddings to perform either an addition (`add`) or an upsert operation.*


### insert_docs (method, L168-L197, parent: ChromaVectorDB)

> *Summary: This method ingests a list of `Document` objects into the vector database collection. It validates that each document has content and an ID, then inserts or updates them using provided embeddings, IDs, metadata, and text content.*


### update_docs (method, L199-L209, parent: ChromaVectorDB)

> *Summary: Inserts or updates a provided list of `Document` objects within a specified ChromaDB collection. It delegates the operation to an internal insertion method, ensuring existing documents are overwritten if they match.*


### delete_docs (method, L211-L223, parent: ChromaVectorDB)

> *Summary: Removes specified documents from a vector database collection using a list of document IDs. It accepts an optional collection name and passes any additional keyword arguments to the underlying deletion operation.*


### retrieve_docs (method, L225-L258, parent: ChromaVectorDB)

> *Summary: Fetches relevant documents from a ChromaDB collection using a list of text queries. It accepts optional parameters to specify the number of results and apply a distance score threshold before returning structured query results.*


### _chroma_get_results_to_list_documents (method, L261-L295, parent: ChromaVectorDB)

> *Summary: Transforms a dictionary containing lists into a list of dictionaries, where each inner dictionary represents a row by combining elements from the corresponding index across all non-null input lists. It effectively pivots columnar data (lists in a dict) into row-based records.*


### get_docs_by_ids (method, L297-L316, parent: ChromaVectorDB)

> *Summary: Retrieves documents from a ChromaDB collection using specified IDs or all documents if no IDs are provided. It accepts optional parameters to filter by collection name and specify which fields (like metadata or content) should be returned in the output list of `Document` objects.*

