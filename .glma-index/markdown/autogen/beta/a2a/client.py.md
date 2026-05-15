# autogen/beta/a2a/client.py

3 function(s): _ensure_stream_response, _extract_status_prompt, _read_extra_parts. 3 class(es): A2ADriveState, A2ATurnOutcome, A2AClient. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2ADriveState | class |  |
| A2ATurnOutcome | class |  |
| A2AClient | class |  |
| _ensure_stream_response | function |  |
| _extract_status_prompt | function |  |
| _read_extra_parts | function |  |

## Chunks

### A2ADriveState (class, L119-L129)

> *Summary: This class maintains the state across a single interaction cycle with an agent, persisting data through interruptions. It tracks accumulated text, pending tool calls, completion status, and unique identifiers for artifacts and messages to prevent reprocessing during reconnections or polling.*


### A2ATurnOutcome (class, L133-L137)

> *Summary: Represents the outcome of a single turn in an agent interaction, indicating whether human input is needed. It stores a boolean flag for required input and an optional prompt string if input is necessary.*


### A2AClient (class, L140-L628)

> *Summary: This class manages communication with a remote A2A agent by handling the entire conversational drive loop. It accepts messages and context as input, managing state across turns to produce a final `ModelResponse` containing accumulated text and any pending tool calls. The core behavior involves either streaming or polling the server for responses while maintaining task IDs and context history.*


### __init__ (method, L153-L191, parent: A2AClient)

> *Summary: Initializes a client instance by accepting configuration parameters such as a required card URL, transport preferences, timeouts, and various optional connection/behavior settings. It stores these inputs internally to manage subsequent interactions with an external service.*


### __call__ (method, L193-L260, parent: A2AClient)

> *Summary: Executes a conversational loop by processing incoming messages and context to drive an agent's interaction with a model. It iteratively sends requests, awaits potential user input for tool execution or prompting, and returns the final `ModelResponse` containing accumulated text and any pending tool calls.*


### aclose (method, L262-L267, parent: A2AClient)

> *Summary: This method safely shuts down the client by closing the underlying `httpx` and SDK connections if they exist. It ensures this cleanup operation is idempotent, meaning it can be called multiple times without error.*


### _ensure_connected (method, L269-L294, parent: A2AClient)

> *Summary: This method establishes the necessary connection infrastructure by initializing an HTTP client and then creating an A2A SDK client based on a resolved agent card. It optionally fetches an extended version of the agent card if the initial card supports it, ensuring full connectivity for subsequent operations.*


### _validate_and_extract_tools (method, L296-L309, parent: A2AClient)

> *Summary: Filters an iterable of `ToolSchema` objects to return only those matching `FunctionToolSchema`. It asserts the agent card exists and verifies the server advertises a specific extension before returning the list of valid function tools.*


### _build_outgoing (method, L311-L353, parent: A2AClient)

> *Summary: Constructs an outgoing message by inspecting the provided sequence of events and context. It determines whether to build a tool result message (if the last event was `ToolResultsEvent`) or a user input message based on the contents of the messages and context state.*


### _drive_task (method, L355-L364, parent: A2AClient)

> *Summary: Determines how to process an incoming message based on streaming capability; if the agent supports streaming, it calls a dedicated streaming consumer, otherwise, it uses a polling mechanism. It takes a `Message`, `ConversationContext`, and `A2ADriveState` as input and returns an `A2ATurnOutcome`.*


### _consume_streaming (method, L366-L388, parent: A2AClient)

> *Summary: This method processes a streaming message by first building and sending a request to the SDK client. It then iteratively drains the resulting stream, automatically handling transient `A2AClientError` exceptions by implementing an exponential backoff and resubscribing if retries remain.*


### _consume_polling (method, L390-L424, parent: A2AClient)

> *Summary: This method initiates a polling loop to monitor the status of an asynchronous task after sending an initial message via an SDK client. It repeatedly fetches and processes task artifacts until the task reaches a terminal state or requires further user input, returning the final outcome accordingly.*


### _drain_stream (method, L426-L475, parent: A2AClient)

> *Summary: Processes an asynchronous stream of raw responses, parsing each into typed A2A events and publishing them to the context. It manages state updates based on event types (snapshot, status update, artifact update, or message), accumulating text and tracking task IDs until the stream is exhausted.*


### _handle_status_update (method, L477-L507, parent: A2AClient)

> *Summary: Processes incoming task status updates to determine the next action for a conversation state. It checks for failure reasons to terminate tasks, flags input requirements if necessary, or absorbs final completion messages from the update payload.*


### _absorb_completion_message (method, L509-L523, parent: A2AClient)

> *Summary: This method processes a completed message by first checking if its ID has already been seen to ensure idempotency. It then merges context updates, handles artifact parts to accumulate text and pending tool calls, and finally records the message ID as processed.*


### _absorb_task_artifacts (method, L525-L551, parent: A2AClient)

> *Summary: Processes task artifacts from a given `Task` object within the context of a conversation and state. It filters tool calls based on the task's status to prevent re-surfacing historical data during non-terminal polling, then applies updates and accumulates text/tool call payloads into the shared state.*


### _apply_artifact_update (method, L553-L576, parent: A2AClient)

> *Summary: This method processes an artifact update event, updating the drive state based on the event type. It accumulates text and pending tool calls from the input event, adding the artifact ID to seen IDs upon completion or if it's a final chunk.*


### _handle_artifact_parts (method, L578-L593, parent: A2AClient)

> *Summary: Aggregates textual content and extracts tool call events from an iterable of artifact parts. It streams accumulated text to the conversation context while collecting structured tool call data for later use.*


### _build_send_request (method, L595-L607, parent: A2AClient)

> *Summary: Constructs a `SendMessageRequest` by packaging the input `Message` and `ConversationContext`. It configures the request using default or specified output modes and an optional history length, then wraps it with tenant-specific context.*


### _read_context_id (method, L609-L610, parent: A2AClient)

> *Summary: Retrieves a specific context ID string from the provided `ConversationContext` object by looking up a variable name constructed using the instance's card URL. It returns this ID if found, or `None` otherwise.*


### _save_context_id (method, L612-L615, parent: A2AClient)

> *Summary: Stores a provided `context_id` into the `ConversationContext`'s variables dictionary, keyed by a template incorporating the client's card URL, only if the ID is non-empty.*


### _maybe_tenant (method, L617-L622, parent: A2AClient)

> *Summary: Determines the active tenant by checking for an override in the conversation context; if found and valid, it sets the `tenant` key in the provided keyword arguments before returning them.*


### _merge_context_update (method, L625-L628, parent: A2AClient)

> *Summary: Updates the `ConversationContext`'s variables dictionary by merging key-value pairs from the provided payload mapping. If the input payload is empty, no changes are made to the context.*


### _ensure_stream_response (function, L631-L640)

> *Summary: This helper function standardizes incoming events by ensuring the output is always a `StreamResponse`. It wraps bare `Task` or `Message` objects into a `StreamResponse` wrapper if they are not already of that type, raising an error for unknown event types.*


### _extract_status_prompt (function, L643-L649)

> *Summary: This function extracts a string prompt from a `TaskStatus` object's message field, returning `None` if the message is missing or empty. It concatenates all non-empty text parts found within the status message.*


### _read_extra_parts (function, L652-L657)

> *Summary: Retrieves and filters user-supplied extra `Part` objects from the conversation context's dependencies. It returns a list containing only valid `Part` instances found under the designated dependency key.*

