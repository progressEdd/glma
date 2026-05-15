# test/llm_clients/test_openai_completions_client.py

1 function(s): mock_openai_client. 14 class(es): MockOpenAIResponse, MockChoice, MockMessage, MockUsage, MockToolCall, TestOpenAICompletionsClientCreation, TestOpenAICompletionsClientCreate, TestOpenAICompletionsClientCost, TestOpenAICompletionsClientGetUsage, TestOpenAICompletionsClientMessageRetrieval, TestOpenAICompletionsClientV1Compatible, TestOpenAICompletionsClientIntegration, TestOpenAICompletionsClientGenericContent, TestOpenAICompletionsClientStructuredOutputs. 30 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MockOpenAIResponse | class |  |
| MockChoice | class |  |
| MockMessage | class |  |
| MockUsage | class |  |
| MockToolCall | class |  |
| mock_openai_client | function |  |
| TestOpenAICompletionsClientCreation | class |  |
| TestOpenAICompletionsClientCreate | class |  |
| TestOpenAICompletionsClientCost | class |  |
| TestOpenAICompletionsClientGetUsage | class |  |
| TestOpenAICompletionsClientMessageRetrieval | class |  |
| TestOpenAICompletionsClientV1Compatible | class |  |
| TestOpenAICompletionsClientIntegration | class |  |
| TestOpenAICompletionsClientGenericContent | class |  |
| TestOpenAICompletionsClientStructuredOutputs | class |  |

## Chunks

### MockOpenAIResponse (class, L22-L39)

> *Summary: Provides a mock object simulating an OpenAI API response, initialized with parameters like `response_id`, `model`, and optional lists for `choices` and dictionaries for `usage`. It serves as a controlled fixture to test code interacting with the actual OpenAI service.*


### __init__ (method, L25-L39, parent: MockOpenAIResponse)

> *Summary: Initializes an object representing an OpenAI completion response, accepting parameters like a response ID, model name, and optional data such as choices or usage statistics. It sets default values for these attributes and hardcodes a system fingerprint.*


### MockChoice (class, L42-L48)

> *Summary: Represents a mock object mirroring an OpenAI API choice structure. It initializes with a `message` content and an optional `finish_reason`, setting the index to zero by default.*


### __init__ (method, L45-L48, parent: MockChoice)

> *Summary: Initializes the client with a prompt message and an optional `finish_reason`, setting up internal state tracking via an index counter.*


### MockMessage (class, L51-L59)

> *Summary: Represents a mock message structure mirroring OpenAI response objects. It initializes with optional fields like `role`, `content`, `reasoning`, `tool_calls`, and `name` to simulate API responses for testing purposes.*


### __init__ (method, L54-L59, parent: MockMessage)

> *Summary: Initializes an object to hold parameters for an OpenAI completion request, accepting optional values for the assistant's role, message content, reasoning, tool calls, and a specific name. These attributes are stored internally for subsequent API interaction.*


### MockUsage (class, L62-L68)

> *Summary: Provides a mock object to simulate usage statistics for LLM interactions. It accepts optional initial values for prompt and completion tokens, calculating the total token count upon instantiation.*


### __init__ (method, L65-L68, parent: MockUsage)

> *Summary: Initializes the client by setting maximum token limits for both input prompts and generated completions, calculating a total token budget from these inputs.*


### MockToolCall (class, L71-L79)

> *Summary: This class simulates an OpenAI tool call by storing a unique ID, the intended function name, and its JSON-formatted arguments. It wraps these details into a mock object structure for testing purposes.*


### __init__ (method, L74-L79, parent: MockToolCall)

> *Summary: Initializes an instance by storing a unique `call_id` and creating a mock function object populated with the provided `name` and JSON string of `arguments`. This setup prepares the client to interact with external services using specified parameters.*


### mock_openai_client (function, L83-L90)

> *Summary: This function sets up a mock for the `OpenAI` class by patching its import within the module. It yields a mock instance of this client, allowing tests to control responses when interacting with OpenAI services.*


### TestOpenAICompletionsClientCreation (class, L93-L132)

> *Summary: This test suite verifies the initialization and core functionality of an OpenAI completions client. It checks that clients can be created with API keys or custom base URLs, validates that input roles are correctly normalized to an enum, and confirms the presence of all required methods on the instantiated client object.*


### test_create_client_with_api_key (method, L96-L100, parent: TestOpenAICompletionsClientCreation)

> *Summary: Verifies that instantiating the completion client with a provided API key successfully creates both the client object and its underlying HTTP client instance. It confirms the initialization process completes without errors.*


### test_role_normalization_to_enum (method, L102-L117, parent: TestOpenAICompletionsClientCreation)

> *Summary: This test verifies that the client correctly normalizes incoming role strings from an OpenAI mock response into a specific `UserRoleEnum`. It asserts that the resulting message's role is an instance of the enum and matches the expected value ("assistant").*


### test_create_client_with_base_url (method, L119-L122, parent: TestOpenAICompletionsClientCreation)

> *Summary: Verifies that an `OpenAICompletionsClient` instance can be successfully initialized using a custom `base_url`. The function takes no arguments other than the mock client and asserts the resulting client object is not null.*


