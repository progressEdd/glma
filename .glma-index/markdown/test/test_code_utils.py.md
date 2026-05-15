# test/test_code_utils.py

18 function(s): test_infer_lang, test_extract_code, test_execute_code, test_execute_code_with_custom_filename_on_docker, test_execute_code_with_malformed_filename_on_docker, test_execute_code_raises_when_code_and_filename_are_both_none, test_execute_code_no_docker, test_execute_code_timeout_no_docker, get_current_autogen_env_var, restore_autogen_env_var and 8 more. 2 class(es): TestContentStr, TestGetPowerShellCommand. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_infer_lang | function |  |
| test_extract_code | function |  |
| test_execute_code | function |  |
| test_execute_code_with_custom_filename_on_docker | function |  |
| test_execute_code_with_malformed_filename_on_docker | function |  |
| test_execute_code_raises_when_code_and_filename_are_both_none | function |  |
| test_execute_code_no_docker | function |  |
| test_execute_code_timeout_no_docker | function |  |
| get_current_autogen_env_var | function |  |
| restore_autogen_env_var | function |  |
| test_decide_use_docker_truthy_values | function |  |
| test_decide_use_docker_falsy_values | function |  |
| test_decide_use_docker | function |  |
| test_decide_use_docker_with_env_var | function |  |
| test_decide_use_docker_with_env_var_and_argument | function |  |
| test_can_use_docker_or_throw | function |  |
| test_create_virtual_env | function |  |
| test_create_virtual_env_with_extra_args | function |  |
| TestContentStr | class |  |
| TestGetPowerShellCommand | class |  |

## Chunks

### test_infer_lang (function, L36-L42)

> *Summary: This test verifies the language inference utility by asserting correct outputs for known code snippets (e.g., Python and shell commands). It also confirms that invalid or non-code inputs correctly return an `UNKNOWN` status.*


### test_extract_code (function, L45-L171)

> *Summary: This test suite verifies the functionality of a function designed to parse markdown input, extracting all contained code blocks. It tests various scenarios including multi-block extraction, different languages, handling of indentation, line ending variations, and behavior when no code is present or when single-line detection is toggled.*


### test_execute_code (function, L176-L236)

> *Summary: This test verifies the `execute_code` utility by running various code snippets—including direct execution, file-based execution, and shell commands—to ensure correct output and behavior. It also tests error handling for assertions and timeouts when executing code within a temporary directory structure.*


### test_execute_code_with_custom_filename_on_docker (function, L241-L251)

> *Summary: This test verifies that code execution within a Docker container correctly uses a specified custom filename. It calls `execute_code` with Python script content, sets the filename to `"codetest.py"`, and asserts the successful execution output and the resulting image tag reflects this custom name.*


### test_execute_code_with_malformed_filename_on_docker (function, L259-L269)

> *Summary: This test verifies that the `execute_code` function correctly handles a filename containing special characters when running code inside a Docker container. It asserts that the execution succeeds and that the resulting image name incorporates the full, malformed input filename.*


### test_execute_code_raises_when_code_and_filename_are_both_none (function, L272-L274)

> *Summary: Asserts that calling `execute_code` with both `code` and `filename` set to `None` raises an `AssertionError`. This tests the function's input validation for missing required arguments.*


### test_execute_code_no_docker (function, L277-L278)

> *Summary: This test verifies the execution of code when Docker is explicitly disabled. It calls `test_execute_code` with a `use_docker=False` flag to ensure functionality without containerization overhead.*


### test_execute_code_timeout_no_docker (function, L281-L284)

> *Summary: This test verifies that executing code with a short timeout when Docker is disabled results in a timeout error. It asserts the execution returns a non-zero exit code and an error message indicating a timeout, while confirming no container image was generated.*


### get_current_autogen_env_var (function, L287-L288)

> *Summary: Retrieves the value of the `AUTOGEN_USE_DOCKER` environment variable from the system's environment. It returns this value or `None` if the variable is not set.*


### restore_autogen_env_var (function, L291-L295)

