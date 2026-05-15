# autogen/beta/network/hub/core.py

9 function(s): _utc_now_iso, _error_code, _match_any, _is_channel_protocol_event, _is_task_event, _is_protocol_event, _expires_at, _task_metadata_to_dict, _task_metadata_from_dict. 1 class(es): Hub. 84 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _utc_now_iso | function |  |
| _error_code | function |  |
| _match_any | function |  |
| _is_channel_protocol_event | function |  |
| _is_task_event | function |  |
| _is_protocol_event | function |  |
| _expires_at | function |  |
| Hub | class |  |
| _task_metadata_to_dict | function |  |
| _task_metadata_from_dict | function |  |

## Chunks

### _utc_now_iso (function, L116-L117)

> *Summary: Generates the current time formatted as an ISO string, ensuring it is in UTC. This function takes no inputs and returns a standardized timestamp string.*


### _error_code (function, L127-L131)

> *Summary: This utility inspects an exception object to determine a standardized error string. It iterates through a predefined map of exception types and returns the corresponding code if a match is found, defaulting to `"error"` otherwise.*


### _match_any (function, L134-L136)

> *Summary: Checks if a given string name matches any pattern within a list using case-sensitive glob matching. Returns `True` immediately upon finding the first match or if the patterns include a wildcard that matches everything.*


### _is_channel_protocol_event (function, L139-L140)

> *Summary: Checks if a given string, representing an event type, originates from the internal channel protocol by testing for a specific prefix. Returns `True` if the event starts with `"ag2.channel."`, otherwise returns `False`.*


### _is_task_event (function, L143-L144)

> *Summary: Checks if a given string, representing an event type, signifies a task-related event by verifying it begins with the "ag2.task." prefix. Returns `True` if it is a task event and `False` otherwise.*


### _is_protocol_event (function, L147-L148)

> *Summary: Checks if a given event type string corresponds to either a channel protocol event or a task-related event. It returns `True` if the event matches either category, and `False` otherwise.*


### _expires_at (function, L151-L156)

> *Summary: Calculates an expiration time string by adding a specified duration in seconds to a given ISO timestamp. It returns an empty string if the provided time-to-live is zero or negative.*


### Hub (class, L159-L2067)

> *Summary: This class acts as the central state manager and event dispatcher for a distributed system, maintaining registries for agents, channels, tasks, and adapters. It handles lifecycle management (opening/closing), persistence via a `KnowledgeStore`, and processes incoming messages by validating them against registered rules and channel states before dispatching events to attached listeners.*


### __init__ (method, L167-L261, parent: Hub)

> *Summary: Initializes the core hub state by storing configuration parameters like timeouts and sweep intervals. It sets up various internal registries, caches (for agents, channels, tasks), and locks to manage system state, including audit logging and expectation tracking.*


### open (method, L266-L310, parent: Hub)

> *Summary: Creates and initializes a production-ready Hub instance by taking a `KnowledgeStore` and optional configuration parameters. It registers default adapters and evaluators if specified, then asynchronously hydrates the state from disk and starts background sweepers before returning the fully configured Hub object.*


### hydrate (method, L312-L361, parent: Hub)

> *Summary: This method reconstructs the system's state by clearing existing caches and then loading identities, channels, and tasks from persistent storage via `self._store`. It deterministically rebuilds internal indexes, such as capability mappings, by re-processing loaded agent resumes.*


### start (method, L363-L388, parent: Hub)

> *Summary: This method initializes and starts various background sweepers—TTL, expectation, and any custom ones—based on configured intervals. It ensures idempotency by only starting a sweeper if it hasn't been initialized yet, setting the internal `_started` flag upon completion.*


### close (method, L390-L408, parent: Hub)

> *Summary: This method gracefully shuts down the network hub by stopping all associated background tasks and sweepers (TTL, expectation, and custom). It then cancels and awaits completion for any active endpoint tasks before marking the hub as closed.*


### register_sweeper (method, L412-L444, parent: Hub)

> *Summary: Attaches a periodic background task by storing a custom worker with a given name, interval, and callable function. It either starts the worker immediately if the hub is running or queues it to begin when `Hub.start()` is called.*


