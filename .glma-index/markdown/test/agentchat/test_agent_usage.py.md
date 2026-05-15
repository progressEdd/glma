# test/agentchat/test_agent_usage.py

2 function(s): test_gathering, test_agent_usage.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_gathering | function |  |
| test_agent_usage | function |  |

## Chunks

### test_gathering (function, L18-L66)

> *Summary: This test function initializes three `AssistantAgent` instances with different LLM configurations and manually sets their usage summaries. It then calls a helper to aggregate these usages, asserting the correct total costs for both GPT-4o Mini and GPT-4o across the agents. Finally, it tests the aggregation logic by passing a `UserProxyAgent` without pre-set client data.*


### test_agent_usage (function, L70-L128)

> *Summary: This test function initializes an `AssistantAgent` and a `UserProxyAgent`, then initiates a chat with a math problem to verify agent interaction. It further asserts the logging output of both agents' usage summaries and checks their actual and total usage statistics.*

