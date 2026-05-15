# test/coding/test_daytona_code_executor.py

2 function(s): mock_sandbox, executor. 10 class(es): TestDaytonaCodeExecutorInit, TestCreateSandbox, TestDaytonaCodeExecutorProperties, TestNormalizeLanguage, TestExecuteCodeBlocks, TestRestart, TestLifecycle, TestDaytonaCodeResult, TestSupportedLanguages, TestDaytonaSandboxResources. 73 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock_sandbox | function |  |
| executor | function |  |
| TestDaytonaCodeExecutorInit | class |  |
| TestCreateSandbox | class |  |
| TestDaytonaCodeExecutorProperties | class |  |
| TestNormalizeLanguage | class |  |
| TestExecuteCodeBlocks | class |  |
| TestRestart | class |  |
| TestLifecycle | class |  |
| TestDaytonaCodeResult | class |  |
| TestSupportedLanguages | class |  |
| TestDaytonaSandboxResources | class |  |

## Chunks

### mock_sandbox (function, L31-L40)

> *Summary: Creates and returns a fully configured mock object representing a Daytona execution environment. This mock pre-sets return values for process execution, file system operations, and deletion methods to simulate successful outcomes.*


### executor (function, L44-L53)

> *Summary: This function sets up a test environment by mocking several external dependencies, including the `Daytona` class and related configuration/creation functions. It yields an instance of `DaytonaCodeExecutor`, configured to use a provided mock sandbox object for its operations.*


### TestDaytonaCodeExecutorInit (class, L62-L218)

> *Summary: This test suite verifies the initialization and behavior of a code executor class, ensuring it correctly configures itself based on various input parameters like API keys, timeouts, snapshots, and resource specifications. It also validates error handling for invalid inputs (e.g., conflicting configurations or bad timeouts) and simulates failures during sandbox creation to confirm appropriate runtime exceptions are raised.*


### _make_executor (method, L63-L73, parent: TestDaytonaCodeExecutorInit)

> *Summary: This helper method constructs a `DaytonaCodeExecutor` instance by patching several external SDK components to ensure all interactions are mocked. It configures the mocked Daytona client's creation method to return the provided sandbox object, allowing for isolated testing.*


### test_default_init (method, L75-L83, parent: TestDaytonaCodeExecutorInit)

> *Summary: Verifies that the default initialization of an executor correctly sets up a sandbox using the provided mock, while assigning standard defaults for timeout (60), and setting snapshot, image, environment variables, and resources to `None` or empty. This confirms the baseline configuration when no specific settings are supplied.*


### test_init_with_api_key (method, L85-L94, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that the `DaytonaCodeExecutor` correctly initializes when provided with an API key. It asserts that the configuration class is instantiated exactly once using the supplied API key during object creation.*


### test_init_with_all_connection_params (method, L96-L105, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that the `DaytonaCodeExecutor` correctly initializes by calling `DaytonaConfig` with all provided connection parameters (`api_key`, `api_url`, and `target`). It asserts that the configuration object is instantiated exactly once using these specific inputs.*


### test_init_omits_none_connection_params (method, L107-L117, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that the `DaytonaCodeExecutor` constructor correctly omits any `None` connection parameters when initializing `DaytonaConfig`, relying instead on environment variables for those values. It asserts that `DaytonaConfig` is called without any keyword arguments.*


### test_init_with_timeout (method, L119-L121, parent: TestDaytonaCodeExecutorInit)

> *Summary: Verifies that an executor instance is correctly initialized with a specified timeout value. It calls the setup method to create the executor and then asserts that the internal `_timeout` attribute matches the provided input of 120.*


### test_init_with_snapshot (method, L123-L125, parent: TestDaytonaCodeExecutorInit)

> *Summary: Verifies that an executor instance correctly initializes and stores a specified snapshot identifier when created. It confirms the internal `_snapshot` attribute matches the provided string argument.*


### test_init_with_image_string (method, L127-L129, parent: TestDaytonaCodeExecutorInit)

> *Summary: Verifies that an executor instance correctly stores the provided image string upon initialization by asserting its internal `_image` attribute matches the input value.*


### test_init_with_name (method, L131-L133, parent: TestDaytonaCodeExecutorInit)

> *Summary: Verifies that an executor instance is correctly initialized with a specified name. It calls the executor creation method using a provided mock sandbox and asserts that the internal `_name` attribute matches the input string.*


