# test/beta/config/anthropic/test_convert_messages.py

11 function(s): _model_response_with_tool_call, _matching_tool_result, test_full_sequence_with_empty_args, test_image_url_input_converts_to_url_block, test_document_url_input_converts_to_url_block, test_multiple_inputs_grouped_into_one_message, test_unsupported_input_raises, _server_tool_use_block, _web_search_result_block, test_full_sequence_round_trip and 1 more. 8 class(es): TestConvertMessagesEmptyArguments, TestImageBinaryInput, TestDocumentBinaryInput, TestFileIdInput, TestToolResult, TestAnthropicServerToolCallEvent, TestAnthropicServerToolResultEvent, TestUnsupportedInputs. 32 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _model_response_with_tool_call | function |  |
| _matching_tool_result | function |  |
| TestConvertMessagesEmptyArguments | class |  |
| test_full_sequence_with_empty_args | function |  |
| test_image_url_input_converts_to_url_block | function |  |
| TestImageBinaryInput | class |  |
| test_document_url_input_converts_to_url_block | function |  |
| TestDocumentBinaryInput | class |  |
| TestFileIdInput | class |  |
| test_multiple_inputs_grouped_into_one_message | function |  |
| TestToolResult | class |  |
| test_unsupported_input_raises | function |  |
| _server_tool_use_block | function |  |
| _web_search_result_block | function |  |
| TestAnthropicServerToolCallEvent | class |  |
| TestAnthropicServerToolResultEvent | class |  |
| test_full_sequence_round_trip | function |  |
| test_code_execution_subtool_preserves_block_shape | function |  |
| TestUnsupportedInputs | class |  |

## Chunks

### _model_response_with_tool_call (function, L45-L52)

> *Summary: Constructs a `ModelResponse` object that exclusively contains one tool call event. It accepts an optional string of arguments to populate the specified tool call's parameters.*


### _matching_tool_result (function, L55-L65)

> *Summary: Creates a `ToolResultsEvent` containing a single `ToolResultEvent` for the "list\_items" tool, using the provided string content as the result. This helper ensures that tool usage results are not lost when testing interactions.*


### TestConvertMessagesEmptyArguments (class, L68-L95)

> *Summary: This test suite verifies that the message conversion logic correctly handles various inputs for tool call arguments. It asserts that providing empty strings, `None`, or an empty JSON object results in a tool use input dictionary being empty, while valid JSON arguments are preserved.*


### test_empty_arguments_produce_empty_dict (method, L72-L79, parent: TestConvertMessagesEmptyArguments)

> *Summary: When provided with no arguments, this test verifies that the message conversion process results in a specific partial dictionary structure. It calls a helper function to generate a response and then converts it using `convert_messages` against a predefined tool result.*


### test_valid_arguments_are_preserved (method, L81-L87, parent: TestConvertMessagesEmptyArguments)

> *Summary: This test verifies that valid arguments are correctly preserved when converting messages. It takes a mock model response and a matching tool result, passing them to the conversion function which should return a specific structured message format.*


### test_empty_object_arguments (method, L89-L95, parent: TestConvertMessagesEmptyArguments)

> *Summary: When provided with a model response containing an empty tool call input and a matching tool result, this test asserts that the message conversion correctly structures the output to reflect the partial dictionary state. The function takes a list of responses and a serializer class as input, returning the converted messages.*


### test_full_sequence_with_empty_args (function, L98-L123)

> *Summary: This test verifies that a sequence involving an initial user request, followed by a model response containing a tool call, and finally the corresponding tool results converts correctly. It asserts that the resulting message list accurately reflects these three distinct event types in order.*


### test_image_url_input_converts_to_url_block (function, L126-L135)

> *Summary: This test verifies that an input containing an image URL within a `ModelRequest` is correctly transformed into a structured JSON output. It asserts the resulting message content includes a `"type": "image"` with a `"source"` block specifying the provided URL.*


### TestImageBinaryInput (class, L138-L207)

> *Summary: This test suite verifies the `convert_messages` function's behavior when processing image inputs. It asserts that binary data is correctly encoded to Base64, and it validates specific rules for how vendor metadata (like merging cache control or filtering filenames) is handled during serialization.*


