# test/agentchat/group/test_handoffs.py

1 class(es): TestHandoffs. 38 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestHandoffs | class |  |

## Chunks

### TestHandoffs (class, L23-L483)

> *Summary: This test suite verifies the functionality of a `Handoffs` object, which manages lists of context conditions, LLM conditions, and after-work transitions. It extensively tests methods for adding, setting, clearing, and retrieving these components, ensuring correct type validation and method chaining behavior.*


### mock_agent_target (method, L25-L29, parent: TestHandoffs)

> *Summary: Generates a simulated `AgentTarget` object populated with a mocked agent instance named "test\_agent". This helper is used to provide predictable, testable targets for group interaction scenarios.*


### mock_agent_name_target (method, L32-L34, parent: TestHandoffs)

> *Summary: Generates a predefined `AgentNameTarget` object, specifically setting the agent name to "test\_agent", for use in tests.*


### mock_nested_chat_target (method, L37-L40, parent: TestHandoffs)

> *Summary: Generates a mock `NestedChatTarget` object configured with a list of chat queues and asynchronous usage enabled. This helper is used to simulate complex nested chat scenarios during testing.*


### mock_on_context_condition (method, L43-L46, parent: TestHandoffs)

> *Summary: Generates a mock `OnContextCondition` object by pairing a provided `AgentTarget` with a predefined string context condition. This helper is used to simulate specific trigger conditions during testing scenarios.*


### mock_on_condition (method, L49-L52, parent: TestHandoffs)

> *Summary: Generates a mock `OnCondition` object by pairing a provided `AgentTarget` with a predefined string-based LLM condition. This helper is used specifically for testing scenarios involving agent handoffs.*


### mock_on_context_condition_require_wrapping (method, L55-L59, parent: TestHandoffs)

> *Summary: Generates a mock `OnContextCondition` object for testing purposes. It constructs this by pairing a specific string-based context condition with a nested chat target configuration involving multiple agents and asynchronous use.*


### mock_on_condition_require_wrapping (method, L62-L66, parent: TestHandoffs)

> *Summary: Generates a mock `OnCondition` object for testing purposes. It combines a simple string-based LLM condition with a nested chat target configured to queue messages between two agents asynchronously.*


### mock_after_work (method, L69-L71, parent: TestHandoffs)

> *Summary: This method creates and returns a mock `AfterWork` target by directly returning the provided `AgentTarget`. It serves to simulate an "after work" state during testing scenarios.*


### test_init_empty (method, L73-L78, parent: TestHandoffs)

> *Summary: Verifies that a newly instantiated `Handoffs` object initializes its condition lists—context, LLM, and after-work—to be empty. This confirms the default state when no conditions are provided during setup.*


### test_init_with_conditions (method, L80-L96, parent: TestHandoffs)

> *Summary: This test verifies that an `Handoffs` object correctly initializes and stores provided context, LLM, and after-work conditions. It asserts the internal lists match the input mocks and confirms the structure of the single configured after-work transition.*


### test_add_context_condition (method, L98-L104, parent: TestHandoffs)

> *Summary: This test verifies that adding a single `OnContextCondition` to an instance correctly populates the internal list of context conditions and returns the modified object for method chaining.*


### test_add_context_condition_invalid_type (method, L106-L113, parent: TestHandoffs)

> *Summary: This test verifies that attempting to add an improperly typed argument to the `Handoffs` object raises a `TypeError`. It confirms the exception message specifically indicates that an `OnContextCondition` instance was expected.*


### test_add_context_conditions (method, L115-L126, parent: TestHandoffs)

> *Summary: This test verifies that the `Handoffs` object correctly accepts and stores a list of multiple context conditions provided as input. It asserts that the internal list of conditions matches the input and that the method returns the instance itself, enabling method chaining.*


### test_add_context_conditions_invalid_type (method, L128-L135, parent: TestHandoffs)

> *Summary: This test verifies that attempting to add an improperly typed element to the `Handoffs` object raises a `TypeError`. It asserts that the raised exception message specifically indicates that all added conditions must conform to the `OnContextCondition` type.*


### test_add_llm_condition (method, L137-L143, parent: TestHandoffs)

> *Summary: This test verifies that adding a single `OnCondition` object to an instance correctly populates the internal list of LLM conditions and returns the modified instance for method chaining.*


### test_add_llm_condition_invalid_type (method, L145-L152, parent: TestHandoffs)

> *Summary: This test verifies that attempting to add a non-`OnCondition` object to the `Handoffs` instance raises a `TypeError`. It confirms the error message specifically indicates the expected type mismatch.*


### test_add_llm_conditions (method, L154-L165, parent: TestHandoffs)

> *Summary: This test verifies that the `Handoffs` object correctly accepts and stores an array of `OnCondition` objects when calling `add_llm_conditions`. It asserts that the internal list of conditions matches the input and that the method returns the instance itself for fluent API usage.*


### test_add_llm_conditions_invalid_type (method, L167-L174, parent: TestHandoffs)

> *Summary: This test verifies that attempting to add a non-`OnCondition` type to the `Handoffs` object correctly raises a `TypeError`. It asserts that the raised exception message specifically indicates all added conditions must be of type `OnCondition`.*


### test_set_after_work (method, L176-L184, parent: TestHandoffs)

> *Summary: This test verifies that the `set_after_work` method correctly registers a provided transition target into the `Handoffs` object's list of after-work conditions. It asserts that exactly one condition is added, matches the input target, has no associated condition, and that the method returns the instance for chaining.*


