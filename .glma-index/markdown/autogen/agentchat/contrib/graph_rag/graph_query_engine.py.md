# autogen/agentchat/contrib/graph_rag/graph_query_engine.py

2 class(es): GraphStoreQueryResult, GraphQueryEngine. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GraphStoreQueryResult | class |  |
| GraphQueryEngine | class |  |

## Chunks

### GraphStoreQueryResult (class, L16-L24)

> *Summary: This class encapsulates the output from a graph store query, holding both a human-readable answer and a list of intermediate results like entity nodes. It provides structured access to the final response and supporting data derived from the graph traversal.*


### GraphQueryEngine (class, L28-L53)

> *Summary: Defines an interface for graph-based Retrieval Augmented Generation (RAG), requiring methods to initialize the underlying graph database with documents, add new records, and execute natural language queries against the graph. It accepts input documents or new records and returns a structured query result based on the provided question.*


### init_db (method, L34-L45, parent: GraphQueryEngine)

> *Summary: Establishes a connection to a graph database and populates it by extracting nodes and edges from provided input documents, subsequently building necessary indexes. It accepts an optional list of `Document` objects as its sole input.*


### add_records (method, L47-L49, parent: GraphQueryEngine)

> *Summary: This method accepts a list of new data records and persists them into the internal database. It also conditionally updates the knowledge graph based on the added records, returning a boolean indicating success.*


### query (method, L51-L53, parent: GraphQueryEngine)

> *Summary: Transforms an input string question into a database query to retrieve information from a graph store. It accepts the question and an optional number of results, returning a `GraphStoreQueryResult` object containing the findings.*