> *Summary: This function restores the `AUTOGEN_USE_DOCKER` environment variable based on an input value. If the provided value is `None`, it removes the variable; otherwise, it sets or updates the variable with the given value.*


### test_decide_use_docker_truthy_values (function, L298-L305)

> *Summary: This test verifies that the `decide_use_docker` function returns `True` when the environment variable `AUTOGEN_USE_DOCKER` is set to common truthy strings like "1", "true", "yes", or "t". It temporarily sets and then restores the original environment variable state during this check.*


### test_decide_use_docker_falsy_values (function, L308-L315)

> *Summary: This test verifies that when the `AUTOGEN_USE_DOCKER` environment variable is set to common falsy strings ("0", "false", "no", "f"), the `decide_use_docker` function correctly returns `False`. It temporarily modifies and then restores the environment variable state during execution.*


### test_decide_use_docker (function, L318-L327)

> *Summary: This test verifies the `decide_use_docker` function's behavior by manipulating the `AUTOGEN_USE_DOCKER` environment variable. It asserts that the function returns `None` when set to `"none"` and raises a `ValueError` when set to an invalid value like `"invalid"`.*


### test_decide_use_docker_with_env_var (function, L330-L343)

> *Summary: This test verifies the `decide_use_docker` logic by manipulating the `AUTOGEN_USE_DOCKER` environment variable. It asserts that the function correctly returns `False`, `True`, or `None` based on specific string values, and raises a `ValueError` for invalid inputs.*


### test_decide_use_docker_with_env_var_and_argument (function, L346-L358)

> *Summary: This test verifies the logic of `decide_use_docker` by manipulating the `AUTOGEN_USE_DOCKER` environment variable. It asserts that the function returns specific boolean values based on whether the environment variable is set to "false", "true", or other values like "none" or "invalid," while also testing with a provided argument.*


### test_can_use_docker_or_throw (function, L361-L367)

> *Summary: This test verifies the behavior of a function by calling it with various inputs, ensuring it handles `None` gracefully. It further asserts that if Docker is not running and the code isn't inside a container, attempting to use the function with `True` raises a `RuntimeError`.*


### test_create_virtual_env (function, L370-L374)

> *Summary: This test verifies that the `create_virtual_env` function successfully creates a virtual environment within a temporary directory. It asserts that the returned object is a `SimpleNamespace` containing the correct environment name derived from the temporary directory's path.*


### test_create_virtual_env_with_extra_args (function, L377-L381)

> *Summary: This test verifies that the `create_virtual_env` function correctly initializes a virtual environment within a temporary directory when explicitly disabling pip installation. It asserts that the returned context object is a `SimpleNamespace` and contains the expected environment name derived from the parent directory.*


### TestContentStr (class, L384-L529)

> *Summary: This test suite verifies the `content_str` function's ability to serialize various structured inputs into a readable string format. It handles simple text, mixed content types like images and patches, validates error conditions for invalid or malformed data, and correctly formats complex operations such as file creation, updating, and deletion via patch calls.*


### test_string_content (method, L385-L386, parent: TestContentStr)

> *Summary: Verifies that the `content_str` function correctly returns the exact input string when provided with a simple string argument.*


### test_list_of_text_content (method, L388-L390, parent: TestContentStr)

> *Summary: This test verifies that a list of text content dictionaries is correctly joined into a single string, specifically expecting each element to be separated by a newline character. It takes a list containing objects with a `"text"` key and asserts the resulting concatenated string matches the expected format.*


### test_mixed_content (method, L392-L394, parent: TestContentStr)

> *Summary: This test verifies that a mixed list of content objects, containing both text and image URLs, is correctly serialized into a string format. It asserts the output matches the expected concatenation of the text content followed by an image placeholder tag.*


### test_invalid_content (method, L396-L399, parent: TestContentStr)

> *Summary: Asserts that passing a list containing an element with an unrecognized type raises a `ValueError` when processed by the content serialization function. The input is a mixed-type list, and the expected output is an exception being raised.*


### test_empty_list (method, L401-L402, parent: TestContentStr)

