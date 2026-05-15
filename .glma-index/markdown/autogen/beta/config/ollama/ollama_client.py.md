# autogen/beta/config/ollama/ollama_client.py

2 class(es): CreateOptions, OllamaClient. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CreateOptions | class |  |
| OllamaClient | class |  |

## Chunks

### CreateOptions (class, L33-L40)

> *Summary: Defines a structure for configuring model generation parameters, allowing optional inputs like temperature, top\_p, and maximum tokens. This dictionary holds settings that control the behavior of an LLM inference call.*


### OllamaClient (class, L43-L193)

> *Summary: This class interfaces with the Ollama API to generate responses from a specified model. It accepts conversation history and optional tools/schemas as input, returning a structured `ModelResponse` containing the generated message, tool calls, and usage statistics, handling both streaming and non-streaming requests.*


### __init__ (method, L44-L55, parent: OllamaClient)

> *Summary: Initializes an asynchronous client configured to interact with a specific Ollama model at a given host. It stores the model name, streaming preference, and any non-null creation options for later use.*


### __call__ (method, L57-L86, parent: OllamaClient)

> *Summary: This method constructs and executes an API call to Ollama based on provided messages, conversation context, optional tools, and response schema. It handles both streaming and non-streaming requests by preparing necessary arguments like message conversions and tool definitions before invoking the underlying client methods.*


### _call_non_streaming (method, L88-L134, parent: OllamaClient)

> *Summary: This method sends a list of messages and optional keyword arguments to the underlying Ollama client for a non-streaming chat request. It processes the resulting response by extracting content, tool calls, token usage statistics, and reasoning steps before returning a structured `ModelResponse`.*


### _call_streaming (method, L136-L193, parent: OllamaClient)

> *Summary: Receives a list of messages and optional keyword arguments to initiate a streaming chat request via the underlying client. It yields content chunks as they arrive, tracks tool calls, and aggregates usage metrics before returning a final `ModelResponse` containing the complete message, tool call events, and metadata.*

