# test/agentchat/contrib/test_img_utils.py

1 function(s): are_b64_images_equal. 7 class(es): TestGetPilImage, TestGetImageData, TestLlavaFormatter, TestGpt4vFormatter, TestExtractImgPaths, MessageFormatterPILtoB64Test, ImageTokenCountTest. 19 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGetPilImage | class |  |
| are_b64_images_equal | function |  |
| TestGetImageData | class |  |
| TestLlavaFormatter | class |  |
| TestGpt4vFormatter | class |  |
| TestExtractImgPaths | class |  |
| MessageFormatterPILtoB64Test | class |  |
| ImageTokenCountTest | class |  |

## Chunks

### TestGetPilImage (class, L53-L64)

> *Summary: This test suite verifies the `get_pil_image` utility by ensuring it correctly reads and processes image data from both local file paths and existing PIL Image objects. It asserts that the resulting NumPy array representation matches the original input image's array.*


### test_read_local_file (method, L54-L59, parent: TestGetPilImage)

> *Summary: This test verifies image reading functionality by saving a generated PIL image to a temporary file and then loading it back using `get_pil_image`. It asserts that the loaded image data matches the original in-memory representation.*


### test_read_pil (method, L61-L64, parent: TestGetPilImage)

> *Summary: This test verifies that an input PIL image is correctly converted and compared against its NumPy array representation. It asserts equality between the original raw PIL image's NumPy conversion and the processed version obtained via `get_pil_image`.*


### are_b64_images_equal (function, L68-L72)

> *Summary: Compares two base64 encoded image strings by decoding them into PIL images and then checking if their NumPy array representations are element-wise identical. It returns a boolean indicating equality.*


### TestGetImageData (class, L76-L108)

> *Summary: This test suite verifies the `get_image_data` function's ability to retrieve image data from three sources: HTTP URLs, base64 strings, and local files. It asserts that the returned content is correctly encoded as a Base64 string matching the input source.*


### test_http_image (method, L77-L85, parent: TestGetImageData)

> *Summary: This test verifies the `get_image_data` function by mocking an HTTP GET request to return a specific image payload. It asserts that the returned data matches the expected base64 encoded string derived from the mock response content.*


### test_base64_encoded_image (method, L87-L90, parent: TestGetImageData)

> *Summary: This test verifies that decoding a Base64-encoded image string using `get_image_data` yields the exact same raw data as the original encoded string (minus the prefix). It confirms correct image data extraction from a standard Base64 format.*


### test_local_image (method, L92-L108, parent: TestGetImageData)

> *Summary: This test verifies that the `get_image_data` function correctly reads and encodes various local image file types (PNG, JPG, GIF, etc.) into a base64 string representation of its PNG equivalent. It achieves this by creating temporary images, calling the function under test, and asserting the output matches the expected PNG encoding derived from the original file.*


### TestLlavaFormatter (class, L112-L140)

> *Summary: Verifies the `llava_formatter` utility by testing its behavior when processing prompts with or without image tags. It confirms that the function correctly extracts and replaces image references with placeholders, optionally assigning sequential indices to multiple images.*


### test_no_images (method, L113-L118, parent: TestLlavaFormatter)

> *Summary: Verifies that when provided a text-only prompt without any image references, the formatter returns the original prompt paired with an empty list of images. This confirms correct handling for purely textual inputs.*


### test_with_images (method, L121-L129, parent: TestLlavaFormatter)

> *Summary: Verifies that the `llava_formatter` correctly processes prompts containing image tags by mocking image data retrieval. It asserts that the function replaces the image tag with a placeholder and returns the associated raw encoded image data.*


### test_with_ordered_images (method, L132-L140, parent: TestLlavaFormatter)

> *Summary: Verifies that the `llava_formatter` correctly processes prompts containing ordered image tokens when `order_image_tokens` is set to true. It takes a prompt string and returns a tuple containing the formatted text and a list of encoded images, asserting against a predefined expected output.*


### TestGpt4vFormatter (class, L144-L213)

> *Summary: This test suite verifies the `gpt4v_formatter` function's ability to convert prompts containing text and image tags into structured message formats. It tests various scenarios, including no images, single images (with different data sources like base64 or PIL), URL-based images, and multiple embedded images.*


