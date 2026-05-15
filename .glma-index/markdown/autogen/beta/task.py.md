# autogen/beta/task.py

2 function(s): _now_iso, _expires_iso. 4 class(es): TaskState, TaskSpec, TaskMetadata, Task. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TaskState | class |  |
| TaskSpec | class |  |
| TaskMetadata | class |  |
| _now_iso | function |  |
| _expires_iso | function |  |
| Task | class |  |

## Chunks

### TaskState (class, L43-L50)

> *Summary: Defines the possible lifecycle stages for a task using an enumeration. It provides constant string values representing states such as `CREATED`, `RUNNING`, `COMPLETED`, `FAILED`, and `EXPIRED`.*


### TaskSpec (class, L61-L75)

> *Summary: Represents a task with a title, optional description, and data payload. It can optionally include a `capability` tag used to track specific agent observations during execution.*


### TaskMetadata (class, L79-L95)

> *Summary: This class serves as a mutable record tracking the lifecycle and status of a specific task. It stores essential metadata such as IDs, current state, timestamps for creation/completion, progress details, and any associated results or errors.*


### _now_iso (function, L98-L99)

> *Summary: Generates the current time formatted as an ISO 8601 string, ensuring it is in UTC. This function takes no inputs and returns a standardized timestamp string.*


### _expires_iso (function, L102-L105)

> *Summary: Calculates an ISO-formatted expiration time string by adding a specified duration in seconds to a given base `datetime` object, returning `None` if no TTL is provided.*


### Task (class, L108-L319)

> *Summary: Manages the lifecycle of a unit of work, tracking its state from creation to completion or failure. It accepts an owner ID and task specification, emitting progress, completion, or failure events via a provided or newly created context stream upon entering or exiting its asynchronous context manager block.*


### __init__ (method, L131-L147, parent: Task)

> *Summary: Initializes a task object by storing its owner ID, specification, optional conversation context, and time-to-live. It sets up internal state variables to track ownership, metadata, and dependency information for later use.*


### task_id (method, L150-L153, parent: Task)

> *Summary: Retrieves the unique identifier for the current task from its metadata, raising an error if the metadata hasn't been initialized yet. This method returns a string representing the task ID.*


### state (method, L156-L159, parent: Task)

> *Summary: Returns the current operational status of the task, defaulting to `TaskState.CREATED` if no metadata has been initialized. This method accesses the internal state stored within the task's metadata object.*


### metadata (method, L162-L165, parent: Task)

> *Summary: Retrieves the task's associated metadata object, provided it has been initialized via `__aenter__`. Raises a runtime error if the metadata hasn't been set yet.*


### context (method, L168-L171, parent: Task)

> *Summary: Retrieves the associated `ConversationContext` for the task, raising a runtime error if the task hasn't been properly initialized within an asynchronous context manager.*


### progress (method, L173-L192, parent: Task)

> *Summary: Updates the task's progress metadata by merging a provided payload and then emits a `TaskProgress` event containing this updated information to the context. This operation is skipped if the task has already reached a terminal state or if it hasn't been properly initialized.*


### complete (method, L194-L214, parent: Task)

> *Summary: When called on a task that is not already terminal, this method transitions the task's state to `COMPLETED`, records the final result and completion time, and emits a `TaskCompleted` message containing the task details and outcome. It raises an error if invoked before the task context has been entered.*


### fail (method, L216-L240, parent: Task)

> *Summary: When a task encounters an error, this method transitions its state to `FAILED`, records the exception details, and emits a `TaskFailed` message through the context. It accepts either a string (wrapped as a `RuntimeError`) or any `BaseException` as input.*


### expire (method, L242-L261, parent: Task)

> *Summary: When called by an external TTL observer, this method transitions the task's state to `EXPIRED` if it is not already terminal. It records the completion time and emits a `TaskExpired` event containing the task ID, owner name, and objective title.*


### __aenter__ (method, L263-L297, parent: Task)

> *Summary: When entering the asynchronous context, this method initializes or validates a task's state and metadata, generating a unique ID and setting the status to `RUNNING`. It then registers the task within its conversation context and sends a `TaskStarted` notification.*


### __aexit__ (method, L299-L319, parent: Task)

> *Summary: When an asynchronous context manager exits, it checks for exceptions to potentially fail the task or completes it if it was running. Finally, it cleans up dependency tracking within the associated context object.*

