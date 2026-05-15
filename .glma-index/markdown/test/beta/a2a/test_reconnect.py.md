# test/beta/a2a/test_reconnect.py

6 function(s): _make_agent_card, _make_context, _task_event, _artifact_event, _completed_event, _attach_mock. 2 class(es): _ScriptedSdk, TestStreamingReconnect. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_agent_card | function |  |
| _make_context | function |  |
| _task_event | function |  |
| _artifact_event | function |  |
| _completed_event | function |  |
| _ScriptedSdk | class |  |
| _attach_mock | function |  |
| TestStreamingReconnect | class |  |

## Chunks

### _make_agent_card (function, L32-L41)

> *Summary: Creates a default `AgentCard` instance with specific configurations, including setting the name to "t" and enabling streaming capabilities. This function returns a fully initialized object representing an agent's metadata structure.*


### _make_context (function, L44-L52)

> *Summary: Creates a testing context object by initializing an `Agent` instance and populating the `Context` with necessary components like a memory stream and dependency provider from the agent. This setup provides the environment needed for running tests involving agent interactions.*


### _task_event (function, L55-L58)

> *Summary: Generates a `StreamResponse` containing a new task object initialized with the provided `task_id` and `context_id`, setting its state to "working." This function serves as an event trigger for starting a background process.*


### _artifact_event (function, L61-L70)

> *Summary: Generates a `StreamResponse` containing an artifact update event. It takes task, context, and artifact identifiers, along with the text content and a flag indicating if it's the final chunk, to signal progress on an artifact.*


### _completed_event (function, L73-L80)

> *Summary: Generates a `StreamResponse` indicating task completion by packaging the provided `task_id` and `context_id` into a `TaskStatusUpdateEvent` with the state set to completed. This function serves as a standardized way to signal successful task finalization within the streaming response mechanism.*


### _ScriptedSdk (class, L83-L109)

> *Summary: This class simulates SDK behavior by yielding predefined lists of `StreamResponse` events when its methods are called. It tracks the number of calls made to `send_message` and `subscribe`, and can optionally raise an error after a specified count during event streaming.*


### __init__ (method, L84-L95, parent: _ScriptedSdk)

> *Summary: Initializes the object by storing lists of initial and replay stream responses, along with a drop limit. It also sets counters for tracking outgoing messages and subscriptions to zero.*


### send_message (method, L97-L99, parent: _ScriptedSdk)

> *Summary: Increments a call counter and returns an asynchronous iterator of `StreamResponse` objects by invoking an internal scripted method with predefined events. This method handles the actual message sending process based on configured event streams.*


### subscribe (method, L101-L103, parent: _ScriptedSdk)

> *Summary: Increments a counter tracking subscription attempts and returns an asynchronous iterator yielding stream responses based on pre-recorded events. This method takes an arbitrary request object as input.*


### _scripted (method, L105-L109, parent: _ScriptedSdk)

> *Summary: This asynchronous method iterates over a list of `StreamResponse` events, yielding each one sequentially. It optionally terminates the iteration early by raising an error if the current index matches the specified `drop_after` count.*


### _attach_mock (function, L112-L114)

> *Summary: This helper function configures a client instance by assigning it a mock agent card and setting its SDK client reference. It modifies the provided `A2AClient` object in place to prepare it for testing.*


### TestStreamingReconnect (class, L118-L190)

> *Summary: These tests verify the reconnection logic of an `A2AClient` when streaming data. They simulate scenarios where a connection drops and then resumes, checking if streams correctly resume after a drop, deduplicate replayed artifacts, or raise an error when maximum reconnect attempts are exhausted.*


### test_reconnect_after_drop_resumes_stream (method, L119-L141, parent: TestStreamingReconnect)

> *Summary: This test verifies that the A2A client successfully resumes a stream after an intentional connection drop by simulating initial events, dropping the connection, and then replaying subsequent events. It asserts that the final accumulated text correctly combines data from both the initial and replayed event sequences.*


### test_reconnect_dedupes_replayed_artifact (method, L143-L164, parent: TestStreamingReconnect)

> *Summary: This test verifies that the client correctly deduplicates a replayed artifact event received during a reconnection scenario. It simulates sending an initial artifact followed by a replay of that same final artifact and a completion event to ensure only one instance is processed.*


### test_reconnect_exhausted_raises (method, L166-L190, parent: TestStreamingReconnect)

> *Summary: This test verifies that an `A2AClient` correctly raises an `A2AReconnectError` when the configured maximum number of reconnection attempts is exhausted during streaming consumption. It achieves this by mocking the subscription method to always fail, forcing the client into a reconnect loop until it gives up.*

