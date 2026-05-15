# test/agentchat/contrib/capabilities/chat_with_teachable_agent.py

2 function(s): create_teachable_agent, interact_freely_with_user.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| create_teachable_agent | function |  |
| interact_freely_with_user | function |  |

## Chunks

### create_teachable_agent (function, L20-L44)

> *Summary: This function constructs and returns a `ConversableAgent` equipped with a `Teachability` capability. It loads LLM configurations from environment variables or files, initializes the agent and the teachability module with specified parameters, and then integrates the latter into the former.*


### interact_freely_with_user (function, L47-L55)

> *Summary: Initializes an interactive session by creating and connecting a `TeachableAgent` with a human-controlled `UserProxyAgent`. This function then starts a free-form chat conversation between the two agents.*

