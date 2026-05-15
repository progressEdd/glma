# test/beta/extensions/daytona/test_daytona_environment.py

3 function(s): _fake_sandbox, _fake_client, _patch_async_daytona. 5 class(es): TestConstruction, TestRun, TestLifecycle, TestResources, TestVariableResolution. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _fake_sandbox | function |  |
| _fake_client | function |  |
| _patch_async_daytona | function |  |
| TestConstruction | class |  |
| TestRun | class |  |
| TestLifecycle | class |  |
| TestResources | class |  |
| TestVariableResolution | class |  |

## Chunks

### _fake_sandbox (function, L16-L30)

> *Summary: Creates a mock object simulating a Daytona sandbox environment. It accepts optional parameters for the execution result, exit code, and sandbox ID to configure its mocked methods like `code_run`, `exec`, file operations, and deletion.*


### _fake_client (function, L33-L37)

> *Summary: Creates a mock client object containing asynchronous `create` and `close` methods. The `create` method is configured to return the provided sandbox object upon invocation.*


### _patch_async_daytona (function, L40-L45)

> *Summary: This function patches the `AsyncDaytona` class to ensure that any returned client's `.create()` method yields a specific sandbox object provided as input. It returns a patch object configured for this mock behavior.*


### TestConstruction (class, L48-L69)

> *Summary: This test suite verifies the initialization logic of `DaytonaCodeEnvironment`, ensuring that mutually exclusive parameters like `snapshot` and `image` raise errors, invalid timeouts are rejected, default or custom supported languages are correctly set, and no sandbox is instantiated during construction.*


### test_snapshot_and_image_mutually_exclusive (method, L49-L51, parent: TestConstruction)

> *Summary: Asserts that attempting to initialize a `DaytonaCodeEnvironment` with both a `snapshot` and an `image` argument raises a `ValueError`. This confirms the mutual exclusivity constraint between these two configuration parameters.*


### test_invalid_timeout_rejected (method, L53-L55, parent: TestConstruction)

> *Summary: Asserts that initializing the `DaytonaCodeEnvironment` with a zero timeout raises a `ValueError` containing "timeout". This verifies input validation for the environment's timeout setting.*


### test_supported_languages_default (method, L57-L59, parent: TestConstruction)

> *Summary: Verifies that a newly instantiated `DaytonaCodeEnvironment` correctly exposes the default set of supported languages, which should include Python, Bash, JavaScript, and TypeScript.*


### test_supported_languages_custom (method, L61-L63, parent: TestConstruction)

> *Summary: Verifies that a custom environment initialized with specific languages correctly reports those supported languages. It takes a tuple of language strings as input and asserts the resulting `supported_languages` attribute matches exactly.*


### test_construction_creates_no_sandbox (method, L65-L69, parent: TestConstruction)

> *Summary: Verifies that the `DaytonaCodeEnvironment` constructor does not immediately instantiate or call the underlying asynchronous client when initialized with a test API key. This confirms the sandbox initialization is lazy, adhering to design constraints.*


### TestRun (class, L73-L148)

> *Summary: These tests verify the functionality of a code execution environment by simulating various scenarios. They confirm correct behavior for different languages (Python, Bash, JavaScript), error handling for disabled or timed-out languages, and ensure resource management like single sandbox creation across multiple runs.*


### test_python_uses_code_run (method, L74-L82, parent: TestRun)

> *Summary: This test verifies that the environment correctly executes provided code using a mocked sandbox. It asserts that running `"print(40+2)"` with Python results in an exit code of 0 and captures the expected output, while also confirming the underlying `code_run` method was called once.*


### test_bash_uploads_and_execs (method, L84-L95, parent: TestRun)

> *Summary: This test verifies that executing a bash command within the Daytona environment correctly uploads and executes files in a mocked sandbox. It asserts that the execution succeeds with exit code 0, contains expected output, and that file upload, process execution, and cleanup operations were all called exactly once on the sandbox mocks.*


### test_javascript_uses_node (method, L97-L105, parent: TestRun)

> *Summary: This test verifies that when running JavaScript code within a Daytona environment, the underlying execution process invokes Node.js. It achieves this by setting up a mocked sandbox and asserting that the command arguments passed to the process executor begin with "node ".*


### test_disabled_language_returns_error_without_creating_sandbox (method, L107-L113, parent: TestRun)