### test_no_images (method, L145-L150, parent: TestGpt4vFormatter)

> *Summary: Verifies that the `gpt4v_formatter` correctly processes a text-only prompt, expecting an output structure containing only a text element matching the input.*


### test_with_images (method, L153-L165, parent: TestGpt4vFormatter)

> *Summary: This test verifies the `gpt4v_formatter` function's ability to process prompts containing image tags. It mocks image data retrieval and asserts that the formatter correctly transforms the input string into a structured list of text and image URL objects.*


### test_with_images_for_pil (method, L168-L180, parent: TestGpt4vFormatter)

> *Summary: Verifies that the `gpt4v_formatter` correctly processes a prompt containing an image tag by substituting it with a structured list of text and image URL objects. It uses a mocked PIL image data to ensure the output matches the expected format when using "pil" as the image format.*


### test_with_images_for_url (method, L182-L191, parent: TestGpt4vFormatter)

> *Summary: This test verifies that the `gpt4v_formatter` correctly parses a prompt containing an image tag. It takes a string input with an embedded URL and asserts the output matches a structured list of text and image URL objects.*


### test_multiple_images (method, L194-L213, parent: TestGpt4vFormatter)

> *Summary: Verifies that the `gpt4v_formatter` correctly processes a prompt containing multiple image tags. It takes a string input with embedded image URLs and asserts the output is a list of structured message parts, alternating between text and encoded image data.*


### TestExtractImgPaths (class, L217-L259)

> *Summary: This test suite verifies the `extract_img_paths` function's ability to correctly identify image URLs and paths from text input. It confirms proper handling for cases with no images, multiple HTTP links, mixed-case extensions, and local file path references.*


### test_no_images (method, L218-L223, parent: TestExtractImgPaths)

> *Summary: Verifies that the `extract_img_paths` function correctly returns an empty list when provided with text containing no image references. The input is a string paragraph, and the expected output is an empty list.*


### test_with_images (method, L225-L238, parent: TestExtractImgPaths)

> *Summary: This test verifies that the `extract_img_paths` function correctly parses a string containing multiple image URLs. It takes a paragraph as input and asserts that the returned list matches the expected sequence of image paths found within it.*


### test_mixed_case (method, L240-L252, parent: TestExtractImgPaths)

> *Summary: Verifies that the `extract_img_paths` function correctly identifies image URLs even when their extensions use mixed casing (e.g., `.JPG`, `.Png`). It takes a string containing various image links as input and asserts the returned list matches the expected set of paths.*


### test_local_paths (method, L254-L259, parent: TestExtractImgPaths)

> *Summary: This test verifies that the `extract_img_paths` function correctly parses a string containing local image file names, returning a list of those extracted paths. It takes a paragraph as input and asserts the output matches the expected list of filenames.*


### MessageFormatterPILtoB64Test (class, L263-L290)

> *Summary: This test verifies that a function correctly converts messages containing PIL image objects into the required JSON format for API calls. It takes a list of structured messages as input and asserts the output matches an expected structure where the raw image is encoded into a base64 data URI within the message content.*


### test_formatting (method, L264-L290, parent: MessageFormatterPILtoB64Test)

> *Summary: This test verifies that a function correctly converts a list of messages containing a PIL image object into the required JSON format using base64 encoding. It takes an input structure with system and user roles, including text and an image placeholder, and asserts the output matches the expected structure with the image data URI embedded.*


### ImageTokenCountTest (class, L293-L324)

> *Summary: This test suite verifies the token counting mechanism for images by asserting expected values returned by `num_tokens_from_gpt_image`. It uses various sized and shaped PIL Image objects as input to check against known ground truth counts for different OpenAI models, including a low-quality flag.*


### test_tokens (method, L294-L324, parent: ImageTokenCountTest)

> *Summary: This test verifies the token counting function by asserting expected token values for various image sizes and models. It inputs `PIL.Image` objects (small, medium, tall, huge, wide) and optionally a model name or a `low_quality` flag to check against predefined ground truth counts.*

