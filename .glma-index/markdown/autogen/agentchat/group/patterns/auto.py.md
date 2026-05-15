# autogen/agentchat/group/patterns/auto.py

1 class(es): AutoPattern. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AutoPattern | class |  |

## Chunks

### AutoPattern (class, L19-L160)

> *Summary: This class manages a group chat where the next speaker is automatically selected by a designated group manager based on agent expertise. It initializes with participating agents and configuration, ensuring all necessary LLM and description prerequisites are met before preparing the group chat components for execution.*


### __init__ (method, L27-L69, parent: AutoPattern)

> *Summary: Configures an automated group chat pattern by initializing a `GroupChatManager` whose subsequent action is dictated by a provided selection message. It accepts various agents, context variables, and configuration options to manage the flow of conversation among participants.*


### prepare_group_chat (method, L71-L160, parent: AutoPattern)

> *Summary: This method configures the necessary components for an organic group chat by validating LLM configurations and ensuring all agents possess descriptions. It takes maximum rounds and initial messages as input, returning a comprehensive tuple containing agents, managers, tools, and conversation state objects.*

