# autogen/agentchat/contrib/captainagent/captainagent.py

2 class(es): CaptainAgent, CaptainUserProxyAgent. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CaptainAgent | class |  |
| CaptainUserProxyAgent | class |  |

## Chunks

### CaptainAgent (class, L21-L244)

> *Summary: This class orchestrates complex tasks by acting as a manager that can either solve problems directly or delegate them to a group of specialized agents via a `seek_experts_help` tool. It initializes an internal assistant and executor, configuring nested chats for expert collaboration based on provided system messages and configuration dictionaries.*


### __init__ (method, L136-L227, parent: CaptainAgent)

> *Summary: Initializes a specialized agent by configuring its core components like system messages and LLM settings based on provided arguments. It then sets up an internal assistant and executor agents, linking them with nested chat configurations for complex interactions.*


### _update_config (method, L230-L244, parent: CaptainAgent)

> *Summary: This method merges configuration settings from an `update_dict` into a `default_dict`. It recursively updates nested dictionaries while overwriting existing values with those provided in the update dictionary.*


### CaptainUserProxyAgent (class, L247-L513)

> *Summary: This agent acts as a proxy to execute code and provide feedback within an automated group chat environment. It initializes by accepting configuration for nested chats, then uses `AgentBuilder` to construct a team of specialized agents based on provided tasks, optionally binding them with relevant tools before initiating the conversation and summarizing the resulting history.*


### __init__ (method, L295-L375, parent: CaptainUserProxyAgent)

> *Summary: Initializes a specialized agent by accepting configurations for its name, nested chat, LLM settings, and operational modes like human input handling and code execution. It sets up internal state management, registers a function to seek expert help, and stores the provided configuration parameters.*


### _run_autobuild (method, L377-L513, parent: CaptainUserProxyAgent)

> *Summary: Constructs and configures a group of agents using an `AgentBuilder` based on provided tasks, either by loading previous configurations or building anew. It optionally binds relevant tools to the agents if coding is enabled, then initiates a nested group chat with the resulting agent team before summarizing the entire conversation history for output.*