### test_client_has_required_methods (method, L124-L132, parent: TestOpenAICompletionsClientCreation)

> *Summary: Verifies that an initialized `OpenAICompletionsClient` instance possesses all necessary methods (`create`, `cost`, etc.) required by the `ModelClientV2` interface. It confirms the client structure meets expected API contract requirements using a mock OpenAI client for setup.*


### TestOpenAICompletionsClientCreate (class, L135-L231)

> *Summary: This test suite verifies the `create` method of an OpenAI completions client by mocking various API responses. It confirms correct parsing and extraction of different output types, including simple text, structured reasoning blocks, tool calls, and usage statistics.*


### test_create_simple_response (method, L138-L157, parent: TestOpenAICompletionsClientCreate)

> *Summary: This test verifies the successful creation of a standardized response object when calling an OpenAI completions client. It mocks the API call to return a predefined structure and asserts that the resulting `UnifiedResponse` correctly extracts and contains the expected text, model information, and provider details.*


### test_create_response_with_reasoning (method, L159-L186, parent: TestOpenAICompletionsClientCreate)

> *Summary: This test verifies that the client correctly parses and extracts structured reasoning blocks from an OpenAI response containing both textual content and detailed reasoning. It asserts that the resulting object contains one `ReasoningContent` block with specific steps, alongside a separate text block containing the final answer.*


### test_create_response_with_tool_calls (method, L188-L211, parent: TestOpenAICompletionsClientCreate)

> *Summary: This test verifies that the client correctly extracts structured tool call information from an OpenAI response. It simulates a response containing one tool call and asserts that the resulting object contains the expected ID and function name.*


### test_create_response_with_usage (method, L213-L231, parent: TestOpenAICompletionsClientCreate)

> *Summary: This test verifies that the client correctly extracts token usage data from a mocked OpenAI API response. It asserts that the returned object contains the expected values for prompt, completion, and total tokens based on the mock setup.*


### TestOpenAICompletionsClientCost (class, L234-L272)

> *Summary: This test suite verifies the cost calculation logic within an OpenAI completions client by simulating API responses with known token usage. It asserts that the calculated cost matches expected values for specific models and confirms a fallback mechanism is used when encountering unknown model identifiers.*


### test_cost_calculation_o1_preview (method, L237-L256, parent: TestOpenAICompletionsClientCost)

> *Summary: This test verifies the cost calculation logic for a specific model (`o1-preview`) by mocking an OpenAI API response with predefined token usage. It asserts that the resulting calculated cost matches the expected value based on the model's pricing structure.*


### test_cost_calculation_unknown_model (method, L258-L272, parent: TestOpenAICompletionsClientCost)

> *Summary: This test verifies that the cost calculation mechanism defaults to a standard rate when an unsupported model is provided during API calls. It mocks an OpenAI response for an unknown model and asserts that the resulting calculated cost is greater than zero, indicating fallback pricing was applied.*


### TestOpenAICompletionsClientGetUsage (class, L275-L300)

> *Summary: This test verifies that the `get_usage` method correctly extracts and validates all expected metrics from a mocked OpenAI response object. It ensures the resulting dictionary contains specific keys like token counts, model name, and cost based on predefined mock data.*


### test_get_usage_returns_all_keys (method, L278-L300, parent: TestOpenAICompletionsClientGetUsage)

> *Summary: This test verifies that the `get_usage` method correctly extracts and returns all expected keys from a mocked OpenAI response object. It asserts that the returned dictionary contains specific token counts, model information, and a positive cost based on the mock input.*


### TestOpenAICompletionsClientMessageRetrieval (class, L303-L336)

> *Summary: This test suite verifies the `message_retrieval` functionality of an OpenAI client by simulating API responses. It asserts that the method correctly extracts and formats content from mock responses, either returning simple text or concatenating reasoning with the primary answer.*


### test_message_retrieval_simple_text (method, L306-L319, parent: TestOpenAICompletionsClientMessageRetrieval)

> *Summary: This test verifies that the message retrieval function correctly extracts text content from a mocked OpenAI response structure. It inputs a mock API response containing a single message and asserts that the output is a list containing the expected string content.*


### test_message_retrieval_with_reasoning (method, L321-L336, parent: TestOpenAICompletionsClientMessageRetrieval)

> *Summary: This test verifies that the client correctly extracts and combines both the primary answer and associated reasoning from a mocked OpenAI response. It asserts that the resulting message contains both the content ("Answer: 42") and the detailed thought process ("Let me think... 40 + 2 = 42").*


### TestOpenAICompletionsClientV1Compatible (class, L339-L379)

> *Summary: This test suite verifies that a client correctly transforms modern OpenAI API responses into an older, backward-compatible dictionary format. It asserts the structure of the output and specifically confirms that certain advanced features, like reasoning blocks, are lost during this compatibility conversion.*


### test_create_v1_compatible_format (method, L342-L361, parent: TestOpenAICompletionsClientV1Compatible)

> *Summary: This test verifies that the client correctly transforms an OpenAI API response into a backward-compatible dictionary format. It mocks an OpenAI response and asserts that the resulting output contains expected keys like `id`, `choices`, and `usage`.*


