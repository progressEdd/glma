# test/coding/test_daytona_code_executor_integration.py

2 function(s): load_env, executor. 10 class(es): TestDaytonaPythonIntegration, TestDaytonaBashIntegration, TestDaytonaJavaScriptIntegration, TestDaytonaTypeScriptIntegration, TestDaytonaMultipleBlocksIntegration, TestDaytonaResultMetadata, TestDaytonaCustomImageIntegration, TestDaytonaEnvVarsIntegration, TestDaytonaRestartIntegration, TestDaytonaContextManagerIntegration. 29 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| load_env | function |  |
| executor | function |  |
| TestDaytonaPythonIntegration | class |  |
| TestDaytonaBashIntegration | class |  |
| TestDaytonaJavaScriptIntegration | class |  |
| TestDaytonaTypeScriptIntegration | class |  |
| TestDaytonaMultipleBlocksIntegration | class |  |
| TestDaytonaResultMetadata | class |  |
| TestDaytonaCustomImageIntegration | class |  |
| TestDaytonaEnvVarsIntegration | class |  |
| TestDaytonaRestartIntegration | class |  |
| TestDaytonaContextManagerIntegration | class |  |

## Chunks

### load_env (function, L31-L35)

> *Summary: Reads the `.env` file located in the repository root directory and loads its environment variables into the process if it exists. This ensures configuration settings are available for testing purposes.*


### executor (function, L39-L44)

> *Summary: Provides a shared, sandboxed code execution environment for all integration tests in the module. It requires the `DAYTONA_API_KEY` environment variable to be set before yielding an initialized executor instance.*


### TestDaytonaPythonIntegration (class, L54-L88)

> *Summary: This test suite verifies the functionality of a code executor by running various Python snippets. It checks for correct output on successful execution (e.g., printing strings or performing math) and validates non-zero exit codes when encountering runtime errors or syntax issues, while also testing language aliases like 'py'.*


### test_basic_print (method, L55-L58, parent: TestDaytonaPythonIntegration)

> *Summary: Executes a single Python code block containing a `print` statement and asserts that the execution exits successfully (code 0) and captures the expected output string.*


### test_math_computation (method, L60-L63, parent: TestDaytonaPythonIntegration)

> *Summary: Executes a Python code block that calculates the square root of 144 using the `math` module. It asserts that the execution succeeds (exit code 0) and that the output string contains "12.0".*


### test_multiline_code (method, L65-L74, parent: TestDaytonaPythonIntegration)

> *Summary: Executes a multi-line Python code block that calculates the sum of numbers from 1 to 5 and prints it. It asserts that the execution succeeds (exit code 0) and that the output string contains "15".*


### test_runtime_error_returns_nonzero_exit (method, L76-L79, parent: TestDaytonaPythonIntegration)

> *Summary: When executing code containing a runtime error, the function asserts that the execution returns a non-zero exit code and that the output contains an indication of the `NameError` or the undefined variable name. This verifies proper error handling during code execution.*


### test_syntax_error_returns_nonzero_exit (method, L81-L83, parent: TestDaytonaPythonIntegration)

> *Summary: When provided with code containing a syntax error in Python, the execution returns an exit code that is not zero, indicating failure. This test verifies that the executor correctly signals errors during code parsing or execution.*


### test_py_alias_works (method, L85-L88, parent: TestDaytonaPythonIntegration)

> *Summary: Executes a Python code block containing `print('alias ok')` using the provided executor. It asserts that the execution succeeds (exit code 0) and that the output string contains "alias ok".*


### TestDaytonaBashIntegration (class, L98-L118)

> *Summary: This suite verifies the integration of a code execution environment by testing basic shell commands across Bash and Sh interpreters. It confirms correct output capture, successful execution status (exit code 0), and proper propagation of non-zero exit codes from scripts.*


### test_basic_echo (method, L99-L102, parent: TestDaytonaBashIntegration)

> *Summary: This test verifies basic command execution by running a simple `echo` script via the executor. It asserts that the execution returns an exit code of zero and that the expected output string is present in the results.*


### test_multiline_bash (method, L104-L109, parent: TestDaytonaBashIntegration)

