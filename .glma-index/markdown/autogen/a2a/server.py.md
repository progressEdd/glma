# autogen/a2a/server.py

2 class(es): CardSettings, A2aAgentServer. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CardSettings | class |  |
| A2aAgentServer | class |  |

## Chunks

### CardSettings (class, L36-L82)

> *Summary: This class extends `AgentCard` to define configuration for an agent by holding optional metadata like name, description, and URL, alongside fixed properties such as versioning, default input/output modes, supported capabilities, and a list of defined skills. It serves as the structured data container for describing an agent's operational parameters.*


### A2aAgentServer (class, L86-L300)

> *Summary: Wraps an `ConversableAgent` to expose it as an A2A server via HTTP. It accepts the agent, configuration settings for its card (and extended card), and optional modifiers/middlewares. The primary output is a configured Starlette application instance ready to handle A2A requests or a specialized request handler.*


### __init__ (method, L93-L184, parent: A2aAgentServer)

> *Summary: Initializes a server instance to expose an `ConversableAgent`, configuring its base and optional extended agent cards using provided settings and modifiers. It validates URL conflicts and conditionally adds A2UI extensions if the served agent is an `A2UIAgent`.*


### add_middleware (method, L186-L188, parent: A2aAgentServer)

> *Summary: Registers an HTTP middleware instance and its associated keyword arguments into the server's list of middlewares. This allows the server to process incoming requests through the specified middleware chain.*


### executor (method, L191-L209, parent: A2aAgentServer)

> *Summary: This method conditionally returns a specialized `A2UIAgentExecutor` if the internal agent is an `A2UIAgent`, ensuring A2UI data preservation and extension negotiation; otherwise, it defaults to returning a standard `AutogenAgentExecutor`.*


### build_request_handler (method, L211-L255, parent: A2aAgentServer)

> *Summary: Constructs and returns a configured `RequestHandler` instance by assembling various dependencies like task stores, queue managers, and notification services. It bridges older synchronous card modifiers to the required asynchronous signature if one is provided.*


### build_starlette_app (method, L257-L298, parent: A2aAgentServer)

> *Summary: Constructs a Starlette ASGI application by combining routes for agent cards and JSON-RPC endpoints. It accepts optional request and context builders to configure the resulting application instance with necessary middleware.*

