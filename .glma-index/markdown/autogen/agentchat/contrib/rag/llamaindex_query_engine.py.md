# autogen/agentchat/contrib/rag/llamaindex_query_engine.py

1 function(s): _check_implement_protocol. 1 class(es): LlamaIndexQueryEngine. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LlamaIndexQueryEngine | class |  |
| _check_implement_protocol | function |  |

## Chunks

### LlamaIndexQueryEngine (class, L36-L187)

> *Summary: This class provides a query engine that uses LlamaIndex to index documents from various sources (directories or file lists) into a vector store. It allows initialization by building an index from new data, connecting to an existing one, adding more documents, and finally querying the indexed knowledge base using a specified LLM.*


### __init__ (method, L43-L58, parent: LlamaIndexQueryEngine)

> *Summary: Sets up a query engine by accepting a `BasePydanticVectorStore` and optional LLM or document reader classes. It defaults to using GPT-4o as the LLM if none is provided, ensuring readiness for RAG operations.*


### init_db (method, L60-L86, parent: LlamaIndexQueryEngine)

> *Summary: This method initializes the database by setting up a LlamaIndex storage context using an existing vector store. It then loads documents from specified directories or paths/URLs and builds a `VectorStoreIndex` on those documents.*


### connect_db (method, L88-L104, parent: LlamaIndexQueryEngine)

> *Summary: Establishes a connection by initializing LlamaIndex's `StorageContext` using the provided vector store and then constructs a `VectorStoreIndex` from that same vector store. It returns `True` upon successful setup of these components.*


### add_docs (method, L106-L124, parent: LlamaIndexQueryEngine)

> *Summary: This method ingests new data by loading documents from a specified directory or list of paths/URLs. It then iterates over these loaded documents, inserting each one into the underlying index for retrieval.*


### query (method, L126-L142, parent: LlamaIndexQueryEngine)

> *Summary: This method takes a natural language question string as input and uses the configured index and LLM to retrieve an answer from indexed documents. It returns the resulting text response, handling cases where the query engine produces an empty result.*


### _validate_query_index (method, L144-L147, parent: LlamaIndexQueryEngine)

> *Summary: Checks if the necessary query index attribute has been set on the instance. If it's missing, it raises an exception, requiring prior database initialization or connection.*


### _load_doc (method, L149-L187, parent: LlamaIndexQueryEngine)

> *Summary: Loads documents either from a specified directory using LlamaIndex's `SimpleDirectoryReader` or from an explicit sequence of file paths. It returns a list of `LlamaDocument` objects, raising errors if inputs are missing or files/directories do not exist.*


### _check_implement_protocol (function, L194-L195)

> *Summary: This helper function verifies that an input object conforms to the `LlamaIndexQueryEngine` protocol and returns it as a type-checked `RAGQueryEngine`. It essentially acts as a type assertion or validation step for query engine objects.*

