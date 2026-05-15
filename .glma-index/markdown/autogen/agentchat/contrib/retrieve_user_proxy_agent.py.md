# autogen/agentchat/contrib/retrieve_user_proxy_agent.py

1 class(es): RetrieveUserProxyAgent. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RetrieveUserProxyAgent | class |  |

## Chunks

### RetrieveUserProxyAgent (class, L96-L704)

> *Summary: This class acts as a specialized user proxy agent that retrieves relevant document chunks from a vector database based on embedding similarity before interacting with an assistant. It manages complex configuration for retrieval (e.g., chunking, model selection) and dynamically updates the conversation context when specific trigger phrases are detected in messages.*


### __init__ (method, L101-L322, parent: RetrieveUserProxyAgent)

> *Summary: Initializes a retrieval agent by accepting configuration for its behavior, including human input modes and vector database settings. It parses these inputs to set up internal parameters like chunking strategy, model selection, and the specific vector store instance or client connection.*


### _init_db (method, L324-L394, parent: RetrieveUserProxyAgent)

> *Summary: Initializes the vector database by either creating a new collection or using an existing one based on configuration flags and file path availability. It processes input documents—either chunking raw files from a directory or using pre-existing data—and inserts them into the specified collection, ensuring no duplicate document IDs are added during insertion.*


### _is_termination_msg_retrievechat (method, L396-L413, parent: RetrieveUserProxyAgent)

> *Summary: Determines if a given message signals the end of an interaction based on its content. It returns `True` if the message contains no detectable Python code and does not trigger context updates for either question answering or code generation scenarios.*


### _check_update_context_before_send (method, L415-L441, parent: RetrieveUserProxyAgent)

> *Summary: If a received message contains "UPDATE CONTEXT", this method retrieves and regenerates the message content using relevant documents based on the agent's problem. It iteratively attempts to fetch more context if the initial retrieval yields no results, ultimately returning the modified or original message structure.*


### get_max_tokens (method, L444-L452, parent: RetrieveUserProxyAgent)

> *Summary: Determines the maximum token limit based on a provided model name string. It returns specific values (32000, 16000, 8000, or 4000) depending on whether "32k", "16k", "gpt-4", or none of those substrings are present in the input model identifier.*


### _reset (method, L454-L460, parent: RetrieveUserProxyAgent)

> *Summary: Resets the agent's state by clearing tracking variables for document indices, query results, and associated content/IDs. If not running in an intermediate mode, it also clears sets and lists holding intermediate answers and document contents.*


### _get_context (method, L462-L495, parent: RetrieveUserProxyAgent)

> *Summary: This method filters and aggregates document contents from a list of query results, ensuring the total token count does not exceed a predefined maximum. It skips documents already processed or those exceeding the size limit, returning a concatenated string of the selected content.*


### _generate_message (method, L497-L513, parent: RetrieveUserProxyAgent)

> *Summary: This method constructs a prompt string by selecting a template based on the provided `task` argument. It uses the agent's internal problem statement and the input document contents to format the final message, returning "TERMINATE" if no context is supplied.*


### _check_update_context (method, L515-L522, parent: RetrieveUserProxyAgent)

> *Summary: Determines if a given message warrants context updates by checking for specific trigger phrases ("UPDATE CONTEXT") or the absence of a predefined answer prefix within the content. It returns two boolean flags indicating these distinct conditions.*


### _generate_retrieve_user_reply (method, L524-L581, parent: RetrieveUserProxyAgent)

> *Summary: Determines whether to update the conversation context and reset history based on message content and configuration flags. If conditions are met, it extracts intermediate information, potentially re-runs document retrieval using either the problem statement or the extracted info as a query, clears histories, and returns a success status along with generated context.*


### retrieve_docs (method, L583-L654, parent: RetrieveUserProxyAgent)

> *Summary: This method retrieves relevant documents by querying a vector database using a given problem string, optionally filtering by an exact search term and limiting the number of results. It stores the retrieved document-distance tuples in the instance's `_results` attribute, handling initialization logic for both existing and newly created database connections.*


### message_generator (method, L657-L682, parent: RetrieveUserProxyAgent)

> *Summary: This method constructs an initial prompt for a recipient agent by first executing document retrieval using the provided problem, result count, and optional search string. It then formats the retrieved document contents into a final message ready for transmission.*


### run_code (method, L684-L704, parent: RetrieveUserProxyAgent)

> *Summary: Executes provided code using an IPython kernel if the language is Python and the environment supports it; otherwise, it delegates to a superclass method. It specifically blocks execution for shell commands or any code starting with `!` or `pip`.*

