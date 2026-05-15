# autogen/beta/network/client/hub_client.py

1 class(es): HubClient. 35 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| HubClient | class |  |

## Chunks

### HubClient (class, L46-L484)

> *Summary: Manages a single connection to a hub, handling inbound frame demultiplexing and routing notifications to registered agents or humans. It provides methods to register participants, discover entities (agents/channels), mutate state, and interact with the hub's control plane via direct calls to an internal `Hub` reference.*


### __init__ (method, L59-L66, parent: HubClient)

> *Summary: Initializes the client by storing a local link and an optional hub reference; it also sets up internal state variables for managing connections, tasks, and registered clients. The constructor defaults to using the provided link's hub if no explicit hub is given.*


### _ensure_connected (method, L70-L75, parent: HubClient)

> *Summary: This method establishes and returns a connection to the client if one hasn't been created yet. It initializes the link by calling `self._link.client()` and starts an asynchronous receiving task upon first invocation.*


### _receive_loop (method, L77-L105, parent: HubClient)

> *Summary: This asynchronous method continuously reads incoming frames from a client link and dispatches `NotifyFrame` instances to their respective handlers. It handles exceptions during frame dispatch by logging the error while keeping the loop alive, and catches transport-level errors to log termination without propagating them.*


### _dispatch_notify (method, L107-L125, parent: HubClient)

> *Summary: Routes a notification frame to the intended recipient or recipients based on its `recipient_id` or `audience`. If a specific `recipient_id` exists, it delivers directly; otherwise, it iterates through the audience list and sends the message to all matching clients.*


### register (method, L129-L185, parent: HubClient)

> *Summary: Registers an agent with the hub using provided credentials and profile information, returning a handle to interact with the newly registered agent. It ensures the connection is active, validates that the participant is not human, registers the entity via the hub, binds the local endpoint to the new agent ID, and optionally attaches network-specific tools to the agent.*


### register_human (method, L187-L239, parent: HubClient)

> *Summary: Registers a non-LLM participant using a provided `Passport`, optionally with a `Resume` and `Rule`. It forces the passport's kind to "human" and returns a specialized `HumanClient` handle, which manages inbound/outbound communication for that human agent.*


### get_agent (method, L249-L250, parent: HubClient)

> *Summary: Retrieves a specific agent from the hub using either its name or ID as input. It asynchronously returns the corresponding `Passport` object.*


### get_resume (method, L252-L253, parent: HubClient)

> *Summary: Retrieves a `Resume` object for a specified `agent_id` by forwarding the request to an underlying hub client. This asynchronous method acts as a simple wrapper around the hub's resume retrieval functionality.*


### get_skill (method, L255-L256, parent: HubClient)

> *Summary: Retrieves a specific skill string from the hub using an provided `agent_id`. It acts as a direct asynchronous wrapper around the underlying hub's `get_skill` method.*


### list_agents (method, L258-L273, parent: HubClient)

> *Summary: Retrieves a paginated list of agents from the underlying hub client based on optional filtering criteria like capability, query string, kind, and sorting preference. It returns a list of `Passport` objects representing the matching agents.*


### set_resume (method, L277-L278, parent: HubClient)

> *Summary: This method asynchronously delegates the setting of a resume state for a specific agent ID to the underlying hub client. It takes an `agent_id` string and a `Resume` object as input and returns nothing upon successful execution.*


### set_skill (method, L280-L281, parent: HubClient)

> *Summary: This method asynchronously updates the skills associated with a specific agent ID by calling an underlying hub client. It accepts an agent identifier and an optional string representing the new skill definition.*


### set_rule (method, L283-L284, parent: HubClient)

> *Summary: This method asynchronously delegates the setting of a specific `Rule` for an `agent_id` to the underlying hub client. It takes an agent identifier and a rule object as input and returns nothing upon successful execution.*


### unregister_agent (method, L286-L287, parent: HubClient)

> *Summary: This method asynchronously removes a specified agent from the central hub by calling the underlying hub's unregister function with the provided agent ID. It takes an `agent_id` string as input and returns nothing upon successful execution.*


### create_channel (method, L291-L314, parent: HubClient)

> *Summary: This method initiates a new communication channel on the hub by forwarding all provided configuration parameters—such as creator ID, manifest type, participants, and optional settings like TTL or labels—to the underlying hub service. It returns the metadata describing the newly created channel upon successful creation.*


### get_channel (method, L316-L317, parent: HubClient)

> *Summary: Retrieves metadata for a specific communication channel by accepting a `channel_id` string as input and returning the corresponding `ChannelMetadata` object. This method acts as a direct asynchronous wrapper around the underlying hub's get\_channel functionality.*


