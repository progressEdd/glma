# cli/tests/test_mcp_config.py

3 class(es): TestConfigureMcpServer, TestDetectMcpTargets, TestRemoveMcpServer. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestConfigureMcpServer | class |  |
| TestDetectMcpTargets | class |  |
| TestRemoveMcpServer | class |  |

## Chunks

### TestConfigureMcpServer (class, L7-L84)

> *Summary: These tests verify the `configure_mcp_server` function's behavior when writing configuration files for various IDEs (Claude, Cursor, VSCode). It ensures correct file creation, proper structure based on the target IDE, and successful merging of new server configurations into existing ones.*


### test_creates_claude_config (method, L10-L24, parent: TestConfigureMcpServer)

> *Summary: This test verifies that the `configure_mcp_server` function correctly generates a configuration file. It takes project directory, server name, command details, and IDE targets as input, asserting that the resulting `.mcp.json` contains the specified server configuration under `mcpServers`.*


### test_creates_cursor_config (method, L26-L38, parent: TestConfigureMcpServer)

> *Summary: This test verifies that calling `configure_mcp_server` with a specified project directory, server name, and configuration correctly generates an `mcp.json` file containing the expected server entry under `mcpServers`. It asserts the presence of the configured server within the generated JSON structure.*


### test_creates_vscode_config_with_servers_key (method, L40-L53, parent: TestConfigureMcpServer)

> *Summary: This test verifies that the configuration function correctly generates a `.vscode/mcp.json` file containing a `servers` key when targeting VS Code. It passes project directory, server name, command details, and targets to ensure the output JSON structure is correct.*


### test_merges_into_existing_config (method, L55-L72, parent: TestConfigureMcpServer)

> *Summary: This test verifies that a new server configuration is correctly merged into an existing `.mcp.json` file. It takes an initial configuration and adds a new server definition, asserting both the old and new entries persist after the operation.*


### test_multiple_ide_targets (method, L74-L84, parent: TestConfigureMcpServer)

> *Summary: This test verifies that the configuration function correctly generates multiple server paths when provided with a list of IDE targets. It asserts that the returned list contains one path for each specified target ("claude", "cursor", and "vscode").*


### TestDetectMcpTargets (class, L87-L117)

> *Summary: These tests verify the `detect_mcp_targets` function's ability to automatically identify configured MCP targets within a given directory structure. It checks that the function correctly finds specific markers (like `.claude`, `.cursor`, or files like `CLAUDE.md`) and returns an accurate list of detected target names, including handling empty directories.*


### test_detects_claude (method, L90-L95, parent: TestDetectMcpTargets)

> *Summary: This test verifies that the `detect_mcp_targets` function correctly identifies a specific configuration by checking for the presence of `"claude"` in the returned list of targets when a `.claude` directory exists. It uses a temporary path to simulate the necessary file structure for testing.*


### test_detects_cursor (method, L97-L102, parent: TestDetectMcpTargets)

> *Summary: This test verifies that the `detect_mcp_targets` function correctly identifies a specific configuration target. It achieves this by creating a directory named `.cursor` within a temporary path and asserting that `"cursor"` is present in the returned list of targets.*


### test_detects_multiple (method, L104-L111, parent: TestDetectMcpTargets)

> *Summary: This test verifies that the `detect_mcp_targets` function correctly identifies multiple configuration sources. It achieves this by creating dummy files and directories within a temporary path and asserting that both "claude" and "vscode" are present in the returned list of targets.*


### test_empty_project (method, L113-L117, parent: TestDetectMcpTargets)

> *Summary: When provided with an empty directory path, this test asserts that the function returns an empty list of detected MCP targets. It verifies the behavior of `detect_mcp_targets` when no project structure is present.*


### TestRemoveMcpServer (class, L120-L134)

> *Summary: This test verifies the functionality of removing an MCP server configuration from a JSON file. It first sets up two servers, then calls the removal function for one, asserting that exactly one entry was returned and the specified server is absent from the final configuration while the other remains present.*


### test_removes_server_entry (method, L123-L134, parent: TestRemoveMcpServer)

> *Summary: This test verifies that a specific server entry can be successfully deleted from the configuration file. It first sets up two servers, then calls the removal function for one, asserting that only the intended server is gone and the other remains in the resulting JSON configuration.*

