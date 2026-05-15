# autogen/agentchat/group/patterns/manual.py

1 class(es): ManualPattern. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ManualPattern | class |  |

## Chunks

### ManualPattern (class, L18-L177)

> *Summary: This class configures a group chat where user input dictates the next speaker turn. It initializes with participating agents and sets up the `GroupChatManager` to use an `AskUserTarget`, ensuring the conversation flow pauses to prompt the user for agent selection after each round.*


### __init__ (method, L21-L56, parent: ManualPattern)

> *Summary: This constructor sets up a manual group chat pattern by accepting an initial agent, a list of all participating agents, and various configuration options like user proxies and summary methods. It configures the group to always prompt the user for the next action after the conversation concludes.*


### prepare_group_chat (method, L58-L134, parent: ManualPattern)

> *Summary: This method configures the necessary components for an organic group chat by calling a parent implementation. It then overrides the resulting configuration to ensure the `group_after_work` state is used and sets up specific agent transition rules within the group chat instance.*


### _setup_allowed_transitions (method, L136-L177, parent: ManualPattern)

> *Summary: Configures speaker transition rules for a group chat by establishing that any eligible agent can follow any other eligible agent. It filters out the provided user agent and tool executor from the set of possible next speakers.*

