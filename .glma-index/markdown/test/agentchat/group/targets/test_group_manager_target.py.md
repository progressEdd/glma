# test/agentchat/group/targets/test_group_manager_target.py

3 class(es): TestPrepareGroupchatAutoSpeaker, TestGroupManagerSelectionMessages, TestGroupManagerTarget. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestPrepareGroupchatAutoSpeaker | class |  |
| TestGroupManagerSelectionMessages | class |  |
| TestGroupManagerTarget | class |  |

## Chunks

### TestPrepareGroupchatAutoSpeaker (class, L24-L107)

> *Summary: This test suite verifies the `prepare_groupchat_auto_speaker` function, which configures a group chat's speaker selection prompt. It tests three scenarios: using a default template when no custom message is provided, applying a specific custom message via an input object, and ensuring that only non-tool/non-wrapped agents are passed to the speaker selection method.*


### mock_groupchat (method, L26-L32, parent: TestPrepareGroupchatAutoSpeaker)

> *Summary: Generates a mock object conforming to the `GroupChat` interface for testing purposes. This mock preconfigures the `select_speaker_prompt` method to return a specific prompt string containing placeholders for agent roles.*


### mock_agent (method, L35-L39, parent: TestPrepareGroupchatAutoSpeaker)

> *Summary: Generates a `MagicMock` instance conforming to the `ConversableAgent` interface, setting its name to "MockAgent" for use in tests. This mock object simulates an agent without requiring actual implementation logic.*


### mock_tool_executor (method, L42-L46, parent: TestPrepareGroupchatAutoSpeaker)

> *Summary: Generates a mocked instance of `GroupToolExecutor` configured with the name "ToolExecutor". This mock object is returned to simulate tool execution during testing scenarios.*


### mock_wrapped_agent (method, L49-L53, parent: TestPrepareGroupchatAutoSpeaker)

> *Summary: Generates and returns a `MagicMock` instance conforming to the `ConversableAgent` interface, pre-setting its name with a specific prefix for testing purposes.*


### test_prepare_groupchat_auto_speaker_with_default_message (method, L55-L67, parent: TestPrepareGroupchatAutoSpeaker)

> *Summary: This test verifies that when preparing a group chat auto-speaker without providing a custom message, the system correctly uses the default speaker selection prompt template and calls the `select_speaker_prompt` method with all agents in the group. It asserts that the correct default template constant is applied to the mock groupchat object.*


### test_prepare_groupchat_auto_speaker_with_custom_message (method, L69-L85, parent: TestPrepareGroupchatAutoSpeaker)

> *Summary: This test verifies that the `prepare_groupchat_auto_speaker` function correctly utilizes a provided custom selection message when setting up group chat speaker prompts. It asserts that the custom message's getter was called with the agent and that the group chat object received the correct list of agents for speaker selection.*


### test_prepare_groupchat_auto_speaker_filters_agents (method, L87-L107, parent: TestPrepareGroupchatAutoSpeaker)

> *Summary: This test verifies that the `prepare_groupchat_auto_speaker` function correctly filters a list of group chat participants. It asserts that only the standard agent remains when tool executors and wrapped agents are present, ensuring only eligible speakers are passed to speaker selection logic.*


### TestGroupManagerSelectionMessages (class, L110-L179)

> *Summary: This test suite verifies the behavior of various message implementations derived from a base class for group manager selection messages. It confirms that the base implementation raises `NotImplementedError`, while specific string and context-aware subclasses correctly format messages using provided agent contexts, handling placeholders like `{agentlist}` appropriately during formatting and validation.*


### test_base_class_get_message_raises_not_implemented (method, L111-L118, parent: TestGroupManagerSelectionMessages)

> *Summary: Verifies that the base `GroupManagerSelectionMessage` correctly raises a `NotImplementedError` when its `get_message` method is called with a mock agent, ensuring derived classes must override this functionality.*


### test_string_message_get_message (method, L120-L127, parent: TestGroupManagerSelectionMessages)

> *Summary: Verifies that a `GroupManagerSelectionMessageString` instance correctly returns its stored message text when the `get_message` method is called with a mock agent. The input is an initialized string message object and a mock agent, yielding the original message string as output.*


### test_context_str_message_get_message (method, L129-L138, parent: TestGroupManagerSelectionMessages)

