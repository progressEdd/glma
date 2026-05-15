# test/agentchat/group/test_transition_events.py

5 class(es): TestTransitionEvents, TestAfterWorksTransitionEvent, TestOnContextConditionTransitionEvent, TestOnConditionLLMTransitionEvent, TestReplyResultTransitionEvent. 29 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTransitionEvents | class |  |
| TestAfterWorksTransitionEvent | class |  |
| TestOnContextConditionTransitionEvent | class |  |
| TestOnConditionLLMTransitionEvent | class |  |
| TestReplyResultTransitionEvent | class |  |

## Chunks

### TestTransitionEvents (class, L20-L38)

> *Summary: This test fixture setup provides mocked instances of an `Agent`, a `TransitionTarget`, and a `GroupToolExecutor`. These mocks are used to isolate and test the logic related to transition events within a group context.*


### mock_agent (method, L22-L26, parent: TestTransitionEvents)

> *Summary: This method constructs and returns a mocked `Agent` object, pre-setting its name to "TestAgent" for use in tests. It allows test code to simulate the behavior of an actual agent without needing a full implementation.*


### mock_transition_target (method, L29-L33, parent: TestTransitionEvents)

> *Summary: Generates a mocked `TransitionTarget` object configured to return "TestTarget" when its `display_name` method is called, facilitating isolated testing of transition logic.*


### executor (method, L36-L38, parent: TestTransitionEvents)

> *Summary: Instantiates and returns a `GroupToolExecutor` instance, primarily used to set up the environment for group-related testing.*


### TestAfterWorksTransitionEvent (class, L41-L70)

> *Summary: This test suite verifies the correct initialization and behavior of an `AfterWorksTransitionEvent`. It ensures the event correctly stores its source agent and transition target, outputs the expected type identifier when serialized, and prints a descriptive message containing agent names.*


### event (method, L43-L45, parent: TestAfterWorksTransitionEvent)

> *Summary: Constructs and returns an `AfterWorksTransitionEvent` by accepting a mock agent and a mock transition target as inputs. This method is specifically designed for testing purposes to create the necessary event object.*


### test_initialization (method, L47-L53, parent: TestAfterWorksTransitionEvent)

> *Summary: Verifies that an `AfterWorksTransitionEvent` correctly stores the provided source agent and transition target within its wrapped content field upon initialization. It asserts that the internal state matches the input parameters passed to the constructor.*


### test_event_type (method, L55-L58, parent: TestAfterWorksTransitionEvent)

> *Summary: Verifies that an `AfterWorksTransitionEvent` correctly exposes its specific event type as `"after_works_transition"` when serialized via `model_dump()`. This confirms the decorator successfully sets the intended event classification.*


### test_print_with_agent_name (method, L60-L70, parent: TestAfterWorksTransitionEvent)

> *Summary: This test verifies that the `print` method on an event's content correctly outputs a string containing both the agent's name and target information. It asserts that the mock print function was called exactly once with the expected descriptive message.*


### TestOnContextConditionTransitionEvent (class, L73-L101)

> *Summary: This test suite verifies the correct initialization and behavior of an `OnContextConditionTransitionEvent`. It ensures the event correctly stores its source agent and target, has the proper type identifier when serialized, and prints descriptive information containing agent names.*


### event (method, L75-L77, parent: TestOnContextConditionTransitionEvent)

> *Summary: Constructs and returns an `OnContextConditionTransitionEvent` by accepting a mock agent and a mock transition target as inputs. This method is specifically designed for testing purposes to create the required event object.*


### test_initialization (method, L79-L84, parent: TestOnContextConditionTransitionEvent)

> *Summary: Verifies that an `OnContextConditionTransitionEvent` correctly stores the provided source agent and transition target within its content upon initialization. It asserts that the internal attributes match the input mocks.*


### test_event_type (method, L86-L89, parent: TestOnContextConditionTransitionEvent)

> *Summary: Verifies that an incoming `OnContextConditionTransitionEvent` correctly has its `"type"` field set to `"on_context_condition_transition"` after being processed by the `@wrap_event` decorator. This confirms the event's classification upon serialization.*


### test_print_with_agent_name (method, L91-L101, parent: TestOnContextConditionTransitionEvent)

> *Summary: This test verifies that the `print` method on an event's content correctly formats and outputs a message when the associated agent has a name. It asserts that the output string contains specific identifiers like "OnContextCondition handoff," "TestAgent," and "TestTarget."*


### TestOnConditionLLMTransitionEvent (class, L104-L177)

> *Summary: This test suite verifies the functionality of an `OnConditionLLMTransitionEvent` by checking its correct initialization, event typing, and string representation when printed. It also extensively tests a private method that sends this handoff event via an IOStream, ensuring it only fires correctly when both a valid sender agent and a recognized handoff function are present.*


### event (method, L106-L108, parent: TestOnConditionLLMTransitionEvent)

> *Summary: Constructs an `OnConditionLLMTransitionEvent` by accepting a mock agent and a mock transition target as inputs. This method is specifically designed to create test instances of the event object.*


### test_initialization (method, L110-L115, parent: TestOnConditionLLMTransitionEvent)

> *Summary: Verifies that an `OnConditionLLMTransitionEvent` correctly stores the provided source agent and transition target upon instantiation. It asserts that the event's content attributes match the input mocks.*


