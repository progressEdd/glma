# test/agentchat/test_function_targets.py

33 function(s): minimal_correct_fn_target, correct_fn_target_extra_args, fn_with_optional_param, fn_with_kwargs, invalid_fn, test_fn_target_init, test_fn_target_init_with_extra_args, test_fn_target_init_invalid_args, test_fn_target_init_non_callable_raises, test_function_target_display_and_normalized_name and 23 more. 2 class(es): DummyGroupManager, DummyContextVariables. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DummyGroupManager | class |  |
| DummyContextVariables | class |  |
| minimal_correct_fn_target | function |  |
| correct_fn_target_extra_args | function |  |
| fn_with_optional_param | function |  |
| fn_with_kwargs | function |  |
| invalid_fn | function |  |
| test_fn_target_init | function |  |
| test_fn_target_init_with_extra_args | function |  |
| test_fn_target_init_invalid_args | function |  |
| test_fn_target_init_non_callable_raises | function |  |
| test_function_target_display_and_normalized_name | function |  |
| test_function_target_never_needs_wrapper_and_raises_if_created | function |  |
| test_validate_fn_sig_valid_fn | function |  |
| test_validate_fn_sig_raises_on_missing_args | function |  |
| test_validate_fn_sig_raises_on_invalid_args | function |  |
| test_validate_fn_sig_allows_optional_params_without_extra_args | function |  |
| test_validate_fn_sig_allows_kwargs_for_unknown_extra_args | function |  |
| test_construct_broadcast_messages_list_with_string_and_agenttarget | function |  |
| test_construct_broadcast_messages_list_with_string_and_agentnametarget | function |  |
| test_construct_broadcast_messages_list_raises_if_agent_name_not_found | function |  |
| test_construct_broadcast_messages_list_with_string_and_revert_to_user_target | function |  |
| test_construct_broadcast_messages_list_with_string_and_revert_to_user_no_user_defaults_to_current | function |  |
| test_construct_broadcast_messages_list_with_string_and_staytarget | function |  |
| test_construct_broadcast_messages_list_passthrough_for_list_of_messages | function |  |
| test_broadcast_string_to_agent_uses_group_manager | function |  |
| test_broadcast_list_of_messages_sends_to_all_targets | function |  |
| test_broadcast_raises_without_group_manager | function |  |
| function_target_updates_context_and_messages | function |  |
| function_target_no_messages_just_target | function |  |
| function_target_returns_wrong_type | function |  |
| test_function_target_resolve_updates_context_and_broadcasts | function |  |
| test_function_target_resolve_without_messages_does_not_broadcast | function |  |
| test_function_target_resolve_raises_if_function_returns_wrong_type | function |  |
| test_function_target_resolve_uses_provided_target_resolve | function |  |

## Chunks

### DummyGroupManager (class, L34-L46)

> *Summary: This class acts as a mock implementation of a group chat manager, storing records of messages sent to specific agents. It accepts a message dictionary and a target agent upon calling its `send` method, appending the details to an internal list.*


### __init__ (method, L37-L38, parent: DummyGroupManager)

> *Summary: Initializes an instance by setting up an empty list named `sent` to store message dictionaries. This structure is used to maintain a history of sent messages within the object.*


### send (method, L40-L46, parent: DummyGroupManager)

> *Summary: Records a message sent to a specific agent, storing the message content, recipient, and flags indicating if a reply is expected or if the transmission should be silent. It appends this structured record to an internal list of sent messages.*


### DummyContextVariables (class, L49-L59)

> *Summary: Provides a minimal implementation of context variables, accepting an optional initial dictionary. It allows updating the stored data and retrieving the current state as a standard dictionary.*


### __init__ (method, L52-L53, parent: DummyContextVariables)

> *Summary: Initializes an object by storing provided dictionary data; if no data is supplied, it defaults to an empty dictionary.*


### update (method, L55-L56, parent: DummyContextVariables)

> *Summary: Merges a dictionary of new data into the instance's internal state. It modifies the object in place by updating its existing data structure with the provided key-value pairs.*


### to_dict (method, L58-L59, parent: DummyContextVariables)

> *Summary: Converts the internal data structure of the object into a standard Python dictionary. It takes no arguments and returns a `dict[str, Any]`.*


### minimal_correct_fn_target (function, L67-L72)

> *Summary: Constructs a minimal, valid `FunctionTargetResult` by wrapping the provided string output in an `AgentTarget`. This function requires the desired message content and context variables as input to produce the result.*


### correct_fn_target_extra_args (function, L75-L80)

