# test/beta/config/ollama/test_convert_messages.py

8 function(s): _model_response_with_tool_call, test_audio_url_input_raises, test_image_input_raises, test_document_url_input_raises, test_file_id_input_raises, test_binary_input_raises, test_multiple_text_inputs_emit_separate_messages, test_multiple_text_inputs_with_images_attach_to_last. 2 class(es): TestConvertMessagesEmptyArguments, TestImageBinaryInput. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _model_response_with_tool_call | function |  |
| TestConvertMessagesEmptyArguments | class |  |
| test_audio_url_input_raises | function |  |
| test_image_input_raises | function |  |
| test_document_url_input_raises | function |  |
| test_file_id_input_raises | function |  |
| test_binary_input_raises | function |  |
| TestImageBinaryInput | class |  |
| test_multiple_text_inputs_emit_separate_messages | function |  |
| test_multiple_text_inputs_with_images_attach_to_last | function |  |

## Chunks

### _model_response_with_tool_call (function, L27-L33)

> *Summary: Constructs a `ModelResponse` object that contains no message but includes a single tool call event. This function accepts an optional string argument for the tool's parameters and returns a structured response indicating a required action by the model.*


### TestConvertMessagesEmptyArguments (class, L36-L53)

> *Summary: This test suite verifies that the message conversion utility handles empty or `None` tool call arguments gracefully, ensuring it produces an expected structure with empty argument dictionaries. It also confirms that valid JSON string arguments are correctly parsed and preserved within the output structure.*


### test_empty_arguments_produce_empty_dict (method, L40-L46, parent: TestConvertMessagesEmptyArguments)

> *Summary: When provided with no input arguments, this test asserts that the message conversion process yields a specific partial dictionary structure containing an assistant role and a tool call with empty function arguments. This verifies correct handling of null or empty inputs during serialization.*


### test_valid_arguments_are_preserved (method, L48-L53, parent: TestConvertMessagesEmptyArguments)

> *Summary: This test verifies that when converting messages, valid arguments within tool calls are correctly preserved. It asserts the structure of the resulting message list after processing an empty input with a specific model response containing a tool call argument.*


### test_audio_url_input_raises (function, L56-L58)

> *Summary: This test asserts that providing an audio URL as input to the message conversion process raises an `UnsupportedInputError` when using a specific serializer class. It verifies the error message contains "UrlInput" and "ollama".*


### test_image_input_raises (function, L61-L63)

> *Summary: This test verifies that providing an image URL as input to the message conversion process correctly raises an `UnsupportedInputError` when using the specified serializer class. It asserts that the error message specifically mentions "UrlInput" and "ollama".*


### test_document_url_input_raises (function, L66-L68)

> *Summary: This test asserts that providing a document URL within the input messages raises an `UnsupportedInputError` when processing with the specified serializer class. It verifies the error message specifically mentions "UrlInput" and "ollama".*


### test_file_id_input_raises (function, L71-L73)

> *Summary: This test asserts that passing a `FileIdInput` within the message list to the conversion function raises an `UnsupportedInputError`. It specifically checks for an error matching "FileIdInput.*ollama" when processing the provided inputs.*


### test_binary_input_raises (function, L76-L78)

> *Summary: Asserts that passing a binary input within the message structure to the serializer raises an `UnsupportedInputError` when using the specified class. This test verifies correct error handling for unsupported data types during serialization.*


### TestImageBinaryInput (class, L81-L131)

> *Summary: This test suite verifies the serialization of multimodal inputs for Ollama models, specifically ensuring that image data (provided as binary PNG bytes) is correctly encoded into Base64 and placed in the `images` field of a user message. It confirms correct handling for single images, text combined with images, multiple images, and plain text messages without any image components.*


### test_image_only (method, L86-L92, parent: TestImageBinaryInput)

> *Summary: When provided with an empty list of messages and a request containing only an image input, this test asserts that the conversion function returns a user message structure containing the base64 encoded image data. This verifies correct handling when text content is absent but media is present in the input.*


### test_text_plus_image (method, L94-L104, parent: TestImageBinaryInput)

> *Summary: This test verifies that the `convert_messages` function correctly transforms a mixed input containing text and an image into the expected structured output format. It asserts that the resulting list contains a single user message object with the prompt text and the base64-encoded image data.*


### test_multiple_images (method, L106-L125, parent: TestImageBinaryInput)

> *Summary: This test verifies that the `convert_messages` function correctly processes a request containing multiple image inputs. It asserts that the output structure contains a single user message with an array of base64-encoded strings corresponding to both input images.*


### test_text_without_image_stays_plain (method, L127-L131, parent: TestImageBinaryInput)

> *Summary: Verifies that when converting messages containing only text, the resulting structure does not include an `images` key. It takes an empty list and a list of model requests with text input as input, asserting the output matches a plain dictionary format.*


### test_multiple_text_inputs_emit_separate_messages (function, L134-L144)

> *Summary: When provided with a list containing multiple `TextInput` objects within a single model request, the function converts each input into its own distinct user message in the output. This ensures that separate text inputs are not concatenated but appear as individual messages.*


### test_multiple_text_inputs_with_images_attach_to_last (function, L147-L160)

> *Summary: This test verifies that when multiple text inputs and an image are provided in a sequence, the image correctly attaches only to the final `TextInput` within the same user turn. It asserts that the resulting message structure separates the initial text from the subsequent text containing the encoded image data.*

