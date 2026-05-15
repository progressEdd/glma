# autogen/beta/config/openai/openai_client.py

2 class(es): CreateOptions, OpenAIClient. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CreateOptions | class |  |
| OpenAIClient | class |  |

## Chunks

### CreateOptions (class, L37-L67)

> *Summary: Defines a structure for configuring API calls to an OpenAI-compatible service. It accepts various optional parameters like temperature, token limits, and tool configurations, while mandating the `stream` flag and allowing for model specification via `model`.*


### OpenAIClient (class, L70-L244)

> *Summary: This class wraps the OpenAI API client to facilitate LLM interactions within a conversational context. It accepts configuration parameters like API keys and timeouts, then processes incoming messages against tools or response schemas to generate a `ModelResponse`, handling both synchronous completions and asynchronous streaming responses.*


### __init__ (method, L71-L99, parent: OpenAIClient)

> *Summary: Initializes an OpenAI client by configuring an underlying `AsyncOpenAI` instance with provided credentials and network settings. It also stores streaming preferences derived from optional creation options.*


### __call__ (method, L101-L135, parent: OpenAIClient)

> *Summary: This method interfaces with the OpenAI API to generate model responses based on a sequence of messages and conversation context. It constructs the necessary API call parameters, including optional response schemas and tools, then processes either a streamed or complete response from the underlying client.*


### _process_completion (method, L137-L169, parent: OpenAIClient)

> *Summary: This method transforms an OpenAI `ChatCompletion` object into a structured `ModelResponse`. It extracts and sends reasoning, message content, and any tool calls from the completion to the provided conversation context before returning the final response structure.*


### _process_stream (method, L171-L244, parent: OpenAIClient)

> *Summary: This asynchronous method consumes a streaming response from an OpenAI API call, accumulating content and tool calls chunk by chunk. It yields intermediate messages and reasoning updates to the provided context while aggregating all final data into a comprehensive `ModelResponse` upon stream completion.*

