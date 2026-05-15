# test/beta/ag_ui/test_adapter.py

1 function(s): test_custom_event. 6 class(es): TestBasicConversation, TestBackendTools, TestFrontendTools, TestMixedTools, TestEventTypes, TestStateSnapshotEvent. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestBasicConversation | class |  |
| TestBackendTools | class |  |
| TestFrontendTools | class |  |
| TestMixedTools | class |  |
| TestEventTypes | class |  |
| TestStateSnapshotEvent | class |  |
| test_custom_event | function |  |

## Chunks

### TestBasicConversation (class, L37-L81)

> *Summary: This test class verifies the conversational flow of an agent by simulating interactions. It asserts that when provided with user messages (and optionally assistant responses), the system emits expected events like `RUN_STARTED`, chunks of text (`TEXT_MESSAGE_CHUNK`), and `RUN_FINISHED`.*


### test_basic_user_message (method, L38-L64, parent: TestBasicConversation)

> *Summary: This test verifies the streaming behavior of an agent by sending a user message and asserting that the resulting event stream contains `RUN_STARTED`, a chunked `TEXT_MESSAGE_CHUNK` containing the expected response, and finally, a `RUN_FINISHED` event. It confirms the correct structure and content of these events based on the initial configuration and input message.*


### test_multiple_messages_history (method, L66-L81, parent: TestBasicConversation)

> *Summary: This test verifies the agent's ability to handle a sequence of conversational turns. It feeds a predefined history of user and assistant messages into an `AGUIStream` and asserts that the stream emits the expected lifecycle events, including start, text chunks, and finish.*


### TestBackendTools (class, L84-L201)

> *Summary: This code verifies the functionality of an agent by simulating interactions with backend tools. It tests scenarios including single tool calls (with and without arguments), multiple sequential tool calls, ensuring the correct sequence of events like `TOOL_CALL_START`, `TOOL_CALL_ARGS`, and `TOOL_CALL_RESULT` are emitted for a given user input.*


### test_backend_tool_call_and_result (method, L85-L127, parent: TestBackendTools)

> *Summary: This test verifies the end-to-end flow of an agent interacting with a defined tool. It simulates a user query ("What time is it?"), asserts that the system correctly triggers a `TOOL_CALL`, receives the predefined result from the mocked function, and finally outputs the resulting text message before concluding the run.*


### test_backend_tool_with_arguments (method, L129-L162, parent: TestBackendTools)

> *Summary: This test verifies that an agent correctly invokes a defined tool with specific arguments when prompted. It simulates the interaction by sending a user message and asserts that the resulting event stream contains sequential calls for tool start, argument passing (with `a=5`, `b=3`), and final result reporting.*


### test_multiple_backend_tool_calls (method, L164-L201, parent: TestBackendTools)

> *Summary: This test verifies that an agent correctly invokes multiple backend tools when prompted. It asserts that the system emits two `TOOL_CALL_START` events for both defined tools and subsequently receives two corresponding `TOOL_CALL_RESULT` events.*


### TestFrontendTools (class, L204-L297)

> *Summary: This class provides asynchronous tests to validate the interaction flow of an agent with frontend tools. It simulates scenarios where the agent requests tool calls, receives results, and generates final text responses based on various inputs.*


### test_frontend_tool_call (method, L205-L228, parent: TestFrontendTools)

> *Summary: This test verifies the agent's ability to correctly initiate a tool call when prompted. It feeds an `Agent` with a specific tool definition and user message, then asserts that the resulting event stream contains exactly one partial chunk indicating the invocation of the `get_weather` tool for "Paris," followed by a final completion event.*


### test_frontend_tool_with_result (method, L230-L269, parent: TestFrontendTools)

> *Summary: This test verifies the agent's response when provided with a complete sequence including a tool call and its result. It feeds an input containing user query, assistant request for weather, and the actual weather data to assert that the resulting streamed text message contains both "sunny" and "22".*


### test_multiple_frontend_tools (method, L271-L297, parent: TestFrontendTools)

