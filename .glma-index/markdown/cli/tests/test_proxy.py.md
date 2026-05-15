# cli/tests/test_proxy.py

3 function(s): openapi_spec_file, scripts_dir, _make_help_result. 12 class(es): TestToolSpec, TestTypeMapping, TestParseCLI, TestParseCLIHelpText, TestParseOpenAPI, TestInspectModule, TestWrapScripts, TestGenerateToolFile, TestProxyCLI, TestProxyOpenAPI, TestProxyModule, TestProxyScripts. 39 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| openapi_spec_file | function |  |
| scripts_dir | function |  |
| TestToolSpec | class |  |
| TestTypeMapping | class |  |
| TestParseCLI | class |  |
| _make_help_result | function |  |
| TestParseCLIHelpText | class |  |
| TestParseOpenAPI | class |  |
| TestInspectModule | class |  |
| TestWrapScripts | class |  |
| TestGenerateToolFile | class |  |
| TestProxyCLI | class |  |
| TestProxyOpenAPI | class |  |
| TestProxyModule | class |  |
| TestProxyScripts | class |  |

## Chunks

### openapi_spec_file (function, L35-L99)

> *Summary: Generates a minimal OpenAPI 3.0 specification dictionary and saves it as `openapi.json` within the provided temporary path. It returns the full `Path` object pointing to the newly created spec file.*


### scripts_dir (function, L103-L112)

> *Summary: Creates and populates a directory named "scripts" within the provided temporary path. It writes sample shell scripts (`deploy.sh`) and Python scripts (`check.py`), setting appropriate executable permissions, and returns the path to this new directory.*


### TestToolSpec (class, L120-L136)

> *Summary: Verifies the `ToolSpec` object's initialization by testing basic creation with no parameters and a more complex case including multiple defined parameters with specific types and defaults. It ensures that the name, description, and parameter list are correctly set upon instantiation.*


### test_basic_creation (method, L121-L124, parent: TestToolSpec)

> *Summary: Verifies that a newly created `ToolSpec` object correctly initializes with the provided name and an empty list of parameters. It asserts the internal state matches the input values during basic instantiation.*


### test_with_params (method, L126-L136, parent: TestToolSpec)

> *Summary: This test verifies the construction of a `ToolSpec` object by asserting that it correctly includes two parameters: one string query and one optional integer limit with a default value of 10. It confirms the structure and default settings of the defined tool specification.*


### TestTypeMapping (class, L144-L157)

> *Summary: This test suite verifies the mapping logic between OpenAPI type definitions and corresponding Python types. It asserts correct conversions for various OpenAPI types (like "string" to "str") and tests a fallback mechanism when an unknown or empty input is provided.*


### test_openapi_types (method, L145-L152, parent: TestTypeMapping)

> *Summary: Verifies that a helper function correctly maps OpenAPI type definitions (like `"string"` or `"integer"`) to their corresponding Python types. It also asserts a default return value of `"str"` when no type information is provided in the input dictionary.*


### test_python_type (method, L154-L157, parent: TestTypeMapping)

> *Summary: Verifies that a helper function correctly maps string representations of Python types to their actual type names. It asserts expected outputs for known types like "str" and "int", and confirms a default return value ("str") for unrecognized inputs.*


### TestParseCLI (class, L165-L176)

> *Summary: This test suite verifies that the CLI parsing utility correctly interprets help requests for both simple commands (like `echo`) and nested subcommands (like `git status`). It asserts that the resulting specification object accurately reflects the command name and its source type as coming from the CLI.*


### test_parses_echo_help (method, L166-L170, parent: TestParseCLI)

> *Summary: This test verifies that the CLI parser correctly processes the help command for the `echo` utility. It asserts that the resulting specification object identifies the source as "cli" and names it "echo".*


### test_parses_subcommand (method, L172-L176, parent: TestParseCLI)

> *Summary: This test verifies that the CLI help parsing mechanism correctly identifies and includes both a main command ("git") and its subcommand ("status") within the parsed specification object, confirming the source type is "cli".*


