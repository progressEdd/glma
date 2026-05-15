# test/opentelemetry/test_instrument_agent.py

1 function(s): otel_setup. 15 class(es): TestInstrumentAgentBasic, TestInstrumentAgentIdempotency, TestConversationSpan, TestAgentInvokeSpan, TestSpanHierarchy, TestMultipleTurns, TestToolExecutionSpan, TestAsyncInstrumentAgent, TestToolExecutionDictArguments, TestAsyncToolExecutionSpan, TestConversationSpanDictMessage, TestConversationSpanCostAndUsage, TestInstrumentResume, TestInstrumentRunChat, TestInstrumentInitiateChats. 64 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| otel_setup | function |  |
| TestInstrumentAgentBasic | class |  |
| TestInstrumentAgentIdempotency | class |  |
| TestConversationSpan | class |  |
| TestAgentInvokeSpan | class |  |
| TestSpanHierarchy | class |  |
| TestMultipleTurns | class |  |
| TestToolExecutionSpan | class |  |
| TestAsyncInstrumentAgent | class |  |
| TestToolExecutionDictArguments | class |  |
| TestAsyncToolExecutionSpan | class |  |
| TestConversationSpanDictMessage | class |  |
| TestConversationSpanCostAndUsage | class |  |
| TestInstrumentResume | class |  |
| TestInstrumentRunChat | class |  |
| TestInstrumentInitiateChats | class |  |

## Chunks

### otel_setup (function, L21-L26)

> *Summary: This function initializes and configures OpenTelemetry components by creating an in-memory span exporter and a tracer provider. It returns both the configured exporter and the provider, allowing for capturing spans during testing.*


### TestInstrumentAgentBasic (class, L32-L69)

> *Summary: This test suite verifies the functionality of an instrumentation agent by asserting that it correctly wraps methods on a `ConversableAgent` instance using OpenTelemetry tracing. It confirms that the agent returns the original object and that key methods like `initiate_chat`, `generate_reply`, and others gain an `__otel_wrapped__` attribute after processing.*


### test_returns_same_agent (method, L35-L39, parent: TestInstrumentAgentBasic)

> *Summary: This test verifies that the `instrument_agent` function returns the exact same agent instance passed into it. It takes an initialized agent and a tracing provider as input to confirm identity preservation after instrumentation.*


### test_wraps_initiate_chat (method, L41-L45, parent: TestInstrumentAgentBasic)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps the `initiate_chat` method of a `ConversableAgent`. It asserts that the wrapped method now possesses an attribute indicating it has been instrumented by OpenTelemetry.*


### test_wraps_generate_reply (method, L47-L51, parent: TestInstrumentAgentBasic)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps the `generate_reply` method of a given agent instance with OpenTelemetry instrumentation. It asserts the presence of a specific attribute (`__otel_wrapped__`) on the wrapped method after instrumentation is applied.*


### test_wraps_a_generate_reply (method, L53-L57, parent: TestInstrumentAgentBasic)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps a specific method on an agent instance. It asserts that the target method now possesses an attribute indicating it has been instrumented with OpenTelemetry tracing.*


### test_wraps_execute_function (method, L59-L63, parent: TestInstrumentAgentBasic)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps the `execute_function` method on a given agent instance using OpenTelemetry tracing. It asserts the presence of a specific attribute (`__otel_wrapped__`) on the wrapped method to confirm instrumentation occurred.*


### test_wraps_get_human_input (method, L65-L69, parent: TestInstrumentAgentBasic)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps the `get_human_input` method of a conversational agent instance. It asserts the presence of an internal wrapper attribute on the method after instrumentation is applied.*


### TestInstrumentAgentIdempotency (class, L75-L100)

> *Summary: Verifies that applying the `instrument_agent` function multiple times to a `ConversableAgent` does not result in nested or double-wrapped methods. It confirms that subsequent instrumentation calls return references to the original, unmodified wrapped functions for key agent methods like `initiate_chat`, `generate_reply`, and `execute_function`.*


