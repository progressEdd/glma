# test/agents/contrib/time/test_timereplyagent.py

1 class(es): TestTimeReplyAgent. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTimeReplyAgent | class |  |

## Chunks

### TestTimeReplyAgent (class, L13-L59)

> *Summary: This test suite verifies the functionality of a time-replying agent by checking its initialization parameters (format, prefix, system message). It also confirms that the agent correctly responds to a query about the current date and time, validating both the content and any specified output prefixes.*


### test_init (method, L14-L25, parent: TestTimeReplyAgent)

> *Summary: Verifies that an instance of `TimeReplyAgent` initializes correctly with specified configuration parameters, asserting that internal attributes like format string, output prefix, and system message match the provided inputs.*


### test_output (method, L27-L59, parent: TestTimeReplyAgent)

> *Summary: This test verifies that a `TimeReplyAgent` correctly responds to a query about the current date and time from another agent. It asserts both the standard output format and confirms the ability to prepend custom prefixes to the response.*

