# autogen/beta/config/gemini/gemini_client.py

2 class(es): CreateConfig, GeminiClient. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CreateConfig | class |  |
| GeminiClient | class |  |

## Chunks

### CreateConfig (class, L45-L54)

> *Summary: Defines a configuration structure for Gemini API calls, allowing optional settings like temperature, token limits, and penalty values. It accepts various numerical and list inputs to control the model's generation behavior.*


### GeminiClient (class, L57-L279)

> *Summary: This class manages interaction with the Gemini API, initializing a client based on provided configuration like model name and credentials. It exposes an asynchronous interface to send messages, optionally including tools and response schemas, returning a structured `ModelResponse` which can be either complete or streamed chunk-by-chunk.*


### __init__ (method, L58-L82, parent: GeminiClient)

> *Summary: Initializes a Gemini client by configuring it with a specified model name and optional authentication details like API keys, service account credentials, project, and location. It sets up the underlying `genai.Client` instance based on these inputs and stores configuration flags for streaming and content caching.*


### __call__ (method, L84-L129, parent: GeminiClient)

> *Summary: This method orchestrates a call to the Gemini API by transforming input messages and configuration parameters. It constructs the necessary request payload, handling optional system prompts, tools, and response schemas before either streaming or fetching a single model response.*


### _process_response (method, L131-L198, parent: GeminiClient)

> *Summary: This method processes a `GenerateContentResponse` from the Gemini API to extract various components like text messages, tool calls, and code execution results. It iterates through candidates, sending reasoning, content, function calls, and code/grounding events to the provided conversation context before returning a structured `ModelResponse`.*


### _process_stream (method, L200-L279, parent: GeminiClient)

> *Summary: Processes a streaming response from a Gemini model to extract content, tool calls, and usage statistics. It asynchronously sends chunks of text, reasoning steps, function calls, and code execution results to the provided context before returning a final `ModelResponse`.*

