# autogen/beta/a2a/executor.py

1 class(es): AgentExecutor. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AgentExecutor | class |  |

## Chunks

### AgentExecutor (class, L42-L334)

> *Summary: This class manages the stateless execution of an AI agent by processing incoming requests as self-contained turns. It ingests conversation history and tool schemas from a message, rebuilds the necessary context, dispatches the request to the underlying agent logic, and streams resulting events back through an event queue. The primary behavior is ensuring each `execute` call is independent, relying on the client to provide full state on every invocation.*


### __init__ (method, L72-L73, parent: AgentExecutor)

> *Summary: Initializes the executor by storing a reference to an input `Agent` object. This sets up the necessary context for subsequent execution logic.*


### execute (method, L75-L194, parent: AgentExecutor)

> *Summary: Processes an incoming request by parsing the message and initializing a task updater with unique IDs for tracking. It then streams events from the execution lifecycle—including model chunks and tool calls—into an event queue, managing state transitions and handling potential exceptions to report final task status.*


### cancel (method, L196-L207, parent: AgentExecutor)

> *Summary: When called during a cancellation event, this method publishes a `CANCELED` status update for the associated task using provided request and event queues. It relies on the framework to have already cancelled the running execution task before invoking this hook.*


### _run_one_turn (method, L209-L265, parent: AgentExecutor)

> *Summary: Executes a single turn of agent interaction by dispatching an initial event to the agent using provided tools and context updates. It either signals that input is required if tool calls are pending or completes the task with the final response message, ensuring streamed content isn't duplicated.*


### _build_final_message (method, L268-L279, parent: AgentExecutor)

> *Summary: Constructs the final message payload for an agent update by combining provided text and variables. It returns `None` if both text and variables are empty, otherwise it packages the content into a structured message via the updater object.*


### _build_initial_event (method, L282-L291, parent: AgentExecutor)

> *Summary: Constructs the starting event based on a parsed message, returning a `ToolResultsEvent` if tool results are present, or a `ModelRequest` containing user inputs otherwise. This determines whether the next step is to process tool outcomes or send a new model request.*


### _make_client_tool (method, L294-L301, parent: AgentExecutor)

> *Summary: Constructs a `ClientTool` object from a provided `FunctionToolSchema`. It packages the function's name, description, and parameters into the tool definition for client use.*


### _dispatch_to_agent (method, L303-L334, parent: AgentExecutor)

> *Summary: This method orchestrates the execution of an agent by initializing a conversation context with provided variables and system prompts. It then calls the agent's internal execution logic using a client to process an initial event and returns the resulting model response along with the updated state variables.*

