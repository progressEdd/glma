# cli/tests/test_discovery.py

3 class(es): TestImportAgentFile, TestDiscover, TestLoadYamlConfig. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestImportAgentFile | class |  |
| TestDiscover | class |  |
| TestLoadYamlConfig | class |  |

## Chunks

### TestImportAgentFile (class, L16-L42)

> *Summary: This test suite verifies the `import_agent_file` function's behavior when processing Python files. It asserts correct loading of valid modules, handles missing or non-Python file inputs by raising appropriate exceptions, and confirms that imported agents can successfully import sibling modules within the same directory.*


### test_imports_valid_python_file (method, L17-L20, parent: TestImportAgentFile)

> *Summary: Verifies that a provided Python file, when imported, contains an accessible and callable `main` attribute. It takes a path to a valid agent file as input and asserts the structure of the resulting module object.*


### test_raises_on_missing_file (method, L22-L24, parent: TestImportAgentFile)

> *Summary: Asserts that attempting to import a file specified by a path that does not exist raises a `FileNotFoundError`. It uses the provided temporary directory context to test this failure condition.*


### test_raises_on_non_python_file (method, L26-L30, parent: TestImportAgentFile)

> *Summary: Asserts that attempting to import a non-Python file (like `test.txt`) using the agent function raises a `ValueError` with a specific message. It tests the input validation mechanism for file types.*


### test_module_can_import_sibling (method, L32-L42, parent: TestImportAgentFile)

> *Summary: This test verifies that a Python module can successfully import and use variables from its sibling file within the same directory. It creates two files, imports one, and asserts that the imported module correctly accesses data defined in the other.*


### TestDiscover (class, L45-L121)

> *Summary: This test suite verifies the `discover` function's ability to parse Python files, correctly identifying and extracting different structures like a primary entry point (`main`), single agents, lists of agents, or team variables based on file content. It asserts expected outcomes for various inputs, including handling empty files by raising an error and prioritizing main functions over agent definitions.*


### test_discovers_main_function (method, L46-L50, parent: TestDiscover)

> *Summary: This test verifies that the `discover` function correctly identifies and extracts the main entry point from a provided agent file path. It asserts that the discovered item's kind is "main" and that its associated function object is present and callable.*


### test_discovers_agent_variable (method, L52-L57, parent: TestDiscover)

> *Summary: This test verifies that the `discover` function correctly identifies an agent variable from a provided file path. It asserts that the discovered object is of type "agent," contains a non-null agent, and matches expected names like "researcher."*


### test_discovers_agents_list (method, L59-L63, parent: TestDiscover)

> *Summary: This test verifies that the `discover` function correctly parses a file containing an agents list, asserting the resulting object is of type "agents," contains exactly two agents, and lists their names as "alice" and "bob."*


### test_raises_on_empty_file (method, L65-L67, parent: TestDiscover)

> *Summary: Asserts that calling `discover` with an empty file path raises a `ValueError` containing the message "No runnable agent found." This verifies correct error handling when no agents can be detected in the provided input.*


### test_discovers_team_variable (method, L69-L84, parent: TestDiscover)

> *Summary: This test verifies that the `discover` function correctly identifies and extracts a specific variable from a Python file. It writes a temporary file containing an agent definition and asserts that the returned discovery object is of type "agent" with the expected name.*


### test_discovers_single_agent_instance (method, L86-L102, parent: TestDiscover)

> *Summary: This test verifies that the discovery mechanism can find an agent instance when no standard naming conventions are present. It writes a file containing a custom `FakeAgent` object and asserts that the resulting discovery correctly identifies it as an "agent" with the expected name.*


### test_main_takes_priority_over_agent (method, L104-L121, parent: TestDiscover)

> *Summary: This test verifies that the discovery mechanism prioritizes a `main` function over an agent class when analyzing a provided Python file. It achieves this by writing a temporary file containing both a fake agent and a main function, then asserting the discovered kind is `"main"`.*


### TestLoadYamlConfig (class, L124-L139)

> *Summary: This test suite verifies the `load_yaml_config` function by asserting correct parsing of valid YAML inputs, ensuring it raises `FileNotFoundError` for missing files, and confirming it throws a `ValueError` when provided with malformed YAML content.*


### test_loads_valid_yaml (method, L125-L129, parent: TestLoadYamlConfig)

> *Summary: This test verifies that a valid YAML configuration file is correctly parsed by loading it. It asserts specific values within the resulting dictionary, checking for a predefined LLM model and the presence of two agents with expected names.*


### test_raises_on_missing_file (method, L131-L133, parent: TestLoadYamlConfig)

> *Summary: Asserts that attempting to load a YAML configuration from a non-existent file path raises a `FileNotFoundError`. It uses the provided temporary directory context to specify the missing input file.*


### test_raises_on_invalid_yaml (method, L135-L139, parent: TestLoadYamlConfig)

> *Summary: Asserts that attempting to load a YAML file containing an invalid structure (a sequence instead of a mapping) raises a `ValueError` with the expected message. It takes a temporary path and writes malformed content to test the loading function's error handling.*

