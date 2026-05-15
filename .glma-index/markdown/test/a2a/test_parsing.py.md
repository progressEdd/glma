# test/a2a/test_parsing.py

1 function(s): _artifact_event. 10 class(es): TestMessageToPart, TestMessageFromPart, TestRequestMessageToA2A, TestRequestMessageFromA2A, TestResponseMessageFromA2AArtifacts, TestResponseMessageFromA2ATask, TestResponseMessageFromA2AMessage, TestResponseMessageToA2A, TestUpdateArtifactToStreaming, TestRoundTripConversions. 36 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMessageToPart | class |  |
| TestMessageFromPart | class |  |
| TestRequestMessageToA2A | class |  |
| TestRequestMessageFromA2A | class |  |
| TestResponseMessageFromA2AArtifacts | class |  |
| TestResponseMessageFromA2ATask | class |  |
| TestResponseMessageFromA2AMessage | class |  |
| TestResponseMessageToA2A | class |  |
| _artifact_event | function |  |
| TestUpdateArtifactToStreaming | class |  |
| TestRoundTripConversions | class |  |

## Chunks

### TestMessageToPart (class, L38-L65)

> *Summary: This test suite verifies the `message_to_part` conversion utility by asserting that input dictionaries are correctly transformed into `TextPart` objects. It covers cases with simple text, messages including metadata like role and name, and edge cases where content is empty, null, or missing.*


### test_simple_text_message (method, L39-L42, parent: TestMessageToPart)

> *Summary: This test verifies that a simple dictionary containing text content is correctly converted into a `TextPart` object. It asserts the resulting part matches an expected instance with the provided text.*


### test_message_with_metadata (method, L44-L50, parent: TestMessageToPart)

> *Summary: This test verifies that a dictionary containing message content and metadata correctly transforms into a `TextPart` object. It asserts the resulting part has the correct text content and the associated metadata dictionary.*


### test_message_to_part_without_content (method, L60-L65, parent: TestMessageToPart)

> *Summary: This test verifies that a given `message` object correctly transforms into a `TextPart` with empty content and specific metadata. It asserts the resulting structure matches an expected `TextPart` instance.*


### TestMessageFromPart (class, L68-L95)

> *Summary: This test suite verifies the `message_from_part` function's ability to convert different types of `Part` objects into structured messages. It confirms correct parsing for text parts (with and without metadata), raw data parts, and specialized data parts containing AI results.*


### test_text_part_without_metadata (method, L69-L73, parent: TestMessageFromPart)

> *Summary: Given a `Part` containing only a `TextPart`, this test verifies that the conversion function produces a dictionary with the text content under the `"content"` key. The expected output is `{"content": "Test content"}` for the input part.*


### test_text_part_to_message (method, L75-L79, parent: TestMessageFromPart)

> *Summary: This test verifies that a `Part` containing a `TextPart` correctly transforms into a standard message dictionary. It asserts the output matches the expected structure: role and content extracted from the input part.*


### test_data_part_to_message (method, L81-L87, parent: TestMessageFromPart)

> *Summary: This test verifies that a `Part` object, constructed from a dictionary-like structure wrapped in `DataPart`, correctly converts into its original dictionary content when passed to `message_from_part`. It asserts the resulting message matches the input data.*


### test_data_part_with_pydantic_ai_result (method, L89-L95, parent: TestMessageFromPart)

> *Summary: This test verifies that a `Part` object containing specific data is correctly transformed into a dictionary representation. It asserts that the resulting message accurately reflects the input data structure, specifically extracting the answer value.*


### TestRequestMessageToA2A (class, L98-L127)

> *Summary: This test verifies the conversion of a `RequestMessage` containing multiple messages and context into an A2A `Message`. It asserts that the resulting A2A message correctly encapsulates all input content, roles, provided context, and client tools.*


### test_request_with_multiple_messages (method, L99-L127, parent: TestRequestMessageToA2A)

> *Summary: This test verifies the conversion of a `RequestMessage` containing multiple user and assistant messages into an A2A `Message`. It asserts that the resulting A2A message correctly encapsulates all input content, context data, and client tool definitions.*


### TestRequestMessageFromA2A (class, L130-L159)

> *Summary: This test suite verifies the `request_message_from_a2a` function by converting mock A2A messages into structured request objects. It confirms correct transformation for both simple text content and complex messages containing metadata like context and client tools.*


### test_simple_a2a_to_request (method, L131-L140, parent: TestRequestMessageFromA2A)

> *Summary: This test verifies that a simple `Message` object, containing user text, is correctly transformed into a `RequestMessage`. It asserts the resulting structure matches an expected list of content dictionaries.*


### test_a2a_complete_message (method, L142-L159, parent: TestRequestMessageFromA2A)

> *Summary: This test verifies the conversion of a structured `Message` object into a simplified `RequestMessage`. It takes an input message containing text and metadata, asserting that the output correctly maps the content and extracts specific context and tool definitions.*