### test_double_instrument_does_not_double_wrap_initiate_chat (method, L78-L84, parent: TestInstrumentAgentIdempotency)

> *Summary: This test verifies that applying the instrumentation wrapper twice to an agent's `initiate_chat` method does not result in nested wrapping. It asserts that the function reference remains unchanged after the second application of `instrument_agent`.*


### test_double_instrument_does_not_double_wrap_generate_reply (method, L86-L92, parent: TestInstrumentAgentIdempotency)

> *Summary: This test verifies that applying the instrumentation logic twice to an agent does not result in nested wrappers for its `generate_reply` method. It asserts that the reference of the function remains unchanged after the second instrumentation call.*


### test_double_instrument_does_not_double_wrap_execute_function (method, L94-L100, parent: TestInstrumentAgentIdempotency)

> *Summary: This test verifies that applying the instrumentation logic twice to an agent does not result in nested wrappers for its `execute_function`. It asserts that the function reference remains unchanged after the second application of the instrumenter.*


### TestConversationSpan (class, L106-L196)

> *Summary: This test suite verifies that the `initiate_chat` method correctly generates and populates OpenTelemetry conversation spans when instrumented. It asserts specific attributes on these spans, such as span type, agent names, recorded input messages, output history, maximum turns, and total conversation turns.*


### test_initiate_chat_creates_conversation_span (method, L109-L126, parent: TestConversationSpan)

> *Summary: This test verifies that initiating a chat between two agents correctly generates at least one OpenTelemetry conversation span. It asserts the presence and specific attributes of this generated span, confirming proper instrumentation for the interaction.*


### test_initiate_chat_records_max_turns (method, L128-L141, parent: TestConversationSpan)

> *Summary: This test verifies that the OpenTelemetry instrumentation correctly records the `max_turns` parameter during a simulated chat interaction between two agents. It asserts that the resulting conversation span contains an attribute matching the specified maximum turn count of 1.*


### test_initiate_chat_records_input_message (method, L143-L164, parent: TestConversationSpan)

> *Summary: This test verifies that an agent's initial message is correctly captured as input within OpenTelemetry spans during a simulated chat interaction. It asserts that the conversation span attributes contain at least one message matching the expected "Hello world" content.*


### test_initiate_chat_records_chat_history_output (method, L166-L180, parent: TestConversationSpan)

> *Summary: This test verifies that initiating a chat between two agents correctly records the conversation history in OpenTelemetry spans. It asserts that the resulting span contains at least one message in its attributes after the interaction completes.*


### test_initiate_chat_records_conversation_turns (method, L182-L196, parent: TestConversationSpan)

> *Summary: This test verifies that when two agents engage in a single turn of chat, the OpenTelemetry instrumentation correctly records conversation spans. It asserts that the resulting span contains an attribute tracking the number of turns exchanged during the interaction.*


### TestAgentInvokeSpan (class, L202-L279)

> *Summary: These tests verify that the `instrument_agent` function correctly generates OpenTelemetry spans for conversational agents during chat interactions. It asserts that these generated spans contain specific attributes, such as operation names, input messages, and output messages, when an agent initiates a conversation with another.*


### test_generate_reply_creates_agent_span (method, L205-L218, parent: TestAgentInvokeSpan)

> *Summary: This test verifies that instrumenting two agents results in the creation of at least one agent-specific span during a simulated chat interaction. It initializes agents, wraps them in a testing context, calls the instrumentation function for both, and then asserts the presence of an `AGENT` type span from the exporter.*


### test_agent_span_attributes (method, L220-L237, parent: TestAgentInvokeSpan)

> *Summary: This test verifies that OpenTelemetry instrumentation correctly captures specific attributes on spans generated by two agents during a simulated chat interaction. It asserts the presence of expected tags, such as `ag2.span.type` and `gen_ai.operation.name`, on the recorded spans.*


