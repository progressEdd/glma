# test/agentchat/contrib/test_lmm.py

1 function(s): test_group_chat_with_lmm. 2 class(es): TestMultimodalConversableAgent, TestMultimodalConversableAgentImageTagProcessing. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMultimodalConversableAgent | class |  |
| test_group_chat_with_lmm | function |  |
| TestMultimodalConversableAgentImageTagProcessing | class |  |

## Chunks

### TestMultimodalConversableAgent (class, L31-L85)

> *Summary: This test suite verifies the functionality of a multimodal conversational agent initialized with an LLM configuration. It tests setting and updating system messages (including image embedding), converting various message formats to a dictionary structure, and mocking the printing of received messages.*


### setUp (method, L33-L43, parent: TestMultimodalConversableAgent)

> *Summary: Initializes a test agent instance configured to use the `gpt-4-vision-preview` model via OpenAI, setting a 600-second timeout and a fixed seed for reproducibility. This setup prepares the environment for testing multimodal conversational capabilities.*


### test_system_message (method, L45-L63, parent: TestMultimodalConversableAgent)

> *Summary: Verifies the agent's initial system message and tests its update mechanism. It confirms that updating with a string containing an image placeholder correctly parses and replaces it with structured text and image URL components within the system message list.*


### test_message_to_dict (method, L65-L78, parent: TestMultimodalConversableAgent)

> *Summary: This method verifies the `_message_to_dict` utility by testing its ability to correctly convert various input types—a string, a list of content objects, or an existing dictionary—into a standardized message dictionary format. It asserts that the output matches the expected structure for each tested input type.*


### test_print_received_message (method, L80-L85, parent: TestMultimodalConversableAgent)

> *Summary: This test verifies that the agent correctly calls its internal `_print_received_message` method when a message is received. It mocks this printing function and asserts it was called with the correct message string and the sending agent object as inputs.*


### test_group_chat_with_lmm (function, L90-L136)

> *Summary: This test verifies group chat behavior between two specialized agents, ensuring the conversation terminates correctly based on a predefined `max_round` limit. It initializes agents with distinct system prompts and uses a mock speaker selection to control the flow while asserting that no participant exceeds the round constraint during the interaction.*


### TestMultimodalConversableAgentImageTagProcessing (class, L141-L259)

> *Summary: This test suite verifies that `<img>` tags embedded within messages are correctly parsed and converted into multimodal content structures when interacting with a `MultimodalConversableAgent`. It tests both incoming (`receive`) and outgoing (`send`) messages to ensure image data is properly formatted for the underlying LLM API, while also confirming standard text messages remain functional.*


### setUp (method, L150-L166, parent: TestMultimodalConversableAgentImageTagProcessing)

> *Summary: Initializes two agents for testing: a multimodal agent configured with GPT-4 Vision and a standard user agent. These objects are set up to facilitate interactions between the visual and conversational components during tests.*


### test_img_tag_processed_in_received_message (method, L168-L207, parent: TestMultimodalConversableAgentImageTagProcessing)

> *Summary: Verifies that an input message containing an `<img>` tag is correctly parsed and converted into a multimodal content structure when received by the visual agent. It asserts that the resulting stored message contains both text and exactly one image part with a valid URL, ensuring proper handling of embedded images.*


### test_img_tag_processed_in_sent_message (method, L209-L225, parent: TestMultimodalConversableAgentImageTagProcessing)

> *Summary: Verifies that an agent correctly processes and sends a message containing embedded image tags. It asserts that the resulting message content stored by the visual agent is in a multimodal list format after sending it to another agent.*


### test_message_without_img_tag_preserved (method, L227-L243, parent: TestMultimodalConversableAgentImageTagProcessing)

> *Summary: Verifies that a standard text message, lacking image tags, is correctly processed and stored by the visual agent. It asserts that the resulting stored message content maintains a multimodal list structure containing exactly one text element matching the input string.*


### test_dict_message_with_string_content_processed (method, L245-L259, parent: TestMultimodalConversableAgentImageTagProcessing)

> *Summary: This test verifies that a dictionary message containing an HTML `<img>` tag within its string content is correctly transformed into a multimodal format. It asserts that the resulting message content is a list and contains exactly one image URL part after processing by the visual agent.*

