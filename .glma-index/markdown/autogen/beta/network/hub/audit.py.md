# autogen/beta/network/hub/audit.py

1 function(s): _default_clock. 1 class(es): AuditLog. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _default_clock | function |  |
| AuditLog | class |  |

## Chunks

### _default_clock (function, L50-L53)

> *Summary: Generates a standardized UTC timestamp string suitable for logging or auditing purposes. It captures the current time in UTC and formats it into an ISO 8601 string ending with 'Z'.*


### AuditLog (class, L98-L330)

> *Summary: This class acts as an append-only log writer over a `KnowledgeStore`, capturing state transitions from various hub events. It accepts event data (e.g., agent lifecycle, channel changes) via specific listener methods and serializes them into structured audit records before persisting them to disk and notifying registered subscribers live.*


### __init__ (method, L112-L119, parent: AuditLog)

> *Summary: Initializes an audit mechanism by storing a `KnowledgeStore` dependency and optionally setting a clock function. It also initializes an empty list of subscribers and sets up a local byte counter for health monitoring.*


### append (method, L123-L137, parent: AuditLog)

> *Summary: Serializes a dictionary record into a JSON line and appends it to the audit store. After writing, it notifies all registered subscribers asynchronously with the original record data.*


### bytes_written (method, L140-L147, parent: AuditLog)

> *Summary: Returns the current count of bytes written to the audit log, which is a process-local counter that resets upon hub restart. This value is exposed via `Hub.health` for monitoring audit volume.*


### read_all (method, L149-L159, parent: AuditLog)

> *Summary: Retrieves and parses all entries from the audit log file stored by the instance. It reads the raw data, skips empty lines, and returns a list of dictionaries representing each parsed log record, or an empty list if no data is found.*


### subscribe (method, L161-L169, parent: AuditLog)

> *Summary: Registers a subscriber to receive real-time notifications whenever a new record is added to the audit stream. Callbacks are executed sequentially in the order they were registered, with exceptions in one callback being caught and ignored for subsequent ones.*


### unsubscribe (method, L171-L174, parent: AuditLog)

> *Summary: Removes a specified `AuditSubscriber` from the internal list of subscribers, silently ignoring an error if the subscriber was not registered.*


### on_agent_event (method, L178-L233, parent: AuditLog)

> *Summary: Transforms incoming agent lifecycle events (like registration or skill set changes) from `agent_id`, event `kind`, and a data `payload` into structured audit records. It maps specific event kinds to corresponding predefined audit types, appending the resulting record with a timestamp.*


### on_channel_event (method, L235-L275, parent: AuditLog)

> *Summary: Processes incoming channel lifecycle events by translating specific kinds ("created", "closed", "expired") into structured audit records. It accepts a `channel_id`, event `kind`, and a `payload` dictionary, outputting asynchronous calls to append the relevant audit entry based on the event type.*


### on_expectation_fired (method, L277-L289, parent: AuditLog)

> *Summary: Records an audit event whenever a predefined expectation is violated within a specific channel. It takes the channel ID, the expectation object, and the violation details as input to log the timestamped incident.*


### on_task_event (method, L291-L312, parent: AuditLog)

> *Summary: This method records terminal task transitions by asynchronously appending an audit record when a task reaches "completed," "failed," "expired," or "cancelled." It filters out non-terminal events and uses provided payload data to construct the detailed audit entry.*


### on_turn_failed (method, L314-L330, parent: AuditLog)

> *Summary: Records an audit log entry when a turn handler fails during communication. It takes channel, agent, and envelope identifiers along with the exception to record the failure details.*