### test_init_auto_generates_name_when_none (method, L135-L138, parent: TestDaytonaCodeExecutorInit)

> *Summary: When initialized without a name, the executor automatically generates a unique identifier starting with "ag2-" and having a specific length. This test verifies that the generated internal name adheres to this predefined format.*


### test_init_with_env_vars (method, L140-L142, parent: TestDaytonaCodeExecutorInit)

> *Summary: Verifies that the code executor correctly initializes with a provided dictionary of environment variables. It asserts that the internal `_env_vars` attribute matches the input configuration.*


### test_init_with_resources (method, L144-L147, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that an executor instance correctly stores the provided resource configuration. It initializes the executor using a mock sandbox and specific CPU, memory, and disk allocations to confirm internal state integrity.*


### test_invalid_timeout_raises (method, L149-L155, parent: TestDaytonaCodeExecutorInit)

> *Summary: Asserts that instantiating the executor with a timeout of zero raises a `ValueError` containing a specific message. This test verifies input validation for the execution timeout parameter.*


### test_snapshot_and_image_both_raises (method, L157-L163, parent: TestDaytonaCodeExecutorInit)

> *Summary: Asserts that instantiating the executor with both a `snapshot` and an `image` argument raises a `ValueError`. This test verifies the input validation logic for conflicting configuration parameters.*


### test_sandbox_creation_failure_raises_runtime_error (method, L165-L174, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that instantiating the executor raises a `RuntimeError` when the underlying Daytona service fails during sandbox creation due to an external exception. It mocks the necessary dependencies and asserts that the expected error message is raised upon initialization failure.*


### test_sandbox_creation_timeout_raises_runtime_error (method, L176-L185, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that initializing the executor raises a `RuntimeError` when the underlying sandbox creation process times out. It mocks the Daytona client to simulate a timeout error during sandbox creation and asserts the expected exception is raised upon instantiation.*


### test_sandbox_creation_rate_limit_raises_runtime_error (method, L187-L196, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that instantiating the executor raises a `RuntimeError` when the underlying service enforces a rate limit during sandbox creation. It mocks the Daytona client to simulate a "quota exceeded" error and asserts the expected exception is thrown upon initialization.*


### test_sandbox_creation_daytona_error_raises_runtime_error (method, L198-L207, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that instantiating the executor raises a `RuntimeError` when the underlying Daytona API call fails with a specific `DaytonaError`. It mocks necessary dependencies and asserts that the expected error message is raised upon sandbox creation failure.*


### test_atexit_registered (method, L209-L218, parent: TestDaytonaCodeExecutorInit)

> *Summary: This test verifies that the `DaytonaCodeExecutor` instance registers its cleanup method with `atexit`. It mocks necessary dependencies like `Daytona`, configuration, and sandbox creation to isolate the registration check.*


### TestCreateSandbox (class, L227-L350)

> *Summary: This test suite verifies the correct parameter passing logic for creating sandboxes via `DaytonaCodeExecutor`. It asserts that different input types (snapshot string, snapshot object, image string, or declarative image object) correctly trigger and populate the appropriate creation methods (`CreateSandboxFromSnapshotParams` or `CreateSandboxFromImageParams`) with expected values, while ensuring auto-stop intervals are always zero.*


### test_default_uses_snapshot_params_without_snapshot_arg (method, L228-L241, parent: TestCreateSandbox)

> *Summary: This test verifies that when initializing the executor without explicitly providing snapshot parameters, it correctly calls `CreateSandboxFromSnapshotParams` using the executor's environment variables and name. It asserts that the call uses default values for arguments like `auto_stop_interval`.*


### test_snapshot_uses_snapshot_params_with_snapshot_arg (method, L243-L257, parent: TestCreateSandbox)

> *Summary: This test verifies that the `DaytonaCodeExecutor` correctly calls `CreateSandboxFromSnapshotParams` when initialized with a snapshot argument. It asserts that the call uses the provided snapshot name and other relevant configuration parameters from the executor instance.*


### test_image_string_uses_image_params (method, L259-L275, parent: TestCreateSandbox)

> *Summary: This test verifies that the `DaytonaCodeExecutor` correctly calls `CreateSandboxFromImageParams` when initialized with an image string. It asserts that the parameters passed to this function match the executor's configuration, including the specified image and name.*


