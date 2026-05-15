# test/agentchat/test_groupchat_eligibility.py

13 function(s): _make_agent, _make_func_agent, test_groupchat_accepts_eligibility_policies, test_groupchat_default_eligibility_policies_is_empty, _get_candidates, test_single_agent_ineligible_removed_from_candidates, test_all_agents_ineligible_raises, test_no_policies_all_agents_eligible, test_multiple_policies_and_condition, test_circuit_breaker_trips_mid_chat and 3 more. 5 class(es): _PolicyAllowAll, _PolicyBlockByName, _CBPolicy, TestAdversarialGroupChatEligibility, TestAdversarialGroupChatEligibilityDeep. 30 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_agent | function |  |
| _make_func_agent | function |  |
| _PolicyAllowAll | class |  |
| _PolicyBlockByName | class |  |
| _CBPolicy | class |  |
| test_groupchat_accepts_eligibility_policies | function |  |
| test_groupchat_default_eligibility_policies_is_empty | function |  |
| _get_candidates | function |  |
| test_single_agent_ineligible_removed_from_candidates | function |  |
| test_all_agents_ineligible_raises | function |  |
| test_no_policies_all_agents_eligible | function |  |
| test_multiple_policies_and_condition | function |  |
| test_circuit_breaker_trips_mid_chat | function |  |
| test_circuit_breaker_half_open_retry | function |  |
| test_msze_scenario_cheap_planner_cb_trip_falls_back_to_pricey | function |  |
| TestAdversarialGroupChatEligibility | class |  |
| test_callable_speaker_selection_bypasses_policies | function |  |
| TestAdversarialGroupChatEligibilityDeep | class |  |

## Chunks

### _make_agent (function, L15-L21)

> *Summary: Creates and returns a `ConversableAgent` instance configured with the provided name. This agent is initialized without an LLM configuration and is set to never accept human input.*


### _make_func_agent (function, L24-L31)

> *Summary: Creates a `ConversableAgent` instance configured to use a provided function map for its capabilities. It initializes the agent with a specific name and disables LLM configuration and human input modes.*


### _PolicyAllowAll (class, L34-L36)

> *Summary: This class implements a policy that always grants eligibility. It accepts an `agent` and a `SelectionContext` as input and unconditionally returns `True`.*


### is_eligible (method, L35-L36, parent: _PolicyAllowAll)

> *Summary: This method checks if an agent qualifies for group chat participation by accepting an `agent` and a `SelectionContext`. Currently, it unconditionally returns `True`, indicating eligibility.*


### _PolicyBlockByName (class, L39-L44)

> *Summary: This class checks if an agent is eligible for participation based on a predefined block list. It takes a blocked agent name during initialization and returns `True` if the provided agent's name does not match the stored blocked name.*


### __init__ (method, L40-L41, parent: _PolicyBlockByName)

> *Summary: Initializes an object by storing a string representing a block status. This attribute dictates the eligibility or restriction of the agent in group chats.*


### is_eligible (method, L43-L44, parent: _PolicyBlockByName)

> *Summary: Checks if an agent is eligible for group chat by comparing the agent's name against a stored blocked list. Returns `True` if the agent's name does not match the blocked identifier.*


### _CBPolicy (class, L47-L58)

> *Summary: Manages the eligibility status of agents within a group chat context by tracking names that have been "tripped." It allows adding or removing tripped names and returns `True` if an agent's name is not present in the set of tripped agents.*


### __init__ (method, L48-L49, parent: _CBPolicy)

> *Summary: Initializes an object by creating an empty set named `tripped` to track specific states or conditions. This set will store strings representing tripped events during the object's lifecycle.*


### trip (method, L51-L52, parent: _CBPolicy)

> *Summary: Adds a given `name` string to the internal set of tripped participants. This method modifies the object's state by updating the `tripped` collection.*


### recover (method, L54-L55, parent: _CBPolicy)

