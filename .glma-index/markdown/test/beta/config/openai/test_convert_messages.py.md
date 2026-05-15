# test/beta/config/openai/test_convert_messages.py

1 function(s): test_data_input_in_model_request_becomes_input_text. 9 class(es): TestTextInput, TestImageUrlInput, TestFileIdInput, TestAudioUrlInput, TestAudioBinaryInput, TestBinaryInput, TestDocumentUrlInput, TestDocumentBinaryInput, TestResponsesToolResult. 36 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTextInput | class |  |
| TestImageUrlInput | class |  |
| TestFileIdInput | class |  |
| TestAudioUrlInput | class |  |
| TestAudioBinaryInput | class |  |
| TestBinaryInput | class |  |
| TestDocumentUrlInput | class |  |
| TestDocumentBinaryInput | class |  |
| test_data_input_in_model_request_becomes_input_text | function |  |
| TestResponsesToolResult | class |  |

## Chunks

### TestTextInput (class, L30-L61)

> *Summary: This test suite verifies the message conversion logic by asserting correct transformations from various input formats to standardized output structures. It specifically checks how text-only, mixed text/image inputs, and empty inputs are serialized into structured messages for model requests.*


### test_completions (method, L31-L34, parent: TestTextInput)

> *Summary: This test verifies the message conversion process by taking an empty list of messages and a specific model request containing a single user input. It asserts that the resulting output correctly formats the input into a standard dictionary structure for the user role.*


### test_responses (method, L36-L39, parent: TestTextInput)

> *Summary: This test verifies that a list of model requests containing user input is correctly transformed into the expected structured response format. It asserts that an input request with text "hello" yields a specific JSON-like structure representing the user's message.*


### test_completions_text_with_image_url (method, L41-L61, parent: TestTextInput)

> *Summary: This test verifies that a `ModelRequest` containing both text and an image URL is correctly transformed into a single user message structure. It asserts the output matches a specific JSON format, ensuring the content array properly nests both text and image URL objects.*


### TestImageUrlInput (class, L64-L83)

> *Summary: This test suite verifies message conversion logic for image inputs, specifically checking how an `ImageInput` object with a URL is transformed into both completion request formats and response structures. It asserts that the input URL correctly populates the corresponding fields in the serialized output messages.*


### test_completions (method, L67-L73, parent: TestImageUrlInput)

> *Summary: This test verifies the message conversion process by taking an empty list of messages and a request containing only an image input, asserting that the output correctly formats the user role with an embedded image URL structure.*


### test_responses (method, L75-L83, parent: TestImageUrlInput)

> *Summary: This test verifies that a list containing an image input request is correctly transformed into the expected OpenAI message format. It asserts that the output structure matches a user role with content specifying an `input_image` type and URL.*


### TestFileIdInput (class, L86-L149)

> *Summary: This test suite verifies how file ID inputs are correctly converted into message formats for different APIs. It asserts that when converting requests, the `filename` parameter is ignored or rejected depending on the target API's specific requirements (e.g., completions vs. responses).*


### test_completions (method, L89-L95, parent: TestFileIdInput)

> *Summary: This test verifies that an empty message list, when combined with a request containing a file ID input, correctly transforms into a user role message structure containing the specified file object. The function asserts the resulting dictionary matches the expected format for file-based user content.*


### test_completions_filename_forbidden_with_file_id (method, L97-L106, parent: TestFileIdInput)

> *Summary: This test verifies that the message conversion process correctly omits the `filename` when a `file_id` is provided in the input structure. It asserts that the resulting user message contains only the `file_id`, not both the ID and filename.*


### test_responses (method, L108-L116, parent: TestFileIdInput)

> *Summary: This test verifies that a list containing a model request with a file ID input correctly converts into the expected OpenAI message format. It asserts that the output structure matches a user role message containing an `input_file` content type referencing the provided file ID.*


### test_responses_with_filename_ignores_filename (method, L118-L129, parent: TestFileIdInput)

> *Summary: This test verifies that when converting a message input containing both a `file_id` and a `filename`, the resulting structure correctly omits the filename, adhering to the API's mutual exclusivity rule for file identifiers. It takes a list of model requests with file inputs and asserts the output matches the expected format using only the `file_id`.*


### test_responses_foreign_provider_raises (method, L131-L136, parent: TestFileIdInput)

> *Summary: Asserts that passing a request containing an Anthropic file provider to the message conversion function raises an `UnsupportedInputError` when using the OpenAI serializer class. This verifies correct error handling for unsupported external providers during serialization.*


### test_responses_matching_provider_passes (method, L138-L149, parent: TestFileIdInput)

> *Summary: This test verifies that a list containing a model request with an uploaded file from OpenAI correctly transforms into the expected structured message format. It asserts that the output matches a specific dictionary structure representing a user role with an input file content type.*


### TestAudioUrlInput (class, L152-L161)