### test_image_object_uses_image_params (method, L277-L292, parent: TestCreateSandbox)

> *Summary: This test verifies that the `DaytonaCodeExecutor` correctly passes the provided image object to the sandbox creation parameters when initializing. It asserts that the input image and a zero auto-stop interval are used in the call arguments passed to `CreateSandboxFromImageParams`.*


### test_image_with_resources_passes_sdk_resources (method, L294-L310, parent: TestCreateSandbox)

> *Summary: This test verifies that when initializing a code executor with specified resources, the system correctly calls resource creation functions using those exact parameters. It asserts that the `CreateSandboxFromImageParams` receives the mocked SDK resources object during sandbox creation setup.*


### test_resources_not_forwarded_without_any_field_set (method, L312-L325, parent: TestCreateSandbox)

> *Summary: This test verifies that when no resource fields are set on a `DaytonaSandboxResources` instance, the code executor does not attempt to build or forward SDK Resources. It asserts that the resource creation method was never called and that the image parameters received `None` for resources.*


### test_auto_stop_interval_always_zero_snapshot_path (method, L327-L337, parent: TestCreateSandbox)

> *Summary: This test verifies that the `DaytonaCodeExecutor` initializes a sandbox with an `auto_stop_interval` of zero, ensuring it never automatically stops during execution. It achieves this by mocking necessary components and asserting the keyword arguments passed to the snapshot creation parameters.*


### test_auto_stop_interval_always_zero_image_path (method, L339-L350, parent: TestCreateSandbox)

> *Summary: This test verifies that when initializing the `DaytonaCodeExecutor` with a specific image, the `auto_stop_interval` parameter is correctly set to zero during sandbox creation via `CreateSandboxFromImageParams`. It mocks several dependencies to isolate and assert this configuration behavior.*


### TestDaytonaCodeExecutorProperties (class, L359-L364)

> *Summary: Verifies that the code extractor component is an instance of `MarkdownCodeExtractor` and asserts that the execution timeout property is set to 60 seconds for a given executor object.*


### test_code_extractor_is_markdown (method, L360-L361, parent: TestDaytonaCodeExecutorProperties)

> *Summary: Verifies that the code extractor component within the provided executor instance is specifically an instance of `MarkdownCodeExtractor`. This confirms the expected type for markdown parsing capabilities.*


### test_timeout_property (method, L363-L364, parent: TestDaytonaCodeExecutorProperties)

> *Summary: Verifies that the provided code execution environment is configured with a timeout of 60 seconds. This assertion checks the `timeout` attribute of the executor object passed into the test method.*


### TestNormalizeLanguage (class, L373-L396)

> *Summary: This test suite verifies the language normalization logic by asserting that various input variations (e.g., case differences, abbreviations) map to a consistent canonical form for several languages like Python, JavaScript, and TypeScript. It also confirms that unknown or already canonical inputs pass through unchanged.*


### test_python_variants (method, L374-L378, parent: TestNormalizeLanguage)

> *Summary: Verifies that the language normalization method correctly maps various case and abbreviation inputs like "py", "Python", and "PYTHON" to the standard lowercase "python". This ensures consistent handling of Python language identifiers across different casings.*


### test_javascript_variants (method, L380-L383, parent: TestNormalizeLanguage)

> *Summary: Verifies that the language normalization function correctly maps various JavaScript input strings ("javascript", "js", "JavaScript") to the standardized lowercase "javascript". This confirms robust handling of common variations for JavaScript identification.*


### test_typescript_variants (method, L385-L387, parent: TestNormalizeLanguage)

> *Summary: Verifies that the language normalization method correctly maps both `"typescript"` and its alias `"ts"` to the canonical `"typescript"` identifier. This test ensures consistent handling of TypeScript input variations within the code execution environment.*


### test_bash_variants (method, L389-L392, parent: TestNormalizeLanguage)

> *Summary: This test verifies the language normalization logic by asserting that inputs like "bash" and "shell" are mapped to their canonical form ("bash"), while "sh" remains unchanged. It confirms the expected behavior of the `_normalize_language` method for different shell identifiers.*


### test_unknown_passthrough (method, L394-L396, parent: TestNormalizeLanguage)

> *Summary: Verifies that the language normalization method correctly passes through unknown or valid languages like "java" and "rust" without modification. It asserts that the input string matches the output string for these specific cases.*


