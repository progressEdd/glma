# test/beta/config/openai/test_builtin_tool_events.py

2 function(s): _process, test_process_response_routes_all_item_types. 2 class(es): TestReasoning, TestResultParts. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _process | function |  |
| test_process_response_routes_all_item_types | function |  |
| TestReasoning | class |  |
| TestResultParts | class |  |

## Chunks

### _process (function, L54-L66)

> *Summary: This asynchronous function simulates processing an iterable of model outputs by constructing a mock `Response` object and passing it to a test client. It returns the processed response along with a list of generated events captured from an in-memory stream.*


### test_process_response_routes_all_item_types (function, L70-L141)

> *Summary: This test verifies the system's ability to process a mixed batch of tool call and response events, including web search, code execution, image generation, and standard messages. It asserts that the final aggregated response correctly reflects the message content, pending function calls, and generated files, while also validating the sequence of emitted server-side event notifications.*


### TestReasoning (class, L145-L239)

> *Summary: These asynchronous tests verify the serialization and persistence logic for OpenAI reasoning events. They ensure that reasoning items are correctly recorded in history, map accurately to the Responses API input format across various scenarios (e.g., multiple summaries, empty summaries), and handle item deduplication when generating API payloads.*


### test_persisted_in_history (method, L146-L162, parent: TestReasoning)

> *Summary: This test verifies that an `OpenAIReasoningEvent` is correctly persisted into the event history when sent through a memory stream. It confirms that after sending the reasoning event with specific content, the stream's history contains exactly one entry matching the input event.*


### test_round_trips_to_responses_api_input (method, L164-L189, parent: TestReasoning)

> *Summary: This test verifies that a list of OpenAI-related events (reasoning, tool call, and tool result) correctly transforms into the expected API input structure. It asserts that the resulting `api_input` matches the serialized representations of the initial reasoning and web search items.*


### test_emits_one_event_per_summary (method, L191-L206, parent: TestReasoning)

> *Summary: This test verifies that processing a single reasoning item containing multiple summaries results in an equal number of emitted events. It asserts that the output list contains one `OpenAIReasoningEvent` for each summary provided in the input item.*


### test_empty_summary_emits_anchor_event (method, L208-L219, parent: TestReasoning)

> *Summary: When processing a `ResponseReasoningItem` with an empty summary, the system emits an `OpenAIReasoningEvent` containing an empty string as the summary. This ensures that items lacking summary text are still persisted correctly for round-trip consistency.*


### test_per_summary_events_serialise_item_once (method, L221-L239, parent: TestReasoning)

> *Summary: This test verifies that when multiple events reference the same underlying item, the serialization process correctly deduplicates it by ID to prevent API rejection. It takes a list of `OpenAIReasoningEvent` objects sharing one `ResponseReasoningItem` and asserts the resulting input contains only a single instance of that item's data.*


### TestResultParts (class, L243-L490)

> *Summary: This class contains several asynchronous test methods that validate how different tool call and result objects (like web search actions or code interpreter outputs) are transformed into structured `OpenAIServerToolCallEvent` and `OpenAIServerToolResultEvent` streams when processed by an internal function. It ensures correct serialization of inputs, metadata, and specific data types like URLs or binary content based on the tool's nature.*


### test_web_search_search_action_without_sources_is_metadata_only (method, L244-L266, parent: TestResultParts)

> *Summary: This test verifies that when a web search action is processed without source inclusion, the resulting events contain only metadata in the tool result. It asserts that the output sequence includes an initial `ToolCallEvent` followed by a `ToolResultEvent` where the result payload contains only descriptive metadata.*


### test_web_search_search_action_emits_url_inputs_from_sources (method, L268-L303, parent: TestResultParts)

> *Summary: This test verifies that a `ResponseFunctionWebSearch` object correctly emits specific events when processed. It asserts the output contains both an initial tool call event and a subsequent result event, where the result includes URL inputs derived from the original search sources.*


### test_web_search_search_action_skips_sources_with_empty_url (method, L305-L330, parent: TestResultParts)

> *Summary: This test verifies that when a web search action is provided with a source having an empty URL, the processing correctly generates tool call and result events without incorrectly converting the `None` URL into a `UrlInput(None)`. It asserts the resulting sequence of OpenAI server tool events matches expectations for a completed search.*


### test_web_search_open_page_emits_url (method, L332-L354, parent: TestResultParts)

> *Summary: This test verifies that a `ResponseFunctionWebSearch` object, representing an action to open a specific URL, correctly emits both a tool call event and a subsequent tool result event. It asserts the emitted events match expected structures containing the provided URL in the result payload.*


### test_web_search_find_in_page_emits_url_and_pattern (method, L356-L378, parent: TestResultParts)

> *Summary: This test verifies that a `ResponseFunctionWebSearch` object, representing a completed in-page search action on a specific URL with a pattern, correctly emits both an initial tool call event and a subsequent tool result event. The output asserts the structure of these events, including the provided URL and metadata from the action.*


### test_code_interpreter_logs_emit_text_input (method, L380-L401, parent: TestResultParts)

> *Summary: This test verifies that processing a `ResponseCodeInterpreterToolCall` correctly emits two specific events: an initial tool call event and a subsequent tool result event containing the text output. It asserts that these emitted events match expected structures derived from the input code execution details.*


### test_code_interpreter_image_emits_url_input (method, L403-L427, parent: TestResultParts)

> *Summary: This test verifies that processing a `code_interpreter_call` containing an image output correctly generates two sequential events: a tool call event and a subsequent tool result event. The resulting tool result event must contain the provided URL as a `UrlInput`.*


### test_code_interpreter_outputs_none_empty_parts (method, L429-L448, parent: TestResultParts)

> *Summary: This test verifies that processing a code interpreter call with no outputs correctly generates specific tool events. It asserts the resulting list contains both the initial tool call event and a subsequent tool result event indicating failure for the given input structure.*


### test_image_generation_emits_binary_input (method, L450-L472, parent: TestResultParts)

> *Summary: This test verifies that processing an `ImageGenerationCall` results in a sequence of events: first, a tool call event, followed by a tool result event containing the image data as binary input. It confirms the structure and content of these emitted events match expectations for successful image generation.*


### test_image_generation_response_files_share_bytes (method, L474-L490, parent: TestResultParts)

> *Summary: This test verifies that the image data within a generated response shares bytes with the corresponding event result. It simulates an image generation call and asserts that the `response.files` data matches the data found in the processed tool result event.*

