# cli/tests/test_create.py

4 class(es): TestCreateProject, TestCreateAgent, TestCreateTool, TestCreateTeam. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestCreateProject | class |  |
| TestCreateAgent | class |  |
| TestCreateTool | class |  |
| TestCreateTeam | class |  |

## Chunks

### TestCreateProject (class, L14-L58)

> *Summary: These tests verify the functionality of a project creation command-line interface by invoking it with various inputs like project names and templates. They assert that the correct directory structure, configuration files, and specific content are generated upon successful execution, while also confirming failure modes for existing directories or unknown templates.*


### test_creates_project_structure (method, L15-L30, parent: TestCreateProject)

> *Summary: This test verifies that invoking the `create project` command with a given name successfully generates a complete, expected directory and file structure within a temporary path. It asserts the existence of key files like `pyproject.toml`, `.env.example`, and subdirectories containing initial code stubs.*


### test_pyproject_has_correct_name (method, L32-L37, parent: TestCreateProject)

> *Summary: This test verifies that the `create project` command correctly configures the generated `pyproject.toml` file. It asserts that the resulting project directory contains the expected package name and a specific identifier within its configuration.*


### test_research_team_template (method, L39-L45, parent: TestCreateProject)

> *Summary: This test verifies that invoking the `create project research --template research-team` command successfully generates a new project structure. It asserts that the expected files, specifically `researcher.py` and `writer.py`, are created within the generated directory.*


### test_fails_on_existing_directory (method, L47-L52, parent: TestCreateProject)

> *Summary: This test verifies that the project creation command fails when a directory with the specified name already exists. It asserts that the invocation returns a non-zero exit code and contains an "already exists" message in its output.*


### test_fails_on_unknown_template (method, L54-L58, parent: TestCreateProject)

> *Summary: This test verifies that the application correctly fails when a user attempts to create a project using an unknown template name. It asserts that the command returns a non-zero exit code and includes an "Unknown template" message in its output.*


### TestCreateAgent (class, L61-L91)

> *Summary: This test suite verifies the agent creation functionality by invoking CLI commands against a temporary project structure. It asserts that agents are created correctly with default or specified tools, handles errors when files already exist, and defaults to creating the file in the current working directory if no dedicated agents folder is present.*


### test_creates_agent_file (method, L62-L70, parent: TestCreateAgent)

> *Summary: This test verifies that running the `create agent researcher` command successfully generates an agent file within the project structure. It asserts that the command exits cleanly and the resulting Python file contains expected class and name definitions.*


### test_creates_agent_with_tools (method, L72-L78, parent: TestCreateAgent)

> *Summary: This test verifies that the CLI successfully creates an agent named "helper" and correctly injects specified tools ("web-search", "code-exec") into its generated Python file. It asserts a successful exit code and checks for the presence of tool names within the created agent's source code.*


### test_fails_on_existing_file (method, L80-L85, parent: TestCreateAgent)

> *Summary: This test verifies that the agent creation command fails when a file with the same name already exists in the project directory. It asserts that the execution returns a non-zero exit code and contains an "already exists" message in its output.*


### test_creates_in_cwd_when_no_agents_dir (method, L87-L91, parent: TestCreateAgent)

> *Summary: When no dedicated agents directory is specified, this test verifies that the agent creation command places the new agent file directly into the current working directory. It asserts successful execution and confirms the existence of the expected Python file in `tmp_path`.*


### TestCreateTool (class, L94-L111)

> *Summary: This test suite verifies the CLI's ability to generate tool files based on command-line arguments. It asserts that running `create tool` with and without a description correctly produces Python files containing specific metadata tags and names within a temporary project directory.*


### test_creates_tool_file (method, L95-L104, parent: TestCreateTool)

> *Summary: This test verifies that invoking the `create tool` command successfully generates a Python file within the project's `tools` directory. It asserts that the generated file exists and contains specific metadata tags corresponding to the provided tool name and description.*


### test_creates_tool_without_description (method, L106-L111, parent: TestCreateTool)

> *Summary: This test verifies that invoking the `create tool` command successfully generates a Python file for the specified tool. It asserts that the resulting file contains the `@tool` marker, confirming its basic creation and structure.*


### TestCreateTeam (class, L114-L143)

> *Summary: These tests verify the team creation functionality by invoking a CLI command with various inputs. They assert that teams are created correctly, checking for file existence and specific content based on provided patterns or default agent configurations, while also ensuring failure when an invalid pattern is supplied.*


### test_creates_team_file (method, L115-L128, parent: TestCreateTeam)

> *Summary: This test verifies that invoking the `create team` command with specific arguments successfully generates a team configuration file. It asserts that the operation exits cleanly and the resulting Python file contains expected pattern and agent names.*


### test_default_agents_when_none_specified (method, L130-L137, parent: TestCreateTeam)

> *Summary: When creating a new team without specifying agents, this test verifies that the resulting team file contains default agent definitions (`agent_a` and `agent_b`). It achieves this by invoking the application's create command within a temporary project directory.*


### test_fails_on_unknown_pattern (method, L139-L143, parent: TestCreateTeam)

> *Summary: This test verifies that the application correctly fails when provided with an unrecognized `--pattern` argument during team creation. It asserts that the command exits with a non-zero code and includes an "Unknown pattern" message in its output.*

