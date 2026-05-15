# test/agentchat/group/targets/test_transition_target.py

9 class(es): TestTransitionTarget, TestAgentTarget, TestAgentNameTarget, TestNestedChatTarget, TestTerminateTarget, TestStayTarget, TestRevertToUserTarget, TestAskUserTarget, TestRandomAgentTarget. 74 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTransitionTarget | class |  |
| TestAgentTarget | class |  |
| TestAgentNameTarget | class |  |
| TestNestedChatTarget | class |  |
| TestTerminateTarget | class |  |
| TestStayTarget | class |  |
| TestRevertToUserTarget | class |  |
| TestAskUserTarget | class |  |
| TestRandomAgentTarget | class |  |

## Chunks

### TestTransitionTarget (class, L27-L100)

> *Summary: This test suite verifies the contract of a base `TransitionTarget` class by asserting that its abstract methods (like `resolve`, `display_name`, etc.) correctly raise `NotImplementedError`. It also tests the concrete behavior of activating a target, ensuring only the designated `GroupToolExecutor` agent receives the next target assignment within a group chat.*


### test_base_target_can_resolve_for_speaker_selection (method, L28-L31, parent: TestTransitionTarget)

> *Summary: Verifies that a default `TransitionTarget` instance correctly reports it cannot resolve for speaker selection by asserting the method returns `False`.*


### test_base_target_resolve (method, L33-L40, parent: TestTransitionTarget)

> *Summary: Verifies that the base `TransitionTarget` class correctly raises a `NotImplementedError` when its `resolve` method is called with mocked group chat and agent objects. This ensures derived classes must override this method for functionality.*


### test_base_target_display_name (method, L42-L47, parent: TestTransitionTarget)

> *Summary: Verifies that the base `TransitionTarget` class correctly raises a `NotImplementedError` when its `display_name()` method is called, ensuring derived classes must override this functionality.*


### test_base_target_normalized_name (method, L49-L54, parent: TestTransitionTarget)

> *Summary: Verifies that the base `TransitionTarget` class correctly raises a `NotImplementedError` when its `normalized_name()` method is called, ensuring derived classes must override this functionality.*


### test_base_target_needs_agent_wrapper (method, L56-L61, parent: TestTransitionTarget)

> *Summary: Verifies that the base `TransitionTarget` class correctly raises a `NotImplementedError` when its `needs_agent_wrapper` method is called, ensuring derived classes must override this functionality. The test asserts that the error message specifically indicates subclasses are required to implement the method.*


### test_base_target_create_wrapper_agent (method, L63-L69, parent: TestTransitionTarget)

> *Summary: Verifies that the base `TransitionTarget` class correctly raises a `NotImplementedError` when its `create_wrapper_agent` method is called with a mock agent and an integer argument. This ensures derived classes must override this method to provide concrete implementation.*


### test_activate_target (method, L71-L100, parent: TestTransitionTarget)

> *Summary: This test verifies that when a `TerminateTarget` is activated within a group chat containing a `GroupToolExecutor`, the target correctly sets itself as the next target specifically on the executor agent. It asserts that no other agents in the group are affected by this targeting action.*


### TestAgentTarget (class, L103-L169)

> *Summary: These tests verify the functionality of an `AgentTarget` class by instantiating it with a mock agent and asserting correct behavior for methods like resolution, name retrieval, and string representation. The tests confirm that the target correctly identifies itself and handles scenarios where wrapping might be required or unnecessary.*


### test_init (method, L104-L109, parent: TestAgentTarget)

> *Summary: This test verifies that an `AgentTarget` correctly initializes by setting the agent's name from a provided mock agent instance. It asserts that the internal `agent_name` attribute matches the mocked agent's assigned name.*


### test_can_resolve_for_speaker_selection (method, L111-L116, parent: TestAgentTarget)

> *Summary: This test verifies that an `AgentTarget` instance, initialized with a mock agent, correctly reports its ability to resolve for speaker selection. It asserts that the method returns `True` when provided with a configured conversational agent object.*


