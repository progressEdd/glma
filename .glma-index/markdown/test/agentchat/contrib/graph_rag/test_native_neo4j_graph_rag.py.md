# test/agentchat/contrib/graph_rag/test_native_neo4j_graph_rag.py

5 function(s): neo4j_native_query_engine, neo4j_native_query_engine_auto, test_neo4j_native_query_engine, test_neo4j_native_query_auto, test_neo4j_add_records.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| neo4j_native_query_engine | function |  |
| neo4j_native_query_engine_auto | function |  |
| test_neo4j_native_query_engine | function |  |
| test_neo4j_native_query_auto | function |  |
| test_neo4j_add_records | function |  |

## Chunks

### neo4j_native_query_engine (function, L24-L82)

> *Summary: This function configures and initializes a Neo4j graph query engine for RAG by loading a specific text document. It sets up predefined entity types, relationship types, and a potential schema to structure the knowledge graph before returning the ready-to-use engine instance.*


### neo4j_native_query_engine_auto (function, L87-L101)

> *Summary: This function initializes a Neo4j graph query engine by connecting to a local instance and ingesting text data from a specified file path into the database. It returns the configured `Neo4jNativeGraphQueryEngine` ready for querying.*


### test_neo4j_native_query_engine (function, L111-L117)

> *Summary: This test verifies the functionality of a native Neo4j graph query engine by passing a natural language question to it. It asserts that the resulting answer from the query contains the string "BUZZ".*


### test_neo4j_native_query_auto (function, L127-L133)

> *Summary: This test verifies that an auto-generated Neo4j graph query correctly answers a specific question about employer information. It takes a `Neo4jNativeGraphQueryEngine` instance as input and asserts the resulting answer contains the string "BUZZ".*


### test_neo4j_add_records (function, L138-L152)

> *Summary: This test verifies the `add_records` method of a Neo4j graph engine by feeding it documents from a specified text file. It then queries the populated graph with a question about "The Matrix" to assert that the expected answer, mentioning "Keanu Reeves," is present in the result.*

