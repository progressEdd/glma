# test/beta/config/openai/tools/test_image_generation.py

8 function(s): test_responses_api_defaults, test_responses_api_quality, test_responses_api_size, test_responses_api_background, test_responses_api_output_format, test_responses_api_output_compression, test_responses_api_partial_images, test_responses_api_all_params.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_responses_api_defaults | function |  |
| test_responses_api_quality | function |  |
| test_responses_api_size | function |  |
| test_responses_api_background | function |  |
| test_responses_api_output_format | function |  |
| test_responses_api_output_compression | function |  |
| test_responses_api_partial_images | function |  |
| test_responses_api_all_params | function |  |

## Chunks

### test_responses_api_defaults (function, L13-L18)

> *Summary: This test verifies that the `ImageGenerationTool`'s schema, when processed by `tool_to_responses_api`, correctly maps to a specific API response type. It takes a testing context as input and asserts the resulting dictionary matches `{"type": "image_generation"}`.*


### test_responses_api_quality (function, L22-L27)

> *Summary: This test verifies that the `ImageGenerationTool` correctly translates its configuration into a standardized API response format. It takes a context, initializes the tool with high quality, retrieves its schema, and asserts the resulting structure matches an expected dictionary.*


### test_responses_api_size (function, L31-L36)

> *Summary: This test verifies that the `ImageGenerationTool` correctly translates its configuration into a standardized API response format. It asserts that the tool's schema, when processed by `tool_to_responses_api`, yields the expected dictionary containing the image generation type and specified size.*


### test_responses_api_background (function, L40-L45)

> *Summary: This test verifies that the `ImageGenerationTool` correctly translates its schema into a specific API response format when provided with a context. It asserts that the resulting structure matches an expected dictionary containing the image generation type and background setting.*


### test_responses_api_output_format (function, L49-L54)

> *Summary: This test verifies that the `ImageGenerationTool` correctly formats its schema output for the responses API when configured to produce WebP images. It asserts that the resulting structure matches a specific dictionary format containing the tool type and desired output format.*


### test_responses_api_output_compression (function, L58-L67)

> *Summary: This test verifies that the `ImageGenerationTool` correctly serializes its configuration into the expected API response format. It takes a context object and asserts that the resulting structure accurately reflects the specified output format ("jpeg") and compression level (75).*


### test_responses_api_partial_images (function, L71-L76)

> *Summary: This test verifies that an `ImageGenerationTool` configured for partial images correctly translates its schema into the expected API response format. It asserts that the resulting structure includes `"type": "image_generation"` and the specified `"partial_images"` count of 2.*


### test_responses_api_all_params (function, L80-L98)

> *Summary: This test verifies that the `ImageGenerationTool` correctly translates its configuration parameters into a standardized API response schema. It takes a `Context` object as input and asserts the resulting dictionary matches the tool's defined settings for quality, size, format, etc.*

