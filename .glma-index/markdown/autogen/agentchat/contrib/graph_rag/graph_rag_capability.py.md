# autogen/agentchat/contrib/graph_rag/graph_rag_capability.py

1 class(es): GraphRagCapability. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GraphRagCapability | class |  |

## Chunks

### GraphRagCapability (class, L14-L63)

> *Summary: Provides graph-based Retrieval Augmented Generation (RAG) functionality by wrapping a `GraphQueryEngine`. It allows an agent to build a knowledge graph from documents, retrieve relevant information based on conversation history, and generate answers.*


### __init__ (method, L57-L59, parent: GraphRagCapability)

> *Summary: Initializes the component by accepting a `GraphQueryEngine` instance. This sets up the necessary infrastructure for performing Retrieval Augmented Generation using graph data.*


### add_to_agent (method, L61-L63, parent: GraphRagCapability)

> *Summary: Attaches this graph RAG functionality to a specified `ConversableAgent` instance. It modifies the provided agent object to incorporate the retrieval-augmented generation capabilities.*

