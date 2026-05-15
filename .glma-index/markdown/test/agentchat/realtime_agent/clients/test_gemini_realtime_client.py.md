# test/agentchat/realtime_agent/clients/test_gemini_realtime_client.py

1 class(es): TestGeminiRealtimeClient. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGeminiRealtimeClient | class |  |

## Chunks

### TestGeminiRealtimeClient (class, L18-L104)

> *Summary: This test suite verifies the functionality of a Gemini Realtime Client by instantiating it with provided credentials and executing various asynchronous tests. It checks initialization, connection state handling (e.g., failing when not connected), event reading during active sessions, and successful text sending interactions that result in specific server events like `SessionCreated` or `turnComplete`.*


### client (method, L20-L24, parent: TestGeminiRealtimeClient)

> *Summary: This method constructs and returns a `GeminiRealtimeClient` instance by extracting the LLM configuration from provided `Credentials`. It serves as a factory to initialize the client with necessary model settings.*


### test_init (method, L26-L32, parent: TestGeminiRealtimeClient)

> *Summary: This test method initializes a `GeminiRealtimeClient` using provided mock credentials' LLM configuration. It asserts that the resulting client object conforms to the `RealtimeClientProtocol`.*


### test_not_connected (method, L37-L43, parent: TestGeminiRealtimeClient)

> *Summary: This test verifies that attempting to read events from a `GeminiRealtimeClient` instance before it has been connected raises a specific `RuntimeError`. It asserts that the expected exception is caught and that no other cancellation occurred during the attempt.*


### test_start_read_events (method, L49-L67, parent: TestGeminiRealtimeClient)

> *Summary: This test verifies that a client correctly processes incoming events from a real-time connection before being interrupted after a set duration. It asserts that the event stream was successfully read and that the first received event matches an expected `SessionCreated` type.*


### test_send_text (method, L73-L104, parent: TestGeminiRealtimeClient)

> *Summary: This test verifies the text sending functionality by connecting to a real-time client and asynchronously reading events for up to five seconds. It asserts that specific sequence of events, including `SessionCreated` and potentially an `AudioDelta` followed by a turn completion signal, are received based on whether the agent finishes speaking within the timeout.*

