# autogen/beta/a2a/mappers/history.py

8 function(s): events_to_payload, payload_to_events, _event_to_dict, _tool_result_event_to_dict, _dict_to_event, _input_to_dict, _dict_to_input, _binary_kind_or_default.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| events_to_payload | function |  |
| payload_to_events | function |  |
| _event_to_dict | function |  |
| _tool_result_event_to_dict | function |  |
| _dict_to_event | function |  |
| _input_to_dict | function |  |
| _dict_to_input | function |  |
| _binary_kind_or_default | function |  |

## Chunks

### events_to_payload (function, L42-L55)

> *Summary: Converts a sequence of `BaseEvent` objects into a JSON-serializable payload structure. It filters out transient events and unknown types, returning a dictionary containing a list of serialized event dictionaries.*


### payload_to_events (function, L58-L72)

> *Summary: Converts a dictionary payload containing event data into a list of structured `BaseEvent` objects. It iterates over the "events" array in the input, safely converting each entry while skipping any entries with an unknown type to maintain backward compatibility.*


### _event_to_dict (function, L75-L117)

> *Summary: Converts a specific event object (`BaseEvent`) into a standardized dictionary format for history tracking. It inspects the input event type (e.g., `ModelRequest`, `ToolResultsEvent`, `ModelResponse`) and maps it to the corresponding structured output containing its kind and relevant payload data.*


### _tool_result_event_to_dict (function, L120-L127)

> *Summary: Converts a `ToolResultEvent` object into a dictionary representation suitable for event serialization. It maps the event's parent ID, name, and result content to standard fields, optionally including an error string if the input is a `ToolErrorEvent`.*


### _dict_to_event (function, L130-L156)

> *Summary: Converts a dictionary entry, identified by its "kind," into a specific `BaseEvent` object. It handles various event types like user input, tool calls/results, and model responses by calling specialized conversion helpers based on the entry's structure.*


### _input_to_dict (function, L166-L183)

> *Summary: Converts various input object types (`TextInput`, `BinaryInput`, etc.) into a standardized dictionary format suitable for serialization or processing. It maps specific input structures—like text content, base64 encoded binary data, URLs, or file IDs—to corresponding structured dictionaries with defined part types.*


### _dict_to_input (function, L186-L215)

> *Summary: Converts a dictionary entry into a specific `Input` object based on its `"type"` field. It handles various input types like text, binary (decoding base64 data), URL, file ID, and raw data. If the type is unrecognized or decoding fails for binary data, it returns `None`.*


### _binary_kind_or_default (function, L218-L224)

> *Summary: This helper function determines the appropriate `BinaryType` for a given input value. If the input is a string, it attempts to parse it as a specific binary type; otherwise, it defaults to `BinaryType.BINARY`.*

