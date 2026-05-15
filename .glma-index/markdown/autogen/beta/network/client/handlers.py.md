# autogen/beta/network/client/handlers.py

8 function(s): _is_task_event, read_wal_until, resolve_view_policy, stamp_dependencies, _auto_ack_invite, _process_substantive, _report_turn_failure, default_handler.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_task_event | function |  |
| read_wal_until | function |  |
| resolve_view_policy | function |  |
| stamp_dependencies | function |  |
| _auto_ack_invite | function |  |
| _process_substantive | function |  |
| _report_turn_failure | function |  |
| default_handler | function |  |

## Chunks

### _is_task_event (function, L54-L55)

> *Summary: Checks if a given string, representing an event type, signifies a task-related event by testing for the "ag2.task." prefix. Returns `True` if it matches, otherwise `False`.*


### read_wal_until (function, L58-L71)

> *Summary: Retrieves a slice of the Write-Ahead Log (WAL) from the client's hub, stopping just before a specified `Envelope`. This function returns a list of preceding `Envelope` objects that constitute the conversation history up to the current turn.*


### resolve_view_policy (function, L74-L79)

> *Summary: Retrieves the designated view policy for a specific agent within a channel by querying the hub client using the provided channel and agent IDs from the metadata. This function returns the determined `ViewPolicy` object.*


### stamp_dependencies (function, L82-L98)

> *Summary: Constructs a dictionary containing necessary dependencies for an LLM turn context. It injects the `AgentClient`, the current `Channel` object, the hub reference from the client, and the channel's specific state object.*


### _auto_ack_invite (function, L101-L119)

> *Summary: This function automatically acknowledges any incoming channel invite addressed to the client. It constructs and sends an `EV_CHANNEL_INVITE_ACK` envelope back to the sender, unless a custom handler overrides this default behavior.*


### _process_substantive (function, L122-L248)

> *Summary: Processes an incoming substantive message by extracting input via an adapter, projecting conversation history, and invoking the agent's LLM with relevant tools. It then uses the adapter to build a response envelope from the LLM output and sends it back, handling any processing errors by reporting a turn failure.*


### _report_turn_failure (function, L251-L272)

> *Summary: This asynchronous function reports an exception that occurred within a notification handler by forwarding it to the central hub client. It takes the client, envelope, and exception as input, ensuring the failure is logged and propagated through the system's audit mechanisms if a hub client is available.*


### default_handler (function, L275-L298)

> *Summary: This function routes incoming `Envelope` messages based on their `event_type`. It handles specific invitation events, passes through certain channel and task events without action, and delegates all other substantive events for processing.*

