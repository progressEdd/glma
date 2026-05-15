# cli/src/ag2_cli/commands/install.py

23 function(s): _make_installers, install_skills, install_template, install_tool, install_dataset, install_agent, install_bundle, search_cmd, list_cmd, update_cmd and 13 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_installers | function |  |
| install_skills | function |  |
| install_template | function |  |
| install_tool | function |  |
| install_dataset | function |  |
| install_agent | function |  |
| install_bundle | function |  |
| search_cmd | function |  |
| list_cmd | function |  |
| update_cmd | function |  |
| uninstall_cmd | function |  |
| install_from | function |  |
| _print_result | function |  |
| _install_local_artifact | function |  |
| _install_local_via_cache | function |  |
| _list_targets | function |  |
| _list_installed | function |  |
| _list_skills_pack | function |  |
| _list_all_remote | function |  |
| _list_remote | function |  |
| _resolve_targets | function |  |
| _is_interactive | function |  |
| _interactive_select | function |  |

## Chunks

### _make_installers (function, L31-L61)

> *Summary: This function constructs and returns a dictionary containing initialized instances of various installer types (Skills, Templates, Tools, etc.), along with shared dependencies like an `ArtifactClient`, `Lockfile`, and `DependencyResolver`. It takes a project directory path as input to set up the necessary environment for creating these installers.*


### install_skills (function, L70-L109)

> *Summary: This function installs AI agent skills, accepting optional skill packs, a specific item name, target IDEs, and a project directory as inputs. It fetches necessary components, executes the installation via a skill manager, and reports the total number of files created across all successful installations.*


### install_template (function, L118-L150)

> *Summary: This function scaffolds a project by installing a specified template into a given directory, optionally targeting specific IDEs or providing configuration variables. It takes the template name and various optional arguments like target, project path, variables, and a preview flag to execute the installation process.*


### install_tool (function, L159-L191)

> *Summary: This function installs a specified AG2 tool or MCP server, using provided arguments for the tool name, target IDE/agent, and project directory. It fetches the necessary source code and skills, handles potential download errors, and finally lists any newly available functions or tools from the installed artifact.*


### install_dataset (function, L200-L223)

> *Summary: This function installs a specified dataset by taking the dataset name and optional configuration parameters like a target IDE, project directory, and whether to download all remote files. It resolves targets and prepares installers before calling the core installation logic and reporting the outcome or any fetch errors.*


### install_agent (function, L232-L262)

> *Summary: This function installs a pre-built Claude Code subagent, taking the agent's name as a required argument and optionally accepting a target IDE or project directory. It resolves targets and builds an installation stack to execute the agent installation via `stack["agents"].install()`, finally printing usage instructions upon success.*


### install_bundle (function, L271-L293)

> *Summary: This function installs a curated collection of artifacts (a bundle) given its name, an optional target IDE, and a project directory. It resolves targets and prepares installers before executing the installation via the `stack["bundles"].install` method, handling potential fetch errors gracefully.*


### search_cmd (function, L302-L342)

> *Summary: This function queries an artifact client to find artifacts matching a provided search query and optional type filter. It fetches the registry, executes the search, and then displays the results in a formatted panel, suggesting installation commands for each found item.*


### list_cmd (function, L351-L364)

> *Summary: This function serves as a command handler that lists various system components based on the provided string argument. It delegates to specific internal functions (`_list_targets`, `_list_installed`, etc.) depending on whether the input specifies targets, installed items, all available artifacts, or a particular type of remote artifact.*


### update_cmd (function, L373-L421)

> *Summary: This function checks installed artifacts against a remote registry to determine available updates. It accepts an optional specific artifact name and a project directory, returning nothing but printing a list of outdated artifacts if any are found.*


### uninstall_cmd (function, L430-L467)

> *Summary: Removes installed artifacts based on the provided artifact name, optionally targeting a specific IDE or agent. It first attempts a precise uninstall using lockfile tracking; otherwise, it falls back to a legacy target-based removal process for skills.*


### install_from (function, L476-L508)

> *Summary: This function installs an artifact either from a local directory or (currently unsupported) a remote URL. It takes a source path/URL, an optional target IDE, and a project directory as input, ultimately executing installation logic based on the source type.*


### _print_result (function, L516-L537)

> *Summary: Displays a summary of an installation operation, taking an `InstallResult` object as input. It prints the count of created files and optionally lists dependencies and any warnings encountered during the process.*


### _install_local_artifact (function, L540-L578)

> *Summary: This function handles the installation of a locally resolved artifact based on its type. It delegates to specific logic—like loading skills or using cached installers for templates, tools, agents, and datasets—and records successful installations in the stack's lockfile when applicable.*


### _install_local_via_cache (function, L581-L596)

> *Summary: This function stages a local artifact into the client's designated cache directory by copying its source contents and marking it as fetched. It then delegates the actual installation process to the main installer using the artifact's qualified name.*


### _list_targets (function, L599-L608)

> *Summary: This function retrieves all supported IDE and agent targets by calling `get_all_targets()` and then prints them in a formatted table to the console. It serves to display available configuration options to the user via the command-line interface.*


### _list_installed (function, L611-L629)

> *Summary: Reads a project directory to load and list artifacts from its lockfile. It then formats and prints a table summarizing the artifact reference, version, file count, and installation date to the console if any are found.*


### _list_skills_pack (function, L632-L655)

> *Summary: Retrieves and displays the contents of a bundled "skills" pack if it exists; otherwise, it prints an error and exits. It iterates through predefined categories ("rule", "skill", etc.) within the loaded pack and renders each group as a formatted table showing item names and descriptions.*


### _list_all_remote (function, L658-L704)

> *Summary: Fetches all artifacts from a remote registry, handling potential fetch errors gracefully. It then groups these artifacts by predefined types and prints them to the console in categorized tables, along with the corresponding installation command for each type.*


### _list_remote (function, L707-L751)

> *Summary: Fetches and displays a list of artifacts from a remote registry based on the provided artifact type string. It normalizes the input type, retrieves entries using an `ArtifactClient`, formats them into a readable table, and finally suggests the corresponding installation command for the user.*


### _resolve_targets (function, L759-L784)

> *Summary: This function translates a target specification string into a list of `Target` objects based on the provided project path. It handles "all" targets, parses comma-separated inputs with error checking, or automatically detects and optionally prompts for targets if no explicit input is given.*


### _is_interactive (function, L787-L791)

> *Summary: Checks if standard input is connected to a terminal by attempting `sys.stdin.isatty()`; returns `True` if interactive, otherwise `False`.*


### _interactive_select (function, L794-L847)

> *Summary: Presents an interactive prompt allowing a user to select installation targets from a list of all available targets, highlighting any that were pre-detected. It accepts comma-separated indices or names as input and returns a list of the chosen target objects, exiting with an error if no valid selections are made.*

