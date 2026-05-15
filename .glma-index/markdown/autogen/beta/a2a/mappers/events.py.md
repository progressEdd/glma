# autogen/beta/a2a/mappers/events.py

9 function(s): chunk_to_text_artifact, client_call_to_artifact, task_state_to_status_update, _build_artifact, _build_artifact_update, a2a_event_to_sdk, parse_stream_response, parse_artifact_update, parse_task_artifact.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| chunk_to_text_artifact | function |  |
| client_call_to_artifact | function |  |
| task_state_to_status_update | function |  |
| _build_artifact | function |  |
| _build_artifact_update | function |  |
| a2a_event_to_sdk | function |  |
| parse_stream_response | function |  |
| parse_artifact_update | function |  |
| parse_task_artifact | function |  |

## Chunks

### chunk_to_text_artifact (function, L37-L81)

> *Summary: Transforms a streaming text chunk and associated metadata into an `A2ATextArtifact` event suitable for append-streaming. It constructs the artifact using provided IDs and content, managing whether it's an update or the final piece of data.*


### client_call_to_artifact (function, L84-L122)

> *Summary: Transforms a `ClientToolCallEvent` into an `A2AToolCallArtifact`, representing a complete, non-streamed tool invocation. It constructs the artifact using the event's ID and name, incorporating provided metadata for tracking within a specific task and context.*


### task_state_to_status_update (function, L125-L150)

> *Summary: Converts a `TaskState` into an `A2ATaskStatusUpdate` event structure. It accepts the task's current state and optional message or timestamp to construct and return the standardized status update object for lifecycle transitions.*


### _build_artifact (function, L153-L168)

> *Summary: Constructs an `Artifact` object by combining a unique ID and a list of constituent parts. It optionally incorporates a name, description, and structured metadata into the final artifact instance.*


### _build_artifact_update (function, L171-L189)

> *Summary: Constructs a `TaskArtifactUpdateEvent` by packaging task and context identifiers along with an artifact object. It optionally includes metadata, which is converted from a dictionary structure before being returned as the event.*


### a2a_event_to_sdk (function, L192-L210)

> *Summary: This function unwraps a specific `A2AEvent` instance into its underlying bare SDK protobuf message or task object. It inspects the input event type and returns the contained payload (`update`, `message`, or `task`) accordingly, raising an error for unsupported types.*


### parse_stream_response (function, L213-L231)

> *Summary: This function decodes a `StreamResponse` object into a specific typed `A2AEvent`. It inspects the response's payload type to return either a task snapshot, message, status update, or an artifact update.*


### parse_artifact_update (function, L234-L264)

> *Summary: This function transforms a `TaskArtifactUpdateEvent` into the most specific `A2ATaskArtifactUpdate` subclass based on its content. It checks if all parts are text to return an `A2ATextArtifact`, otherwise it checks for a single tool-call part to return an `A2AToolCallArtifact`, defaulting to the base update type otherwise.*


### parse_task_artifact (function, L267-L289)

> *Summary: Converts a polled `Artifact` snapshot into a typed update event structure. It wraps the input artifact with specific flags (`append=False`, `last_chunk=True`) to simulate an incremental stream for downstream processing.*

