# test/ag_ui/test_asgi.py

1 class(es): TestASGIEndpoint. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestASGIEndpoint | class |  |

## Chunks

### TestASGIEndpoint (class, L33-L86)

> *Summary: This test suite verifies the functionality of an ASGI endpoint generated from an `AGUIStream` wrapping a `ConversableAgent`. It confirms that the built endpoint correctly handles incoming HTTP POST requests containing user messages and returns a stream of events, specifically asserting the presence of `RUN_STARTED` and `RUN_FINISHED` events.*


### test_build_asgi_creates_endpoint (method, L34-L40, parent: TestASGIEndpoint)

> *Summary: This test verifies that building an ASGI interface from a `ConversableAgent` results in a class inheriting from `HTTPEndpoint`. It confirms the generated endpoint correctly wraps the agent's streaming capabilities.*


### test_asgi_endpoint_handles_request (method, L42-L86, parent: TestASGIEndpoint)

> *Summary: This test verifies that an ASGI endpoint correctly processes a user message input via a POST request to the root path. It asserts that the resulting response stream contains `RUN_STARTED` and `RUN_FINISHED` events matching the provided input's thread and run IDs.*

