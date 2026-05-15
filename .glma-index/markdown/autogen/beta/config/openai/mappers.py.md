# autogen/beta/config/openai/mappers.py

11 function(s): response_proto_to_schema, _ensure_additional_properties_false, response_proto_to_text_config, events_to_responses_input, convert_messages, _ensure_object_schema, tool_to_api, tool_to_responses_api, responses_api_includes, normalize_usage and 1 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| response_proto_to_schema | function |  |
| _ensure_additional_properties_false | function |  |
| response_proto_to_text_config | function |  |
| events_to_responses_input | function |  |
| convert_messages | function |  |
| _ensure_object_schema | function |  |
| tool_to_api | function |  |
| tool_to_responses_api | function |  |
| responses_api_includes | function |  |
| normalize_usage | function |  |
| normalize_responses_usage | function |  |

## Chunks

### response_proto_to_schema (function, L44-L58)

> *Summary: Transforms a `ResponseProto` object containing JSON schema information into a structured dictionary suitable for chat completions' `response_format`. It ensures the schema is strict and packages it with the response name and description.*


### _ensure_additional_properties_false (function, L61-L91)

> *Summary: This function recursively traverses a JSON schema dictionary, ensuring that every object node explicitly sets `"additionalProperties": false`. It modifies the input schema in place (by returning a copy) to satisfy OpenAI API requirements for all object definitions.*


### response_proto_to_text_config (function, L94-L112)

> *Summary: Transforms a `ResponseProto` object into a dictionary structure suitable for the Responses API text configuration. It uses the proto's JSON schema and name to construct a strict, JSON-schema based format definition, optionally including a description.*


### events_to_responses_input (function, L115-L275)

> *Summary: Transforms a sequence of various internal events (like model responses, tool results, and user requests) into the structured input format required by the OpenAI Responses API. It handles serialization and conversion for different data types, including text, images, files via base64 or URLs, and function call outputs.*


### convert_messages (function, L278-L368)

> *Summary: This function transforms a sequence of internal event objects (`BaseEvent`) and a system prompt into the list-of-dictionaries format required by the OpenAI API. It handles different message types—including model responses, tool results, and user requests with various inputs like text, data, images, or files—to construct the final structured output.*


### _ensure_object_schema (function, L371-L377)

> *Summary: This utility function transforms a dictionary of parameters into a valid OpenAI object schema structure. It ensures the resulting dictionary has `"type": "object"` and initializes empty `"properties"` and `additionalProperties: false` fields.*


### tool_to_api (function, L380-L392)

> *Summary: Converts a `FunctionToolSchema` object into the specific dictionary format required by the OpenAI Chat Completions API. It maps the tool's name, description, and parameters schema to the expected structure, raising an error for unsupported tool types.*


### tool_to_responses_api (function, L395-L490)

> *Summary: This function transforms various internal tool schema objects into a standardized dictionary format compatible with the OpenAI Responses API. It handles specific conversions for functions, web search, code execution, shell commands, image generation, and remote MCP servers based on the input tool type.*


### responses_api_includes (function, L493-L498)

> *Summary: This function filters a collection of tool schemas to identify and return specific API inclusion strings for web search capabilities. It iterates through the input tools and adds `"web_search_call.action.sources"` to the output list if any tool is an instance of `WebSearchToolSchema`.*


### normalize_usage (function, L501-L510)

> *Summary: Transforms a `CompletionUsage` object into a standardized `Usage` structure. It maps token counts from the input to the output, specifically extracting cached and reasoning tokens if available in the source details.*


### normalize_responses_usage (function, L513-L520)

> *Summary: Transforms a detailed `ResponseUsage` object into a simplified `Usage` structure by mapping specific token counts from the input and output details. It consolidates various usage metrics like prompt, completion, and total tokens for standardized reporting.*

