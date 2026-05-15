# autogen/beta/network/client/human_client.py

1 class(es): HumanClient. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| HumanClient | class |  |

## Chunks

### HumanClient (class, L54-L437)

> *Summary: Manages interactions for a non-LLM participant, receiving and sending network envelopes via an associated `HubClient`. It provides pull interfaces (`next_envelope`, `envelopes`) to consume inbound messages from a global queue or specific channel inboxes, while also supporting push callbacks.*


### __init__ (method, L62-L99, parent: HumanClient)

> *Summary: Initializes the client by storing configuration objects like `Passport`, `Resume`, and `Rule`, along with communication handlers (`Hub`, `HubClient`). It sets up an unbounded internal queue for receiving all incoming messages and a dictionary of per-channel queues to support waiting for specific replies.*


### agent_id (method, L104-L107, parent: HumanClient)

> *Summary: Retrieves the unique identifier for the client's agent from the internal passport object, raising an error if the ID has not been set.*


### passport (method, L110-L111, parent: HumanClient)

> *Summary: Returns the stored `Passport` object associated with the client instance. This method provides direct access to the client's credential data.*


### resume (method, L114-L115, parent: HumanClient)

> *Summary: Returns the stored `Resume` object from an internal attribute. This method provides access to the client's saved state or profile information.*


### rule (method, L118-L119, parent: HumanClient)

> *Summary: Returns the internal `Rule` object associated with this client instance. This method provides access to the predefined operational rules governing the client's behavior.*


### receive (method, L123-L173, parent: HumanClient)

> *Summary: Receives an incoming `Envelope` from the hub, first automatically acknowledging channel invites if configured. It then places the envelope into a per-channel inbox and a global pull queue before sequentially dispatching it to registered push callbacks, logging any exceptions encountered during callback execution.*


### disconnect (method, L175-L193, parent: HumanClient)

> *Summary: This method signals a client's disconnection by setting an internal flag and injecting `None` sentinels into the main and all channel-specific message queues. This action unblocks any consumers currently waiting on these queues, allowing them to gracefully terminate or raise an end-of-stream signal.*


### receive_chunk (method, L195-L211, parent: HumanClient)

> *Summary: This method acts as a placeholder for handling streaming output chunks from an LLM, accepting a delta object and channel/envelope IDs. It currently does nothing (`return None`), but subclasses can override it to process token-level updates for UI display.*


### on_envelope (method, L215-L222, parent: HumanClient)

> *Summary: Registers a provided `EnvelopeCallback` to be executed for every incoming envelope. Callbacks are chained in registration order, and any exceptions they raise are logged without interrupting the main message dispatch flow.*


### remove_envelope_callback (method, L224-L227, parent: HumanClient)

> *Summary: Detaches a specific `EnvelopeCallback` from the client's registered callbacks, safely ignoring errors if the callback was not present.*


### next_envelope (method, L231-L264, parent: HumanClient)

> *Summary: Waits asynchronously for an incoming `Envelope` from the client's inbox, optionally filtering results using a provided `predicate`. It blocks until a matching envelope arrives or a specified timeout expires, raising errors upon disconnection.*


### envelopes (method, L266-L280, parent: HumanClient)

> *Summary: This method asynchronously streams incoming `Envelope` objects from an internal inbox until a disconnect signal (`None`) is received. It yields each received envelope in the order of arrival, terminating when the sentinel value signals disconnection.*


### send (method, L284-L306, parent: HumanClient)

> *Summary: This method constructs and posts a standard `EV_TEXT` envelope to a specified channel. It takes the target channel ID, the message text, and optional audience or causation IDs as input, returning the unique identifier of the posted envelope.*


### post_envelope (method, L308-L319, parent: HumanClient)

> *Summary: This method sends a provided `Envelope` object through the connected hub client, ensuring the sender ID is set to the agent's ID if it was not specified in the envelope. It raises an error if the client is currently disconnected before posting the message.*


### open (method, L321-L357, parent: HumanClient)

> *Summary: Initiates a communication channel by resolving target names or IDs through the bound `HubClient` and creating metadata for the connection. It returns a `Channel` handle upon successful creation, provided the client is connected.*


### close_channel (method, L359-L363, parent: HumanClient)

> *Summary: This method terminates the connection for a specified channel ID, optionally providing a closing reason. It delegates the actual closure to an underlying hub client and returns the resulting channel metadata upon success.*


### send_envelope (method, L371-L373, parent: HumanClient)

> *Summary: This method acts as a channel-compatible wrapper around `post_envelope`, accepting an `Envelope` object and returning the resulting string after posting it.*


### ensure_channel_inbox (method, L375-L382, parent: HumanClient)

> *Summary: Provides a public interface to retrieve or create an asynchronous queue for a specific channel ID. It delegates the actual inbox creation logic to an internal helper method, ensuring uniform access for future client implementations.*


### wait_for_channel_event (method, L384-L411, parent: HumanClient)

> *Summary: This asynchronous method blocks execution until an incoming message within a specified channel matches a given predicate, respecting a defined timeout. It retrieves messages from the client's inbox and returns the first matching `Envelope` or raises a `TimeoutError` if no match occurs within the allotted time.*


### _ensure_channel_inbox (method, L415-L425, parent: HumanClient)

> *Summary: Retrieves or creates an `asyncio.Queue` for a given channel ID, storing it in internal state. If the client is currently disconnected, it immediately seeds the new queue with `None` to prevent indefinite blocking on subsequent event waits.*


### hub_client (method, L432-L433, parent: HumanClient)

> *Summary: Returns the internal `HubClient` instance managed by the object. This method provides access to the established connection client for interacting with a central hub.*


### hub (method, L436-L437, parent: HumanClient)

> *Summary: Returns the internal `_hub` object, which is typed as either a `Hub` instance or `None`. This method provides access to the client's central communication hub.*