> *Summary: Removes a specified `name` from the internal set of tripped entities. This method takes one string input and performs an in-place modification to the object's state without returning a value.*


### is_eligible (method, L57-L58, parent: _CBPolicy)

> *Summary: Checks if a given agent's name is present within the instance's `tripped` set to determine eligibility for group chat participation. Returns a boolean indicating whether the agent is eligible based on this membership test.*


### test_groupchat_accepts_eligibility_policies (function, L61-L69)

> *Summary: This test verifies that a `GroupChat` instance correctly registers the provided eligibility policies upon initialization. It creates a chat with two agents and one policy, asserting the count matches the input.*


### test_groupchat_default_eligibility_policies_is_empty (function, L72-L75)

> *Summary: When initialized with a list of agents and no existing messages, the `GroupChat` object should have an empty set of eligibility policies. This test verifies that default configuration results in no active policy constraints for participation.*


### _get_candidates (function, L78-L85)

> *Summary: Retrieves the names of eligible agents from a group chat based on the last speaker's input. It calls an internal selection method and returns a list containing only the agent names if candidates are found, otherwise it returns an empty list.*


### test_single_agent_ineligible_removed_from_candidates (function, L88-L99)

> *Summary: When initialized with a group chat containing multiple agents and an eligibility policy that blocks one agent (Bob), this test verifies that the candidate selection process correctly excludes the ineligible agent from the list of potential speakers. It asserts that Bob's name is absent from the returned candidates while ensuring at least one other agent remains eligible.*


### test_all_agents_ineligible_raises (function, L102-L116)

> *Summary: When all provided agents are ineligible according to the configured policies, calling `_prepare_and_select_agents` on a `GroupChat` instance will raise a `NoEligibleSpeakerError`. This test verifies that the system correctly handles scenarios where no agent meets the eligibility criteria.*


### test_no_policies_all_agents_eligible (function, L119-L124)

> *Summary: When no policies are active, this test verifies that all agents in a group chat are eligible for participation. It confirms that at least one candidate is selected and an agent is chosen as the speaker during the preparation phase.*


### test_multiple_policies_and_condition (function, L127-L140)

> *Summary: When initialized with a group chat containing three agents and specific eligibility policies blocking "alice" and "carol," this test asserts that only "bob" is considered eligible to participate. The function verifies the correct filtering of potential speakers based on defined policy constraints.*


### test_circuit_breaker_trips_mid_chat (function, L143-L158)

> *Summary: This test verifies that a circuit breaker policy correctly prevents an agent from being selected for group chat participation after it has been tripped. It initializes a group chat with three agents and asserts that one agent is removed from the candidate pool when the circuit breaker explicitly trips against them.*


### test_circuit_breaker_half_open_retry (function, L161-L177)

> *Summary: This test verifies the circuit breaker's half-open state by first tripping it for a specific agent ("bob"), ensuring they are excluded from group chat candidates. Subsequently, recovering the agent allows them to be included again when checking candidate eligibility.*


### test_msze_scenario_cheap_planner_cb_trip_falls_back_to_pricey (function, L180-L196)

> *Summary: This test verifies that when a cheap planner agent's trip fails according to the eligibility policy, the group chat correctly falls back to only considering the more expensive planner. It initializes a group chat with two agents and asserts that after triggering the failure condition on the cheap agent, the candidate list narrows down to just the pricey agent.*


### TestAdversarialGroupChatEligibility (class, L199-L338)

> *Summary: This test suite verifies the robustness and correctness of group chat eligibility filtering by simulating adversarial scenarios against a `GroupChat` instance. It ensures that policy exceptions propagate correctly, handles edge cases like empty inputs, validates state integrity during runtime policy mutation, and confirms policies are respected even when transition rules might otherwise bypass them.*


### test_policy_raises_during_filtering_propagates (method, L202-L217, parent: TestAdversarialGroupChatEligibility)

> *Summary: This test verifies that an exception raised within an agent's eligibility policy during the selection process propagates correctly. It instantiates a `GroupChat` with a custom policy designed to always raise a `ValueError`, asserting that this error is caught by `pytest`.*


