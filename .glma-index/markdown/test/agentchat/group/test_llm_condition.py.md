# test/agentchat/group/test_llm_condition.py

3 class(es): TestLLMCondition, TestStringLLMCondition, TestContextStrLLMCondition. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLLMCondition | class |  |
| TestStringLLMCondition | class |  |
| TestContextStrLLMCondition | class |  |

## Chunks

### TestLLMCondition (class, L24-L45)

> *Summary: Verifies that an un-overridden implementation of the `LLMCondition` protocol correctly raises a `NotImplementedError`. It also confirms that instantiating the base class without parameters results in a callable object that immediately fails when its required method is invoked.*


### test_protocol_raise_not_implemented (method, L25-L37, parent: TestLLMCondition)

> *Summary: Verifies that an implementation of the `LLMCondition` protocol correctly raises a `NotImplementedError` when its required `get_prompt` method is present but not fully overridden by the subclass. It asserts that the raised exception contains a specific message indicating the requirement for further implementation.*


### test_initialisation_with_no_parameters (method, L39-L45, parent: TestLLMCondition)

> *Summary: Verifies that an instance of the base class can be created without arguments and confirms that calling its `get_prompt` method raises a `NotImplementedError`, indicating it requires further implementation.*


### TestStringLLMCondition (class, L48-L100)

> *Summary: This test suite verifies the behavior of a string-based LLM condition checker. It ensures that an instance is correctly initialized with a given prompt string and that the `get_prompt` method consistently returns this static prompt, regardless of any provided agent or message inputs.*


### test_init (method, L49-L53, parent: TestStringLLMCondition)

> *Summary: Verifies that an instance of `StringLLMCondition` correctly stores the provided input prompt string upon initialization. It confirms the internal state matches the initial argument passed to the constructor.*


### test_get_prompt (method, L55-L65, parent: TestStringLLMCondition)

> *Summary: This test verifies that the `StringLLMCondition` instance returns its initialized static prompt string when `get_prompt` is called, regardless of provided agent or message inputs. It asserts that the output exactly matches the input prompt used during initialization.*


### test_get_prompt_ignores_agent_and_messages (method, L67-L81, parent: TestStringLLMCondition)

> *Summary: Verifies that the `StringLLMCondition`'s `get_prompt` method returns only the initial prompt string, regardless of which mock agent or message list is provided as input. It asserts that calling the method with different agents and messages yields identical results equal to the configured prompt.*


### test_init_with_empty_prompt (method, L83-L89, parent: TestStringLLMCondition)

> *Summary: When initialized with an empty prompt string, this test verifies that the resulting `StringLLMCondition` object retains the empty prompt. It further asserts that calling `get_prompt` on the instance with a mock agent and no history returns an empty string.*


### test_init_with_multiline_prompt (method, L91-L100, parent: TestStringLLMCondition)

> *Summary: Verifies that an instance initialized with a multi-line string correctly stores the prompt and returns it unchanged when queried against a mock agent. The function confirms the `StringLLMCondition` accurately handles and retrieves complex input prompts.*


### TestContextStrLLMCondition (class, L103-L245)

> *Summary: This class tests the functionality of an LLM condition that generates prompts from a `ContextStr` object. It verifies that the prompt correctly substitutes placeholders using context variables provided by a mocked agent, handling cases with multiple variables, missing keys, and nested data structures.*


### test_init (method, L104-L108, parent: TestContextStrLLMCondition)

> *Summary: Verifies that an instance of `ContextStrLLMCondition` correctly stores the provided `ContextStr` mock object upon initialization. It confirms the internal state matches the input argument.*


### test_get_prompt (method, L111-L132, parent: TestContextStrLLMCondition)

> *Summary: This test verifies that the `get_prompt` method correctly formats a prompt string using an agent's context variables. It asserts that the underlying formatting function is called once with the provided context and returns the expected formatted output.*


### test_get_prompt_with_real_context_str (method, L134-L150, parent: TestContextStrLLMCondition)

> *Summary: This test verifies that a `ContextStrLLMCondition` correctly substitutes variables from an agent's context into a template string when generating a prompt. It asserts that the resulting prompt matches the expected string after replacing placeholders like `{x}` with actual values provided in the mock agent's context.*


### test_get_prompt_with_multiple_variables (method, L152-L170, parent: TestContextStrLLMCondition)

> *Summary: This test verifies that a `ContextStrLLMCondition` correctly formats a prompt template containing multiple placeholders using provided context variables. It inputs a mock agent with specific data and asserts the output matches the fully substituted string.*


### test_get_prompt_with_missing_variables (method, L172-L191, parent: TestContextStrLLMCondition)

> *Summary: This test verifies that the prompt generation mechanism correctly raises a `KeyError` when required context variables are absent from the provided agent's data. It specifically asserts that the missing variable name is present within the raised exception message.*


### test_init_with_template_string (method, L193-L197, parent: TestContextStrLLMCondition)

> *Summary: Verifies that the `ContextStrLLMCondition` constructor strictly requires a `ContextStr` object for its context input, raising a `ValidationError` if a raw string is provided instead.*


### test_get_prompt_with_empty_context_variables (method, L199-L216, parent: TestContextStrLLMCondition)

> *Summary: Verifies that when an LLM condition is initialized with a static prompt template and provided an agent lacking context variables, it returns the original template unmodified. The function takes a mock agent and message list as input to test this behavior.*


### test_integration_with_nested_context_variables (method, L218-L245, parent: TestContextStrLLMCondition)

> *Summary: This test verifies that an LLM condition correctly formats a prompt using nested context variables. It passes a mock agent containing structured data, expecting the resulting prompt string to accurately embed the deeply nested dictionary structure.*