> *Summary: This test suite verifies that attempting to process audio input provided via a URL fails when using OpenAI completion and response serialization methods. It asserts that `UnsupportedInputError` is raised for both scenarios when an audio URL is supplied as input.*


### test_completions_raises (method, L155-L157, parent: TestAudioUrlInput)

> *Summary: Asserts that attempting to convert an empty message list with a request containing audio URL input raises an `UnsupportedInputError` specifically mentioning "UrlInput" and "audio" when using OpenAI completions. This verifies the system correctly rejects unsupported audio inputs during message serialization for completion requests.*


### test_responses_raises (method, L159-L161, parent: TestAudioUrlInput)

> *Summary: Asserts that passing a request containing an audio URL as input to the conversion function raises an `UnsupportedInputError` specifically mentioning "UrlInput" and "audio" when using OpenAI responses serialization. This verifies the system correctly rejects unsupported media types in the input structure.*


### TestAudioBinaryInput (class, L164-L187)

> *Summary: This test suite verifies the `convert_messages` function's ability to correctly transform audio inputs into a standardized message format. It asserts that raw binary audio data, provided with different MIME types (like WAV or MP3), is encoded in Base64 and structured within the expected user content object.*


### test_completions (method, L167-L176, parent: TestAudioBinaryInput)

> *Summary: This test verifies the `convert_messages` function by passing an empty list and a request containing audio input. It asserts that the resulting message structure correctly encodes the raw audio bytes into a base64 string within a user role content block.*


### test_completions_mp3 (method, L178-L187, parent: TestAudioBinaryInput)

> *Summary: This test verifies that an empty message list combined with a single audio input request correctly transforms the audio data into a base64-encoded user content structure. It asserts that the resulting output matches the expected format containing the encoded MP3 bytes.*


### TestBinaryInput (class, L190-L309)

> *Summary: This test suite verifies the serialization of various image and binary inputs into different message formats, such as chat completions and responses. It confirms that raw byte data, file paths, and vendor metadata are correctly encoded into base64 URLs or specific structured fields without leaking sensitive information like filenames where unintended.*


### test_completions (method, L193-L202, parent: TestBinaryInput)

> *Summary: This test verifies that the `convert_messages` function correctly transforms an input containing raw image bytes into a structured message format. It asserts that the output includes a user role with content specifying an image URL encoded in base64.*


### test_completions_with_vendor_metadata (method, L204-L224, parent: TestBinaryInput)

> *Summary: This test verifies that image data sent with vendor metadata is correctly transformed into the OpenAI message format. It takes an empty list of messages and a request containing a PNG image with specific metadata, asserting the output structure matches the expected user role content including the base64 encoded URL and the original detail level.*


### test_completions_image_path_no_vendor_leak (method, L226-L237, parent: TestBinaryInput)

> *Summary: This test verifies that when an `ImageInput` is provided with a local file path, the resulting message structure contains only the base64-encoded image data and does not leak vendor metadata like the original filename. It takes an empty list of messages and a request containing one image input as input, returning the serialized message content for assertion.*


### test_responses (method, L239-L251, parent: TestBinaryInput)

> *Summary: This test verifies that a list of model requests containing an image input is correctly transformed into the expected OpenAI message format. It asserts that the output structure matches a user role with content specifying an `input_image` type and a base64-encoded URL for the provided sample bytes.*


### test_responses_image_path_no_vendor_leak (method, L253-L270, parent: TestBinaryInput)

> *Summary: This test verifies that when an `ImageInput` referencing a local file path is processed, the resulting message structure embeds the image data as a base64-encoded URI rather than leaking the original file path. It takes a list of model requests containing an image input and asserts the output matches the expected format with embedded data.*


### test_responses_image_with_detail (method, L272-L288, parent: TestBinaryInput)

> *Summary: This test verifies that when an input image includes vendor metadata specifying a "high" detail level, the conversion process correctly embeds this detail information into the resulting response structure. It takes a list containing a single binary image input with specific metadata and asserts the output reflects this embedded detail.*


### test_responses_document_with_vendor_metadata (method, L290-L309, parent: TestBinaryInput)

> *Summary: This test verifies that a list of model requests containing binary input with vendor metadata is correctly transformed into the expected response format. It asserts that the output structure accurately reflects the user role and includes the file's filename within the content.*


### TestDocumentUrlInput (class, L312-L327)

> *Summary: This test class verifies how document URLs are handled during message conversion for OpenAI interactions. It asserts that attempting to use a URL input in completions raises an error, while successfully converting the same URL into the expected `input_file` structure within a response.*


### test_completions_raises (method, L315-L317, parent: TestDocumentUrlInput)

> *Summary: This test asserts that attempting to convert messages when the input contains a URL document for OpenAI completions raises an `UnsupportedInputError`. It verifies this by calling the conversion function with empty message inputs and a request containing a URL-based document.*


### test_responses (method, L319-L327, parent: TestDocumentUrlInput)

> *Summary: This test verifies that a list of document inputs, when processed by `events_to_responses_input`, correctly transforms into the expected OpenAI message format containing a user role and file URL content. It asserts the resulting structure matches a specific dictionary representation.*


