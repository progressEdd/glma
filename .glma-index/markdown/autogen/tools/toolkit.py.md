# autogen/tools/toolkit.py

1 class(es): Toolkit. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Toolkit | class |  |

## Chunks

### Toolkit (class, L17-L86)

> *Summary: Manages a collection of `Tool` objects, allowing for registration with an agent for both LLM prompting and execution. It provides methods to retrieve, add, or remove tools by name from its internal dictionary structure.*


### __init__ (method, L20-L26, parent: Toolkit)

> *Summary: Initializes an object by accepting a list of `Tool` instances and storing them in a dictionary keyed by each tool's name for quick lookup.*


### tools (method, L29-L31, parent: Toolkit)

> *Summary: Retrieves all available `Tool` objects stored within the instance's toolkit dictionary and returns them as a standard Python list.*


### register_for_llm (method, L33-L40, parent: Toolkit)

> *Summary: Iterates over all available tools within a toolkit and registers each one with the provided conversational LLM agent. This ensures that the agent is aware of and can utilize all defined tools.*


### register_for_execution (method, L42-L49, parent: Toolkit)

> *Summary: Iterates over all available tools within a toolkit and registers each one with the provided conversational agent, enabling the agent to utilize those tools during execution.*


### get_tool (method, L51-L63, parent: Toolkit)

> *Summary: Retrieves a specific `Tool` object from an internal collection using its string name as input. If the provided name does not match any registered tool, it raises a `ValueError`.*


### set_tool (method, L65-L71, parent: Toolkit)

> *Summary: Assigns a specific `Tool` object to the toolkit's internal mapping using the tool's name as the key. This updates or adds a capability available within the system's toolset.*


### remove_tool (method, L73-L82, parent: Toolkit)

> *Summary: This method deletes a specified tool from the toolkit's internal dictionary if it exists. It raises a `ValueError` if the provided tool name is not present.*


### __len__ (method, L84-L86, parent: Toolkit)

> *Summary: Returns the total count of available tools stored within the toolkit's internal collection. This method provides a size indicator for the toolkit object.*

