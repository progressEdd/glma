# cli/tests/test_runner.py

4 class(es): TestCliIOStream, TestRunResult, TestExecuteMain, TestExecuteUnknownKind. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestCliIOStream | class |  |
| TestRunResult | class |  |
| TestExecuteMain | class |  |
| TestExecuteUnknownKind | class |  |

## Chunks

### TestCliIOStream (class, L11-L39)

> *Summary: This test suite verifies the functionality of `CliIOStream` by asserting correct behavior for capturing printed output via callbacks, handling print calls without a callback, recording sent events, and simulating input/output operations. It confirms that printing with custom separators works as expected when an event handler is provided.*


### test_print_callback (method, L14-L18, parent: TestCliIOStream)

> *Summary: This test verifies that the `CliIOStream` correctly captures output when its `on_print` callback is used. It calls `stream.print()` with two arguments and asserts that the captured list contains a single string combining those inputs separated by a space.*


### test_print_no_callback (method, L20-L22, parent: TestCliIOStream)

> *Summary: This test verifies that calling the `print` method on a `CliIOStream` instance with no callback handler executes without error. It confirms basic, non-callback printing functionality.*


### test_send_callback (method, L24-L29, parent: TestCliIOStream)

> *Summary: This test verifies that a stream correctly captures events sent to it. It sends two strings, and asserts that the internal capture list contains both inputs in order.*


### test_input_returns_empty (method, L31-L33, parent: TestCliIOStream)

> *Summary: Verifies that when the input method is called on a `CliIOStream` instance, it correctly returns an empty string. This tests the default behavior of reading from the simulated input source.*


### test_print_with_sep (method, L35-L39, parent: TestCliIOStream)

> *Summary: This test verifies that the `print` method, when provided with a separator, correctly joins multiple arguments into a single string output. It asserts that the resulting list of printed strings matches the expected joined format using the specified separator.*


### TestRunResult (class, L42-L68)

> *Summary: This class contains unit tests verifying the default and populated states of a `RunResult` object. It asserts that an instance initializes with expected empty or null values, and confirms correct attribute assignment when initialized with specific data.*


### test_defaults (method, L45-L54, parent: TestRunResult)

> *Summary: Verifies that a newly instantiated `RunResult` object initializes all its attributes to default, empty, or null values. It asserts the initial state of fields like output, turn count, cost, and error lists are as expected upon creation.*


### test_with_values (method, L56-L68, parent: TestRunResult)

> *Summary: This test verifies the correct initialization and attribute assignment of a `RunResult` object using predefined values for output, turn count, elapsed time, agent names, and last speaker. It asserts that all provided input parameters are accurately reflected in the resulting object's state.*


### TestExecuteMain (class, L71-L175)

> *Summary: This test suite verifies the execution logic for discovered agent main functions by creating temporary Python files. It tests various scenarios including successful synchronous and asynchronous execution, handling missing functions or exceptions, capturing printed output, and measuring execution time.*


### test_execute_main_with_message (method, L74-L88, parent: TestExecuteMain)

> *Summary: This test verifies the execution flow by creating a temporary Python file containing a simple `main` function. It then discovers this module, executes it with an input message ("hello world"), and asserts that the returned output matches the expected string and that the execution resulted in one turn without errors.*


### test_execute_main_without_message_param (method, L90-L102, parent: TestExecuteMain)

> *Summary: This test verifies the execution flow when no message parameter is provided to the main entry point. It writes a simple Python file containing a `main` function and asserts that the execution returns the expected hardcoded output from that function.*


### test_execute_main_no_function (method, L104-L115, parent: TestExecuteMain)

> *Summary: When provided with an agent configuration lacking a `main_fn`, the execution process is expected to fail and return an error indicating that no main function was found. This test verifies this failure condition by calling `execute` with `main_fn=None`.*


### test_execute_captures_print (method, L117-L131, parent: TestExecuteMain)

> *Summary: This test verifies that the `on_print` callback correctly captures output from an executed script. It runs a simple Python function defined in a temporary file and asserts that the returned result matches the expected uppercase transformation of the input string.*


### test_execute_async_main (method, L133-L145, parent: TestExecuteMain)

> *Summary: This test verifies the execution of an asynchronous main function by creating a temporary Python file containing `async def main()`. It then discovers and runs this function with a specific input ("test"), asserting that the returned output matches the expected string format.*


### test_execute_records_elapsed (method, L147-L160, parent: TestExecuteMain)

> *Summary: This test verifies the execution time of a simple script by first creating an agent file on disk. It then discovers and executes this script with an input message, asserting that the elapsed time is positive but less than five seconds.*


### test_execute_handles_exception (method, L162-L175, parent: TestExecuteMain)

> *Summary: This test verifies that the execution mechanism correctly catches and reports exceptions raised by a script. It writes a file containing code that raises a `ValueError` and asserts that the resulting execution output contains this specific error message.*


### TestExecuteUnknownKind (class, L178-L190)

> *Summary: This test verifies that the execution function correctly handles an agent with an unrecognized `kind`. It asserts that when provided a `DiscoveredAgent` of unknown type, the resulting execution object contains an error message indicating the unsupported discovery kind.*


### test_unknown_kind_errors (method, L181-L190, parent: TestExecuteUnknownKind)

> *Summary: When provided with an agent of an unknown `kind`, the execution process returns a result containing at least one error message indicating an "Unknown discovery kind." This test verifies that the system correctly handles and reports errors for unsupported agent types during execution.*

