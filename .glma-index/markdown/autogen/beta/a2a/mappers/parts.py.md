# autogen/beta/a2a/mappers/parts.py

12 function(s): input_to_part, part_to_input, data_part, is_data_part_with_mime, part_data_to_python, tool_result_to_text, _value_from, _value_to_python, struct_from_dict, struct_to_dict and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| input_to_part | function |  |
| part_to_input | function |  |
| data_part | function |  |
| is_data_part_with_mime | function |  |
| part_data_to_python | function |  |
| tool_result_to_text | function |  |
| _value_from | function |  |
| _value_to_python | function |  |
| struct_from_dict | function |  |
| struct_to_dict | function |  |
| _binary_kind | function |  |
| _json_default | function |  |

## Chunks

### input_to_part (function, L31-L66)

> *Summary: Transforms an `Input` object into a standardized `Part` protobuf message based on the input type. It handles various input forms—text, binary data, URLs, file IDs, and raw data—mapping them to the appropriate field (`text`, `raw`, `url`, or `data`) within the output structure.*


### part_to_input (function, L69-L100)

> *Summary: Transforms an A2A `Part` object into a corresponding AG2 `Input` event by prioritizing text, then checking for file IDs, raw binary data, URLs, or structured data fields. If none of these fields are present in the part, it raises a `ValueError`.*


### data_part (function, L103-L109)

> *Summary: Constructs a `Part` object containing structured data by wrapping the input payload using an internal conversion utility. It requires the raw payload and a specific MIME type string to define the content's nature.*


### is_data_part_with_mime (function, L112-L113)

> *Summary: Checks if a given `Part` object contains data and matches the specified MIME type string. Returns a boolean indicating this condition is true.*


### part_data_to_python (function, L116-L118)

> *Summary: Converts the raw `data` field from a structured `Part` object into its corresponding native Python type using an internal decoding utility. It takes a `Part` instance as input and returns any decoded Python object.*


### tool_result_to_text (function, L121-L130)

> *Summary: Converts a `ToolResult` object into a single string by concatenating the text content of its constituent parts. It handles both explicit text inputs and other parts by falling back to their standard string representation.*


### _value_from (function, L133-L136)

> *Summary: Converts a Python object into a `struct_pb2.Value` protobuf message by serializing the input using JSON encoding. It takes any arbitrary value as input and returns the structured protobuf representation.*


### _value_to_python (function, L139-L140)

> *Summary: Converts a protobuf `Value` message into a standard Python dictionary using JSON formatting. It preserves the original field names during this conversion process.*


### struct_from_dict (function, L143-L146)

> *Summary: Converts a Python dictionary into a `struct_pb2.Struct` protobuf message by parsing the input payload using `json_format`. This function takes a dictionary as input and returns a populated Protobuf struct object.*


### struct_to_dict (function, L149-L152)

> *Summary: Converts a Protocol Buffer `Struct` message into a standard Python dictionary. It handles empty inputs by returning an empty dictionary and uses `json_format.MessageToDict` for the conversion while retaining original field names.*


### _binary_kind (function, L155-L160)

> *Summary: Determines the specific type of binary data from a metadata dictionary. It attempts to cast the value associated with `_BINARY_KIND_METADATA_KEY` into a `BinaryType`, defaulting to `BinaryType.BINARY` if casting fails.*


### _json_default (function, L163-L170)

> *Summary: This function acts as a custom JSON encoder default handler, converting `datetime` and `Decimal` objects to strings, encoding `bytes` into base64 strings, and serializing dataclasses using `asdict`. If an object type is encountered that it cannot handle, it raises a `TypeError`.*

