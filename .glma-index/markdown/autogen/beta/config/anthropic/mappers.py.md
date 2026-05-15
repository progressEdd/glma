# autogen/beta/config/anthropic/mappers.py

10 function(s): _ensure_additional_properties_false, response_proto_to_output_config, _ensure_object_schema, tool_to_api, extract_mcp_servers, extract_skills_for_container, _file_id_block_type, has_file_id_references, convert_messages, normalize_usage.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _ensure_additional_properties_false | function |  |
| response_proto_to_output_config | function |  |
| _ensure_object_schema | function |  |
| tool_to_api | function |  |
| extract_mcp_servers | function |  |
| extract_skills_for_container | function |  |
| _file_id_block_type | function |  |
| has_file_id_references | function |  |
| convert_messages | function |  |
| normalize_usage | function |  |

## Chunks

### _ensure_additional_properties_false (function, L46-L76)

> *Summary: Recursively traverses a JSON schema dictionary to enforce `additionalProperties: false` on all object nodes. It modifies the input schema in place (returning a copy) by setting this property for objects and applying the transformation to nested properties, definitions, and array item schemas.*


### response_proto_to_output_config (function, L79-L91)

> *Summary: Transforms a `ResponseProto` containing a JSON schema into an Anthropic-compatible output configuration dictionary. It returns `None` if the input response or its schema is missing, otherwise it wraps the validated schema in the required format structure.*


### _ensure_object_schema (function, L94-L99)

> *Summary: This utility function modifies a parameter dictionary to conform to Anthropic's requirement for an `input_schema`. It ensures the resulting dictionary has `"type": "object"` and initializes an empty `"properties"` field if it doesn't already exist.*


### tool_to_api (function, L102-L181)

> *Summary: Converts various tool schema objects into a standardized dictionary format suitable for API consumption. It handles different tool types—such as functions, web search, code execution, and memory—by mapping their specific attributes to the required API structure, raising errors for unsupported schemas like `ShellToolSchema`.*


### extract_mcp_servers (function, L184-L197)

> *Summary: This function processes an iterable of `ToolSchema` objects to filter and extract specific server configurations from instances of `MCPServerToolSchema`. It returns a list of dictionaries, each representing an Anthropic MCP server with its URL, name, and optional authorization token.*


### extract_skills_for_container (function, L200-L212)

> *Summary: This function processes an iterable of `ToolSchema` objects to extract specific Anthropic skill definitions. It filters for `SkillsToolSchema` instances and returns a list of dictionaries, each containing the skill ID and version formatted for container use.*


### _file_id_block_type (function, L221-L227)

> *Summary: Determines the Anthropic content block type by inspecting a provided filename. It returns `"image"` if the extension matches known image types, otherwise it defaults to `"document"`.*


### has_file_id_references (function, L230-L243)

> *Summary: Checks a sequence of messages to determine if any user request or tool result contains references to file IDs. It returns `True` if a `FileIdInput` is found within the message parts, otherwise it returns `False`.*


### convert_messages (function, L246-L481)

> *Summary: Transforms a stream of internal conversation events into a list of structured messages suitable for the Anthropic API. It processes various event types—including model responses, tool calls, and results—while intelligently filtering out orphaned tool use or result blocks to maintain API contract validity despite potential data loss during state reduction.*


### normalize_usage (function, L484-L496)

> *Summary: Transforms raw usage data from Anthropic into a standardized `Usage` object. It extracts and converts input/output token counts, including specific cache-related metrics, ensuring all values are correctly typed for downstream use.*

