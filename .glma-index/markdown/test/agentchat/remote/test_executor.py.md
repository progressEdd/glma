# test/agentchat/remote/test_executor.py

4 function(s): test_smoke, test_remote_tool_call, test_update_context, test_guardrails.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_smoke | function |  |
| test_remote_tool_call | function |  |
| test_update_context | function |  |
| test_guardrails | function |  |

## Chunks

### test_smoke (function, L19-L38)

> *Summary: This test verifies the basic functionality of a remote agent by sending an initial message and asserting that the service returns the expected predefined response. It uses a `TestAgent` wrapper to simulate the remote interaction flow.*


### test_remote_tool_call (function, L42-L98)

> *Summary: This test verifies the end-to-end execution flow when an agent invokes a registered remote tool. It sends an initial message to the agent service and asserts that the resulting sequence of responses correctly includes the tool call, the tool's output, and the final conversational reply.*


### test_update_context (function, L102-L143)

> *Summary: This test verifies that an agent correctly updates its internal context when invoked with a specific tool call. It passes initial context data to the service, which triggers the registered `update_context` function to modify the time variable before returning the final state.*


### test_guardrails (function, L147-L175)

> *Summary: This test verifies that input and output guardrails are correctly triggered when an agent processes a message. It mocks the guardrail checks to assert that the respective `check` methods were called exactly once with the expected input and output content.*

