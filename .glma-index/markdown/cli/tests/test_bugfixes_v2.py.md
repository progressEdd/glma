# cli/tests/test_bugfixes_v2.py

5 class(es): TestProxyScriptEscaping, TestFrontmatterQuoteEscaping, TestEvalYamlErrorHandling, TestAssertionNumericValidation, TestSharedModules. 21 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestProxyScriptEscaping | class |  |
| TestFrontmatterQuoteEscaping | class |  |
| TestEvalYamlErrorHandling | class |  |
| TestAssertionNumericValidation | class |  |
| TestSharedModules | class |  |

## Chunks

### TestProxyScriptEscaping (class, L20-L61)

> *Summary: This test suite verifies that script paths containing special characters (like quotes or backslashes) are safely escaped when processed by `_wrap_scripts`. It asserts that the generated implementation code remains valid Python syntax after handling these problematic path inputs.*


### test_script_path_with_double_quotes_escaped (method, L23-L42, parent: TestProxyScriptEscaping)

> *Summary: This test verifies that when a script path contains double quotes, the wrapping mechanism correctly handles escaping so that the resulting implementation string remains valid Python code. It asserts that the generated implementation does not contain unescaped quotes while still including the quoted filename within it.*


### test_script_path_with_backslash_escaped (method, L44-L61, parent: TestProxyScriptEscaping)

> *Summary: This test verifies that script paths containing backslashes are correctly processed by the `_wrap_scripts` utility. It creates a sample shell script in a temporary directory and asserts that the resulting wrapped code compiles successfully as valid Python.*


### TestFrontmatterQuoteEscaping (class, L69-L88)

> *Summary: This test suite verifies that double quotes and backslashes within string values are correctly escaped when formatting YAML frontmatter. It uses the `format_frontmatter` utility to ensure proper escaping for inputs like `"She said "hello""` and `"C:\\Users\\test"`.*


### test_value_with_double_quotes_escaped (method, L72-L76, parent: TestFrontmatterQuoteEscaping)

> *Summary: This test verifies that the `format_frontmatter` function correctly escapes double quotes within a description field. It asserts that the resulting string contains the properly escaped sequence `"hello"` when given an input dictionary with `'desc': 'She said "hello"'`.*


### test_value_with_backslash_escaped (method, L78-L82, parent: TestFrontmatterQuoteEscaping)

> *Summary: This test verifies that the `format_frontmatter` function correctly escapes backslashes within a provided path string. It asserts that an input path containing single backslashes is transformed into one with double backslashes in the output.*


### test_plain_value_unchanged (method, L84-L88, parent: TestFrontmatterQuoteEscaping)

> *Summary: This test verifies that a simple key-value pair remains correctly formatted when processed by the `format_frontmatter` utility. It asserts that the input dictionary's content is preserved within the resulting string output.*


### TestEvalYamlErrorHandling (class, L96-L119)

> *Summary: This test suite verifies that parsing functions correctly raise `ValueError` when essential fields are missing from input YAML structures, such as assertions or cases. It confirms proper error handling for incomplete data while also validating successful parsing of a complete case structure.*


### test_assertion_missing_type_raises_valueerror (method, L99-L101, parent: TestEvalYamlErrorHandling)

> *Summary: This test verifies that attempting to parse an assertion dictionary lacking a required `'type'` field correctly raises a `ValueError` with a specific error message. It uses `pytest.raises` to assert this expected exception behavior when passing incomplete input data.*


### test_case_missing_name_raises_valueerror (method, L103-L105, parent: TestEvalYamlErrorHandling)

> *Summary: This test asserts that attempting to parse a case dictionary lacking the required 'name' field raises a `ValueError` with a specific error message. It verifies the input validation logic of the parsing function.*


### test_case_missing_input_raises_valueerror (method, L107-L109, parent: TestEvalYamlErrorHandling)

> *Summary: Asserts that attempting to parse a case object without the required 'input' field raises a `ValueError` with a specific message. This verifies input validation for the parsing utility.*


### test_valid_case_works (method, L111-L119, parent: TestEvalYamlErrorHandling)

> *Summary: This test verifies that the `_parse_case` function correctly processes a valid input structure, ensuring the resulting object accurately reflects the provided name, input string, and assertion count. It confirms successful parsing of a sample case definition.*