### unregister_sweeper (method, L446-L457, parent: Hub)

> *Summary: Removes a specified custom sweeper from the internal registry and asynchronously calls its `stop()` method if it exists. This ensures that registered sweepers are properly shut down when unregistered.*


### __aenter__ (method, L459-L460, parent: Hub)

> *Summary: When used as an asynchronous context manager, this method returns the current hub instance itself. This allows for clean setup and teardown operations within `async with` blocks.*


### __aexit__ (method, L462-L463, parent: Hub)

> *Summary: When an asynchronous context manager exits, this method ensures the associated resource is properly shut down by calling `self.close()`. It accepts any exception that occurred within the context block as input and returns nothing.*


### register_adapter (method, L467-L475, parent: Hub)

> *Summary: Stores a provided `ChannelAdapter` using a composite key derived from the adapter's type and version. If an adapter already exists for that key, it is overwritten, though existing in-flight channels retain their original manifest snapshot.*


### _adapter_for (method, L477-L481, parent: Hub)

> *Summary: Retrieves a specific `ChannelAdapter` instance from an internal registry based on provided manifest type and version. It raises a `NotFoundError` if no corresponding adapter is found in the stored mappings.*


### register_listener (method, L485-L493, parent: Hub)

> *Summary: Attaches a `HubListener` to receive state-transition events, adding it to an ordered list of listeners. It ensures that exceptions thrown by any single listener during event dispatch are caught and logged without halting the processing for subsequent listeners.*


### unregister_listener (method, L495-L498, parent: Hub)

> *Summary: Removes a specified `HubListener` from the hub's internal list of listeners, safely ignoring errors if the listener was not previously registered.*


### report_turn_failure (method, L500-L522, parent: Hub)

> *Summary: Dispatches an `on_turn_failed` event to all registered listeners when a turn fails. It accepts the channel ID, agent ID, envelope ID, and the exception object as inputs to notify observers of the failure.*


### fire_task_event (method, L524-L540, parent: Hub)

> *Summary: This method broadcasts a notification across all registered listeners using the internal fan-out mechanism. It accepts a `task_id`, an event `kind` string (e.g., "started", "completed"), and a data `payload` dictionary to distribute.*


### audit_log (method, L543-L551, parent: Hub)

> *Summary: Provides external access to the internal `HubListener` instance responsible for logging events. This allows tooling to read all recorded logs or subscribe to live updates from the hub.*


### replace_audit_log (method, L553-L565, parent: Hub)

> *Summary: Swaps the internal `AuditLog` instance with a provided one by removing the old log from the listener chain and inserting the new log as the first listener. This ensures tenant-provided logs are processed before other listeners observe an event.*


### register_arbiter (method, L567-L580, parent: Hub)

> *Summary: This method allows replacing the currently active arbitration logic within the hub instance. It accepts a `HubArbiter` object, which dictates how agent access and limits are enforced, overriding any default rule-based behavior with custom protocols.*


### arbiter (method, L583-L585, parent: Hub)

> *Summary: Returns the instance of the currently active `HubArbiter` object, providing read-only access to it. This method is intended primarily for testing purposes.*


### health (method, L587-L622, parent: Hub)

> *Summary: Provides a lightweight operational snapshot of the hub's current state by returning a dictionary containing counts for active channels, registered identities, and loaded adapters. It calculates metrics like total pending messages and maximum queue depth based on internal state variables.*


### _fan_out (method, L624-L657, parent: Hub)

> *Summary: Dispatches a specified method call and its arguments to the hub instance itself (if overridden) and every registered listener. It ensures fault tolerance by wrapping each execution in a `try/except` block so that one failing listener does not halt the entire fan-out process.*


### on_envelope_posted (method, L666-L667, parent: Hub)

> *Summary: This asynchronous method receives an `Envelope` and `ChannelMetadata`, currently serving as a placeholder that does nothing. It is intended to handle the event when an envelope has been posted within a channel context.*


### on_envelope_rejected (method, L669-L670, parent: Hub)

> *Summary: This asynchronous method handles the rejection of a network envelope. It accepts an `Envelope` and a `NetworkError` as input but currently performs no action, returning immediately.*


