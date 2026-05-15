# test/agentchat/contrib/capabilities/test_tools_capability.py

2 function(s): add_tools, test_agent. 1 class(es): TestToolsCapability. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| add_tools | function |  |
| test_agent | function |  |
| TestToolsCapability | class |  |

## Chunks

### add_tools (function, L13-L21)

> *Summary: This function returns a `Tool` object configured with an addition capability. It encapsulates a simple helper function that takes two integers as input and returns their sum.*


### test_agent (function, L25-L31)

> *Summary: This test function instantiates and returns an `AssistantAgent` configured to use the GPT-4o model via OpenAI, using a placeholder API key. It serves as a setup fixture for testing agent capabilities.*


### TestToolsCapability (class, L34-L45)

> *Summary: This test verifies that a capability correctly adds provided tools to an agent's configuration. It asserts that the tool count increases in both the LLM configuration and the execution function map after calling `add_to_agent`.*


### test_add_capability (method, L35-L45, parent: TestToolsCapability)

> *Summary: This test verifies that adding a capability successfully integrates tools into an agent's configuration. It asserts that the tool count increases in both the LLM configuration and the execution function map after calling `add_to_agent`.*