> *Summary: Verifies that when an empty list is passed as input, the function returns an empty string. This confirms correct handling of zero-length inputs.*


### test_non_dict_in_list (method, L404-L407, parent: TestContentStr)

> *Summary: Asserts that passing a list containing non-dictionary elements to `content_str` raises a `TypeError`. This verifies the function's expected behavior when encountering mixed data types in its input list.*


### test_apply_patch_call_create_file (method, L409-L426, parent: TestContentStr)

> *Summary: This test verifies the serialization of an `apply_patch_call` structure containing a `create_file` operation. It takes a list describing the patch application and asserts that it correctly formats into a specific string representation including the file path, status, and diff content.*


### test_apply_patch_call_update_file (method, L428-L444, parent: TestContentStr)

> *Summary: This test verifies that the `apply_patch_call` structure correctly processes an `update_file` operation, asserting that the resulting string contains the file path, operation type, and completion status from the input data. It simulates applying a patch to modify a specific source file.*


### test_apply_patch_call_delete_file (method, L446-L459, parent: TestContentStr)

> *Summary: This test verifies the serialization of an `apply_patch_call` structure that executes a file deletion operation. It takes a list containing a patch call specifying `"delete_file"` for `"old_file.py"` and asserts the resulting string matches the expected format.*


### test_apply_patch_call_with_missing_fields (method, L461-L473, parent: TestContentStr)

> *Summary: When provided with a patch operation structure lacking specific fields, this test verifies that the resulting object defaults to "unknown" values for its operation, path, status, and difference. It confirms the expected string representation of this default state is produced.*


### test_apply_patch_call_with_partial_operation (method, L475-L491, parent: TestContentStr)

> *Summary: This test verifies the serialization of a patch call containing a partial operation that failed during execution. It asserts that the resulting string correctly includes the operation type, file path, failure status, and an indicator for unknown differences.*


### test_apply_patch_call_mixed_with_text (method, L493-L513, parent: TestContentStr)

> *Summary: This test verifies that a sequence containing both text segments and file creation patch operations is correctly serialized into a string representation. It asserts that all input components—the initial text, the patched file path, and the final text—are present in the resulting output string with specific newline formatting.*


### test_apply_patch_call_with_empty_diff (method, L515-L529, parent: TestContentStr)

> *Summary: This test verifies the serialization of an `apply_patch_call` operation when the associated difference string is empty. It asserts that the resulting string correctly represents a deletion action on "file.py" with a blank diff.*


### TestGetPowerShellCommand (class, L532-L560)

> *Summary: These tests verify the logic for determining the correct PowerShell executable by attempting to run both `powershell` and `pwsh`. It asserts that the function correctly returns `"powershell"` or `"pwsh"` upon successful execution, while also testing error handling for missing files (`FileNotFoundError`) or permission issues (`PermissionError`).*


### test_get_powershell_command_powershell (method, L534-L539, parent: TestGetPowerShellCommand)

> *Summary: When called, this test verifies that the `get_powershell_command` function correctly returns `"powershell"` by mocking subprocess execution to simulate a successful command retrieval. It asserts the output matches the expected string based on the mocked environment.*


### test_get_powershell_command_pwsh (method, L542-L548, parent: TestGetPowerShellCommand)

> *Summary: This test verifies that the function correctly identifies and returns `"pwsh"` when executing a PowerShell command via `pwsh`. It mocks subprocess execution to simulate successful retrieval of the value "7".*


### test_get_powershell_command_not_found (method, L551-L554, parent: TestGetPowerShellCommand)

> *Summary: This test verifies that calling `get_powershell_command()` raises a `FileNotFoundError` when the underlying subprocess execution fails with this specific exception. It achieves this by mocking `subprocess_run` to return `FileNotFoundError` twice.*


### test_get_powershell_command_no_permission (method, L557-L560, parent: TestGetPowerShellCommand)

> *Summary: This test verifies that calling `get_powershell_command()` raises a `PermissionError` when the underlying subprocess execution fails with both a `PermissionError` and a `FileNotFoundError`. It mocks the subprocess call to simulate these specific failure conditions.*

