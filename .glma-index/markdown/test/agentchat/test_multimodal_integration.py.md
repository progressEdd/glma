# test/agentchat/test_multimodal_integration.py

17 function(s): _assert_multimodal_content_handling, _create_test_multimodal_content, _create_test_multimodal_content_responses_api, _verify_content_str_processing, test_conversable_agent_multimodal_message_handling, test_two_agent_multimodal_conversation, test_group_chat_multimodal_content, test_sequential_chat_multimodal_carryover, test_multimodal_content_str_integration, test_multimodal_backwards_compatibility_integration and 7 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _assert_multimodal_content_handling | function |  |
| _create_test_multimodal_content | function |  |
| _create_test_multimodal_content_responses_api | function |  |
| _verify_content_str_processing | function |  |
| test_conversable_agent_multimodal_message_handling | function |  |
| test_two_agent_multimodal_conversation | function |  |
| test_group_chat_multimodal_content | function |  |
| test_sequential_chat_multimodal_carryover | function |  |
| test_multimodal_content_str_integration | function |  |
| test_multimodal_backwards_compatibility_integration | function |  |
| test_error_handling_multimodal_integration | function |  |
| test_conversable_agent_run_multimodal | function |  |
| test_initiate_group_chat_multimodal | function |  |
| test_run_group_chat_multimodal | function |  |
| test_pattern_based_multimodal_orchestration | function |  |
| test_group_chat_context_variables_multimodal | function |  |
| test_responses_api_phase_field_handling | function |  |

## Chunks

### _assert_multimodal_content_handling (function, L19-L44)

> *Summary: This function validates the structure of a message's content to ensure proper handling of multimodal data. It checks if the content is either a non-empty string or a list containing dictionaries that correctly specify types like "text," "image\_url," or "input\_image."*


### _create_test_multimodal_content (function, L47-L58)

> *Summary: Generates a list of dictionaries structured for the Chat Completion API, containing both text prompts and a reference to an image URL. This serves as standardized input data for testing multimodal integration within the agent chat system.*


### _create_test_multimodal_content_responses_api (function, L61-L70)

> *Summary: Generates a list of dictionaries structured for the Responses API, containing both text prompts and an image URL pointing to a test visualization. This output serves as predefined multimodal content for integration testing purposes.*


### _verify_content_str_processing (function, L73-L90)

> *Summary: This test function validates that the `content_str` utility correctly processes multimodal input lists. It asserts that the output is a non-empty string containing all original text segments and includes the `<image>` placeholder if any image data was present in the input.*


### test_conversable_agent_multimodal_message_handling (function, L95-L136)

> *Summary: This test verifies that a `ConversableAgent` can successfully process and respond to multimodal inputs (text and images) during a chat session. It initiates a conversation using a pre-generated multimodal message, then asserts that both the initial user message and the agent's reply contain and correctly handle this complex content.*


### test_two_agent_multimodal_conversation (function, L141-L190)

> *Summary: Tests a two-agent conversation flow where the initial message includes both text and an image URL. It verifies that the agents successfully exchange messages, the multimodal content is preserved in the history, and the designated analyst agent participates in the chat.*


### test_group_chat_multimodal_content (function, L195-L263)

> *Summary: This test sets up a group chat involving a user proxy and two specialized agents (analyst and designer). It initiates a conversation using a multimodal message containing text and an image URL, then asserts that the chat completes successfully, preserves the initial multimodal content across all messages, and ensures at least one expert agent participates in the discussion.*


### test_sequential_chat_multimodal_carryover (function, L268-L338)

> *Summary: This test verifies that a multi-agent workflow correctly handles and carries over multimodal context across sequential conversations. It initiates chats with an initial message containing both text and an image, then asserts that subsequent agents receive context from the preceding steps.*


### test_multimodal_content_str_integration (function, L343-L422)

> *Summary: This test verifies the `content_str` function's ability to process various multimodal inputs (text-only, image-only, and mixed) sent to an AI agent. It asserts that text content is preserved as strings and that image URLs are correctly converted into `<image>` placeholders within the resulting string output.*


### test_multimodal_backwards_compatibility_integration (function, L427-L482)

> *Summary: Verifies that the multimodal agent integration maintains backward compatibility by successfully processing both traditional string and dictionary message formats during chat interactions. It asserts that a helper function, `content_str`, correctly converts all received content types into strings across various conversation scenarios.*


### test_error_handling_multimodal_integration (function, L487-L554)

> *Summary: This test verifies the robustness of a function designed to process multimodal content by asserting that it correctly raises specific exceptions for malformed inputs (like missing keys or incorrect types). It also confirms that valid and gracefully handled edge cases produce expected string outputs, finally ensuring agents can successfully use well-formed multimodal data in a chat session.*


### test_conversable_agent_run_multimodal (function, L559-L617)

> *Summary: This test verifies the `run` method of a conversational agent when provided with multimodal input. It initializes an agent, sends text-only content via its `run` method, and then asserts that the resulting response object contains correctly processed messages from both the user and the assistant.*


### test_initiate_group_chat_multimodal (function, L622-L690)

> *Summary: This test verifies the `initiate_group_chat` functionality by first running a standard string-based group chat and then executing a second run using multimodal content (text and images). It asserts that both runs complete successfully, maintain conversation history, and specifically validates that the multimodal input is correctly preserved and processed throughout the interaction.*


### test_run_group_chat_multimodal (function, L695-L759)

> *Summary: This test verifies the `run_group_chat` function's capability to handle both text-only and multimodal inputs within a round-robin group chat setup. It executes two scenarios: one with a simple string prompt and another using a list containing text and an image URL, asserting that responses are returned and support streaming capabilities.*


### test_pattern_based_multimodal_orchestration (function, L764-L836)

> *Summary: This test verifies that different multi-agent orchestration patterns (AutoPattern and RandomPattern) correctly process multimodal inputs, specifically an image alongside text. It initiates group chats using predefined agents and a user proxy, asserting that the resulting chat history contains the expected content structure after interaction.*


### test_group_chat_context_variables_multimodal (function, L841-L907)

> *Summary: This test verifies that context variables are correctly maintained during a group chat involving multimodal inputs. It initiates a conversation with an image and text, then asserts that the final context retains predefined session and content type identifiers while also validating the processing of the multimodal message within the chat history.*


### test_responses_api_phase_field_handling (function, L912-L946)

> *Summary: This test verifies that the message retrieval process correctly handles potential extra fields, like a `phase` attribute from the OpenAI SDK, without causing Pydantic validation errors during chat execution. It initiates a short conversation between two agents and asserts that the assistant provides a non-empty response.*