### test_set_after_work_invalid_type (method, L186-L193, parent: TestHandoffs)

> *Summary: This test verifies that attempting to set an invalid data type for the `after_work` attribute raises a `TypeError`. It confirms the exception message specifically indicates that a `TransitionTarget` instance was expected.*


### test_set_after_work_multiple_times (method, L195-L209, parent: TestHandoffs)

> *Summary: This test verifies that repeatedly calling a setter method overwrites the previous value instead of accumulating them. It confirms that after setting two different transition targets, only the last provided target remains in the internal list.*


### test_add_on_context_condition (method, L211-L217, parent: TestHandoffs)

> *Summary: This test verifies that an `OnContextCondition` object is correctly added to a `Handoffs` instance via the generic `add` method. It asserts that the condition appears in the internal list and that the method returns the modified `Handoffs` object itself for fluent chaining.*


### test_add_on_condition (method, L219-L225, parent: TestHandoffs)

> *Summary: This test verifies that an `OnCondition` object is correctly added to a set of handoffs via the generic `add` method. It asserts that the condition is present in the internal list and that the method returns the modified handoffs instance for fluent API usage.*


### test_add_invalid_type (method, L227-L234, parent: TestHandoffs)

> *Summary: This test verifies that attempting to add an improperly typed value to the `Handoffs` object correctly raises a `TypeError`. It asserts that the raised exception message specifically indicates an unsupported condition type.*


### test_add_many (method, L236-L243, parent: TestHandoffs)

> *Summary: This test verifies that the `add_many` method correctly registers multiple conditions into a `Handoffs` object, separating context and LLM conditions. It asserts that the returned instance allows for method chaining by returning itself.*


### test_add_many_invalid_type (method, L245-L252, parent: TestHandoffs)

> *Summary: This test verifies that attempting to add multiple items of an invalid type to the `Handoffs` object raises a `TypeError`. It asserts that the raised exception message specifically indicates an "Unsupported condition type."*


### test_add_empty_lists (method, L254-L269, parent: TestHandoffs)

> *Summary: Verifies that adding empty lists to the `Handoffs` object correctly initializes or maintains empty condition sets for both context and LLM conditions, while ensuring methods support method chaining by returning `self`.*


### test_clear (method, L271-L289, parent: TestHandoffs)

> *Summary: This test verifies that the `clear` method successfully empties all internal condition and target lists within a `Handoffs` instance. It asserts that after calling `clear()`, the context conditions, LLM conditions, and after-work targets are all empty, while also confirming the method returns the instance itself for chaining.*


### test_adding_after_clear (method, L291-L319, parent: TestHandoffs)

> *Summary: This test verifies that after clearing existing configurations, the system correctly accepts and stores newly added context conditions, LLM conditions, and a transition target. It asserts that the internal lists are updated with the provided mock objects.*


### test_get_llm_conditions_by_target_type (method, L321-L333, parent: TestHandoffs)

> *Summary: This test verifies that a `Handoffs` object correctly filters and returns LLM conditions based on the provided target type. It asserts that all conditions are returned for an `AgentTarget` but none are returned for a `NestedChatTarget`.*


### test_get_context_conditions_by_target_type (method, L335-L347, parent: TestHandoffs)

> *Summary: This test verifies that a `Handoffs` object correctly filters and returns context conditions based on the provided target type. It asserts that all conditions are returned for an `AgentTarget` but none are returned for a `NestedChatTarget`.*


### test_get_llm_conditions_requiring_wrapping (method, L349-L363, parent: TestHandoffs)

> *Summary: This test verifies the logic for identifying LLM conditions that necessitate wrapping within a `Handoffs` object. It asserts that an empty list is returned when no condition requires wrapping, but returns the specific condition when one does.*


### test_get_context_conditions_requiring_wrapping (method, L365-L381, parent: TestHandoffs)

> *Summary: This test verifies the logic for identifying context conditions that necessitate wrapping within a `Handoffs` object. It asserts that an empty list is returned when no condition requires wrapping, and correctly returns the specific condition when one does.*


### test_set_llm_function_names (method, L383-L402, parent: TestHandoffs)

> *Summary: This test verifies that the `Handoffs` object correctly assigns indexed function names to its constituent conditions when calling `set_llm_function_names()`. It ensures that each condition receives a unique name formatted as "transfer\_to\_[normalized\_name]\_[index]".*


### test_set_llm_function_names_empty (method, L404-L412, parent: TestHandoffs)

> *Summary: Verifies that initializing and calling `set_llm_function_names` on an `Handoffs` object with no provided names results in an empty condition list without errors. The function confirms the internal state remains unchanged when given an empty input set of function names.*


### test_set_llm_function_names_complex (method, L414-L433, parent: TestHandoffs)

> *Summary: This test verifies that when multiple transition targets share the same normalized name, the system correctly assigns unique LLM function names to each associated condition. It inputs three conditions pointing to a target named "same\_target" and asserts that `set_llm_function_names()` results in distinct, sequentially numbered function names for all three.*


### test_adding_duplicate_conditions (method, L435-L456, parent: TestHandoffs)

> *Summary: This test verifies that the `Handoffs` object allows adding identical context and LLM conditions multiple times without automatically deduplicating them. It asserts that both the context and LLM condition lists contain two instances of the same provided mocks after being added twice.*


### test_method_chaining (method, L458-L483, parent: TestHandoffs)

> *Summary: This test verifies that a `Handoffs` object correctly chains multiple configuration methods by returning itself after each call. It asserts that the added context condition, LLM condition, and after-work target are successfully stored on the instance.*