### TestAssertionNumericValidation (class, L127-L162)

> *Summary: This test suite verifies that assertion checks for `min_length`, `max_length`, and `max_turns` correctly fail when provided with non-numeric inputs like `None` or strings. It also confirms that the assertions function as expected when valid integer values are supplied.*


### test_min_length_with_none_value (method, L130-L134, parent: TestAssertionNumericValidation)

> *Summary: When checking a minimum length assertion configured with `None` against the string "some output," the function correctly fails and reports an "Invalid min\_length" error message. This verifies that `None` as a value for this specific assertion type is handled as invalid input.*


### test_min_length_with_string_value (method, L136-L140, parent: TestAssertionNumericValidation)

> *Summary: Verifies that an assertion expecting a minimum length on a string input fails correctly when the expected value is non-numeric. It confirms the failure status and checks for a specific error message indicating invalid input type.*


### test_max_length_with_none_value (method, L142-L146, parent: TestAssertionNumericValidation)

> *Summary: Verifies that an assertion checking for a maximum length when the expected value is `None` correctly fails. It confirms the failure message contains "Invalid max\_length".*


### test_max_turns_with_string_value (method, L148-L152, parent: TestAssertionNumericValidation)

> *Summary: When checking a `max_turns` assertion with a string input instead of an integer, the function correctly fails and reports an "Invalid max\_turns" error message. This verifies that non-numeric values are rejected for turn limits.*


### test_min_length_with_valid_int_still_works (method, L154-L157, parent: TestAssertionNumericValidation)

> *Summary: Verifies that the minimum length assertion correctly passes when provided a string longer than the specified threshold. It calls `check_assertion` with an `EvalAssertion` set to 5 and the input string "hello world", asserting the result indicates success.*


### test_max_turns_with_valid_int_still_works (method, L159-L162, parent: TestAssertionNumericValidation)

> *Summary: Verifies that the system correctly handles a maximum turn assertion of 10 when the actual output provides only 5 turns. It confirms the assertion passes under these conditions.*


### TestSharedModules (class, L170-L230)

> *Summary: This test suite verifies the functionality of shared modules by testing `CaseResult` calculations for various pass/fail scenarios, ensuring cost extraction from dictionaries works correctly with valid and invalid inputs, and confirming that a tree copying utility successfully replicates file structures.*


### test_case_result_importable_from_testing (method, L173-L183, parent: TestSharedModules)

> *Summary: This test verifies that a `CaseResult` object, instantiated with mock evaluation and assertion data, correctly reports its status. It asserts that the resulting object indicates success (`passed=True`) and has a score of $1.0$ based on one passed assertion out of one total.*


### test_case_result_score_with_partial_pass (method, L185-L196, parent: TestSharedModules)

> *Summary: Given a `CaseResult` object containing mixed assertion outcomes (some passed, some failed), this test verifies that the overall result is marked as not passed and assigns a score of 0.5.*


### test_extract_cost_with_valid_dict (method, L198-L202, parent: TestSharedModules)

> *Summary: This test verifies that the `extract_cost` function correctly retrieves a specific cost value from an input dictionary structure. It asserts that passing a dictionary containing `"usage_excluding_cached_inference"` with a total cost of $0.05 results in the function returning exactly $0.05$.*


### test_extract_cost_with_empty_dict (method, L204-L207, parent: TestSharedModules)

> *Summary: Verifies that the `extract_cost` function correctly returns $0.0$ when provided with an empty dictionary as input. This test ensures proper handling of zero-value scenarios during cost extraction.*


### test_extract_cost_with_non_dict (method, L209-L213, parent: TestSharedModules)

> *Summary: Verifies that the `extract_cost` function gracefully handles non-dictionary inputs, such as strings and `None`, by returning a default value of $0.0$. This test ensures robustness when unexpected data types are passed to the cost extraction logic.*


### test_copy_tree_copies_files (method, L215-L230, parent: TestSharedModules)

> *Summary: This test verifies that the `copy_tree` utility correctly replicates a source directory structure, including all files and subdirectories. It asserts that both individual file contents are preserved in the destination path after copying.*

