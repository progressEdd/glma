# test/beta/ag_ui/utils.py

7 function(s): uuid_str, create_run_input, get_weather_tool, collect_events, assert_event_type, assert_no_event_type, get_events_of_type.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| uuid_str | function |  |
| create_run_input | function |  |
| get_weather_tool | function |  |
| collect_events | function |  |
| assert_event_type | function |  |
| assert_no_event_type | function |  |
| get_events_of_type | function |  |

## Chunks

### uuid_str (function, L14-L15)

> *Summary: Generates a universally unique identifier as a string by calling `uuid4()` and casting the result to a string. This function produces a standard UUID string output.*


### create_run_input (function, L18-L33)

> *Summary: Constructs a `RunAgentInput` object by accepting messages, optional tools, and an optional thread ID. It generates unique IDs for the run and thread if not provided, serializes the state, and packages all inputs into the return structure.*


### get_weather_tool (function, L36-L50)

> *Summary: Constructs and returns a `Tool` object designed to retrieve weather information. This tool requires one string argument, `location`, specifying where the weather should be fetched.*


### collect_events (function, L53-L59)

> *Summary: This asynchronous function consumes an `AGUIStream` by dispatching a `RunAgentInput`, parsing each received message as JSON, and returns a list of these parsed event dictionaries. It filters out empty or prefixed data strings during the stream iteration.*


### assert_event_type (function, L62-L66)

> *Summary: This utility iterates through a list of event dictionaries, searching for one matching the specified `event_type`. It returns the first matching event dictionary or raises an `AssertionError` if no such event is found.*


### assert_no_event_type (function, L69-L72)

> *Summary: Checks a list of event dictionaries to ensure none possess a specific `event_type`. If an event matching the provided type is found, it raises an assertion error detailing the unexpected occurrence.*


### get_events_of_type (function, L75-L76)

> *Summary: Filters a list of event dictionaries to return only those matching a specified `event_type`. It takes a list of all events and the desired type string as input, yielding a subset of matching events.*

