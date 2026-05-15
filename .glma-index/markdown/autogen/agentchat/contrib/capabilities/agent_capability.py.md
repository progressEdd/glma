# autogen/agentchat/contrib/capabilities/agent_capability.py

1 class(es): AgentCapability. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AgentCapability | class |  |

## Chunks

### AgentCapability (class, L10-L20)

> *Summary: Provides a base structure for defining modular functionalities that can augment an AI agent. Subclasses must implement the `add_to_agent` method to integrate their specific behavior into a given `ConversableAgent`.*


### __init__ (method, L13-L14, parent: AgentCapability)

> *Summary: Initializes an agent capability object with no specific parameters. This constructor sets up the basic structure for defining and managing capabilities within an agent system.*


### add_to_agent (method, L16-L20, parent: AgentCapability)

> *Summary: This method requires subclasses to implement logic for integrating a specific capability into a provided `ConversableAgent`. Typically, this involves registering hooks on the target agent instance.*

