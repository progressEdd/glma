# autogen/beta/config/gemini/events.py

3 class(es): GeminiToolCallEvent, GeminiServerToolCallEvent, GeminiServerToolResultEvent. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GeminiToolCallEvent | class |  |
| GeminiServerToolCallEvent | class |  |
| GeminiServerToolResultEvent | class |  |

## Chunks

### GeminiToolCallEvent (class, L25-L28)

> *Summary: Represents a function tool call originating from Gemini, inheriting from `ToolCallEvent`. It optionally stores internal thinking metadata as a byte string.*


### GeminiServerToolCallEvent (class, L31-L56)

> *Summary: Represents an event signaling a tool call to the Gemini server, capable of being constructed from executable code parts or grounding metadata. It serializes necessary information like code/language or web search queries into arguments for the tool invocation.*


### from_executable_code (method, L36-L47, parent: GeminiServerToolCallEvent)

> *Summary: Constructs a `GeminiServerToolCallEvent` from a `types.Part` object containing executable code. It serializes the code and its associated language into the event's arguments if the part has executable content.*


### from_grounding (method, L50-L56, parent: GeminiServerToolCallEvent)

> *Summary: Creates a `GeminiServerToolCallEvent` instance from grounding metadata and a specified name. It serializes the web search queries from the input metadata into the event's arguments field.*


### GeminiServerToolResultEvent (class, L59-L95)

> *Summary: This class models the result of a tool execution or grounding event from Gemini. It provides factory methods to construct instances either from code execution results (providing output and outcome) or from grounding metadata (providing source URLs and search queries).*


### from_code_execution_result (method, L64-L75, parent: GeminiServerToolResultEvent)

> *Summary: Constructs a `GeminiServerToolResultEvent` from a code execution result contained within a message part. It extracts the output and outcome to build a `ToolResult`, returning `None` if no execution result is present in the input part.*


### from_grounding (method, L78-L95, parent: GeminiServerToolResultEvent)

> *Summary: Constructs a `GeminiServerToolResultEvent` from grounding metadata by extracting web URIs and associated titles/domains into input parts. It also includes the original web search queries in the event's metadata if any grounding chunks are present.*

