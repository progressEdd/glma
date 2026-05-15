# autogen/agentchat/contrib/qdrant_retrieve_user_proxy_agent.py

2 function(s): create_qdrant_from_dir, query_qdrant. 1 class(es): QdrantRetrieveUserProxyAgent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| QdrantRetrieveUserProxyAgent | class |  |
| create_qdrant_from_dir | function |  |
| query_qdrant | function |  |

## Chunks

### QdrantRetrieveUserProxyAgent (class, L35-L164)

> *Summary: This class extends a base agent to incorporate retrieval capabilities using Qdrant. It initializes with configuration for human interaction and the vector database setup, then uses `retrieve_docs` to query documents from Qdrant based on an input problem string, returning filtered search results.*


### __init__ (method, L36-L121, parent: QdrantRetrieveUserProxyAgent)

> *Summary: Initializes an agent designed for retrieving information from a Qdrant vector database, accepting configuration for human interaction modes, termination conditions, and detailed retrieval settings like document paths, embedding models, and indexing configurations. It sets up the necessary internal components based on the provided `retrieve_config`, including connecting to a Qdrant client instance or defaulting to an in-memory one.*


### retrieve_docs (method, L123-L164, parent: QdrantRetrieveUserProxyAgent)

> *Summary: Retrieves relevant documents from a Qdrant vector store based on a given problem string and optional exact match criteria. It initializes the collection if it doesn't exist, queries the database, transforms the output format, and filters the results by a predefined distance threshold before returning them.*


### create_qdrant_from_dir (function, L168-L270)

> *Summary: Ingests files from a specified path (directory, file, or URL), splits their content into chunks based on provided parameters, and populates a Qdrant vector collection. It handles collection creation if it doesn't exist, upserts the generated document chunks in batches, and optionally creates a payload index for efficient filtering.*


### query_qdrant (function, L274-L331)

> *Summary: Performs a similarity search against a specified Qdrant collection using provided query texts and optional filters. It accepts client configuration, collection name, and a search string to return structured results containing IDs, documents, scores (distances), and metadata for each query.*

