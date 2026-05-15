# autogen/agentchat/remote/agent_service.py

3 class(es): AgentService, HITLStream, AsyncIOQueueStream. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AgentService | class |  |
| HITLStream | class |  |
| AsyncIOQueueStream | class |  |

## Chunks

### AgentService (class, L25-L206)

> *Summary: This service acts as an asynchronous interface for an agent, processing incoming requests by first checking input guardrails. It iteratively runs the agent to generate responses, handling LLM streaming, local tool execution, and user interaction prompts until a termination condition is met or a client tool call is initiated.*


### __init__ (method, L26-L28, parent: AgentService)

> *Summary: Initializes the service by storing a reference to the provided `ConversableAgent` and capturing its name for identification. This sets up the necessary context for remote communication with the specified agent instance.*


### __call__ (method, L30-L109, parent: AgentService)

> *Summary: This method processes a request message by first checking for input guardrail violations; otherwise, it iteratively runs an agent loop that checks for human intervention, generates LLM responses (streaming them if applicable), executes local tools based on the agent's output, and yields appropriate responses back to the client until termination or tool execution is complete. It takes a `RequestMessage` as input and yields `ServiceResponse` objects containing messages, streaming text, or prompts for user input.*


### _add_message_to_local_history (method, L111-L125, parent: AgentService)

> *Summary: This method processes an incoming message by first checking it against agent guardrails; if a guardrail triggers, it returns the sanitized output and halts processing. Otherwise, it validates and normalizes the message into an OpenAI format before returning success along with the processed message.*


### _streaming_oai_reply (method, L127-L157, parent: AgentService)

> *Summary: This asynchronous method streams responses from an LLM by yielding incremental text chunks or intermediate events while the generation task is running. Upon completion, it yields a final tuple indicating success and containing the complete reply object.*


### _make_tool_executor (method, L159-L165, parent: AgentService)

> *Summary: Constructs a `GroupToolExecutor` by iterating over the agent's available tools and registering them for execution within the executor. It uses provided context variables to create copies of each tool before adding it to the group.*


### _try_execute_local_tool (method, L167-L206, parent: AgentService)

> *Summary: Executes local tools based on incoming messages by utilizing a provided executor. It processes the results to return the tool output, any updated context variables, and a boolean indicating if user interaction is required next.*


### HITLStream (class, L209-L232)

> *Summary: This class manages a human-in-the-loop interaction stream, tracking whether user input is required via the `is_input_required` property. It accepts an input prompt asynchronously and prevents sending certain control or termination events while raising an error for other message types.*


### __init__ (method, L210-L211, parent: HITLStream)

> *Summary: Initializes the service instance by setting an empty string for `input_prompt`. This attribute will subsequently hold user or system prompts for agent interactions.*


### is_input_required (method, L214-L215, parent: HITLStream)

> *Summary: Checks if the agent requires user input by evaluating the truthiness of its `input_prompt` attribute, returning a boolean indicating necessity.*


### input (method, L217-L219, parent: HITLStream)

> *Summary: This method accepts an optional string prompt and a boolean flag to set the agent's input state. It stores the provided prompt internally and immediately returns an empty string.*


### send (method, L221-L232, parent: HITLStream)

> *Summary: This method checks if the incoming `BaseEvent` is one of several specific termination or auto-reply events; otherwise, it raises an error indicating that message sending is unsupported by the current implementation.*


### AsyncIOQueueStream (class, L235-L241)

> *Summary: This class implements an asynchronous stream protocol by managing a thread-safe `asyncio.Queue` for incoming data. It accepts messages and immediately enqueues the string content if the message is of type `StreamEvent`.*


### __init__ (method, L236-L237, parent: AsyncIOQueueStream)

> *Summary: Initializes the service by creating an asynchronous queue to manage incoming string messages for communication between agents. This queue serves as the primary input buffer for the agent's operations.*


### send (method, L239-L241, parent: AsyncIOQueueStream)

> *Summary: If the incoming event is a stream event, it immediately queues the content payload for asynchronous processing. This method handles streaming data by placing its contents directly into an internal queue without blocking.*

