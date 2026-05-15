# cli/src/ag2_cli/core/discovery.py

6 function(s): import_agent_file, _is_agent_instance, _get_agent_name, discover, load_yaml_config, build_agents_from_yaml. 1 class(es): DiscoveredAgent.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DiscoveredAgent | class |  |
| import_agent_file | function |  |
| _is_agent_instance | function |  |
| _get_agent_name | function |  |
| discover | function |  |
| load_yaml_config | function |  |
| build_agents_from_yaml | function |  |

## Chunks

### DiscoveredAgent (class, L23-L31)

> *Summary: Represents the outcome of scanning a file for agent definitions. It stores metadata including the discovery type, source path, and optional references to main functions or discovered agents/agent lists.*


### import_agent_file (function, L34-L65)

> *Summary: Loads a Python file from the given path into a runnable module object by dynamically creating and executing it using `importlib`. It ensures the parent directory is temporarily added to `sys.path` to resolve relative imports during execution, returning the fully loaded module.*


### _is_agent_instance (function, L68-L78)

> *Summary: Determines if an input object behaves like a `ConversableAgent` by first checking for direct inheritance from the `autogen.ConversableAgent`. If that fails or is unavailable, it falls back to verifying the presence of `initiate_chat` and `name` attributes on the object.*


### _get_agent_name (function, L81-L83)

> *Summary: Retrieves a string identifier for an object by first checking for a `name` attribute; if absent, it defaults to the object's class name as a fallback.*


### discover (function, L86-L136)

> *Summary: Scans a given file path to locate and return a `DiscoveredAgent` object. It checks for a `main()` function, specific variables (`agent`, `team`), an `agents` list, or any other exposed agent instance within the module's namespace; otherwise, it raises a `ValueError`.*


### load_yaml_config (function, L139-L153)

> *Summary: Reads and parses a YAML file located at the provided path into a Python dictionary. It validates that the loaded content is a dictionary and raises errors if the file is missing or improperly formatted.*


### build_agents_from_yaml (function, L156-L206)

> *Summary: Constructs one or more `AssistantAgent` instances from a dictionary representing YAML configuration data. It uses the provided LLM settings and agent definitions (name, system message) to create agents, returning a `DiscoveredAgent` object containing either a single agent or a list of agents.*

