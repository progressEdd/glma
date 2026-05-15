# autogen/agents/experimental/a2ui/a2a_executor.py

1 class(es): A2UIAgentExecutor. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2UIAgentExecutor | class |  |

## Chunks

### A2UIAgentExecutor (class, L56-L312)

> *Summary: This executor processes agent interactions by parsing incoming messages for A2UI actions or streaming the agent's response. It can either execute tool-based actions directly or route LLM-driven actions back to the agent, ultimately formatting the final output as plain text or a combination of text and structured `DataPart`s if A2UI content is present.*


### __init__ (method, L67-L75, parent: A2UIAgentExecutor)

> *Summary: Initializes the executor by storing a reference to a `ConversableAgent`, creating an associated `AgentService`, and setting up a response parser using provided delimiters and versioning. This setup prepares the component to interact with and process responses from the specified agent.*


### _extract_incoming_action (method, L77-L100, parent: A2UIAgentExecutor)

> *Summary: Parses an incoming `RequestContext` to extract a structured action dictionary from message parts. It supports two formats: A2UI MIME-typed messages wrapped in a list, or a direct genui v0.9 style DataPart containing the action. Returns the extracted action dictionary or `None` if no matching action is found.*


### _handle_action (method, L102-L181, parent: A2UIAgentExecutor)

> *Summary: This method processes an incoming A2UI action dictionary, determining if it's a tool call or an LLM instruction. If it's a tool action, it executes the corresponding function using provided context and reports the result; otherwise, it constructs a prompt from the action details and modifies the current message context to route the request to the main agent logic.*


### _setup_task (method, L183-L203, parent: A2UIAgentExecutor)

> *Summary: This method initializes or retrieves a `Task` based on the incoming request context and event queue. It either creates a new task with submitted status if none exists, or converts the existing one, then returns both the task object and an associated updater to manage its lifecycle.*


### _stream_agent_response (method, L205-L247, parent: A2UIAgentExecutor)

> *Summary: This asynchronous method streams an agent's response by iterating over chunks from the underlying service. It updates a task's status with each text chunk and returns the complete text along with a boolean indicating if streaming occurred, exiting early if the agent requires user input.*


### _build_final_parts (method, L249-L271, parent: A2UIAgentExecutor)

> *Summary: This method processes a complete response string to construct a list of structured artifact parts. It conditionally returns either a single text part or a combination of text and data parts if A2UI content is successfully parsed from the input.*


### execute (method, L273-L309, parent: A2UIAgentExecutor)

> *Summary: This method processes a request by first checking for and activating an A2UI extension, then handling any incoming A2UI actions if present. It subsequently streams the agent's response and finally sends the complete result back via a status update to the core system.*


### cancel (method, L311-L312, parent: A2UIAgentExecutor)

> *Summary: This asynchronous method accepts a request context and an event queue to signal cancellation. It currently does nothing (`pass`), indicating it's a placeholder for stopping ongoing operations.*