### test_converts_to_image_base64_block (method, L141-L157, parent: TestImageBinaryInput)

> *Summary: This test verifies that a list containing an image input is correctly transformed into the Anthropic message format. It asserts that the output structure contains a user role with content specifying the image as base64 encoded data.*


### test_vendor_metadata_cache_control_merges (method, L159-L179, parent: TestImageBinaryInput)

> *Summary: This test verifies that vendor metadata, specifically `cache_control`, is correctly merged when converting a list of model requests into the target message format. It asserts that an input image with ephemeral cache control results in the same structure within the output user content.*


### test_vendor_metadata_filename_filtered_out (method, L181-L207, parent: TestImageBinaryInput)

> *Summary: This test verifies that vendor metadata, specifically the filename, is stripped out when converting a list of model requests containing binary image data. It asserts that the resulting structure contains only the base64 encoded image data and media type, omitting any extra metadata.*


### test_document_url_input_converts_to_url_block (function, L210-L219)

> *Summary: When provided with a document URL in the input, this test verifies that the message conversion process transforms it into a structured JSON object representing a URL block within the user's content. The function takes a list containing a `DocumentInput` with a URL and asserts the output matches the expected serialized format.*


### TestDocumentBinaryInput (class, L222-L263)

> *Summary: This test suite verifies the serialization of binary document inputs into API message formats. It confirms that raw bytes are correctly encoded to Base64 and that associated vendor metadata is properly merged into the resulting structure.*


### test_converts_to_document_base64_block (method, L225-L241, parent: TestDocumentBinaryInput)

> *Summary: This test verifies that a list of model requests containing PDF data is correctly transformed into a specific JSON structure. It asserts the output matches a user role message containing a base64-encoded document block with the correct media type.*


### test_vendor_metadata_merges (method, L243-L263, parent: TestDocumentBinaryInput)

> *Summary: This test verifies that vendor metadata is correctly merged when converting a message containing binary input. It takes a list of `ModelRequest` objects with specific metadata and asserts the output matches the expected structure, including the preserved metadata within the content.*


### TestFileIdInput (class, L266-L321)

> *Summary: This test suite verifies the `convert_messages` function's behavior when processing file inputs for Anthropic models. It asserts that the conversion correctly distinguishes between image and document content based on provided filenames, handles provider-specific errors, and successfully processes matching providers.*


### test_no_filename_defaults_to_document (method, L269-L277, parent: TestFileIdInput)

> *Summary: When provided with a `FileIdInput` without an explicit filename, this test verifies that the message conversion correctly defaults the content type to `"document"` and includes the file ID in the source metadata. The function takes a list of model requests containing a single file input and asserts the output matches the expected structured JSON format.*


### test_image_filename_uses_image_block (method, L279-L289, parent: TestFileIdInput)

> *Summary: This test verifies that a message containing a file ID and filename is correctly transformed into the Anthropic API format. It takes a `ModelRequest` with a file input and asserts the output matches the expected structure using an image block referencing the file ID.*


### test_pdf_filename_uses_document_block (method, L291-L301, parent: TestFileIdInput)

> *Summary: This test verifies that when converting a message containing a file reference, the output correctly structures the content as a document block referencing the provided `file_id`. It takes a list of model requests with a file input and asserts the resulting structured message format.*


### test_foreign_provider_raises (method, L303-L308, parent: TestFileIdInput)

> *Summary: This test asserts that attempting to convert messages containing an OpenAI file reference when using the Anthropic serializer raises an `UnsupportedInputError`. It verifies the error message specifically mentions both 'openai' and 'anthropic'.*


### test_matching_provider_passes (method, L310-L321, parent: TestFileIdInput)

> *Summary: This test verifies that the `convert_messages` function correctly transforms a list containing an Anthropic file request into the expected structured message format. It asserts that the output matches a specific dictionary structure representing a user role with document content referencing the provided file ID.*


### test_multiple_inputs_grouped_into_one_message (function, L324-L345)

