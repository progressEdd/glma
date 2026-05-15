# autogen/beta/network/transport/link.py

2 class(es): LinkClient, LinkEndpoint. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LinkClient | class |  |
| LinkEndpoint | class |  |

## Chunks

### LinkClient (class, L25-L55)

> *Summary: Represents a tenant's interface for interacting with a central hub, providing methods to establish a connection, send outgoing data frames, stream incoming frames asynchronously, and gracefully close the link. It requires an `endpoint_id` to identify its connection context.*


### open (method, L34-L40, parent: LinkClient)

> *Summary: Establishes the network connection and performs a "hello" handshake, expecting a "welcome" response from the peer. For local links, this operation does nothing as the connection is established upon object creation.*


### send_frame (method, L42-L44, parent: LinkClient)

> *Summary: This asynchronous method pushes a given `Frame` object toward the network hub. It handles the transmission of data frames within the transport layer.*


### frames (method, L46-L51, parent: LinkClient)

> *Summary: Provides an asynchronous iterator yielding incoming `Frame` objects received from the network hub until a close signal is issued.*


### close (method, L53-L55, parent: LinkClient)

> *Summary: This asynchronous method drains internal queues and sends a closure signal to the associated hub-side handler. It is responsible for gracefully shutting down the transport link's communication channels.*


### LinkEndpoint (class, L58-L78)

> *Summary: Defines a protocol for representing a single connection endpoint on the hub side. It provides methods to asynchronously send frames to the connected client and iterate over incoming frames from that client.*


### send_frame (method, L68-L70, parent: LinkEndpoint)

> *Summary: Asynchronously pushes a given `Frame` object out to the connected client. This method handles the transmission of data frames across the network link.*


### frames (method, L72-L74, parent: LinkEndpoint)

> *Summary: Provides an asynchronous iterator yielding incoming `Frame` objects received from a connected client. This method allows consumers to process data as it arrives over the network link.*


### close (method, L76-L78, parent: LinkEndpoint)

> *Summary: This method asynchronously drains internal queues and signals a closing event to the connected client-side handler. It is responsible for gracefully shutting down the transport link.*

