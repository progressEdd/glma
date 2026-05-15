# autogen/beta/config/anthropic/events.py

2 class(es): AnthropicServerToolCallEvent, AnthropicServerToolResultEvent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AnthropicServerToolCallEvent | class |  |
| AnthropicServerToolResultEvent | class |  |

## Chunks

### AnthropicServerToolCallEvent (class, L58-L77)

> *Summary: This class represents an event signaling a tool call initiated by the Anthropic server. It converts a `ServerToolUseBlock` into this event, mapping specific block names like "web\_search" or "code\_execution" to predefined internal tool names.*


### from_block (method, L62-L77, parent: AnthropicServerToolCallEvent)

> *Summary: This method transforms a `ServerToolUseBlock` into an Anthropic server tool call event by mapping the block's name to a predefined constant. It returns an instance of the specified class containing the block's ID, standardized name, serialized input arguments, and the original block object, or `None` if the block type is unrecognized.*


### AnthropicServerToolResultEvent (class, L80-L184)

> *Summary: This class transforms various tool result blocks (like web search, file fetching, or code execution results) into a standardized event structure. It inspects the input block type to extract relevant content, errors, and metadata, producing an instance containing structured parts and associated metadata.*


### from_block (method, L84-L184, parent: AnthropicServerToolResultEvent)

> *Summary: Transforms a specific tool result block into an event object by inspecting the block's type. It processes various input types—such as web search results, fetched documents, code execution outputs, or text editor actions—to populate the resulting parts and metadata accordingly before returning the constructed event.*

