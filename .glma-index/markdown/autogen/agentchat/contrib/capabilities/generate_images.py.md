# autogen/agentchat/contrib/capabilities/generate_images.py

2 function(s): _validate_resolution_format, _validate_dalle_model. 3 class(es): ImageGenerator, DalleImageGenerator, ImageGeneration. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ImageGenerator | class |  |
| DalleImageGenerator | class |  |
| ImageGeneration | class |  |
| _validate_resolution_format | function |  |
| _validate_dalle_model | function |  |

## Chunks

### ImageGenerator (class, L34-L68)

> *Summary: Defines an interface requiring implementations to generate a `PIL Image` from a text prompt and provide a method for creating a unique cache key based on that same prompt. It specifies the contract for image generation capabilities without supporting in-place editing of existing images.*


### generate_image (method, L43-L55, parent: ImageGenerator)

> *Summary: This method takes a text prompt as input and returns a `PIL Image` object representing the synthesized visual content. It raises a `ValueError` if the underlying image generation process encounters an error.*


### cache_key (method, L57-L68, parent: ImageGenerator)

> *Summary: Creates a unique string identifier from an input prompt to facilitate caching of generated images. This method takes a descriptive string and returns a deterministic key for retrieval.*


### DalleImageGenerator (class, L73-L122)

> *Summary: This class interfaces with OpenAI's DALL-E models to create images from text prompts. It accepts configuration details like model name, resolution, quality, and quantity as input, returning a PIL Image object derived from the generated image URL.*


### __init__ (method, L82-L103, parent: DalleImageGenerator)

> *Summary: Initializes an image generation capability by setting parameters like model, resolution, quality, and count. It validates the provided LLM configuration for a DALL-E model and initializes an `OpenAI` client using the API key from the config.*


### generate_image (method, L105-L118, parent: DalleImageGenerator)

> *Summary: This method takes a text prompt as input and uses an internal DALL-E client to generate images based on specified model, resolution, quality, and count settings. It returns the first generated image converted into a PIL Image object, raising an error if no URL is returned.*


### cache_key (method, L120-L122, parent: DalleImageGenerator)

> *Summary: Generates a unique string identifier by concatenating the input prompt with configuration parameters like the model, resolution, quality, and number of images. This key is used to cache image generation results based on all relevant inputs.*


### ImageGeneration (class, L130-L304)

> *Summary: This deprecated capability allows an agent to generate images based on incoming messages by first using a `TextAnalyzerAgent` to detect and extract image generation requests. It then utilizes a provided `ImageGenerator` to create the image, optionally caching results before returning a message containing both text confirmation and the generated image URL.*


### __init__ (method, L164-L204, parent: ImageGeneration)

> *Summary: Initializes an image generation capability by accepting an `ImageGenerator`, optional caching, and configuration for a text analyzer. It sets up internal state variables based on these inputs, while also issuing a deprecation warning about its reliance on older components.*


### add_to_agent (method, L206-L231, parent: ImageGeneration)

> *Summary: This method integrates image generation functionality into a given `ConversableAgent` by registering a specialized reply handler, creating an auxiliary text analyzer agent, and updating the target agent's system message and description to reflect the new capability. It modifies the input agent in place to enable it to process and respond to image generation requests.*


### _image_gen_reply (method, L233-L259, parent: ImageGeneration)

> *Summary: This method checks the last message in a conversation to determine if an image generation request is present. If so, it retrieves or generates the corresponding image using a cached prompt and returns a success status along with the generated content message.*


### _should_generate_image (method, L261-L271, parent: ImageGeneration)

> *Summary: Determines if a given message explicitly requests image generation by using a text analyzer to check for specific keywords within the input string. It returns `True` if the analysis indicates an explicit request to generate an image, otherwise `False`.*


### _extract_prompt (method, L273-L277, parent: ImageGeneration)

> *Summary: This method analyzes the `last_message` using a configured text analyzer to determine the prompt content. It returns the extracted prompt string based on the analysis results.*


### _cache_get (method, L279-L285, parent: ImageGeneration)

> *Summary: Retrieves a previously generated image from an internal cache using the provided prompt as input. If found, it returns the corresponding PIL Image object; otherwise, it implicitly proceeds to generate a new one.*


### _cache_set (method, L287-L290, parent: ImageGeneration)

> *Summary: Stores a generated image in an internal cache using the prompt as part of the key. It converts the input `Image` object into a data URI before saving it to the cache dictionary.*


### _extract_analysis (method, L292-L296, parent: ImageGeneration)

> *Summary: This method extracts the textual content from an input analysis, which can be either a string or a dictionary. It returns the extracted string after processing it through `code_utils.content_str`.*


### _generate_content_message (method, L298-L304, parent: ImageGeneration)

> *Summary: Constructs a message dictionary containing both text and an embedded image URL. It takes a prompt string and an `Image` object as input, returning the structured content ready for communication.*


### _validate_resolution_format (function, L308-L313)

> *Summary: Validates if an input string adheres to the "widthxheight" pattern using a regular expression. It raises a `ValueError` if the provided resolution string does not match the expected numeric format separated by 'x'.*


### _validate_dalle_model (function, L316-L318)

> *Summary: Ensures the provided string input is one of the supported DALL-E models ("dall-e-3" or "dall-e-2"). If an unsupported model name is passed, it raises a `ValueError`.*