### test_v1_compatible_loses_reasoning (method, L363-L379, parent: TestOpenAICompletionsClientV1Compatible)

> *Summary: This test verifies that when using a v1-compatible API format, the reasoning blocks present in the input are lost in the resulting output. It mocks an OpenAI response containing structured messages and asserts that the returned dictionary only contains the flattened content.*


### TestOpenAICompletionsClientIntegration (class, L382-L437)

> *Summary: These tests validate the `OpenAICompletionsClient` by simulating a full workflow, asserting that the returned response correctly contains text, model information, and extracted reasoning steps from mocked OpenAI API calls. Additionally, one test verifies that the client adheres to a specific `ModelClientV2` protocol by checking for required methods and attributes.*


### test_full_workflow_with_reasoning (method, L385-L425, parent: TestOpenAICompletionsClientIntegration)

> *Summary: This test verifies the end-to-end workflow of an OpenAI client by mocking a response that includes structured reasoning. It asserts that the resulting `UnifiedResponse` correctly captures the model's text, provider details, associated usage metrics, and extracted reasoning steps from the mocked API output.*


### test_protocol_compliance (method, L427-L437, parent: TestOpenAICompletionsClientIntegration)

> *Summary: Verifies that an `OpenAICompletionsClient` adheres to the `ModelClientV2` protocol by checking for the presence of specific attributes and ensuring several key methods are callable. It confirms the client supports required functionalities like usage tracking, creation, and message retrieval.*


### TestOpenAICompletionsClientGenericContent (class, L440-L485)

> *Summary: This test verifies that the client correctly parses unknown fields within an OpenAI response message by treating them as `GenericContent` blocks. It simulates a mock API response containing extra fields like "thinking" and "confidence\_score" to assert that exactly two corresponding generic content blocks are extracted from the resulting message object.*


### test_unknown_message_field_as_generic_content (method, L448-L485, parent: TestOpenAICompletionsClientGenericContent)

> *Summary: When provided with a mock message containing unknown fields, this test verifies that the client correctly parses these extra attributes into separate `GenericContent` blocks within the response structure. It asserts that specific unknown fields like "thinking" and "confidence\_score" are captured as distinct content types in the final output.*


### TestOpenAICompletionsClientStructuredOutputs (class, L488-L715)

> *Summary: This test suite verifies the `OpenAICompletionsClient`'s handling of structured output requests, specifically when using Pydantic models or JSON schemas for response formatting. It ensures that the client correctly routes calls to either a specialized `.parse()` method (for Pydantic) or the standard `.create()` method (for raw JSON schema or no format specified), while also testing refusal handling and parameter overriding.*


### test_pydantic_model_detection (method, L491-L511, parent: TestOpenAICompletionsClientStructuredOutputs)

> *Summary: Verifies that the client correctly identifies Pydantic `BaseModel` instances while rejecting standard Python types and dictionaries. It asserts that a custom model inheriting from `BaseModel` returns `True`, whereas built-in types return `False`.*


### test_structured_output_with_pydantic_model (method, L513-L551, parent: TestOpenAICompletionsClientStructuredOutputs)

> *Summary: Verifies that when an `OpenAICompletionsClient` is initialized with a Pydantic model for structured output, the client correctly uses its internal `parse()` method instead of calling the underlying API's `create()` method to process the response. It confirms that the resulting object contains the data successfully parsed into the expected Pydantic structure.*


### test_structured_output_with_json_schema (method, L553-L590, parent: TestOpenAICompletionsClientStructuredOutputs)

> *Summary: This test verifies that the client correctly uses the `create()` method when a JSON schema is provided for structured output, rather than calling a parsing function. It asserts that the resulting response contains the expected structured content based on the mocked API call.*


### test_structured_output_with_refusal (method, L592-L622, parent: TestOpenAICompletionsClientStructuredOutputs)

> *Summary: This test verifies that the client correctly handles and extracts a refusal message when an LLM response is structured but explicitly declines to process the request. It mocks an OpenAI response containing a `refusal` attribute on the assistant's message, asserting that the resulting object contains this refusal content.*


### test_default_response_format_merged_into_params (method, L624-L654, parent: TestOpenAICompletionsClientStructuredOutputs)

> *Summary: This test verifies that a default `response_format` provided during client initialization is correctly merged into the API request parameters when calling completion methods. It asserts that the underlying mock client's parsing function is called with the expected default format object included in its arguments.*


### test_explicit_response_format_overrides_default (method, L656-L694, parent: TestOpenAICompletionsClientStructuredOutputs)

> *Summary: Verifies that providing an explicit `response_format` object during a client call overrides the default model configured on the client instance. It simulates an API response and asserts that the parsing mechanism correctly uses the explicitly provided format for deserialization.*


### test_no_response_format_uses_create (method, L696-L715, parent: TestOpenAICompletionsClientStructuredOutputs)

> *Summary: This test verifies that when an API request lacks a specified `response_format`, the underlying OpenAI client calls the `create()` method instead of the `parse()` method. It asserts that the returned object contains the expected text content from the mocked successful response.*

