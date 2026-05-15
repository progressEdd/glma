# autogen/beta/events/task_events.py

6 class(es): TaskEvent, TaskStarted, TaskProgress, TaskCompleted, TaskFailed, TaskExpired. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TaskEvent | class |  |
| TaskStarted | class |  |
| TaskProgress | class |  |
| TaskCompleted | class |  |
| TaskFailed | class |  |
| TaskExpired | class |  |

## Chunks

### TaskEvent (class, L16-L19)

> *Summary: Represents a specific event related to a task, encapsulating the unique `task_id`, the name of the involved agent (`agent_name`), and the task's overall goal (`objective`). This structure is used to signal state changes or occurrences within a multi-agent workflow.*


### TaskStarted (class, L22-L26)

> *Summary: Represents an event signaling that a task has begun execution. It optionally carries a `TaskSpec` detailing the nature of the running task.*


### TaskProgress (class, L29-L45)

> *Summary: Represents a progress update for an active task, carrying either streamed sub-agent output in `content` or structured checkpoint data in `payload`. This event is marked as transient and serves to report ongoing status until the task concludes.*


### TaskCompleted (class, L48-L54)

> *Summary: Represents the completion of a task by including an optional structured `result`, a reference to the associated `task_stream`, and usage metrics. It inherits from `TaskEvent` to signal that a specific task has finished execution.*


### TaskFailed (class, L57-L76)

> *Summary: Represents a task failure event by storing an `Exception` object. It automatically generates and returns the full traceback string of the provided error upon access to its `content` property.*


### content (method, L67-L76, parent: TaskFailed)

> *Summary: Retrieves the error content as a string; if not already computed, it formats and joins the exception traceback into an internal attribute before returning it.*


### TaskExpired (class, L79-L86)

> *Summary: Represents a terminal event signaling that a task's time-to-live (TTL) has elapsed without reaching another completion state. This event is emitted by the observer managing the TTL clock for the task.*

