# autogen/beta/a2a/events.py

7 class(es): A2AEvent, A2ATaskSnapshot, A2AMessage, A2ATaskStatusUpdate, A2ATaskArtifactUpdate, A2ATextArtifact, A2AToolCallArtifact.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2AEvent | class |  |
| A2ATaskSnapshot | class |  |
| A2AMessage | class |  |
| A2ATaskStatusUpdate | class |  |
| A2ATaskArtifactUpdate | class |  |
| A2ATextArtifact | class |  |
| A2AToolCallArtifact | class |  |

## Chunks

### A2AEvent (class, L16-L25)

> *Summary: Serves as a base marker for all A2A wire events entering the AG2 stream. It is marked transient to prevent transport-agnostic echoes from persisting in the stream history.*


### A2ATaskSnapshot (class, L28-L31)

> *Summary: Represents a complete state of a task within an event structure, holding the entire `Task` object as its primary data payload. This class inherits from `A2AEvent` and is used when the stream response specifically indicates a "task" payload.*


### A2AMessage (class, L34-L37)

> *Summary: Represents a standalone message event within the A2A system, encapsulating a `Message` object as its primary payload. This class inherits from `A2AEvent` to conform to the event structure.*


### A2ATaskStatusUpdate (class, L40-L44)

> *Summary: Represents a status update event within the A2A system, carrying a `TaskStatusUpdateEvent` payload and an explicit `TaskState`. This structure allows for easy filtering based on the task's current state.*


### A2ATaskArtifactUpdate (class, L47-L52)

> *Summary: Represents an event signaling an update to a task's artifact. It carries the `TaskArtifactUpdateEvent` payload and includes boolean flags (`append`, `last_chunk`) for chunk-aware processing logic.*


### A2ATextArtifact (class, L55-L58)

> *Summary: Represents a typed, text-only version of an artifact update. It holds the extracted `text` content alongside the underlying raw protobuf data from its parent class.*


### A2AToolCallArtifact (class, L61-L64)

> *Summary: Represents a typed view of a `tool-call+json` artifact, providing direct access to the parsed `ToolCallEvent`. This structure allows subscribers to bypass JSON decoding when processing tool call information.*

