# autogen/agentchat/contrib/rag/mongodb_query_engine.py

1 function(s): _check_implement_protocol. 1 class(es): MongoDBQueryEngine. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MongoDBQueryEngine | class |  |
| _check_implement_protocol | function |  |

## Chunks

### MongoDBQueryEngine (class, L40-L312)

> *Summary: This class manages a MongoDB-backed vector database, allowing for document ingestion and retrieval via a chat interface. It initializes connections using a connection string, builds an index from provided documents (via directory or paths), and executes queries against the indexed data using an integrated LLM.*


### __init__ (method, L53-L94, parent: MongoDBQueryEngine)

> *Summary: This constructor sets up a MongoDB query engine by accepting connection details, an optional LLM, and configuration for embedding and database/collection names. It initializes default values for the LLM (OpenAI) and embedding function if none are provided, preparing the object to later connect to and interact with MongoDB.*


### _set_up (method, L96-L121, parent: MongoDBQueryEngine)

> *Summary: Initializes the necessary components for a MongoDB-backed RAG system by creating a vector database, setting up a vector search engine using connection details and an optional overwrite flag, and establishing a storage context around the search engine. This method configures the entire retrieval infrastructure based on provided connection parameters.*


### _check_existing_collection (method, L123-L131, parent: MongoDBQueryEngine)

> *Summary: Determines if a MongoDB collection exists by connecting to the database using stored connection and name parameters. It returns `True` if the specified collection is present, otherwise `False`.*


### connect_db (method, L133-L163, parent: MongoDBQueryEngine)

> *Summary: Establishes a connection to MongoDB by verifying collection existence, setting up the database context without overwriting data, building a vector store index from the existing search engine, and pinging the server. It returns `True` upon successful connection and indexing, or `False` if any step fails.*


### init_db (method, L165-L210, parent: MongoDBQueryEngine)

> *Summary: This method initializes a MongoDB-backed vector store by loading documents from specified directories or paths/URLs. It sets up (or overwrites) the collection, builds an index using provided embedding and storage contexts, and inserts all loaded documents into the database, returning `True` on success or `False` upon failure.*


### _validate_query_index (method, L212-L219, parent: MongoDBQueryEngine)

> *Summary: Ensures that a necessary database index object exists before proceeding with operations. It raises an exception if the `index` attribute has not been set via initialization methods.*


### _load_doc (method, L221-L252, parent: MongoDBQueryEngine)

> *Summary: This method loads documents either from a specified directory or a list of individual file paths. It accepts an optional directory path and/or a sequence of document paths, returning a collection of `LlamaDocument` objects after validating that the inputs exist.*


### add_docs (method, L254-L275, parent: MongoDBQueryEngine)

> *Summary: Loads new documents from a specified directory or list of paths/URLs and inserts them into the existing vector store index after validating the index's existence. It accepts optional inputs for either a document directory or a sequence of individual file locations.*


### query (method, L277-L298, parent: MongoDBQueryEngine)

> *Summary: This method takes a question string and executes it against an initialized vector store index to retrieve relevant documents. It returns the resulting query response as a string, or a predefined default reply if no results are found.*


### get_collection_name (method, L300-L312, parent: MongoDBQueryEngine)

> *Summary: Retrieves the configured MongoDB collection name from the instance's state. It returns the stored string if present, otherwise raises a `ValueError`.*


### _check_implement_protocol (function, L318-L319)

> *Summary: This internal helper validates that the provided object adheres to the `MongoDBQueryEngine` protocol and returns it as a conforming `RAGQueryEngine`. It essentially ensures type compatibility within the retrieval-augmented generation system.*