### on_dispatch_failed (method, L672-L678, parent: Hub)

> *Summary: This asynchronous method handles failures during message dispatch. It accepts an `Envelope`, a `recipient_id`, and the exception that caused the failure as input, returning nothing upon execution.*


### on_channel_event (method, L680-L681, parent: Hub)

> *Summary: This asynchronous method processes events received from a specific channel. It accepts the channel ID, event type (`kind`), and associated data (`payload`) as input, but currently returns nothing.*


### on_agent_event (method, L683-L684, parent: Hub)

> *Summary: This asynchronous method receives an agent ID, event type, and associated data. It serves as a hook to process events originating from other agents within the system.*


### on_expectation_fired (method, L686-L687, parent: Hub)

> *Summary: This asynchronous method handles the event when a predefined expectation is triggered within a communication channel. It accepts the channel ID, the fired expectation object, and the corresponding violation object as input, returning nothing upon execution.*


### on_turn_failed (method, L689-L696, parent: Hub)

> *Summary: This asynchronous method handles failures during a conversational turn. It accepts identifiers for the channel, agent, and message envelope, along with the exception that occurred, but currently performs no action other than returning.*


### on_task_event (method, L698-L699, parent: Hub)

> *Summary: This asynchronous method handles events related to a specific task. It accepts a task ID, an event type string, and a dictionary payload as input, returning nothing upon execution.*


### on_inbox_pressure (method, L701-L702, parent: Hub)

> *Summary: This asynchronous method accepts an agent ID, the number of pending items, and a capacity limit. It currently does nothing but returns immediately, suggesting it's a placeholder for handling inbox pressure notifications.*


### register_expectation_evaluator (method, L706-L711, parent: Hub)

> *Summary: Adds a specific expectation evaluation logic to the system, using the provided `ExpectationEvaluator`'s name as the unique key. If an evaluator with the same name already exists, it will be overwritten by the new one.*


### register_violation_handler (method, L713-L718, parent: Hub)

> *Summary: This method associates a specific `ViolationHandler` instance with its unique name within the object's internal registry. It overwrites any existing handler if one shares the same name, ensuring only one handler per name is active.*


### _expectation_tick (method, L720-L781, parent: Hub)

> *Summary: Evaluates all defined expectations against active channels using their current state and Write-Ahead Logs (WAL). It triggers registered handlers for any detected violations, ensuring each unique violation is only processed once per channel until the channel terminates.*


### register (method, L785-L839, parent: Hub)

> *Summary: Validates a provided `Passport` against its authentication scheme and then persists the agent's registration details (including `Resume`, optional `Rule`, and `skill_md`) to storage. It returns the updated `Passport` object, ensuring that no two agents can register with the same name without first unregistering.*


### unregister (method, L841-L892, parent: Hub)

> *Summary: Removes an agent's registration data from the hub state, including passports, resumes, rules, skills, and endpoint bindings, upon receiving an `agent_id`. It then cleans up associated on-disk identity files and notifies subscribers of the unregistration event.*


### get_agent (method, L896-L901, parent: Hub)

> *Summary: Retrieves a `Passport` object for a given agent name or ID by first resolving the input to an internal agent ID. It raises a `NotFoundError` if no corresponding passport is found in the stored collection.*


### get_resume (method, L903-L907, parent: Hub)

> *Summary: Retrieves a stored `Resume` object for a given agent ID from an internal dictionary. It raises a `NotFoundError` if no corresponding resume exists for the provided ID.*


### get_skill (method, L909-L917, parent: Hub)

> *Summary: Retrieves a skill associated with a given agent ID, first checking an in-memory cache; if absent, it queries a persistent store and updates the cache upon successful retrieval. Returns the skill string or `None` if no skill is found for the provided agent.*


### list_agents (method, L919-L960, parent: Hub)

> *Summary: Retrieves a list of registered participants, filtering them based on specified criteria like kind, capability, or a text query against their summary. It returns up to the limit number of matching `Passport` objects after optionally sorting by name.*


### set_resume (method, L964-L1003, parent: Hub)