> *Summary: This test verifies that an agent correctly handles multiple tool calls requested in a single user message. It asserts that the stream produces exactly two `TOOL_CALL_CHUNK` events, and checks the order of these chunks based on their delta content matching specific location strings.*


### TestMixedTools (class, L300-L331)

> *Summary: This test verifies that an agent correctly handles mixed tool calls by simulating a request for both backend and frontend tools. It asserts the sequence of events, confirming that the system first initiates the `get_current_time` call before processing the `get_weather` chunk.*


### test_backend_and_frontend_tools (method, L301-L331, parent: TestMixedTools)

> *Summary: This test verifies the agent's ability to handle concurrent backend and frontend tool calls. It simulates a user request that triggers both time retrieval and weather fetching, asserting specific event types for each tool call initiation and chunking.*


### TestEventTypes (class, L334-L388)

> *Summary: These asynchronous tests validate the expected structure of various events emitted by an agent stream. They confirm that text messages, tool call starts/arguments/results/ends, adhere to specific dictionary schemas when processing user inputs.*


### test_text_message_event_structure (method, L335-L348, parent: TestEventTypes)

> *Summary: This test verifies the structure of a `TEXT_MESSAGE_CHUNK` event generated by an agent. It feeds a user message into an AGUI stream and asserts that the resulting chunk contains specific fields like `messageId`, `delta`, and `timestamp`.*


### test_tool_call_event_structure (method, L350-L388, parent: TestEventTypes)

> *Summary: This test verifies the expected sequence and structure of events when an agent invokes a defined tool. It simulates a user request, collects the resulting stream events, and asserts that `TOOL_CALL_START`, `TOOL_CALL_ARGS`, `TOOL_CALL_RESULT`, and `TOOL_CALL_END` events appear with specific required fields.*


### TestStateSnapshotEvent (class, L391-L486)

> *Summary: These asynchronous tests verify how state snapshots are generated during agent execution based on initial variables, runtime context updates, and input states. They assert that the correct `STATE_SNAPSHOT` events containing variable values are emitted when expected, or omitted otherwise.*


### test_initial_agent_variables_send_state_event (method, L392-L411, parent: TestStateSnapshotEvent)

> *Summary: This test verifies that an agent correctly emits a `STATE_SNAPSHOT` event containing its initial variables after processing a user message. It confirms the snapshot accurately reflects the input variable values provided to the agent upon initialization.*


### test_agent_turn_variables_send_state_event (method, L413-L434, parent: TestStateSnapshotEvent)

> *Summary: This test verifies that an agent correctly emits a `STATE_SNAPSHOT` event after executing a tool call, reflecting the input variables provided during the run. It asserts that the captured state snapshot contains the expected variable value passed to the mocked tool function.*


### test_frontend_variables_usage (method, L436-L454, parent: TestStateSnapshotEvent)

> *Summary: This test verifies that an agent correctly utilizes frontend variables when executing a tool call. It initializes an agent with a mockable tool and runs it with input containing state data, asserting the mock was called with the expected variable value from the input state.*


### test_no_initial_state_snapshot_when_state_matches (method, L456-L464, parent: TestStateSnapshotEvent)

> *Summary: When an agent's state matches the expected final state immediately upon initialization, this test verifies that no initial state snapshot event is generated. It achieves this by running a single input through the stream and asserting the absence of any `STATE_SNAPSHOT` events in the collected output.*


### test_state_snapshot_when_tool_returns_reply_result_with_context (method, L466-L486, parent: TestStateSnapshotEvent)

> *Summary: This test verifies that the agent's state correctly captures variable changes when a tool returns a reply with context. It asserts that two specific `STATE_SNAPSHOT` events are generated, reflecting initial and updated variable values after the tool execution modifies the context.*


### test_custom_event (function, L489-L506)

> *Summary: This test verifies that a custom event is correctly emitted when an agent executes a defined tool. It initializes an agent with a specific tool and then asserts that the collected stream events contain the expected partial dictionary structure for the custom event.*

