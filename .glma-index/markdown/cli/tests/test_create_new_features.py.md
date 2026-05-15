# cli/tests/test_create_new_features.py

1 function(s): _mock_llm_generate. 10 class(es): TestDetectGenerationModel, TestParseJsonResponse, TestFullstackAgenticTemplate, TestProjectScaffoldFixes, TestCreateProjectFromDescription, TestCreateAgentFromDescription, TestCreateToolFromModule, TestCreateToolFromOpenAPI, TestLLMConfigBugFix, TestTestCmdChanges. 39 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _mock_llm_generate | function |  |
| TestDetectGenerationModel | class |  |
| TestParseJsonResponse | class |  |
| TestFullstackAgenticTemplate | class |  |
| TestProjectScaffoldFixes | class |  |
| TestCreateProjectFromDescription | class |  |
| TestCreateAgentFromDescription | class |  |
| TestCreateToolFromModule | class |  |
| TestCreateToolFromOpenAPI | class |  |
| TestLLMConfigBugFix | class |  |
| TestTestCmdChanges | class |  |

## Chunks

### _mock_llm_generate (function, L26-L28)

> *Summary: This helper function generates a `MagicMock` object configured to return a JSON-serialized string based on an input dictionary. It simulates the output of an LLM generation call for testing purposes.*


### TestDetectGenerationModel (class, L36-L59)

> *Summary: This test suite verifies the `_detect_generation_model` function's behavior by setting environment variables for different AI providers (OpenAI, Anthropic, Google). It asserts that the function correctly identifies and returns the expected model string based on the presence of specific API keys, returning `None` when no keys are set.*


### test_detects_openai (method, L37-L40, parent: TestDetectGenerationModel)

> *Summary: When the `OPENAI_API_KEY` environment variable is set to a test key, this test asserts that the internal function correctly identifies and returns `"gpt-4o"` as the generation model.*


### test_detects_anthropic (method, L42-L47, parent: TestDetectGenerationModel)

> *Summary: When an environment variable for the Anthropic API key is set, this test verifies that the model detection function successfully identifies and returns a model string containing "claude". It asserts that the returned model is neither null nor missing the expected identifier.*


### test_detects_google (method, L49-L54, parent: TestDetectGenerationModel)

> *Summary: When provided with an environment variable containing a Google API key, this test verifies that the model detection function successfully identifies and returns a Gemini-related model object. It asserts that the returned model is not null and contains the string "gemini".*


### test_returns_none_when_no_keys (method, L56-L59, parent: TestDetectGenerationModel)

> *Summary: When the environment variables are cleared, this test asserts that the function responsible for detecting a generation model returns `None`. This verifies the expected behavior when no configuration keys are present.*


### TestParseJsonResponse (class, L67-L90)

> *Summary: These tests verify that a utility function correctly extracts and parses JSON objects from various string inputs, including plain text, markdown code blocks, generic code blocks, and embedded snippets. It also asserts that the function raises an error when provided with non-JSON content.*


### test_parses_plain_json (method, L68-L71, parent: TestParseJsonResponse)

> *Summary: This test verifies that the `_parse_json_response` utility correctly deserializes a simple JSON string input into its corresponding Python dictionary output. It asserts that the parsed structure matches the original data provided in the input text.*


### test_parses_json_in_markdown_block (method, L73-L76, parent: TestParseJsonResponse)

> *Summary: This test verifies that a utility function correctly extracts and parses JSON content embedded within a markdown code block string. It takes a string containing the JSON snippet as input and asserts the output matches the expected Python dictionary structure.*


### test_parses_json_in_generic_code_block (method, L78-L81, parent: TestParseJsonResponse)

> *Summary: This test verifies that a utility function correctly extracts and parses JSON content embedded within a markdown code block string. It takes a string containing the JSON snippet as input and asserts the output is the corresponding Python dictionary.*


### test_extracts_json_object_from_text (method, L83-L86, parent: TestParseJsonResponse)

