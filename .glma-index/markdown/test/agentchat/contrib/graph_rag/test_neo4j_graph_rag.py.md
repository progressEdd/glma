# test/agentchat/contrib/graph_rag/test_neo4j_graph_rag.py

7 function(s): neo4j_query_engine_with_json, neo4j_query_engine, neo4j_query_engine_auto, test_neo4j_query_engine, test_neo4j_add_records, test_neo4j_auto, test_neo4j_json_auto.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| neo4j_query_engine_with_json | function |  |
| neo4j_query_engine | function |  |
| neo4j_query_engine_auto | function |  |
| test_neo4j_query_engine | function |  |
| test_neo4j_add_records | function |  |
| test_neo4j_auto | function |  |
| test_neo4j_json_auto | function |  |

## Chunks

### neo4j_query_engine_with_json (function, L27-L41)

> *Summary: Initializes and configures a `Neo4jGraphQueryEngine` instance by connecting to a local Neo4j database using provided credentials. It then ingests data from a specified JSON file path, building a new property graph within the engine.*


### neo4j_query_engine (function, L46-L94)

> *Summary: Initializes a Neo4j graph query engine by loading a specified document, defining allowed entities and relations, and setting up a strict schema for triplet extraction. It returns the configured `Neo4jGraphQueryEngine` instance after ingesting data into the database.*


### neo4j_query_engine_auto (function, L99-L113)

> *Summary: Initializes and returns a `Neo4jGraphQueryEngine` instance configured to connect to a local Neo4j database. It processes a specified text file (`BUZZ_Employee_Handbook.txt`) during initialization to build the property graph within the database.*


### test_neo4j_query_engine (function, L123-L132)

> *Summary: This test verifies the Neo4j query engine's functionality by passing a natural language question to it. It asserts that the resulting answer from the database contains the string "BUZZ".*


### test_neo4j_add_records (function, L142-L156)

> *Summary: This test verifies the `add_records` method by feeding it a text document from a specified path. It then queries the Neo4j graph using a question related to the input data and asserts that the expected answer, "Keanu Reeves," is present in the returned result.*


### test_neo4j_auto (function, L166-L172)

> *Summary: This test verifies the functionality of an auto-generated property graph query engine by submitting a specific question to it. It asserts that the resulting answer from the query contains the string "BUZZ".*


### test_neo4j_json_auto (function, L182-L188)

> *Summary: This test verifies that a Neo4j graph query engine can correctly answer a question by automatically generating a property graph from a JSON input. It asserts that the resulting answer contains specific expected information, such as "PRImA".*

