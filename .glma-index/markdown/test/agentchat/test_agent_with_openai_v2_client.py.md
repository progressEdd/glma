# test/agentchat/test_agent_with_openai_v2_client.py

39 function(s): _assert_v2_response_structure, _create_test_v2_config, test_v2_client_simple_chat, test_v2_client_with_vision_multimodal, test_v2_client_multi_turn_conversation, test_v2_client_with_system_message, test_v2_client_cost_tracking, test_v2_client_group_chat, test_v2_client_run_interface, test_v2_client_content_str_compatibility and 29 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _assert_v2_response_structure | function |  |
| _create_test_v2_config | function |  |
| test_v2_client_simple_chat | function |  |
| test_v2_client_with_vision_multimodal | function |  |
| test_v2_client_multi_turn_conversation | function |  |
| test_v2_client_with_system_message | function |  |
| test_v2_client_cost_tracking | function |  |
| test_v2_client_group_chat | function |  |
| test_v2_client_run_interface | function |  |
| test_v2_client_content_str_compatibility | function |  |
| test_v2_client_vs_standard_comparison | function |  |
| test_v2_client_error_handling_invalid_model | function |  |
| test_v2_client_sequential_chats | function |  |
| test_v2_client_backwards_compatibility | function |  |
| test_v2_client_multimodal_with_multiple_images | function |  |
| test_v2_client_with_group_pattern | function |  |
| test_v2_client_pattern_with_vision | function |  |
| test_v2_client_run_group_chat_basic | function |  |
| test_v2_client_run_group_chat_multimodal | function |  |
| test_v2_client_run_group_chat_content_preservation | function |  |
| test_v2_client_structured_output_pydantic_simple | function |  |
| test_v2_client_structured_output_pydantic_complex | function |  |
| test_v2_client_structured_output_multi_turn | function |  |
| test_v2_client_structured_output_group_chat | function |  |
| test_v2_client_structured_output_pattern_based | function |  |
| test_v2_client_structured_output_override_in_params | function |  |
| test_v2_client_tool_calling_two_agent | function |  |
| test_v2_client_tool_calling_group_chat | function |  |
| test_v2_client_function_call_legacy | function |  |
| test_v2_client_multimodal_image_two_agent | function |  |
| test_v2_client_multimodal_group_chat | function |  |
| test_v2_client_reasoning_model_basic | function |  |
| test_v2_client_reasoning_parameter_processing | function |  |
| test_v2_client_reasoning_with_system_message | function |  |
| test_v2_client_reasoning_non_streaming | function |  |
| test_v2_client_reasoning_no_tools | function |  |
| test_v2_client_combined_structured_output_and_tools | function |  |
| test_v2_client_multimodal_with_tools | function |  |
| test_v2_client_auto_pattern_with_tools | function |  |

## Chunks

### _assert_v2_response_structure (function, L37-L43)

> *Summary: This helper function validates the structure of a chat result object by ensuring it is not null and contains specific attributes: `chat_history`, `cost`, and `summary`. It also asserts that the `chat_history` list contains at least two entries.*


### _create_test_v2_config (function, L46-L60)

> *Summary: Generates a configuration dictionary for an OpenAI V2 client using provided credentials. It extracts model and API key information from the input `Credentials` object to structure the necessary settings, defaulting if values are missing.*


### test_v2_client_simple_chat (function, L65-L87)

> *Summary: This test verifies basic conversational functionality by initiating a single-turn chat between an assistant and a user proxy using the V2 OpenAI client configuration. It asserts that the response structure is correct, the expected answer ("4") is present in the summary, and cost tracking data is recorded.*


### test_v2_client_with_vision_multimodal (function, L92-L127)

> *Summary: Tests the V2 client's ability to process and respond to multimodal inputs, specifically combining text prompts with an image URL. It initiates a chat between a vision-enabled assistant and a user proxy, asserting that the response structure is correct, the summary mentions "blue," and cost tracking includes usage for cached inference.*


### test_v2_client_multi_turn_conversation (function, L132-L156)

> *Summary: This test verifies that an `AssistantAgent` maintains conversational context across multiple turns when using the V2 OpenAI client. It initiates a chat to set a preference and then queries the agent about that preference, asserting the correct information is recalled.*


### test_v2_client_with_system_message (function, L161-L178)

> *Summary: This test verifies that an `AssistantAgent` correctly adheres to a provided system message when interacting with the V2 OpenAI client. It initiates a short chat exchange and asserts that the final summary contains the expected numerical answer, confirming the tutor persona was respected.*


### test_v2_client_cost_tracking (function, L183-L197)

> *Summary: This test verifies that the V2 OpenAI client accurately tracks costs during a simulated conversation. It initiates a short chat between an assistant and user proxies and asserts that the resulting cost object contains usage metrics, specifically `usage_including_cached_inference`.*


### test_v2_client_group_chat (function, L202-L240)

> *Summary: This test verifies the functionality of a V2 client within a group chat simulation. It initializes three agents—an analyst, a reviewer, and a user proxy—and initiates a conversation to ensure all participants engage in the discussion according to predefined roles. The function asserts that the resulting chat history contains responses from at least one of the specialized agents.*