### test_apply_eligibility_policies_empty_input_raises (method, L219-L235, parent: TestAdversarialGroupChatEligibility)

> *Summary: When provided with an empty list of agents, the system raises a `NoEligibleSpeakerError` because no participants meet the eligibility criteria. This test verifies that applying policies to zero inputs correctly triggers this specific error state.*


### test_apply_eligibility_policies_empty_input_no_policies_returns_empty (method, L237-L244, parent: TestAdversarialGroupChatEligibility)

> *Summary: When provided with an empty policy list and no input messages, the function returns an empty list. This test verifies that eligibility checks correctly yield no results under these minimal conditions.*


### test_eligibility_policies_list_mutation_between_rounds_safe (method, L246-L275, parent: TestAdversarialGroupChatEligibility)

> *Summary: This test verifies that modifying the list of eligibility policies during runtime between chat rounds does not corrupt the group chat state. It confirms that adding a new policy allows subsequent selection rounds to correctly incorporate and execute the updated set of rules.*


### test_policy_returns_truthy_non_bool (method, L277-L295, parent: TestAdversarialGroupChatEligibility)

> *Summary: This test verifies that a group chat system correctly handles eligibility policies that return truthy but non-boolean values. It confirms that when an agent's policy returns `1`, the selection process treats it as true, allowing all agents to be considered candidates.*


### test_policy_returns_falsy_non_bool (method, L297-L313, parent: TestAdversarialGroupChatEligibility)

> *Summary: When an eligibility policy returns a falsy non-boolean value (like 0), the agent is excluded from candidate selection. This test verifies that Bob is correctly omitted from the list of potential speakers when such a policy is applied to a group chat setup.*


### test_transitions_plus_policy_not_bypassed (method, L315-L338, parent: TestAdversarialGroupChatEligibility)

> *Summary: This test verifies that the eligibility policy is enforced even when transition rules restrict candidate selection to a single agent. It asserts that if a policy blocks the only possible next speaker, an error indicating no eligible speakers should be raised instead of silently selecting them.*


### test_callable_speaker_selection_bypasses_policies (function, L341-L362)

> *Summary: When a speaker selection method is provided as a callable function, the system bypasses all configured eligibility policies during agent selection. This test confirms that using a custom callable overrides policy checks, forcing the selection of the returned agent regardless of policy outcomes.*


### TestAdversarialGroupChatEligibilityDeep (class, L365-L717)

> *Summary: This test suite verifies various adversarial scenarios for agent group chat eligibility logic. It tests how the system handles policies returning `None`, exceptions during policy evaluation, concurrent access, and complex interactions between function call filtering, speaker repetition rules, and custom eligibility policies.*


### test_policy_returns_none_excluded (method, L368-L385, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: When an eligibility policy returns `None` for a specific agent, that agent must be excluded from the candidate pool. This test verifies that an agent whose policy yields `None` is correctly filtered out during group chat selection while other agents remain eligible.*


### test_policy_raises_on_second_agent_propagates (method, L387-L405, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies that if an eligibility policy raises an exception for a specific agent (like "bob"), the entire group chat preparation process propagates that error when attempting to select agents. It uses a custom policy to force a `RuntimeError` during agent selection within a configured `GroupChat`.*


### test_concurrent_prepare_and_select_agents (method, L407-L436, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies the thread safety of agent preparation and selection by concurrently calling `_prepare_and_select_agents` from twenty separate threads. It asserts that no exceptions are raised during this concurrent execution and that exactly twenty results are collected.*


### test_single_agent_groupchat_underpopulated_guard_fires_first (method, L438-L449, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: When initializing a `GroupChat` with only one agent, the system immediately raises a `ValueError('underpopulated')` during agent preparation, bypassing any configured eligibility policies. This test confirms that the built-in guard check executes before policy evaluation in underpopulated scenarios.*


