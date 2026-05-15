# autogen/agentchat/contrib/rag/chromadb_query_engine.py

1 function(s): _check_implement_protocol. 1 class(es): ChromaDBQueryEngine. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ChromaDBQueryEngine | class |  |
| _check_implement_protocol | function |  |

## Chunks

### ChromaDBQueryEngine (class, L40-L260)

> *Summary: This class manages a Retrieval-Augmented Generation (RAG) pipeline using ChromaDB for vector storage. It initializes by connecting to a specified or in-memory ChromaDB instance, allowing users to load documents via `init_db` (overwriting data) or incrementally add them with `add_docs`. Finally, it uses the configured LLM to answer natural language queries against the indexed data via the `query` method.*


### __init__ (method, L52-L100, parent: ChromaDBQueryEngine)

> *Summary: Initializes a query engine for ChromaDB by configuring connection details (host/port), an optional LLM, and embedding function. It establishes either a remote HTTP client or defaults to an in-memory client based on provided host and port arguments.*


### init_db (method, L102-L131, parent: ChromaDBQueryEngine)

> *Summary: Sets up and populates the ChromaDB instance by loading documents from a specified directory or list of paths/URLs. It overwrites any existing collection, builds vector indexes from the loaded documents, and returns `True` upon successful initialization.*


### connect_db (method, L133-L153, parent: ChromaDBQueryEngine)

> *Summary: Establishes a connection to the ChromaDB instance without replacing existing data by setting up LlamaIndex storage and creating a queryable vector store index from the configured vector store. Returns `True` upon successful initialization of the database connection and index.*


### add_docs (method, L155-L173, parent: ChromaDBQueryEngine)

> *Summary: This method ingests new data by loading documents from a specified directory or list of paths/URLs. It then iterates over these loaded documents and inserts each one into the underlying vector index for retrieval.*


### query (method, L175-L191, parent: ChromaDBQueryEngine)

> *Summary: This method takes a natural language question string as input and uses the configured index and LLM to retrieve an answer from indexed documents. It returns the resulting text response, or a predefined empty reply if the query engine yields no content.*


### get_collection_name (method, L193-L202, parent: ChromaDBQueryEngine)

> *Summary: Retrieves the configured ChromaDB collection name from the instance's state, raising an error if no collection name has been explicitly set.*


### _validate_query_index (method, L204-L207, parent: ChromaDBQueryEngine)

> *Summary: Checks if the necessary query index attribute has been set on the instance. If it hasn't, it raises an exception, requiring prior database initialization or connection.*


### _set_up (method, L209-L220, parent: ChromaDBQueryEngine)

> *Summary: Initializes the necessary components for RAG by creating a ChromaDB instance and collection based on provided configuration. It then sets up the LlamaIndex vector store and storage context using the newly created database collection.*


### _load_doc (method, L222-L260, parent: ChromaDBQueryEngine)

> *Summary: Loads documents into `LlamaDocument` objects by reading from either a specified directory or a list of individual file paths, utilizing LlamaIndex's `SimpleDirectoryReader`. It raises errors if the inputs are missing or if any specified path/directory does not exist.*


### _check_implement_protocol (function, L267-L268)

> *Summary: This internal helper validates that the provided object conforms to the `ChromaDBQueryEngine` type and asserts it adheres to the `RAGQueryEngine` protocol before returning it.*

