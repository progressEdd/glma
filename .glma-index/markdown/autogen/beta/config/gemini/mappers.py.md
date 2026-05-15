# autogen/beta/config/gemini/mappers.py

11 function(s): response_proto_to_config, build_system_instruction, _strip_additional_properties, _ensure_object_schema, build_tools, _mime_from_url, _apply_vendor_metadata, convert_messages, normalize_usage, _to_float and 1 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| response_proto_to_config | function |  |
| build_system_instruction | function |  |
| _strip_additional_properties | function |  |
| _ensure_object_schema | function |  |
| build_tools | function |  |
| _mime_from_url | function |  |
| _apply_vendor_metadata | function |  |
| convert_messages | function |  |
| normalize_usage | function |  |
| _to_float | function |  |
| grounding_tool_name | function |  |

## Chunks

### response_proto_to_config (function, L39-L47)

> *Summary: Transforms a `ResponseProto` object into a dictionary suitable for Gemini's `GenerateContentConfig`. It extracts the JSON schema from the proto if present, otherwise returns an empty configuration.*


### build_system_instruction (function, L50-L55)

> *Summary: Concatenates an iterable of strings from the `system_prompt` input, joining them with newlines. It returns the resulting single string instruction or `None` if the input is empty.*


### _strip_additional_properties (function, L58-L71)

> *Summary: Recursively traverses a JSON Schema structure (dict or list) to remove any key named `"additionalProperties"`. This sanitizes the schema by stripping these properties, which is necessary because the Gemini API rejects them within `anyOf` or `oneOf` constructs.*


### _ensure_object_schema (function, L74-L87)

> *Summary: Ensures that function parameter schemas conform to Gemini's requirements by converting null or empty types into an empty object schema. It also recursively removes `additionalProperties` from the structure, as this feature is unsupported within `anyOf` branches in the target API.*


### build_tools (function, L90-L128)

> *Summary: Converts a list of various tool schemas into Gemini-compatible `Tool` objects. It processes different schema types—like function, web search, and code execution—to construct the appropriate tool definitions for the model. Returns a list of tools, or `None` if no tools are provided.*


### _mime_from_url (function, L163-L172)

> *Summary: Derives a MIME type string from the file extension found in a given URL path. It parses the URL, extracts the extension after the last dot, and looks up the corresponding MIME type in a predefined map, returning `None` if no match is found.*


### _apply_vendor_metadata (function, L175-L194)

> *Summary: This function updates a `Part` object by injecting Gemini-specific metadata from an input dictionary. It specifically sets fields like `media_resolution`, handles nested `video_metadata`, and modifies the `display_name` on either inline or file data within the part.*


### convert_messages (function, L197-L300)

> *Summary: Transforms an iterable of various event messages into a list of structured `types.Content` objects suitable for Gemini API interaction. It processes different message types—including model responses, tool calls, and user inputs—to correctly map content, function calls, and file data into the target format.*


### normalize_usage (function, L303-L314)

> *Summary: Transforms Gemini-specific usage metadata into a standardized `Usage` object. It extracts and converts token counts for prompts, completions, total usage, cached reads, and internal thinking processes from the input metadata.*


### _to_float (function, L317-L318)

> *Summary: Converts an input value to a floating-point number, returning `None` if the input itself is `None`. This utility ensures type consistency when numerical data is expected.*


### grounding_tool_name (function, L321-L324)

> *Summary: Determines the appropriate tool name based on whether `GroundingMetadata` contains web search queries. It returns a specific constant if queries exist, otherwise it defaults to another specified tool name.*