### test_resolve (method, L118-L131, parent: TestAgentTarget)

> *Summary: This test verifies that resolving an `AgentTarget` against a mock group chat and agent returns a `SpeakerSelectionResult`. The expected output confirms the correct agent name was selected, with no termination or specific speaker selection method indicated.*


### test_display_name (method, L133-L138, parent: TestAgentTarget)

> *Summary: Verifies that the `display_name` method correctly returns the name assigned to an input agent mock. It asserts that calling this method on an initialized `AgentTarget` yields the mocked agent's name.*


### test_normalized_name (method, L140-L145, parent: TestAgentTarget)

> *Summary: Verifies that the `normalized_name` method correctly returns the agent's assigned name when provided with a mocked agent object. It asserts that calling this method on an `AgentTarget` instance yields the expected string value from the mock agent's `name` attribute.*


### test_str_representation (method, L147-L152, parent: TestAgentTarget)

> *Summary: Verifies that the `AgentTarget` object correctly formats its string representation by prepending "Transfer to " to the name of the associated agent. It uses a mocked agent with a specific name to confirm this output.*


### test_needs_agent_wrapper (method, L154-L159, parent: TestAgentTarget)

> *Summary: When provided with a mock agent instance, this test asserts that the `AgentTarget` object correctly reports that it does not require an agent wrapper. The function uses a mocked `ConversableAgent` to verify this specific behavior of the target object.*


### test_create_wrapper_agent_raises_error (method, L161-L169, parent: TestAgentTarget)

> *Summary: This test verifies that attempting to create a wrapper agent using `create_wrapper_agent` on an `AgentTarget` instance raises a `NotImplementedError`. It asserts that the error message specifically indicates that no wrapping is required for the target.*


### TestAgentNameTarget (class, L172-L222)

> *Summary: This test suite verifies the functionality of an agent target that resolves to a specific named agent within a group chat context. It confirms initialization, resolution logic against mock agents/chats, and correct string/name representations for the target.*


### test_init (method, L173-L176, parent: TestAgentNameTarget)

> *Summary: Verifies that an `AgentNameTarget` instance correctly stores the provided string when initialized with an agent name. It confirms the internal `agent_name` attribute matches the input value.*


### test_can_resolve_for_speaker_selection (method, L178-L181, parent: TestAgentNameTarget)

> *Summary: Verifies that an `AgentNameTarget` instance, initialized with a specific agent name, correctly reports its ability to resolve for speaker selection by returning `True`.*


### test_resolve (method, L183-L193, parent: TestAgentNameTarget)

> *Summary: This test verifies that an `AgentNameTarget` correctly resolves to a `SpeakerSelectionResult` containing the specified agent's name when provided with mock group chat and agent objects. It asserts the resulting object type, the correct agent name, and confirms termination/speaker selection methods are unset.*


### test_display_name (method, L195-L198, parent: TestAgentNameTarget)

> *Summary: Verifies that an `AgentNameTarget` instance correctly returns its assigned agent name when its `display_name()` method is called, using `"test_agent"` as the input.*


### test_normalized_name (method, L200-L203, parent: TestAgentNameTarget)

> *Summary: Verifies that an `AgentNameTarget` instance correctly returns its initial agent name when calling the `normalized_name()` method. It takes an agent name as input and asserts the output matches that input.*


### test_str_representation (method, L205-L208, parent: TestAgentNameTarget)

> *Summary: Verifies that an `AgentNameTarget` instance correctly formats its string representation. It asserts that the output matches a specific transfer message format using a provided agent name.*


### test_needs_agent_wrapper (method, L210-L213, parent: TestAgentNameTarget)

> *Summary: Verifies that an `AgentNameTarget` instance, initialized with a specific agent name, correctly reports that it does not require an agent wrapper. The method asserts the boolean return value of the `needs_agent_wrapper()` call on the target object.*


### test_create_wrapper_agent_raises_error (method, L215-L222, parent: TestAgentNameTarget)