> *Summary: This function constructs a `FunctionTargetResult` by wrapping the provided output string with an extra parameter value. It uses this to simulate a valid function target that satisfies an additional required argument.*


### fn_with_optional_param (function, L83-L85)

> *Summary: This function constructs a `FunctionTargetResult` by embedding the provided output and the value of an optional integer parameter into a message string. It returns this result, associating it with a specific test agent.*


### fn_with_kwargs (function, L88-L93)

> *Summary: This function constructs a `FunctionTargetResult` by embedding the provided output and any arbitrary keyword arguments into a message string. It returns this result associated with a specific test agent target.*


### invalid_fn (function, L96-L101)

> *Summary: This function takes a string as input and returns a `FunctionTargetResult` object. It wraps the input string within the messages field of the result, targeting a specific test agent.*


### test_fn_target_init (function, L109-L115)

> *Summary: This test verifies that a `FunctionTarget` correctly wraps an input callable, ensuring the target's name and function reference are set as expected, while its extra arguments remain empty. It confirms the initialization successfully exposes basic metadata about the wrapped function.*


### test_fn_target_init_with_extra_args (function, L118-L125)

> *Summary: This test verifies that a `FunctionTarget` instance correctly stores and exposes additional keyword arguments provided during initialization. It confirms the function name, the bound function object, and the custom arguments are all set as expected.*


### test_fn_target_init_invalid_args (function, L128-L131)

> *Summary: Asserts that initializing a `FunctionTarget` with a function expecting fewer than two positional arguments raises a `ValueError`. This verifies the input validation logic for target functions.*


### test_fn_target_init_non_callable_raises (function, L134-L137)

> *Summary: This test verifies that attempting to initialize a `FunctionTarget` with a non-callable value raises a specific `ValueError`. It confirms the target correctly enforces that its input must be a callable function.*


### test_function_target_display_and_normalized_name (function, L140-L146)

> *Summary: This test verifies that a `FunctionTarget` instance correctly exposes user-friendly information through its display name, normalized name, and string representation. It asserts these attributes match the underlying function target's identifier.*


### test_function_target_never_needs_wrapper_and_raises_if_created (function, L149-L156)

> *Summary: Verifies that a `FunctionTarget` instance executes directly without needing an agent wrapper and raises a specific error if an attempt is made to create one. It confirms the target's intrinsic nature prevents unnecessary wrapping logic.*


### test_validate_fn_sig_valid_fn (function, L164-L167)

> *Summary: This test verifies that functions with correct signatures are accepted by the validation logic. It calls `validate_fn_sig` using predefined valid function targets, optionally supplying extra arguments for testing flexibility.*


### test_validate_fn_sig_raises_on_missing_args (function, L170-L173)

> *Summary: This test asserts that the signature validation function raises a `ValueError` when no additional arguments are provided for a target function. It specifically checks that missing required parameters result in an error message indicating missing `extra_args`.*


### test_validate_fn_sig_raises_on_invalid_args (function, L176-L179)

> *Summary: This test asserts that calling `validate_fn_sig` with an `extra_args` dictionary containing keys not present in the target function raises a `ValueError`. It specifically checks for the error message indicating invalid arguments were provided.*


### test_validate_fn_sig_allows_optional_params_without_extra_args (function, L182-L185)

> *Summary: This test verifies that a function signature validator correctly handles functions containing optional parameters when no additional arguments are provided. It asserts that calling the validation with an empty `extra_args` dictionary does not raise an error for such functions.*


### test_validate_fn_sig_allows_kwargs_for_unknown_extra_args (function, L188-L191)

> *Summary: This test verifies that when a function signature accepts arbitrary keyword arguments (`**kwargs`), the validation process permits unknown extra arguments passed via `extra_args`. It asserts no error is raised when providing unlisted keys like `"foo"` and `"bar"`.*


### test_construct_broadcast_messages_list_with_string_and_agenttarget (function, L199-L218)

> *Summary: This test verifies that providing a string message and an `AgentTarget` results in a list containing exactly one `FunctionTargetMessage`. This single message correctly targets the specified recipient agent with the input string content.*


### test_construct_broadcast_messages_list_with_string_and_agentnametarget (function, L221-L240)

> *Summary: This test verifies that a broadcast message string containing an agent's name is correctly resolved to the specific `ConversableAgent` instance within a `GroupChat`. It asserts that the resulting list contains one message whose content matches the input and whose target is the intended named agent.*


### test_construct_broadcast_messages_list_raises_if_agent_name_not_found (function, L243-L256)

