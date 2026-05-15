# test/ag_ui/test_adapter.py

7 class(es): TestBasicConversation, TestBackendTools, TestFrontendTools, TestMixedTools, TestEventTypes, TestContextHandling, TestStateSnapshotEvent. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestBasicConversation | class |  |
| TestBackendTools | class |  |
| TestFrontendTools | class |  |
| TestMixedTools | class |  |
| TestEventTypes | class |  |
| TestContextHandling | class |  |
| TestStateSnapshotEvent | class |  |

## Chunks

### TestBasicConversation (class, L35-L80)

> *Summary: This test suite verifies the basic conversational flow of an agent by simulating user inputs and asserting the sequence of emitted events. It checks for correct start, streamed text chunks, and final completion events when processing single or multiple message histories.*


### test_basic_user_message (method, L36-L63, parent: TestBasicConversation)

> *Summary: This test verifies the interaction flow by simulating a user message input to an agent and asserting that the resulting stream emits specific events: `RUN_STARTED`, followed by a chunked `TEXT_MESSAGE_CHUNK` containing the expected response, and finally `RUN_FINISHED`. It confirms the structure of these emitted events using predefined assertion helpers.*


### test_multiple_messages_history (method, L65-L80, parent: TestBasicConversation)

> *Summary: This test verifies the system's handling of a multi-turn conversation history. It simulates an interaction by providing a sequence of user and assistant messages as input to an agent stream and asserts that specific lifecycle events are emitted during execution.*


### TestBackendTools (class, L83-L224)

> *Summary: This code chunk contains unit tests that verify the execution flow of an AI agent when interacting with backend tools. It simulates user input and asserts that the system correctly emits events for tool calls (start, arguments, result, end) and final text responses based on predefined local functions.*


### test_backend_tool_call_and_result (method, L84-L135, parent: TestBackendTools)

> *Summary: This test verifies the end-to-end flow of a conversational agent when it invokes and receives results from a registered local tool. It simulates user input, asserts that the system correctly emits events for tool calling start/arguments, result reception, and final text output before concluding the run.*


### test_backend_tool_with_arguments (method, L137-L178, parent: TestBackendTools)

> *Summary: This test verifies that an agent correctly executes a registered backend tool with specific arguments when prompted. It simulates the interaction flow, asserting that the system emits events for tool call start, argument passing (with values 5 and 3), and the final result containing the sum of 8.*


### test_multiple_backend_tool_calls (method, L180-L224, parent: TestBackendTools)

> *Summary: This test verifies that an agent correctly executes multiple registered backend tools when prompted. It simulates a run by providing inputs and asserts that the system emits the correct number of `TOOL_CALL_START` and `TOOL_CALL_RESULT` events for each tool called.*


### TestFrontendTools (class, L227-L359)

> *Summary: This code contains unit tests that verify the behavior of an agent interface when interacting with frontend tools. It simulates scenarios involving single tool calls, subsequent responses after receiving tool results, and handling multiple concurrent tool calls to ensure correct event streaming and processing.*


### test_frontend_tool_call (method, L228-L259, parent: TestFrontendTools)

> *Summary: This test verifies the agent's behavior when handling a tool call request. It simulates an interaction where the agent receives a user query and correctly triggers a partial `TOOL_CALL_CHUNK` event for the specified weather tool.*


### test_frontend_tool_with_result (method, L261-L307, parent: TestFrontendTools)

> *Summary: This test verifies the agent's behavior when provided with a pre-existing tool result. It simulates an interaction where the user asks for weather, the agent calls a function, and then immediately receives the function's output to generate a final text response.*


### test_multiple_frontend_tools (method, L309-L359, parent: TestFrontendTools)

> *Summary: This test verifies that an agent correctly handles and processes multiple concurrent tool calls initiated from a single user prompt. It asserts that the system emits two distinct `TOOL_CALL_CHUNK` events corresponding to the specified weather queries for Paris and London.*


### TestMixedTools (class, L362-L418)

> *Summary: This test verifies an agent's ability to handle mixed tool calls by simulating a scenario where the LLM requests both a registered backend function (`get_current_time`) and a frontend-provided tool (`get_weather`). It asserts that the event stream correctly processes the start of the backend call followed by a chunk for the frontend call.*


### test_backend_and_frontend_tools (method, L363-L418, parent: TestMixedTools)

> *Summary: This test verifies the agent's ability to handle mixed tool calls by simulating a scenario where both a registered backend function and an external frontend tool are invoked. It asserts that the event stream correctly reports the start of execution for both the internal time retrieval and the external weather query.*


### TestEventTypes (class, L421-L490)

> *Summary: This test suite verifies the expected structure of various events emitted by an agent interaction stream. It specifically asserts that text message chunks and different stages of a tool call (start, arguments, result, end) conform to predefined dictionary schemas when processing user inputs.*


### test_text_message_event_structure (method, L422-L436, parent: TestEventTypes)

> *Summary: This test verifies the structure of a `TEXT_MESSAGE_CHUNK` event generated by an agent. It simulates sending a user message and asserts that the resulting event contains specific fields like `messageId`, `delta`, and `timestamp`.*


### test_tool_call_event_structure (method, L438-L490, parent: TestEventTypes)

> *Summary: This test verifies the expected sequence and structure of events when an agent executes a registered tool. It simulates a user request to call "my\_tool" and asserts that the stream emits `TOOL_CALL_START`, `TOOL_CALL_ARGS`, `TOOL_CALL_RESULT`, and `TOOL_CALL_END` events with specific payload schemas.*


### TestContextHandling (class, L493-L515)

> *Summary: This test verifies that context data is correctly passed to an agent stream during execution. It initializes a conversational agent and streams its output while providing specific user and session context, asserting that the resulting events include start and finish markers.*


### test_context_passed_to_stream (method, L494-L515, parent: TestContextHandling)

> *Summary: This test verifies that contextual data is correctly passed through the streaming interface during agent execution. It initializes an agent and streams its output while providing a specific context dictionary to the `dispatch` method, asserting that both start and finish events are received.*


### TestStateSnapshotEvent (class, L518-L619)

> *Summary: These asynchronous test methods verify the behavior of state snapshots during agent execution. They assert that a `STATE_SNAPSHOT` event is emitted when context variables are present or after tool execution updates the state, and conversely, no snapshot occurs if the initial state matches expectations.*


### test_initial_state_snapshot_when_agent_has_context_variables (method, L519-L548, parent: TestStateSnapshotEvent)

> *Summary: This test verifies that an initial state snapshot correctly captures predefined context variables when a conversational agent is initialized. It simulates the start of a run and asserts that the emitted `STATE_SNAPSHOT` event contains the expected context data.*


### test_no_initial_state_snapshot_when_state_matches (method, L550-L565, parent: TestStateSnapshotEvent)

> *Summary: This test verifies that no initial state snapshot is generated when the agent's starting state matches the provided input state. It runs a conversation simulation with an empty initial state and asserts the sequence of events includes `RUN_STARTED`, `TEXT_MESSAGE_CHUNK`, and `RUN_FINISHED` while explicitly excluding any `STATE_SNAPSHOT`.*


### test_state_snapshot_when_tool_returns_reply_result_with_context (method, L567-L619, parent: TestStateSnapshotEvent)

> *Summary: This test verifies that the agent correctly captures and reflects its internal state after a tool execution returns a result containing context. It simulates an interaction where a user asks for proverbs, triggering a tool call that reads existing context variables, and then asserts that a state snapshot accurately records these initial proverb values.*

