# autogen/agentchat/group/safeguards/api.py

2 function(s): reset_safeguard_policy, apply_safeguard_policy.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| reset_safeguard_policy | function |  |
| apply_safeguard_policy | function |  |

## Chunks

### reset_safeguard_policy (function, L20-L109)

> *Summary: Removes all applied safeguard hooks and inter-agent guardrails from specified agents or a `GroupChatManager`. It accepts either a list of agents or the manager object as input, logging events throughout the process to confirm the removal of safeguards.*


### apply_safeguard_policy (function, L112-L241)

> *Summary: Configures and enforces safety policies across a set of agents or an entire group chat manager based on a provided policy file or dictionary. It validates the policy against agent names and available tools, then injects necessary safeguard hooks into the target agents for runtime monitoring.*

