# test/beta/ag_ui/test_asgi.py

1 class(es): TestASGIEndpoint. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestASGIEndpoint | class |  |

## Chunks

### TestASGIEndpoint (class, L33-L83)

> *Summary: This test suite verifies the functionality of an ASGI endpoint generated from an `AGUIStream`. It confirms that the built endpoint correctly handles incoming HTTP POST requests containing a user message and returns a stream of events indicating the run started and finished successfully.*


### test_build_asgi_creates_endpoint (method, L34-L40, parent: TestASGIEndpoint)

> *Summary: This test verifies that the `AGUIStream` object correctly constructs an ASGI endpoint class when its `build_asgi()` method is called. It asserts that the resulting class inherits from `HTTPEndpoint`.*


### test_asgi_endpoint_handles_request (method, L42-L83, parent: TestASGIEndpoint)

> *Summary: This test verifies that an ASGI endpoint correctly processes a POST request containing a user message input for an agent. It asserts that the resulting streamed response contains expected `RUN_STARTED` and `RUN_FINISHED` events with matching thread and run IDs.*

