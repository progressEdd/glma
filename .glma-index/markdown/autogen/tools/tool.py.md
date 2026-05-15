# autogen/tools/tool.py

1 function(s): tool. 1 class(es): Tool. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Tool | class |  |
| tool | function |  |

## Chunks

### Tool (class, L20-L170)

> *Summary: Encapsulates a callable function or another tool with metadata like name and description. It allows registering the tool for both LLM-based suggestion and direct execution by an agent, providing various methods to retrieve its associated JSON schemas.*


### __init__ (method, L33-L75, parent: Tool)

> *Summary: Initializes a tool object by accepting a function/tool instance and optional metadata. It determines the underlying callable and sets up its name, description, and associated JSON schema based on whether it receives an existing `Tool` or a raw Python function.*


### name (method, L78-L79, parent: Tool)

> *Summary: Returns the stored name attribute of the object as a string. This method provides read access to the instance's designated name.*


### description (method, L82-L83, parent: Tool)

> *Summary: Returns the stored textual description of the tool as a string attribute.*


### func (method, L86-L87, parent: Tool)

> *Summary: Returns a callable object stored internally, allowing external code to execute the method's logic. This acts as an accessor for the underlying function implementation.*


### register_for_llm (method, L89-L101, parent: Tool)

> *Summary: This method makes the current tool available to a specified agent's language model by updating its tool signature or registering it directly with the agent if no schema is present. It ensures the agent can invoke the tool during interactions.*


### register_for_execution (method, L103-L112, parent: Tool)

> *Summary: This method registers the current tool instance with a specified `ConversableAgent` so it can be invoked directly by the agent, bypassing LLM interaction. It achieves this by calling the agent's internal registration mechanism with itself as the argument.*


### register_tool (method, L114-L126, parent: Tool)

> *Summary: This method registers a specified agent to both propose and execute a tool. It achieves this by calling separate registration methods for LLM proposal and execution on the provided agent object.*


### __call__ (method, L128-L138, parent: Tool)

> *Summary: This method executes the wrapped underlying function by passing all received positional and keyword arguments directly to it. It returns whatever value that internal function produces.*


### tool_schema (method, L141-L147, parent: Tool)

> *Summary: Retrieves a dictionary representing the schema for the tool by using the provided function object, name, and description. This output is designed for use with OpeaAI and compatible frameworks to handle function calls.*


### function_schema (method, L150-L158, parent: Tool)

> *Summary: Retrieves the structured JSON schema for a function definition using its associated callable, name, and description. This method returns the specific "function" part of the generated schema dictionary for backward compatibility with older OpenAI integration patterns.*


### realtime_tool_schema (method, L161-L170, parent: Tool)

> *Summary: Generates a structured dictionary representing the tool's API schema by combining its function definition with metadata like name and description. This output is intended for use in OpeaAI compatible frameworks to facilitate function calling.*


### tool (function, L174-L188)

> *Summary: This decorator wraps an existing function to transform it into a `Tool` object. It accepts optional name and description arguments to configure the resulting tool before returning it.*

