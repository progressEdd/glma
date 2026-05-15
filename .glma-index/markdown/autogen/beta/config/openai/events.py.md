# autogen/beta/config/openai/events.py

3 class(es): OpenAIServerToolCallEvent, OpenAIServerToolResultEvent, OpenAIReasoningEvent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OpenAIServerToolCallEvent | class |  |
| OpenAIServerToolResultEvent | class |  |
| OpenAIReasoningEvent | class |  |

## Chunks

### OpenAIServerToolCallEvent (class, L37-L67)

> *Summary: This class models an event representing a tool call made to an OpenAI server. It converts various input item types—such as web search responses or code interpreter results—into a standardized event structure containing the necessary ID, name, and serialized arguments.*


### from_item (method, L41-L67, parent: OpenAIServerToolCallEvent)

> *Summary: Converts various response objects—such as web search results, code interpreter outputs, or image generation calls—into a standardized tool call event structure. It inspects the input item type to correctly populate the `id`, `name`, and serialized `arguments` for the resulting event object.*


### OpenAIServerToolResultEvent (class, L70-L116)

> *Summary: Constructs an event representing the outcome of a tool execution by inspecting various input types. It processes `ResponseFunctionWebSearch`, `ResponseCodeInterpreterToolCall`, or `ImageGenerationCall` objects to build structured inputs (URLs, text, images) and associated metadata for the resulting tool result.*


### from_item (method, L72-L116, parent: OpenAIServerToolResultEvent)

> *Summary: Converts various tool response items (like web search results, code execution outputs, or image generation calls) into a standardized `ToolResultEvent`. It inspects the input item type to extract relevant data—such as URLs, logs, queries, and metadata—and packages it for event emission.*


### OpenAIReasoningEvent (class, L119-L122)

> *Summary: This class encapsulates a reasoning event from an OpenAI model, holding a `ResponseReasoningItem` as its primary data. It inherits from `ModelReasoning`, suggesting it's part of a structured system for tracking AI thought processes.*

