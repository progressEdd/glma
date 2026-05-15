# autogen/testing/messages.py

1 function(s): tools_message. 1 class(es): ToolCall. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ToolCall | class |  |
| tools_message | function |  |

## Chunks

### ToolCall (class, L14-L36)

> *Summary: This class encapsulates a request to execute an external function by storing the target tool name and its associated keyword arguments. It serializes this information into a standardized dictionary format suitable for communication with an API or message queue.*


### __init__ (method, L22-L27, parent: ToolCall)

> *Summary: Initializes a message object by creating a `RawToolCall` structure. It takes a tool name and arbitrary keyword arguments to construct a standardized function call representation within the message.*


### to_message (method, L29-L36, parent: ToolCall)

> *Summary: Converts an instance of the class into a standardized dictionary structure suitable for external API communication. It delegates this conversion by calling another helper function, `tools_message`.*


### tools_message (function, L39-L45)

> *Summary: Transforms a variable number of `ToolCall` objects into a dictionary structure containing the corresponding tool messages under the `"tool_calls"` key. This output format is designed to be consumed by an API call.*