> *Summary: Updates an agent's resume state by accepting an `agent_id` and a `Resume` object. It persists the new state, increments the version, and crucially updates an internal capability index to reflect changes in claimed or observed capabilities before broadcasting an event.*


### set_skill (method, L1005-L1019, parent: Hub)

> *Summary: Updates an agent's associated skill by either setting a new skill string or removing the existing one. It validates the agent ID against registered passports and then broadcasts an event notifying subscribers of the change.*


### set_rule (method, L1021-L1032, parent: Hub)

> *Summary: Updates an agent's associated rule by incrementing its version if it already exists in the system. It persists the updated rule and broadcasts a `rule_set` event to notify other components of the change.*


### record_observation (method, L1034-L1101, parent: Hub)

> *Summary: Updates an agent's observed statistics for a specific capability based on a terminal task event, using `owner_id`, `capability`, and the final `TaskState`. It increments counters (completed, failed, expired), optionally sets latency, and ensures unique recording via `task_id` before persisting state and broadcasting an event.*


### agents_with_capability (method, L1103-L1105, parent: Hub)

> *Summary: Retrieves a sorted list of agent IDs that possess a specified capability, checking both claimed and observed attributes within the internal capability index.*


### create_channel (method, L1109-L1276, parent: Hub)

> *Summary: This method initiates a new communication channel by first validating participants and authorizing the creation via an arbiter check. It then generates metadata, posts invitation events to all invitees, waits for acknowledgments within a timeout period, and finally transitions the channel state upon success or failure.*


### close_channel (method, L1278-L1280, parent: Hub)

> *Summary: Transitions a specified channel to the `CLOSED` state with an optional reason and returns the updated metadata for that channel.*


### get_channel (method, L1282-L1286, parent: Hub)

> *Summary: Retrieves the metadata for a specified channel ID from an internal dictionary, raising a `NotFoundError` if the ID does not exist. It accepts a string `channel_id` and returns the corresponding `ChannelMetadata` object.*


### can_send (method, L1288-L1320, parent: Hub)

> *Summary: Determines if a sender can submit content to a specific channel by validating the proposed send against the current adapter state. It wraps the underlying adapter's validation with a minimal probe envelope and returns `True` only if no exception occurs during this check.*


### default_view_policy (method, L1322-L1335, parent: Hub)

> *Summary: Retrieves the default view policy for a specific participant within a channel by first locating the channel's metadata and then delegating the request to the appropriate registered adapter. It raises an error if the specified channel ID cannot be found.*


### adapter_for (method, L1337-L1347, parent: Hub)

> *Summary: Retrieves the appropriate `ChannelAdapter` by looking up a given `channel_id` in internal channel metadata. It raises a `NotFoundError` if the specified channel ID does not exist before returning the resolved adapter instance.*


### adapter_state (method, L1349-L1356, parent: Hub)

> *Summary: Retrieves the current folded adapter state for a specified `channel_id` from internal storage, returning `None` if no state is cached for that channel. This method provides a public interface to access the stored states without direct internal access.*


### list_channels (method, L1358-L1372, parent: Hub)

> *Summary: Retrieves a list of channel metadata objects from internal storage, optionally filtering by a specific `ChannelState` or requiring participation from an `agent_id`. The method returns up to the specified `limit` number of matching channels.*


### read_wal (method, L1374-L1391, parent: Hub)

> *Summary: Retrieves a list of `Envelope` objects from the Write-Ahead Log (WAL) associated with a given channel ID. It filters these records based on optional start (`since`) and end (`until`) timestamps or indices, returning only the requested subset.*


### observe_task (method, L1395-L1431, parent: Hub)

> *Summary: Registers task metadata received from an agent stream, storing it and initiating TTL tracking without modifying the task itself. It checks against owner-defined concurrency limits before adding a new task to prevent exceeding `max_concurrent_tasks`.*


### get_task (method, L1433-L1437, parent: Hub)

> *Summary: Retrieves the metadata for a specific task using its ID from an internal task registry. It raises a `NotFoundError` if no matching task ID is present in the system.*


### update_task (method, L1439-L1469, parent: Hub)

> *Summary: This method updates the lifecycle of a specific task by accepting optional inputs for its state, progress, result, or error. It modifies the stored task metadata accordingly and persists these changes, ensuring terminal-state transitions are idempotent.*