### test_agent_span_captures_input_messages (method, L239-L258, parent: TestAgentInvokeSpan)

> *Summary: This test verifies that the instrumentation correctly captures input messages within OpenTelemetry spans generated by agents during a simulated chat interaction. It asserts that at least one relevant span exists and contains the `gen_ai.input.messages` attribute.*


### test_agent_span_captures_output_messages (method, L260-L279, parent: TestAgentInvokeSpan)

> *Summary: This test verifies that the instrumentation correctly captures output messages within OpenTelemetry spans generated during a chat interaction between two agents. It asserts that at least one span associated with the recipient contains the `gen_ai.output.messages` attribute after running the conversation.*


### TestSpanHierarchy (class, L285-L323)

> *Summary: This test class verifies that OpenTelemetry instrumentation correctly establishes the parent-child relationship between conversation and agent spans during a chat interaction. It asserts that all generated spans belong to a single trace ID and that individual agent actions are properly nested under the main conversation span.*


### test_agent_spans_are_children_of_conversation (method, L288-L308, parent: TestSpanHierarchy)

> *Summary: This test verifies that spans generated by agents during a chat session are correctly linked to the main conversation span within OpenTelemetry. It asserts that all recorded agent spans share the same `trace_id` as the initial conversation span, confirming proper parent-child relationship tracing.*


### test_all_spans_share_same_trace_id (method, L310-L323, parent: TestSpanHierarchy)

> *Summary: This test verifies that all generated OpenTelemetry spans share a consistent `trace_id` when two agents interact. It instruments both agents and asserts that the set of collected span trace IDs contains only one element after an initiated chat exchange.*


### TestMultipleTurns (class, L329-L345)

> *Summary: This test verifies multi-turn conversation tracing by setting up two agents and initiating a two-turn chat between them. It asserts that the OpenTelemetry exporter captures at least two agent invocation spans during the interaction.*


### test_two_turn_conversation (method, L332-L345, parent: TestMultipleTurns)

> *Summary: This test verifies that OpenTelemetry instrumentation correctly captures interaction spans during a two-turn conversation between two agents. It initiates a chat and asserts that the resulting exporter contains at least two spans tagged as agent activity.*


### TestToolExecutionSpan (class, L351-L451)

> *Summary: This test suite verifies that the `instrument_agent` function correctly generates OpenTelemetry spans when executing functions via a conversational agent. It asserts various aspects of these generated spans, including correct span types, metadata for tool names and arguments, call IDs, and recording success or failure results.*


### test_execute_function_creates_tool_span (method, L354-L377, parent: TestToolExecutionSpan)

> *Summary: This test verifies that executing a registered function via the agent correctly generates an OpenTelemetry span of type `TOOL`. It asserts that exactly one such span is created and contains specific attributes identifying the operation name, tool name, and tool type.*


### test_execute_function_records_arguments (method, L379-L395, parent: TestToolExecutionSpan)

> *Summary: This test verifies that when an agent executes a registered function, the arguments passed to that function are correctly recorded as attributes on the resulting OpenTelemetry span. It achieves this by executing a specific function call and asserting the presence of the argument key within the captured tool span's attributes.*


### test_execute_function_records_call_id (method, L397-L413, parent: TestToolExecutionSpan)

> *Summary: This test verifies that when a function is executed by an agent, the provided `call_id` is correctly recorded as an attribute on the resulting OpenTelemetry span. It sets up an agent, instruments it with tracing, executes a registered tool call with a specific ID, and asserts this ID appears in the captured spans.*


### test_execute_function_records_result_on_success (method, L415-L432, parent: TestToolExecutionSpan)

> *Summary: This test verifies that when an agent successfully executes a registered function, the resulting outcome is recorded in OpenTelemetry spans. It asserts that the span attributes contain the `gen_ai.tool.call.result` key after calling `agent.execute_function`.*