### TestResponseMessageFromA2AArtifacts (class, L162-L230)

> *Summary: This test suite verifies the `response_message_from_a2a_artifacts` function by testing various inputs of artifacts. It asserts correct output for single-artifact scenarios (including context), handles null or empty artifact lists by returning `None`, and validates error conditions for multiple artifacts or specific part configurations.*


### test_response_message_from_a2a_none_cases (method, L171-L173, parent: TestResponseMessageFromA2AArtifacts)

> *Summary: When provided with `None` for the input artifacts, this test asserts that the function returns `None`. It verifies the expected behavior when no artifact data is supplied to generate a response message.*


### test_single_artifact_single_part (method, L175-L185, parent: TestResponseMessageFromA2AArtifacts)

> *Summary: This test verifies that a list containing one artifact, which itself has a single text part, correctly translates into a specific `ResponseMessage` structure. It confirms the parsing logic accurately extracts the content from the input artifact to form the output message.*


### test_artifact_with_context (method, L187-L199, parent: TestResponseMessageFromA2AArtifacts)

> *Summary: This test verifies that a specific artifact, containing text content and associated metadata, is correctly processed by the A2A response mechanism. It asserts that the resulting `ResponseMessage` accurately reflects both the artifact's content and its contextual data.*


### test_multiple_artifacts_raises_error (method, L201-L216, parent: TestResponseMessageFromA2AArtifacts)

> *Summary: This test verifies that the `response_message_from_a2a_artifacts` function raises a `NotImplementedError` when provided with a list containing more than one artifact. It asserts this error message specifically mentions that multiple artifacts are unsupported.*


### test_multiple_parts_raises_error (method, L218-L230, parent: TestResponseMessageFromA2AArtifacts)

> *Summary: When provided with an artifact containing multiple distinct parts, the function is expected to return a response message listing each part's content separately. This test verifies that the system correctly processes and enumerates all constituent parts of a single artifact input.*


### TestResponseMessageFromA2ATask (class, L233-L320)

> *Summary: This test suite verifies the `response_message_from_a2a_task` function by providing various `Task` objects as input. It asserts that the function correctly generates a `ResponseMessage`, handling cases where input is required (with or without history), tasks are completed with artifacts, and tasks are completed with artifact metadata for context extraction.*


### test_task_input_required_with_history (method, L234-L254, parent: TestResponseMessageFromA2ATask)

> *Summary: When provided a `Task` object in the `input_required` state with existing history, this test verifies that the function returns a `ResponseMessage` containing the prompt from the last agent message and sets the `input_required` field accordingly. This confirms correct handling of tasks awaiting user input while maintaining conversation context.*


### test_task_input_required_with_empty_history (method, L256-L267, parent: TestResponseMessageFromA2ATask)

> *Summary: When provided a `Task` object in the "input\_required" state with no history or artifacts, this test asserts that the system returns a specific `ResponseMessage` indicating that user input is needed.*


### test_task_completed_with_artifacts (method, L269-L285, parent: TestResponseMessageFromA2ATask)

> *Summary: This test verifies that a task marked as completed, which includes an artifact containing the text "Task completed," correctly generates a specific `ResponseMessage`. It takes a constructed `Task` object as input and asserts the resulting message structure.*


### test_task_completed_with_no_artifacts (method, L287-L298, parent: TestResponseMessageFromA2ATask)

> *Summary: When provided with a `Task` object already marked as completed and containing no artifacts, the function returns `None`. This test verifies that the A2A processing correctly handles such a state without generating any response message.*


### test_task_completed_with_artifact_context (method, L300-L320, parent: TestResponseMessageFromA2ATask)

> *Summary: This test verifies that a task marked as completed, which includes an artifact containing specific text and metadata, correctly generates a response message. It asserts the output matches the expected structure, including the content from the artifact and the session context provided in its metadata.*


### TestResponseMessageFromA2AMessage (class, L323-L412)

> *Summary: This test suite verifies the `response_message_from_a2a_message` function by providing various `Message` inputs. It asserts that the function correctly transforms different combinations of text, data parts, and metadata into a structured `ResponseMessage`.*


### test_empty_message (method, L324-L332, parent: TestResponseMessageFromA2AMessage)

> *Summary: When provided with a `Message` object containing no parts, the function returns a `ResponseMessage` whose internal message list is empty. This tests the expected behavior for handling an entirely empty input message structure.*


### test_single_text_part (method, L334-L342, parent: TestResponseMessageFromA2AMessage)

> *Summary: When provided with a `Message` containing a single text part, the function transforms it into a `ResponseMessage` structure where the content is extracted from that text. This verifies correct parsing of simple agent messages.*


### test_multiple_text_parts (method, L344-L356, parent: TestResponseMessageFromA2AMessage)

> *Summary: This test verifies that a message containing multiple distinct text parts is correctly aggregated into a single string within the resulting response. It takes a `Message` object with separate text components and asserts the output contains them concatenated with newline characters.*


