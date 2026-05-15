# test/beta/extensions/docker/test_docker_environment.py

4 function(s): _exec_result, _fake_container, _fake_client, _patch_docker. 4 class(es): TestConstruction, TestRun, TestLifecycle, TestVariableResolution. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _exec_result | function |  |
| _fake_container | function |  |
| _fake_client | function |  |
| _patch_docker | function |  |
| TestConstruction | class |  |
| TestRun | class |  |
| TestLifecycle | class |  |
| TestVariableResolution | class |  |

## Chunks

### _exec_result (function, L15-L16)

> *Summary: Creates a structured result object containing byte output and an integer exit code. It serves as a standardized return value for execution tests.*


### _fake_container (function, L19-L25)

> *Summary: Creates a mock container object populated with mocked methods for execution, stopping, and removal. It accepts an optional execution result and a default container ID to configure its behavior.*


### _fake_client (function, L28-L32)

> *Summary: Creates a mock Docker client object that simulates running a specific container and allows for closing the connection. It accepts a `container` object as input and returns a namespace containing mocked methods for interaction.*


### _patch_docker (function, L35-L39)

> *Summary: This function applies a mock patch to the `from_env` method within the Docker environment module. It replaces the real implementation with a fake client instance derived from the provided container object.*


### TestConstruction (class, L42-L65)

> *Summary: This test suite verifies the initialization logic of a `DockerCodeEnvironment` object. It confirms that invalid timeouts raise errors, validates default and custom language settings, ensures no Docker container is created upon instantiation, and checks for safe default configurations like network mode and memory limits.*


### test_invalid_timeout_rejected (method, L43-L45, parent: TestConstruction)

> *Summary: Asserts that attempting to initialize a `DockerCodeEnvironment` with a zero timeout raises a `ValueError` containing the string "timeout". This verifies input validation for the environment's timeout setting.*


### test_supported_languages_default (method, L47-L49, parent: TestConstruction)

> *Summary: Verifies that a default `DockerCodeEnvironment` instance correctly reports support for Python and Bash languages. It asserts the expected tuple of supported languages is returned by the environment object.*


### test_supported_languages_custom (method, L51-L53, parent: TestConstruction)

> *Summary: Verifies that a custom `DockerCodeEnvironment` correctly initializes and exposes the specified set of supported languages, in this case, Python and JavaScript. It asserts that the environment's internal list matches the input tuple provided during instantiation.*


### test_construction_creates_no_container (method, L55-L59, parent: TestConstruction)

> *Summary: Verifies that the `DockerCodeEnvironment` constructor does not immediately create a container by mocking the environment retrieval function and asserting it was never called during initialization. This confirms the design pattern of lazy container instantiation.*


### test_safety_defaults (method, L61-L65, parent: TestConstruction)

> *Summary: Verifies that a newly initialized `DockerCodeEnvironment` adheres to predefined safety defaults, specifically checking for network isolation, memory limits, and automatic removal settings. It asserts the environment's internal state matches expected safe configurations.*


### TestRun (class, L69-L140)

> *Summary: These tests verify the `DockerCodeEnvironment`'s behavior when executing code in different languages by interacting with a mocked Docker environment. They confirm correct command construction for Python and Bash, handle JavaScript execution via temporary files, enforce language enablement checks, ensure container reuse across multiple runs, and validate that configuration arguments are passed correctly during container creation.*


### test_python_uses_python_dash_c (method, L70-L80, parent: TestRun)

> *Summary: This test verifies that the environment correctly executes Python code by invoking `python -c` with the provided script. It asserts that the execution returns a zero exit code and contains the expected output, while also validating the arguments passed to the container's execution command.*


### test_bash_uses_bash_dash_c (method, L82-L90, parent: TestRun)

> *Summary: This test verifies that when running a command in a Docker environment, the execution is correctly invoked using `bash -c`. It sets up a mocked container and asserts that the underlying execution call uses the expected shell invocation format.*


### test_javascript_uses_node_via_tempfile (method, L92-L101, parent: TestRun)

> *Summary: This test verifies that the environment correctly executes JavaScript code by invoking Node.js within a mocked Docker container. It asserts that the executed command string passed to the container's execution method starts with `["sh", "-c"]` and contains `"node "`.*


### test_disabled_language_returns_error_without_creating_container (method, L103-L109, parent: TestRun)

> *Summary: When running a command with an environment configured for only specific languages, the execution fails immediately if the requested language is disabled, and no container is provisioned. The function asserts that the returned result has a non-zero exit code and contains a message indicating the language is not enabled.*


### test_container_created_only_once (method, L111-L124, parent: TestRun)

> *Summary: This test verifies that a Docker environment only creates a single container instance across multiple execution calls. It achieves this by mocking the underlying Docker client and asserting that the `containers.run` method is called exactly once during three sequential runs.*


### test_run_passes_safety_kwargs (method, L126-L140, parent: TestRun)

> *Summary: This test verifies that the `DockerCodeEnvironment` correctly passes safety-related configuration arguments when executing code within a container. It asserts that the underlying client's run method receives the specified image, network mode, and memory limits as expected.*


### TestLifecycle (class, L144-L179)

> *Summary: These tests verify the proper lifecycle management of a `DockerCodeEnvironment` instance, ensuring that calling `aclose()` correctly stops the associated Docker container and closes the client connection. They specifically test cleanup behavior when running code, when no code is run, and when `aclose()` is called multiple times idempotently.*


### test_aclose_stops_container_and_closes_client (method, L145-L157, parent: TestLifecycle)

> *Summary: This test verifies that calling `aclose()` on a Docker environment correctly stops the associated container and closes the client connection. It simulates running code within the environment to ensure cleanup methods are invoked upon closing.*


### test_aclose_idempotent (method, L159-L167, parent: TestLifecycle)

> *Summary: This test verifies that calling the `aclose` method twice on a Docker environment has no adverse effects, ensuring idempotency. It runs a simple command within a mocked container and then calls `aclose()` sequentially before asserting the container's stop method was called exactly once.*


### test_aclose_without_run_is_safe (method, L169-L171, parent: TestLifecycle)

> *Summary: Verifies that calling the close method on a `DockerCodeEnvironment` instance, when no container has been started, executes without raising an exception. This confirms safe resource cleanup even in uninitialized states.*


### test_async_context_manager_cleans_up (method, L173-L179, parent: TestLifecycle)

> *Summary: This test verifies that the `DockerCodeEnvironment` correctly cleans up resources after use. It runs a simple command within a mocked Docker environment and asserts that the container's stop method was called exactly once upon exiting the context manager.*


### TestVariableResolution (class, L183-L206)

> *Summary: This test suite verifies how environment variables are resolved when configuring a Docker execution environment. It asserts that an image specified via a variable is correctly substituted from the provided context, and it confirms that attempting to use an undefined variable raises a `KeyError`.*


### test_image_resolved_from_context (method, L186-L199, parent: TestVariableResolution)

> *Summary: This test verifies that a Docker environment correctly resolves an image name from a provided context variable during execution. It asserts that the `client.containers.run` method is called with the specific image string defined in the mock context.*


### test_missing_variable_raises_key_error (method, L201-L206, parent: TestVariableResolution)

> *Summary: When provided with a `Context` lacking specific variables and an environment configured to require one, the execution will raise a `KeyError` matching the missing variable name. This test verifies that the Docker environment correctly fails when necessary configuration is absent during runtime.*

