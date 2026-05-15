# autogen/agents/experimental/document_agent/inmemory_query_engine.py

1 function(s): _check_implement_protocol. 3 class(es): DocumentStore, QueryAnswer, InMemoryQueryEngine. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DocumentStore | class |  |
| QueryAnswer | class |  |
| InMemoryQueryEngine | class |  |
| _check_implement_protocol | function |  |

## Chunks

### DocumentStore (class, L29-L31)

> *Summary: This data structure holds a document by storing its unique `ingestation_name` and the associated textual `content`. It serves as a basic container for managing ingested documents.*


### QueryAnswer (class, L35-L37)

> *Summary: This data structure encapsulates a response to a query, containing a boolean indicating if an answer was found and the resulting string content. It serves as a standardized output format for querying mechanisms.*


### InMemoryQueryEngine (class, L41-L206)

> *Summary: Stores documents in memory and uses an internal agent to answer questions based on that content. It accepts document paths or directories via `add_docs` and returns a string containing the AI-generated answer when `query` is called.*


### __init__ (method, L47-L64, parent: InMemoryQueryEngine)

> *Summary: Initializes the engine by creating a dedicated query agent configured to produce structured responses. It also sets up an internal list to store documents loaded into memory for querying.*


### query (method, L66-L114, parent: InMemoryQueryEngine)

> *Summary: This method executes a query against stored documents by constructing a detailed system prompt containing all ingested content. It passes this context and the user's question to an underlying agent, then parses the resulting JSON summary to return either the direct answer or a predefined failure message.*


### add_docs (method, L116-L134, parent: InMemoryQueryEngine)

> *Summary: Loads and inserts new documents into the in-memory store by processing Markdown files from either a specified directory or an explicit list of paths. It delegates the actual loading to an internal method using the provided directory or path inputs.*


### _load_doc (method, L136-L175, parent: InMemoryQueryEngine)

> *Summary: Reads files from a specified directory or a list of individual paths, using native Python I/O to populate the internal document store. It validates that at least one input source is provided and raises errors if directories or specific files are missing.*


### _read_and_store_file (method, L177-L192, parent: InMemoryQueryEngine)

> *Summary: Reads the content from a specified file path and stores it as a `Document` object within the agent's in-memory document store. It handles potential I/O errors by raising a `ValueError`.*


### init_db (method, L194-L202, parent: InMemoryQueryEngine)

> *Summary: This method is intentionally unimplemented and raises a `NotImplementedError` because the in-memory query engine does not require or support database initialization. It accepts optional arguments for new document directories or paths/URLs but performs no setup.*


### connect_db (method, L204-L206, parent: InMemoryQueryEngine)

> *Summary: This method intentionally raises a `NotImplementedError` because the in-memory query engine does not require or implement database connection logic. It accepts arbitrary positional and keyword arguments but always returns a boolean indicating failure to execute.*


### _check_implement_protocol (function, L213-L214)

> *Summary: This helper function validates that an object conforms to the `InMemoryQueryEngine` protocol and returns it cast as a `RAGQueryEngine`. It essentially ensures type compatibility for downstream processing.*