### list_tasks (method, L1471-L1488, parent: Hub)

> *Summary: Retrieves a paginated list of task metadata from internal storage, optionally filtering by agent ID, channel ID, or specific task state. It returns up to the specified limit of matching `TaskMetadata` objects.*


### expire_due (method, L1492-L1515, parent: Hub)

> *Summary: This method iterates through active channels and standalone tasks to identify any that have passed their Time-To-Live (TTL). It then transitions these expired entities to an `EXPIRED` state, cascading closures for tasks under expiring channels.*


### post_envelope (method, L1519-L1546, parent: Hub)

> *Summary: This method validates an incoming `Envelope` by performing sender checks, adapter processing, WAL appending, and dispatching. It returns the unique ID of the posted envelope upon success or propagates a `NetworkError` after notifying listeners if validation fails.*


### _post_envelope_impl (method, L1548-L1676, parent: Hub)

> *Summary: This method processes an incoming `Envelope` by first authorizing the send based on sender rules and recipient audiences. It then validates channel state against registered adapters, atomically appends the event to a write-ahead log, folds it into the current state, and finally dispatches the event or handles specific protocol acknowledgments before notifying listeners of the successful post.*


### attach_endpoint (method, L1680-L1686, parent: Hub)

> *Summary: Registers a new `LinkEndpoint` by storing it in an internal map and concurrently starts a background task to manage its lifecycle. This method ensures the endpoint is only attached if the network hub is not already closed.*


### bind_endpoint (method, L1688-L1695, parent: Hub)

> *Summary: Attaches a specific endpoint to an agent by updating internal mappings. It requires valid `endpoint_id` and `agent_id`, raising errors if either is not found before establishing the association.*


### _wal_lock (method, L1699-L1704, parent: Hub)

> *Summary: Retrieves or creates an `asyncio.Lock` associated with a specific channel ID from internal storage. This ensures that concurrent operations targeting the same channel are serialized by returning the appropriate lock object.*


### _wal_append (method, L1706-L1707, parent: Hub)

> *Summary: This method asynchronously appends a serialized `Envelope` to the Write-Ahead Log (WAL) file corresponding to the channel ID. It ensures data persistence by writing the JSON representation of the envelope followed by a newline character.*


### _dispatch (method, L1709-L1769, parent: Hub)

> *Summary: Sends notification frames to specified recipients based on an incoming envelope and channel metadata. It first resolves unknown audience IDs via a federation hook, then iterates through recipients, checking authorization rules before sending the frame or updating inbox pressure counters.*


### _maybe_fire_inbox_pressure (method, L1771-L1793, parent: Hub)

> *Summary: This method checks if the inbox pressure for a given recipient has crossed the defined high-water mark. If it crosses from below to above this threshold, it asynchronously broadcasts an `on_inbox_pressure` event using the current pending count and capacity.*


### _endpoint_for (method, L1795-L1799, parent: Hub)

> *Summary: Retrieves the `LinkEndpoint` associated with a given agent ID by first looking up the corresponding endpoint ID in an internal mapping, and then fetching the endpoint object itself. Returns `None` if no endpoint is mapped to the provided agent ID.*


### _handle_endpoint (method, L1801-L1808, parent: Hub)

> *Summary: This method asynchronously iterates over frames provided by a `LinkEndpoint` and dispatches each one using an internal handler. It gracefully handles cancellation errors while suppressing other exceptions during the processing loop.*


### _dispatch_frame (method, L1810-L1829, parent: Hub)

> *Summary: This method processes incoming network frames by dispatching actions based on the frame type. It handles `SendFrame` by posting an envelope and sending an acknowledgment, validates `HelloFrame` to bind endpoints, and responds to `PingFrame` with a `PongFrame`.*


### _handle_invite_ack (method, L1833-L1840, parent: Hub)

> *Summary: When an invitation acknowledgment is received for a pending channel, this method removes the sender from the list of pending acknowledgments if they were tracked. If no other pending acknowledgments or rejections exist, it proceeds to activate the channel.*


### _handle_invite_reject (method, L1842-L1854, parent: Hub)