> *Summary: This test verifies that a parsing utility correctly extracts a JSON object from a string containing surrounding text. It takes a mixed-content string as input and asserts the output matches the expected dictionary structure.*


### test_exits_on_unparsable_response (method, L88-L90, parent: TestParseJsonResponse)

> *Summary: Asserts that attempting to parse a non-JSON string causes the function to raise either `SystemExit` or a general `Exception`. This verifies error handling when input data is malformed.*


### TestFullstackAgenticTemplate (class, L98-L114)

> *Summary: This test suite verifies the functionality of a project creation command by invoking it with a specific template. It asserts that the resulting directory structure contains expected agent files and further checks that these generated files contain valid, predefined code snippets.*


### test_creates_all_agents (method, L99-L106, parent: TestFullstackAgenticTemplate)

> *Summary: This test verifies that running the `create project` command with a specific template successfully generates all expected agent files within the new project directory. It asserts that `planner.py`, `coder.py`, and `reviewer.py` exist in the generated agents subdirectory.*


### test_agent_files_contain_valid_code (method, L108-L114, parent: TestFullstackAgenticTemplate)

> *Summary: This test verifies that the generated agent files contain expected code structures after creating a new project. It checks if specific strings, like `AssistantAgent`, configuration details, and HTML attributes, are present within the `planner.py` file of the newly created project structure.*


### TestProjectScaffoldFixes (class, L122-L146)

> *Summary: This test suite verifies that the project scaffolding command correctly generates necessary configuration and tool files for various templates. It executes `create project` commands, asserting the existence and basic content of `llm.yaml` and `web_search.py` within the newly created project directories.*


### test_config_llm_yaml_created (method, L125-L128, parent: TestProjectScaffoldFixes)

> *Summary: This test verifies that running the `create project scaffold-test` command successfully generates an `llm.yaml` configuration file within the newly created project directory structure. It asserts the existence of this specific YAML file after invoking the application runner in a temporary environment.*


### test_tools_web_search_created (method, L130-L137, parent: TestProjectScaffoldFixes)

> *Summary: This test verifies that scaffolding a new project successfully creates the `web_search.py` file within the tools directory. It asserts the file exists and contains specific markers indicating it is a recognized tool.*


### test_all_templates_create_config_and_tools (method, L139-L146, parent: TestProjectScaffoldFixes)

> *Summary: This test iterates over several predefined templates, invoking a project creation command for each one within a temporary directory. It asserts that the process succeeds and verifies the existence of expected configuration (`llm.yaml`) and tool files (`web_search.py`) within the newly created project structure.*


### TestCreateProjectFromDescription (class, L154-L248)

> *Summary: This test suite verifies the functionality of creating a new project from a natural language description by mocking LLM generation. It asserts that the CLI correctly scaffolds the project structure, handles name overrides, and configures the main execution logic based on whether the generated specification contains one or multiple agents.*


### test_generates_project_from_description (method, L181-L194, parent: TestCreateProjectFromDescription)

> *Summary: This test verifies that the CLI successfully creates a new project directory structure when provided with a natural language description via the `--from-description` flag. It asserts that the resulting directory contains expected files like `pyproject.toml`, agent scripts, and main application files.*


### test_name_override (method, L197-L202, parent: TestCreateProjectFromDescription)

> *Summary: This test verifies that providing a custom name during project creation successfully overrides the default naming convention. It invokes the CLI command with a specified name and asserts that the operation succeeds and creates a directory matching that custom name.*


### test_main_py_uses_group_chat_for_multiple_agents (method, L205-L211, parent: TestCreateProjectFromDescription)

> *Summary: This test verifies that the application's main script utilizes group chat functionality when creating a project from a multi-agent description. It achieves this by invoking the `create project` command with a specific input and asserting the presence of relevant keywords in the generated Python file content.*


### test_single_agent_project_uses_initiate_chat (method, L214-L226, parent: TestCreateProjectFromDescription)