> *Summary: Executes a multi-line bash script containing a loop that prints numbers 1 through 3. It asserts the execution succeeds (exit code 0) and verifies that the output string contains both "1" and "3".*


### test_sh_alias (method, L111-L114, parent: TestDaytonaBashIntegration)

> *Summary: Executes a shell script block containing `echo 'sh works'` using the provided executor. It asserts that the execution exits successfully (code 0) and that the output string contains "sh works".*


### test_bash_exit_code_propagated (method, L116-L118, parent: TestDaytonaBashIntegration)

> *Summary: When executing a bash script containing `exit 42`, this test verifies that the execution result correctly captures and propagates the exit code of 42. It asserts that the returned object's `exit_code` matches the specified value.*


### TestDaytonaJavaScriptIntegration (class, L128-L142)

> *Summary: This test suite verifies JavaScript execution capabilities by passing code blocks to an executor and asserting the resulting output and exit code. It specifically tests basic console logging, language alias support (using "js"), and arithmetic operations within the executed JavaScript code.*


### test_basic_console_log (method, L129-L132, parent: TestDaytonaJavaScriptIntegration)

> *Summary: Executes a single JavaScript code block containing `console.log` and asserts that the execution succeeds (exit code 0) and the output string contains the expected message.*


### test_js_alias (method, L134-L137, parent: TestDaytonaJavaScriptIntegration)

> *Summary: Executes a JavaScript code block containing `console.log` to verify alias functionality. It asserts that the execution exits successfully and captures the expected output string.*


### test_js_arithmetic (method, L139-L142, parent: TestDaytonaJavaScriptIntegration)

> *Summary: Executes a JavaScript code block that performs multiplication and logs the result to standard output. It asserts that the execution completes successfully (exit code 0) and that the expected value ("42") is present in the captured output.*


### TestDaytonaTypeScriptIntegration (class, L152-L169)

> *Summary: This test suite verifies the TypeScript execution capabilities of a code executor by running several snippets. It confirms successful compilation and output for basic variable declarations, type assertions, and module imports within the provided code blocks.*


### test_basic_ts (method, L153-L157, parent: TestDaytonaTypeScriptIntegration)

> *Summary: Executes a simple TypeScript code block containing a string declaration and console log. It asserts that the execution exits successfully (code 0) and that the expected string output is present in the results.*


### test_ts_alias (method, L159-L162, parent: TestDaytonaTypeScriptIntegration)

> *Summary: Executes a TypeScript code block that declares and logs a constant variable to verify correct execution. It asserts that the process exits successfully and the output contains the expected value "42".*


### test_ts_with_import_statement (method, L164-L169, parent: TestDaytonaTypeScriptIntegration)

> *Summary: Executes TypeScript code containing an `import` statement to verify that CommonJS flags correctly handle module imports. It asserts successful execution and checks if the output contains the expected joined path string.*


### TestDaytonaMultipleBlocksIntegration (class, L179-L204)

> *Summary: This test suite verifies the integration of executing multiple code blocks sequentially using an executor. It confirms that outputs from sequential blocks are joined correctly, execution halts immediately upon the first failure, and it successfully handles mixed language inputs (e.g., Python and Bash).*


### test_multiple_blocks_outputs_joined (method, L180-L187, parent: TestDaytonaMultipleBlocksIntegration)

> *Summary: Executes a list of code blocks sequentially and verifies the combined output. It asserts that the execution completes successfully (exit code 0) and that the concatenated output contains strings from all executed blocks.*


### test_multiple_blocks_stops_on_first_failure (method, L189-L195, parent: TestDaytonaMultipleBlocksIntegration)

> *Summary: This test verifies that when executing multiple code blocks, the execution halts immediately upon encountering a failure in any block. It asserts that the overall exit code is non-zero and that subsequent output from later blocks is suppressed.*


### test_mixed_languages (method, L197-L204, parent: TestDaytonaMultipleBlocksIntegration)

> *Summary: Executes a sequence of code blocks containing mixed languages (Python and Bash) via the provided executor. It asserts that the execution completes successfully and that the combined output contains expected strings from both languages.*


### TestDaytonaResultMetadata (class, L214-L233)

