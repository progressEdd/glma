# test/beta/config/openai/tools/test_shell.py

4 function(s): test_no_environment, test_container_auto, test_container_auto_with_network_policy, test_container_reference.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_no_environment | function |  |
| test_container_auto | function |  |
| test_container_auto_with_network_policy | function |  |
| test_container_reference | function |  |

## Chunks

### test_no_environment (function, L18-L23)

> *Summary: This asynchronous test verifies that a `ShellTool` correctly generates a schema when no environment context is provided. It asserts that the resulting schema identifies the tool type as `"shell"`.*


### test_container_auto (function, L27-L32)

> *Summary: This test verifies that a `ShellTool` configured with `ContainerAutoEnvironment` correctly generates a schema indicating its type is "shell" and specifies the environment as "container\_auto". It achieves this by calling the tool's `schemas` method with a provided context.*


### test_container_auto_with_network_policy (function, L36-L49)

> *Summary: This test verifies that a `ShellTool` correctly generates an OpenAPI schema when configured with a specific network policy. It asserts the resulting schema accurately reflects the container auto environment, including the allowed domains list.*


### test_container_reference (function, L53-L61)

> *Summary: This test verifies that a `ShellTool` initialized with a specific container reference correctly generates the expected JSON schema. It asserts that the resulting schema accurately reflects the container ID provided during tool instantiation.*