> *Summary: This test verifies that multiple text and image inputs provided within a single `ModelRequest` are correctly serialized into a unified message structure for the Anthropic API format. It asserts the output matches a list containing one user role message with an array of content parts, including both text and URL-based images.*


### TestToolResult (class, L348-L580)

> *Summary: This test suite verifies the `convert_messages` function's ability to serialize various types of tool results into a standardized message format. It tests inputs including plain text, binary images/documents (via base64), remote URLs for media, and file IDs, ensuring correct output structure for each case while also asserting that unsupported audio inputs raise an error.*


### test_text_only_stays_string (method, L353-L362, parent: TestToolResult)

> *Summary: When provided with a `ToolResultsEvent` containing a single text-based tool result, this test verifies that the message conversion process correctly transforms it into a list containing a user role object with a string content type. The input event is converted to a specific JSON structure representing the tool output.*


### test_binary_image (method, L364-L393, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing binary image data is correctly converted into the Anthropic message format. It asserts that the input PNG data is encoded to Base64 and structured within a user role content block as an image type.*


### test_url_image (method, L395-L418, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing an image URL input is correctly transformed into the expected JSON message format for Anthropic API calls. It asserts that the output structure accurately represents the tool result, including the image source type and URL.*


### test_mixed_text_and_image (method, L420-L446, parent: TestToolResult)

> *Summary: This test verifies that a mixed input containing both text and an image within a tool result event is correctly converted. It asserts the resulting structure matches the expected format, including separate entries for text and image content types.*


### test_binary_document (method, L448-L478, parent: TestToolResult)

> *Summary: This test verifies that a binary document input, provided within a `ToolResultsEvent`, is correctly converted into a structured JSON message format. It asserts the output matches an expected structure containing base64-encoded data for the PDF file under the "document" type.*


### test_url_document (method, L480-L498, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing a URL document input is correctly transformed into a structured message format. It asserts the output matches a specific JSON structure representing the user's tool result, including the original URL source.*


### test_file_id_image (method, L500-L523, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing a file ID input is correctly transformed into a structured message format. It asserts the output matches a user role message containing an image content block referencing the provided file ID.*


### test_file_id_document (method, L525-L548, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing a file ID input is correctly transformed into a structured message format. It asserts the output matches a user role message containing a document content type referencing the provided file ID.*


### test_file_id_no_filename_defaults_to_document (method, L550-L567, parent: TestToolResult)

> *Summary: When provided with a `ToolResultsEvent` containing a file ID without an associated filename, this test asserts that the message conversion correctly maps it to a document type within the output structure. The function takes a list of events and returns a list of structured messages representing the tool result.*


### test_audio_in_tool_result_raises (method, L569-L580, parent: TestToolResult)

> *Summary: When provided with a `ToolResultsEvent` containing an audio input within a tool result, the conversion process is expected to raise an `UnsupportedInputError`. This test verifies that binary audio data from Anthropic tools triggers this specific exception during message serialization.*


### test_unsupported_input_raises (function, L613-L615)

> *Summary: This test verifies that passing an unsupported input to the message conversion process correctly raises an `UnsupportedInputError`. It achieves this by calling `convert_messages` with a specific model request generated by the provided factory and asserting the expected exception.*


### _server_tool_use_block (function, L618-L629)

> *Summary: Creates a `ServerToolUseBlock` instance representing a tool invocation request. It accepts an optional ID and name, defaulting the input to a dictionary containing a "bitcoin price" query if none is provided.*


### _web_search_result_block (function, L632-L641)

> *Summary: Constructs a `WebSearchToolResultBlock` instance to represent the outcome of a web search tool call. It accepts an optional `tool_use_id` and a list of `content`, defaulting to an empty list if no content is provided.*


### TestAnthropicServerToolCallEvent (class, L644-L679)

> *Summary: This test suite verifies how a specific event type is transformed during message conversion. It asserts that tool call events are correctly wrapped as assistant content, either as the sole content or appended to existing text within an assistant message.*


### test_emits_wrapped_sdk_block_as_assistant_content (method, L645-L659, parent: TestAnthropicServerToolCallEvent)

