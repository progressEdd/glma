# test/agentchat/contrib/retrievechat/test_qdrant_retrievechat.py

3 function(s): test_retrievechat, test_qdrant_filter, test_qdrant_search.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_retrievechat | function |  |
| test_qdrant_filter | function |  |
| test_qdrant_search | function |  |

## Chunks

### test_retrievechat (function, L33-L63)

> *Summary: This test sets up an AI agent system using a Qdrant in-memory client to simulate retrieval-augmented generation (RAG). It initiates a chat between the assistant and the RAG proxy agent, feeding it a specific coding problem to test the retrieval functionality.*


### test_qdrant_filter (function, L68-L79)

> *Summary: This test verifies that a Qdrant query correctly filters results based on a search string. It queries an in-memory Qdrant instance populated with documentation, expecting exactly four matching document IDs when filtering for "AutoGen".*


### test_qdrant_search (function, L84-L93)

> *Summary: This test verifies the functionality of a Qdrant search by initializing an in-memory client and populating it with documents from a specified directory. It then executes a semantic query against the "all-my-documents" collection, asserting that the returned results contain relevant content matching the input term.*

