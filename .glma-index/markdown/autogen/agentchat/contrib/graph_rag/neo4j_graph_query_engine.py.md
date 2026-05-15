# autogen/agentchat/contrib/graph_rag/neo4j_graph_query_engine.py

1 class(es): Neo4jGraphQueryEngine. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Neo4jGraphQueryEngine | class |  |

## Chunks

### Neo4jGraphQueryEngine (class, L30-L263)

> *Summary: This class manages a property graph index backed by Neo4j, allowing users to build and query knowledge graphs from documents. It initializes the database with input files or connects to an existing one, using LLMs and optional schemas to extract entity-relationship triplets for storage and retrieval via a chat engine.*


### __init__ (method, L51-L92, parent: Neo4jGraphQueryEngine)

> *Summary: Configures a Neo4j graph query engine by accepting connection details (host, port, credentials) and optional components like an LLM, embedding model, and predefined schemas for entity/relation constraints. It initializes the necessary connections and defaults to using GPT-4o and OpenAI embeddings if not provided.*


### init_db (method, L94-L118, parent: Neo4jGraphQueryEngine)

> *Summary: This method initializes a knowledge graph by loading input documents and connecting to a Neo4j database via `Neo4jPropertyGraphStore`. It then clears any existing graph data before building the index using document embeddings and specialized graph extractors.*


### connect_db (method, L120-L137, parent: Neo4jGraphQueryEngine)

> *Summary: Establishes a connection to a Neo4j knowledge graph database using provided credentials and host details. It initializes the property graph store, creates necessary KG extractors, and builds an index over the existing graph structure.*


### add_records (method, L139-L164, parent: Neo4jGraphQueryEngine)

> *Summary: This method ingests a list of `Document` objects, extracts their content using `SimpleDirectoryReader`, and inserts the resulting documents into an indexed knowledge graph. It returns `True` upon successful insertion or `False` if any error occurs during the process.*


### query (method, L166-L189, parent: Neo4jGraphQueryEngine)

> *Summary: This method queries a property graph using an initialized LlamaIndex chat engine configured for `CONDENSE_PLUS_CONTEXT`. It takes a user question and returns a `GraphStoreQueryResult` containing the generated answer.*


### _clear (method, L191-L196, parent: Neo4jGraphQueryEngine)

> *Summary: This method empties the entire graph store by executing a Cypher query that deletes all nodes and relationships within the database. It operates on the internal `graph_store` driver to perform this complete data removal.*


### _load_doc (method, L198-L231, parent: Neo4jGraphQueryEngine)

> *Summary: Reads a list of input documents, supporting various file types like PDF, DOCX, and JSON. It separates files into common and JSON types before using respective readers to load the content into a list of `LlamaDocument` objects.*


### _create_kg_extractors (method, L233-L263, parent: Neo4jGraphQueryEngine)

> *Summary: This method generates a list of knowledge graph extractors based on the `strict` configuration. It initializes with a schema-validated extractor if strict mode is enabled, and conditionally adds a dynamic extractor that auto-creates relationships if strict mode is disabled.*