### test_single_data_part (method, L358-L368, parent: TestResponseMessageFromA2AMessage)

> *Summary: When provided with a `Message` containing a single data part, this test verifies that the conversion function correctly transforms it into a `ResponseMessage` structure where the input data is present in the messages list. The expected output mirrors the content of the input's `DataPart`.*


### test_mixed_text_and_data_parts (method, L370-L383, parent: TestResponseMessageFromA2AMessage)

> *Summary: This test verifies that a message containing both text and structured data parts is correctly transformed. It takes an input `Message` object with mixed content and asserts the output matches a specific `ResponseMessage` structure containing separate entries for the text and data.*


### test_multiple_data_parts (method, L385-L398, parent: TestResponseMessageFromA2AMessage)

> *Summary: This test verifies that a message containing multiple distinct data parts is correctly transformed. It takes an input `Message` with two separate `DataPart`s and asserts the output `ResponseMessage` contains both associated data dictionaries in its list of messages.*


### test_message_with_context (method, L400-L412, parent: TestResponseMessageFromA2AMessage)

> *Summary: This test verifies that a specific message structure, containing context metadata, is correctly transformed into a `ResponseMessage`. It asserts the output matches an expected response object populated with the original session ID from the input's context.*


### TestResponseMessageToA2A (class, L415-L435)

> *Summary: This test suite verifies how a response message is converted into an `Artifact` object. It checks two scenarios: one where the input message is `None`, and another where both content and context are provided in the input.*


### test_none_response (method, L416-L424, parent: TestResponseMessageToA2A)

> *Summary: This test verifies that when an input message is `None`, the resulting artifact structure contains no parts and has a default name of "result". It asserts equality against a newly constructed artifact object using the generated ID.*


### test_response_with_context (method, L426-L435, parent: TestResponseMessageToA2A)

> *Summary: This test verifies that an artifact created from a message and context correctly structures its output. It asserts the resulting `Artifact` object contains the message content in its parts and the provided context within its metadata.*


### _artifact_event (function, L438-L439)

> *Summary: Creates a namespace object containing the provided `Artifact` instance and an optional boolean indicating if it's the final chunk. This helper structures artifact data for subsequent processing steps.*


### TestUpdateArtifactToStreaming (class, L442-L522)

> *Summary: This test suite verifies the `update_artifact_to_streaming` function's behavior when processing different artifact part types. It confirms that text and data parts correctly yield streamed content, handles missing data gracefully, and respects the `last_chunk` flag to control output.*


### test_text_part_yields_stream_event (method, L443-L453, parent: TestUpdateArtifactToStreaming)

> *Summary: This test verifies that a text part within an artifact correctly generates a stream event when processed by `update_artifact_to_streaming`. It asserts that the resulting list of records contains one item with the content matching the input text.*


### test_data_part_yields_content_from_data (method, L455-L465, parent: TestUpdateArtifactToStreaming)

> *Summary: This test verifies that the `update_artifact_to_streaming` function correctly extracts content from a data part within an artifact event. It asserts that the resulting list of updated artifacts contains the expected content payload.*


### test_data_part_missing_content_yields_empty_string (method, L467-L477, parent: TestUpdateArtifactToStreaming)

> *Summary: When an artifact part lacks content, the streaming update function processes it to yield a list containing a single record with an empty string content. This test verifies that missing data results in an empty content payload being returned during the stream processing.*


### test_last_chunk_true_yields_nothing (method, L479-L489, parent: TestUpdateArtifactToStreaming)

> *Summary: When processing an artifact event marked as the final chunk, this test verifies that the streaming update function yields no results. It confirms that `list()` conversion of the output is an empty list when provided with a complete artifact structure.*


### test_last_chunk_none_yields_nothing (method, L491-L502, parent: TestUpdateArtifactToStreaming)

> *Summary: When processing an artifact event where the `last_chunk` is explicitly set to `None`, the streaming update function yields no results. This test confirms that providing `None` for the last chunk correctly results in an empty output list.*


### test_multiple_parts_yields_multiple_events (method, L504-L522, parent: TestUpdateArtifactToStreaming)

> *Summary: This test verifies that an artifact containing multiple distinct parts (text, text, and data) correctly yields a sequence of separate events when processed by the streaming update function. It asserts that each part is transformed into its own event structure in the resulting list.*


### TestRoundTripConversions (class, L525-L536)

> *Summary: This test verifies that converting a `RequestMessage` to an A2A format and then back results in the original message being perfectly reconstructed. It uses a sample request containing user content, context data, and client tools as input for this round-trip assertion.*


### test_request_round_trip (method, L526-L536, parent: TestRoundTripConversions)

> *Summary: This test verifies the bidirectional serialization of a `RequestMessage` structure. It takes an initial message object, converts it to an A2A format using a generated UUID, and then converts it back, asserting that the final object matches the original input exactly.*

