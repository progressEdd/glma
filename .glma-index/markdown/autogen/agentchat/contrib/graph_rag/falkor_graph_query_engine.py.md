# autogen/agentchat/contrib/graph_rag/falkor_graph_query_engine.py

1 class(es): FalkorGraphQueryEngine. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FalkorGraphQueryEngine | class |  |

## Chunks

### FalkorGraphQueryEngine (class, L23-L167)

> *Summary: This class wraps a FalkorDB KnowledgeGraph, managing connections and operations for building and querying knowledge graphs. It initializes with database credentials and an optional LLM/ontology, allowing users to either connect to an existing graph or build one from input documents before executing queries.*


### __init__ (method, L26-L61, parent: FalkorGraphQueryEngine)

> *Summary: Sets up a connection to a FalkorDB knowledge graph instance using provided credentials and configuration parameters. It initializes the database client and sets defaults for the LLM model and ontology if not explicitly supplied.*


### connect_db (method, L63-L87, parent: FalkorGraphQueryEngine)

> *Summary: Establishes a connection to an existing knowledge graph by first verifying its existence and loading the associated ontology from the database. If successful, it initializes a `KnowledgeGraph` instance and creates a persistent chat session for querying.*


### init_db (method, L89-L121, parent: FalkorGraphQueryEngine)

> *Summary: This method constructs and initializes a knowledge graph by processing a list of input `Document` objects, extracting sources from them. It automatically generates an ontology if one isn't provided, saves it to the database, sets up the graph connection, processes the sources, and establishes a chat session for subsequent interaction.*


### add_records (method, L123-L124, parent: FalkorGraphQueryEngine)

> *Summary: This method is intended to ingest a list of `Document` objects into the database but currently raises an error because the underlying FalkorDB SDK does not support this operation. It expects a list of documents as input and returns a boolean upon successful execution (though it will always fail in its current state).*


### query (method, L126-L142, parent: FalkorGraphQueryEngine)

> *Summary: This method queries a knowledge graph using a provided string question, optionally including message history via `kwargs`. It returns a structured result containing the AI's textual answer derived from the chat session.*


### delete (method, L144-L151, parent: FalkorGraphQueryEngine)

> *Summary: Removes a graph and its associated data from the database by first listing all available graphs. It checks for both the main graph name and the ontology table name before executing deletion commands on the underlying database connection.*


### __get_ontology_storage_graph (method, L153-L154, parent: FalkorGraphQueryEngine)

> *Summary: Retrieves the specific graph structure from the underlying database using a predefined table name. This method returns a `Graph` object representing the ontology storage.*


### _save_ontology_to_db (method, L156-L161, parent: FalkorGraphQueryEngine)

> *Summary: This method persists the provided `Ontology` object into a dedicated database table named `{graph_name}_ontology`. It first checks if the graph already exists to prevent overwriting before saving the ontology data.*


### _load_ontology_from_db (method, L163-L167, parent: FalkorGraphQueryEngine)

> *Summary: Retrieves the knowledge graph structure from a specified database table, validating its existence first. It then converts this schema graph into an `Ontology` object for use by the query engine.*

