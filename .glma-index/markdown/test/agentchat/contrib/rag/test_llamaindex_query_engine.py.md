# test/agentchat/contrib/rag/test_llamaindex_query_engine.py

5 function(s): chroma_query_engine, test_lllamindex_query_engine_query, test_llamaindex_query_engine_connect_db, test_llamaindex_query_engine_add_docs, test_implements_protocol.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| chroma_query_engine | function |  |
| test_lllamindex_query_engine_query | function |  |
| test_llamaindex_query_engine_connect_db | function |  |
| test_llamaindex_query_engine_add_docs | function |  |
| test_implements_protocol | function |  |

## Chunks

### chroma_query_engine (function, L33-L44)

> *Summary: This function initializes and returns a `LlamaIndexQueryEngine` configured to query an existing ChromaDB collection named "default\_collection." It achieves this by connecting to a specified local ChromaDB instance via an HTTP client.*


### test_lllamindex_query_engine_query (function, L49-L56)

> *Summary: This test verifies that an initialized `LlamaIndexQueryEngine` correctly answers a specific question based on provided documents. It asserts that the returned answer string contains the expected value, "45.3 billion".*


### test_llamaindex_query_engine_connect_db (function, L61-L65)

> *Summary: Verifies that a `LlamaIndexQueryEngine` instance successfully connects to an existing database collection by asserting the return value of its `connect_db()` method is `True`.*


### test_llamaindex_query_engine_add_docs (function, L70-L78)

> *Summary: This test verifies the `add_docs` functionality of a LlamaIndex query engine by first ingesting documents and then querying it with a specific question. It asserts that the returned answer contains one of two expected monetary values, confirming successful data ingestion and retrieval.*


### test_implements_protocol (function, L81-L82)

> *Summary: Verifies that the `LlamaIndexQueryEngine` correctly inherits from the `RAGQueryEngine` base class. This confirms adherence to the expected interface for retrieval-augmented generation engines.*

