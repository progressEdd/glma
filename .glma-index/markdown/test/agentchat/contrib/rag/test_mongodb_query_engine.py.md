# test/agentchat/contrib/rag/test_mongodb_query_engine.py

6 function(s): mongodb_query_engine, test_get_collection_name, test_mongodb_query_engine_query, test_mongodb_query_engine_connect_db, test_mongodb_query_engine_add_docs, test_implements_protocol.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mongodb_query_engine | function |  |
| test_get_collection_name | function |  |
| test_mongodb_query_engine_query | function |  |
| test_mongodb_query_engine_connect_db | function |  |
| test_mongodb_query_engine_add_docs | function |  |
| test_implements_protocol | function |  |

## Chunks

### mongodb_query_engine (function, L27-L38)

> *Summary: This fixture sets up and initializes a `MongoDBQueryEngine` instance using predefined connection details and document paths/URLs. It returns the configured engine after successfully loading data into the specified MongoDB collection.*


### test_get_collection_name (function, L42-L47)

> *Summary: Verifies that the `MongoDBQueryEngine` returns its predefined default collection name, which is expected to be `"docling-parsed-docs"`. This test confirms the engine's initial configuration for database interaction.*


### test_mongodb_query_engine_query (function, L51-L57)

> *Summary: This test verifies the querying capability of a MongoDB engine by first loading documents via `add_docs`. It then executes a specific question against the loaded data and asserts that the returned answer contains "New York Stock Exchange".*


### test_mongodb_query_engine_connect_db (function, L61-L69)

> *Summary: This test verifies that the `MongoDBQueryEngine` successfully establishes a connection to a specified MongoDB collection using provided credentials and names. It asserts that the connection attempt returns `True`.*


### test_mongodb_query_engine_add_docs (function, L73-L82)

> *Summary: This test verifies that documents added via `add_docs` are successfully indexed and retrievable by the query engine. It adds new data sources and then asserts that a subsequent natural language query returns an answer containing the expected keyword ("maximum").*


### test_implements_protocol (function, L85-L87)

> *Summary: Verifies that the `MongoDBQueryEngine` class correctly inherits from and adheres to the `RAGQueryEngine` interface. This test confirms structural compliance for query engine functionality.*

