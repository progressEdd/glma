# test/beta/a2a/test_e2e_client_tools.py

1 function(s): get_weather. 1 class(es): TestE2EClientTools. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_weather | function |  |
| TestE2EClientTools | class |  |

## Chunks

### get_weather (function, L12-L13)

> *Summary: Accepts a city name string as input and returns a formatted string describing the weather for that location. This function simulates fetching weather data by returning a hardcoded message.*


### TestE2EClientTools (class, L17-L55)

> *Summary: This test suite verifies the end-to-end functionality of client tools by simulating interactions with a system. It tests scenarios including synchronous and streaming tool call round trips, as well as ensuring server history correctly records tool results after an initial query.*


### test_round_trip_with_local_tool (method, L18-L28, parent: TestE2EClientTools)

> *Summary: This test verifies a complete request-response cycle by simulating a user query ("how is paris?"). It uses a predefined tool call event and local tool implementation to ensure the client correctly processes the tool execution and returns the expected result string.*


### test_server_sees_tool_results_in_history_replay (method, L30-L43, parent: TestE2EClientTools)

> *Summary: This test verifies that the server correctly records tool execution results during a history replay scenario. It simulates a client asking for weather data and asserts that the tracking mechanism receives the expected `ToolResultsEvent` containing the mocked result.*


### test_streaming_tool_round_trip (method, L45-L55, parent: TestE2EClientTools)

> *Summary: This test verifies the end-to-end flow of a streaming tool call by simulating a request for weather in Paris. It asserts that the final response content matches the expected completion signal ("Done").*