> *Summary: When a pending channel receives an invite rejection, this method updates the channel metadata to record the rejection and immediately transitions the channel state to closed. It then notifies any waiting coroutines associated with that channel of the failure.*


### _activate_channel (method, L1856-L1879, parent: Hub)

> *Summary: When a channel's metadata indicates it is pending, this method transitions its state to active, persists the change, logs the event, broadcasts an "opened" notification, posts a corresponding envelope, and resolves any waiting tasks for that channel. It requires a `channel_id` string as input and performs asynchronous updates and notifications internally.*


### _transition_channel (method, L1881-L1952, parent: Hub)

> *Summary: Updates a channel's state based on provided ID, new state, and reason. If the transition is terminal, it cascades task expirations, records closure details, dispatches a closing envelope via WAL, and notifies listeners before cleaning up internal synchronization primitives.*


### _transition_task (method, L1954-L1982, parent: Hub)

> *Summary: Updates a task's state based on the provided `new_state` and `reason`, persisting changes to internal storage. If the transition results in a terminal state, it records completion time, sets an error if expired, and broadcasts an event notification to subscribers.*


### _persist_passport (method, L1986-L1988, parent: Hub)

> *Summary: This method asynchronously saves a `Passport` object to persistent storage using the agent's ID as part of the file path. It serializes the passport data into JSON before writing it to disk via the internal store.*


### _persist_resume (method, L1990-L1991, parent: Hub)

> *Summary: Saves the state of a given `Resume` object for an agent to disk using its ID as part of the file path. This asynchronous method serializes the resume data into JSON and writes it to storage.*


### _persist_rule (method, L1993-L1994, parent: Hub)

> *Summary: This method asynchronously saves a given `Rule` object to persistent storage using the agent's ID as part of the file path. It serializes the rule into JSON before writing it to disk.*


### _persist_skill (method, L1996-L1997, parent: Hub)

> *Summary: This asynchronous method saves a specific skill's markdown content to persistent storage using the provided agent ID and skill data. It writes the `skill_md` to a file path determined by the `agent_id`.*


### _persist_capability_index (method, L1999-L2002, parent: Hub)

> *Summary: This method serializes the internal capability index into a deterministic JSON format by sorting IDs within each capability group. It then asynchronously writes this snapshot to persistent storage using a specific path derived from the object's state.*


### _persist_channel_metadata (method, L2004-L2008, parent: Hub)

> *Summary: This method asynchronously saves the provided `ChannelMetadata` object to a file path derived from its ID. It serializes the metadata into JSON format before writing it to the underlying storage mechanism.*


### _persist_task_metadata (method, L2010-L2014, parent: Hub)

> *Summary: This asynchronous method saves the provided `TaskMetadata` object to disk using a specified path derived from its ID. It serializes the metadata into JSON format before writing it to the underlying storage mechanism.*


### _load_agent (method, L2016-L2032, parent: Hub)

> *Summary: Retrieves and initializes an agent's state by fetching passport, resume, and rule data from persistent storage using the provided `agent_id`. It populates internal dictionaries with these loaded objects, ensuring a default `Rule` object exists if none is found.*


### _load_channel (method, L2034-L2058, parent: Hub)

> *Summary: Retrieves and processes channel metadata from storage using a provided `channel_id`. It then initializes or updates the corresponding adapter's state by folding all entries found in the channel's Write-Ahead Log (WAL).*


### _load_task (method, L2060-L2067, parent: Hub)

> *Summary: Retrieves task metadata from storage using a provided `task_id`, parses it, and then registers the resulting metadata into the internal tasks dictionary. If the loaded metadata contains a channel ID, the task is also added to the corresponding channel's set of tasks.*


### _task_metadata_to_dict (function, L2070-L2095)

> *Summary: Converts a `TaskMetadata` object into a serializable dictionary format suitable for persistence. It specifically transforms the enum state to a string and nests the task specification details within the output structure.*


### _task_metadata_from_dict (function, L2098-L2126)

> *Summary: Parses a dictionary containing task data to construct a `TaskMetadata` object. It extracts and validates fields like title, description, capability, state, and various timestamps from the input dictionary.*