> *Summary: When running code with a disabled language configured, the environment should return an error indicating the language is not enabled without attempting to create a sandbox. This test verifies that executing a command using a disallowed language results in a non-zero exit code and an output message containing "not enabled".*


### test_sandbox_created_only_once (method, L115-L128, parent: TestRun)

> *Summary: This test verifies that the underlying sandboxing mechanism is initialized only once across multiple execution calls. It simulates running three separate code snippets within a controlled environment and asserts that the `create` method on the mock client was called exactly one time.*


### test_timeout_returns_124 (method, L130-L138, parent: TestRun)

> *Summary: This test verifies that when the underlying process times out, the environment correctly returns an exit code of 124 and includes a "timed out" message in its output. It achieves this by mocking the sandbox's execution to raise a `DaytonaTimeoutError`.*


### test_rate_limit_surfaces_as_error_string (method, L140-L148, parent: TestRun)

> *Summary: This test verifies that when the underlying Daytona API simulates a rate limit error, the execution environment correctly captures it as an error string within the output. It achieves this by mocking the sandbox's code run to raise a `DaytonaRateLimitError` and asserting the resulting exit code is non-zero while containing "rate limit".*


### TestLifecycle (class, L152-L188)

> *Summary: These tests verify the cleanup behavior of a code execution environment, ensuring that calling `aclose()` correctly deletes the associated sandbox and closes the client connection after running code or when used as an asynchronous context manager. They also confirm that closing is idempotent and safe even if no sandbox was initialized.*


### test_aclose_deletes_sandbox_and_closes_client (method, L153-L165, parent: TestLifecycle)

> *Summary: This test verifies that calling `aclose()` on a Daytona environment correctly triggers the deletion of its associated sandbox and closes the client connection. It mocks the environment setup to assert these cleanup methods are called exactly once after execution.*


### test_aclose_idempotent (method, L167-L175, parent: TestLifecycle)

> *Summary: This test verifies that calling the `aclose` method twice on a Daytona environment has no adverse effects, ensuring idempotency. It runs a simple code execution within a mocked sandbox and asserts that the underlying sandbox deletion is called exactly once across both calls to `aclose`.*


### test_aclose_without_run_is_safe (method, L177-L180, parent: TestLifecycle)

> *Summary: This test verifies that calling the `aclose` method on a newly initialized environment, without ever running any code or creating a sandbox, executes safely without raising an exception. It confirms proper cleanup behavior even in a minimal setup.*


### test_async_context_manager_cleans_up (method, L182-L188, parent: TestLifecycle)

> *Summary: This test verifies that the asynchronous context manager correctly cleans up resources after execution. It runs a simple code snippet within a patched environment and asserts that the sandbox's delete method was called exactly once upon exiting the context.*


### TestResources (class, L191-L202)

> *Summary: Verifies the `DaytonaResources` dataclass by testing instantiation with explicit values to confirm correct attribute assignment, and also tests default initialization where all resource attributes are expected to be `None`.*


### test_resources_dataclass (method, L192-L196, parent: TestResources)

> *Summary: Verifies that the `DaytonaResources` dataclass correctly initializes and stores provided resource values (CPU, memory, disk). It asserts that the instantiated object's attributes match the input parameters.*


### test_resources_all_optional (method, L198-L202, parent: TestResources)

> *Summary: Verifies that the `DaytonaResources` object initializes with all resource attributes (`cpu`, `memory`, `disk`) set to `None`. This confirms the default optional nature of these resource configurations upon instantiation.*


### TestVariableResolution (class, L206-L231)

> *Summary: This test suite verifies how variable parameters are resolved within a Daytona environment. It confirms that an image specified as a `Variable` correctly pulls its value from the provided execution context, and it also asserts that attempting to resolve a missing variable raises a `KeyError`.*


### test_image_resolved_from_context (method, L213-L223, parent: TestVariableResolution)

> *Summary: This test verifies that an environment correctly resolves a container image specified in the execution context. It runs code within a mocked Daytona environment, asserting that the `create` method is called with the image value derived from the provided context variables.*


### test_missing_variable_raises_key_error (method, L225-L231, parent: TestVariableResolution)

> *Summary: When initialized with an empty variable set, attempting to run code that references a missing variable like `tenant_image` will raise a `KeyError`. This test verifies the environment correctly fails when required configuration variables are absent during execution.*

