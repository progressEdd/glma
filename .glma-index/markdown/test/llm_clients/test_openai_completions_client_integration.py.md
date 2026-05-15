# test/llm_clients/test_openai_completions_client_integration.py

1 function(s): openai_completions_client. 9 class(es): TestOpenAICompletionsClientBasicChat, TestOpenAICompletionsClientReasoningModels, TestOpenAICompletionsClientToolCalling, TestOpenAICompletionsClientStructuredOutput, TestOpenAICompletionsClientImageUrlInput, TestOpenAICompletionsClientUsageAndCost, TestOpenAICompletionsClientV1Compatibility, TestOpenAICompletionsClientErrorHandling, TestOpenAICompletionsClientMultiTurnConversation. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| openai_completions_client | function |  |
| TestOpenAICompletionsClientBasicChat | class |  |
| TestOpenAICompletionsClientReasoningModels | class |  |
| TestOpenAICompletionsClientToolCalling | class |  |
| TestOpenAICompletionsClientStructuredOutput | class |  |
| TestOpenAICompletionsClientImageUrlInput | class |  |
| TestOpenAICompletionsClientUsageAndCost | class |  |
| TestOpenAICompletionsClientV1Compatibility | class |  |
| TestOpenAICompletionsClientErrorHandling | class |  |
| TestOpenAICompletionsClientMultiTurnConversation | class |  |

## Chunks

### openai_completions_client (function, L28-L30)

> *Summary: This function constructs an `OpenAICompletionsClient` instance by extracting the API key from provided `Credentials`. It serves to initialize and return a configured client object for interacting with OpenAI completions.*


### TestOpenAICompletionsClientBasicChat (class, L33-L78)

> *Summary: This test suite verifies basic chat functionality by making live API calls to OpenAI's GPT-4 model using a provided client instance. It asserts that the returned response correctly identifies the provider, contains expected content based on the prompt (e.g., "4" for $2+2$), and accurately tracks token usage and cost.*


### test_simple_chat_gpt4 (method, L38-L61, parent: TestOpenAICompletionsClientBasicChat)

> *Summary: This test verifies the integration of a chat client with GPT-4 by sending a simple query and asserting that the returned response structure, content ("4"), token usage metrics, and calculated cost are all present and valid. It confirms the client correctly interacts with the OpenAI API for basic conversational tasks.*


### test_chat_with_system_message (method, L65-L78, parent: TestOpenAICompletionsClientBasicChat)

> *Summary: This test verifies that the client correctly handles a chat request including a system message prompt. It sends a structured input containing roles and content to the OpenAI endpoint and asserts the returned text is non-empty and contains the expected keyword.*


### TestOpenAICompletionsClientReasoningModels (class, L81-L120)

> *Summary: This test executes real API calls against OpenAI's `o1-preview` model to validate its reasoning capabilities for complex queries like factorial calculation. It asserts that the returned response contains expected structure, a non-empty text answer, positive cost, and crucially, populated reasoning blocks if available.*


### test_o1_model_with_reasoning (method, L90-L120, parent: TestOpenAICompletionsClientReasoningModels)

> *Summary: This test verifies that the `o1-preview` model correctly extracts and returns reasoning blocks when prompted with a mathematical question. It asserts the response structure, checks for non-empty reasoning content, confirms the presence of a text answer, and validates that the associated cost is greater than zero.*


### TestOpenAICompletionsClientToolCalling (class, L123-L203)

> *Summary: This test suite verifies the OpenAI client's ability to handle function/tool calling with real API interactions. It tests two scenarios: first, ensuring the model correctly requests a specific tool call based on user input; and second, verifying the initial request structure when asking for external data like weather.*


### test_tool_calling_basic (method, L128-L169, parent: TestOpenAICompletionsClientToolCalling)

> *Summary: This test verifies basic tool calling by sending a prompt requesting an addition to the OpenAI client, which is expected to return a message containing a structured call to the defined `add_numbers` function with the correct input arguments (42 and 58). It asserts that the response successfully contains one such tool call matching the specified function name.*


### test_tool_calling_with_result (method, L173-L203, parent: TestOpenAICompletionsClientToolCalling)

> *Summary: This test verifies that the client correctly prompts an LLM to invoke a specified function, like `get_weather`, when given a user query. It asserts that the initial API response contains at least one recognized tool call matching the expected function name.*


### TestOpenAICompletionsClientStructuredOutput (class, L206-L400)

> *Summary: This test suite verifies the functionality of structured output generation when interacting with an OpenAI completions client. It executes several tests to confirm that the API correctly returns data conforming to JSON schemas, simple JSON objects, and custom Pydantic models, both when configured on the client instance and when passed directly in the request parameters.*


### test_structured_output_json_schema (method, L211-L256, parent: TestOpenAICompletionsClientStructuredOutput)

> *Summary: This test verifies that the OpenAI client correctly enforces a structured JSON output based on a provided schema. It sends a prompt to `gpt-4o-mini` with a specific JSON structure requirement and asserts that the resulting parsed object contains the expected keys and relevant content.*


### test_structured_output_simple_json (method, L260-L282, parent: TestOpenAICompletionsClientStructuredOutput)

> *Summary: This test verifies that the OpenAI client correctly generates a structured JSON response when explicitly requested via `response_format`. It sends a prompt asking for an explanation and asserts that the resulting text can be parsed as a non-empty dictionary.*


### test_structured_output_with_pydantic_model (method, L286-L324, parent: TestOpenAICompletionsClientStructuredOutput)

