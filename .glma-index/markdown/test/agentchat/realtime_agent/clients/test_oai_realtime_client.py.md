# test/agentchat/realtime_agent/clients/test_oai_realtime_client.py

1 class(es): TestOAIRealtimeClient. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestOAIRealtimeClient | class |  |

## Chunks

### TestOAIRealtimeClient (class, L16-L92)

> *Summary: This test suite verifies the functionality of an `OpenAIRealtimeClient` by instantiating it with provided credentials and testing its asynchronous behavior. It asserts correct initialization, failure when not connected, successful event streaming upon connection, and proper text sending during a session.*


### client (method, L18-L22, parent: TestOAIRealtimeClient)

> *Summary: This method constructs and returns an `OpenAIRealtimeClient` instance by extracting the LLM configuration from the provided `Credentials`. It serves to initialize the client with necessary model settings.*


### test_init (method, L24-L30, parent: TestOAIRealtimeClient)

> *Summary: This test method initializes an `OpenAIRealtimeClient` using provided LLM configuration credentials. It asserts that the resulting client object conforms to the expected `RealtimeClientProtocol`.*


### test_not_connected (method, L34-L40, parent: TestOAIRealtimeClient)

> *Summary: Asserts that attempting to read events from an unconnected `OpenAIRealtimeClient` raises a specific `RuntimeError`. This verifies the client correctly enforces connection status before allowing event streaming.*


### test_start_read_events (method, L45-L64, parent: TestOAIRealtimeClient)

> *Summary: This test verifies the client's ability to process events over a limited time window. It connects, reads incoming events for three seconds while mocking them, and asserts that exactly two specific event types (`SessionCreated` and `SessionUpdated`) were received before the reading loop was interrupted.*


### test_send_text (method, L69-L92, parent: TestOAIRealtimeClient)

> *Summary: This test verifies the `send_text` functionality by establishing a connection, reading events for a fixed duration, and then asserting that specific session lifecycle events (`SessionCreated`, `SessionUpdated`) were received before the read loop was interrupted. It further confirms that the final event received is either an audio delta or a completion signal from the model response.*

