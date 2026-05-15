# test/agentchat/group/test_safeguards.py

5 class(es): TestSafeguardEnforcer, TestInvalidPolicies, TestSafeguardChecks, TestApplySafeguards, TestResetSafeguards. 26 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestSafeguardEnforcer | class |  |
| TestInvalidPolicies | class |  |
| TestSafeguardChecks | class |  |
| TestApplySafeguards | class |  |
| TestResetSafeguards | class |  |

## Chunks

### TestSafeguardEnforcer (class, L25-L73)

> *Summary: This test suite verifies the `SafeguardEnforcer` class by testing its initialization with valid and invalid policy configurations. It ensures correct loading from JSON files, validates required fields, and checks for proper error handling when encountering unsupported check methods.*


### test_valid_policy_initialization (method, L28-L45, parent: TestSafeguardEnforcer)

> *Summary: This test verifies that the `SafeguardEnforcer` correctly initializes when provided with a valid policy structure containing inter-agent transition rules. It asserts that the internal list of configured rules is populated upon successful instantiation.*


### test_policy_file_loading (method, L47-L53, parent: TestSafeguardEnforcer)

> *Summary: This test verifies that the `SafeguardEnforcer` correctly loads a predefined policy structure from a simulated file input. It asserts that the internal policy attribute matches the expected dictionary content after initialization.*


### test_missing_required_fields (method, L55-L60, parent: TestSafeguardEnforcer)

> *Summary: Asserts that instantiating the `SafeguardEnforcer` with a policy missing required fields raises a `ValueError`. This verifies the input validation mechanism for safeguard policies.*


### test_invalid_check_method (method, L62-L73, parent: TestSafeguardEnforcer)

> *Summary: This test verifies that initializing a `SafeguardEnforcer` with an invalid `check_method` within the policy raises a `ValueError`. It asserts that the error message specifically indicates an "invalid check\_method".*


### TestInvalidPolicies (class, L76-L262)

> *Summary: This test suite verifies that the `SafeguardEnforcer` correctly validates various policy structures by asserting that it raises a `ValueError` when policies are missing required fields, use invalid methods (like outdated patterns), or contain syntactically incorrect data (such as bad regex). It ensures comprehensive input validation across different safeguard types like agent transitions and tool interactions.*


### test_missing_check_method (method, L79-L95, parent: TestInvalidPolicies)

> *Summary: Asserts that initializing a `SafeguardEnforcer` with a policy lacking the mandatory `check_method` field raises a `ValueError`. This verifies the enforcement mechanism correctly validates input structure.*


### test_missing_action_fields (method, L97-L113, parent: TestInvalidPolicies)

> *Summary: Asserts that initializing a `SafeguardEnforcer` with an incomplete policy structure raises a `ValueError`. This occurs because the provided policy lacks the necessary "violation\_response" or "action" fields within its agent transition definitions.*


### test_invalid_check_method_pattern (method, L115-L132, parent: TestInvalidPolicies)

> *Summary: Asserts that initializing a `SafeguardEnforcer` with an outdated `"pattern"` value for `check_method` raises a `ValueError`. This verifies the system correctly rejects policies using deprecated validation methods.*


### test_tool_interaction_missing_action (method, L134-L151, parent: TestInvalidPolicies)

> *Summary: Verifies that the `SafeguardEnforcer` raises a `ValueError` when a tool interaction policy is missing the required "action" field. This test confirms proper validation of input policies during enforcement setup.*


### test_llm_interaction_missing_action (method, L153-L170, parent: TestInvalidPolicies)

> *Summary: Verifies that the `SafeguardEnforcer` raises a `ValueError` when an LLM interaction safeguard policy is missing the mandatory "action" field. It tests this by initializing the enforcer with a configuration dictionary lacking the required action parameter in its regex check.*


### test_llm_check_method_missing_required_fields (method, L172-L189, parent: TestInvalidPolicies)

> *Summary: Verifies that the `SafeguardEnforcer` raises a `ValueError` when an LLM check method is configured without specifying either a `custom_prompt` or a `disallow_item`. This test ensures required configuration fields are present for LLM-based safeguards.*


### test_regex_check_method_missing_pattern (method, L191-L208, parent: TestInvalidPolicies)

> *Summary: Verifies that the `SafeguardEnforcer` raises a `ValueError` when an agent transition rule specifies `"regex"` as the check method but omits the required `"pattern"` field in the policy configuration. This ensures proper validation of regex-based safeguards during initialization.*


### test_invalid_regex_pattern (method, L210-L227, parent: TestInvalidPolicies)

> *Summary: Verifies that initializing a `SafeguardEnforcer` with a policy containing an invalid regular expression pattern raises a `ValueError`. This test confirms the system correctly rejects configurations where the specified regex is malformed.*


### test_tool_interaction_llm_missing_message_fields (method, L229-L245, parent: TestInvalidPolicies)