> *Summary: This test verifies that a message context object correctly formats its template string using provided agent context variables. It takes an agent mock with specific context data and asserts the output matches the expected formatted string.*


### test_context_str_message_with_agentlist_placeholder (method, L140-L151, parent: TestGroupManagerSelectionMessages)

> *Summary: This test verifies that a message context string correctly substitutes specified variables while preserving the `{agentlist}` placeholder. It takes a template and a mock agent with context data as input, asserting the output matches the expected format where known criteria are filled but the agent list marker remains intact.*


### test_context_str_message_validator (method, L153-L167, parent: TestGroupManagerSelectionMessages)

> *Summary: Verifies that a string template validator replaces `{agentlist}` with `<<agent_list>>` internally, but the subsequent `get_message` method correctly restores the original placeholder when provided with an agent mock. This confirms proper handling of context substitution for message generation.*


### test_context_str_message_with_missing_variables (method, L169-L179, parent: TestGroupManagerSelectionMessages)

> *Summary: This test verifies that when a message context string contains undefined variables, the resulting output remains the original template string. It achieves this by initializing a `GroupManagerSelectionMessageContextStr` with a template containing missing placeholders and asserting the returned message matches the input template.*


### TestGroupManagerTarget (class, L182-L271)

> *Summary: This test suite verifies the functionality of `GroupManagerTarget`, ensuring it correctly initializes with or without a selection message and behaves as expected during group chat resolution. It confirms that when resolving, the target either bypasses external speaker preparation or calls it using the provided selection message to return a specific `SpeakerSelectionResult`.*


### mock_selection_message (method, L184-L188, parent: TestGroupManagerTarget)

> *Summary: Generates a mocked `GroupManagerSelectionMessage` object configured to return a specific string when its `get_message` method is called, facilitating isolated testing of group management logic.*


### test_init (method, L190-L199, parent: TestGroupManagerTarget)

> *Summary: Verifies that the `GroupManagerTarget` initializes correctly, asserting that its `selection_message` attribute is `None` by default and can be successfully set when provided a message object during instantiation.*


### test_can_resolve_for_speaker_selection (method, L201-L204, parent: TestGroupManagerTarget)

> *Summary: Verifies that the `GroupManagerTarget` instance correctly reports its ability to resolve for speaker selection by asserting a boolean return value of `True`.*


### test_resolve_without_selection_message (method, L207-L224, parent: TestGroupManagerTarget)

> *Summary: When resolving without an explicit selection message, the target should return a `SpeakerSelectionResult` indicating automatic speaker selection. This process must not invoke any preparation methods on the provided mock objects.*


### test_resolve_with_selection_message (method, L227-L242, parent: TestGroupManagerTarget)

> *Summary: This test verifies that when resolving within a group chat context, the target correctly uses a provided selection message to prepare the group chat automatically. It asserts that the resolution returns a `SpeakerSelectionResult` indicating an "auto" selection method was used.*


### test_display_name (method, L244-L247, parent: TestGroupManagerTarget)

> *Summary: Verifies that the `GroupManagerTarget` instance correctly returns the string `"the group manager"` when its `display_name()` method is called. This test confirms the expected human-readable name for the target object.*


### test_normalized_name (method, L249-L252, parent: TestGroupManagerTarget)

> *Summary: Verifies that calling `normalized_name()` on a `GroupManagerTarget` instance correctly returns its predefined display name, which is expected to be "the group manager".*


### test_str_representation (method, L254-L257, parent: TestGroupManagerTarget)

> *Summary: Verifies that an instance of `GroupManagerTarget` produces the expected string output, `"Transfer to the group manager"`, when cast to a string. This confirms correct serialization for debugging or logging purposes.*


### test_needs_agent_wrapper (method, L259-L262, parent: TestGroupManagerTarget)

> *Summary: Verifies that the `GroupManagerTarget` instance correctly reports that it does not require an agent wrapper by asserting a `False` return value from its method.*


### test_create_wrapper_agent_raises_error (method, L264-L271, parent: TestGroupManagerTarget)

> *Summary: This test verifies that attempting to wrap an agent using `create_wrapper_agent` on a `GroupManagerTarget` instance raises a specific `NotImplementedError`. It confirms the error message indicates that no wrapping is necessary for this target type.*

