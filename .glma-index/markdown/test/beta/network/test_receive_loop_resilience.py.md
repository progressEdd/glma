# test/beta/network/test_receive_loop_resilience.py

2 function(s): _agent, test_handler_exception_does_not_stop_receive_loop.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_handler_exception_does_not_stop_receive_loop | function |  |

## Chunks

### _agent (function, L30-L31)

> *Summary: Creates and returns a new `Agent` instance, initializing it with the provided name and a default test configuration. This function serves to instantiate an agent object for testing purposes.*


### test_handler_exception_does_not_stop_receive_loop (function, L35-L97)

> *Summary: This test verifies that a receiving loop continues processing subsequent messages even if an envelope handler raises an exception for the first message. It sets up two agents, forces one agent's receiver to crash on the first incoming text envelope, and then asserts that both sent envelopes are successfully delivered and received.*