> *Summary: This class verifies the integration of a code execution environment by testing various behaviors of the `executor`. It asserts that executed results contain a valid sandbox ID, are of the expected type, maintain a consistent sandbox across multiple calls, and correctly handle empty input blocks.*


### test_sandbox_id_is_present (method, L215-L218, parent: TestDaytonaResultMetadata)

> *Summary: Verifies that the execution result from running a simple code block contains a non-null and non-empty `sandbox_id`. This test confirms the executor correctly assigns an ID upon code execution.*


### test_result_is_daytona_code_result (method, L220-L222, parent: TestDaytonaResultMetadata)

> *Summary: This test verifies that the execution of a provided code block returns an object specifically typed as `DaytonaCodeResult`. It achieves this by passing a simple Python code block to the executor and asserting the type of the returned value.*


### test_sandbox_reused_across_calls (method, L224-L228, parent: TestDaytonaResultMetadata)

> *Summary: Verifies that a single execution environment maintains state by asserting both calls to `executor.execute_code_blocks` share the same sandbox ID, regardless of the input code blocks. This confirms resource reuse across sequential executions within one executor instance.*


### test_empty_code_blocks_returns_success (method, L230-L233, parent: TestDaytonaResultMetadata)

> *Summary: When provided with an empty list of code blocks, the execution returns a successful state with no output. This test verifies that processing zero inputs results in a clean exit.*


### TestDaytonaCustomImageIntegration (class, L243-L276)

> *Summary: This test suite verifies the functionality of code execution within sandboxes configured using different image specifications. It tests executing simple Python code blocks when providing an image name string or a declarative `Image` object, including verifying package installation via `pip_install`.*


### test_image_string (method, L244-L251, parent: TestDaytonaCustomImageIntegration)

> *Summary: Verifies that code execution within a sandbox environment initialized from an image name string functions correctly. It runs a simple print statement and asserts the exit code is zero and the expected output is present.*


### test_image_object (method, L253-L263, parent: TestDaytonaCustomImageIntegration)

> *Summary: This test verifies that a sandbox environment initialized from a declarative `Image` object executes code correctly. It uses the executor to run a simple Python print statement and asserts that the execution succeeds with an exit code of 0 and captures the expected output string.*


### test_image_object_with_pip_install (method, L265-L276, parent: TestDaytonaCustomImageIntegration)

> *Summary: This test verifies that a declarative image configured with `pip_install` successfully makes specified packages available within the execution sandbox. It runs Python code using an executor initialized with this custom image and asserts that the package import and version check succeed.*


### TestDaytonaEnvVarsIntegration (class, L286-L295)

> *Summary: This test verifies that custom environment variables can be successfully injected into the execution sandbox. It runs a Python code block within an executor, asserting that the output correctly retrieves the provided secret value.*


### test_env_vars_available_in_sandbox (method, L287-L295, parent: TestDaytonaEnvVarsIntegration)

> *Summary: Verifies that custom environment variables provided to the executor are accessible within the sandboxed execution environment. It runs a Python script expecting the injected variable's value ("hunter2") to be present in the output if the required API key is set.*


### TestDaytonaRestartIntegration (class, L305-L312)

> *Summary: This test verifies that restarting the code execution environment creates a new, distinct sandbox instance. It initializes an executor, captures its initial sandbox ID, calls `restart()`, and asserts that the resulting sandbox has a different ID.*


### test_restart_creates_fresh_sandbox (method, L306-L312, parent: TestDaytonaRestartIntegration)

> *Summary: Verifies that calling the restart method on an executor instance results in a new, distinct sandbox being created. It checks this by asserting that the sandbox ID changes after the restart operation is performed.*


### TestDaytonaContextManagerIntegration (class, L322-L330)

> *Summary: This test verifies that the `DaytonaCodeExecutor` properly cleans up its execution environment after use. It executes a simple code block and asserts that the internal sandbox attribute is set to `None` upon exiting the context manager.*


### test_context_manager_cleans_up (method, L323-L330, parent: TestDaytonaContextManagerIntegration)

> *Summary: Verifies that the `DaytonaCodeExecutor` context manager properly cleans up its internal state after execution. It runs a simple Python code block and asserts that the internal sandbox attribute is set to `None` upon exiting the `with` block.*