### test_execute_function_records_error_on_failure (method, L434-L451, parent: TestToolExecutionSpan)

> *Summary: This test verifies that when an agent executes a registered function that raises an exception, the OpenTelemetry instrumentation correctly records this failure. It asserts that the resulting span for the tool execution contains the `"ExecutionError"` attribute.*


### TestAsyncInstrumentAgent (class, L457-L507)

> *Summary: These asynchronous tests verify that instrumenting agents correctly generates OpenTelemetry spans during chat interactions. They assert the creation of specific span types (conversation and agent), check attribute values on those spans, and confirm all generated spans share a single trace ID for end-to-end tracing.*


### test_a_initiate_chat_creates_conversation_span (method, L461-L476, parent: TestAsyncInstrumentAgent)

> *Summary: This test verifies that initiating a chat between two agents correctly generates at least one OpenTelemetry conversation span. It asserts the presence and specific attributes of this generated span, confirming proper instrumentation during the interaction.*


### test_a_generate_reply_creates_agent_span (method, L479-L491, parent: TestAsyncInstrumentAgent)

> *Summary: This test verifies that instrumenting two agents results in the creation of at least one agent-specific span when a chat interaction is initiated between them. It uses an OpenTelemetry setup to capture and assert the presence of these spans after running the conversation logic.*


### test_async_all_spans_share_same_trace_id (method, L494-L507, parent: TestAsyncInstrumentAgent)

> *Summary: This test verifies that all generated spans from two agents share a single trace ID during an asynchronous chat interaction. It instruments both agents using the provided tracer provider and asserts that only one unique trace ID exists among the collected finished spans.*


### TestToolExecutionDictArguments (class, L513-L545)

> *Summary: Verifies that when a function call is passed with dictionary arguments instead of a JSON string, the tracing layer correctly serializes those arguments into a JSON string within the resulting span attributes. It confirms that even if the agent's internal execution fails due to incorrect input type, the tracing wrapper successfully captures and records the intended argument structure.*


### test_execute_function_with_dict_arguments_records_span (method, L516-L545, parent: TestToolExecutionDictArguments)

> *Summary: This test verifies that when a function call is passed with dictionary arguments, the tracing layer correctly serializes those arguments into JSON before recording them in the span attributes. It asserts that a tool span is created and contains the expected serialized argument structure, even if the agent's internal execution might fail due to parsing issues.*


### TestAsyncToolExecutionSpan (class, L551-L687)

> *Summary: This test suite verifies that the `a_execute_function` method correctly instruments asynchronous tool calls using OpenTelemetry. It asserts various aspects of the generated spans, including correct span type, operation name, recording input arguments (both JSON strings and dictionaries), capturing call IDs, logging successful results, and properly reporting execution errors.*


### test_a_execute_function_creates_tool_span (method, L555-L578, parent: TestAsyncToolExecutionSpan)

> *Summary: This test verifies that when an agent executes a registered asynchronous function, OpenTelemetry correctly generates and records a specific tool span. It asserts the presence of exactly one tool span with expected attributes detailing the executed tool name and operation.*


### test_a_execute_function_records_arguments (method, L581-L600, parent: TestAsyncToolExecutionSpan)

> *Summary: This test verifies that when an agent executes a registered function, the arguments passed during the call are correctly captured and recorded in the resulting OpenTelemetry span attributes. It asserts that the deserialized arguments from the span match the input dictionary provided to the execution method.*


### test_a_execute_function_records_call_id (method, L603-L619, parent: TestAsyncToolExecutionSpan)

> *Summary: This test verifies that when an agent executes a registered asynchronous function, the provided `call_id` is correctly recorded as an attribute on the resulting OpenTelemetry span. It achieves this by instrumenting the agent and asserting the presence of the specific ID in the captured tool span attributes.*


### test_a_execute_function_records_result_on_success (method, L622-L639, parent: TestAsyncToolExecutionSpan)

