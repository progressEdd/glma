# autogen/agentchat/realtime/experimental/function_observer.py

1 class(es): FunctionObserver. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FunctionObserver | class |  |

## Chunks

### FunctionObserver (class, L20-L80)

> *Summary: This class observes events from the OpenAI Realtime API, specifically handling incoming `FunctionCall` events. Upon receiving a call, it executes the corresponding registered function using provided arguments and sends the resulting output back to the API via the realtime client.*


### __init__ (method, L23-L25, parent: FunctionObserver)

> *Summary: Initializes an observer designed to process function call events originating from the OpenAI Realtime API. It accepts an optional logger instance during construction.*


### on_event (method, L27-L39, parent: FunctionObserver)

> *Summary: When a `FunctionCall` event is received from the OpenAI Realtime API, this method logs the reception and asynchronously executes the corresponding function using the provided call ID, name, and arguments.*


### call_function (method, L41-L68, parent: FunctionObserver)

> *Summary: Executes a specified function by name and arguments against the agent's registered tools. It handles potential execution errors, serializes the return value (JSON or string), and sends the final result back via the real-time client using the provided call ID.*


### initialize_session (method, L70-L76, parent: FunctionObserver)

> *Summary: This method updates the active session with a list of registered tools and sets tool choice to automatic. It sends this configuration via an asynchronous call to the `realtime_client`.*


### run_loop (method, L78-L80, parent: FunctionObserver)

> *Summary: This asynchronous method initiates and runs the core observation loop for the agent. It is intended to manage continuous monitoring or interaction within the system.*

