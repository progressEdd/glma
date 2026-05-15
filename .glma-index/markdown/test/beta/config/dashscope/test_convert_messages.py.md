# test/beta/config/dashscope/test_convert_messages.py

4 function(s): test_audio_url_input_raises, test_document_url_input_raises, test_file_id_input_raises, test_non_image_binary_raises. 2 class(es): TestQwenVLImage, TestToolResult. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_audio_url_input_raises | function |  |
| test_document_url_input_raises | function |  |
| test_file_id_input_raises | function |  |
| test_non_image_binary_raises | function |  |
| TestQwenVLImage | class |  |
| TestToolResult | class |  |

## Chunks

### test_audio_url_input_raises (function, L26-L28)

> *Summary: This test asserts that providing an audio URL as input to the message conversion process raises a specific `UnsupportedInputError` when using the DashScope serializer. It verifies the expected error handling for unsupported URL inputs.*


### test_document_url_input_raises (function, L31-L33)

> *Summary: This test asserts that providing a document URL as input to the message conversion process raises an `UnsupportedInputError` specifically when dealing with DashScope models. It verifies the error message contains "UrlInput" and "dashscope".*


### test_file_id_input_raises (function, L36-L38)

> *Summary: Asserts that providing a `FileIdInput` within the request messages raises an `UnsupportedInputError` when processing with the specified serializer. This test verifies input validation for file ID usage in message conversion.*


### test_non_image_binary_raises (function, L41-L48)

> *Summary: Asserts that attempting to convert messages containing a non-image binary input type will raise an `UnsupportedInputError` when using the DashScope serializer. This test verifies the system correctly rejects unsupported binary data formats during message conversion.*


### TestQwenVLImage (class, L51-L80)

> *Summary: This test suite verifies the serialization logic for Qwen-VL multimodal content, ensuring that different input types—plain text, image URLs, raw binary data, and combinations thereof—are correctly transformed into the expected structured message format. It confirms how `convert_messages` handles various inputs to produce standardized JSON-like outputs containing roles and content blocks.*


### test_text_only_stays_string (method, L57-L60, parent: TestQwenVLImage)

> *Summary: When provided with an empty list of messages and a request containing only text input, this test asserts that the conversion process returns a specific structured message format. The output confirms that the single text input is correctly transformed into a user role message object.*


### test_image_url (method, L62-L65, parent: TestQwenVLImage)

> *Summary: This test verifies that an empty message list, when combined with a request containing only an image URL input, correctly serializes into a user role message structure containing the provided image URL. It asserts the resulting serialized format matches the expected dictionary representation.*


### test_image_binary (method, L67-L73, parent: TestQwenVLImage)

> *Summary: This test verifies that an image binary input is correctly converted into a base64-encoded message format expected by the API. It asserts that the output structure matches a user role containing a data URI for the provided PNG image.*


### test_text_plus_image (method, L75-L80, parent: TestQwenVLImage)

> *Summary: This test verifies that the `convert_messages` function correctly transforms a list containing one user message with both text and an image URL into the expected structured output format. It asserts the resulting structure matches a specific dictionary representation for multimodal input.*


### TestToolResult (class, L83-L152)

> *Summary: This test suite verifies the `convert_messages` function's ability to serialize various tool result formats into a standardized message structure. It tests handling of plain text, image URLs, embedded binary images (Base64), mixed content, and ensures that unsupported inputs like PDF documents raise an expected error.*


### test_text_only_stays_string (method, L89-L93, parent: TestToolResult)

> *Summary: When provided with an event containing a single text-based tool result, this test verifies that the message conversion process correctly transforms it into a list containing a dictionary representing the tool output. The input is an empty message list and a list of `ToolResultsEvent` objects; the expected output is a specific structured list of dictionaries.*


### test_image_url (method, L95-L101, parent: TestToolResult)

> *Summary: This test verifies the message conversion process when an input contains a tool result referencing an image URL. It asserts that the resulting list of messages correctly formats this input as a structured content object containing the image URL under the "tool" role.*


### test_image_binary (method, L103-L118, parent: TestToolResult)

> *Summary: This test verifies that an event containing a binary image input is correctly serialized into the expected JSON format. It takes an `ToolResultsEvent` with a PNG image and asserts the output matches a list containing a tool message with base64-encoded content.*


### test_mixed_text_and_image (method, L120-L138, parent: TestToolResult)

> *Summary: This test verifies that a list of events containing mixed text and image inputs is correctly serialized into the expected JSON format for tool results. It takes an event structure with a specific tool result containing both text and an image URL as input, asserting the output matches the standardized message representation.*


### test_document_in_tool_result_raises (method, L140-L152, parent: TestToolResult)

> *Summary: This test verifies that the message conversion process raises an `UnsupportedInputError` when a tool result contains binary PDF data as input. It asserts this behavior by passing a specific `ToolResultsEvent` containing a document input to the serializer function.*