### TestExecuteCodeBlocks (class, L405-L561)

> *Summary: This test suite verifies the `execute_code_blocks` functionality by simulating various execution scenarios against a mocked sandbox environment. It confirms correct handling for empty inputs, unsupported languages, specific language implementations (Python via `code_run`, Bash/JS/TS via file execution), error propagation (timeouts, runtime errors), and sequential block processing logic.*


### test_empty_blocks_returns_success (method, L406-L410, parent: TestExecuteCodeBlocks)

> *Summary: When provided with an empty list of code blocks, the execution returns a successful result with no output and retains the sandbox ID. This test verifies that processing zero inputs does not cause errors in the executor.*


### test_unsupported_language_returns_error (method, L412-L416, parent: TestExecuteCodeBlocks)

> *Summary: When provided with code blocks specifying an unsupported language like Java, the executor returns a result indicating failure (exit code 1) and includes a specific error message about the unsupported language in its output. The execution is performed within a mocked sandbox environment.*


### test_python_uses_code_run (method, L418-L423, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that the executor correctly runs Python code blocks by mocking the sandbox execution. It asserts that the `code_run` method is called with the correct code and timeout, and confirms the returned result matches the mocked successful output.*


### test_bash_uploads_file_and_execs (method, L425-L433, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that the executor correctly uploads a provided bash code block to the sandbox filesystem and then executes it. It asserts that the file upload occurred with the correct content and extension, and that the execution command included "bash," ultimately confirming a successful exit code of zero.*


### test_javascript_uses_node (method, L435-L440, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that the code executor invokes Node.js when processing JavaScript code blocks. It asserts that the executed command string begins with "node " and ends with ".js".*


### test_typescript_uses_ts_node (method, L442-L448, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that the code executor invokes `ts-node` with specific flags when processing TypeScript code blocks. It asserts that the executed command includes `"ts-node"` and `"--transpile-only"` and ends with `.ts`.*


### test_script_file_cleaned_up_after_exec (method, L450-L453, parent: TestExecuteCodeBlocks)

> *Summary: Ensures that the execution environment cleans up temporary files after running code blocks by asserting a call to `delete_file` on the mock sandbox filesystem. It simulates successful execution of a simple bash command within the executor.*


### test_script_cleanup_failure_does_not_propagate (method, L455-L460, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that a failure during the script's cleanup phase does not prevent the overall execution result from being reported as successful. It simulates a file deletion error within the sandbox while ensuring the main code execution returns an exit code of zero.*


### test_nonzero_exit_code_returns_early (method, L462-L466, parent: TestExecuteCodeBlocks)

> *Summary: When the executed code returns a non-zero exit code, this test verifies that the executor correctly captures both the specific exit code and any associated output from the sandboxed process. It asserts that the returned result object reflects these failure indicators.*


### test_daytona_error_during_exec_returns_error (method, L468-L472, parent: TestExecuteCodeBlocks)

> *Summary: When the execution environment throws a `DaytonaError` during code processing, this test verifies that the executor correctly captures it, resulting in an exit code of 1 and including the error message in the output.*


### test_timeout_error_during_exec_returns_error (method, L474-L478, parent: TestExecuteCodeBlocks)

> *Summary: When the execution environment raises a `DaytonaTimeoutError`, this test verifies that the executor correctly captures it, resulting in an exit code of 1 and including "timed out" in the output. It simulates a timeout during code block execution to confirm proper error handling.*


### test_rate_limit_error_during_exec_returns_error (method, L480-L484, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that when the execution sandbox throws a `DaytonaRateLimitError`, the code executor correctly returns an error state with exit code 1 and includes "rate limit" in its output. It simulates a rate-limiting failure during code block execution to confirm proper error handling.*


### test_unexpected_error_during_exec_returns_error (method, L486-L490, parent: TestExecuteCodeBlocks)

> *Summary: When the execution environment throws a `RuntimeError` during code processing, this test verifies that the executor correctly captures it, resulting in an exit code of 1 and including the error message in the output.*


### test_multiple_blocks_all_success_joins_output (method, L492-L502, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that when multiple code blocks execute successfully, the executor correctly aggregates their standard output. It simulates two successful runs and asserts the final combined output matches the expected concatenated strings.*


