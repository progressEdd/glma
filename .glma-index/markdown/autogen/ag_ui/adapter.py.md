# autogen/ag_ui/adapter.py

3 function(s): _get_timestamp, run_stream, _encode_context. 2 class(es): AGUIStream, AGStreamInput. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _get_timestamp | function |  |
| AGUIStream | class |  |
| AGStreamInput | class |  |
| run_stream | function |  |
| _encode_context | function |  |

## Chunks

### _get_timestamp (function, L45-L46)

> *Summary: Retrieves the current time as a Unix timestamp in milliseconds, ensuring it is timezone-aware and UTC-based. This function provides a precise, millisecond-level integer representation of the present moment.*


### AGUIStream (class, L50-L100)

> *Summary: This class manages the interaction between a conversational agent and a UI stream, taking an agent instance and optional event interceptors as input. It asynchronously dispatches incoming requests by setting up a state context, running the agent's logic in a background task group, and yielding encoded events from the resulting stream.*


### __init__ (method, L51-L59, parent: AGUIStream)

> *Summary: Initializes an adapter by storing a `ConversableAgent` instance and a list of optional event interceptor functions. It then creates an associated `AgentService` using the provided agent.*


### dispatch (method, L61-L93, parent: AGUIStream)

> *Summary: This method processes an incoming agent input by aggregating context from the agent, input, and optional arguments into a unified state. It then concurrently runs the agent's service with this state and yields encoded events as they are generated from the resulting event stream.*


### build_asgi (method, L95-L100, parent: AGUIStream)

> *Summary: This method constructs and returns an ASGI endpoint object representing the AGUIStream. It delegates the actual construction logic by importing and calling a function from the local `asgi` module.*


### AGStreamInput (class, L104-L106)

> *Summary: This class holds the necessary data for streaming agent input, encapsulating a `RunAgentInput` object and associated `ContextVariables`. It serves as a container to pass runtime information into the processing pipeline.*


### run_stream (function, L109-L280)

> *Summary: Processes an incoming agent command by transforming it into a request for the service and streaming responses back to the caller via a write stream. It emits various events—such as run start/finish, state snapshots, text content updates, tool calls, and errors—based on the received service response.*


### _encode_context (function, L283-L292)

> *Summary: Filters a provided dictionary context by removing any non-serializable Python objects to ensure it contains only JSON-compatible data suitable for frontend consumption. It returns an empty dictionary if the input context is null or after filtering.*