> *Summary: This test verifies that attempting to wrap an agent using `AgentNameTarget` raises a specific `NotImplementedError`. It achieves this by passing a mock agent and an integer to the target's creation method, asserting the error message content.*


### TestNestedChatTarget (class, L225-L304)

> *Summary: This test suite verifies the functionality of a `NestedChatTarget` class, which is initialized with a nested chat configuration dictionary. It asserts various behaviors such as correct initialization, display name generation, and confirms that its `resolve` method raises a `NotImplementedError`. The tests also validate agent wrapping capabilities by checking wrapper creation logic.*


### test_init (method, L226-L230, parent: TestNestedChatTarget)

> *Summary: Verifies that an instance of `NestedChatTarget` correctly stores a provided, deeply structured configuration dictionary upon initialization. It confirms the input configuration is accurately reflected in the object's internal state.*


### test_can_resolve_for_speaker_selection (method, L232-L236, parent: TestNestedChatTarget)

> *Summary: When initialized with a specific nested chat configuration, the target object should return `False` when queried about its ability to resolve for speaker selection. This test verifies that this expected behavior holds true for the provided input structure.*


### test_resolve_raises_error (method, L238-L247, parent: TestNestedChatTarget)

> *Summary: This test verifies that attempting to resolve a `NestedChatTarget` instance with mocked group chat and agent objects raises a `NotImplementedError`. It confirms the specific error message indicating the target's lack of resolution support.*


### test_display_name (method, L249-L253, parent: TestNestedChatTarget)

> *Summary: Verifies that an instance of `NestedChatTarget`, initialized with a specific configuration, correctly returns the string `"a nested chat"` when its display name method is called.*


### test_normalized_name (method, L255-L259, parent: TestNestedChatTarget)

> *Summary: Verifies that the `normalized_name` method correctly returns `"nested_chat"` when initialized with a specific configuration dictionary. This test confirms the expected standardized name output for a `NestedChatTarget`.*


### test_str_representation (method, L261-L265, parent: TestNestedChatTarget)

> *Summary: Verifies that the string representation of a `NestedChatTarget` object correctly outputs `"Transfer to nested chat"` when initialized with specific configuration. This test confirms the expected textual output for the target object.*


### test_needs_agent_wrapper (method, L267-L271, parent: TestNestedChatTarget)

> *Summary: When initialized with a specific nested chat configuration, the target object's `needs_agent_wrapper` method asserts that it returns `True`. This test verifies the expected behavior for targets configured in this manner.*


### test_create_wrapper_agent (method, L273-L304, parent: TestNestedChatTarget)

> *Summary: This test verifies the creation of a wrapper agent around a nested chat target configuration. It takes a parent `ConversableAgent` and an index as input, returning a new wrapped agent instance with a specific naming convention.*


### TestTerminateTarget (class, L307-L357)

> *Summary: This test suite verifies the behavior of a `TerminateTarget` implementation used for controlling conversation flow. It asserts that the target correctly resolves to terminate the session when called with mock group chat and agent objects, and confirms its string representations and wrapper requirements are as expected.*


### test_init (method, L308-L311, parent: TestTerminateTarget)

> *Summary: Verifies that an instance created from `TerminateTarget` correctly inherits from the base `TransitionTarget`. This test confirms the proper setup and type relationship upon object instantiation.*


### test_can_resolve_for_speaker_selection (method, L313-L316, parent: TestTerminateTarget)

> *Summary: Verifies that a `TerminateTarget` instance correctly reports its ability to resolve for speaker selection, asserting the method returns `True`.*


### test_resolve (method, L318-L328, parent: TestTerminateTarget)

> *Summary: When resolving a `TerminateTarget` against mocked group chat and agent objects, the method returns a `SpeakerSelectionResult` indicating termination with `terminate=True`, while setting speaker selection details to `None`. This verifies that the target correctly signals an end to the conversation flow.*


### test_display_name (method, L330-L333, parent: TestTerminateTarget)

