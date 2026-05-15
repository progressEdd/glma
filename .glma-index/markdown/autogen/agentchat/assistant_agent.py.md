# autogen/agentchat/assistant_agent.py

1 class(es): AssistantAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AssistantAgent | class |  |

## Chunks

### AssistantAgent (class, L17-L86)

> *Summary: This agent acts as a helpful AI assistant designed to solve tasks using LLM capabilities, including suggesting Python or shell code blocks for execution. It accepts configuration parameters like name, system message, and LLM settings, defaulting to a strict mode where it suggests code but doesn't execute it automatically.*


### __init__ (method, L43-L86, parent: AssistantAgent)

> *Summary: Initializes an assistant agent by accepting configuration parameters such as a name, system message, LLM settings, and behavior controls like termination checks and input modes. It then sets up the agent's description, potentially defaulting it if none is provided and the standard system message is used.*

