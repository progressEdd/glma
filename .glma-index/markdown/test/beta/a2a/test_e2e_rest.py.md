# test/beta/a2a/test_e2e_rest.py

1 class(es): TestE2ERest. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestE2ERest | class |  |

## Chunks

### TestE2ERest (class, L13-L37)

> *Summary: This test suite verifies the end-to-end behavior of REST interactions by simulating various communication patterns. It tests single-turn round trips with both non-streaming and streaming modes, as well as multi-turn conversations where history is correctly propagated through subsequent requests.*


### test_single_turn_round_trip_polling (method, L14-L19, parent: TestE2ERest)

> *Summary: This test verifies a single-turn request/response cycle by sending a "ping" message and asserting that the received response content matches the expected "pong" value from the established REST pair. It confirms successful synchronous communication between two endpoints.*


### test_single_turn_round_trip_streaming (method, L21-L26, parent: TestE2ERest)

> *Summary: This test verifies a single-turn, round-trip communication over a streamed REST connection. It sends the "rest ping" request and asserts that the received response content matches the expected stream identifier.*


### test_multi_turn_history_propagated_through_rest (method, L28-L37, parent: TestE2ERest)

> *Summary: This test verifies that a sequence of interactions maintains conversational context across multiple turns using the REST interface. It sends two sequential inputs, asserting that the underlying tracking mechanism correctly records only the final input ("second").*

