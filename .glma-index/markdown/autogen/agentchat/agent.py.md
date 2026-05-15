# autogen/agentchat/agent.py

1 function(s): _check_protocol_implementation. 2 class(es): Agent, LLMAgent. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Agent | class |  |
| LLMAgent | class |  |
| _check_protocol_implementation | function |  |

## Chunks

### Agent (class, L22-L153)

> *Summary: Defines a contract for an entity capable of communication and action within a multi-agent system. It requires methods to send/receive messages (sync/async) between agents, generate replies based on message history, and manage associated UI tools.*


### name (method, L30-L32, parent: Agent)

> *Summary: Retrieves and returns the designated string identifier for the agent instance. This method requires no input parameters to execute.*


### description (method, L35-L39, parent: Agent)

> *Summary: Returns a string describing the agent, which is intended to be used when introducing it within a group chat context.*


### send (method, L41-L55, parent: Agent)

> *Summary: Transmits a message, which can be a string or an OpenAI-formatted dictionary, to a specified agent. It optionally dictates whether the receiving agent should respond by setting the `request_reply` flag.*


### a_send (method, L57-L71, parent: Agent)

> *Summary: Sends a message, which can be a string or an OpenAI-formatted dictionary, to a specified agent. It optionally requests a reply from the recipient agent upon sending.*


### receive (method, L73-L86, parent: Agent)

> *Summary: Accepts an incoming message, which can be a string or a dictionary conforming to the OpenAI chat completion schema, along with the sending agent and an optional flag indicating if a response is expected. This method processes the received communication from another agent within the system.*


### a_receive (method, L88-L102, parent: Agent)

> *Summary: This asynchronous method processes an incoming message, which can be either a string or a dictionary conforming to the OpenAI ChatCompletion schema. It accepts the message content and the originating agent as inputs, performing internal logic based on these details.*


### generate_reply (method, L104-L119, parent: Agent)

> *Summary: This method generates a response by processing a list of messages adhering to the OpenAI ChatCompletion schema and optionally using a specified agent as context. It returns the resulting reply as either a string, a dictionary, or `None` if no reply is generated.*


### a_generate_reply (method, L121-L137, parent: Agent)

> *Summary: This asynchronous method generates a response by processing a list of messages adhering to the OpenAI ChatCompletion schema and optionally using a specified sender agent. It returns the resulting reply as either a string, a dictionary, or `None` if no reply is generated.*


### set_ui_tools (method, L139-L145, parent: Agent)

> *Summary: Assigns a provided list of `Tool` objects to configure the agent's user interface capabilities. This method takes a list of tools as input and modifies the internal state of the agent instance.*


### unset_ui_tools (method, L147-L153, parent: Agent)

> *Summary: Removes previously configured user interface tools from the agent's available functions, accepting a list of `Tool` objects as input and returning nothing.*


### LLMAgent (class, L158-L170)

> *Summary: Defines a protocol requiring an agent to expose its `system_message` and provide a method to update that message with a new string input. This allows for standardized interaction when managing LLM agents within the system.*


### system_message (method, L162-L163, parent: LLMAgent)

> *Summary: Returns the predefined system prompt string that dictates the agent's behavior and persona. This method takes no inputs and outputs a single string.*


### update_system_message (method, L165-L170, parent: LLMAgent)

> *Summary: Sets the internal system prompt for an agent using a provided string input. This method modifies the agent's configuration in place and returns nothing.*


### _check_protocol_implementation (function, L177-L178)

> *Summary: This function validates that the provided `ConversableAgent` adheres to the expected protocol and returns the agent instance if validation passes. It acts as a simple type check wrapper around the input agent object.*

