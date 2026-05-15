# autogen/beta/config/anthropic/anthropic_client.py

2 class(es): CreateOptions, AnthropicClient. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CreateOptions | class |  |
| AnthropicClient | class |  |

## Chunks

### CreateOptions (class, L49-L58)

> *Summary: Defines a structure for configuring API calls to Anthropic. It accepts optional parameters like model name, token limits, sampling controls (temperature, top\_p, top\_k), stopping sequences, streaming preference, and metadata.*


### AnthropicClient (class, L61-L339)

> *Summary: This class wraps the Anthropic API client to handle interactions with large language models. It accepts configuration parameters like API keys and caching settings, then processes incoming messages, tools, and context to make streaming or non-streaming calls to generate model responses. The core behavior involves managing conversation state, handling tool use/results, and emitting events for both streamed and complete responses.*


### __init__ (method, L62-L86, parent: AnthropicClient)

> *Summary: Initializes an Anthropic client by configuring an underlying `AsyncAnthropic` instance with provided credentials and network settings. It also stores configuration flags like streaming preference, caching status, and any additional request body data for later use.*


### __call__ (method, L88-L190, parent: AnthropicClient)

> *Summary: This method executes a call to the Anthropic API, taking messages, conversation context, and optional tools/schemas as input. It constructs complex request arguments, handling system prompts, tool definitions, and specific beta header configurations based on the inputs. The output is either a streamed or final `ModelResponse`, with built-in logic to handle multi-turn conversations if the initial response indicates a "pause\_turn."*


### _emit_builtin_tool_events (method, L192-L205, parent: AnthropicClient)

> *Summary: This method processes a list of content blocks to emit typed server-tool events for the conversation context. It specifically checks for `ServerToolUseBlock` and `AnthropicServerToolResultBlockType` instances, converting them into respective event objects before sending them via the context.*


### _build_system (method, L207-L211, parent: AnthropicClient)

> *Summary: Concatenates an iterable of strings into a single text block. If caching is enabled, it wraps the resulting text in a specific structure; otherwise, it returns the raw string.*


### _inject_cache_control (method, L214-L222, parent: AnthropicClient)

> *Summary: Modifies the last user message in a sequence of messages by injecting an ephemeral cache control directive. This ensures that the initial user input is marked as temporary for API calls.*


### _process_response (method, L224-L268, parent: AnthropicClient)

> *Summary: This method parses an incoming `Message` response from the Anthropic API, iterating through its content blocks to extract text, tool calls, and server tool interactions. It aggregates these components into a structured `ModelResponse`, including usage statistics and finish reason.*


### _process_stream (method, L270-L339, parent: AnthropicClient)

> *Summary: This method processes a streaming response from an Anthropic API call, accumulating text content and tracking tool use events as chunks arrive. It yields intermediate messages to the context while collecting final tool calls and returning a complete `ModelResponse` containing the aggregated message, tool calls, usage statistics, and finish reason upon stream completion.*