> *Summary: Verifies that an instance of `TerminateTarget` correctly reports its name as "Terminate". This test confirms the expected string output from the target object's display method.*


### test_normalized_name (method, L335-L338, parent: TestTerminateTarget)

> *Summary: Verifies that an instance of `TerminateTarget` correctly returns the string `"terminate"` when its `normalized_name()` method is called. This confirms the standardized naming convention for termination targets.*


### test_str_representation (method, L340-L343, parent: TestTerminateTarget)

> *Summary: Verifies that an instance of `TerminateTarget` correctly renders as the string `"Terminate"` when converted to a string. This test confirms the expected textual output for the target object.*


### test_needs_agent_wrapper (method, L345-L348, parent: TestTerminateTarget)

> *Summary: Verifies that a `TerminateTarget` instance correctly reports that it does not require an agent wrapper by asserting the return value of its `needs_agent_wrapper()` method is `False`.*


### test_create_wrapper_agent_raises_error (method, L350-L357, parent: TestTerminateTarget)

> *Summary: This test verifies that attempting to create a wrapper agent using `TerminateTarget` raises a specific `NotImplementedError`. It asserts the error message confirms that this target type does not necessitate wrapping another agent.*


### TestStayTarget (class, L360-L411)

> *Summary: This test suite verifies the functionality of a `StayTarget` implementation used for speaker selection within group chats. It asserts that the target correctly resolves to keep the current agent speaking, provides specific display and normalized names, and confirms it does not require agent wrapping.*


### test_init (method, L361-L364, parent: TestStayTarget)

> *Summary: Verifies that an instance created from `StayTarget` correctly inherits from the base `TransitionTarget`. This test confirms the proper setup and type relationship upon object instantiation.*


### test_can_resolve_for_speaker_selection (method, L366-L369, parent: TestStayTarget)

> *Summary: Verifies that a `StayTarget` instance correctly reports its ability to resolve for speaker selection by asserting the method returns `True`.*


### test_resolve (method, L371-L382, parent: TestStayTarget)

> *Summary: Verifies that a `StayTarget` resolves to a `SpeakerSelectionResult` containing the name of the provided agent. It confirms the resulting object correctly holds the agent's name and has no termination or speaker selection methods set.*


### test_display_name (method, L384-L387, parent: TestStayTarget)

> *Summary: Verifies that an instance of `StayTarget` correctly reports its display name as "Stay". This test confirms the expected string output from the target object.*


### test_normalized_name (method, L389-L392, parent: TestStayTarget)

> *Summary: Verifies that an instance of `StayTarget` correctly returns the string `"stay"` when its `normalized_name()` method is called. This confirms the standardized representation for this specific target type.*


### test_str_representation (method, L394-L397, parent: TestStayTarget)

> *Summary: Verifies that an instance of `StayTarget` produces the expected string output, `"Stay with agent"`, when converted to a string.*


### test_needs_agent_wrapper (method, L399-L402, parent: TestStayTarget)

> *Summary: Verifies that a `StayTarget` instance correctly reports that it does not require an agent wrapper by asserting the return value of its `needs_agent_wrapper()` method is `False`.*


### test_create_wrapper_agent_raises_error (method, L404-L411, parent: TestStayTarget)

> *Summary: This test verifies that attempting to create a wrapper agent for a `StayTarget` using a mock agent raises a specific `NotImplementedError`. It confirms the error message indicates that no wrapping is necessary for this target type.*


### TestRevertToUserTarget (class, L414-L476)

> *Summary: This test suite verifies the functionality of a target that forces speaker selection to revert to a specific user agent. It confirms correct initialization, resolution logic (including error handling when no user agent is provided), and proper string/name representations for the target.*


### test_init (method, L415-L418, parent: TestRevertToUserTarget)

> *Summary: Verifies that an instance created from `RevertToUserTarget` correctly inherits from the `TransitionTarget` base class. This test confirms proper object instantiation and type conformance upon initialization.*


