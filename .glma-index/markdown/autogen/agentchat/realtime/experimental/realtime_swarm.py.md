# autogen/agentchat/realtime/experimental/realtime_swarm.py

4 function(s): message_to_dict, parse_oai_message, _create_swarmable_agent, register_swarm. 2 class(es): SwarmableAgent, SwarmableRealtimeAgent. 34 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| message_to_dict | function |  |
| parse_oai_message | function |  |
| SwarmableAgent | class |  |
| _create_swarmable_agent | function |  |
| SwarmableRealtimeAgent | class |  |
| register_swarm | function |  |

## Chunks

### message_to_dict (function, L51-L57)

> *Summary: Converts an input that can be a string or dictionary into a standardized dictionary format. If the input is a string, it wraps it in a `{"content": ...}` structure; otherwise, it returns the input as-is or converts it to a dictionary if necessary.*


### parse_oai_message (function, L60-L109)

> *Summary: Converts an input message, along with its role and intended recipient agent, into a standardized dictionary matching OpenAI's message format. It validates required fields like content or function/tool calls, sets the appropriate role based on message type, and ensures necessary metadata is present before returning the structured output.*


### SwarmableAgent (class, L112-L351)

> *Summary: This class manages agent interactions within a swarm chat environment, maintaining message history for multiple participants. It allows agents to send and receive messages, process input/output guardrails, and initiate structured chats that generate summaries from conversation logs.*


### __init__ (method, L115-L142, parent: SwarmableAgent)

> *Summary: Initializes a swarm agent with configuration parameters like a name, system message, and termination condition. It sets up internal state management for messages, guardrails, and client caching to control its behavior during interactions.*


### system_message (method, L145-L146, parent: SwarmableAgent)

> *Summary: Retrieves the predefined system prompt string stored internally within the agent instance. This method provides the core instructions that guide the agent's behavior during interactions.*


### update_system_message (method, L148-L154, parent: SwarmableAgent)

> *Summary: Sets the internal system prompt for an agent using a provided string input, updating its configuration for subsequent inferences.*


### name (method, L157-L158, parent: SwarmableAgent)

> *Summary: Returns the internal name attribute of the agent instance as a string. This method provides a way to identify the specific agent object.*


### description (method, L161-L162, parent: SwarmableAgent)

> *Summary: Returns the internal string representation of the swarm agent, which describes its purpose or state. This method takes no inputs and outputs a single string.*


### register_input_guardrail (method, L164-L165, parent: SwarmableAgent)

> *Summary: Adds a specified `Guardrail` object to the agent's list of input validation checks. This method accepts one `Guardrail` instance and modifies the internal state by appending it to `self.input_guardrails`.*


### register_input_guardrails (method, L167-L168, parent: SwarmableAgent)

> *Summary: Appends a list of `Guardrail` objects to the instance's internal collection of input guards. This method configures the system with specific validation rules for incoming data.*


### register_output_guardrail (method, L170-L171, parent: SwarmableAgent)

> *Summary: Adds a specified `Guardrail` object to the agent's list of output validation checks. This method accepts one `Guardrail` input and modifies the internal state by appending it to `self.output_guardrails`.*


### register_output_guardrails (method, L173-L174, parent: SwarmableAgent)

> *Summary: Appends a list of `Guardrail` objects to the instance's existing collection of output guards. This method configures runtime safety checks for generated outputs.*


### run_input_guardrails (method, L176-L181, parent: SwarmableAgent)

> *Summary: Iterates through configured input guardrails, checking each against the provided list of messages. It immediately returns the result of the first activated guardrail or `None` if no guardrails are triggered.*


### run_output_guardrails (method, L183-L188, parent: SwarmableAgent)

> *Summary: Iterates through configured output guardrails, checking the provided reply (string or dictionary) against each one. It immediately returns the first `GuardrailResult` if any guardrail is activated; otherwise, it returns `None`.*


### send (method, L190-L198, parent: SwarmableAgent)

> *Summary: Appends a parsed message to the internal message history for a specific agent and then forwards the original message to that agent's receive method. This allows one agent to communicate with another within the swarm structure.*


### receive (method, L200-L212, parent: SwarmableAgent)

> *Summary: This method processes an incoming message from a specific agent by logging it to the internal chat history. If configured to respond and no explicit silence flag is set, it generates and sends a reply back to the sender.*


### generate_reply (method, L214-L226, parent: SwarmableAgent)

> *Summary: Retrieves a response by first ensuring the input messages are available, either from provided arguments or cached agent history. It then checks for termination conditions and human replies before returning the resulting message content.*


### check_termination_and_human_reply (method, L228-L234, parent: SwarmableAgent)

> *Summary: This method is intended to determine if the conversation should end or if a human response is required. It accepts message history, an agent instance, and configuration settings as input, returning a boolean indicating termination status and an optional string for human feedback.*


### initiate_chat (method, L236-L268, parent: SwarmableAgent)

> *Summary: This method starts a new conversation by preparing the sender and recipient agents, sending an initial message, and generating a summary of the last exchange. It returns a `ChatResult` object containing the unique chat ID, history, summary, and usage cost.*


### a_generate_reply (method, L270-L275, parent: SwarmableAgent)

