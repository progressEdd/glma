# test/agentchat/test_agent_setup_with_use_docker_settings.py

8 function(s): docker_running, test_agent_setup_with_code_execution_off, test_agent_setup_with_use_docker_false, test_agent_setup_with_env_variable_false_and_docker_running, test_agent_setup_with_default_and_docker_running, test_raises_error_agent_setup_with_default_and_docker_not_running, test_raises_error_agent_setup_with_env_variable_true_and_docker_not_running, test_agent_setup_with_env_variable_true_and_docker_running.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| docker_running | function |  |
| test_agent_setup_with_code_execution_off | function |  |
| test_agent_setup_with_use_docker_false | function |  |
| test_agent_setup_with_env_variable_false_and_docker_running | function |  |
| test_agent_setup_with_default_and_docker_running | function |  |
| test_raises_error_agent_setup_with_default_and_docker_not_running | function |  |
| test_raises_error_agent_setup_with_env_variable_true_and_docker_not_running | function |  |
| test_agent_setup_with_env_variable_true_and_docker_running | function |  |

## Chunks

### docker_running (function, L18-L19)

> *Summary: Checks if the current environment is running inside a Docker container by combining checks for both general Docker execution and specific container presence. Returns a boolean indicating whether Docker is active or the code is executing within a containerized environment.*


### test_agent_setup_with_code_execution_off (function, L22-L29)

> *Summary: Verifies that the `UserProxyAgent` instance correctly initializes with code execution disabled when configured via `code_execution_config=False`. It asserts that the internal state reflects this configuration.*


### test_agent_setup_with_use_docker_false (function, L32-L39)

> *Summary: This test verifies that the `UserProxyAgent` instance correctly configures its code execution settings when explicitly set to disable Docker usage. It asserts that the internal configuration reflects `use_docker` being `False`.*


### test_agent_setup_with_env_variable_false_and_docker_running (function, L42-L50)

> *Summary: This test verifies that when the `AUTOGEN_USE_DOCKER` environment variable is set to "False," the agent's code execution configuration correctly disables Docker usage. It asserts that the internal `use_docker` flag within the `UserProxyAgent` instance is set to `False`.*


### test_agent_setup_with_default_and_docker_running (function, L54-L66)

> *Summary: This test verifies that when the `AUTOGEN_USE_DOCKER` environment variable is unset, the agent's code execution configuration defaults to using Docker. It asserts that the internal setting for Docker usage is correctly set to `True`.*


### test_raises_error_agent_setup_with_default_and_docker_not_running (function, L70-L76)

> *Summary: When the `AUTOGEN_USE_DOCKER` environment variable is unset, instantiating a `UserProxyAgent` without Docker running will raise a `RuntimeError`. This test verifies that the agent setup correctly fails when required dependencies like Docker are unavailable.*


### test_raises_error_agent_setup_with_env_variable_true_and_docker_not_running (function, L80-L87)

> *Summary: When the `AUTOGEN_USE_DOCKER` environment variable is set to "True," this test asserts that initializing a `UserProxyAgent` raises a `RuntimeError` if Docker is not running.*


### test_agent_setup_with_env_variable_true_and_docker_running (function, L91-L99)

> *Summary: Sets an environment variable to enable Docker usage and then asserts that the `UserProxyAgent` instance correctly configures its code execution settings to use Docker. This verifies the agent setup respects the specified environment flag.*