### TestDocumentBinaryInput (class, L330-L366)

> *Summary: These tests verify how binary document inputs are processed by `convert_messages`. They assert that the resulting message content correctly embeds the base64-encoded file data and either infers a filename from the media type or uses a provided vendor metadata filename.*


### test_completions_infers_filename_from_media_type (method, L333-L344, parent: TestDocumentBinaryInput)

> *Summary: This test verifies that the message conversion utility correctly infers a filename when provided with media type information for file inputs. It takes sample bytes and a PDF media type as input to assert the resulting structure contains the correct base64-encoded data prefixed with the appropriate MIME type and a hardcoded filename.*


### test_completions_uses_vendor_metadata_filename (method, L346-L366, parent: TestDocumentBinaryInput)

> *Summary: This test verifies that the message conversion process correctly incorporates vendor metadata from a binary input into the output structure. It takes an empty list of messages and a request containing a PDF with custom filename metadata, asserting the resulting user content includes this filename.*


### test_data_input_in_model_request_becomes_input_text (function, L369-L378)

> *Summary: This test verifies that a `DataInput` object within a model request is correctly serialized into the `input_text` format in the resulting response structure. It confirms that the input data, specifically `{"key":"value"}`, becomes a JSON string under the `"content"` field with type `"input_text"`.*


### TestResponsesToolResult (class, L381-L588)

> *Summary: This test suite verifies the serialization logic for converting various tool result inputs (text, images, files, etc.) into a standardized response format. It ensures that different input types—like binary data, URLs, or simple strings—are correctly mapped to corresponding structured output blocks (`input_image`, `input_file`, etc.) when processed by `events_to_responses_input`.*


### test_text_only_stays_string (method, L384-L388, parent: TestResponsesToolResult)

> *Summary: When provided with a `ToolResultsEvent` containing a text-only tool result, this test asserts that the conversion process yields a list containing a single dictionary representing the function call output with the original string value.*


### test_image_binary_becomes_input_image_block (method, L390-L410, parent: TestResponsesToolResult)

> *Summary: This test verifies that raw binary image data, provided within a `ToolResultsEvent`, is correctly transformed into an OpenAI-compatible input image block. It asserts the resulting structure contains a base64-encoded URL pointing to the original PNG data.*


### test_image_url_becomes_input_image_block (method, L412-L430, parent: TestResponsesToolResult)

> *Summary: This test verifies that an `ImageInput` object containing a URL within a tool result event is correctly transformed into a structured JSON output block for the model. It takes a specific `ToolResultsEvent` as input and asserts the resulting list of responses matches the expected format, including the image URL under `"type": "input_image"`.*


### test_document_url_becomes_input_file_url_block (method, L432-L451, parent: TestResponsesToolResult)

> *Summary: This test verifies that a `DocumentInput` containing a URL is correctly transformed into an `input_file` structure with the same URL when processed by the event-to-response converter. It confirms the API output format expects a file URL instead of handling the original document URL directly.*


### test_document_binary_becomes_input_file_with_filename (method, L453-L473, parent: TestResponsesToolResult)

> *Summary: This test verifies that a binary document input is correctly transformed into an API-compatible `input_file` structure. It takes a `DocumentInput` containing raw PDF bytes and asserts the output includes both the base64 encoded data URI and a required filename.*


### test_document_binary_uses_vendor_filename (method, L475-L501, parent: TestResponsesToolResult)

> *Summary: This test verifies that a custom filename provided in `vendor_metadata` within a binary tool result is correctly preserved when converting the event to an OpenAI-compatible response format. It asserts that the output structure contains an `input_file` object with the expected filename.*


### test_file_id_becomes_input_file_block (method, L503-L522, parent: TestResponsesToolResult)

> *Summary: This test verifies that when a `ToolResult` provides both a `file_id` and a `filename`, the resulting API response correctly extracts only the `file_id` into an `input_file` block. It confirms the system adheres to the API constraint where only the file ID is accepted for input files.*


### test_mixed_text_and_image (method, L524-L549, parent: TestResponsesToolResult)

> *Summary: This test verifies that a mixed input containing both text and an image correctly transforms into the OpenAI API's required structure. It takes a `ToolResultsEvent` with combined text and image data as input and asserts the output is a list of function call outputs containing separate `input_text` and `input_image` objects.*


### test_data_input_with_image_url (method, L551-L575, parent: TestResponsesToolResult)

> *Summary: This test verifies that a `ToolResultsEvent` containing both text and an image URL is correctly transformed by the serialization function. It asserts that the output structure accurately represents the input data as separate text and image components within a function call output object.*


### test_audio_binary_raises (method, L577-L588, parent: TestResponsesToolResult)

> *Summary: This test verifies that passing an `AudioInput` containing binary data to the message conversion function raises an `UnsupportedInputError`. It asserts this error specifically matches a pattern indicating unsupported binary input for OpenAI responses.*

