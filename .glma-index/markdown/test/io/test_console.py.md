# test/io/test_console.py

1 class(es): TestConsoleIO. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestConsoleIO | class |  |

## Chunks

### TestConsoleIO (class, L15-L52)

> *Summary: This test suite verifies the input/output functionality of an `IOConsole` instance by mocking system calls like `event_print`, `input`, and `getpass`. It confirms that methods like `print()` route through event logging, `send()` triggers printing, and both standard and password-protected `input()` correctly interact with mocked I/O streams.*


### setup_method (method, L16-L17, parent: TestConsoleIO)

> *Summary: Initializes an `IOConsole` instance and assigns it to the test object's `console_io` attribute before each test execution. This prepares a mock or real console interface for subsequent testing operations.*


### test_print (method, L20-L23, parent: TestConsoleIO)

> *Summary: This test verifies that calling `console_io.print()` correctly routes the output through a mocked event logger. It asserts that the mock was called exactly once with the provided string and specific formatting arguments.*


### test_send (method, L26-L30, parent: TestConsoleIO)

> *Summary: This test verifies that sending a `PrintEvent` message to the console I/O correctly invokes the underlying print mechanism with specific formatting arguments. It asserts that the mock print function was called exactly once using the provided event parameters, but with `flush=True`.*


### test_input (method, L33-L39, parent: TestConsoleIO)

> *Summary: This test verifies that the `input` method correctly utilizes a mocked built-in input function. It sets the mock's return value and asserts that calling the system's input retrieves this predefined string, while also confirming the correct prompt was passed to the mock.*


### test_input_password (method, L42-L52, parent: TestConsoleIO)

> *Summary: This test verifies that the `input` method correctly handles password prompts by mocking `getpass.getpass`. It asserts that the returned value matches the mocked input and checks if the underlying function was called with the expected prompt string.*

