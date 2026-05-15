# test/agentchat/realtime_agent/test_e2e.py

1 class(es): TestE2E. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestE2E | class |  |

## Chunks

### TestE2E (class, L24-L124)

> *Summary: This code sets up and executes end-to-end tests for a `RealtimeAgent` by spinning up a FastAPI server with a WebSocket endpoint. It simulates an audio stream input, verifies that the agent correctly invokes a registered weather function based on user input, and asserts the correct parameters were passed to that mock function.*


### _test_e2e (method, L25-L87, parent: TestE2E)

> *Summary: This test sets up a FastAPI application with a WebSocket endpoint to simulate an end-to-end interaction with `RealtimeAgent`. It sends a text-to-speech audio payload via the WebSocket and asserts that the agent successfully calls a registered mock weather function with the correct input.*


### test_e2e (method, L104-L124, parent: TestE2E)

> *Summary: This asynchronous test repeatedly executes an end-to-end check for the `RealtimeAgent` up to five times. It uses provided LLM and OpenAI credentials as input, exiting successfully upon the first pass or raising an exception if all retries fail.*