> *Summary: This method acts as a simple wrapper that delegates the actual reply generation to an internal `generate_reply` function. It accepts optional message history and a sender agent to produce either a string response or a dictionary object.*


### a_receive (method, L277-L283, parent: SwarmableAgent)

> *Summary: This method accepts a message (dict or string), the sending agent, and an optional reply flag to pass to its internal `receive` handler. It acts as a wrapper to delegate incoming communication to the object's core receiving logic.*


### a_send (method, L285-L291, parent: SwarmableAgent)

> *Summary: This method forwards a message, which can be a dictionary or string, to a specified agent. It delegates the actual sending operation to an internal `send` method while optionally controlling whether a reply is expected.*


### chat_messages (method, L294-L296, parent: SwarmableAgent)

> *Summary: Retrieves a mapping where each `Agent` is associated with a list of its corresponding message dictionaries. This method returns the internal storage containing all recorded conversation history.*


### last_message (method, L298-L311, parent: SwarmableAgent)

> *Summary: Retrieves the most recent message from a chat history, either across all conversations or specifically for a given agent. It returns `None` if no messages exist, raises an error if multiple conversations are present without specifying an agent, or throws a `KeyError` if the specified agent has no recorded history.*


### _prepare_chat (method, L313-L324, parent: SwarmableAgent)

> *Summary: This method configures the chat state for a specific recipient by setting a `reply_at_receive` flag. It optionally clears the existing message history and recursively calls preparation on the recipient agent itself.*


### _raise_exception_on_async_reply_functions (method, L326-L327, parent: SwarmableAgent)

> *Summary: This method serves as a placeholder to enforce that any asynchronous reply functions must explicitly raise an exception if they are called. It currently does nothing, indicating it's likely part of a larger framework check.*


### set_ui_tools (method, L329-L331, parent: SwarmableAgent)

> *Summary: This method configures the available user interface tools for an agent. It accepts an optional list of tools to be assigned to the agent's interface.*


### unset_ui_tools (method, L333-L335, parent: SwarmableAgent)

> *Summary: This method removes any currently configured user interface tools from the agent. It takes no inputs and produces no output.*


### _last_msg_as_summary (method, L338-L351, parent: SwarmableAgent)

> *Summary: Extracts a chat summary by retrieving and processing the content of the recipient's most recent message from the sender. It handles both string and list-based message contents, stripping "TERMINATE" markers, and returns an empty string upon failure.*


### _create_swarmable_agent (function, L357-L370)

> *Summary: This helper function instantiates and returns a `SwarmableAgent` object. It configures the agent using provided parameters such as its name, system prompt, termination condition, description, and silence setting.*


### SwarmableRealtimeAgent (class, L373-L508)

> *Summary: Manages a real-time swarm interaction by coordinating multiple agents and an external realtime agent. It accepts initial agents and a question message, allowing it to asynchronously poll for answers via the realtime client or repeatedly ask the user until a timeout is reached. The core behavior involves setting up tool registration on the realtime agent based on all participating agents' capabilities.*


### __init__ (method, L374-L396, parent: SwarmableRealtimeAgent)

> *Summary: Initializes a swarm manager by storing references to the primary realtime agent, an initial conversational agent, and a list of other agents. It sets up internal state for managing responses, including a question message and an event flag for signaling answers.*


### reset_answer (method, L398-L400, parent: SwarmableRealtimeAgent)

> *Summary: Resets an internal `anyio.Event` used to signal when an answer is available, effectively clearing any previous state for answer notification.*


### set_answer (method, L402-L406, parent: SwarmableRealtimeAgent)

> *Summary: This method updates an internal answer string and signals a change via an event object. It accepts a string as input and returns a confirmation message upon successful update.*


### get_answer (method, L408-L411, parent: SwarmableRealtimeAgent)

> *Summary: Waits for an internal answer event signal and then returns the stored response string. This method is used to retrieve the final computed answer after asynchronous processing completes.*


### ask_question (method, L413-L433, parent: SwarmableRealtimeAgent)

> *Summary: This method prompts the user with a given question and waits for a response using an internal event mechanism. If no answer is received within the specified timeout period, it repeatedly resends the same question to the user.*


### check_termination_and_human_reply (method, L435-L463, parent: SwarmableRealtimeAgent)

> *Summary: This method determines if a conversation should end and prepares an agent reply after checking the message history. It asynchronously prompts for user input using `ask_question` before returning `True` along with a predefined user response containing stored content.*


### start_chat (method, L465-L466, parent: SwarmableRealtimeAgent)

> *Summary: This method is intended to initiate a chat session but currently raises a `NotImplementedError`, indicating it requires specific implementation in subclasses. It takes no inputs and returns nothing.*


### configure_realtime_agent (method, L468-L508, parent: SwarmableRealtimeAgent)

> *Summary: Sets up a real-time agent by configuring its system message and registering available tools from all associated agents as callable functions. It also schedules an asynchronous chat initiation to begin once the observers are ready.*


### register_swarm (function, L512-L533)

> *Summary: This function constructs a `SwarmableRealtimeAgent` by combining a base `RealtimeAgent`, an initial agent, and a list of other agents. It configures the resulting swarm agent with optional system and question messages provided as input.*