### list_channels (method, L319-L329, parent: HubClient)

> *Summary: Retrieves a paginated list of channel metadata from the underlying hub client. It optionally filters out closed or expired channels and limits the final returned set to the specified count.*


### close_channel (method, L331-L332, parent: HubClient)

> *Summary: This method asynchronously signals the hub to terminate a specific communication channel using its ID and an optional reason string. It returns metadata describing the closed channel upon successful execution.*


### post_envelope (method, L334-L335, parent: HubClient)

> *Summary: This method forwards an incoming `Envelope` object to the underlying hub client and returns the resulting string response from that call. It acts as a simple asynchronous wrapper for posting envelopes.*


### report_turn_failure (method, L337-L358, parent: HubClient)

> *Summary: This method reports a failure that occurred during an agent's turn by forwarding the exception and associated IDs to the underlying hub. It ensures the failure is broadcast to all registered listeners for observability purposes.*


### fire_task_event (method, L360-L367, parent: HubClient)

> *Summary: This method broadcasts a task lifecycle event across all registered listeners via the underlying hub. It accepts a `task_id`, an event `kind` string, and a `payload` dictionary as input, performing no return value.*


### read_wal (method, L369-L370, parent: HubClient)

> *Summary: Retrieves a list of `Envelope` objects from the hub's write-ahead log for a specified channel ID. It accepts optional start (`since`) and end (`until`) timestamps to filter the returned records.*


### can_send (method, L372-L379, parent: HubClient)

> *Summary: Delegates the check to an internal hub object to determine if a specific sender is permitted to transmit on a given channel for an optional event type. Returns a boolean indicating permission status.*


### default_view_policy (method, L381-L382, parent: HubClient)

> *Summary: This method delegates the determination of a view policy to the underlying hub object, accepting a `channel_id` and `participant_id` as input and returning a `ViewPolicy`.*


### adapter_for (method, L384-L391, parent: HubClient)

> *Summary: Retrieves the appropriate `ChannelAdapter` instance by forwarding the provided `channel_id` request to the internal hub object. This method ensures external code can access adapters without directly accessing private hub members.*


### adapter_state (method, L393-L399, parent: HubClient)

> *Summary: Retrieves the cached `AdapterState` object for a given channel ID by forwarding the request to the underlying hub client. It returns `None` if no state is currently available for that channel.*


### get_task (method, L403-L404, parent: HubClient)

> *Summary: Retrieves the metadata for a specific task by accepting a `task_id` string as input and returning a `TaskMetadata` object. This method acts as a direct asynchronous wrapper around the underlying hub's task retrieval functionality.*


### list_tasks (method, L406-L419, parent: HubClient)

> *Summary: Retrieves a paginated list of task metadata from the underlying hub client. It accepts optional filters for agent ID, channel ID, and task state, along with a limit on the number of results returned.*


### observe_task (method, L421-L422, parent: HubClient)

> *Summary: This method asynchronously forwards a `TaskMetadata` object to the internal hub's observation mechanism. It serves as a simple wrapper to pass task state information upstream.*


### update_task (method, L424-L439, parent: HubClient)

> *Summary: This method asynchronously relays updates for a specific task ID to the underlying hub client. It accepts optional parameters like new state, progress details, final result, or error messages to modify the task's status remotely.*


### record_observation (method, L441-L456, parent: HubClient)

> *Summary: This method asynchronously forwards observation data—including owner ID, capability, task state, and optional latency/task IDs—to the underlying hub client. It serves as a wrapper to record performance metrics for specific tasks within the system.*


### close (method, L460-L470, parent: HubClient)

> *Summary: This method safely terminates the client connection and stops any ongoing receive operations. It first checks if it's already closed, then closes the underlying link and cancels the background receiving task, handling potential cancellation errors gracefully.*


### shutdown (method, L472-L478, parent: HubClient)

> *Summary: This method gracefully terminates the hub by iterating through all registered agent clients, calling `unregister()` on each to remove them, clearing the internal client registry, and finally closing the hub itself.*


### __aenter__ (method, L480-L481, parent: HubClient)

> *Summary: When used as an asynchronous context manager, this method returns the client instance itself. This allows for setup and teardown logic to be managed cleanly around resource usage.*


### __aexit__ (method, L483-L484, parent: HubClient)

> *Summary: When an asynchronous context manager exits, this method ensures the underlying connection is properly closed by calling `self.close()`. It handles any exceptions that occurred within the managed block without propagating them further.*

