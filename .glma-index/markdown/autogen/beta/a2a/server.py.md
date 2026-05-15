# autogen/beta/a2a/server.py

1 class(es): A2AServer. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2AServer | class |  |

## Chunks

### A2AServer (class, L36-L207)

> *Summary: This class encapsulates an agent and its associated state (stores, executors, modifiers) to serve it as a standardized A2A endpoint. It provides builder methods (`build_jsonrpc`, `build_rest`, `build_grpc`) that take transport-specific parameters like URLs and return ready-to-serve ASGI or gRPC server objects.*


### __init__ (method, L67-L91, parent: A2AServer)

> *Summary: Initializes the server by storing an `Agent` and optional components like card modifiers, notification services, and executors. It ensures a shared in-memory task store is used unless one is explicitly provided for multi-transport setups.*


### agent (method, L94-L95, parent: A2AServer)

> *Summary: Returns the internal `Agent` instance held by the object. This method provides direct access to the configured agent component.*


### extended_card (method, L98-L99, parent: A2AServer)

> *Summary: Returns the internal `_extended_card` attribute, which is of type `AgentCard` or `None`. This method provides read access to an extended card object associated with the instance.*


### task_store (method, L102-L104, parent: A2AServer)

> *Summary: Provides access to the centralized `TaskStore` instance, which is shared among all transport builder components. This method returns the internal reference to that shared state object.*


### _shared_kwargs (method, L106-L121, parent: A2AServer)

> *Summary: Constructs a dictionary containing shared dependencies like executors and stores for various build methods. It conditionally includes the `card_modifier` based on the provided boolean flag.*


### build_jsonrpc (method, L123-L145, parent: A2AServer)

> *Summary: Creates and returns a Starlette ASGI application that exposes JSON-RPC endpoints alongside an agent card. It constructs the necessary card using provided or internally generated data based on the input URL and configuration.*


### build_rest (method, L147-L174, parent: A2AServer)

> *Summary: Creates a Starlette ASGI application that exposes REST endpoints and an agent card interface. It accepts a base URL and optional path prefixes to mount the API routes under a specific sub-path.*


### build_grpc (method, L176-L207, parent: A2AServer)

> *Summary: Constructs and returns a gRPC server instance configured to listen on a specified address (`bind`) and advertise itself via a public URL (`grpc_url`). It resolves or uses an existing `AgentCard` to define the service's identity before initializing the underlying gRPC server.*

