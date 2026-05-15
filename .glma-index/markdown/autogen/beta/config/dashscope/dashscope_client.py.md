# autogen/beta/config/dashscope/dashscope_client.py

2 class(es): CreateOptions, DashScopeClient. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CreateOptions | class |  |
| DashScopeClient | class |  |

## Chunks

### CreateOptions (class, L34-L41)

> *Summary: Defines a structure for configuring generation parameters, accepting optional values like `temperature`, `max_tokens`, and various penalty settings. This dictionary is used to specify how an AI model should generate output during a creation process.*


### DashScopeClient (class, L44-L232)

> *Summary: This client class interfaces with the DashScope API to generate model responses. It accepts messages and optional configuration like tools or response schemas, then executes either a synchronous or streaming call against the configured model endpoint. The output is a `ModelResponse` containing the generated message content, tool calls, and usage statistics.*


### __init__ (method, L45-L57, parent: DashScopeClient)

> *Summary: Initializes a client by storing the specified model name, optional API key, base URL, and streaming preference. It also processes provided creation options, filtering out any that are explicitly set to `None`.*


### __call__ (method, L59-L92, parent: DashScopeClient)

> *Summary: This method executes a call to the DashScope API using provided messages and context. It constructs the necessary request payload by incorporating system prompts if a response schema is present, then either streams or makes a standard asynchronous call based on the client's configuration.*


### _call_non_streaming (method, L94-L154, parent: DashScopeClient)

> *Summary: Executes a non-streaming API call to DashScope using provided messages and optional arguments. It processes the response by sending reasoning content, extracting text from message content (string or list of blocks), collecting tool calls, and returning a structured `ModelResponse` containing the final message, tool events, and usage statistics.*


### _call_streaming (method, L156-L232, parent: DashScopeClient)

> *Summary: This method streams responses from a DashScope model by iterating over chunks received from an asynchronous call. It aggregates the content, tracks token usage, and emits intermediate messages and tool calls to a provided context before returning a final `ModelResponse`.*

