# autogen/beta/network/client/agent_client.py

1 class(es): AgentClient. 25 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AgentClient | class |  |

## Chunks

### AgentClient (class, L51-L314)

> *Summary: Manages an agent's interaction with a network hub by holding references to its identity, rules, and communication channels. It handles receiving incoming envelopes via dedicated inboxes, allows sending messages through the hub client, and provides methods for lifecycle management like opening channels or updating agent metadata.*


### __init__ (method, L54-L87, parent: AgentClient)

> *Summary: Initializes a client by storing references to core components like an `Agent`, `Passport`, and `Rule`. It sets up internal state, including queues for channel events and stacks to track currently processed envelopes.*


### agent (method, L92-L93, parent: AgentClient)

> *Summary: Returns the internal `Agent` instance held by the client object. This method provides direct access to the managed agent resource.*


### passport (method, L96-L97, parent: AgentClient)

> *Summary: Returns the internal `Passport` object associated with the client instance. This method provides read access to the stored credential information.*


### resume (method, L100-L101, parent: AgentClient)

> *Summary: Returns the stored `Resume` object from an internal attribute, effectively retrieving the agent's saved state or profile.*


### rule (method, L104-L105, parent: AgentClient)

> *Summary: Returns the internal `Rule` object associated with the client instance. This method provides read access to the configured rule set.*


### agent_id (method, L108-L111, parent: AgentClient)

> *Summary: Retrieves the unique identifier for the client's associated agent, raising an error if the internal passport object lacks a registered ID.*


### receive (method, L115-L122, parent: AgentClient)

> *Summary: This method accepts an `Envelope` and routes it to the corresponding channel's inbox for storage. It then optionally executes a registered handler function if the envelope's channel ID is not suppressed.*


### on_envelope (method, L124-L131, parent: AgentClient)

> *Summary: Sets a custom handler for envelope notifications, allowing external logic to process incoming envelopes. If this method is called with `None` or by using the default constructor, the original notification mechanism is restored.*


### disconnect (method, L133-L135, parent: AgentClient)

> *Summary: Sets an internal flag to indicate the client is disconnected and clears any registered envelope handler. This method signals a clean shutdown state for the agent client.*


### _run_default_handler (method, L137-L149, parent: AgentClient)

> *Summary: This method wraps the standard handler by pushing an incoming `Envelope` onto a stack before execution. It ensures that any nested calls within the LLM turn can correctly increment the envelope's depth for rule enforcement, and then pops the envelope upon completion.*


### current_handling_depth (method, L152-L161, parent: AgentClient)

> *Summary: Retrieves the nesting level of envelope processing for this agent. It returns zero if no envelopes are currently being handled on the internal stack, otherwise it returns the depth of the topmost envelope.*


### open (method, L165-L202, parent: AgentClient)

> *Summary: Establishes a communication channel through the hub by resolving target names or IDs and creating a channel manifest. It returns a `Channel` handle object upon successful creation, provided the client is connected.*


### ensure_channel_inbox (method, L204-L219, parent: AgentClient)

> *Summary: Retrieves or creates an `asyncio.Queue` associated with a specific channel ID, storing it internally if new. This ensures that incoming messages for a given channel are always directed to a dedicated queue before any sending operations occur.*


### discard_channel_inbox (method, L221-L228, parent: AgentClient)

> *Summary: Removes a specific channel's inbox queue from the client's internal storage using its ID. This is intended to prevent memory accumulation after a channel has been fully processed.*


### wait_for_channel_event (method, L230-L256, parent: AgentClient)

> *Summary: This asynchronous method blocks execution until an incoming message on a specified channel satisfies a given condition, raising a `TimeoutError` if the wait exceeds the provided duration. It utilizes a shared inbox mechanism to efficiently await and filter for matching envelopes.*


### _suppress_handler (method, L258-L265, parent: AgentClient)

> *Summary: Adds a specified `channel_id` to an internal set, effectively preventing the agent's default notification handler from processing incoming events for that channel. This mechanism allows another component, like a delegate, to manage the channel lifecycle without interference from standard event handling logic.*


### _unsuppress_handler (method, L267-L268, parent: AgentClient)

> *Summary: Removes a specified `channel_id` from the internal set of suppressed channels. This method is called to explicitly allow communication on a previously blocked channel.*


### send_envelope (method, L272-L278, parent: AgentClient)

> *Summary: This method posts a given `Envelope` object to the hub, automatically setting the sender ID if it's empty. It returns the unique identifier assigned to the posted envelope upon successful transmission.*


### set_resume (method, L282-L285, parent: AgentClient)

> *Summary: This method updates the agent's resume status by calling a remote hub client with the provided `Resume` object. It then refreshes the local cache by fetching and storing the latest resume from the hub.*


### add_example (method, L287-L296, parent: AgentClient)

> *Summary: This method appends a provided `ResumeExample` to the agent's resume by first fetching the current version from the hub, modifying it locally, and then saving the updated resume back. This ensures that concurrent updates do not overwrite each other.*


### set_skill (method, L298-L299, parent: AgentClient)

> *Summary: This method asynchronously updates the agent's registered skill by calling a corresponding function on the internal hub client, using the provided string or `None` as input. It performs no return value.*


### set_rule (method, L301-L303, parent: AgentClient)

> *Summary: This method asynchronously sends a specified `Rule` object to the hub client using the agent's ID and then updates the local instance's stored rule with the provided input.*


### unregister (method, L305-L308, parent: AgentClient)

> *Summary: This method asynchronously notifies the central hub that the agent is no longer active by calling `unregister_agent` with the agent's ID, and then sets an internal flag to mark the client as disconnected.*


### __aenter__ (method, L310-L311, parent: AgentClient)

> *Summary: When used as an asynchronous context manager, this method returns the client instance itself. This allows for setup and teardown logic to be managed cleanly around operations involving the agent client.*


### __aexit__ (method, L313-L314, parent: AgentClient)

> *Summary: When an asynchronous context manager exits, this method ensures the client unregisters itself by calling `self.unregister()`. It handles cleanup automatically upon exiting the `async with` block.*

