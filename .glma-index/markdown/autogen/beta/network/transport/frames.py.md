# autogen/beta/network/transport/frames.py

2 function(s): encode_frame, decode_frame. 12 class(es): HelloFrame, WelcomeFrame, PingFrame, PongFrame, SendFrame, AcceptFrame, ErrorFrame, NotifyFrame, ReceiptFrame, SubscribeFrame, UnsubscribeFrame, EventFrame.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| HelloFrame | class |  |
| WelcomeFrame | class |  |
| PingFrame | class |  |
| PongFrame | class |  |
| SendFrame | class |  |
| AcceptFrame | class |  |
| ErrorFrame | class |  |
| NotifyFrame | class |  |
| ReceiptFrame | class |  |
| SubscribeFrame | class |  |
| UnsubscribeFrame | class |  |
| EventFrame | class |  |
| encode_frame | function |  |
| decode_frame | function |  |

## Chunks

### HelloFrame (class, L42-L53)

> *Summary: Represents a connection initiation message sent from a client to the hub. It carries a `name` for identity management and optional authentication details via `auth_scheme` and `auth_claim`.*


### WelcomeFrame (class, L57-L62)

> *Summary: Represents a welcome message sent from the hub to a client upon successful handshake. It encapsulates the connection's unique ID and the current time reported by the hub.*


### PingFrame (class, L66-L69)

> *Summary: Represents a heartbeat message used for bidirectional communication checks, identified by the constant `"ping"`. This structure is intended to be sent across network links as a simple status signal.*


### PongFrame (class, L73-L76)

> *Summary: Represents a heartbeat reply message, designated with the `"pong"` kind. This class serves as a standardized structure for bidirectional acknowledgment traffic.*


### SendFrame (class, L80-L88)

> *Summary: Represents a message intended for the hub, acting as an envelope to be posted into a channel. It contains an `Envelope` object that will be stamped by the hub upon acceptance or rejection.*


### AcceptFrame (class, L92-L96)

> *Summary: Represents an acknowledgment frame sent from the hub to a client, confirming receipt of a previous message using its unique `envelope_id`. This structure is used specifically for acknowledging outgoing transmissions.*


### ErrorFrame (class, L100-L111)

> *Summary: Represents a structured rejection message sent from the hub to a client. It contains an error code, a descriptive message, and optionally an `envelope_id` if the error pertains to a specific transmission.*


### NotifyFrame (class, L115-L128)

> *Summary: Represents a message envelope intended for delivery from the hub to a specific client participant. It carries an `Envelope` payload and includes a `recipient_id` to allow direct demultiplexing by the `HubClient`.*


### ReceiptFrame (class, L132-L144)

> *Summary: Represents a message sent from a client to the hub to acknowledge or negatively acknowledge a notification. It carries an envelope ID, a status ("ack" or "nack"), and an optional diagnostic reason for logging purposes.*


### SubscribeFrame (class, L148-L162)

> *Summary: Represents a client request to establish a push subscription on a specific channel or task. It accepts optional identifiers for the target, event types to receive, and a cursor ID for replay upon reconnection.*


### UnsubscribeFrame (class, L166-L170)

> *Summary: Represents a message sent from a client to the hub to terminate an existing subscription. It requires a `subscription_id` string as input to identify which subscription should be closed.*


### EventFrame (class, L174-L179)

> *Summary: Represents a message frame used for delivering subscriptions from a hub to a client. It contains the `subscription_id` and an associated `Envelope`.*


### encode_frame (function, L214-L223)

> *Summary: Converts a `Frame` object into a serializable dictionary format suitable for JSON transmission. It achieves this by using `dataclasses.asdict` on the frame and explicitly adding the frame's type discriminator (`kind`).*


### decode_frame (function, L226-L240)

> *Summary: This function reconstructs a structured `Frame` object from a dictionary representation. It uses the `"kind"` field to select the correct class, optionally rehydrates a nested `Envelope`, and returns an instance of that frame type or raises an error if the kind is unknown.*