> *Summary: This test verifies that attempting to construct a broadcast message list fails with a `ValueError` if the specified agent name in the target is not present within the provided group chat. It asserts this failure when calling `construct_broadcast_messages_list` with an agent name that doesn't exist in the initialized group.*


### test_construct_broadcast_messages_list_with_string_and_revert_to_user_target (function, L259-L276)

> *Summary: This test verifies that when a string message and a `RevertToUserTarget` are provided to the message construction utility, the resulting broadcast list contains exactly one message targeted specifically at the designated user agent. It confirms the correct routing behavior for mixed input types.*


### test_construct_broadcast_messages_list_with_string_and_revert_to_user_no_user_defaults_to_current (function, L279-L295)

> *Summary: This test verifies that when a `RevertToUserTarget` lacks a specified user agent, the message construction logic defaults to targeting the provided `current_agent`. It asserts that the resulting broadcast message list contains exactly one message directed at this fallback agent.*


### test_construct_broadcast_messages_list_with_string_and_staytarget (function, L298-L315)

> *Summary: This test verifies that when a string message and a `StayTarget` are provided to the message construction utility, it generates exactly one broadcast message directed specifically to the `current_agent`. The function takes a message string, a group chat context, agent instances, and a target object as input.*


### test_construct_broadcast_messages_list_passthrough_for_list_of_messages (function, L318-L338)

> *Summary: When provided with an existing list of `FunctionTargetMessage` objects, this test verifies that the message construction utility returns the input list unchanged. It confirms that the returned list maintains the original order and targets specified in the input messages.*


### test_broadcast_string_to_agent_uses_group_manager (function, L346-L377)

> *Summary: This test verifies that broadcasting a string message to an agent correctly wraps the content in a `FUNCTION_HANDOFF` system message and sends it through the configured group manager. It asserts that the sent message targets the correct recipient, is not silent or requesting a reply, and contains the expected function handoff structure.*


### test_broadcast_list_of_messages_sends_to_all_targets (function, L380-L405)

> *Summary: This test verifies that a broadcast function correctly distributes multiple `FunctionTargetMessage` instances to all specified agents within a group chat. It asserts that the underlying group manager records exactly two sent messages, targeting both designated recipient agents.*


### test_broadcast_raises_without_group_manager (function, L408-L423)

> *Summary: This test verifies that the `broadcast` function raises a `ValueError` if the `current_agent` lacks an associated group manager. It simulates a broadcast attempt using two agents in a `GroupChat` where the initiating agent is missing the necessary management context.*


### function_target_updates_context_and_messages (function, L431-L440)

> *Summary: This function processes an output string and an integer value to generate a result. It creates new context variables containing the input data and returns a `FunctionTargetResult` that includes a predefined message reply and specifies staying in the current target state.*


### function_target_no_messages_just_target (function, L443-L449)

> *Summary: This test helper constructs a `FunctionTargetResult` containing only a `StayTarget()` without any associated messages or context variables. It is used to verify scenarios where the agent's output should solely be a target action.*


### function_target_returns_wrong_type (function, L452-L454)

> *Summary: This test helper intentionally violates the expected return contract by outputting a raw string instead of the required `FunctionTargetResult` object. It accepts an arbitrary string and context object as input to demonstrate type mismatch failure.*


### test_function_target_resolve_updates_context_and_broadcasts (function, L458-L498)

> *Summary: This test verifies that resolving a function target correctly passes the last message and context to the target function, updates the agent's context variables with new data, broadcasts messages, and returns the next speaker selection. It asserts that the context is updated as expected and the returned result designates the current agent as the next speaker.*


### test_function_target_resolve_without_messages_does_not_broadcast (function, L502-L528)

> *Summary: This test verifies that when a `FunctionTarget` is resolved without any existing messages in the group chat, no new messages are broadcasted or added to the chat history. It initializes a single-agent group chat and asserts the message count remains unchanged after calling the target's resolve method.*


### test_function_target_resolve_raises_if_function_returns_wrong_type (function, L532-L552)

> *Summary: This test verifies that resolving a `FunctionTarget` raises a `ValueError` if the underlying function does not return the expected `FunctionTargetResult`. It sets up an agent and group chat environment to execute this type-checking assertion.*


### test_function_target_resolve_uses_provided_target_resolve (function, L556-L596)

> *Summary: Verifies that a `FunctionTarget` correctly delegates its resolution logic to the underlying target type when called with a group chat context. It tests this by providing targets for staying with the current agent and targeting another specific agent, asserting the correct agent name is returned in both cases.*

