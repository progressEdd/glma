# cli/src/ag2_cli/install/mcp_config.py

5 function(s): detect_mcp_targets, configure_mcp_server, remove_mcp_server, _read_json, _write_json.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| detect_mcp_targets | function |  |
| configure_mcp_server | function |  |
| remove_mcp_server | function |  |
| _read_json | function |  |
| _write_json | function |  |

## Chunks

### detect_mcp_targets (function, L16-L27)

> *Summary: Scans a given project directory to identify supported IDEs by checking for specific marker files within the directory structure. It returns a list of strings representing the names of the detected IDEs (e.g., "claude", "vscode").*


### configure_mcp_server (function, L30-L70)

> *Summary: This function modifies IDE configuration files within a project directory by adding or updating an MCP server entry based on provided server details and configuration. It accepts the project path, server name, configuration dictionary, and optional target IDEs, returning a list of all modified config file paths.*


### remove_mcp_server (function, L73-L89)

> *Summary: This function iterates through predefined IDE configuration files within a project directory to locate and remove a specified server entry. It takes the project path and server name as input, returning a list of paths for every configuration file where the server was successfully deleted.*


### _read_json (function, L92-L99)

> *Summary: Reads the content of a specified file path as JSON; returns an empty dictionary if the file is missing or contains invalid JSON data.*


### _write_json (function, L102-L107)

> *Summary: This utility function saves a Python dictionary to a specified file path as formatted JSON. It ensures atomic writing by first saving the data to a temporary file and then renaming it over the target path.*

