# test/beta/a2a/_helpers.py

6 function(s): _materialize, make_pair, make_executor_pair, make_recording_pair, make_rest_pair, start_grpc_pair. 9 class(es): A2APair, ExecutorPair, RecordingPair, GrpcPair, StatelessScript, StatelessScriptClient, PromptThenAckExecutor, RecordingConfig, RecordingClient. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2APair | class |  |
| ExecutorPair | class |  |
| RecordingPair | class |  |
| GrpcPair | class |  |
| StatelessScript | class |  |
| StatelessScriptClient | class |  |
| _materialize | function |  |
| PromptThenAckExecutor | class |  |
| make_pair | function |  |
| make_executor_pair | function |  |
| RecordingConfig | class |  |
| RecordingClient | class |  |
| make_recording_pair | function |  |
| make_rest_pair | function |  |
| start_grpc_pair | function |  |

## Chunks

### A2APair (class, L43-L47)

> *Summary: This class aggregates the necessary components for an asynchronous pair interaction, holding references to a server instance, two agents (one acting as a client and one potentially related to the server), and tracking configuration. It serves as a container structure for managing the state of a peer-to-peer connection setup.*


### ExecutorPair (class, L51-L54)

> *Summary: This class aggregates a server instance, an agent executor base, and an agent object. It serves as a container to hold the necessary components for executing cross-agent interactions.*


### RecordingPair (class, L58-L62)

> *Summary: This class aggregates the necessary components for an end-to-end test scenario, holding references to a server instance, two agents (one acting as a client and one potentially related to the server), and the configuration defining the recording parameters. It serves as a container structure for managing all elements involved in capturing interaction data.*


### GrpcPair (class, L66-L72)

> *Summary: This class aggregates necessary components for gRPC communication, holding references to the server and client agents, tracking configuration, a target URL string, and the active asynchronous gRPC server instance. It serves as a container to manage all related entities required for an A2A service interaction.*


### StatelessScript (class, L79-L95)

> *Summary: This configuration object holds the initial input and optional post-tool response for a stateless script execution. It provides methods to clone itself or instantiate a corresponding client based on its stored parameters.*


### __init__ (method, L80-L86, parent: StatelessScript)

> *Summary: Initializes an object by storing a primary input (`initial`), which can be various response or event types, and an optional secondary input (`after_tool`). This sets up the state for subsequent processing based on these provided values.*


### copy (method, L88-L89, parent: StatelessScript)

> *Summary: Returns a reference to the current instance, effectively creating a shallow copy of the object. This method allows for immutable-like behavior by returning `self` instead of a new object.*


### create (method, L91-L92, parent: StatelessScript)

> *Summary: Instantiates and returns a `StatelessScriptClient` object using the instance's initial state and after-tool configuration. This method serves to construct a new client based on existing setup parameters.*


### create_files_client (method, L94-L95, parent: StatelessScript)

> *Summary: This method is intended to instantiate a client responsible for file operations, but currently raises `NotImplementedError` as its implementation is missing. It takes no arguments and returns nothing.*


### StatelessScriptClient (class, L98-L120)

> *Summary: This client processes a sequence of events to determine the final response. It selects an initial or post-tool message based on whether a `ToolResultEvent` exists in the input messages and then materializes that chosen content into a `ModelResponse`.*


### __init__ (method, L99-L105, parent: StatelessScriptClient)

> *Summary: Initializes an object by storing a primary input, which can be various response or event types, and an optional secondary input representing the state after tool execution. These inputs are stored internally for later use within the instance.*


### __call__ (method, L107-L120, parent: StatelessScriptClient)

> *Summary: Determines the response by selecting a pre-defined message template—either based on the most recent tool result or an initial default—and then materializes that choice using the provided context. It accepts a sequence of events and a context object to produce a `ModelResponse`.*


### _materialize (function, L123-L134)

> *Summary: Converts various input types into a standardized `ModelResponse` object. It handles direct returns, strings (by sending them as messages), `ToolCallEvent`s, and iterables containing tool calls.*