> *Summary: This test verifies that when an agent successfully executes a registered asynchronous function, the resulting outcome is correctly recorded as an attribute on the corresponding OpenTelemetry span. It asserts that the `gen_ai.tool.call.result` key exists within the captured tool span attributes after execution.*


### test_a_execute_function_error (method, L642-L659, parent: TestAsyncToolExecutionSpan)

> *Summary: This test verifies that when an agent executes a registered function that raises an error, the instrumentation correctly captures this failure. It asserts that the execution result indicates failure and that the corresponding OpenTelemetry span is marked with an `ExecutionError` attribute.*


### test_a_execute_function_with_dict_arguments (method, L662-L687, parent: TestAsyncToolExecutionSpan)

> *Summary: This test verifies that when a function call is provided with arguments as a Python dictionary, the tracing layer correctly serializes those arguments into JSON format before recording them in an OpenTelemetry span. It executes a registered async tool via an agent and asserts that the recorded arguments match the input dictionary structure.*


### TestConversationSpanDictMessage (class, L693-L734)

> *Summary: These tests verify that the `initiate_chat` and `a_initiate_chat` methods correctly record dictionary-formatted message inputs into OpenTelemetry spans. They pass a structured dictionary as an input message to two agents and assert that the content of this message is present in the recorded conversation span attributes.*


### test_initiate_chat_dict_message_records_input (method, L696-L714, parent: TestConversationSpanDictMessage)

> *Summary: This test verifies that when a chat is initiated with a dictionary message, the OpenTelemetry instrumentation correctly captures the input. It asserts that at least one conversation span exists and contains the expected "Hello from dict" content within its recorded input messages.*


### test_a_initiate_chat_dict_message_records_input (method, L717-L734, parent: TestConversationSpanDictMessage)

> *Summary: This test verifies that an agent correctly records a dictionary message as input when initiating a chat conversation. It asserts that the resulting OpenTelemetry spans contain the expected "Async dict msg" within the recorded input messages.*


### TestConversationSpanCostAndUsage (class, L740-L805)

> *Summary: These tests verify that initiating a chat between two agents correctly records specific metadata within OpenTelemetry spans. The functions execute agent interactions and assert the presence of `gen_ai.conversation.id` and `gen_ai.usage.cost` attributes on the resulting conversation span.*


### test_initiate_chat_records_chat_id (method, L743-L757, parent: TestConversationSpanCostAndUsage)

> *Summary: This test verifies that an OpenTelemetry instrumentation correctly captures a conversation ID when two agents initiate a chat. It sets up two agents, instruments them using the provided tracer provider, and asserts that the resulting conversation span contains a non-empty `gen_ai.conversation.id` attribute.*


### test_initiate_chat_records_cost (method, L759-L772, parent: TestConversationSpanCostAndUsage)

> *Summary: This test verifies that the OpenTelemetry instrumentation correctly captures cost metrics during a simulated chat interaction between two agents. It asserts that the resulting conversation span contains an attribute for `gen_ai.usage.cost`.*


### test_a_initiate_chat_records_chat_id (method, L775-L789, parent: TestConversationSpanCostAndUsage)

> *Summary: This test verifies that initiating a chat between two agents correctly records the conversation ID within OpenTelemetry spans. It sets up agents, instruments them with an agent tracer provider, runs a single-turn chat, and asserts the presence of a non-empty `gen_ai.conversation.id` attribute on the resulting conversation span.*


### test_a_initiate_chat_records_cost (method, L792-L805, parent: TestConversationSpanCostAndUsage)

> *Summary: This test verifies that the cost metric is recorded for a simulated chat interaction between two agents. It instruments both agents with OpenTelemetry and asserts that the resulting conversation span contains the `gen_ai.usage.cost` attribute after initiating a single-turn chat.*


### TestInstrumentResume (class, L811-L868)

