# autogen/agentchat/group/patterns/random.py

1 class(es): RandomPattern. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RandomPattern | class |  |

## Chunks

### RandomPattern (class, L17-L106)

> *Summary: This class configures a group chat to facilitate random agent interaction. It takes maximum rounds and initial messages as input, then sets up random handoffs between all participating agents (including the user agent) before returning all necessary components for the group chat execution.*


### _generate_handoffs (method, L20-L34, parent: RandomPattern)

> *Summary: This method configures agents to randomly pass control to other participants in the conversation group. It iterates through all involved agents and sets their post-task handoff target to a random selection from the remaining agents.*


### prepare_group_chat (method, L36-L106, parent: RandomPattern)

> *Summary: This method configures a group chat environment by first calling the parent's preparation logic to set up agents and context. It then overrides this setup by generating random handoffs between the participating agents before returning all necessary components for the conversation flow.*