### PromptThenAckExecutor (class, L137-L175)

> *Summary: This executor manages a two-step interaction flow based on an initial prompt. If no current task exists, it submits a new task and requests user input using the stored prompt; otherwise, it processes incoming text from the request context and completes the existing task with an echo response.*


### __init__ (method, L138-L140, parent: PromptThenAckExecutor)

> *Summary: Initializes an object by storing a required string prompt and setting the user text to `None`. This sets up the state for processing subsequent user input.*


### execute (method, L142-L168, parent: PromptThenAckExecutor)

> *Summary: This method processes an incoming message from a request context, generating unique IDs if they are missing. It either initiates a new task by submitting it and requesting input, or completes the current task by echoing the received user text back to the agent.*


### cancel (method, L170-L175, parent: PromptThenAckExecutor)

> *Summary: This method cancels the current asynchronous task by obtaining a reference to it from the request context and then invoking a cancellation routine via a `TaskUpdater` using the provided event queue. It safely exits if no active task is present in the context.*


### make_pair (function, L178-L212)

> *Summary: This function constructs a complete two-way communication pair by initializing and configuring both a server agent and a client agent. It takes initial data and tool definitions for both sides to set up the necessary agents, servers, and clients for testing interactions.*


### make_executor_pair (function, L215-L244)

> *Summary: This function constructs a complete testing environment by pairing an existing agent executor with newly instantiated server and client agents. It configures the server using optional task or push configuration stores, while the client is set up to communicate with the server via a provided URL and streaming setting.*


### RecordingConfig (class, L251-L263)

> *Summary: This configuration object holds a response string and a list of events for recording purposes. It provides methods to clone itself and instantiate a `RecordingClient` using its stored data.*


### __init__ (method, L252-L254, parent: RecordingConfig)

> *Summary: Initializes an object by storing a string response and setting up an empty list to track event calls. This structure is used to manage the state of a test or interaction involving responses and events.*


### copy (method, L256-L257, parent: RecordingConfig)

> *Summary: Returns a reference to the current instance, effectively creating a shallow copy of the object. This method allows for chaining operations on the object without modification.*


### create (method, L259-L260, parent: RecordingConfig)

> *Summary: Instantiates and returns a `RecordingClient` object using the current instance's response data and call history. This method is responsible for finalizing the client setup based on collected interaction details.*


### create_files_client (method, L262-L263, parent: RecordingConfig)

> *Summary: This method is intended to initialize a client for file operations but currently raises `NotImplementedError`, indicating it requires further implementation. It takes no arguments and returns nothing.*


### RecordingClient (class, L266-L280)

> *Summary: This client wraps a predefined response and call history, allowing it to act as an LLM interface. When invoked with messages and context, it logs the input messages into its internal call list and sends a message containing the stored response via the provided context.*


### __init__ (method, L267-L269, parent: RecordingClient)

> *Summary: Initializes an object by storing a string response and a list of event call records. These inputs are stored internally for later use within the instance.*


### __call__ (method, L271-L280, parent: RecordingClient)

> *Summary: This method processes a sequence of incoming `BaseEvent` messages and sends a corresponding response message via the provided `Context`. It records the received messages internally before returning a `ModelResponse` containing the sent message.*


### make_recording_pair (function, L283-L298)

> *Summary: This function constructs a complete pair of agents—a server and a client—for testing A2A interactions. It takes an initial response string and optional configuration parameters to set up the necessary communication infrastructure for recording tests.*


### make_rest_pair (function, L301-L322)

> *Summary: This function constructs a complete pair of interacting agents—a server and a client—for testing asynchronous communication. It takes an initial message or event, optional subsequent data, and configuration parameters to set up the necessary HTTP clients and tracking mechanisms.*


### start_grpc_pair (function, L325-L357)

> *Summary: This function initializes and starts a bidirectional gRPC communication pair between two agents. It takes an initial message or event as input and returns a `GrpcPair` object containing the running server, client agent, and necessary configuration details for interaction.*

