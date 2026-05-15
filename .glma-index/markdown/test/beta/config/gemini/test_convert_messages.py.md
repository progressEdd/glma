# test/beta/config/gemini/test_convert_messages.py

8 function(s): _model_response_with_tool_call, test_image_url, test_image_binary, test_audio_url, test_audio_binary, test_document_url, test_document_binary, test_video_binary. 7 class(es): TestConvertMessagesEmptyArguments, TestVideoUrl, TestVendorMetadata, TestAudioFormatVariants, TestMultipleInputs, TestToolResult, TestBuiltinToolEventReplay. 25 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _model_response_with_tool_call | function |  |
| TestConvertMessagesEmptyArguments | class |  |
| test_image_url | function |  |
| test_image_binary | function |  |
| test_audio_url | function |  |
| test_audio_binary | function |  |
| test_document_url | function |  |
| test_document_binary | function |  |
| TestVideoUrl | class |  |
| test_video_binary | function |  |
| TestVendorMetadata | class |  |
| TestAudioFormatVariants | class |  |
| TestMultipleInputs | class |  |
| TestToolResult | class |  |
| TestBuiltinToolEventReplay | class |  |

## Chunks

### _model_response_with_tool_call (function, L33-L39)

> *Summary: Constructs a `ModelResponse` object that contains no message but includes a single tool call event named "list\_items" with the provided arguments. This helper is used to simulate a model response that requires external function execution.*


### TestConvertMessagesEmptyArguments (class, L42-L60)

> *Summary: This test suite verifies that the message conversion utility handles empty or `None` tool call arguments gracefully, ensuring it produces a dictionary with empty arguments. It also confirms that valid JSON string arguments are correctly parsed and preserved in the output structure.*


### test_empty_arguments_produce_empty_dict (method, L46-L52, parent: TestConvertMessagesEmptyArguments)

> *Summary: When provided with no arguments, this test asserts that the message conversion process results in a dictionary containing a model role and an empty function call argument structure. It verifies the output structure when the input `arguments` parameter is null or empty.*


### test_valid_arguments_are_preserved (method, L54-L60, parent: TestConvertMessagesEmptyArguments)

> *Summary: This test verifies that when converting a message containing a tool call, the original arguments are correctly preserved in the output structure. It takes a model response with a specific function call and asserts the resulting content matches the expected dictionary format.*


### test_image_url (function, L63-L70)

> *Summary: This test verifies that an input containing a URL for an image is correctly transformed into the expected structured format. It takes a list of messages with an `ImageInput` and asserts the resulting content matches the specified dictionary structure, including the file URI and MIME type.*


### test_image_binary (function, L73-L80)

> *Summary: This test verifies that a raw binary image input is correctly processed by the message conversion utility. It takes a list containing an `ImageInput` object with PNG data and asserts the resulting structure matches the expected API format.*


### test_audio_url (function, L83-L90)

> *Summary: This test verifies that an input containing a URL pointing to an audio file is correctly transformed into the expected structured message format. It asserts that the output includes the original audio URL and its MIME type within the `parts` section of the user role message.*


### test_audio_binary (function, L93-L100)

> *Summary: This test verifies that an input containing raw binary audio data is correctly transformed into the expected structured message format. It asserts that the output dictionary accurately reflects the original audio bytes and MIME type within the `parts` field of a user role message.*


### test_document_url (function, L103-L110)

> *Summary: This test verifies that a document URL input is correctly transformed into the expected message structure for model consumption. It takes a list containing a `DocumentInput` with a PDF URL and asserts the output matches a user role message containing the file URI and MIME type.*


### test_document_binary (function, L113-L120)

> *Summary: This test verifies that a binary PDF input is correctly processed by the message conversion utility. It asserts that the output structure accurately represents the raw byte data and MIME type within the expected model format.*


### TestVideoUrl (class, L123-L140)

> *Summary: This test suite verifies the `convert_messages` function's behavior when processing video URLs. It asserts that a known file extension results in a specific MIME type being included, while a YouTube URL omits the MIME type entirely.*


### test_known_extension (method, L124-L131, parent: TestVideoUrl)

