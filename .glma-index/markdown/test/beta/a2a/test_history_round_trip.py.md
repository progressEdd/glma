# test/beta/a2a/test_history_round_trip.py

3 function(s): test_tool_calls_event_wrapper_round_trips, test_tool_results_event_wrapper_round_trips, test_wrapper_and_leaves_serialize_independently.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_tool_calls_event_wrapper_round_trips | function |  |
| test_tool_results_event_wrapper_round_trips | function |  |
| test_wrapper_and_leaves_serialize_independently | function |  |

## Chunks

### test_tool_calls_event_wrapper_round_trips (function, L15-L23)

> *Summary: This test verifies the round-trip integrity of tool call events by serializing a list of `ToolCallEvent` objects into a payload and then deserializing it back. It asserts that the resulting event structure exactly matches the initial input, confirming lossless serialization/deserialization.*


### test_tool_results_event_wrapper_round_trips (function, L26-L34)

> *Summary: This test verifies the round-trip integrity of `ToolResultsEvent` objects by serializing them to a payload and then deserializing them back into events. It asserts that the resulting event structure exactly matches the initial input, confirming serialization/deserialization correctness.*


### test_wrapper_and_leaves_serialize_independently (function, L37-L46)

> *Summary: This test verifies that serialization and deserialization correctly handle a wrapper event alongside its contained leaf events. It ensures that when both are processed through the round-trip mechanism, they are perfectly reconstructed in the output list.*

