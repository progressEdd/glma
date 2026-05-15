# autogen/beta/a2a/mappers/tools.py

8 function(s): schemas_to_payload, payload_to_schemas, call_to_payload, payload_to_call, result_event_to_payload, payload_to_result_event, results_to_payload, payload_to_results.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| schemas_to_payload | function |  |
| payload_to_schemas | function |  |
| call_to_payload | function |  |
| payload_to_call | function |  |
| result_event_to_payload | function |  |
| payload_to_result_event | function |  |
| results_to_payload | function |  |
| payload_to_results | function |  |

## Chunks

### schemas_to_payload (function, L20-L35)

> *Summary: Converts a collection of `FunctionToolSchema` objects into a dictionary payload suitable for the `tool-schemas+json` extension. It structures the output to list each tool's name, description, and parameters for transmission from client to server.*


### payload_to_schemas (function, L38-L48)

> *Summary: Transforms a dictionary containing tool definitions into a list of `FunctionToolSchema` objects. It iterates over the "tools" array within the input payload, mapping each tool definition to its corresponding schema structure.*


### call_to_payload (function, L51-L57)

> *Summary: Converts a `ToolCallEvent` object into a dictionary structure suitable for the `tool-call+json` Part. It serializes the event's ID, name, and arguments into the output payload.*


### payload_to_call (function, L60-L65)

> *Summary: Transforms a dictionary payload containing an ID, name, and optional arguments into a structured `ToolCallEvent`. It extracts these fields from the input mapping to construct the event object.*


### result_event_to_payload (function, L68-L80)

> *Summary: Converts a `ToolResultEvent` object into a dictionary format suitable for wire transmission. It maps the internal `parent_id` to the external `"id"` field and serializes the result content and any associated errors.*


### payload_to_result_event (function, L83-L103)

> *Summary: Converts a dictionary payload from various wire formats into either a `ToolResultEvent` or a `ToolErrorEvent`. It normalizes inputs by accepting either an `id` or `parent_id`, and switches to the error event type if an "error" key is present in the input.*


### results_to_payload (function, L106-L114)

> *Summary: Converts an iterable of `ToolResultEvent` objects into a dictionary payload suitable for the `tool-result+json` part. It serializes each result event, ensuring necessary context like the tool name is included for stateless server processing.*


### payload_to_results (function, L117-L124)

> *Summary: Converts a dictionary containing tool results into a list of `ToolResultEvent` objects. It processes the "results" array within the input payload, automatically handling and wrapping any errors found in individual entries as `ToolErrorEvent`s.*

