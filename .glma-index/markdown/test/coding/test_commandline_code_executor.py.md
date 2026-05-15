# test/coding/test_commandline_code_executor.py

25 function(s): test_execution_policy_enforcement, test_is_code_executor, test_create_local, test_create_docker, test_container_create_kwargs_forwarding, test_commandline_executor_init, test_commandline_executor_execute_code, _test_execute_code, test_local_commandline_code_executor_save_files, test_local_commandline_code_executor_save_files_only and 15 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_execution_policy_enforcement | function |  |
| test_is_code_executor | function |  |
| test_create_local | function |  |
| test_create_docker | function |  |
| test_container_create_kwargs_forwarding | function |  |
| test_commandline_executor_init | function |  |
| test_commandline_executor_execute_code | function |  |
| _test_execute_code | function |  |
| test_local_commandline_code_executor_save_files | function |  |
| test_local_commandline_code_executor_save_files_only | function |  |
| _test_save_files | function |  |
| test_commandline_code_executor_timeout | function |  |
| _test_timeout | function |  |
| test_local_commandline_code_executor_restart | function |  |
| test_docker_commandline_code_executor_restart | function |  |
| test_policy_override | function |  |
| _test_restart | function |  |
| test_commandline_executor_conversable_agent_code_execution | function |  |
| _test_conversable_agent_code_execution | function |  |
| test_dangerous_commands | function |  |
| test_invalid_relative_path | function |  |
| test_valid_relative_path | function |  |
| test_silent_pip_install | function |  |
| test_local_executor_with_custom_python_env | function |  |
| test_local_executor_with_custom_python_env_in_local_relative_path | function |  |

## Chunks

### test_execution_policy_enforcement (function, L48-L64)

> *Summary: This test verifies that the executor respects defined execution policies by running a provided code block in a temporary directory. It asserts whether the output contains expected text based on the `should_execute` flag, while also confirming that the source code is always saved to a file.*


### test_is_code_executor (function, L68-L69)

> *Summary: Verifies that the class instance being tested is indeed an instance of `CodeExecutor`. This acts as a basic type check to ensure correct inheritance or implementation.*


### test_create_local (function, L72-L79)

> *Summary: This test verifies the `CodeExecutorFactory`'s ability to instantiate a specific local command-line executor based on configuration dictionaries, ensuring both correct type instantiation and direct object reference when provided explicitly.*


### test_create_docker (function, L87-L90)

> *Summary: This test verifies that the `CodeExecutorFactory` correctly instantiates and returns a specific `DockerCommandLineCodeExecutor` instance when provided with its configuration. It asserts that the returned object is indeed the expected executor object.*


### test_container_create_kwargs_forwarding (function, L95-L103)

> *Summary: This test verifies that environment variables passed to the executor are correctly forwarded to the underlying Docker container creation process. It executes a shell command within a container configured with specific environment variables and asserts that the output reflects those values.*


### test_commandline_executor_init (function, L107-L113)

> *Summary: Verifies the initialization of a command-line executor by asserting correct default and provided timeout and working directory settings. It also confirms that attempting to initialize with an invalid working directory raises a `FileNotFoundError`.*


### test_commandline_executor_execute_code (function, L118-L121)

> *Summary: This test function sets up a temporary directory and initializes an executor instance within it. It then calls another testing utility to execute code using the provided Python variant against this executor.*


### _test_execute_code (function, L125-L165)

> *Summary: This function verifies the `CodeExecutor`'s functionality by executing various sets of code blocks—including single/multiple Python snippets and a Bash script—and asserts that the execution returns an exit code of zero, contains expected output, and correctly saves the source code to a file. It confirms the integrity of the saved file content against the input lines.*


### test_local_commandline_code_executor_save_files (function, L169-L172)

> *Summary: This test sets up a temporary directory and initializes an executor within it to verify file saving functionality. It then calls a helper function to execute tests that involve writing files using the initialized executor.*


### test_local_commandline_code_executor_save_files_only (function, L176-L183)