### test_func_call_filter_singleton_not_early_returned (method, L451-L470, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: When a group chat is initialized with specific constraints like `allow_repeat_speaker=False`, this test verifies that the agent selection process correctly excludes the last speaker from candidates, ensuring another eligible agent is chosen instead. It confirms that Bob is selected over Alice when Alice was the previous speaker and both are capable of executing the required function call.*


### test_func_call_filter_policy_blocks_function_agent (method, L472-L486, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: When a group chat is configured with an eligibility policy that blocks all potential function-calling speakers, attempting to prepare and select agents will raise a `NoEligibleSpeakerError`. This test verifies that the system correctly identifies no eligible participants when the designated agent's function call capability is blocked by policy.*


### test_func_call_filter_fallback_applies_policies (method, L488-L509, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: When no agent possesses the requested function, this test verifies that GroupChat falls back to all agents with a `function_map` and subsequently applies eligibility policies to select one from that fallback group. It asserts that only Bob is selected because Alice is blocked by an explicit policy, even though both have functions defined.*


### test_func_call_filter_fallback_all_blocked_raises (method, L511-L533, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies that when an eligibility policy blocks all function-calling agents in a group chat scenario, the system correctly raises a `NoEligibleSpeakerError`. It simulates a situation where no agent can fulfill the required function call due to restrictive policies.*


### test_sync_manual_fallback_uses_filtered_agents (method, L535-L557, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: When manual speaker selection fails (returns `None`), this test verifies that the system falls back to selecting an agent from a pre-filtered list based on eligibility policies. Given agents Alice, Bob, and Carol with Bob blocked by policy, it asserts that Carol is chosen as the next speaker.*


### test_async_manual_fallback_uses_filtered_agents (method, L559-L584, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies that when manual speaker selection fails (returns `None`), the system correctly falls back to selecting an agent from a pre-filtered list based on eligibility policies. It confirms that in a group chat with one blocked agent, the fallback mechanism selects the next available agent according to policy constraints.*


### test_invalid_policy_rejected_at_construction (method, L586-L595, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies that the `GroupChat` constructor raises a `ValueError` when provided with an invalid or non-compliant eligibility policy. It confirms that the system rejects initialization if the specified policies do not adhere to the required interface.*


### test_policy_filtered_set_is_subset_of_input (method, L597-L617, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: Verifies that an eligibility policy correctly filters the agent pool, ensuring the resulting candidate set is always a subset of the initial input agents and excludes any agents explicitly blocked by the policy. This test confirms the core invariant that selection logic never introduces unauthorized participants into the group chat process.*


### test_policy_plus_allow_repeat_speaker_false_normal_path (method, L619-L635, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: When configured with `allow_repeat_speaker=False` and a specific eligibility policy blocking one agent, the system selects only the remaining eligible speaker from the group chat based on round-robin selection. This test verifies that only Carol is selected when Alice is the last speaker (and thus excluded) and Bob is blocked by policy.*


### test_agent_count_boundary_triple (method, L645-L660, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies the group chat's agent count boundaries by initializing a `GroupChat` with varying numbers of agents. It asserts that an error is raised when the agent count falls below the minimum threshold, while confirming successful agent selection otherwise.*


### test_h10_func_call_filter_policies_applied_then_allow_repeat_speaker_empties_candidates (method, L662-L691, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies that when function call filtering policies are applied and then a speaker repetition restriction eliminates all potential speakers, the system correctly raises a `NoEligibleSpeakerError` instead of crashing. It simulates a scenario where only one agent can execute a required function, but a policy prevents them from speaking again.*


### test_h10_guard_does_not_fire_when_last_speaker_outside_group (method, L693-L717, parent: TestAdversarialGroupChatEligibilityDeep)

> *Summary: This test verifies that a specific eligibility guard does not incorrectly trigger when the most recent speaker is outside the defined group. It confirms that if no agents are eligible within the group context, the system correctly defaults to allowing all agents rather than signaling zero candidates.*