> *Summary: This test verifies that when creating a project from a description, the generated `main.py` file correctly includes the `initiate_chat` function while excluding `run_group_chat`. It simulates invoking the CLI command with specific project configuration data provided via a mock generator.*


### test_fails_on_existing_dir (method, L229-L235, parent: TestCreateProjectFromDescription)

> *Summary: When a directory already exists at the target location, this test asserts that the project creation command fails with a non-zero exit code and includes an "already exists" message in its output. It simulates this by creating the necessary directory before invoking the CLI runner.*


### test_fails_on_empty_agents (method, L238-L243, parent: TestCreateProjectFromDescription)

> *Summary: This test verifies that the system fails when attempting to create a new project from an input description that results in no agents being generated. It asserts that the command execution returns a non-zero exit code and contains a specific failure message.*


### test_requires_name_without_from_description (method, L245-L248, parent: TestCreateProjectFromDescription)

> *Summary: This test verifies that the `create project` command fails if a required name is missing from the description input. It invokes the application with the specified arguments and asserts a non-zero exit code to confirm the failure.*


### TestCreateAgentFromDescription (class, L256-L317)

> *Summary: This test suite verifies the functionality of creating AI agents from a natural language description using an LLM-generated specification. It asserts that the CLI correctly generates agent and tool files in the appropriate directories, handles name overrides, manages cases with no tools, and enforces required arguments like a name or description.*


### test_generates_agent_and_tools (method, L270-L276, parent: TestCreateAgentFromDescription)

> *Summary: When invoked with a description, this test verifies that the application successfully creates both an agent file and a corresponding tool file within the specified project directory structure. It asserts successful execution and the existence of these generated files based on mock generation data.*


### test_agent_file_has_tool_registration (method, L279-L285, parent: TestCreateAgentFromDescription)

> *Summary: This test verifies that when creating a new agent from a description, the generated Python file correctly imports and registers necessary tools. It asserts the presence of specific tool registration lines within the output agent script.*


### test_name_override (method, L288-L293, parent: TestCreateAgentFromDescription)

> *Summary: This test verifies that providing a custom name during agent creation results in the generation of a file with that specific name. It invokes the `create` command, asserting successful execution and the existence of the corresponding Python file in the project directory.*


### test_agent_without_tools (method, L296-L303, parent: TestCreateAgentFromDescription)

> *Summary: This test verifies that an agent created without any specified tools results in a Python file lacking tool registration calls. It simulates the creation process by providing a configuration specifying no tools and asserts the resulting code's content accordingly.*


### test_creates_in_cwd_when_no_agents_dir (method, L306-L312, parent: TestCreateAgentFromDescription)

> *Summary: When no agents directory is specified, this test verifies that the CLI command creates a new agent file directly in the current working directory. It asserts successful execution and confirms the existence of the generated Python file based on the provided specification.*


### test_requires_name_without_from_description (method, L314-L317, parent: TestCreateAgentFromDescription)

> *Summary: This test verifies that the `create agent` command fails if a name is provided within the description field. It invokes the application with this input and asserts that the execution exits with a non-zero status code.*


### TestCreateToolFromModule (class, L325-L349)

> *Summary: These tests verify the CLI's ability to generate Python tool files from specified modules and functions. It checks successful creation with default or custom names, failure when the module doesn't exist, and required argument validation.*


### test_generates_tools_from_json_module (method, L326-L333, parent: TestCreateToolFromModule)

> *Summary: This test verifies that the CLI successfully generates a Python module containing specific functions when instructed to create tools from a JSON source. It asserts that the command exits cleanly and the resulting file contains the expected function definitions (`json_dumps` and `json_loads`).*


### test_generates_with_custom_name (method, L335-L339, parent: TestCreateToolFromModule)

> *Summary: When invoked with specific arguments, this test verifies that a new tool file is successfully created within the temporary project directory. It asserts successful execution and confirms the existence of the generated Python module named `my_json.py`.*


### test_fails_on_nonexistent_module (method, L341-L344, parent: TestCreateToolFromModule)

