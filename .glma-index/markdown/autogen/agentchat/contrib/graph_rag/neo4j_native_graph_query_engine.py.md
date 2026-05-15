# autogen/agentchat/contrib/graph_rag/neo4j_native_graph_query_engine.py

1 class(es): Neo4jNativeGraphQueryEngine. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Neo4jNativeGraphQueryEngine | class |  |

## Chunks

### Neo4jNativeGraphQueryEngine (class, L29-L210)

> *Summary: This class manages a Neo4j knowledge graph, initializing connections and components like embedding models and LLMs based on provided configuration. It allows users to build the graph from input documents (text or PDF), create vector indexes, and subsequently query the structured data using natural language questions via an integrated RAG pipeline.*


### __init__ (method, L35-L75, parent: Neo4jNativeGraphQueryEngine)

> *Summary: Sets up a Neo4j graph query engine by establishing a connection to the specified database using provided credentials. It initializes default embedding, knowledge graph generation, and querying LLMs if none are supplied during instantiation.*


### init_db (method, L77-L106, parent: Neo4jNativeGraphQueryEngine)

> *Summary: This method initializes a Neo4j graph database by first clearing any existing data and then building a knowledge graph from the provided input document. It extracts nodes and relationships, followed by creating a vector index for subsequent retrieval operations.*


### add_records (method, L108-L123, parent: Neo4jNativeGraphQueryEngine)

> *Summary: This method ingests a list of `Document` objects and persists them into the Neo4j database by calling an internal graph building function. It validates that all provided records are instances of `Document` before proceeding, returning `True` upon successful addition.*


### query (method, L125-L142, parent: Neo4jNativeGraphQueryEngine)

> *Summary: This method takes a natural language question string and uses it to query the Neo4j graph via a RAG pipeline. It initializes a vector retriever and a `GraphRAG` instance, then returns the extracted answer wrapped in a `GraphStoreQueryResult`.*


### _create_index (method, L144-L159, parent: Neo4jNativeGraphQueryEngine)

> *Summary: This method establishes a vector index within the Neo4j graph for storing embeddings associated with "Chunk" nodes. It takes an index name as input and configures the index using Euclidean distance on the specified embedding property.*


### _clear_db (method, L161-L165, parent: Neo4jNativeGraphQueryEngine)

> *Summary: This method executes a Cypher query against the connected Neo4j driver to completely remove all nodes and relationships from the database. It logs informational messages before and after the deletion process completes.*


### _initialize_kg_builders (method, L167-L190, parent: Neo4jNativeGraphQueryEngine)

> *Summary: Sets up two knowledge graph builders: one for text-based input and another specifically for PDF documents. Both builders utilize the provided Neo4j driver, embeddings model, LLM, schema definitions, and error handling configuration.*


### _build_graph (method, L192-L210, parent: Neo4jNativeGraphQueryEngine)

> *Summary: This method constructs a knowledge graph by iterating over a list of input documents. It processes text files by reading their content and passing it to an asynchronous text builder, or handles PDF files by passing their file path to an asynchronous PDF builder.*