> *Summary: This test verifies that the code executor saves files without executing any language-specific code. It initializes an executor within a temporary directory, explicitly disabling execution policies for common languages before calling a helper function to perform file saving operations.*


### _test_save_files (function, L186-L247)

> *Summary: This function verifies the `CodeExecutor`'s ability to save code blocks to files based on language conventions, accepting a list of `CodeBlock` inputs and returning assertions against the execution results. It tests various scenarios including explicit filename directives and implicit naming for Python, JavaScript, CSS, and HTML.*


### test_commandline_code_executor_timeout (function, L251-L254)

> *Summary: This test verifies that the code executor correctly times out when processing a task. It initializes an executor with a one-second timeout within a temporary directory and then calls a helper function to assert the timeout behavior.*


### _test_timeout (function, L257-L260)

> *Summary: This function tests the timeout mechanism of a code executor by running a Python script designed to sleep for ten seconds. It asserts that the execution result indicates a timeout occurred.*


### test_local_commandline_code_executor_restart (function, L263-L265)

> *Summary: This test verifies the restart functionality of a local command-line code executor by initializing an instance and calling a helper function to execute the restart logic. It confirms that the executor behaves correctly when restarted.*


### test_docker_commandline_code_executor_restart (function, L274-L280)

> *Summary: This test verifies that the code execution environment can successfully run commands both before and after being restarted. It initializes an executor, runs a shell command to print `$HOME`, calls `restart()`, and then runs the same command again to confirm state persistence or successful reinitialization.*


### test_policy_override (function, L288-L306)

> *Summary: Verifies that a custom execution policy correctly overrides specific language settings while retaining the default behavior for all other supported languages. It ensures the resulting executor's policies match the specified overrides and maintain the complete set of expected language keys.*


### _test_restart (function, L309-L312)

> *Summary: This test verifies that calling the executor's restart method emits a `UserWarning` containing the specific message "No action is taken." when no actual restart occurs. It takes an initialized `CodeExecutor` instance as input and returns nothing upon successful assertion of the warning.*


### test_commandline_executor_conversable_agent_code_execution (function, L316-L321)

> *Summary: This test sets up a temporary working directory and initializes an executor instance to verify code execution within a conversational agent context. It mocks the OpenAI API key environment variable before running the core execution logic.*


### _test_conversable_agent_code_execution (function, L324-L344)

> *Summary: This test verifies that a `ConversableAgent` correctly utilizes a provided `CodeExecutor`. It sends a prompt containing example Python code to the agent and asserts that the generated reply includes the expected extracted code snippet.*


### test_dangerous_commands (function, L358-L363)

> *Summary: This test verifies that the command sanitization process raises a `ValueError` when provided with dangerous code, asserting that the exception message contains the expected warning text. It takes language and code as inputs to trigger this validation failure.*


### test_invalid_relative_path (function, L367-L374)

> *Summary: When executing code blocks containing a file reference outside the designated workspace, this test asserts that the execution fails with an exit code of 1 and reports a specific error message about the invalid filename location.*


### test_valid_relative_path (function, L378-L391)

> *Summary: This test verifies that the code executor correctly runs Python code from a valid relative path within a temporary directory. It asserts successful execution, checks for expected output content, and confirms the generated file exists at the correct resolved location.*


### test_silent_pip_install (function, L396-L419)

> *Summary: This test verifies the behavior of executing `pip install` commands across different operating systems and shells. It asserts that installing a valid package succeeds silently, while attempting to install a non-existent package correctly returns an error exit code and output containing an error message.*


### test_local_executor_with_custom_python_env (function, L422-L436)

> *Summary: This test verifies that the local code executor correctly runs Python code within a custom-built virtual environment. It executes a script designed to confirm if the running interpreter is indeed inside the isolated environment, asserting the output confirms this state.*


### test_local_executor_with_custom_python_env_in_local_relative_path (function, L439-L463)

> *Summary: This test verifies that the local code executor correctly utilizes a custom Python environment located in a relative path. It builds a virtual environment, executes a simple script to print the interpreter path, and asserts that the output's parent directory matches the expected virtual environment binary path.*

