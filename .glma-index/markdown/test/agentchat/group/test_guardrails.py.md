# test/agentchat/group/test_guardrails.py

4 class(es): TestGuardrailResult, TestGuardrail, TestLLMGuardrail, TestRegexGuardrail. 30 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGuardrailResult | class |  |
| TestGuardrail | class |  |
| TestLLMGuardrail | class |  |
| TestRegexGuardrail | class |  |

## Chunks

### TestGuardrailResult (class, L15-L67)

> *Summary: This class provides unit tests for a `GuardrailResult` object, verifying its initialization with default or custom values, string representation, and parsing capabilities from JSON strings. It ensures correct behavior when handling both valid and invalid JSON inputs during the parsing process.*


### test_init_default (method, L16-L20, parent: TestGuardrailResult)

> *Summary: Verifies that a `GuardrailResult` object initializes correctly with default settings when constructed. It asserts the `activated` status is true and the `justification` defaults to "No justification provided".*


### test_init_with_justification (method, L22-L27, parent: TestGuardrailResult)

> *Summary: This test verifies that a `GuardrailResult` object correctly initializes when provided with a custom justification string. It asserts that the resulting instance reflects both the specified activation status and the input justification message.*


### test_str_representation (method, L29-L35, parent: TestGuardrailResult)

> *Summary: Verifies that the `GuardrailResult` object produces a specific, formatted string representation when converted to a string. It takes an instance with activation status and justification as input and asserts its output matches the predefined format.*


### test_parse_valid_json (method, L37-L42, parent: TestGuardrailResult)

> *Summary: This test verifies that a valid JSON string can be correctly parsed into a `GuardrailResult` object. It asserts that the resulting object accurately reflects the boolean activation status and the provided justification from the input JSON.*


### test_parse_valid_json_minimal (method, L44-L49, parent: TestGuardrailResult)

> *Summary: This test verifies that the `GuardrailResult` parser correctly processes a minimal valid JSON string input. It asserts that the resulting object accurately reflects the parsed boolean value and defaults to a specific justification message.*


### test_parse_invalid_json (method, L51-L58, parent: TestGuardrailResult)

> *Summary: This test verifies that attempting to parse a malformed JSON string using `GuardrailResult.parse` correctly raises a `ValueError`. It asserts that the exception message specifically indicates a parsing failure.*


### test_parse_invalid_structure (method, L60-L67, parent: TestGuardrailResult)

> *Summary: This test verifies that attempting to parse a JSON string with an invalid structure raises a `ValueError`. It asserts that the raised exception message specifically indicates a failure during GuardrailResult parsing.*


### TestGuardrail (class, L70-L112)

> *Summary: This test suite verifies the initialization behavior of a `Guardrail` object by creating mock and concrete instances. It asserts that the guardrail correctly stores its name, condition, target, and allows for setting a custom activation message upon instantiation.*


### mock_target (method, L72-L74, parent: TestGuardrail)

> *Summary: Generates a mock object conforming to the `TransitionTarget` interface. This is used within tests to simulate target objects without requiring actual implementation details.*


### concrete_guardrail (method, L77-L84, parent: TestGuardrail)

> *Summary: This method constructs and returns a mock `Guardrail` implementation for testing purposes. It defines an inner class that always activates its check, returning a predefined success result regardless of the input context.*


### test_init_default_activation_message (method, L86-L98, parent: TestGuardrail)

> *Summary: Verifies that a `Guardrail` instance initializes correctly with default settings, specifically asserting the presence of a predefined activation message upon instantiation. It uses a concrete implementation to confirm attribute assignment for name, condition, and target.*


### test_init_custom_activation_message (method, L100-L112, parent: TestGuardrail)

> *Summary: This test verifies that a `Guardrail` instance correctly stores a provided custom activation message during initialization. It instantiates a mock guardrail with a specific message and asserts the stored value matches the input.*


### TestLLMGuardrail (class, L115-L223)

> *Summary: These tests verify the functionality of an LLM guardrail by mocking external dependencies like `OpenAIWrapper` and configuration objects. It confirms correct initialization, validates that the guardrail can process both string and list contexts to determine activation status based on mock LLM responses, and ensures proper response format configuration is applied.*


### mock_target (method, L117-L119, parent: TestLLMGuardrail)

> *Summary: Generates a mock object conforming to the `TransitionTarget` interface. This is used within tests to simulate target objects without requiring actual implementation details.*


### mock_llm_config (method, L122-L127, parent: TestLLMGuardrail)

> *Summary: Generates a `MagicMock` object configured to simulate an LLM configuration for testing purposes. This mock ensures that calls to `deepcopy()` and `model_dump()` return predictable, testable values.*


### mock_openai_wrapper (method, L130-L137, parent: TestLLMGuardrail)