### test_multiple_blocks_stops_on_first_failure (method, L504-L515, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that when executing a list of code blocks, the execution halts immediately upon encountering the first failure. It asserts that the executor returns the error details from the initial failing block and only calls the underlying code runner once.*


### test_sandbox_id_included_in_result (method, L517-L520, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that the execution result object contains a specific sandbox ID when running code blocks. It mocks the sandbox to return success and asserts the resulting object's `sandbox_id` matches `"test-sandbox-id"`.*


### test_language_alias_resolved (method, L522-L526, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that a language alias like `"py"` is correctly resolved to the Python execution handler when processing code blocks. It asserts that `executor.execute_code_blocks` calls the underlying `code_run` method exactly once with the provided code.*


### test_sh_command_used_for_sh_language (method, L528-L534, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that when executing shell code, the executor invokes a command starting with `sh` but not `bash`, and ensures the command string ends with `.sh`. It achieves this by mocking the sandbox's process execution to confirm the correct invocation pattern for an "sh" language block.*


### test_timeout_forwarded_to_code_run (method, L536-L546, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that a specified timeout is correctly passed when executing code blocks within the Daytona executor. It mocks dependencies to ensure `code_run` is called exactly once with the provided code and the configured timeout value.*


### test_timeout_forwarded_to_exec (method, L548-L561, parent: TestExecuteCodeBlocks)

> *Summary: This test verifies that the specified timeout value is correctly passed to the execution process when running code blocks. It mocks the necessary executor and sandbox components, then asserts that the `timeout` argument in the `exec` call matches the input configuration.*


### TestRestart (class, L570-L585)

> *Summary: This test suite verifies the `restart` functionality by ensuring that an old sandbox is deleted and a new one is created upon execution. It also confirms that the restart process continues to create a new sandbox even if the deletion of the existing sandbox fails.*


### test_restart_deletes_old_sandbox_and_creates_new (method, L571-L578, parent: TestRestart)

> *Summary: When `restart()` is called, this test verifies that the existing sandbox is deleted and a new one is created via the executor's internal method. It asserts that both the deletion of the old sandbox and the creation of the new sandbox occurred exactly once.*


### test_restart_continues_if_delete_fails (method, L580-L585, parent: TestRestart)

> *Summary: When the sandbox deletion fails during a restart attempt, this test verifies that the execution continues by successfully creating and assigning a new sandbox instance to the executor. It confirms that the `restart()` method does not raise an exception under these failure conditions.*


### TestLifecycle (class, L594-L650)

> *Summary: These tests verify the lifecycle management of a code executor, ensuring that calling `delete()` correctly interacts with a sandbox object, handles idempotency and exceptions gracefully, and properly unregisters cleanup functions from `atexit`. They also confirm correct behavior when used as a context manager, guaranteeing `delete()` is called upon exit, even if an exception occurs.*


### test_delete_calls_sandbox_delete (method, L595-L597, parent: TestLifecycle)

> *Summary: This test verifies that calling the `delete` method on the executor triggers a corresponding call to the sandbox's `delete` function. It asserts that the sandbox's delete method was invoked exactly once after the execution.*


### test_delete_sets_sandbox_to_none (method, L599-L601, parent: TestLifecycle)

> *Summary: When the delete method is called on the executor, it should set the internal sandbox reference to `None`. This verifies that the cleanup process correctly nullifies the sandboxed environment.*


### test_delete_is_idempotent (method, L603-L606, parent: TestLifecycle)

> *Summary: Verifies that calling the delete operation multiple times has the same effect as calling it once, ensuring idempotency. It asserts that the underlying sandbox's delete method is invoked exactly one time across both calls.*


### test_delete_swallows_sandbox_exception (method, L608-L610, parent: TestLifecycle)

> *Summary: This test verifies that the code executor gracefully handles an exception thrown by the sandbox's delete operation. It asserts that calling `executor.delete()` does not result in an unhandled error when the mock sandbox simulates a deletion failure.*


### test_delete_unregisters_atexit (method, L612-L615, parent: TestLifecycle)

> *Summary: This test verifies that the `delete` method correctly unregisters itself from Python's `atexit` handlers. It asserts that `atexit.unregister` is called exactly once with a reference to the executor's delete function.*


### test_delete_unregisters_atexit_on_context_manager_exit (method, L617-L628, parent: TestLifecycle)

