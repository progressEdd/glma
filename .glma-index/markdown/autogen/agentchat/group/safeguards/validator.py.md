# autogen/agentchat/group/safeguards/validator.py

1 class(es): SafeguardValidator. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SafeguardValidator | class |  |

## Chunks

### SafeguardValidator (class, L11-L435)

> *Summary: This class validates the structure and content of a safeguard policy dictionary. It accepts a policy object and, optionally, lists/mappings of available agents and their tools to perform comprehensive checks on inter-agent, environment, and user interaction rules. The output is either successful validation or raises specific `ValueError` exceptions upon finding any structural or semantic inconsistencies in the policy definitions.*


### __init__ (method, L14-L20, parent: SafeguardValidator)

> *Summary: Initializes the validator by storing a provided configuration dictionary that dictates the safety rules it will enforce during validation checks.*


### validate_policy_structure (method, L22-L33, parent: SafeguardValidator)

> *Summary: Checks if the policy object is a dictionary and then validates the structure of its nested inter-agent and agent-environment safeguard configurations. It raises an error if the top-level policy isn't a dictionary or if sub-components fail validation.*


### validate_policy_complete (method, L35-L47, parent: SafeguardValidator)

> *Summary: Ensures the provided list of agent names and their associated tool mappings are valid against existing configurations. It first validates the agents and then checks all tools listed in the mapping if any tools are present.*


### _validate_inter_agent_safeguards (method, L49-L116, parent: SafeguardValidator)

> *Summary: This method validates the structure and content of inter-agent safeguards defined within a policy. It rigorously checks `agent_transitions` for required fields, valid check methods (LLM or regex), and appropriate associated parameters like prompts or patterns. Additionally, it verifies the format of the top-level `groupchat_message_check`.*


### _validate_environment_safeguards (method, L118-L278, parent: SafeguardValidator)

> *Summary: This method validates the structure and content of environment safeguards defined in a policy, specifically checking `tool_interaction`, `llm_interaction`, and `user_interaction` rules. It ensures each rule specifies an explicit check method (`llm` or `regex`), defines required actions/responses, and adheres to specific structural requirements based on the chosen validation method.*


### validate_agent_names (method, L280-L352, parent: SafeguardValidator)

> *Summary: Verifies that all agent names referenced within the policy's safeguards (inter-agent transitions, tool interactions, LLM interactions, and user interactions) actually exist in the provided list of available agents. It raises a `ValueError` if any specified agent name is unknown or improperly formatted according to the safeguard rules.*


### validate_tool_names (method, L354-L381, parent: SafeguardValidator)

> *Summary: Ensures that tool names referenced within policy safeguards are valid and correctly associated with the specified agents. It iterates through environment rules to validate source and destination agent-tool relationships against the provided mappings and lists.*


### _validate_agent_tool_relationship (method, L383-L435, parent: SafeguardValidator)

> *Summary: This method validates the specified relationships between agents and tools within a policy rule. It checks three cases—Agent $\to$ Tool, Tool $\to$ Agent, and Tool $\to$ Tool—ensuring that referenced entities are known and that agents only interact with tools they are authorized to use based on provided mappings.*