> *Summary: Verifies that the system raises a `ValueError` when an LLM tool interaction safeguard policy is missing required fields like `message_source` or `message_destination`. This test confirms proper validation of configuration inputs before enforcement.*


### test_completely_invalid_tool_interaction_format (method, L247-L262, parent: TestInvalidPolicies)

> *Summary: Verifies that an `AgentEnvironmentSafeguards` policy containing a tool interaction with completely missing or invalid fields raises a `ValueError`. This test ensures the system fails early when encountering malformed tool interaction data.*


### TestSafeguardChecks (class, L265-L341)

> *Summary: This test suite verifies the functionality of message safeguards by instantiating an `SafeguardEnforcer` with various policies. It tests whether regex rules correctly block or allow messages, and confirms that both LLM and regex guardrails are instantiated properly based on the provided policy configuration.*


### regex_enforcer (method, L269-L284, parent: TestSafeguardChecks)

> *Summary: Creates a `SafeguardEnforcer` instance configured with an inter-agent safeguard. This policy specifically blocks any message from `agent1` to `agent2` if it contains the word "password".*


### test_regex_block_violation (method, L286-L291, parent: TestSafeguardChecks)

> *Summary: This test verifies that the regex enforcer correctly blocks messages containing sensitive keywords like "password." It asserts that the returned dictionary indicates a block if the message violates the defined rules.*


### test_regex_pass_safe_message (method, L293-L298, parent: TestSafeguardChecks)

> *Summary: Verifies that a benign input message passes the safety checks enforced by a `SafeguardEnforcer`. It calls the inter-agent communication check with a safe string and asserts the original message is returned unchanged.*


### test_llm_guardrail_creation (method, L300-L321, parent: TestSafeguardChecks)

> *Summary: This test verifies that a `SafeguardEnforcer` correctly initializes an inter-agent rule when provided with a specific policy configuration. It asserts that the enforcer contains exactly one rule, and that this rule is instantiated as an `LLMGuardrail`.*


### test_regex_guardrail_creation (method, L323-L341, parent: TestSafeguardChecks)

> *Summary: This test verifies that a `SafeguardEnforcer` correctly initializes an inter-agent rule when provided with a policy defining a regex check between two agents. It asserts the existence and correct type of the created `RegexGuardrail` instance based on the input configuration.*


### TestApplySafeguards (class, L344-L388)

> *Summary: This test suite verifies the integration of safeguard policies by applying them to a mocked agent. It confirms that when a policy is applied with defined targets, hooks are correctly added to the agent's message processing pipeline, and it asserts that an error is raised if no agents or groupchat manager are provided in the policy application call.*


### mock_agent (method, L348-L360, parent: TestApplySafeguards)

> *Summary: Creates a mock implementation of `ConversableAgent` for testing purposes. This mock object is configured with a specific name and empty hook lists across various message processing stages.*


### test_apply_safeguards_to_agents (method, L362-L381, parent: TestApplySafeguards)

> *Summary: This test verifies that a specified safeguard policy is correctly applied to an agent. It asserts that the resulting enforcer object contains hooks on the agent for message processing before sending, based on the defined regex-based inter-agent rules.*


### test_apply_safeguards_no_targets (method, L383-L388, parent: TestApplySafeguards)

> *Summary: When called with an empty safeguard policy dictionary, the function raises a `ValueError` because it requires either agent definitions or a group chat manager to be present. This test verifies that safeguards cannot be applied without specifying targets.*


### TestResetSafeguards (class, L391-L462)

> *Summary: This test suite verifies the `reset_safeguard_policy` function by mocking an agent and asserting that specific safeguard hook lists are cleared after calling the reset function. It also tests error handling for missing targets when resetting safeguards and validates policy application against invalid agent names.*


### mock_agent (method, L395-L409, parent: TestResetSafeguards)

> *Summary: Creates a mock `ConversableAgent` instance configured with empty lists for various safeguard hooks. This mock is specifically designed to bypass certain internal methods, ensuring the test relies on fallback behavior.*


### test_reset_safeguards_from_agents (method, L411-L438, parent: TestResetSafeguards)

> *Summary: This test verifies that the `reset_safeguard_policy` function successfully clears specific hook lists associated with an agent. It injects mock functions into safeguard and message processing hooks, then asserts that these lists are empty after the reset operation.*


### test_reset_safeguards_no_targets (method, L440-L443, parent: TestResetSafeguards)

> *Summary: Asserts that calling the safeguard policy reset function raises a `ValueError` when no agent or group chat manager is supplied as input. This verifies the required dependency check for the reset operation.*


### test_invalid_agent_names (method, L445-L462, parent: TestResetSafeguards)

> *Summary: This test verifies that applying a safeguard policy fails when an invalid agent name ("unknown\_agent") is present in the transition rules. It asserts that calling `apply_safeguard_policy` with this configuration raises a `ValueError`.*

