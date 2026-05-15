# autogen/beta/network/task_mirror.py

1 function(s): _now_iso. 1 class(es): TaskMirror. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _now_iso | function |  |
| TaskMirror | class |  |

## Chunks

### _now_iso (function, L42-L43)

> *Summary: Generates the current time formatted as an ISO 8601 string, ensuring it is in UTC. This function provides a standardized timestamp for logging or data recording purposes.*


### TaskMirror (class, L46-L274)

> *Summary: This class forwards an agent's task lifecycle events (start, progress, completion, failure) to a central hub via either a `HubClient` or a direct `Hub`. It subscribes to event streams using `attach()` and allows for safe disconnection with `detach()`, ensuring that forwarding failures do not crash the calling agent.*


### __init__ (method, L62-L76, parent: TaskMirror)

> *Summary: Initializes a task mirror by requiring either a `HubClient` or a `Hub` object to manage communication. It stores the provided client/hub, along with an `owner_id` and optional `channel_id`, for later use in attaching to a network.*


### _observe (method, L78-L82, parent: TaskMirror)

> *Summary: This method asynchronously reports task metadata to either a configured hub client or a direct hub instance if available. It ensures the provided `TaskMetadata` object is observed by the appropriate communication endpoint.*


### _update (method, L84-L108, parent: TaskMirror)

> *Summary: This method asynchronously updates the status of a specified task by sending its current state, progress, result, or error to either a connected `_hub_client` or a fallback `_hub`. It acts as a unified interface for reporting task lifecycle changes.*


### _record (method, L110-L134, parent: TaskMirror)

> *Summary: This method asynchronously logs task execution details to a connected hub or client. It accepts identifiers for the owner and capability, along with the task's final state, latency, and ID, forwarding this observation data accordingly.*


### attach (method, L136-L144, parent: TaskMirror)

> *Summary: Subscribes to various task lifecycle events (started, progress, completed, failed, expired) from an input stream. It returns a list of subscription IDs necessary for later unsubscribing via a `detach` method.*


### detach (method, L146-L150, parent: TaskMirror)

> *Summary: This method removes prior subscriptions from a given stream using a list of subscription IDs. It iterates through the provided IDs and attempts to unsubscribe each one, silently ignoring any exceptions during the process.*


### _escalate (method, L152-L179, parent: TaskMirror)

> *Summary: When a task mirror encounters an exception during an operation, this method logs the error and broadcasts a `"mirror_failed"` event via the configured hub client or hub instance. It constructs a payload containing operational details, owner ID, channel ID, and exception information before firing the event to notify external listeners.*


### _on_started (method, L181-L196, parent: TaskMirror)

> *Summary: When a task begins, this method constructs `TaskMetadata` using the event's details and sets the state to running. It then attempts to observe this metadata; if an exception occurs during observation, it escalates the failure for the given task ID.*


### _on_progress (method, L198-L207, parent: TaskMirror)

> *Summary: This method asynchronously updates the state of a task using progress information received in an `TaskProgress` event. It handles potential `NotFoundError` gracefully and escalates any other exceptions encountered during the update process.*


### _on_completed (method, L209-L220, parent: TaskMirror)

> *Summary: When a task finishes, this method updates the internal state to `COMPLETED` using the provided result, handling potential `NotFoundError` gracefully. It also records an observation for the completed task unless an exception occurs during the update process, in which case it escalates the error.*


### _on_failed (method, L222-L233, parent: TaskMirror)

> *Summary: When a task fails, this method updates the task's state to `FAILED` with the associated error message, gracefully handling cases where the task ID is no longer found. It also records an observation for the failed state and escalates any unexpected exceptions encountered during the update process.*


### _on_expired (method, L235-L242, parent: TaskMirror)

> *Summary: When a task expires, this method updates the task's state to `EXPIRED`, gracefully handling cases where the task might no longer exist. It also records an observation for the expired state unless an exception occurs during the update, in which case it escalates the error.*


### _record_observation_if_tagged (method, L244-L274, parent: TaskMirror)

> *Summary: When a task reaches a terminal state and possesses a capability tag, this method calculates the execution latency and asynchronously records the observation with the owner. It retrieves necessary metadata like start time and capability from an internal hub cache using the provided task ID.*

