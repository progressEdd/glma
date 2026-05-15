# test/beta/a2a/test_e2e_grpc.py

1 class(es): TestE2EGrpc. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestE2EGrpc | class |  |

## Chunks

### TestE2EGrpc (class, L13-L46)

> *Summary: This test suite verifies end-to-end functionality of a gRPC service by simulating various communication scenarios. It tests single-turn round trips with both non-streaming and streaming modes, as well as multi-turn conversations to ensure message history is correctly propagated.*


### test_single_turn_round_trip_polling (method, L14-L22, parent: TestE2EGrpc)

> *Summary: This test verifies a single-turn round trip by starting a gRPC pair, sending a "ping" request to the client, and asserting that the received response content matches the initial "pong" message sent during setup. It ensures proper cleanup of the server after execution.*


### test_single_turn_round_trip_streaming (method, L24-L32, parent: TestE2EGrpc)

> *Summary: This test verifies a single-turn, round-trip streaming interaction by initiating a gRPC pair and sending a "ping" request to the client. It asserts that the received response content matches the expected string, ensuring successful bidirectional communication.*


### test_multi_turn_history_propagated_through_grpc (method, L34-L46, parent: TestE2EGrpc)

> *Summary: This test verifies that conversational history is correctly passed through a gRPC interaction by sending sequential prompts ("first" then "second"). It asserts that the underlying tracking mechanism receives the second input, confirming stateful message propagation across the RPC boundary.*

