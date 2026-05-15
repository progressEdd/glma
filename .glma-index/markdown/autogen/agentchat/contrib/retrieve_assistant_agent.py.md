# autogen/agentchat/contrib/retrieve_assistant_agent.py

1 class(es): RetrieveAssistantAgent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| RetrieveAssistantAgent | class |  |

## Chunks

### RetrieveAssistantAgent (class, L17-L59)

> *Summary: This deprecated agent subclass of `AssistantAgent` is configured to solve tasks using an LLM with a specific system message. It processes incoming messages and returns a termination signal (`TERMINATE`, `UPDATE CONTEXT`, or continues) based on keywords found in the last message's content, rather than executing code by default.*


### __init__ (method, L28-L35, parent: RetrieveAssistantAgent)

> *Summary: This constructor warns the user that the agent is deprecated in favor of `AssistantAgent`. It then initializes the base class and registers a specific reply generation method for this agent type.*


### _generate_retrieve_assistant_reply (method, L37-L59, parent: RetrieveAssistantAgent)

> *Summary: Determines the next action based on the last message content from a conversation history. It checks for specific termination or context update phrases within the input messages to return a boolean status and an action command ("TERMINATE", "UPDATE CONTEXT", or `None`).*

