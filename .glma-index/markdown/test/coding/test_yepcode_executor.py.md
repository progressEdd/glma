# test/coding/test_yepcode_executor.py

2 class(es): TestYepCodeCodeExecutor, TestYepCodeCodeResult. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestYepCodeCodeExecutor | class |  |
| TestYepCodeCodeResult | class |  |

## Chunks

### TestYepCodeCodeExecutor (class, L27-L246)

> *Summary: This test suite verifies the initialization and core functionality of a code execution service wrapper. It tests various setup scenarios, including token sourcing (API vs. environment), custom parameter handling, input validation for timeouts, and successful/failed execution of code blocks using mocked external API calls.*


### setup_method (method, L30-L34, parent: TestYepCodeCodeExecutor)

> *Summary: Before every test execution, this method clears the `YEPCODE_API_TOKEN` environment variable if it exists. This ensures a clean state for isolated testing of code execution logic.*


### test_init_with_api_token (method, L38-L50, parent: TestYepCodeCodeExecutor)

> *Summary: This test verifies that the `YepCodeCodeExecutor` initializes correctly when provided with an API token. It asserts that the internal state reflects the provided token and default settings, while also confirming that configuration and runner methods were called as expected during instantiation.*


### test_init_with_environment_token (method, L54-L63, parent: TestYepCodeCodeExecutor)

> *Summary: This test verifies that the executor correctly initializes by reading an API token from the environment variables. It asserts that the internal token matches the set environment value and confirms the configuration function was called with that token.*


### test_init_with_custom_parameters (method, L67-L82, parent: TestYepCodeCodeExecutor)

> *Summary: This test verifies that the `YepCodeCodeExecutor` correctly initializes when provided with specific configuration values. It asserts that internal attributes like API token, timeout, and execution modes match the input parameters passed during instantiation.*


### test_init_with_invalid_timeout (method, L84-L87, parent: TestYepCodeCodeExecutor)

> *Summary: Asserts that attempting to initialize the executor with a non-positive `timeout` value raises a `ValueError`. This verifies input validation for the execution timeout parameter.*


### test_init_runner_failure (method, L91-L97, parent: TestYepCodeCodeExecutor)

> *Summary: When the underlying API initialization fails during setup, this test asserts that instantiating the executor raises a `RuntimeError` with a specific failure message. It achieves this by mocking the configuration and forcing the runner to raise an exception upon initialization.*


### test_code_extractor_property (method, L101-L108, parent: TestYepCodeCodeExecutor)

> *Summary: This test verifies that the `YepCodeCodeExecutor` instance correctly initializes its `code_extractor` property to an instance of `MarkdownCodeExtractor`. It achieves this by instantiating the executor and asserting the type of the resulting attribute.*


### test_timeout_property (method, L112-L119, parent: TestYepCodeCodeExecutor)

> *Summary: Verifies that the `YepCodeCodeExecutor` correctly initializes and exposes the provided `timeout` value via its property. It instantiates the executor with a specific timeout and asserts the internal property matches the input.*


### test_normalize_language (method, L123-L136, parent: TestYepCodeCodeExecutor)

> *Summary: This test verifies the language normalization logic by asserting that various input strings (like "py", "Python", "js") are correctly mapped to their standardized lowercase forms ("python", "javascript"). It confirms the method handles case insensitivity and maps common aliases to canonical names.*


### test_execute_empty_code_blocks (method, L140-L149, parent: TestYepCodeCodeExecutor)

> *Summary: When provided with an empty list of code blocks, the execution process should complete successfully with a zero exit code and no output. This test verifies that the executor handles null input gracefully without errors.*


### test_execute_unsupported_language (method, L153-L163, parent: TestYepCodeCodeExecutor)

> *Summary: When provided with a list of `CodeBlock` objects containing an unsupported language like "java", the execution returns a result indicating failure, specifically setting the exit code to 1 and including an error message about the unsupported language in the output.*


### test_execute_successful_python_code (method, L167-L204, parent: TestYepCodeCodeExecutor)

> *Summary: Verifies that the executor successfully runs Python code by mocking a successful execution response from the runner. It asserts that the returned result contains the expected output, exit code zero, and correct execution ID after calling `execute_code_blocks`.*


### test_execute_code_with_error (method, L208-L234, parent: TestYepCodeCodeExecutor)

> *Summary: This test verifies the executor's behavior when code execution fails by simulating an error response from the runner. It asserts that the resulting output correctly reflects the non-zero exit code and contains the specific error message provided during the mock setup.*


### test_restart_method (method, L238-L246, parent: TestYepCodeCodeExecutor)

> *Summary: This test verifies that calling the `restart` method on a code executor instance executes without raising an exception, regardless of mocked configuration or runner dependencies. It initializes the executor with a test token and asserts successful execution of the restart logic.*


### TestYepCodeCodeResult (class, L250-L267)

> *Summary: This test suite verifies the instantiation and attribute setting of a code execution result object. It confirms that provided `exit_code`, `output`, and optional `execution_id` are correctly stored upon creation, handling cases where the ID might be omitted.*


### test_code_result_creation (method, L253-L259, parent: TestYepCodeCodeResult)

> *Summary: This test verifies the correct initialization of a `YepCodeCodeResult` object by asserting that its properties (`exit_code`, `output`, and `execution_id`) match the provided input values. It confirms the constructor correctly stores the execution outcome data.*


### test_code_result_without_execution_id (method, L261-L267, parent: TestYepCodeCodeResult)

> *Summary: Verifies that a `YepCodeCodeResult` object can be instantiated with an exit code and output string while correctly setting the `execution_id` to `None`. This test confirms the basic state initialization of the result object without any execution context.*