### _make_help_result (function, L179-L181)

> *Summary: Constructs a mock `subprocess.CompletedProcess` object using provided standard output. This helper simulates the successful execution of an external command for testing purposes.*


### TestParseCLIHelpText (class, L184-L341)

> *Summary: This test suite validates the logic for parsing command-line help text, accepting a raw string as input and producing a structured `ToolSpec` object containing descriptions and parameters. It rigorously checks edge cases such as stripping man-page formatting, handling invalid parameter names (like digits or keywords), deduplicating entries, and ensuring the resulting specification can generate valid Python code.*


### _parse (method, L187-L189, parent: TestParseCLIHelpText)

> *Summary: This method simulates parsing command-line help text by patching the subprocess execution to return a predefined result based on the input `help_text`. It then calls an internal parser function with a fixed command name, returning a `ToolSpec` object.*


### test_strips_man_page_overstrike (method, L193-L205, parent: TestParseCLIHelpText)

> *Summary: This test verifies that the parser correctly extracts documentation from a mock man page string. It asserts that the description matches and that a specific option, `--verbose`, is present among the parsed parameters.*


### test_description_from_name_section (method, L209-L220, parent: TestParseCLIHelpText)

> *Summary: This test verifies that the parser correctly extracts the description from the `NAME` section of a provided man page string. It asserts that the parsed specification object's `description` attribute matches the expected text found in the input help content.*


### test_description_skips_man_header (method, L222-L226, parent: TestParseCLIHelpText)

> *Summary: When parsing help text containing a manual page header, this test asserts that the resulting parsed description does not include the initial header line. It verifies that only the actual descriptive content is extracted from the input string.*


### test_description_fallback (method, L228-L231, parent: TestParseCLIHelpText)

> *Summary: When provided with a specific help text string, this test verifies that the parsing mechanism correctly assigns a default description ("Run fakecmd") to the resulting specification object. It confirms the fallback behavior for the command's description field.*


### test_skips_empty_param_from_decorative_dashes (method, L235-L246, parent: TestParseCLIHelpText)

> *Summary: This test verifies that the parser correctly ignores empty parameters when they appear between decorative lines in help text. It asserts that only named parameters, like "verbose," are included in the parsed specification's parameter list.*


### test_skips_params_starting_with_digit (method, L248-L257, parent: TestParseCLIHelpText)

> *Summary: This test verifies that the parser correctly ignores parameters whose names begin with a digit, even if they are present in the provided help text. It asserts that only parameter names starting with non-digit characters are included in the parsed specification.*


### test_skips_python_keywords (method, L259-L275, parent: TestParseCLIHelpText)

> *Summary: This test verifies that the parser correctly ignores Python reserved keywords when processing command-line help text. It asserts that specific keywords like "not," "return," and "class" are excluded from the list of recognized parameter names derived from the input string.*


### test_deduplicates_params (method, L279-L296, parent: TestParseCLIHelpText)

> *Summary: This test verifies that a parameter parsing mechanism correctly deduplicates options from help text, ensuring only one instance of each unique flag like `--verbose` is registered. It takes formatted help string input and asserts the resulting list of parameter names contains the expected set of unique flags.*


### test_generated_code_is_valid_python (method, L300-L329, parent: TestParseCLIHelpText)

> *Summary: This test verifies that the code generated from parsed CLI help text is syntactically valid Python. It feeds complex, tricky help strings into a parsing function and then asserts that the resulting generated file contains expected elements while excluding keywords or invalid identifiers as parameters.*


### test_string_params_generated_correctly (method, L331-L341, parent: TestParseCLIHelpText)

> *Summary: This test verifies that string and boolean parameters are correctly parsed from a provided help text specification. It asserts the expected types (`str` for output, `bool` for verbose) and default values (`None` and `False`, respectively) for specific named arguments.*


### TestParseOpenAPI (class, L349-L383)

> *Summary: These tests verify the `_parse_openapi_spec` function by feeding it OpenAPI specification JSON files. They assert that the resulting list of tools contains expected functions (like "list\_users", "create\_user"), validates specific parameters for those tools, and correctly handles empty specifications.*


