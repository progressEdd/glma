# test/io/test_base.py

1 class(es): TestIOStream. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestIOStream | class |  |

## Chunks

### TestIOStream (class, L14-L59)

> *Summary: This test suite verifies the behavior of a global stream management system, ensuring that default I/O streams can be retrieved, set to custom implementations, and correctly managed across different threads. It confirms that setting a new default stream persists until explicitly changed back or the scope exits.*


### test_initial_default_io_stream (method, L15-L16, parent: TestIOStream)

> *Summary: Verifies that the default I/O stream returned by `IOStream` is an instance of `IOConsole`. This test confirms the expected type for the system's initial console output handler.*


### test_set_default_io_stream (method, L18-L39, parent: TestIOStream)

> *Summary: This test verifies that the `set_default` method correctly overrides and restores the globally accessible default I/O stream instance. It confirms that setting a custom stream, then another, and finally reverting ensures the correct stream type is active at each point.*


### test_get_default_on_new_thread (method, L41-L59, parent: TestIOStream)

> *Summary: This test verifies that `IOStream.get_default()` returns an `IOConsole` instance when called within a newly spawned thread. It achieves this by executing a target function in a separate thread and asserting the type of the returned object upon completion.*

