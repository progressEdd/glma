# test/tools/experimental/reliable/test_reliable.py

1 function(s): setup_test_environment. 1 class(es): TestReliableTool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| setup_test_environment | function |  |
| TestReliableTool | class |  |

## Chunks

### setup_test_environment (function, L37-L46)

> *Summary: This generator function creates and manages a temporary directory for testing SQLite databases. It changes the current working directory to this temporary location during execution and restores the original directory upon completion.*


### TestReliableTool (class, L49-L167)

> *Summary: These tests verify the `ReliableTool`'s ability to handle transient failures by automatically retrying execution. They pass a task string and credentials, expecting the tool to successfully complete after one or more internal attempts, depending on whether the underlying function simulates a bad response or an exception.*


### test_bad_response (method, L51-L87, parent: TestReliableTool)

> *Summary: This test verifies the resilience of a tool by simulating an initial failure condition. It executes a `ReliableTool` designed to generate sub-questions, asserting that the execution attempts exactly twice—once failing and once succeeding due to internal state management.*


### test_error (method, L90-L126, parent: TestReliableTool)

> *Summary: This test verifies the error handling mechanism of a `ReliableTool` by intentionally causing the underlying function to raise an exception on its first invocation. It asserts that the tool correctly retries until the internal state changes, resulting in exactly two total attempts for the execution.*


### test_return_tuple (method, L129-L167, parent: TestReliableTool)

> *Summary: This test verifies the behavior of a `ReliableTool` designed to generate sub-questions, expecting it to fail on its first invocation and succeed on the second. It passes an initial question string as input and asserts that the resulting execution details confirm exactly two attempts were made and that the final output is structured as both a list and a string.*

