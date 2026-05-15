# autogen/agents/experimental/document_agent/chroma_query_engine.py

1 function(s): _check_implement_protocol. 3 class(es): VectorChromaQueryEngine, AnswerWithCitations, VectorChromaCitationQueryEngine. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| VectorChromaQueryEngine | class |  |
| AnswerWithCitations | class |  |
| VectorChromaCitationQueryEngine | class |  |
| _check_implement_protocol | function |  |

## Chunks

### VectorChromaQueryEngine (class, L43-L245)

> *Summary: This class manages a Retrieval-Augmented Generation (RAG) pipeline using ChromaDB for persistent storage and LlamaIndex for indexing. It initializes by connecting to or creating a named collection in the database, allowing users to add documents via file paths/directories and subsequently query the indexed content using an LLM.*


### __init__ (method, L52-L84, parent: VectorChromaQueryEngine)

> *Summary: Sets up a vector query engine by initializing connections to ChromaDB, configuring the embedding function and LLM, and setting default metadata for indexing. It accepts optional parameters like database path, specific embeddings, configuration metadata, an LLM instance, and a collection name to manage persistence and querying.*


### connect_db (method, L86-L103, parent: VectorChromaQueryEngine)

> *Summary: This method establishes and initializes a connection to a ChromaDB instance, either by retrieving an existing collection or creating a new one based on configuration. It ensures the necessary index is created within the specified collection before returning `True`.*


### query (method, L105-L121, parent: VectorChromaQueryEngine)

> *Summary: Processes a natural language question against indexed documents to retrieve relevant information. It initializes a query engine using the provided index and LLM, returning the resulting text response or a predefined empty reply if no content is found.*


### add_docs (method, L123-L144, parent: VectorChromaQueryEngine)

> *Summary: This method ingests and adds new documents to the existing vector index. It accepts either a directory path or a sequence of file paths/URLs, loads the specified Markdown files using an internal loader, and then inserts each resulting document into the index.*


### _load_doc (method, L146-L186, parent: VectorChromaQueryEngine)

> *Summary: Reads documents from either a specified directory or a list of individual file paths using `SimpleDirectoryReader`. It returns a list of `LlamaDocument` objects, raising errors if inputs are missing or files/directories do not exist.*


### _create_index (method, L188-L207, parent: VectorChromaQueryEngine)

> *Summary: This method constructs a `VectorStoreIndex` by wrapping an input ChromaDB collection into a custom vector store implementation. It utilizes LlamaIndex's `StorageContext` to build and return the fully configured index object for document retrieval.*


### _collection_exists (method, L209-L219, parent: VectorChromaQueryEngine)

> *Summary: Determines if a specified collection name is present within the Chroma database by listing all available collections and checking for a match. It accepts a string representing the desired collection name and returns a boolean indicating its existence.*


### get_collection_name (method, L221-L230, parent: VectorChromaQueryEngine)

> *Summary: Retrieves the configured ChromaDB collection identifier; it returns the stored name if present, otherwise raises a `ValueError`.*


### validate_query_index (method, L232-L235, parent: VectorChromaQueryEngine)

> *Summary: Checks for the presence of a query index attribute on the instance; if missing, it raises an exception requiring prior document ingestion before any queries can be executed.*


### init_db (method, L237-L245, parent: VectorChromaQueryEngine)

> *Summary: This method is intentionally unimplemented and raises a `NotImplementedError` because it is not required or supported by the `VectorChromaQueryEngine`. It accepts optional arguments for new document directories or paths/URLs but provides no functionality.*


### AnswerWithCitations (class, L248-L250)

> *Summary: This data structure models a response containing both the generated answer text and a list of supporting citations. It requires an `answer` string and a list of `NodeWithScore` objects to be initialized.*


### VectorChromaCitationQueryEngine (class, L255-L293)

> *Summary: This engine extends a base query mechanism to retrieve answers along with specific source citations from a vector database. It accepts a natural language `query` string and returns an object containing both the generated answer and the corresponding citation nodes.*


### __init__ (method, L258-L271, parent: VectorChromaCitationQueryEngine)

> *Summary: Initializes a Chroma query engine by setting up parameters for database location, embeddings, LLM interaction, and collection name via the parent class. It also configures specific behaviors like enabling citations and defining the chunk size for those citations.*


### query_with_citations (method, L273-L293, parent: VectorChromaCitationQueryEngine)

> *Summary: This method takes a string query and uses an internal `CitationQueryEngine` to search the associated index. It returns an object containing both the generated answer and the source nodes that support it as citations.*


### _check_implement_protocol (function, L300-L301)

> *Summary: This internal helper validates that the provided object adheres to the `VectorChromaQueryEngine` protocol and returns it as a conforming `RAGQueryEngine`. It ensures type compatibility for downstream processing.*

