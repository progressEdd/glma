# autogen/beta/network/client/channel.py

1 class(es): Channel. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Channel | class |  |

## Chunks

### Channel (class, L23-L97)

> *Summary: Represents a participant's handle to a communication channel, initialized with metadata and an agent client. It allows sending structured envelopes to the channel, refreshing its state via `info()`, closing the connection using `close()`, and checking if the channel is terminal.*


### __init__ (method, L31-L39, parent: Channel)

> *Summary: Initializes a channel object by storing provided `ChannelMetadata` and a reference to an `AgentClient`. This constructor performs only state setup without causing any external side effects.*


### channel_id (method, L42-L43, parent: Channel)

> *Summary: Retrieves the unique identifier for the current communication channel from the object's metadata. This method returns a string representing the channel ID.*


### metadata (method, L46-L47, parent: Channel)

> *Summary: Returns the stored `ChannelMetadata` object associated with the channel instance. This method provides read access to the channel's descriptive information.*


### state (method, L50-L51, parent: Channel)

> *Summary: Retrieves the current operational status of the channel by accessing and returning the `state` attribute from the internal metadata object. This method provides a snapshot of the channel's lifecycle stage.*


### send (method, L53-L84, parent: Channel)

> *Summary: Constructs an `Envelope` object using provided content or event data and sends it through the underlying client connection. It handles optional parameters like audience targeting, causation IDs, and delegation depth before returning the result of the send operation.*


### info (method, L86-L90, parent: Channel)

> *Summary: This method asynchronously fetches and updates the channel's metadata by querying the hub client using the stored `channel_id`. It returns the newly retrieved `ChannelMetadata` object, effectively refreshing any cached state.*


### close (method, L92-L94, parent: Channel)

> *Summary: This method initiates the closure of the current communication channel by calling a remote hub client function with an optional closing reason. It returns metadata describing the state of the closed channel.*


### is_terminal (method, L96-L97, parent: Channel)

> *Summary: Checks the internal metadata to determine if the current channel has reached a terminal state, returning a boolean indicating its status.*

