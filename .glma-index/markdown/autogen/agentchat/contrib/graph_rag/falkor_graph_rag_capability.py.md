# autogen/agentchat/contrib/graph_rag/falkor_graph_rag_capability.py

1 class(es): FalkorGraphRagCapability. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FalkorGraphRagCapability | class |  |

## Chunks

### FalkorGraphRagCapability (class, L13-L103)

> *Summary: This capability integrates FalkorDB's GraphRAG functionality into an agent by registering a custom reply function that queries the graph database. It takes a `FalkorGraphQueryEngine` upon initialization and uses conversation history, along with the agent's system message, to formulate a query, returning the retrieved answer or a default fallback message.*


### __init__ (method, L20-L22, parent: FalkorGraphRagCapability)

> *Summary: Initializes the RAG capability by accepting and storing an instance of a `FalkorGraphQueryEngine`. This allows the object to perform graph-based queries using the provided engine.*


### add_to_agent (method, L24-L48, parent: FalkorGraphRagCapability)

> *Summary: Attaches GraphRAG functionality to a specified `ConversableAgent` instance. It validates that the agent is of the correct type and has no LLM configuration before overriding its reply mechanism to use FalkorDB queries as the primary response method.*


### _reply_using_falkordb_query (method, L50-L77, parent: FalkorGraphRagCapability)

> *Summary: Queries a knowledge base via FalkorDB using conversation history and the recipient's system message to generate a response. It returns a success status along with the retrieved answer or a default fallback message if no results are found.*


### _messages_summary (method, L79-L103, parent: FalkorGraphRagCapability)

> *Summary: Generates a formatted string summarizing conversation history, filtering out messages containing tool calls or responses. It accepts either a raw string or a list of message dictionaries and prepends the system message if provided.*

