# autogen/beta/network/transport/local.py

3 class(es): LocalLinkClient, LocalLinkEndpoint, LocalLink. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LocalLinkClient | class |  |
| LocalLinkEndpoint | class |  |
| LocalLink | class |  |

## Chunks

### LocalLinkClient (class, L34-L79)

> *Summary: Manages the tenant-side half of an in-memory duplex connection using two provided `asyncio.Queue`s for communication. It allows sending frames to the hub via one queue and asynchronously iterating over received frames from the other, terminating cleanly upon calling `close()`.*


### __init__ (method, L42-L52, parent: LocalLinkClient)

> *Summary: Initializes a local transport mechanism by storing an endpoint identifier and two asyncio queues: one for messages from the client to the hub, and another for messages from the hub to the client. It sets up these communication channels without performing any immediate side effects.*


### open (method, L54-L56, parent: LocalLinkClient)

> *Summary: This method performs no operation, as the network connection is established implicitly when a `LocalLink` client is created. It returns nothing upon execution.*


### send_frame (method, L58-L61, parent: LocalLinkClient)

> *Summary: This method asynchronously sends a `Frame` object by placing it into an internal channel (`_c2h`) if the transport is not closed. It acts as a non-blocking queue insertion for outgoing data.*


### frames (method, L63-L64, parent: LocalLinkClient)

> *Summary: Returns an asynchronous iterator yielding `Frame` objects by calling the internal implementation method. This provides a stream of frame data from the transport layer.*


### _frames_impl (method, L66-L71, parent: LocalLinkClient)

> *Summary: This method asynchronously yields `Frame` objects from an internal channel until the channel signals completion by yielding `None`. It acts as a consumer loop over incoming frames.*


### close (method, L73-L79, parent: LocalLinkClient)

> *Summary: This method safely terminates the transport connection by setting an internal closed flag and sending a `None` sentinel value through both the client-to-host and host-to-client communication channels to signal handlers to stop iterating.*


### LocalLinkEndpoint (class, L82-L124)

> *Summary: Represents the hub-side half of an in-memory duplex connection, managing bidirectional frame transfer between two queues. It allows sending frames from the hub to the client via `send_frame` and asynchronously iterating over incoming frames from the client using `frames()`. Closing the endpoint signals termination by placing `None` into both associated queues.*


### __init__ (method, L91-L102, parent: LocalLinkEndpoint)

> *Summary: Initializes a local transport mechanism by storing an endpoint identifier and two asynchronous queues for communication between clients and the central hub. These queues, `client_to_hub` and `hub_to_client`, are used to manage incoming and outgoing frame data.*


### send_frame (method, L104-L107, parent: LocalLinkEndpoint)

> *Summary: This method asynchronously sends a `Frame` object through the underlying transport layer (`self._h2c`) if the connection is not closed. It acts as a simple forwarding mechanism for outgoing data frames.*


### frames (method, L109-L110, parent: LocalLinkEndpoint)

> *Summary: Returns an asynchronous iterator yielding `Frame` objects by calling the internal implementation method. This provides a stream of message frames from the transport layer.*


### _frames_impl (method, L112-L117, parent: LocalLinkEndpoint)

> *Summary: This method asynchronously yields `Frame` objects from a channel (`self._c2h`) until the channel signals completion by returning `None`. It acts as an iterator to stream incoming frames.*


### close (method, L119-L124, parent: LocalLinkEndpoint)

> *Summary: This method safely shuts down the transport by setting an internal closed flag and signaling termination to both the client-to-host and host-to-client communication channels via `put(None)`. It prevents redundant closing operations if already shut down.*


### LocalLink (class, L127-L158)

> *Summary: This factory creates in-process duplex communication pairs against a provided `Hub`. Calling the `client()` method generates a new endpoint and client pair, immediately registering the endpoint with the hub to initiate frame processing tasks.*


### __init__ (method, L142-L144, parent: LocalLink)

> *Summary: Initializes the transport layer by storing a reference to a provided `Hub` object. This setup defers any actual network communication logic until a subsequent method call.*


### hub (method, L147-L148, parent: LocalLink)

> *Summary: Returns the internal `_hub` object, which represents the central communication point for this transport layer implementation.*


### client (method, L150-L158, parent: LocalLink)

> *Summary: This method initializes and registers a new local endpoint with the hub by creating unique queues for communication. It then returns a fully configured `LocalLinkClient` instance associated with that newly attached endpoint.*

