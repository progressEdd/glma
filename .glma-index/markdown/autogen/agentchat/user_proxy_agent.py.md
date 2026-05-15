# autogen/agentchat/user_proxy_agent.py

1 class(es): UserProxyAgent. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| UserProxyAgent | class |  |

## Chunks

### UserProxyAgent (class, L17-L114)

> *Summary: This class acts as a user proxy agent capable of executing code and receiving human feedback within an automated conversation. It is initialized with configuration parameters controlling its input mode ("ALWAYS", "TERMINATE", or "NEVER"), code execution settings, and LLM interaction capabilities. The primary behavior involves prompting the user for input based on the configured mode while managing conversational flow and code execution.*


### __init__ (method, L36-L114, parent: UserProxyAgent)

> *Summary: Initializes a user proxy agent with configurations for its name, human interaction mode, termination conditions, and capabilities like function calling or code execution. It accepts various optional parameters to customize behavior such as LLM settings, system prompts, and default replies before setting up the base agent.*

