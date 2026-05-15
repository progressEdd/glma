# autogen/tools/experimental/perplexity/perplexity_search.py

6 class(es): Message, Usage, Choice, PerplexityChatCompletionResponse, SearchResponse, PerplexitySearchTool. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Message | class |  |
| Usage | class |  |
| Choice | class |  |
| PerplexityChatCompletionResponse | class |  |
| SearchResponse | class |  |
| PerplexitySearchTool | class |  |

## Chunks

### Message (class, L19-L28)

> *Summary: Defines a data structure for chat messages, requiring both a `role` string indicating the sender and a `content` string holding the message text. This class serves as a standardized representation for conversational turns within the system.*


### Usage (class, L31-L44)

> *Summary: Defines a data structure to encapsulate token usage metrics from an LLM interaction. It accepts and stores the counts for prompt tokens, completion tokens, total tokens, and the context size used during searching.*


### Choice (class, L47-L58)

> *Summary: This data structure models a single option returned by the Perplexity API, holding its sequence index, the termination reason for generation, and the associated response content within a `Message` object. It serves as a standardized container for individual results from the API call.*


### PerplexityChatCompletionResponse (class, L61-L80)

> *Summary: This model defines the structure for a complete response received from the Perplexity API. It encapsulates metadata like ID, model name, and creation time, along with token usage, citation strings, and a list of generated choices.*


### SearchResponse (class, L83-L94)

> *Summary: This model structures the output from a search operation, holding optional textual content and a list of relevant citation URLs. It also includes an optional field to report any errors encountered during the search process.*


### PerplexitySearchTool (class, L97-L249)

> *Summary: This class provides a tool to interact with the Perplexity AI API for web, news, and conversational searches. It accepts configuration like model name, API key, and token limits, executing queries via HTTP POST requests to return structured search results containing content and citations.*


### __init__ (method, L111-L141, parent: PerplexitySearchTool)

> *Summary: Configures a Perplexity search utility by accepting parameters like the model name, API key, maximum tokens, and optional domain filters. It validates these inputs and sets up the necessary configuration for making requests to the Perplexity AI completion endpoint.*


### _validate_tool_config (method, L144-L166, parent: PerplexitySearchTool)

> *Summary: Ensures that provided configuration parameters for the search tool are valid before execution. It checks for the presence of an API key, non-empty model name, positive token limit, and correct type for domain filters, raising `ValueError` upon any failure.*


### _execute_query (method, L168-L213, parent: PerplexitySearchTool)

> *Summary: Sends a POST request with a provided payload to the configured Perplexity API endpoint, using an API key for authorization. It returns a parsed `PerplexityChatCompletionResponse` object or raises a `RuntimeError` upon any network failure, HTTP error, JSON decoding issue, or response validation failure.*


### search (method, L215-L249, parent: PerplexitySearchTool)

> *Summary: Executes a search query against the Perplexity AI API using a provided string input to construct and send a specific payload. It returns a `SearchResponse` containing the resulting content and any associated citations, or an error message if the process fails.*

