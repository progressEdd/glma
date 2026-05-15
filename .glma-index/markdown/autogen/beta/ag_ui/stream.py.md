# autogen/beta/ag_ui/stream.py

5 function(s): run_stream, map_agui_messages_to_events, _stringify_tool_result, _get_timestamp, _encode_context. 2 class(es): AGUIStream, AGStreamInput. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AGUIStream | class |  |
| AGStreamInput | class |  |
| run_stream | function |  |
| map_agui_messages_to_events | function |  |
| _stringify_tool_result | function |  |
| _get_timestamp | function |  |
| _encode_context | function |  |

## Chunks

### AGUIStream (class, L55-L105)

> *Summary: This class provides an interface to stream events from an agent execution. It accepts various configuration inputs like prompts, tools, and middleware, runs the agent asynchronously using a task group, and yields encoded string representations of emitted events as an asynchronous iterator.*


### __init__ (method, L56-L57, parent: AGUIStream)

> *Summary: Initializes the stream object by storing a reference to an `Agent` instance. This allows the stream to operate on or interact with the provided agent throughout its lifecycle.*


### build_asgi (method, L59-L64, parent: AGUIStream)

> *Summary: This method constructs and returns an ASGI endpoint object based on the instance's state. It delegates the actual construction logic by importing and calling a function from the local `asgi` module.*


### dispatch (method, L66-L105, parent: AGUIStream)

> *Summary: This method processes an incoming agent input by launching a streaming execution task and then yields encoded events from the resulting stream. It accepts various configuration parameters like tools, middleware, and hooks to control the agent's behavior during processing.*


### AGStreamInput (class, L109-L118)

> *Summary: This class aggregates all necessary data for streaming agent execution, holding inputs like `RunAgentInput`, configuration details (`ModelConfig`), available tools, and hooks. It serves as a central container to manage the state and flow of an ongoing agent interaction.*


### run_stream (function, L121-L308)

> *Summary: Processes an input command by setting up client tools and history, then executes the agent's request while streaming events to a memory object sender. It translates various internal model and tool events into specific UI stream events (like text chunks or tool calls) as they occur during execution.*


### map_agui_messages_to_events (function, L311-L389)

> *Summary: Transforms an incoming stream message (`AGStreamInput`) into a tuple containing system/developer prompts and a list of structured events. It processes user content to generate various input events (text, URL, file) and maps assistant or tool messages to corresponding model response or tool result events.*


### _stringify_tool_result (function, L392-L416)

> *Summary: This function converts a structured `ToolResult` containing various input types (text, data, URLs, etc.) into a single string suitable for the AG-UI stream format. It iterates over the result's parts, serializing each type appropriately and joining them with newlines if multiple parts exist.*


### _get_timestamp (function, L419-L420)

> *Summary: Retrieves the current time as a Unix timestamp in milliseconds, ensuring it is based on UTC. This function provides a precise, standardized integer representation of the present moment.*


### _encode_context (function, L423-L432)

> *Summary: Filters a provided context dictionary to ensure it only contains JSON-serializable data types suitable for frontend consumption. It recursively cleans the input by dropping non-serializable objects and then removes any remaining `None` values from the resulting structure.*