### test_can_resolve_for_speaker_selection (method, L420-L423, parent: TestRevertToUserTarget)

> *Summary: Verifies that a `RevertToUserTarget` instance correctly reports its ability to resolve for speaker selection, asserting the method returns `True`.*


### test_resolve (method, L425-L437, parent: TestRevertToUserTarget)

> *Summary: This test verifies that a `RevertToUserTarget` correctly resolves to a `SpeakerSelectionResult` when provided with mock agents and a group chat context. The expected output confirms the result contains the specified user agent's name ("user\_agent") and has no termination or speaker selection methods set.*


### test_resolve_with_no_user_agent (method, L439-L447, parent: TestRevertToUserTarget)

> *Summary: This test verifies that attempting to resolve a `RevertToUserTarget` when no user agent is supplied results in a `ValueError`. It asserts that the raised exception specifically indicates that a user agent is required for resolution.*


### test_display_name (method, L449-L452, parent: TestRevertToUserTarget)

> *Summary: Verifies that an instance of `RevertToUserTarget` correctly returns the string "Revert to User" when its display name method is called. This test confirms the expected user-facing label for this specific target type.*


### test_normalized_name (method, L454-L457, parent: TestRevertToUserTarget)

> *Summary: Verifies that an instance of `RevertToUserTarget` correctly returns the string `"revert_to_user"` when its `normalized_name()` method is called. This confirms the standardized naming convention for this specific target type.*


### test_str_representation (method, L459-L462, parent: TestRevertToUserTarget)

> *Summary: Verifies that an instance of `RevertToUserTarget` produces the expected string output, `"Revert to User"`, when converted using `str()`.*


### test_needs_agent_wrapper (method, L464-L467, parent: TestRevertToUserTarget)

> *Summary: Verifies that a `RevertToUserTarget` instance correctly reports that it does not require an agent wrapper by asserting the return value of its `needs_agent_wrapper()` method is `False`.*


### test_create_wrapper_agent_raises_error (method, L469-L476, parent: TestRevertToUserTarget)

> *Summary: This test verifies that attempting to create a wrapper agent for the `RevertToUserTarget` raises a `NotImplementedError`. It asserts that the error message specifically indicates this target type does not require wrapping.*


### TestAskUserTarget (class, L479-L529)

> *Summary: This test suite verifies the functionality of an `AskUserTarget`, ensuring it correctly initializes, resolves to a manual speaker selection method when provided with mock agents and group chats, and adheres to expected naming conventions like `"Ask User"` and `"ask_user"`. It also confirms that this target does not require agent wrapping.*


### test_init (method, L480-L483, parent: TestAskUserTarget)

> *Summary: Verifies that an instance created from `AskUserTarget` correctly inherits from the base `TransitionTarget`. This test confirms the expected type relationship upon object instantiation.*


### test_can_resolve_for_speaker_selection (method, L485-L488, parent: TestAskUserTarget)

> *Summary: Verifies that an `AskUserTarget` instance correctly reports its ability to resolve for speaker selection by asserting the method returns `True`.*


### test_resolve (method, L490-L500, parent: TestAskUserTarget)

> *Summary: When resolving an `AskUserTarget`, the method expects a group chat and agent mocks as input to return a `SpeakerSelectionResult`. This result confirms that manual speaker selection was required, with no specific agent or termination instruction set.*


### test_display_name (method, L502-L505, parent: TestAskUserTarget)

> *Summary: Verifies that an instance of `AskUserTarget` correctly reports its display name as "Ask User". This test confirms the expected string output from the target object.*


### test_normalized_name (method, L507-L510, parent: TestAskUserTarget)

> *Summary: Verifies that an instance of `AskUserTarget` correctly resolves its standardized name to `"ask_user"` when the `normalized_name()` method is called. This confirms the expected string output for this specific target type.*


### test_str_representation (method, L512-L515, parent: TestAskUserTarget)

> *Summary: Verifies that an instance of `AskUserTarget` produces the expected string output, `"Ask User"`, when converted to a string. This confirms correct serialization for user interaction targets.*


