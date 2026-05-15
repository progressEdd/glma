# autogen/agentchat/contrib/graph_rag/neo4j_native_graph_rag_capability.py

1 class(es): Neo4jNativeGraphCapability. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Neo4jNativeGraphCapability | class |  |

## Chunks

### Neo4jNativeGraphCapability (class, L13-L93)

> *Summary: This capability integrates Neo4j's native query engine into an agent, allowing it to retrieve information directly from a graph database instead of using an LLM for generation. It takes conversation history and the agent's system message as input to construct a query via its internal engine, returning either the retrieved answer or a default failure message.*


### __init__ (method, L19-L21, parent: Neo4jNativeGraphCapability)

> *Summary: Initializes the GraphRAG capability by accepting and storing an instance of a `Neo4jNativeGraphQueryEngine`. This allows the component to interact directly with Neo4j for graph-based retrieval tasks.*


### add_to_agent (method, L23-L39, parent: Neo4jNativeGraphCapability)

> *Summary: This method injects native Neo4j GraphRAG functionality into a specified agent. It validates that the target agent has no LLM configuration and then overrides its reply mechanism to exclusively use a function that generates responses based on Neo4j queries.*


### _reply_using_native_neo4j_query (method, L41-L67, parent: Neo4jNativeGraphCapability)

> *Summary: Executes a query against the Neo4j graph using a summarized question derived from conversation history and the recipient's system message. It returns a success status along with the retrieved answer or a default fallback message if no results are found.*


### _messages_summary (method, L69-L93, parent: Neo4jNativeGraphCapability)

> *Summary: Generates a formatted string summarizing conversation history, filtering out messages containing tool calls or responses. It accepts either a raw string or a list of message dictionaries (including name and content) as input, returning the structured summary prefixed by an optional system message.*