> *Summary: This test verifies that a video URL input is correctly converted into the expected structured message format. It takes a list containing a `VideoInput` object with a specific URL and asserts the resulting content matches the predefined structure for user parts.*


### test_youtube_url_has_no_mime_type (method, L133-L140, parent: TestVideoUrl)

> *Summary: This test verifies that a YouTube URL, when passed as video input to the message conversion process, results in an output structure containing only the original URI under `file_data`. It confirms the serialization correctly handles URLs without explicit MIME types.*


### test_video_binary (function, L143-L150)

> *Summary: This test verifies that a raw binary video input is correctly transformed into the expected structured message format. It takes a byte string representing video data and asserts the resulting content matches the structure containing `inline_data` with the correct MIME type.*


### TestVendorMetadata (class, L153-L212)

> *Summary: These tests verify that various vendor metadata provided in a `BinaryInput` is correctly transformed and included when converting messages using `convert_messages`. It asserts the resulting structure contains the original media data alongside any specified metadata fields like resolution, video details, or display names.*


### test_media_resolution (method, L156-L172, parent: TestVendorMetadata)

> *Summary: This test verifies that a specific vendor metadata tag (`media_resolution`) provided in a `BinaryInput` is correctly preserved and reflected within the output message structure after conversion. It asserts that the resulting content dictionary contains the original resolution tag alongside the inline image data.*


### test_video_metadata_dict (method, L174-L190, parent: TestVendorMetadata)

> *Summary: This test verifies that a `BinaryInput` containing video data and specific vendor metadata is correctly transformed by the message conversion process. It asserts that the output structure accurately reflects the input, converting integer FPS to float while preserving other metadata fields within the model dump.*


### test_display_name (method, L192-L203, parent: TestVendorMetadata)

> *Summary: This test verifies that a binary input containing vendor metadata for a display name is correctly transformed into the expected structure within the model output. It takes a `BinaryInput` with a specified `display_name` and asserts the resulting message content includes this name under `inline_data`.*


### test_empty_metadata_is_noop (method, L205-L212, parent: TestVendorMetadata)

> *Summary: When provided with an input containing only image data and no metadata, the conversion process should return a message structure identical to the original user request parts. This test verifies that empty metadata results in no change during serialization.*


### TestAudioFormatVariants (class, L215-L227)

> *Summary: This test verifies that when converting messages containing inline audio data, the specified MIME type is correctly preserved across different audio formats (WAV, MPEG, OGG). It takes a list of requests with audio input and asserts the resulting message structure contains the original media type.*


### test_inline_audio_preserves_media_type (method, L219-L227, parent: TestAudioFormatVariants)

> *Summary: This test verifies that when an audio input with a specific `media_type` is passed to the message conversion utility, the resulting content correctly retains both the audio data and its original MIME type in the output structure. It asserts the final dictionary representation matches the expected format containing inline audio data.*


### TestMultipleInputs (class, L230-L272)

> *Summary: This test suite verifies the `convert_messages` function's ability to correctly serialize various input combinations into a standardized message format. It checks scenarios where multiple inputs (text and URLs) are grouped together, and when text is mixed with raw binary image data.*


### test_multiple_inputs_grouped_into_one_content (method, L231-L252, parent: TestMultipleInputs)

> *Summary: This test verifies that multiple inputs—a text prompt and two image URLs—are correctly consolidated into a single structured content object. It asserts the resulting dictionary matches the expected format containing the user role, text part, and separate file data parts for each provided URL.*


### test_mixed_text_and_binary (method, L254-L272, parent: TestMultipleInputs)

> *Summary: This test verifies that a list containing both text and binary image data is correctly processed by `convert_messages`. It asserts the resulting structure matches the expected format for multimodal input, including separate entries for text and inline image data.*


### TestToolResult (class, L275-L446)

> *Summary: This test suite verifies the `convert_messages` function's behavior when transforming various tool result inputs into a standardized message format for Gemini. It confirms correct serialization for text, mixed content (text and media), and handles specific unsupported input types by raising exceptions.*


### test_text_only_goes_into_response (method, L283-L290, parent: TestToolResult)

