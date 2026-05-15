# test/agentchat/group/test_on_context_condition.py

1 class(es): TestOnContextCondition. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestOnContextCondition | class |  |

## Chunks

### TestOnContextCondition (class, L14-L133)

> *Summary: This test suite verifies the initialization and basic evaluation logic of an `OnContextCondition` object. It confirms that the constructor correctly accepts and stores various types for target, condition (like string or expression-based), and availability checks, and it tests calling the respective `.evaluate()` and `.is_available()` methods on these components.*


### test_init (method, L15-L25, parent: TestOnContextCondition)

> *Summary: This test verifies that an `OnContextCondition` object correctly stores the provided mock instances for its target, context condition, and availability checks upon initialization. It confirms that the constructor successfully assigns these dependencies to the instance attributes.*


### test_init_with_none_available (method, L27-L36, parent: TestOnContextCondition)

> *Summary: Verifies that an `OnContextCondition` instance correctly stores its provided `target`, `condition`, and the initial `available` state, even when `available` is set to `None`. This test confirms proper initialization behavior for the context condition object.*


### test_init_with_string_context_condition (method, L38-L49, parent: TestOnContextCondition)

> *Summary: Verifies that an `OnContextCondition` object correctly initializes with a specific `StringContextCondition`. It confirms the target and condition attributes are set as expected, including checking the variable name within the string condition.*


### test_init_with_expression_context_condition (method, L51-L63, parent: TestOnContextCondition)

> *Summary: This test verifies the correct initialization of an `OnContextCondition` object when provided with an `ExpressionContextCondition`. It asserts that the resulting object correctly holds references to the specified target and the constructed expression-based condition.*


### test_init_with_agent_target (method, L65-L77, parent: TestOnContextCondition)

> *Summary: This test verifies the correct initialization of an `OnContextCondition` by providing an `AgentTarget`. It asserts that the resulting object correctly holds a mock agent instance and its associated name within the target structure.*


### test_init_with_string_available_condition (method, L79-L90, parent: TestOnContextCondition)

> *Summary: This test verifies the correct initialization of an `OnContextCondition` object when provided with specific condition and availability checks. It asserts that the resulting object correctly holds a `StringAvailableCondition` instance configured for the variable `"is_available"`.*


### test_init_with_context_expression_available (method, L92-L100, parent: TestOnContextCondition)

> *Summary: Verifies that an `OnContextCondition` instance correctly stores the provided `StringAvailableCondition`. It initializes the object using mock targets and specific context conditions to confirm attribute assignment.*


### test_condition_evaluate (method, L102-L116, parent: TestOnContextCondition)

> *Summary: This test verifies that an `OnContextCondition` correctly invokes its associated condition's evaluation method when provided with a context object. It asserts that the evaluation returns `True` based on the mocked inputs.*


### test_available_is_available (method, L118-L133, parent: TestOnContextCondition)

> *Summary: This test verifies that an `OnContextCondition` correctly invokes its associated `StringAvailableCondition`'s `is_available` method when provided with a mock agent and message history. It asserts that the call returns `True`, confirming the availability check passes under these conditions.*

