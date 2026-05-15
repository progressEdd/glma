# autogen/agentchat/contrib/vectordb/base.py

3 class(es): Document, VectorDB, VectorDBFactory. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Document | class |  |
| VectorDB | class |  |
| VectorDBFactory | class |  |

## Chunks

### Document (class, L15-L27)

> *Summary: Represents a single record within a vector database, holding essential document information. It requires a unique ID and text content, optionally including metadata and its corresponding vector embedding.*


### VectorDB (class, L38-L182)

> *Summary: Defines a protocol for abstracting vector database operations, allowing implementations to handle storage and retrieval of documents. It supports core functionalities like creating/deleting collections, inserting/updating/deleting documents, and retrieving data via similarity search or by ID.*


### create_collection (method, L62-L77, parent: VectorDB)

> *Summary: This method initializes a vector database collection based on provided parameters. It handles three scenarios: creating a new collection, overwriting an existing one, or retrieving the existing collection while optionally raising an error if it's present but not intended to be retrieved.*


### get_collection (method, L79-L89, parent: VectorDB)

> *Summary: Retrieves a specific vector database collection by its name; if no name is provided, it returns the currently active collection object.*


### delete_collection (method, L91-L100, parent: VectorDB)

> *Summary: Removes a specified collection from the underlying vector database using its name as input, returning an arbitrary result upon completion.*


### insert_docs (method, L102-L114, parent: VectorDB)

> *Summary: Adds a list of `Document` objects into a specified vector database collection, optionally updating existing entries based on the `upsert` flag. It accepts documents and configuration parameters like the collection name and upsert behavior as input.*


### update_docs (method, L116-L127, parent: VectorDB)

> *Summary: This method updates existing or adds new documents to a specified vector database collection. It accepts a list of `Document` objects and an optional collection name, performing the update operation internally.*


### delete_docs (method, L129-L140, parent: VectorDB)

> *Summary: Removes specified documents from a vector database collection using a list of document IDs. It accepts an optional collection name and additional keyword arguments for the deletion operation.*


### retrieve_docs (method, L142-L164, parent: VectorDB)

> *Summary: Fetches relevant documents from a vector database given a list of text queries. It accepts optional parameters to specify the collection, limit the number of returned results, or filter by a distance threshold, returning structured query results.*


### get_docs_by_ids (method, L166-L182, parent: VectorDB)

> *Summary: Retrieves documents from a vector database collection using specified IDs, or all documents if no IDs are provided. It allows filtering by collection name and selecting specific fields to return in the resulting list of `Document` objects.*


### VectorDBFactory (class, L185-L224)

> *Summary: This factory method constructs and returns an instance of a specified vector database implementation based on the provided `db_type` string. It accepts configuration parameters via keyword arguments to initialize the chosen backend, raising an error if the type is unsupported.*


### create_vector_db (method, L191-L224, parent: VectorDBFactory)

> *Summary: This function instantiates and returns a specific `VectorDB` implementation based on the provided `db_type` string. It acts as a factory, routing initialization to Chroma, PostgreSQL, MongoDB, Qdrant, or Couchbase depending on the input type.*

