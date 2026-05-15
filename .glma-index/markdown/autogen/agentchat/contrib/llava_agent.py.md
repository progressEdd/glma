# autogen/agentchat/contrib/llava_agent.py

3 function(s): _llava_call_binary_with_config, llava_call_binary, llava_call. 1 class(es): LLaVAAgent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LLaVAAgent | class |  |
| _llava_call_binary_with_config | function |  |
| llava_call_binary | function |  |
| llava_call | function |  |

## Chunks

### LLaVAAgent (class, L37-L118)

> *Summary: This deprecated agent class handles multimodal conversations by taking a system message and user messages (which may contain images) as input. It constructs a prompt combining text and image URLs, then calls an external `llava_call_binary` function to generate a textual response based on the provided inputs, returning the resulting string.*


### __init__ (method, L45-L73, parent: LLaVAAgent)

> *Summary: Initializes a deprecated multimodal agent by calling the parent constructor with provided name and system message. It asserts that an LLM configuration is present and registers a specific image-handling reply function for the agent.*


### _image_reply (method, L75-L118, parent: LLaVAAgent)

> *Summary: This method processes a list of messages and an optional sender to construct a prompt containing text and image URLs. It then iteratively calls `llava_call_binary` with the constructed prompt and extracted images until a non-empty response is received, finally returning a success status and the generated output string.*


### _llava_call_binary_with_config (function, L122-L169)

> *Summary: Determines whether to connect locally or remotely based on the provided base URL configuration. It then sends a multimodal prompt and image list to either a local HTTP endpoint or the Replicate service, returning the extracted text response after stripping the original prompt.*


### llava_call_binary (function, L173-L189)

> *Summary: Iterates through a list of configurations to execute a binary LLaVA call using a given prompt and image list. It returns the result from the first successful configuration or continues if an error occurs during processing.*


### llava_call (function, L192-L207)

> *Summary: This function prepares a prompt, potentially including images, by formatting it using `llava_formatter`. It then invokes a binary call to the LLaVA service with the formatted prompt and image data, returning the generated text response.*