### test_parses_spec (method, L350-L357, parent: TestParseOpenAPI)

> *Summary: This test validates that a given OpenAPI specification file successfully parses into at least three defined tools, specifically asserting the presence of `list_users`, `create_user`, and `get_user` functions within those parsed tools. It takes a file path as input and asserts the structure and content of the resulting tool list.*


### test_list_users_tool (method, L359-L365, parent: TestParseOpenAPI)

> *Summary: This test verifies the structure of a `list_users` tool extracted from an OpenAPI specification file. It asserts that the tool has the correct description, includes a 'limit' parameter, and originates from the OpenAPI source type.*


### test_path_params (method, L367-L371, parent: TestParseOpenAPI)

> *Summary: This test verifies that the parsed OpenAPI specification contains a path parameter named `user_id` within the definition for the `get_user` tool. It achieves this by loading the spec, parsing it into tools, and asserting the presence of the specific parameter on the target tool.*


### test_request_body_params (method, L373-L379, parent: TestParseOpenAPI)

> *Summary: This test verifies that the `create_user` tool, parsed from an OpenAPI specification file, correctly includes required parameters named "name" and "email". It achieves this by loading the spec, extracting tools, and asserting the presence of these specific parameter names.*


### test_empty_spec (method, L381-L383, parent: TestParseOpenAPI)

> *Summary: When provided with an OpenAPI specification containing no paths, the function returns an empty list of tools. This test verifies that parsing an empty path structure results in zero available tools.*


### TestInspectModule (class, L391-L411)

> *Summary: These tests verify the functionality of a module inspection utility, `_inspect_module_functions`, which takes a module name and optional function names as input. It asserts that the returned list contains expected functions (like `json_dumps` and `json_loads`), respects filtering criteria, checks for parameter presence, and correctly skips private members.*


### test_inspect_json_module (method, L392-L397, parent: TestInspectModule)

> *Summary: Verifies that the `_inspect_module_functions` utility correctly finds and returns functions named `json_dumps` and `json_loads` when inspecting the standard `json` module. It asserts that exactly two such functions are found.*


### test_inspect_with_filter (method, L399-L402, parent: TestInspectModule)

> *Summary: This test verifies that a function correctly filters module functions, expecting only one result named "json\_dumps" when inspecting the "json" module for functions matching the name "dumps". It asserts the length and specific name of the returned list of tools.*


### test_inspect_has_params (method, L404-L406, parent: TestInspectModule)

> *Summary: Verifies that the function returned by inspecting a module contains parameters. It checks if the `params` attribute of the first tool object retrieved from the "json" module's "dumps" function is non-empty.*


### test_inspect_skips_private (method, L408-L411, parent: TestInspectModule)

> *Summary: Verifies that the module inspection function, when run on "json", excludes functions whose names begin with an underscore, specifically checking for private members prefixed with `_`. It asserts that no such private functions are present in the resulting set of tool names.*


### TestWrapScripts (class, L419-L431)

> *Summary: Verifies that a script wrapping utility correctly identifies and includes specific executable scripts (like "deploy" and "check") from a given directory while excluding non-executable files. It also asserts that every resulting wrapped tool possesses an argument parameter named "args".*


### test_wraps_executable_scripts (method, L420-L426, parent: TestWrapScripts)

> *Summary: This test verifies that a script wrapping function correctly identifies and includes specific executables from a given directory while excluding non-executable files like text documents. It asserts the presence of expected scripts ("deploy", "check") and the absence of others ("readme").*


### test_script_tool_has_args_param (method, L428-L431, parent: TestWrapScripts)

> *Summary: This test verifies that every script tool loaded from the specified directory possesses a parameter named "args". It iterates through all discovered tools and asserts the presence of this specific parameter name within each tool's parameters list.*


### TestGenerateToolFile (class, L439-L477)

> *Summary: This test suite verifies that a function correctly generates Python code files from provided tool specifications. It asserts that the generated file contains correct function signatures, parameter types (including optional ones), and descriptions based on the input `ToolSpec` list.*