> *Summary: These tests verify the instrumentation of `a_resume` within a `GroupChatManager`. They confirm that the agent's resume method is correctly wrapped with OpenTelemetry tracing, ensuring idempotency and that resumed conversations generate spans marked as `resumed=True`.*


### test_wraps_a_resume (method, L814-L823, parent: TestInstrumentResume)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps the `a_resume` method of a `GroupChatManager`. It achieves this by creating a manager instance and asserting the presence of an OpenTelemetry wrapper attribute on the target method.*


### test_resume_idempotent (method, L825-L836, parent: TestInstrumentResume)

> *Summary: This test verifies that applying instrumentation twice to a `GroupChatManager` does not result in duplicate wrapping of the `a_resume` method. It achieves this by instrumenting the manager, capturing the original method reference, and then re-instrumenting before asserting the references remain identical.*


### test_a_resume_creates_conversation_span_with_resumed (method, L839-L868, parent: TestInstrumentResume)

> *Summary: This test verifies that when an agent resumes a conversation, the instrumentation correctly creates a `CONVERSATION` span. It mocks the resume method and asserts that the resulting span includes specific attributes indicating the operation name, agent name, and that the conversation was resumed (`gen_ai.conversation.resumed=True`).*


### TestInstrumentRunChat (class, L874-L1094)

> *Summary: This test suite verifies that instrumenting a `GroupChatManager` correctly wraps its `run_chat` and `a_run_chat` methods with OpenTelemetry tracing capabilities. It asserts that these wrapped methods create conversation spans, capture input messages from the call arguments, and record output messages from the configuration object.*


### test_wraps_run_chat (method, L877-L885, parent: TestInstrumentRunChat)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps the `run_chat` method of a `GroupChatManager`. It achieves this by setting up an agent chat environment and asserting the presence of a specific wrapper attribute on the manager's run method.*


### test_wraps_a_run_chat (method, L887-L895, parent: TestInstrumentRunChat)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps a chat execution method on a `GroupChatManager`. It achieves this by creating a manager and asserting the presence of an `__otel_wrapped__` attribute on its `a_run_chat` method after instrumentation.*


### test_run_chat_idempotent (method, L897-L907, parent: TestInstrumentRunChat)

> *Summary: This test verifies that running a chat session multiple times yields the same object reference by instrumenting the `GroupChatManager` with OpenTelemetry tracing. It executes the chat process twice and asserts that the returned chat instance from both calls is identical.*


### test_run_chat_creates_conversation_span (method, L909-L947, parent: TestInstrumentRunChat)

> *Summary: This test verifies that running a chat session correctly generates an OpenTelemetry conversation span. It mocks the chat execution and then asserts that one specific conversation span is created, contains expected attributes like operation name and agent name, and accurately captures the initial input messages provided to the system.*


### test_run_chat_captures_output_from_config (method, L949-L977, parent: TestInstrumentRunChat)

> *Summary: This test verifies that the instrumentation correctly captures chat output messages from a provided configuration during group chat execution. It mocks the chat manager's run method and asserts that the resulting OpenTelemetry span contains at least two message objects in its attributes.*


### test_run_chat_no_messages_no_input_attr (method, L979-L1001, parent: TestInstrumentRunChat)

> *Summary: This test verifies that when running a chat with no messages and no input attributes, the OpenTelemetry instrumentation does not record any `gen_ai.input.messages` attribute on the conversation span. It mocks the chat execution to isolate and assert this specific behavior during tracing.*


### test_run_chat_no_config_messages_no_output_attr (method, L1003-L1026, parent: TestInstrumentRunChat)

> *Summary: This test verifies that when running a chat with no configuration messages, the resulting OpenTelemetry span does not contain the `gen_ai.output.messages` attribute. It mocks the chat execution and asserts the absence of this specific attribute on the conversation span after calling the instrumenting function.*


### test_a_run_chat_creates_conversation_span (method, L1029-L1064, parent: TestInstrumentRunChat)

