# test/agentchat/test_eligibility_policy.py

15 function(s): test_selection_context_fields, test_selection_context_no_last_speaker, test_selection_context_frozen, test_always_eligible_satisfies_protocol, test_never_eligible_satisfies_protocol, test_runtime_checkable_isinstance, test_description_mutation_on_unavailable, test_description_restore_on_available, test_double_mark_unavailable_idempotent, test_mark_available_noop_when_not_marked and 5 more. 3 class(es): _AlwaysEligible, _NeverEligible, TestAdversarialEligibilityPolicy. 11 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _AlwaysEligible | class |  |
| _NeverEligible | class |  |
| test_selection_context_fields | function |  |
| test_selection_context_no_last_speaker | function |  |
| test_selection_context_frozen | function |  |
| test_always_eligible_satisfies_protocol | function |  |
| test_never_eligible_satisfies_protocol | function |  |
| test_runtime_checkable_isinstance | function |  |
| test_description_mutation_on_unavailable | function |  |
| test_description_restore_on_available | function |  |
| test_double_mark_unavailable_idempotent | function |  |
| test_mark_available_noop_when_not_marked | function |  |
| TestAdversarialEligibilityPolicy | class |  |
| test_description_containing_unavailable_substring_not_stripped | function |  |
| test_description_external_modification_preserved | function |  |
| test_description_mutation_thread_safety | function |  |
| test_selection_context_rejects_str_participants | function |  |
| test_mark_available_strips_external_prefix | function |  |

## Chunks

### _AlwaysEligible (class, L14-L16)

> *Summary: This class implements a policy that always returns `True` when queried. It takes an agent and a selection context as input and outputs a boolean indicating eligibility.*


### is_eligible (method, L15-L16, parent: _AlwaysEligible)

> *Summary: This method checks if an agent meets the criteria for selection by accepting an `agent` object and a `SelectionContext`. Currently, it unconditionally returns `True`, indicating eligibility.*


### _NeverEligible (class, L19-L21)

> *Summary: This class implements a policy that always returns `False` when queried. It takes an agent and a selection context as input to determine eligibility.*


### is_eligible (method, L20-L21, parent: _NeverEligible)

> *Summary: This method currently returns `False` unconditionally, indicating that no agent meets the eligibility criteria based on the provided agent and context. It serves as a placeholder for future logic determining agent suitability.*


### test_selection_context_fields (function, L24-L28)

> *Summary: Verifies that a `SelectionContext` object correctly stores and exposes its initial state, including the current round number, the last speaker's name, and the set of participants. It confirms these attributes match the values provided during instantiation.*


### test_selection_context_no_last_speaker (function, L31-L33)

> *Summary: Verifies that a `SelectionContext` initialized with no previous speaker correctly sets the `last_speaker` attribute to `None`. This test confirms the initial state when only one participant exists and no prior turns have occurred.*


### test_selection_context_frozen (function, L36-L39)

> *Summary: Verifies that the `SelectionContext` object is immutable by asserting an exception is raised when attempting to modify its internal state (e.g., changing the `round`). It takes a pre-configured context as input and expects failure upon mutation attempts.*


### test_always_eligible_satisfies_protocol (function, L42-L45)

> *Summary: Verifies that a policy designed to always grant eligibility returns `True` when evaluated against any object and a provided selection context. This test confirms the basic functionality of the $\text{AlwaysEligible}$ implementation.*


### test_never_eligible_satisfies_protocol (function, L48-L51)

> *Summary: Verifies that a policy designed to never grant eligibility correctly returns `False` when evaluated against a specific context and object input. This test confirms the expected behavior of an always-false eligibility check.*


### test_runtime_checkable_isinstance (function, L54-L55)

> *Summary: Verifies that an instance of `_AlwaysEligible` correctly reports as being an instance of the `AgentEligibilityPolicy`. This confirms runtime type checking for eligibility policy implementations.*


### test_description_mutation_on_unavailable (function, L58-L64)

> *Summary: This test verifies that when an `AgentDescriptionGuard` is marked unavailable, the underlying agent's description string is mutated to include a `[UNAVAILABLE]` prefix while retaining its original content. It uses mocks to simulate the agent and guard interaction for this assertion.*


### test_description_restore_on_available (function, L67-L73)

> *Summary: This test verifies that an agent's description is correctly restored when it transitions from an unavailable to an available state. It mocks an agent, sets its description, simulates marking it as unavailable then available, and asserts the original description remains intact.*


### test_double_mark_unavailable_idempotent (function, L76-L82)

> *Summary: This test verifies that calling the `mark_unavailable` method twice on an agent description guard results in only a single "[UNAVAILABLE]" marker being applied to the underlying agent's description. It confirms the idempotency of the unavailability marking process.*


### test_mark_available_noop_when_not_marked (function, L85-L90)

> *Summary: When an `AgentDescriptionGuard` is initialized with a mock agent and its `mark_available()` method is called, the underlying agent's description remains unchanged if it was not previously marked as available. This test verifies that calling the marking function has no side effects when the state doesn't require modification.*


