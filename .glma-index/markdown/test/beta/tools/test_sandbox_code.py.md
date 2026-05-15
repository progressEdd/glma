# test/beta/tools/test_sandbox_code.py

2 function(s): _tool_call, _config. 4 class(es): FakeEnv, TestSandboxCodeToolConstruction, TestSandboxCodeToolExecution, TestSandboxCodeToolWithCustomEnvironment. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FakeEnv | class |  |
| _tool_call | function |  |
| _config | function |  |
| TestSandboxCodeToolConstruction | class |  |
| TestSandboxCodeToolExecution | class |  |
| TestSandboxCodeToolWithCustomEnvironment | class |  |

## Chunks

### FakeEnv (class, L16-L37)

> *Summary: Provides a mock environment implementation that simulates code execution for testing purposes. It accepts configuration like supported languages and predefined output/exit codes, returning a `CodeRunResult` based on its internal settings when the `run` method is called with input code and language.*


### __init__ (method, L19-L29, parent: FakeEnv)

> *Summary: Initializes a sandbox environment by setting default supported programming languages, an optional output string, and an exit code. It also initializes an empty list to track execution calls made within the sandbox.*


### supported_languages (method, L32-L33, parent: FakeEnv)

> *Summary: Returns a tuple containing all the `CodeLanguage` types that the sandbox environment supports. This method accesses and returns an internal list of supported languages.*


### run (method, L35-L37, parent: FakeEnv)

> *Summary: This method records the provided code and language into a list of calls. It then returns a `CodeRunResult` object containing the sandbox's current output and exit status.*


### _tool_call (function, L40-L44)

> *Summary: Constructs a `ToolCallEvent` object to execute provided source code within a specified programming language. It packages the input code and language into JSON arguments for the "run\_code" tool.*


### _config (function, L47-L51)

> *Summary: Constructs a `TestConfig` object by wrapping the provided code and language into a `ToolCall` event within a `ModelResponse`, alongside a specified final reply string. This function prepares configuration data for testing tool execution based on input code and desired completion status.*


### TestSandboxCodeToolConstruction (class, L54-L74)

> *Summary: This class tests the `SandboxCodeTool` by verifying that it requires an environment object upon instantiation, correctly preserves that environment, and can incorporate supported languages into its generated schemas. It also confirms that a custom name provided during construction is correctly assigned to the tool instance.*


### test_environment_is_required (method, L55-L57, parent: TestSandboxCodeToolConstruction)

> *Summary: Asserts that instantiating `SandboxCodeTool` without providing an environment raises a `TypeError` containing the string "environment". This verifies the tool requires an environmental context upon initialization.*


### test_environment_preserved (method, L59-L62, parent: TestSandboxCodeToolConstruction)

> *Summary: Verifies that the `SandboxCodeTool` correctly retains a reference to the provided environment object upon initialization. It asserts that the tool's internal `environment` attribute matches the input `FakeEnv` instance.*


### test_supported_languages_in_description (method, L65-L70, parent: TestSandboxCodeToolConstruction)

> *Summary: This test verifies that the generated schemas for a code execution tool include descriptions listing supported languages, specifically checking for "python" and "bash" when initialized with those languages. It achieves this by instantiating a fake environment and calling the `schemas` method on the sandbox object.*


### test_custom_name_used (method, L72-L74, parent: TestSandboxCodeToolConstruction)

> *Summary: This test verifies that a `SandboxCodeTool` instance correctly accepts and stores a custom name provided during initialization. It asserts the internal `name` attribute matches the input string `"my_runner"`.*


### TestSandboxCodeToolExecution (class, L77-L123)

> *Summary: This test suite verifies the behavior of code execution within a sandbox environment by simulating agent interactions. It checks how successful and failing code executions propagate output, ensuring exit codes are included only on failure, and confirms that the environment correctly receives calls from the executed code.*


### test_success_propagates_output (method, L79-L89, parent: TestSandboxCodeToolExecution)

> *Summary: This test verifies that successful execution of code within a sandbox tool correctly propagates its output. It initializes an environment with a known output, runs an agent to execute the code, and asserts that the expected result is captured in the stream's collected outputs.*


### test_failure_includes_exit_code (method, L92-L102, parent: TestSandboxCodeToolExecution)

> *Summary: This test verifies that when a sandboxed execution intentionally exits with a specific code, the resulting tool output captures this exit status. It simulates an environment failure and asserts that the captured result string contains the expected exit code information.*


### test_success_omits_exit_code (method, L105-L115, parent: TestSandboxCodeToolExecution)

> *Summary: This test verifies that a successful execution, indicated by an exit code of 0, does not include the exit code information in the reported tool result. It simulates running code within a controlled environment and asserts the content of the captured output stream.*


### test_environment_receives_call (method, L118-L123, parent: TestSandboxCodeToolExecution)

> *Summary: This test verifies that an agent correctly invokes a tool when prompted to run code. It sets up a fake environment and asserts that the `SandboxCodeTool` receives the expected function call arguments from the agent's execution.*


### TestSandboxCodeToolWithCustomEnvironment (class, L126-L156)

> *Summary: This test verifies that the code execution tool correctly utilizes any object conforming to the `CodeEnvironment` protocol. It instantiates a mock environment, passes it to the sandbox, and asserts that the agent's request triggers the custom environment's `run` method with the expected inputs.*


### test_arbitrary_environment_is_invoked (method, L132-L156, parent: TestSandboxCodeToolWithCustomEnvironment)

> *Summary: This test verifies that a custom environment implementation is correctly invoked by an agent when executing code. It sets up a mock environment that captures the input code and language, asserting that the agent calls its `run` method with the expected parameters and receives the mocked result.*

