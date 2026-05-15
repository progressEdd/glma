# autogen/agentchat/remote/protocol.py

1 function(s): get_tool_names. 4 class(es): AgentBusMessage, RequestMessage, ResponseMessage, ServiceResponse. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AgentBusMessage | class |  |
| RequestMessage | class |  |
| ResponseMessage | class |  |
| ServiceResponse | class |  |
| get_tool_names | function |  |

## Chunks

### AgentBusMessage (class, L9-L11)

> *Summary: This data structure encapsulates communication between agents by holding a list of message dictionaries and an optional context dictionary. It serves as the standardized payload for inter-agent messaging within the system.*


### RequestMessage (class, L14-L19)

> *Summary: This message structure encapsulates a list of tools provided by the client, allowing for easy retrieval of just the tool names via a computed property. It inherits from `AgentBusMessage` to facilitate communication within the agent system.*


### client_tool_names (method, L18-L19, parent: RequestMessage)

> *Summary: Retrieves a set of strings representing the names of tools available to the client by calling an external function with the client's tool list. This method exposes the client's capabilities for interaction.*


### ResponseMessage (class, L22-L23)

> *Summary: Represents a message sent back from an agent, inheriting from `AgentBusMessage`. It optionally accepts a string input parameter.*


### ServiceResponse (class, L26-L30)

> *Summary: Represents the structured response from a remote service call. It encapsulates the result message, relevant context data, any required further input, and optional streaming text content.*


### get_tool_names (function, L33-L34)

> *Summary: Extracts the names of available functions from a list of tool definitions. It returns these unique function names as a set, filtering out any invalid or missing entries.*

