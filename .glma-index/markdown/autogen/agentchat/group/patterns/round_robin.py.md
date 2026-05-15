# autogen/agentchat/group/patterns/round_robin.py

1 class(es): RoundRobinPattern. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RoundRobinPattern | class |  |

## Chunks

### RoundRobinPattern (class, L17-L117)

> *Summary: This class configures a group chat to cycle through agents in a round-robin fashion. It takes an initial agent, a list of other agents, and an optional user agent as input to establish sequential handoffs between them, ensuring the last agent hands off back to the first. The primary method prepares all necessary components for the group chat while injecting these predefined agent transitions.*


### _generate_handoffs (method, L20-L45, parent: RoundRobinPattern)

> *Summary: This method constructs a sequence of agent handoffs by arranging agents in a round-robin order, starting with the initial agent and ending with the user agent if present. It then configures each agent to pass control to the next agent in this cyclical list after completing its task.*


### prepare_group_chat (method, L47-L117, parent: RoundRobinPattern)

> *Summary: This method configures a group chat environment by calling the parent implementation to set up agents and initial messages. It then customizes this setup by generating agent handoffs before returning all necessary components for the group chat execution.*