### test_generates_valid_python (method, L440-L459, parent: TestGenerateToolFile)

> *Summary: This test verifies that the tool generation utility correctly creates a Python file containing a function definition. It asserts that the generated code includes the correct function signature, parameter types, default values, and description based on the provided `ToolSpec` list.*


### test_generates_optional_params (method, L461-L477, parent: TestGenerateToolFile)

> *Summary: This test verifies that the tool generation utility correctly creates Python function signatures for tools with optional parameters. It asserts that the generated code includes default values (`None` and `False`) corresponding to the defined optional arguments.*


### TestProxyCLI (class, L485-L505)

> *Summary: These tests verify the command-line interface functionality for a proxy tool. They assert that running commands like `proxy cli echo --preview` executes successfully and produces expected output, and also test complex subcommand invocation with file outputs.*


### test_cli_preview (method, L486-L489, parent: TestProxyCLI)

> *Summary: Invokes the application with a specific command to test preview functionality. It asserts that the execution succeeds (exit code 0) and that the output contains the string "echo".*


### test_cli_with_subcommands (method, L491-L505, parent: TestProxyCLI)

> *Summary: Invokes the CLI application with a nested command structure (`proxy cli git --subcommands status`) and an output file path as input. It asserts that the execution completes successfully (exit code 0) and that the specified output file is created.*


### TestProxyOpenAPI (class, L508-L543)

> *Summary: These tests verify the functionality of an OpenAPI proxy command-line interface by invoking it with various inputs. They assert successful execution, check for expected output strings (like endpoint definitions), and confirm file generation based on specified parameters such as preview mode or endpoint filtering.*


### test_openapi_preview (method, L509-L512, parent: TestProxyOpenAPI)

> *Summary: Invokes the proxy command with an OpenAPI specification file and a `--preview` flag. It asserts that the execution succeeds (exit code 0) and that the output contains the string "list\_users".*


### test_openapi_generates_file (method, L514-L524, parent: TestProxyOpenAPI)

> *Summary: This test verifies that running the `proxy openapi` command with a specification file successfully generates an API client Python file. It asserts that the process exits cleanly, the output file exists, and contains expected function definitions like `list_users`.*


### test_openapi_filter_endpoints (method, L526-L543, parent: TestProxyOpenAPI)

> *Summary: This test verifies that a proxy command correctly filters OpenAPI endpoints based on provided arguments. It invokes the `proxy openapi` command with a specification file and a specific endpoint name, asserting that the resulting output file contains only the requested function definition while excluding others.*


### TestProxyModule (class, L546-L571)

> *Summary: This test suite verifies the functionality of a proxy module by invoking it with specific arguments to check for successful execution and expected output content. It tests both generating preview information and creating an output file containing generated code based on specified functions.*


### test_module_preview (method, L547-L554, parent: TestProxyModule)

> *Summary: Invokes the application with specific arguments to generate a module preview for JSON functions, asserting that the command executes successfully and the output contains references to both `json_dumps` and `json_loads`.*


### test_module_generates_file (method, L556-L571, parent: TestProxyModule)

> *Summary: This test verifies that a specific command invocation successfully generates a Python file named `json_tools.py` at the provided temporary path. It asserts both that the process exited cleanly and that the target output file was created.*


### TestProxyScripts (class, L574-L587)

> *Summary: Verifies that the proxy scripts command successfully runs a preview and includes "deploy" in its output when given a directory path. It also confirms that running the script generation command with an output path creates the specified file.*


### test_scripts_preview (method, L575-L578, parent: TestProxyScripts)

> *Summary: Invokes the application's proxy command with a specified directory and `--preview` flag. It asserts that the execution succeeds (exit code 0) and that the output contains the string "deploy".*


### test_scripts_generates_file (method, L580-L587, parent: TestProxyScripts)

> *Summary: This test verifies that a specific command successfully generates an output file. It invokes the application with arguments specifying an input directory and an output path, asserting both a successful exit code and the existence of the generated file.*