### TestAdversarialEligibilityPolicy (class, L93-L204)

> *Summary: This test suite verifies the robustness and correctness of eligibility policies and context handling under adversarial conditions. It tests scenarios like inconsistent state in `SelectionContext`, concurrent access to guard mechanisms (like preventing "thundering herd"), and how description mutations behave for agents with `None` or empty string descriptions.*


### test_selection_context_last_speaker_not_in_participants (method, L96-L101, parent: TestAdversarialEligibilityPolicy)

> *Summary: This test verifies that the `SelectionContext` object can correctly store a `last_speaker` name even if it is not present within the provided set of `participants`. It asserts that the context accepts this potentially inconsistent state without raising an error.*


### test_guard_thundering_herd_mark_unavailable (method, L103-L127, parent: TestAdversarialEligibilityPolicy)

> *Summary: This test simulates a "thundering herd" scenario by having 100 threads concurrently call `mark_unavailable()` on an `AgentDescriptionGuard`. It asserts that exactly one instance of the `[UNAVAILABLE]` prefix is recorded in the underlying agent's description, ensuring thread-safe state management.*


### test_description_mutation_none_description (method, L129-L135, parent: TestAdversarialEligibilityPolicy)

> *Summary: This test verifies that an `AgentDescriptionGuard` correctly handles an agent whose description is set to `None`. It asserts that calling `mark_unavailable()` on the guard does not cause a crash and instead modifies the agent's description to include `"[UNAVAILABLE]"`.*


### test_description_mutation_empty_string (method, L137-L143, parent: TestAdversarialEligibilityPolicy)

> *Summary: When an agent's description is set to an empty string, this test verifies that applying the `AgentDescriptionGuard` causes the agent's description attribute to be prefixed with "[UNAVAILABLE]". This confirms the guard correctly flags agents lacking a description.*


### test_mark_available_after_none_description (method, L145-L153, parent: TestAdversarialEligibilityPolicy)

> *Summary: This test verifies that when an agent's description is initially `None`, calling `mark_unavailable()` preserves this state, and subsequently calling `mark_available()` correctly restores the original `None` value to the agent object.*


### test_mark_available_noop_on_none_description (method, L155-L161, parent: TestAdversarialEligibilityPolicy)

> *Summary: When an agent's description is `None`, calling the availability marking function should execute as a no-operation without error. The test verifies that after the call, the agent's description remains either `None` or an empty string.*


### test_selection_context_participants_empty_tuple (method, L163-L166, parent: TestAdversarialEligibilityPolicy)

> *Summary: Verifies that a `SelectionContext` object initialized with an empty tuple for its participants remains valid and correctly stores the empty tuple. This test confirms the expected state when no participants are provided during context creation.*


### test_selection_context_negative_round (method, L168-L171, parent: TestAdversarialEligibilityPolicy)

> *Summary: This test verifies that the `SelectionContext` object correctly accepts and stores a negative round index (`-1`) without validation errors. It asserts that the provided context's `round` attribute matches the input value of `-1`.*


### test_concurrent_is_eligible_calls (method, L173-L204, parent: TestAdversarialEligibilityPolicy)

> *Summary: This test verifies the thread safety of an eligibility policy by concurrently calling its `is_eligible` method from multiple threads. It asserts that no exceptions occur during concurrent execution and that the internal call counter accurately reflects all initiated calls.*


### test_description_containing_unavailable_substring_not_stripped (function, L207-L222)

> *Summary: This test verifies that the `mark_available` method correctly preserves descriptions containing an `[UNAVAILABLE]` substring when it is not a prefix. It confirms that marking unavailable adds a prefix, and subsequent availability restoration removes only that specific prefix.*


### test_description_external_modification_preserved (function, L225-L239)

> *Summary: This test verifies that an `AgentDescriptionGuard` correctly preserves modifications made to an agent's description externally while the guard is active. It asserts that when transitioning from unavailable back to available, any appended text added outside the guard's control remains intact after the prefix is removed.*


### test_description_mutation_thread_safety (function, L242-L269)

> *Summary: This test verifies that concurrently calling `mark_unavailable` and `mark_available` methods does not corrupt the underlying description string of an agent. It spawns multiple threads to repeatedly toggle the state and asserts that the final description is either the original or contains at most one unavailability prefix.*


### test_selection_context_rejects_str_participants (function, L272-L275)

> *Summary: This test verifies that providing a bare string for the `participants` argument to `SelectionContext` correctly raises a `TypeError`, ensuring the context object does not attempt to iterate over the string's characters.*


### test_mark_available_strips_external_prefix (function, L278-L286)

> *Summary: This test verifies that the `mark_available` method strips an external `[UNAVAILABLE]` prefix from an agent's description, even if the guard itself was not triggered to mark it as unavailable. It asserts the final description matches the content after stripping the prefix.*

