# cli/tests/conftest.py

7 function(s): tmp_project, agent_file_with_main, agent_file_with_variable, agent_file_with_agents_list, agent_file_empty, yaml_config_file, eval_yaml_file.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| tmp_project | function |  |
| agent_file_with_main | function |  |
| agent_file_with_variable | function |  |
| agent_file_with_agents_list | function |  |
| agent_file_empty | function |  |
| yaml_config_file | function |  |
| eval_yaml_file | function |  |

## Chunks

### tmp_project (function, L12-L21)

> *Summary: This function sets up a standardized, temporary directory structure for testing. It creates subdirectories like `agents`, `tools`, and `teams` within the provided path, initializing them as Python packages, and returns the root of this newly created project structure.*


### agent_file_with_main (function, L25-L34)

> *Summary: Generates a temporary Python file containing a simple `main` function that accepts an optional message and returns a formatted response string. This utility is used within tests to provide a predefined agent script for execution.*


### agent_file_with_variable (function, L38-L53)

> *Summary: Generates a temporary Python file containing a `FakeAgent` class instance named `agent`. This function returns the path to this created file, which is intended for testing purposes.*


### agent_file_with_agents_list (function, L57-L72)

> *Summary: Generates a temporary Python file containing a `FakeAgent` class and an initialized list of agents. This function returns the path to the created file, which is useful for testing code that consumes agent definitions.*


### agent_file_empty (function, L76-L80)

> *Summary: Creates an empty Python file within a temporary directory, containing only a single line of code (`x = 42`). This function returns the path to this newly created file for testing purposes.*


### yaml_config_file (function, L84-L103)

> *Summary: Generates a sample YAML configuration file named `team.yaml` within a temporary directory. This file defines LLM settings, agent configurations (like 'researcher' and 'writer'), and team parameters such as maximum rounds.*


### eval_yaml_file (function, L107-L134)

> *Summary: Generates a YAML file containing predefined test cases with inputs and assertions. This function takes a temporary path as input and returns the path to the created `cases.yaml` file, which is used for testing evaluation scenarios.*