### test_needs_agent_wrapper (method, L517-L520, parent: TestAskUserTarget)

> *Summary: Verifies that the `AskUserTarget` instance correctly reports that it does not require an agent wrapper by asserting a boolean return value of `False`.*


### test_create_wrapper_agent_raises_error (method, L522-L529, parent: TestAskUserTarget)

> *Summary: This test verifies that attempting to wrap an agent using `AskUserTarget` raises a specific `NotImplementedError`. It asserts the error message confirms that this particular target type does not necessitate agent wrapping.*


### TestRandomAgentTarget (class, L532-L674)

> *Summary: This test suite verifies the functionality of a random agent selection mechanism initialized with a list of agents. It confirms that the target can resolve to a randomly chosen agent name from its input list, correctly excludes the current agent during resolution, and provides consistent string and display representations based on the nominated agent.*


### test_init (method, L533-L542, parent: TestRandomAgentTarget)

> *Summary: This test verifies that an instance of `RandomAgentTarget` correctly initializes when provided with a list of mock agents. It asserts that the internal list of agent names matches the input and that the initial nominated name is set to a default placeholder.*


### test_can_resolve_for_speaker_selection (method, L544-L549, parent: TestRandomAgentTarget)

> *Summary: This test verifies that a `RandomAgentTarget` containing one mock agent correctly reports its ability to resolve for speaker selection. It asserts that the method returns `True` when initialized with a single mock conversational agent.*


### test_resolve (method, L551-L575, parent: TestRandomAgentTarget)

> *Summary: This test verifies that a `RandomAgentTarget` correctly selects and returns a randomly chosen agent's name when resolving speaker selection within a group chat context. It mocks the random choice to ensure the output is deterministically set to one of the provided agents, confirming the result type and selected name match expectations.*


### test_resolve_with_randomness (method, L577-L598, parent: TestRandomAgentTarget)

> *Summary: This test verifies that a `RandomAgentTarget` correctly selects an agent name randomly from a provided list of agents when its `resolve` method is called. It asserts the returned result contains one of the expected agent names and confirms the target's internal nomination matches this selection.*


### test_resolve_excludes_current_agent (method, L600-L626, parent: TestRandomAgentTarget)

> *Summary: This test verifies that a target selection mechanism correctly excludes the current agent when choosing from a list of available agents. It asserts that the underlying random choice function is called with a list containing all agents except the specified current one, and confirms the returned result matches the expected non-current agent.*


### test_display_name (method, L628-L639, parent: TestRandomAgentTarget)

> *Summary: Verifies that a `RandomAgentTarget` initially returns a placeholder string before agent selection. Once an agent is nominated via `nominated_name`, the method correctly returns the specified agent's name.*


### test_normalized_name (method, L641-L648, parent: TestRandomAgentTarget)

> *Summary: Verifies that the `normalized_name` method returns the value set in `nominated_name`. It uses a mocked agent within a `RandomAgentTarget` instance to test this behavior.*


### test_str_representation (method, L650-L657, parent: TestRandomAgentTarget)

> *Summary: Verifies that the string representation of a `RandomAgentTarget` correctly formats itself as "Transfer to [nominated\_name]". It achieves this by mocking an agent and setting a target's nominated name before asserting the output string.*


### test_needs_agent_wrapper (method, L659-L664, parent: TestRandomAgentTarget)

> *Summary: When provided with a list containing a mock agent, this test asserts that the `RandomAgentTarget` instance correctly reports that it does not require an agent wrapper. The function takes no inputs other than the class instance and returns a boolean indicating the need for wrapping.*


### test_create_wrapper_agent_raises_error (method, L666-L674, parent: TestRandomAgentTarget)

> *Summary: This test verifies that attempting to create a wrapper agent using `create_wrapper_agent` on a `RandomAgentTarget` instance raises a specific `NotImplementedError`. It confirms the target correctly signals that no wrapping is necessary for its agents.*