### test_v2_client_run_interface (function, L245-L271)

> *Summary: This test verifies the `ConversableAgent`'s run interface by initializing an agent with OpenAI credentials and executing a single-turn interaction. It asserts that the returned response object contains expected message structures after processing, confirming successful communication with the LLM.*


### test_v2_client_content_str_compatibility (function, L276-L297)

> *Summary: This test verifies that responses from a V2 OpenAI client are compatible with the `content_str` utility. It initiates a brief chat between two agents and asserts that every message content retrieved from the resulting history can be successfully converted to a string using `content_str`.*


### test_v2_client_vs_standard_comparison (function, L302-L343)

> *Summary: This test function verifies that both the standard and V2 OpenAI clients produce equivalent results when interacting with an `AssistantAgent`. It initiates a chat with both configurations using a fixed prompt and asserts that both responses correctly contain "paris" and include cost tracking metrics.*


### test_v2_client_error_handling_invalid_model (function, L348-L360)

> *Summary: This test verifies that the system correctly handles errors when an unsupported or invalid language model is provided to the agent configuration. It initiates a chat using an `AssistantAgent` configured with a deliberately bad model name and asserts that an exception is raised during the interaction.*


### test_v2_client_sequential_chats (function, L365-L399)

> *Summary: This test verifies that a V2 client correctly handles sequential conversations between agents, ensuring context is carried over from one chat to the next. It initiates two chained chats—one for analysis and one for review—and asserts that the second chat's history contains content related to the preceding interaction.*


### test_v2_client_backwards_compatibility (function, L404-L427)

> *Summary: Verifies that the V2 client supports backwards compatibility by successfully initiating chats using both simple string messages and structured dictionary messages as input to an agent. It asserts that the resulting chat history contains at least two turns for both test cases.*


### test_v2_client_multimodal_with_multiple_images (function, L432-L462)

> *Summary: This test verifies the V2 client's ability to process multimodal inputs containing two Base64-encoded images alongside a text prompt. It initiates a chat with an assistant, asserting that the resulting response structure is correct and that cost tracking includes usage for multiple images.*


### test_v2_client_with_group_pattern (function, L467-L511)

> *Summary: This test verifies the functionality of a V2 client within a group chat orchestrated by `DefaultPattern`. It initializes two specialized agents, runs a multi-round conversation using a specific prompt, and asserts that the resulting chat history contains expected structure, cost metrics, and participation from both defined agents.*


### test_v2_client_pattern_with_vision (function, L516-L575)

> *Summary: This test verifies the V2 client's ability to handle multimodal inputs by setting up a pattern of agents capable of processing images. It initiates a group chat with an image prompt, asserting that the resulting summary correctly identifies the color ("blue") and that cost tracking and multimodal content preservation are accurate.*


### test_v2_client_run_group_chat_basic (function, L580-L651)

> *Summary: This test verifies the basic functionality of a group chat using the V2 client by setting up three specialized agents (Analyst, Reviewer, User). It initiates a conversation via `run_group_chat` with an initial prompt and then blocks execution by calling `.process()` on the response object to ensure all background events are processed before asserting successful completion metrics like message count, summary, and cost.*


### test_v2_client_run_group_chat_multimodal (function, L656-L741)

> *Summary: This test verifies the V2 client's ability to handle multimodal input within a group chat simulation. It initializes agents capable of analyzing images and breed identification, then runs a conversation using an initial message containing both text and an image URL, asserting that the resulting chat history preserves this complex content structure as a list.*


### test_v2_client_run_group_chat_content_preservation (function, L746-L844)

> *Summary: This test verifies that a group chat simulation correctly preserves the structure of multimodal content across conversation turns. It inputs a message containing text and two base64-encoded images, then asserts that the resulting chat history retains all original text and image blocks with intact URLs.*


### test_v2_client_structured_output_pydantic_simple (function, L849-L896)

> *Summary: This test verifies that an agent using the OpenAI V2 client can correctly generate a structured JSON response based on a Pydantic model. It initializes an assistant with a specific configuration, initiates a chat with a user proxy, and asserts that the resulting summary contains the expected data structure and content.*


### test_v2_client_structured_output_pydantic_complex (function, L901-L947)

> *Summary: This test verifies that an agent using the OpenAI V2 client can correctly generate a structured output conforming to a complex Pydantic model when prompted with a math question. It initiates a chat between a specialized assistant and a user proxy, asserting both the structural integrity of the response and the correctness of the final answer.*


### test_v2_client_structured_output_multi_turn (function, L952-L996)

> *Summary: This test verifies that an agent using the OpenAI V2 client can maintain structured output across multiple conversational turns. It initializes an `AssistantAgent` configured to return a specific Pydantic model (`FactCheck`) and then initiates two sequential chats with it, asserting the structure of the responses.*


### test_v2_client_structured_output_group_chat (function, L1001-L1060)

