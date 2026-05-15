# autogen/beta/network/errors.py

6 class(es): NetworkError, NotFoundError, AccessDeniedError, AuthError, ProtocolError, InboxFull.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NetworkError | class |  |
| NotFoundError | class |  |
| AccessDeniedError | class |  |
| AuthError | class |  |
| ProtocolError | class |  |
| InboxFull | class |  |

## Chunks

### NetworkError (class, L21-L22)

> *Summary: Serves as the base exception for all network-related errors within the `autogen.beta.network` module. It inherits from Python's standard `Exception` class to signal network failures.*


### NotFoundError (class, L25-L26)

> *Summary: Represents an error when attempting to find a registered identity, channel, or task within the network. It inherits from `NetworkError` and signals that the requested resource could not be located.*


### AccessDeniedError (class, L29-L30)

> *Summary: Represents an error when a sender's access rules prohibit the requested network operation, inheriting from `NetworkError`. This class signals permission denial during communication attempts.*


### AuthError (class, L33-L34)

> *Summary: Represents a specific network error indicating that authentication failed during the transport handshake process. It inherits from `NetworkError` to signal connection issues related to credentials.*


### ProtocolError (class, L37-L43)

> *Summary: Indicates that an incoming message violated the expected communication protocol contract of a channel adapter. This error is raised during send validation and results in the hub returning a structured error frame without logging the problematic data.*


### InboxFull (class, L46-L47)

> *Summary: Represents a network error indicating that the recipient's inbox has reached its storage limit, causing messages to be rejected. This class inherits from `NetworkError` for consistent error handling.*