### test_event_type (method, L117-L120, parent: TestOnConditionLLMTransitionEvent)

> *Summary: Verifies that an `OnConditionLLMTransitionEvent` correctly has its `"type"` field set to `"on_condition_l_l_m_transition"` after being serialized. This confirms the decorator is assigning the expected event type identifier.*


### test_print_with_agent_name (method, L122-L132, parent: TestOnConditionLLMTransitionEvent)

> *Summary: This test verifies that the `print` method on an event's content correctly outputs a formatted string when the associated agent has a name. It asserts that the output includes specific identifiers for the transition type and both the source and target agents.*


### test_send_llm_handoff_event (method, L135-L177, parent: TestOnConditionLLMTransitionEvent)

> *Summary: This test verifies the logic for sending an LLM handoff event based on message content and agent status. It asserts that the `send` method of the I/O stream is only called when a message originates from a recognized handoff function and has an associated sender agent, correctly packaging the transition details into an `OnConditionLLMTransitionEvent`.*


### TestReplyResultTransitionEvent (class, L180-L313)

> *Summary: This test suite verifies the functionality of a `ReplyResultTransitionEvent` by instantiating it with mock agents and targets. It confirms correct initialization, property accessibility, serialization structure via `model_dump`, and proper behavior when printing to standard output or custom functions.*


### event (method, L182-L184, parent: TestReplyResultTransitionEvent)

> *Summary: Constructs and returns a `ReplyResultTransitionEvent` by accepting mock instances of an `Agent` and a `TransitionTarget`. This method is specifically designed for creating test event objects.*


### test_initialization (method, L186-L192, parent: TestReplyResultTransitionEvent)

> *Summary: Verifies that an `ReplyResultTransitionEvent` correctly stores the provided source agent and transition target within its wrapped content field upon initialization. It asserts that the internal attributes match the input mocks.*


### test_model_config_allows_arbitrary_types (method, L194-L197, parent: TestReplyResultTransitionEvent)

> *Summary: Verifies that the `ReplyResultTransitionEvent`'s internal configuration permits arbitrary types by asserting a specific flag within its content object is set to true. This test confirms the event structure supports flexible data typing as configured.*


### test_properties (method, L199-L204, parent: TestReplyResultTransitionEvent)

> *Summary: Verifies that the `ReplyResultTransitionEvent` correctly exposes references to the originating agent and the intended transition target via its content structure. It asserts equality between these stored objects and the provided mocks.*


### test_print_with_default_function (method, L206-L222, parent: TestReplyResultTransitionEvent)

> *Summary: This test verifies that calling the `print` method on a transition event invokes the mocked built-in `print` function exactly once. It further asserts that the arguments passed to this mock contain specific expected strings related to the event and its targets.*


### test_print_with_custom_function (method, L224-L237, parent: TestReplyResultTransitionEvent)

> *Summary: This test verifies that the `print` method on a transition event correctly invokes a provided mock function. It asserts that the custom print function is called exactly once and contains specific expected strings within its arguments, confirming proper message formatting.*


### test_print_with_agent_without_name (method, L239-L253, parent: TestReplyResultTransitionEvent)

> *Summary: This test verifies that the `print` method of a transition event correctly handles an agent object lacking a `name` attribute. It asserts that the printing mechanism still functions by using the agent's string representation and outputs the expected message content.*


### test_print_calls_flush (method, L255-L263, parent: TestReplyResultTransitionEvent)

> *Summary: This test verifies that when an event's content calls its `print` method, it explicitly passes `flush=True`. It achieves this by mocking the print function and asserting the keyword arguments of the first call.*


### test_event_type_from_wrap_event_decorator (method, L265-L269, parent: TestReplyResultTransitionEvent)

> *Summary: Verifies that an event decorated with `@wrap_event` correctly sets its `type` field to `"reply_result_transition"` when serialized from a `ReplyResultTransitionEvent`. This confirms the decorator properly infers and assigns the expected event type based on the class structure.*


### test_model_dump_structure (method, L271-L284, parent: TestReplyResultTransitionEvent)

> *Summary: Verifies that the `model_dump()` output of a transition event contains expected keys like `"type"` and `"content"`. It specifically asserts that the type is `"reply_result_transition"` and that the content dictionary includes references to the source agent, target, and UUID.*


### test_model_validate_roundtrip (method, L286-L296, parent: TestReplyResultTransitionEvent)

> *Summary: Validates that a `ReplyResultTransitionEvent` can be successfully serialized to a dictionary and then checked for the presence of expected keys like `"type"`, `"content"`, `"source_agent"`, and `"transition_target"` within the resulting structure. This confirms the data integrity during serialization/deserialization.*


### test_super_init_called (method, L298-L305, parent: TestReplyResultTransitionEvent)

> *Summary: Verifies that the `BaseEvent` constructor receives and stores the correct `source_agent`, `transition_target`, and generates a unique identifier when initialized with these inputs. It asserts the presence of these attributes on the event's content after instantiation.*


### test_model_dump_contains_uuid (method, L307-L313, parent: TestReplyResultTransitionEvent)

> *Summary: Verifies that when an `ReplyResultTransitionEvent` is serialized via `model_dump()`, the resulting dictionary structure contains both a `"content"` key and a nested `"uuid"` within that content. This confirms the event object correctly embeds a unique identifier upon serialization.*

