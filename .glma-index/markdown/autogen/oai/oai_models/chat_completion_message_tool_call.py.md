# autogen/oai/oai_models/chat_completion_message_tool_call.py

4 class(es): Function, Custom, ChatCompletionMessageFunctionToolCall, ChatCompletionMessageCustomToolCall.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Function | class |  |
| Custom | class |  |
| ChatCompletionMessageFunctionToolCall | class |  |
| ChatCompletionMessageCustomToolCall | class |  |

## Chunks

### Function (class, L16-L26)

> *Summary: Represents a tool call request containing the function's name and its arguments as a JSON string. It serves as an input structure for invoking external functions based on model output, requiring manual validation of the provided arguments.*


### Custom (class, L29-L34)

> *Summary: Defines a data structure for a custom tool call, requiring both an input string and a unique tool name. This model serves as the expected payload when invoking a user-defined function via an AI agent.*


### ChatCompletionMessageFunctionToolCall (class, L37-L45)

> *Summary: Represents a structured message indicating a tool invocation within a chat completion context. It requires an ID string, the specific function definition being called, and explicitly sets the message type to "function".*


### ChatCompletionMessageCustomToolCall (class, L48-L56)

> *Summary: Represents a specific type of tool call within a chat completion message. It requires an ID string and a `Custom` object detailing the invoked custom tool.*

