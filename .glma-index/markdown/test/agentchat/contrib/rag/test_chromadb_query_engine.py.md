# test/agentchat/contrib/rag/test_chromadb_query_engine.py

6 function(s): chroma_query_engine, test_get_collection_name, test_chroma_db_query_engine_query, test_chroma_db_query_engine_connect_db, test_chroma_db_query_engine_add_docs, test_implements_protocol.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| chroma_query_engine | function |  |
| test_get_collection_name | function |  |
| test_chroma_db_query_engine_query | function |  |
| test_chroma_db_query_engine_connect_db | function |  |
| test_chroma_db_query_engine_add_docs | function |  |
| test_implements_protocol | function |  |

## Chunks

### chroma_query_engine (function, L27-L36)

> *Summary: Initializes a `ChromaDBQueryEngine` instance configured to connect to a specific ChromaDB host and port. It then populates the database using provided input documents and returns the initialized engine object.*


### test_get_collection_name (function, L41-L46)

> *Summary: This test verifies that a `ChromaDBQueryEngine` instance defaults to using the specific collection name `"docling-parsed-docs"` when its getter method is called. It asserts this default value matches the expected string.*


### test_chroma_db_query_engine_query (function, L51-L57)

> *Summary: This test verifies that the `ChromaDBQueryEngine` correctly retrieves information from its knowledge base when provided with a specific question about Nvidia's R&D spending. It asserts that the returned answer string contains the expected value, "45.3 billion".*


### test_chroma_db_query_engine_connect_db (function, L62-L76)

> *Summary: This test verifies the `connect_db` functionality of a ChromaDB query engine by first establishing a connection and then executing a sample query against an existing collection to assert the returned answer contains specific text. It uses predefined host/port details for database interaction.*


### test_chroma_db_query_engine_add_docs (function, L81-L89)

> *Summary: This test verifies the `add_docs` functionality of a ChromaDB query engine by first adding documents and then querying the engine with a specific question. It asserts that the resulting answer contains one of two expected monetary values, confirming successful ingestion and retrieval.*


### test_implements_protocol (function, L92-L93)

> *Summary: Verifies that the `ChromaDBQueryEngine` correctly inherits from the `RAGQueryEngine` base class. This confirms adherence to the expected interface for retrieval-augmented generation components.*