> *Summary: This test verifies that the application correctly fails when attempting to create a tool from a module that does not exist. It invokes the `create tool` command with an invalid module name and asserts that the execution exits with a non-zero status code.*


### test_requires_name_without_from_flags (method, L346-L349, parent: TestCreateToolFromModule)

> *Summary: When invoking the `create tool` command via the runner, this test asserts that the operation fails (non-zero exit code), implying a required name argument was missing or invalid based on flag constraints.*


### TestCreateToolFromOpenAPI (class, L357-L387)

> *Summary: This test suite verifies the functionality for creating tools from an OpenAPI specification provided via CLI arguments. It asserts that successful parsing and generation of tool definitions results in a zero exit code, while failures during spec loading correctly return a non-zero exit code with an appropriate error message.*


### test_generates_tools_from_openapi (method, L361-L379, parent: TestCreateToolFromOpenAPI)

> *Summary: When invoked with an OpenAPI URL, this test verifies that the CLI command successfully parses the specification and generates two specific tool specifications (`list_users` and `get_user`). It asserts a successful exit code and confirms that the generation function was called exactly once.*


### test_fails_on_bad_spec (method, L382-L387, parent: TestCreateToolFromOpenAPI)

> *Summary: This test verifies that the CLI correctly handles an invalid OpenAPI specification by asserting a non-zero exit code and checking for a specific failure message in the output when `mock_load` raises an exception. It simulates running the `create tool --from-openapi bad-url` command under these error conditions.*


### TestLLMConfigBugFix (class, L395-L459)

> *Summary: This test suite verifies a bug fix ensuring that `LLMConfig` is instantiated using dictionary arguments (`{...}`) instead of the `api_type` keyword argument across several modules. It achieves this by statically analyzing source code files and dynamically checking generated agent files for the presence of the forbidden keyword.*


### test_run_chat_uses_dict_config (method, L398-L415, parent: TestLLMConfigBugFix)

> *Summary: This test programmatically inspects `run.py` to verify that calls to `LLMConfig` do not use the `api_type` keyword argument. It parses the source code and asserts that no function call within the file contains this specific keyword.*


### test_discovery_uses_dict_config (method, L417-L433, parent: TestLLMConfigBugFix)

> *Summary: This test programmatically inspects `discovery.py` to ensure that calls to `LLMConfig` instantiation do not use the `api_type` keyword argument. It parses the source code and asserts that no function call within the file contains this specific keyword.*


### test_assertions_uses_dict_config (method, L435-L451, parent: TestLLMConfigBugFix)

> *Summary: This test dynamically parses `assertions.py` to verify that calls to `LLMConfig` do not use the `api_type` keyword argument. It asserts this by walking the Abstract Syntax Tree (AST) of the source file and checking the arguments of function calls.*


### test_scaffolded_agent_uses_dict_config (method, L453-L459, parent: TestLLMConfigBugFix)

> *Summary: Verifies that the scaffolding process generates agent files using a dictionary configuration for `LLMConfig` instead of keyword arguments. It runs a project creation command and asserts the resulting Python file contains the expected dictionary format while excluding any mention of `api_type`.*


### TestTestCmdChanges (class, L467-L515)

> *Summary: This test suite verifies CLI command behavior by asserting that the `--baseline` argument is rejected during evaluation and that specifying models triggers a "coming soon" warning message. It uses mocking to simulate application execution and capture output for validation.*


### test_baseline_param_removed (method, L470-L481, parent: TestTestCmdChanges)

> *Summary: This test verifies that the evaluation command rejects an unknown `--baseline` argument when invoked via `runner.invoke`. It asserts that the execution exits with a non-zero code, confirming the CLI correctly handles invalid options.*


### test_models_shows_coming_soon (method, L483-L515, parent: TestTestCmdChanges)

> *Summary: This test verifies that the CLI outputs a "coming soon" warning when invoking the `test eval` command with specific models listed via the `--models` flag. It mocks internal components to simulate a successful evaluation run and asserts the presence of the warning message in the final output.*

