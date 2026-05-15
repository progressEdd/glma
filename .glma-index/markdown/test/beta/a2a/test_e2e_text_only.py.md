# test/beta/a2a/test_e2e_text_only.py

1 class(es): TestE2ETextOnly. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestE2ETextOnly | class |  |

## Chunks

### TestE2ETextOnly (class, L13-L33)

> *Summary: This test suite verifies end-to-end communication by testing both single-turn and streaming request/response cycles against a service. It confirms that the client correctly receives expected responses and validates that user inputs are accurately logged in the request history sent to the server.*


### test_single_turn_round_trip (method, L14-L19, parent: TestE2ETextOnly)

> *Summary: This test verifies a single-turn interaction by creating a text pair and sending the message "ping". It asserts that the received response content matches the initial input string, "hello world".*


### test_streaming_round_trip (method, L21-L26, parent: TestE2ETextOnly)

> *Summary: This asynchronous test verifies a round-trip communication by sending the "ping" message to a streamed pair and asserting that the received response content matches the expected string, "streamed". It confirms correct data handling within a streaming context.*


### test_server_sees_user_input_in_history (method, L28-L33, parent: TestE2ETextOnly)

> *Summary: This test verifies that the server correctly receives user input by asserting a specific call to `tracking.mock` containing the submitted text within a `ModelRequest`. It simulates a client sending "hello server" and checks if this input is logged as expected.*