> *Summary: This test verifies that calling `a_run_chat` on a chat manager correctly generates an OpenTelemetry conversation span. It asserts that the resulting span exists, has the correct operation name and agent name, and accurately captures the initial input messages provided to the method.*


### test_a_run_chat_captures_output (method, L1067-L1094, parent: TestInstrumentRunChat)

> *Summary: This test verifies that the `a_run_chat` method captures conversation output using OpenTelemetry instrumentation. It mocks the chat execution and then asserts that the resulting span attributes contain at least two messages from the mocked configuration.*


### TestInstrumentInitiateChats (class, L1100-L1349)

> *Summary: These tests verify the OpenTelemetry instrumentation for `initiate_chats` and `a_initiate_chats` methods on a conversational agent. They confirm that these functions correctly wrap calls, create multi-conversation spans (sequential or parallel), and accurately record metadata like recipients, chat IDs, summaries, and prerequisites into the generated traces.*


### test_wraps_initiate_chats (method, L1103-L1107, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps methods on a given agent instance. It asserts that the `initiate_chats` method now possesses an `__otel_wrapped__` attribute after instrumentation.*


### test_wraps_a_initiate_chats (method, L1109-L1113, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that the `instrument_agent` function successfully wraps a method on a `ConversableAgent` instance. It asserts that the target method, `a_initiate_chats`, gains an attribute indicating it has been instrumented with OpenTelemetry tracing.*


### test_initiate_chats_idempotent (method, L1115-L1121, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that instrumenting an agent with OpenTelemetry tracing does not alter the agent's `initiate_chats` method reference when called twice. It initializes a conversational agent, instruments it once, and then calls the instrumentation again before asserting the method object remains unchanged.*


### test_initiate_chats_creates_multi_conversation_span (method, L1123-L1157, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that calling `initiate_chats` on an agent correctly generates a single multi-conversation OpenTelemetry span. It asserts that this span accurately reflects the operation name, agent name, and the count and sequential mode of the initiated chats based on mocked results.*


### test_initiate_chats_records_recipients (method, L1159-L1188, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that when initiating chats, the OpenTelemetry instrumentation correctly records the names of all recipients involved. It mocks chat initiation and asserts that the resulting multi-conversation span attributes contain a list including both expected recipient names ("alice" and "bob").*


### test_initiate_chats_records_chat_ids_and_summaries (method, L1190-L1217, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that when a conversational agent initiates chats, the OpenTelemetry instrumentation correctly records the resulting chat IDs and summaries within a multi-conversation span. It mocks the initiation process to assert that specific data points are present in the captured span attributes.*


### test_a_initiate_chats_creates_multi_conversation_span (method, L1220-L1255, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that when a `ConversableAgent` initiates multiple chats concurrently, it generates a single OpenTelemetry multi-conversation span. It mocks the chat initiation process to simulate two parallel conversations and asserts the resulting span correctly reflects the operation name, count (2), and mode ("parallel").*


### test_a_initiate_chats_records_recipients (method, L1258-L1287, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that when initiating chats, the system correctly records all recipient names within an OpenTelemetry span. It mocks chat initiation calls and asserts that the resulting multi-conversation span attributes contain the expected list of recipient identifiers.*


### test_a_initiate_chats_records_chat_ids_and_summaries (method, L1290-L1317, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that when a conversational agent initiates chats, the resulting chat IDs and summaries are correctly recorded as attributes on an OpenTelemetry span. It mocks the initiation process to ensure these specific values appear in the final collected spans.*


### test_a_initiate_chats_records_prerequisites (method, L1320-L1349, parent: TestInstrumentInitiateChats)

> *Summary: This test verifies that the `a_initiate_chats` method records chat prerequisites as an OpenTelemetry attribute when processing a queue of chats. It mocks agent interactions and asserts that the resulting multi-conversation span contains the expected prerequisite data for specific chats.*

