# test/agentchat/realtime_agent/test_swarm_start.py

1 class(es): TestSwarmE2E. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestSwarmE2E | class |  |

## Chunks

### TestSwarmE2E (class, L32-L147)

> *Summary: This test suite validates the end-to-end functionality of a `RealtimeAgent` by setting up a FastAPI server with a WebSocket endpoint. It simulates an audio input ("How is the weather in Seattle?") and asserts that the agent successfully invokes a mocked weather function, verifying both the call itself and timing constraints across different LLM configurations.*


### _test_e2e (method, L33-L107, parent: TestSwarmE2E)

> *Summary: This test sets up a FastAPI server with a WebSocket endpoint to simulate an end-to-end interaction between a `RealtimeAgent` and a conversational agent (`Weatherman`). It sends an audio stream request via the WebSocket, asserting that the integrated weather function is correctly called by the system.*


### test_e2e (method, L124-L147, parent: TestSwarmE2E)

> *Summary: This asynchronous test function executes an end-to-end verification of the `RealtimeAgent` by repeatedly calling a core testing method up to five times. It accepts LLM and OpenAI credentials as inputs, retrying upon failure to account for transient issues like voice recognition errors before finally raising the exception if all attempts fail.*