> *Summary: This test verifies that a server tool use block is correctly transformed into an assistant role content when processed by the message conversion utility. It takes a list containing one `AnthropicServerToolCallEvent` as input and asserts the output matches a specific structure where the block's serialized data forms the assistant's content.*


### test_appends_to_existing_assistant_message (method, L661-L679, parent: TestAnthropicServerToolCallEvent)

> *Summary: This test verifies that when a model response containing an initial message and subsequent tool call events are processed, the resulting structure correctly merges the text content with the full details of the associated tool use block. It confirms the output format includes both the assistant's initial text and the serialized tool call information within the same message object.*


### TestAnthropicServerToolResultEvent (class, L682-L723)

> *Summary: These tests verify how tool use events are converted into structured message formats for Anthropic. Specifically, they confirm that a single tool result block is wrapped as assistant content, and that sequential tool call and result blocks stack together within one assistant message.*


### test_emits_wrapped_sdk_block_as_assistant_content (method, L683-L697, parent: TestAnthropicServerToolResultEvent)

> *Summary: This test verifies that a specific tool result event, containing a wrapped SDK block, is correctly serialized into an assistant role message. It asserts the output matches a list containing one dictionary with the "assistant" role and the block's JSON representation as content.*


### test_call_and_result_blocks_stack_into_one_assistant_message (method, L699-L723, parent: TestAnthropicServerToolResultEvent)

> *Summary: This test verifies that a sequence of tool call and subsequent result events are correctly consolidated into a single assistant message structure. It takes a list containing an `AnthropicServerToolCallEvent` and an `AnthropicServerToolResultEvent` as input, asserting the output is one message object containing both blocks in its content array.*


### test_full_sequence_round_trip (function, L726-L756)

> *Summary: This test verifies a complete message sequence round-trip by simulating user input, tool calls (like web search), tool results, and subsequent model responses. It asserts that the `convert_messages` function correctly transforms this complex event stream into a standardized list of structured messages.*


### test_code_execution_subtool_preserves_block_shape (function, L798-L822)

> *Summary: This test verifies that converting a pair of tool call and result events preserves the original block structure when serialized for Anthropic's code execution tool. It asserts that the resulting message content accurately reflects the input `ServerToolUseBlock` and `Any` result blocks.*


### TestUnsupportedInputs (class, L825-L851)

> *Summary: This test suite verifies that the message conversion function correctly raises an `UnsupportedInputError` when provided with unsupported media types like audio or video inputs, whether supplied as URLs or raw binary data for Anthropic models. It asserts specific error messages based on the type of unsupported input encountered during serialization.*


### test_audio_url_raises (method, L826-L828, parent: TestUnsupportedInputs)

> *Summary: Asserts that attempting to convert messages containing an audio URL input using the specified serializer raises an `UnsupportedInputError` specific to Anthropic's handling of audio URLs. This test verifies correct error handling when encountering unsupported media types in the input data structure.*


### test_video_url_raises (method, L830-L832, parent: TestUnsupportedInputs)

> *Summary: Asserts that attempting to convert messages containing a video URL input using `SerializerCls` raises an `UnsupportedInputError`. This test verifies the system correctly rejects unsupported media types like videos when processing model requests.*


### test_audio_binary_raises (method, L834-L836, parent: TestUnsupportedInputs)

> *Summary: Asserts that attempting to convert messages containing raw binary audio data using the specified serializer raises an `UnsupportedInputError` with a specific message. This tests the system's rejection of unsupported binary input formats for Anthropic models.*


### test_video_binary_raises (method, L838-L840, parent: TestUnsupportedInputs)

> *Summary: Asserts that attempting to convert messages containing raw video binary data using the specified serializer raises an `UnsupportedInputError` with a specific message. This tests the system's rejection of unsupported binary input types for Anthropic models.*


### test_generic_binary_raises (method, L842-L851, parent: TestUnsupportedInputs)

> *Summary: Asserts that attempting to convert messages containing a generic binary input with an octet stream type raises an `UnsupportedInputError` when using the Anthropic serializer. This test verifies correct error handling for unsupported binary data types during message conversion.*