> *Summary: This test verifies that an OpenAI client can successfully generate structured output conforming to a Pydantic model. It sends a query, configures the client with the desired schema, and asserts that the returned response contains correctly parsed data matching the defined structure (question, answer, confidence).*


### test_structured_output_pydantic_in_params (method, L328-L361, parent: TestOpenAICompletionsClientStructuredOutput)

> *Summary: This test verifies that an OpenAI completions client can successfully generate structured output by passing a Pydantic model directly within the API request parameters. It asserts that the response contains a correctly parsed object matching the defined schema and validates its content against expected values.*


### test_structured_output_pydantic_override_default (method, L365-L400, parent: TestOpenAICompletionsClientStructuredOutput)

> *Summary: This test verifies that providing a `response_format` model within the API call parameters overrides any default response format configured on the client instance. It asserts that the resulting structured output adheres to the structure defined by the provided override model, ignoring the client's initial default model.*


### TestOpenAICompletionsClientImageUrlInput (class, L403-L459)

> *Summary: This test suite verifies the vision capabilities of an OpenAI completions client by sending requests containing a remote image URL. It asserts that the model correctly identifies the color and provides a detailed description based on the provided image input.*


### test_image_url_input (method, L411-L432, parent: TestOpenAICompletionsClientImageUrlInput)

> *Summary: This test verifies the client's ability to process image inputs provided via a URL when calling an OpenAI completion endpoint. It sends a prompt asking for the color of a specific image and asserts that the returned text contains the word "blue".*


### test_image_description (method, L439-L459, parent: TestOpenAICompletionsClientImageUrlInput)

> *Summary: This test verifies the image description capability by sending a specific image URL and a text prompt to an OpenAI completions client configured with `gpt-4o-mini`. It asserts that the resulting text description is substantial (over 50 characters) and that the API call incurred measurable costs.*


### TestOpenAICompletionsClientUsageAndCost (class, L462-L522)

> *Summary: This test suite verifies the functionality of an OpenAI completions client by executing API calls to generate responses. It asserts that usage metrics (tokens, cost) are correctly tracked from the response and validates that a separate cost calculation method matches the reported cost.*


### test_usage_tracking (method, L467-L487, parent: TestOpenAICompletionsClientUsageAndCost)

> *Summary: This test verifies that token and cost metrics are correctly captured after an API call. It sends a request to the OpenAI client, retrieves the associated usage data, and asserts that all expected keys are present and their values adhere to logical constraints (e.g., total tokens match prompt plus completion).*


### test_cost_calculation_accuracy (method, L491-L505, parent: TestOpenAICompletionsClientUsageAndCost)

> *Summary: This test verifies the accuracy of cost reporting by sending a request to an OpenAI completions client and asserting that the returned `cost` is positive and matches a manually calculated value derived from the response. It uses a specific prompt against the "gpt-4" model for this validation.*


### test_message_retrieval (method, L509-L522, parent: TestOpenAICompletionsClientUsageAndCost)

> *Summary: This test verifies the message retrieval functionality by sending a prompt to an OpenAI completions client and then extracting messages from the resulting response. It asserts that at least one non-empty string message is successfully retrieved.*


### TestOpenAICompletionsClientV1Compatibility (class, L525-L554)

> *Summary: This test verifies that the client correctly generates a response adhering to an older, v1-compatible format when provided with standard chat completion parameters. It asserts the presence and structure of specific keys like `id`, `choices`, and `usage` in the resulting dictionary output.*


### test_v1_compatible_format (method, L530-L554, parent: TestOpenAICompletionsClientV1Compatibility)

> *Summary: This test verifies that the client produces a response adhering to the older, v1 compatible format when given a prompt. It asserts the presence and correct structure of fields like `id`, `choices`, and `usage` within the returned dictionary.*


### TestOpenAICompletionsClientErrorHandling (class, L557-L578)

> *Summary: This test suite verifies the client's robustness by simulating API failures when calling the OpenAI completions endpoint. It asserts that exceptions are correctly raised when providing an invalid model name or empty message lists to the `create` method.*


### test_invalid_model_error (method, L562-L568, parent: TestOpenAICompletionsClientErrorHandling)

> *Summary: Asserts that calling the completion client with a non-existent model name raises an exception, verifying proper error handling from the OpenAI SDK. The function takes a configured client and expects an `Exception` when provided an invalid model string in the request payload.*


### test_empty_messages_error (method, L572-L578, parent: TestOpenAICompletionsClientErrorHandling)

> *Summary: Asserts that calling the completion client with an empty `messages` list raises an exception, verifying correct error handling for invalid input to the OpenAI API.*


### TestOpenAICompletionsClientMultiTurnConversation (class, L581-L630)

> *Summary: This test suite verifies the context-awareness of an OpenAI completions client by simulating multi-turn conversations. It asserts that the model retains information from previous turns and correctly adheres to a persistent system prompt instruction.*


### test_multi_turn_conversation (method, L586-L607, parent: TestOpenAICompletionsClientMultiTurnConversation)

> *Summary: This test verifies that an LLM client maintains conversational context across multiple turns. It sends an initial statement, then queries the model about that information after providing both the original user input and the model's previous response as history.*


### test_conversation_with_system_message (method, L611-L630, parent: TestOpenAICompletionsClientMultiTurnConversation)

> *Summary: This test verifies that an LLM client correctly incorporates a persistent system message into a conversation. It sends a prompt with a pirate persona instruction and asserts the resulting response contains characteristic pirate language or mentions the sea/ocean.*