> *Summary: When provided with a `ToolResultsEvent` containing a single tool result, this test asserts that the message conversion process correctly formats the output as a user role message containing the function response details. The input event is transformed into a structured dictionary representing the model's expected response format.*


### test_multiple_text_chunks_become_list (method, L292-L299, parent: TestToolResult)

> *Summary: When provided with a `ToolResultsEvent` containing multiple tool results, this test verifies that the message conversion process transforms these into a list within the output structure. The function takes an event and returns a structured content object reflecting the aggregated results.*


### test_url_image (method, L301-L318, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing an image URL input is correctly converted into a structured message format expected by the model. It asserts that the output contains the user role and a function response detailing the provided file URI and MIME type.*


### test_binary_image (method, L320-L343, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing binary image data is correctly converted into the expected structured message format for an API call. It asserts that the output includes the image data nested within a function response part, tagged with the correct MIME type.*


### test_url_document (method, L345-L362, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing a URL document input is correctly converted into a structured message format suitable for Gemini. It asserts the resulting content matches an expected dictionary structure, specifically showing the function response with file data referencing the provided PDF URL.*


### test_binary_document (method, L364-L387, parent: TestToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing binary PDF data is correctly converted into the expected message format for Gemini. It asserts that the output structure includes the function response with the embedded PDF data under `inline_data`.*


### test_mixed_text_and_image (method, L389-L412, parent: TestToolResult)

> *Summary: This test verifies the message conversion process when an input event contains both text and image data. It takes a `ToolResultsEvent` with an image URL as input and asserts that the resulting content structure correctly represents this mixed media within the expected API format.*


### test_url_audio_raises (method, L414-L419, parent: TestToolResult)

> *Summary: This test verifies that attempting to convert a message containing an audio input from a URL using the specified serializer raises an `UnsupportedInputError` when processing with Gemini. It achieves this by passing an event containing an `AudioInput` object pointing to a remote WAV file.*


### test_url_video_raises (method, L421-L426, parent: TestToolResult)

> *Summary: This test verifies that attempting to convert messages containing a video URL input using the specified serializer raises an `UnsupportedInputError` when processing with Gemini. It achieves this by passing a `ToolResultsEvent` containing a `VideoInput` object to the conversion function and asserting the expected exception is raised.*


### test_binary_audio_raises (method, L428-L439, parent: TestToolResult)

> *Summary: This test verifies that attempting to process a message containing binary audio data using the specified serializer raises an `UnsupportedInputError`. It achieves this by passing a `ToolResultsEvent` with raw byte audio input to the conversion function.*


### test_file_id_raises (method, L441-L446, parent: TestToolResult)

> *Summary: When provided with a `ToolResultsEvent` containing a `FileIdInput`, the conversion process is expected to raise an `UnsupportedInputError` specifically mentioning Gemini. This test verifies that file ID inputs are correctly rejected during message serialization.*


### TestBuiltinToolEventReplay (class, L449-L488)

> *Summary: Tests verify how a message conversion function processes sequences of tool events. It confirms that executable code parts are correctly appended to existing model content, paired execution results stack into a single model content block, and grounding-only events are entirely skipped during conversion.*


### test_executable_code_part_appended_to_existing_model_content (method, L450-L458, parent: TestBuiltinToolEventReplay)

> *Summary: This test verifies that an executable code part appended to existing model content is correctly converted by the `convert_messages` function. It takes a sequence of events, including a tool call event containing Python code, and asserts the output is a single model content object holding that code part.*


### test_code_execution_pair_stacks_into_one_model_content (method, L460-L474, parent: TestBuiltinToolEventReplay)

> *Summary: This test verifies that a sequence of tool call and subsequent tool result events correctly aggregates into a single model content object. It takes a list containing an executable code request and its corresponding execution output as input, asserting the output is a unified `Content` message with both parts.*


### test_grounding_only_events_are_skipped (method, L476-L488, parent: TestBuiltinToolEventReplay)

> *Summary: When provided with a sequence containing only tool call and corresponding tool result events that include grounding metadata, the function asserts that no output is generated. This test verifies that events solely related to grounding are correctly filtered out during message conversion.*

