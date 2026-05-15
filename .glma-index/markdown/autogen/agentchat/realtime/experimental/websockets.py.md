# autogen/agentchat/realtime/experimental/websockets.py

1 class(es): WebSocketProtocol. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WebSocketProtocol | class |  |

## Chunks

### WebSocketProtocol (class, L12-L21)

> *Summary: Defines an asynchronous protocol for handling WebSocket communication, enabling the sending of arbitrary JSON data and receiving either structured JSON or raw text strings. It also provides an iterator to stream incoming text messages asynchronously.*


### send_json (method, L15-L15, parent: WebSocketProtocol)

> *Summary: This method asynchronously sends structured data over a WebSocket connection. It accepts arbitrary data and an optional mode string to control the transmission format.*


### receive_json (method, L17-L17, parent: WebSocketProtocol)

> *Summary: This asynchronous method reads incoming data from a WebSocket connection and parses it as JSON, defaulting to text mode if not specified. It returns the deserialized content of the received message.*


### receive_text (method, L19-L19, parent: WebSocketProtocol)

> *Summary: This asynchronous method retrieves a text message from the WebSocket connection. It is expected to return the received string data.*


### iter_text (method, L21-L21, parent: WebSocketProtocol)

> *Summary: Yields an asynchronous iterator of strings, providing real-time text chunks from the agent's output stream. This method is designed to stream content incrementally as it becomes available.*

