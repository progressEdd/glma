# autogen/beta/config/openai/openai_responses_client.py

2 class(es): CreateOptions, OpenAIResponsesClient. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CreateOptions | class |  |
| OpenAIResponsesClient | class |  |

## Chunks

### CreateOptions (class, L52-L66)

> *Summary: Defines a structure for configuring API requests to an OpenAI-like service. It accepts parameters such as model name, generation settings (temperature, max tokens), and request behavior flags like streaming and tool call limits.*


### OpenAIResponsesClient (class, L69-L263)

> *Summary: This class acts as a client to interact with OpenAI-like APIs for language model responses. It takes configuration parameters like API keys and base URLs upon initialization and exposes an asynchronous call method that accepts messages, context, tools, and response schemas to generate a structured `ModelResponse`. The core behavior involves either processing the full synchronous response or streaming chunks of data while handling reasoning events, tool calls, and file generation.*


### __init__ (method, L70-L98, parent: OpenAIResponsesClient)

> *Summary: Initializes a client by wrapping an `AsyncOpenAI` instance with provided API credentials and configuration parameters like timeouts and retry limits. It also stores streaming preferences derived from optional creation options.*


### __call__ (method, L100-L138, parent: OpenAIResponsesClient)

> *Summary: This method constructs and sends a request to an OpenAI client using provided messages, context, optional tools, and response schema. It processes the resulting API response, either as a complete object or by streaming it back based on configuration.*


### _process_response (method, L140-L192, parent: OpenAIResponsesClient)

> *Summary: This method processes a raw `Response` object from an OpenAI interaction to extract structured data for the conversation context. It iterates through response items, sending reasoning events, model messages, and tool call/result events as appropriate, finally returning a consolidated `ModelResponse` containing the message, tool calls, usage statistics, and any generated files.*


### _process_stream (method, L194-L263, parent: OpenAIResponsesClient)

> *Summary: Processes an asynchronous stream of OpenAI response events to aggregate text content, tool calls, and file data. It yields intermediate updates to a conversation context while collecting final details like usage, model name, and finish reason before returning a complete `ModelResponse`.*

