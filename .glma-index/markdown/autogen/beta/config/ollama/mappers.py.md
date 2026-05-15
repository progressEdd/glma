# autogen/beta/config/ollama/mappers.py

4 function(s): response_proto_to_format, _ensure_object_schema, tool_to_api, convert_messages.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| response_proto_to_format | function |  |
| _ensure_object_schema | function |  |
| tool_to_api | function |  |
| convert_messages | function |  |

## Chunks

### response_proto_to_format (function, L29-L34)

> *Summary: Transforms a `ResponseProto` object into the dictionary structure required by Ollama's format parameter, returning `None` if the input is null or lacks a JSON schema.*


### _ensure_object_schema (function, L37-L42)

> *Summary: This utility function modifies a parameter dictionary by explicitly setting its `type` to `"object"` and ensuring it contains an empty `properties` dictionary if one doesn't already exist, satisfying the Ollama SDK's requirement for tool parameters. It takes a general dictionary as input and returns the modified schema dictionary.*


### tool_to_api (function, L45-L59)

> *Summary: Converts a `ToolSchema` object into an API-compatible dictionary structure. It specifically transforms `FunctionToolSchema` instances into a function call definition while rejecting other tool types like `SkillsToolSchema`.*


### convert_messages (function, L62-L125)

> *Summary: Transforms a sequence of system prompts, model requests, responses, and tool results into a list of dictionaries formatted for the Ollama API. It processes different event types by extracting text, encoding data inputs, base64-encoding images from requests, and structuring tool calls/results appropriately.*

