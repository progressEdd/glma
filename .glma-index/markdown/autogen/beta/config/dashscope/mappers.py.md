# autogen/beta/config/dashscope/mappers.py

3 function(s): response_proto_to_format, tool_to_api, convert_messages.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| response_proto_to_format | function |  |
| tool_to_api | function |  |
| convert_messages | function |  |

## Chunks

### response_proto_to_format (function, L29-L41)

> *Summary: Transforms a `ResponseProto` object into an OpenAI-compatible dictionary format suitable for DashScope responses. It extracts the JSON schema, name, and description from the input proto to construct the output structure.*


### tool_to_api (function, L44-L58)

> *Summary: Converts a `ToolSchema` object into an API-compatible dictionary structure. It specifically transforms `FunctionToolSchema` instances into a function call definition while raising an error for unsupported tool types like `SkillsToolSchema`.*


### convert_messages (function, L61-L122)

> *Summary: Transforms a sequence of system prompts and various event types (requests, responses, tool results) into a standardized list of API message dictionaries. It handles text, serialized data, and image inputs/outputs by converting them into structured content blocks for the target API format.*

