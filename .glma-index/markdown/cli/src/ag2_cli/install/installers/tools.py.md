# cli/src/ag2_cli/install/installers/tools.py

2 function(s): _install_dependencies, _resolve_tool_dir. 1 class(es): ToolInstaller. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ToolInstaller | class |  |
| _install_dependencies | function |  |
| _resolve_tool_dir | function |  |

## Chunks

### ToolInstaller (class, L18-L171)

> *Summary: This class manages the installation of AG2 tool artifacts, distinguishing between standard functions and MCP servers. It fetches an artifact via a client, then either copies source code and installs bundled skills/dependencies for an AG2 tool or handles server setup, dependency resolution, and IDE configuration for an MCP tool before recording the successful installation in a lockfile.*


### __init__ (method, L21-L31, parent: ToolInstaller)

> *Summary: Initializes the tool with necessary dependencies: an artifact client, a lockfile manager, a dependency resolver, and a skills installer. These components are stored as instance attributes for subsequent operations.*


### install (method, L33-L54, parent: ToolInstaller)

> *Summary: Retrieves and validates a tool artifact based on a provided name, then dispatches the installation process. It determines whether to use an MCP or standard AG2 installer based on the artifact's configuration before executing the appropriate installation logic against specified targets within the project directory.*


### _install_ag2_tool (method, L56-L104, parent: ToolInstaller)

> *Summary: Copies tool source files into a specified project directory and installs bundled skills based on provided targets. It then resolves and installs any skill dependencies before recording the installation details in a lockfile and returning an `InstallResult`.*


### _install_mcp_tool (method, L106-L171, parent: ToolInstaller)

> *Summary: Copies server source code to a specified project directory, then installs Python/Node dependencies and configures IDEs if necessary. Finally, it installs bundled skills for given targets and records the installation details in a lockfile before returning an `InstallResult`.*


### _install_dependencies (function, L174-L191)

> *Summary: This function attempts to install a list of required Python packages using `pip` within the specified tool directory. It executes each installation command, logging success or failure warnings based on the subprocess return code or if execution times out or fails to find `pip`.*


### _resolve_tool_dir (function, L194-L206)

> *Summary: This function recursively traverses a configuration dictionary to substitute the placeholder `${toolDir}` with an actual `Path` object. It returns a new, fully resolved configuration dictionary where all string values containing the placeholder have been updated.*

