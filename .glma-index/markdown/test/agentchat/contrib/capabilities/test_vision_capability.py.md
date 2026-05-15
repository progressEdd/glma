# test/agentchat/contrib/capabilities/test_vision_capability.py

7 function(s): lmm_config, vision_capability, conversable_agent, test_add_to_conversable_agent, test_process_last_received_message_text, test_process_last_received_message_with_image, custom_caption_func. 1 class(es): TestCustomCaptionFunc. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| lmm_config | function |  |
| vision_capability | function |  |
| conversable_agent | function |  |
| test_add_to_conversable_agent | function |  |
| test_process_last_received_message_text | function |  |
| test_process_last_received_message_with_image | function |  |
| custom_caption_func | function |  |
| TestCustomCaptionFunc | class |  |

## Chunks

### lmm_config (function, L21-L26)

> *Summary: Returns a dictionary containing configuration settings for an LMM, specifying the OpenAI vision model (`gpt-4-vision-preview`) with a placeholder API key, along with default values for temperature and maximum tokens. This structure dictates how multimodal models will be initialized and utilized.*


### vision_capability (function, L33-L34)

> *Summary: Creates a `VisionCapability` instance using the provided LMM configuration. It initializes this capability without a custom caption function.*


### conversable_agent (function, L38-L39)

> *Summary: Creates and returns a `ConversableAgent` instance configured for conversational interactions, initialized without an LLM configuration. This agent is designed to participate in dialogue-based tasks.*


### test_add_to_conversable_agent (function, L44-L46)

> *Summary: This test verifies that adding a vision capability to an agent grants the agent the `process_last_received_message` method. It achieves this by calling `add_to_agent` on the provided objects and asserting the presence of the expected attribute.*


### test_process_last_received_message_text (function, L52-L56)

> *Summary: When provided with a text-only message, this test verifies that the capability processes and returns the input string unchanged. It mocks an LMM client to ensure no image processing logic is triggered for pure text inputs.*


### test_process_last_received_message_with_image (function, L70-L78)

> *Summary: This test verifies that a vision capability correctly processes an incoming message containing an image URL. It asserts that the output matches a predefined string incorporating the image name and a sample caption.*


### custom_caption_func (function, L85-L92)

> *Summary: Provides a fixture that returns a sample function capable of generating captions for an image given its URL and optional data/client. This returned function accepts an `image_url` string and outputs a descriptive string based on the provided URL.*


### TestCustomCaptionFunc (class, L97-L112)

> *Summary: This test suite verifies a custom caption function's behavior when processing image URLs. It asserts that the provided function correctly generates an expected descriptive string from a valid URL and confirms this output is present after passing image content through a `VisionCapability` instance.*


### test_custom_caption_func_with_valid_url (method, L98-L102, parent: TestCustomCaptionFunc)

> *Summary: Verifies that a provided custom caption function correctly processes a valid image URL input to produce an expected descriptive string output. It asserts the returned caption matches a predefined format incorporating the input URL.*


### test_process_last_received_message_with_custom_func (method, L104-L112, parent: TestCustomCaptionFunc)

> *Summary: This test verifies that a vision capability correctly processes an input containing an image URL by utilizing a provided custom caption function. It asserts that the resulting output string includes the expected description and the original image URL.*

