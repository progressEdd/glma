# autogen/beta/tools/builtin/image_generation.py

2 class(es): ImageGenerationToolSchema, ImageGenerationTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ImageGenerationToolSchema | class |  |
| ImageGenerationTool | class |  |

## Chunks

### ImageGenerationToolSchema (class, L22-L31)

> *Summary: Defines the structure for an image generation tool, accepting optional parameters like quality, size, background type, and output format. This schema dictates the inputs required when invoking the built-in OpenAI Responses API for image creation.*


### ImageGenerationTool (class, L34-L99)

> *Summary: This tool facilitates inline image generation via the OpenAI Responses API, requiring `OpenAIResponsesConfig`. It accepts parameters like quality, size, and format to generate images which are returned as a list of binary results. The implementation registers an execution handler for incoming tool calls matching its name.*


### __init__ (method, L57-L81, parent: ImageGenerationTool)

> *Summary: Initializes an image generation tool by accepting optional parameters like quality, size, background type, output format, compression level, and number of partial images. These provided inputs are stored internally as configuration settings for subsequent use.*


### schemas (method, L83-L85, parent: ImageGenerationTool)

> *Summary: Generates a list containing a single `ImageGenerationToolSchema` instance by resolving all internal parameters against the provided execution context. This method prepares the schema definition required for tool invocation.*


### register (method, L87-L99, parent: ImageGenerationTool)

> *Summary: This method registers a handler for image generation tool calls within an asynchronous context stack. It sets up a scope that intercepts events matching the specific image generation tool name, executing a provided `execute` function upon match.*

