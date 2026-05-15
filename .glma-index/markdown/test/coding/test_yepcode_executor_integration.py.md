# test/coding/test_yepcode_executor_integration.py

1 class(es): TestYepCodeCodeExecutorIntegration. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestYepCodeCodeExecutorIntegration | class |  |

## Chunks

### TestYepCodeCodeExecutorIntegration (class, L30-L135)

> *Summary: This test suite verifies the integration of `YepCodeCodeExecutor` by executing code blocks for Python and JavaScript against a live API. It validates successful execution (checking exit codes and expected output) and tests error handling by submitting invalid code to confirm failure detection.*


### setup_method (method, L33-L42, parent: TestYepCodeCodeExecutorIntegration)

> *Summary: Before each test, this method loads environment variables from a local `.env` file if it exists. It then verifies the presence of the `YEPCODE_API_TOKEN`, skipping the test if the token is missing.*


### test_basic_python_execution (method, L44-L77, parent: TestYepCodeCodeExecutorIntegration)

> *Summary: This test verifies the functionality of a code executor by running a Python script that prints system information and performs a mathematical calculation. It asserts that the execution completes successfully (exit code 0) and that the expected output strings are present in the returned results.*


### test_javascript_execution (method, L79-L111, parent: TestYepCodeCodeExecutorIntegration)

> *Summary: This test verifies the functionality of a code executor by running JavaScript code that uses an external npm package (`moment`). It asserts that the execution completes successfully (exit code 0) and that the output contains expected logging messages and return data.*


### test_error_handling (method, L113-L135, parent: TestYepCodeCodeExecutorIntegration)

> *Summary: This test verifies that the code executor correctly handles invalid Python code by asserting an exit code of 1 and checking for a "NameError" within the execution output when provided with a block containing undefined variable access.*