> *Summary: This test verifies that the `atexit` mechanism correctly unregisters a cleanup function when exiting a context manager. It asserts that the `atexit.unregister` mock is called with the executor's delete method upon leaving the `DaytonaCodeExecutor` block.*


### test_context_manager_enter_returns_executor (method, L630-L632, parent: TestLifecycle)

> *Summary: This test verifies that entering the context manager returns a reference to the original executor object. It asserts that the value returned by `__enter__()` is identical to the input `executor`.*


### test_context_manager_exit_calls_delete (method, L634-L637, parent: TestLifecycle)

> *Summary: This test verifies that the `delete` method is called exactly once when an object's exit protocol (`__exit__`) is invoked within a context manager. It mocks the `executor.delete` method to assert this specific call behavior.*


### test_context_manager_exit_called_on_exception (method, L639-L650, parent: TestLifecycle)

> *Summary: This test verifies that the cleanup method of a context manager is executed when an exception occurs during execution. It simulates running `DaytonaCodeExecutor` within a `pytest.raises(ValueError)` block and asserts that the sandbox's delete method was called afterward.*


### TestDaytonaCodeResult (class, L659-L674)

> *Summary: This class provides unit tests for `DaytonaCodeResult`, verifying that it correctly stores and exposes execution details like exit code, standard output, and an optional sandbox ID. It also confirms the result inherits from a base `CodeResult` type.*


### test_creation_with_sandbox_id (method, L660-L664, parent: TestDaytonaCodeResult)

> *Summary: This test verifies that a `DaytonaCodeResult` object correctly stores and exposes its exit code, output string, and associated sandbox ID upon creation. It asserts these values match the expected inputs provided during instantiation.*


### test_sandbox_id_defaults_to_none (method, L666-L668, parent: TestDaytonaCodeResult)

> *Summary: Verifies that a `DaytonaCodeResult` object initializes its `sandbox_id` attribute to `None`, even when provided with an exit code and output string. This confirms the default state of the sandbox identifier upon instantiation.*


### test_inherits_from_code_result (method, L670-L674, parent: TestDaytonaCodeResult)

> *Summary: Verifies that an instance of `DaytonaCodeResult` correctly inherits from the base `CodeResult` class by asserting its type. It initializes a result object with a zero exit code and empty output for this check.*


### TestSupportedLanguages (class, L683-L689)

> *Summary: Verifies that the executor's predefined set of supported languages matches an expected list and ensures all language identifiers are lowercase strings. This test confirms the integrity and formatting of the hardcoded language configuration.*


### test_supported_languages_constant (method, L684-L685, parent: TestSupportedLanguages)

> *Summary: Verifies that the `SUPPORTED_LANGUAGES` constant within the executor class contains exactly the expected set of languages: Python, Bash, Sh, JavaScript, and TypeScript. This acts as a configuration check for supported execution environments.*


### test_supported_languages_are_all_lowercase (method, L687-L689, parent: TestSupportedLanguages)

> *Summary: Verifies that every language listed in the executor's supported languages set is entirely lowercase. It iterates through `DaytonaCodeExecutor.SUPPORTED_LANGUAGES` and asserts each entry equals its lowercase version.*


### TestDaytonaSandboxResources (class, L693-L710)

> *Summary: This class tests the `DaytonaSandboxResources` object's initialization behavior. It verifies that fields default to `None`, can be explicitly set with values, and correctly handle partial initialization where only some resource attributes are provided.*


### test_all_fields_default_to_none (method, L694-L698, parent: TestDaytonaSandboxResources)

> *Summary: Verifies that when initialized without arguments, the `DaytonaSandboxResources` object sets its CPU, memory, and disk attributes to `None`. This confirms the default state of resource fields upon instantiation.*


### test_fields_can_be_set (method, L700-L704, parent: TestDaytonaSandboxResources)

> *Summary: Verifies that an instance of `DaytonaSandboxResources` correctly initializes and allows setting its resource attributes (CPU, memory, and disk) upon creation with specified values. It asserts the internal state matches the provided input configuration.*


### test_partial_fields (method, L706-L710, parent: TestDaytonaSandboxResources)

> *Summary: This test verifies that when only memory is specified during resource initialization, the resulting object correctly sets the memory value while leaving CPU and disk attributes as `None`. It confirms partial configuration handling for sandbox resources.*

