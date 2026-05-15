# autogen/agentchat/contrib/graph_rag/neo4j_graph_rag_capability.py

1 class(es): Neo4jGraphCapability. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Neo4jGraphCapability | class |  |

## Chunks

### Neo4jGraphCapability (class, L13-L83)

> *Summary: This class integrates Neo4j property graph capabilities into an agent by overriding its reply mechanism. It takes a `Neo4jGraphQueryEngine` upon initialization and, when added to a `UserProxyAgent`, intercepts incoming messages to execute queries against the graph database using the provided engine. The primary output is the answer retrieved directly from the graph query result.*


### __init__ (method, L21-L23, parent: Neo4jGraphCapability)

> *Summary: Initializes the capability by accepting and storing a `Neo4jGraphQueryEngine` instance for subsequent graph interactions. This sets up the necessary connection to perform knowledge retrieval from a Neo4j database.*


### add_to_agent (method, L25-L44, parent: Neo4jGraphCapability)

> *Summary: This method injects Neo4j GraphRAG functionality into a specified `UserProxyAgent`, ensuring the agent has no LLM configuration. It overrides the agent's default reply mechanism to exclusively use a Neo4j query function for generating responses.*


### _reply_using_neo4j_query (method, L46-L75, parent: Neo4jGraphCapability)

> *Summary: This method executes a query against the Neo4j graph using the last question from the provided conversation history. It returns a tuple indicating success and the answer retrieved directly from the graph query engine.*


### _get_last_question (method, L77-L83, parent: Neo4jGraphCapability)

> *Summary: Extracts the content from a provided conversation history element. It accepts either a string or a dictionary containing a "content" key, returning that content as a string if found, otherwise returning `None`.*

