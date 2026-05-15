# autogen/a2a/utils.py

24 function(s): get_message_text, new_artifact, new_agent_text_message, request_message_to_a2a, request_message_from_a2a, response_message_from_a2a_task, response_message_from_a2a_artifacts, update_artifact_to_streaming, response_message_from_a2a_message, make_artifact and 14 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_message_text | function |  |
| new_artifact | function |  |
| new_agent_text_message | function |  |
| request_message_to_a2a | function |  |
| request_message_from_a2a | function |  |
| response_message_from_a2a_task | function |  |
| response_message_from_a2a_artifacts | function |  |
| update_artifact_to_streaming | function |  |
| response_message_from_a2a_message | function |  |
| make_artifact | function |  |
| copy_artifact | function |  |
| make_input_required_message | function |  |
| message_to_part | function |  |
| message_from_part | function |  |
| stream_chunk_to_compat | function |  |
| compat_send_message | function |  |
| compat_subscribe_to_task | function |  |
| compat_get_task | function |  |
| to_core_agent_card | function |  |
| to_compat_agent_card | function |  |
| to_core_message | function |  |
| to_core_parts | function |  |
| make_async_card_modifier | function |  |
| make_async_extended_card_modifier | function |  |

## Chunks

### get_message_text (function, L62-L64)

> *Summary: Concatenates the textual content from all `TextPart` components within a given `Message` object, using an optional newline character as a separator to produce a single string output.*


### new_artifact (function, L67-L69)

> *Summary: Creates a new `Artifact` object by generating a unique ID and accepting a name, list of parts, and optional description as input. The function returns the fully initialized `Artifact` instance.*


### new_agent_text_message (function, L72-L85)

> *Summary: Creates a standardized `Message` object representing text content originating from an agent. It accepts the message text and optional context or task identifiers to construct the final structured message.*


### request_message_to_a2a (function, L97-L118)

> *Summary: Transforms an incoming `RequestMessage` into a standardized outgoing `Message`. It packages the request's messages and associated client/context data into the new message structure, generating a unique ID.*


### request_message_from_a2a (function, L121-L127)

> *Summary: Transforms an incoming `Message` object into a standardized `RequestMessage`. It extracts the context and client tools from the message's metadata while converting each part of the original message using `message_from_part`.*


### response_message_from_a2a_task (function, L130-L156)

> *Summary: Constructs a `ResponseMessage` from a given task by processing its message history and artifacts. It determines the output based on the task's state, either returning an input prompt if input is required or merging artifact responses with the existing conversation history otherwise.*


### response_message_from_a2a_artifacts (function, L159-L216)

> *Summary: Processes a single `Artifact` to construct a `ResponseMessage`, handling cases where the artifact contains only text, only data, or a mix of both. It merges text and A2UI-typed data into one message dictionary if present, otherwise it separates them into distinct messages within the response.*


### update_artifact_to_streaming (function, L219-L227)

> *Summary: Converts a `TaskArtifactUpdateEvent` into an iterator of `StreamEvent`s by iterating over the artifact's parts. If the event does not indicate it is already streaming, it yields content from text or data parts sequentially.*


### response_message_from_a2a_message (function, L230-L268)

> *Summary: Transforms an incoming `Message` object into a structured `ResponseMessage`. It aggregates text and data parts, merging them into a single content block if A2UI data is present; otherwise, it separates text and data into distinct message entries.*


### make_artifact (function, L271-L285)

> *Summary: Creates a new `Artifact` object from an optional message and an optional context dictionary. It packages the message content into parts and attaches the provided context as metadata to the resulting artifact.*


### copy_artifact (function, L288-L308)

> *Summary: Creates a copy of an input artifact, optionally incorporating message content into its parts and merging provided context data into the artifact's metadata. It returns a new `Artifact` object reflecting these modifications while preserving most original attributes.*


### make_input_required_message (function, L311-L324)

> *Summary: Constructs a new text message containing provided content and task/context identifiers. It optionally enriches the message with additional metadata from a supplied context dictionary.*


### message_to_part (function, L327-L335)

> *Summary: Converts a dictionary message into a structured `Part` object. It extracts the text content from the input dictionary and wraps it in a `TextPart`, retaining any remaining metadata as part of the structure.*


### message_from_part (function, L338-L360)

> *Summary: Converts a `Part` object into a dictionary representation based on its root type. If the root is text, it returns metadata merged with the text content; if it's data, it either returns a specific structured artifact or the raw data dictionary. Raises an error for unsupported part types.*


### stream_chunk_to_compat (function, L370-L427)

> *Summary: Translates a protobuf stream chunk from v1.0 format into a compatible v0.3 event structure. It processes different message types within the chunk—such as messages, tasks, status updates, or artifact updates—to return an event and the updated task state for subsequent processing.*


### compat_send_message (function, L430-L441)

> *Summary: This asynchronous function converts a `Message` into a core request and streams the resulting events back to the caller. It iterates over chunks received from the client's send method, transforming each chunk into an event before yielding it.*


### compat_subscribe_to_task (function, L444-L455)

> *Summary: This asynchronous function streams events by subscribing to a specific task ID on the provided client. It converts a compatibility request into a core subscription and yields any resulting `ClientStreamEvent`s as they arrive from the stream.*


### compat_get_task (function, L458-L461)

> *Summary: Retrieves a task using the `Client` and a provided `task_id`, then transforms the resulting core task object into a compatibility-shaped Pydantic `Task`. This function bridges older API structures with newer internal representations.*


### to_core_agent_card (function, L464-L466)

> *Summary: Transforms an `AgentCard` object from the older v0.3 Pydantic format to the newer v1.0 Protobuf structure by delegating the conversion to a dedicated utility function. This ensures compatibility between different versions of agent card definitions.*


### to_compat_agent_card (function, L469-L471)

> *Summary: Converts an older `_CoreAgentCard` object, typically from a v1.0 protobuf format, into the newer `AgentCard` structure expected by v0.3 pydantic models. It delegates this conversion to a dedicated internal helper function.*


### to_core_message (function, L474-L476)

> *Summary: Converts an input `Message` object, structured according to the v0.3 schema, into a corresponding `_CoreMessage` using internal conversion logic. This acts as a wrapper to facilitate migration between message versions.*


### to_core_parts (function, L479-L481)

> *Summary: Transforms a list of `Part` objects from the older v0.3 format to the newer `_CorePart` protobuf structure by applying a specific conversion logic to each element.*


### make_async_card_modifier (function, L484-L500)

> *Summary: This function wraps a synchronous card modifier into an asynchronous callable suitable for SDK 1.0 hooks. It achieves this by translating the incoming proto-based `_CoreAgentCard` to the older v0.3 Pydantic format, executing the sync modifier, and then converting the result back to the core proto format.*


### make_async_extended_card_modifier (function, L503-L518)

> *Summary: This function wraps a synchronous card modifier into an asynchronous one by bridging between internal and external card representations. It accepts a sync modifier and returns an async callable that executes the provided logic while preserving the `ServerCallContext` argument for inspection during execution.*

