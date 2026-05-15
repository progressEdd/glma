# autogen/agentchat/contrib/capabilities/tools_capability.py

1 class(es): ToolsCapability. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ToolsCapability | class |  |

## Chunks

### ToolsCapability (class, L9-L22)

> *Summary: This class encapsulates a collection of `Tool` objects intended for an agent. It initializes with a list of tools and provides a method to register each tool with a specified `ConversableAgent`.*


### __init__ (method, L16-L17, parent: ToolsCapability)

> *Summary: Initializes the capability by storing a provided list of `Tool` objects internally. This allows the agent to access and utilize the specified tools during operation.*


### add_to_agent (method, L19-L22, parent: ToolsCapability)

> *Summary: Registers all available tools within this capability object onto a specified `ConversableAgent`. This method iterates through its internal list of tools and calls each tool's registration function against the provided agent instance.*

