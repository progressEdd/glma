# test/agentchat/group/test_on_condition.py

1 class(es): TestOnCondition. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestOnCondition | class |  |

## Chunks

### TestOnCondition (class, L20-L235)

> *Summary: This test suite verifies the initialization and behavior of an `OnCondition` object by testing various combinations of inputs for its target, condition, and availability checks. It confirms correct attribute assignment, method invocation on associated components (like getting prompts or checking availability), and type-specific logic like determining if a target requires wrapping.*


### test_init (method, L21-L31, parent: TestOnCondition)

> *Summary: This test verifies that an `OnCondition` object correctly stores the provided `TransitionTarget`, `StringLLMCondition`, and `StringAvailableCondition` mocks upon initialization. It asserts that the internal attributes match the input mock objects.*


### test_init_with_none_available (method, L33-L42, parent: TestOnCondition)

> *Summary: Verifies that an `OnCondition` instance correctly stores its provided `target`, `condition`, and the `available` status when initialized with `None`. This test confirms proper attribute assignment during object creation.*


### test_init_with_string_llm_condition (method, L44-L54, parent: TestOnCondition)

> *Summary: This test verifies the correct initialization of an `OnCondition` object when provided with a `StringLLMCondition`. It asserts that the resulting object correctly holds the specified target and the initialized string-based condition, including its prompt text.*


### test_init_with_context_str_llm_condition (method, L56-L67, parent: TestOnCondition)

> *Summary: This test verifies the correct initialization of an `OnCondition` object when provided with a `ContextStrLLMCondition`. It asserts that the resulting object correctly holds the specified target and condition, including verifying the nested `ContextStr` instance within the condition.*


### test_init_with_agent_target (method, L69-L80, parent: TestOnCondition)

> *Summary: This test verifies the correct initialization of an `OnCondition` object when provided with an `AgentTarget`. It confirms that the resulting object correctly holds a mock agent instance and its associated name.*


### test_init_with_string_available_condition (method, L82-L92, parent: TestOnCondition)

> *Summary: This test verifies the correct initialization of an `OnCondition` object when provided with a string-based availability condition. It asserts that the resulting object correctly holds the specified `StringAvailableCondition` instance and its associated context variable.*


### test_init_with_context_expression_available (method, L94-L102, parent: TestOnCondition)

> *Summary: This test verifies that an `OnCondition` object correctly stores a provided `StringAvailableCondition`. It initializes the object using mock targets and specific condition types to confirm the availability setting is set as expected.*


### test_condition_get_prompt (method, L105-L119, parent: TestOnCondition)

> *Summary: This test verifies that an `OnCondition` object correctly retrieves a prompt from its associated `StringLLMCondition`. It passes a mocked agent and message history to the condition's `get_prompt` method and asserts the returned value matches the configured prompt.*


### test_available_is_available (method, L122-L139, parent: TestOnCondition)

> *Summary: This test verifies that an `OnCondition` object correctly invokes the `is_available` method on its associated availability condition when executed with a mocked agent and message history. It asserts that the call returns `True`, confirming proper execution flow.*


### test_has_target_type (method, L141-L170, parent: TestOnCondition)

> *Summary: Verifies that an `OnCondition` object correctly identifies the type of its associated target by checking against provided class types. It tests this behavior across different target implementations, such as `AgentTarget`, `AgentNameTarget`, and `NestedChatTarget`.*


### test_target_requires_wrapping (method, L172-L188, parent: TestOnCondition)

> *Summary: Verifies that the `OnCondition` wrapper correctly determines if a target needs wrapping based on its type. It asserts that an `AgentTarget` does not require wrapping while a `NestedChatTarget` does.*


### test_llm_function_name_handling (method, L190-L202, parent: TestOnCondition)

> *Summary: This test verifies that an `OnCondition` object correctly stores and retrieves a specified LLM function name. It initializes the object without a name, then sets and asserts against a predefined string value.*


### test_integration_with_real_components (method, L204-L235, parent: TestOnCondition)

> *Summary: This test verifies the integration of `OnCondition` by setting up mock agents and conditions. It confirms that the available condition correctly evaluates based on provided context variables and that the LLM condition generates the expected prompt string when given a mock agent.*