> *Summary: This test verifies the V2 client's ability to enforce structured output within a group chat simulation. It configures agents with Pydantic models for analysis and review, then initiates a conversation via `UserProxyAgent` to ensure the resulting chat history adheres to the expected structure.*


### test_v2_client_structured_output_pattern_based (function, L1065-L1124)

> *Summary: This test verifies the V2 client's ability to generate structured JSON output within a pattern-based group chat simulation. It configures two agents, one for analysis and one for review, using a Pydantic model to enforce a specific report structure when processing an initial prompt.*


### test_v2_client_structured_output_override_in_params (function, L1129-L1176)

> *Summary: Verifies that a specified `response_format` within an agent's parameters overrides any client-level defaults when interacting with an OpenAI V2 model. It initializes agents and runs a chat to confirm the expected structured output based on the configuration provided during setup.*


### test_v2_client_tool_calling_two_agent (function, L1186-L1267)

> *Summary: This test verifies two-agent conversation capabilities using the V2 OpenAI client, specifically focusing on function calling. It sets up an assistant with math tools and a user proxy capable of executing those functions to process a multi-step calculation request. The assertion confirms that the chat history correctly reflects tool calls and execution.*


### test_v2_client_tool_calling_group_chat (function, L1272-L1355)

> *Summary: This test verifies that an `AutoPattern` correctly orchestrates a group chat involving specialized agents capable of using defined tools. It inputs a multi-part query and asserts that the system successfully invokes both the weather and time functions to fulfill the request.*


### test_v2_client_function_call_legacy (function, L1360-L1403)

> *Summary: Tests the compatibility of a legacy function-calling format with the V2 client by setting up an agent and user proxy to execute a defined `calculate_sum` function via chat interaction. It verifies that the resulting chat history or summary correctly reflects the expected output (150).*


### test_v2_client_multimodal_image_two_agent (function, L1413-L1451)

> *Summary: Tests multimodal image processing by initiating a two-agent chat using a V2 client configuration and a base64 encoded image input. It asserts that the resulting conversation history is sufficient and contains a descriptive text output based on the provided image.*


### test_v2_client_multimodal_group_chat (function, L1456-L1502)

> *Summary: This test verifies multimodal group chat functionality using the V2 client by setting up a system with an image describer and analyzer agents. It initiates a conversation with a base64 encoded image, expecting the resulting chat history to contain at least two messages after execution.*


### test_v2_client_reasoning_model_basic (function, L1519-L1571)

> *Summary: This test verifies basic reasoning capabilities using an `AssistantAgent` configured with the OpenAI V2 client and the `o4-mini` model. It initiates a chat with a mathematical question, asserting that the final summary contains the correct answer ("36") and that the response structure correctly extracts the underlying reasoning content from the last message.*


### test_v2_client_reasoning_parameter_processing (function, L1580-L1622)

> *Summary: Verifies that the V2 client correctly processes reasoning model parameters by initiating a simple chat with an `AssistantAgent` configured for `o4-mini`. It asserts successful API interaction and verifies the expected numerical output from the conversation summary.*


### test_v2_client_reasoning_with_system_message (function, L1631-L1671)

> *Summary: Verifies that the V2 client correctly processes system messages when interacting with an `o4-mini` model via an `AssistantAgent`. It initiates a chat with a specific system prompt and asserts that the resulting summary contains the expected calculation result ("20").*


### test_v2_client_reasoning_non_streaming (function, L1680-L1716)

> *Summary: This test verifies the basic functionality of an agent using the OpenAI V2 client in non-streaming mode. It initializes an assistant and user proxy, initiates a single-turn chat with a simple prompt, and asserts that the resulting chat object contains a valid summary structure.*


### test_v2_client_reasoning_no_tools (function, L1725-L1764)

> *Summary: This test verifies that a reasoning model using the OpenAI V2 client can correctly solve basic mathematical problems without any registered tools. It initializes an agent and user proxy, then initiates a chat asking for the square of 5 to confirm the expected output structure and result.*


### test_v2_client_combined_structured_output_and_tools (function, L1774-L1832)

> *Summary: Verifies that an agent can successfully use a registered tool for calculation in one turn, followed by subsequent interaction to test structured output capabilities in the next turn. It sets up an assistant and user proxy with a math function tool and initiates a chat sequence to confirm both tool execution and response structure validation.*


### test_v2_client_multimodal_with_tools (function, L1837-L1887)

> *Summary: This test verifies the capability of an agent to process multimodal input (image and text) while utilizing a registered tool for analysis. It initiates a chat by providing a base64 encoded image and a prompt instructing the assistant to identify a color and call the `analyze_color` function, asserting that the resulting conversation history reflects this interaction.*


### test_v2_client_auto_pattern_with_tools (function, L1897-L1997)

> *Summary: This test verifies an LLM-based agent selection mechanism (`AutoPattern`) by simulating a multi-agent conversation. It initializes specialized agents equipped with mock tools for stock price retrieval and portfolio calculation, then initiates a chat to ensure the pattern correctly routes requests and invokes both defined functions.*