> *Summary: This method constructs and returns a mocked `OpenAIWrapper` object configured to simulate a successful API call. The mock is set up so that any call to its `create` method returns a response containing a JSON string indicating activation with a specific justification.*


### test_init_valid_config (method, L139-L151, parent: TestLLMGuardrail)

> *Summary: Verifies that an `LLMGuardrail` object initializes correctly when provided with valid configuration parameters like a name, condition string, target, and LLM settings. It confirms the internal state matches the inputs and ensures the underlying OpenAI wrapper is called upon instantiation.*


### test_check_with_string_context (method, L153-L181, parent: TestLLMGuardrail)

> *Summary: This test verifies the `LLMGuardrail`'s behavior when checking a string context against an LLM. It mocks the OpenAI wrapper to simulate a successful guardrail activation and asserts that the resulting object reflects this, while also confirming the correct system and user messages were sent to the mocked LLM API call.*


### test_check_with_list_context (method, L183-L211, parent: TestLLMGuardrail)

> *Summary: This test verifies the `LLMGuardrail`'s behavior when processing a list of conversational messages. It mocks an OpenAI wrapper to simulate a non-violating response and asserts that the guardrail correctly reports no activation while also confirming the input messages were passed to the LLM with the correct system prompt prepended.*


### test_check_response_format_configuration (method, L213-L223, parent: TestLLMGuardrail)

> *Summary: This test verifies that an `LLMGuardrail` correctly configures the response format when initialized with mock dependencies. It asserts that a deep copy operation is called on the provided LLM configuration object to ensure proper setup.*


### TestRegexGuardrail (class, L226-L370)

> *Summary: This test suite verifies the functionality of a `RegexGuardrail` by testing its initialization with valid and invalid regular expressions. It confirms that the guardrail correctly activates or deactivates based on whether a provided string or list context contains a match for the configured regex pattern, handling various scenarios like case sensitivity and multiple matches.*


### mock_target (method, L228-L230, parent: TestRegexGuardrail)

> *Summary: Generates a mock object conforming to the `TransitionTarget` interface. This is used within tests to simulate target objects without needing actual implementation details.*


### test_init_valid_regex (method, L232-L240, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` initializes correctly when provided with a valid regular expression string and a target object. It asserts that the guardrail stores the correct name, condition pattern, target, and successfully compiles the regex into a `re.Pattern`.*


### test_init_invalid_regex (method, L242-L250, parent: TestRegexGuardrail)

> *Summary: Verifies that attempting to initialize a `RegexGuardrail` with an improperly formed regular expression raises a `ValueError`. The test confirms the exception message correctly indicates an "Invalid regex pattern" and includes the problematic input string.*


### test_check_string_context_match (method, L252-L261, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` correctly activates when the provided string context matches its defined regular expression pattern. It asserts that the resulting check object indicates activation and contains the expected justification message.*


### test_check_string_context_no_match (method, L263-L272, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` correctly deactivates when its specified pattern does not appear within the input string context. It asserts that the resulting check indicates no activation and provides a specific "No match found" justification.*


### test_check_list_context_match (method, L274-L286, parent: TestRegexGuardrail)

> *Summary: This test verifies that a `RegexGuardrail` correctly activates when its defined pattern matches content within a provided list of chat messages. It asserts that the guardrail's activation status is true and that the justification message includes the matched term.*


### test_check_list_context_no_match (method, L288-L300, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` correctly deactivates when its specified pattern does not appear within the provided conversation history. It asserts that the resulting check indicates no activation and provides a specific "No match found" justification.*


### test_check_list_context_missing_content (method, L302-L314, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` correctly deactivates when checking a conversation history where one message lacks the required content field. It asserts that no match is found and the justification reflects this absence of content.*


### test_check_case_sensitive_match (method, L316-L328, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` correctly enforces case sensitivity when checking input against a predefined pattern. It asserts the guardrail remains inactive for lowercase text but activates successfully for matching uppercase text.*


### test_check_case_insensitive_pattern (method, L330-L340, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` correctly triggers when its case-insensitive pattern matches input strings regardless of capitalization. It confirms activation for both lowercase and uppercase instances of the target word.*


### test_check_complex_regex_pattern (method, L342-L355, parent: TestRegexGuardrail)

> *Summary: This test verifies a `RegexGuardrail`'s functionality by checking if it correctly identifies complex patterns, specifically validating that a provided regex matches a valid email string while failing to match an improperly formatted one. It uses a mock target to execute the guardrail check against sample input strings.*


### test_check_multiple_matches_returns_first (method, L357-L370, parent: TestRegexGuardrail)

> *Summary: Verifies that a `RegexGuardrail` stops and reports only upon finding the initial match within an input context. It takes a list of message dictionaries as input and returns a result indicating activation with justification detailing the first matched pattern.*

