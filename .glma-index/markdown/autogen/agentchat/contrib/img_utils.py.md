# autogen/agentchat/contrib/img_utils.py

10 function(s): get_pil_image, get_image_data, llava_formatter, pil_to_data_uri, convert_base64_to_data_uri, gpt4v_formatter, extract_img_paths, _to_pil, message_formatter_pil_to_b64, num_tokens_from_gpt_image.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_pil_image | function |  |
| get_image_data | function |  |
| llava_formatter | function |  |
| pil_to_data_uri | function |  |
| convert_base64_to_data_uri | function |  |
| gpt4v_formatter | function |  |
| extract_img_paths | function |  |
| _to_pil | function |  |
| message_formatter_pil_to_b64 | function |  |
| num_tokens_from_gpt_image | function |  |

## Chunks

### get_pil_image (function, L45-L81)

> *Summary: This utility function loads an image into a PIL `Image` object from various inputs, including local file paths, URLs, base64 strings, or by accepting an existing PIL Image directly. It handles different input formats and ensures the final output is converted to RGB mode.*


### get_image_data (function, L85-L112)

> *Summary: Loads an image from a file path, URL, or existing PIL Image object and serializes it to PNG format in memory. It returns the resulting binary data either as raw bytes or as a UTF-8 decoded base64 string based on the `use_b64` flag.*


### llava_formatter (function, L116-L157)

> *Summary: Transforms an input string containing image tags into a prompt suitable for multimodal models by replacing the tags with structured `<image>` tokens. It returns the modified prompt and a list of the corresponding images loaded in base64 format, optionally numbering the image placeholders.*


### pil_to_data_uri (function, L161-L173)

> *Summary: Takes a PIL Image object as input and serializes it into a PNG format within an in-memory buffer. It then encodes this binary data to Base64 and wraps it into a standard Data URI string for output.*


### convert_base64_to_data_uri (function, L176-L193)

> *Summary: Takes a base64 encoded image string as input and returns a full Data URI. It determines the MIME type by inspecting the initial bytes of the decoded data, supporting JPEG, PNG, GIF, and WebP formats.*


### gpt4v_formatter (function, L197-L242)

> *Summary: This function processes a string prompt, replacing embedded image tags with structured data based on the specified format ("uri", "url", or "pil"). It returns an alternating list of text segments and image representations (either as base64 URIs, direct URLs, or PIL objects).*


### extract_img_paths (function, L245-L262)

> *Summary: This function scans an input string to find and return a list of image paths. It uses a regular expression to match both full URLs and local file paths ending with common image extensions like jpg, png, or webp.*


### _to_pil (function, L266-L278)

> *Summary: Decodes a base64-encoded string into bytes, wraps those bytes in an in-memory buffer, and returns it as a PIL Image object. This utility converts raw image data strings into usable image objects for processing.*


### message_formatter_pil_to_b64 (function, L282-L334)

> *Summary: Transforms a list of message dictionaries by replacing PIL image objects within `image_url` fields with their base64 encoded data URI representations. It iterates through the input messages, deep-copying them to ensure immutability while performing the conversion on any found image URLs.*


### num_tokens_from_gpt_image (function, L338-L397)

> *Summary: Calculates the token cost for processing an image by scaling its dimensions based on the specified GPT model's constraints. It takes image data and a model name as input, returning an integer representing the estimated token count after determining necessary tiling.*

