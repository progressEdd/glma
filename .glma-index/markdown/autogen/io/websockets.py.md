# autogen/io/websockets.py

3 class(es): ServerConnection, WebSocketServer, IOWebsockets. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ServerConnection | class |  |
| WebSocketServer | class |  |
| IOWebsockets | class |  |

## Chunks

### ServerConnection (class, L37-L61)

> *Summary: Defines a protocol for managing bidirectional communication over a WebSocket connection. It provides methods to send data (either a single item or an iterable of items), receive incoming data with an optional timeout, and gracefully close the connection.*


### send (method, L38-L45, parent: ServerConnection)

> *Summary: Transmits data to the connected client, accepting either a single `Data` object or an iterable sequence of `Data` objects as input. It performs the necessary network operation to push the specified message(s) out over the established WebSocket connection.*


### recv (method, L47-L57, parent: ServerConnection)

> *Summary: Retrieves a data message from the connected client, optionally respecting a specified timeout duration. It returns the received `Data` object upon successful reception.*


### close (method, L59-L61, parent: ServerConnection)

> *Summary: This method terminates the current WebSocket connection. It takes no arguments and performs an action to cleanly shut down the established link.*


### WebSocketServer (class, L64-L79)

> *Summary: Provides an interface for managing a WebSocket server lifecycle. It allows developers to start the server indefinitely via `serve_forever()`, gracefully stop it using `shutdown()`, and manage its setup/teardown with context managers (`__enter__`/`__exit__`).*


### serve_forever (method, L65-L67, parent: WebSocketServer)

> *Summary: This method initiates an indefinite loop to keep a WebSocket server running. It has no explicit inputs but continuously serves incoming connections until manually stopped.*


### shutdown (method, L69-L71, parent: WebSocketServer)

> *Summary: This method initiates a graceful shutdown of the WebSocket server instance. It performs necessary cleanup operations to stop the running server process.*


### __enter__ (method, L73-L75, parent: WebSocketServer)

> *Summary: When entering the context, this method initializes and returns the `WebSocketServer` instance. It manages the setup required for using the WebSocket server within a `with` statement block.*


### __exit__ (method, L77-L79, parent: WebSocketServer)

> *Summary: When exiting a WebSocket server context, this method handles cleanup operations. It accepts exception details (`exc_type`, `exc_value`, `traceback`) to manage graceful shutdown if errors occurred during operation.*


### IOWebsockets (class, L84-L214)

> *Summary: This class implements a websocket I/O stream wrapper around a `ServerConnection`. It provides methods to send structured messages (`send`) and receive text input (`input`), while the static method `run_server_in_thread` launches the server in a background thread, yielding the connection URI upon successful startup.*


### __init__ (method, L87-L93, parent: IOWebsockets)

> *Summary: Initializes an I/O stream by storing a reference to a provided `ServerConnection` object. This sets up the necessary connection for subsequent WebSocket operations.*


### _handler (method, L96-L109, parent: IOWebsockets)

> *Summary: This method processes an incoming websocket connection by instantiating an `IOWebsockets` object for it and setting it as the default stream handler. It then executes a provided callback function, passing the new instance to it, while handling potential exceptions during setup or execution.*


### run_server_in_thread (method, L113-L171, parent: IOWebsockets)

> *Summary: This function launches a WebSocket server in a background thread, accepting configuration like host, port, and an `on_connect` callback. It yields the server's URI once it is successfully started and ensures graceful shutdown of the server and thread upon exiting.*


### websocket (method, L174-L176, parent: IOWebsockets)

> *Summary: Returns the configured WebSocket server URI from the instance's internal state. This method provides access to the connection endpoint for WebSocket communication.*


### print (method, L178-L188, parent: IOWebsockets)

> *Summary: This method serializes provided objects into a `PrintEvent` and sends it through the connection's send mechanism. It allows customization of object separation, ending characters, and output flushing behavior.*


### send (method, L190-L196, parent: IOWebsockets)

> *Summary: Transmits a structured event object by serializing it to JSON and sending it through the underlying WebSocket connection. It takes one `BaseEvent` instance as input and performs no return value.*


### input (method, L198-L214, parent: IOWebsockets)

> *Summary: Reads a line of data from the connected WebSocket stream after optionally sending a specified prompt to the remote end. It returns the received message decoded as a UTF-8 string or as is if it's not bytes.*

