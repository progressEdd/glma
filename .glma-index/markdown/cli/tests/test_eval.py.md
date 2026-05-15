# cli/tests/test_eval.py

10 class(es): TestLoadEvalSuite, TestContainsAssertion, TestContainsAllAssertion, TestContainsAnyAssertion, TestNotContainsAssertion, TestRegexAssertion, TestLengthAssertions, TestMaxTurnsAssertion, TestNoErrorAssertion, TestUnknownAssertion. 27 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLoadEvalSuite | class |  |
| TestContainsAssertion | class |  |
| TestContainsAllAssertion | class |  |
| TestContainsAnyAssertion | class |  |
| TestNotContainsAssertion | class |  |
| TestRegexAssertion | class |  |
| TestLengthAssertions | class |  |
| TestMaxTurnsAssertion | class |  |
| TestNoErrorAssertion | class |  |
| TestUnknownAssertion | class |  |

## Chunks

### TestLoadEvalSuite (class, L12-L48)

> *Summary: This test suite verifies the `load_eval_suite` function by providing various YAML files as input to check for correct parsing of suite metadata, individual test cases, and assertions. It also confirms that the loader correctly raises `FileNotFoundError` or `ValueError` when provided with missing or malformed YAML data.*


### test_loads_valid_yaml (method, L13-L17, parent: TestLoadEvalSuite)

> *Summary: This test verifies that a valid YAML file, passed as input, is correctly parsed into an evaluation suite object containing specific expected properties and case counts. It asserts the loaded suite's name, description, and the number of contained cases match predefined values.*


### test_first_case_parsed_correctly (method, L19-L26, parent: TestLoadEvalSuite)

> *Summary: This test verifies that the first evaluation case loaded from a YAML file is parsed correctly. It asserts specific properties of this initial case, including its name, input content, and the structure of its assertions.*


### test_second_case_parsed_correctly (method, L28-L32, parent: TestLoadEvalSuite)

> *Summary: This test verifies the correct parsing of a specific evaluation case from an input YAML file. It loads the suite, accesses the second case, and asserts that its name is "length\_test" and it contains exactly three assertions.*


### test_raises_on_missing_file (method, L34-L36, parent: TestLoadEvalSuite)

> *Summary: Asserts that attempting to load an evaluation suite from a non-existent file path raises a `FileNotFoundError`. It uses the provided temporary directory context to specify the missing input file.*


### test_raises_on_invalid_yaml (method, L38-L42, parent: TestLoadEvalSuite)

> *Summary: This test verifies that attempting to load a file containing invalid YAML content raises a `ValueError`. It achieves this by writing arbitrary text to a temporary file and calling the evaluation loading function.*


### test_empty_cases_list (method, L44-L48, parent: TestLoadEvalSuite)

> *Summary: When provided with a YAML file containing an empty list for the `cases` field, this test verifies that the loaded evaluation suite correctly reflects zero cases. It asserts that the resulting suite object has an empty case collection.*


### TestContainsAssertion (class, L51-L60)

> *Summary: This test suite verifies the behavior of a containment assertion by checking if `check_assertion` correctly returns `True` when the specified substring is present in the input text and `False` otherwise. It uses an `EvalAssertion` object configured for "contains" checks against sample strings.*


### test_passes_when_substring_present (method, L52-L55, parent: TestContainsAssertion)

> *Summary: This test verifies that an assertion checking for a specific substring passes when the target string contains it. It uses `EvalAssertion` with `"contains"` and checks the boolean result returned by `check_assertion`.*


### test_fails_when_substring_absent (method, L57-L60, parent: TestContainsAssertion)

> *Summary: This test verifies that an assertion checking for a substring ("Paris") fails when the target string ("The capital is London.") does not contain it. It asserts that the returned result object indicates failure.*


### TestContainsAllAssertion (class, L63-L72)

> *Summary: This test suite verifies the `contains_all` assertion logic by checking two scenarios: one where all specified values are present and the assertion passes, and another where at least one value is missing, causing the assertion to fail. It uses `EvalAssertion` objects as input for the `check_assertion` function.*


### test_passes_when_all_present (method, L64-L67, parent: TestContainsAllAssertion)

> *Summary: Verifies that an assertion configured to check for the presence of multiple specified values passes when all inputs are present. It calls `check_assertion` with a `"contains_all"` type assertion object and asserts the returned result indicates success.*


### test_fails_when_one_missing (method, L69-L72, parent: TestContainsAllAssertion)

> *Summary: When an assertion expects multiple items but only one is present in the input string, it correctly fails. The function takes a `contains_all` assertion object and checks its result against a provided text, asserting that the outcome is not passed.*


### TestContainsAnyAssertion (class, L75-L84)

> *Summary: This test suite verifies the `contains_any` assertion logic by checking if an input string matches any of the specified values. It confirms that the checker returns `True` when at least one value is present and `False` otherwise.*


### test_passes_when_one_present (method, L76-L79, parent: TestContainsAnyAssertion)

> *Summary: Given an `EvalAssertion` configured to check for the presence of any specified value within a string, this test verifies that the assertion correctly passes when the input string contains one of the target values. The function returns a result object indicating success if a match is found.*


### test_fails_when_none_present (method, L81-L84, parent: TestContainsAnyAssertion)

> *Summary: When checking an assertion expecting one of several values to be present in a string that contains none of them, the function correctly returns a failed result object. This test verifies that `check_assertion` returns `False` for the `passed` attribute when no matching value is found.*


### TestNotContainsAssertion (class, L87-L96)

> *Summary: This test suite verifies the behavior of a "not\_contains" assertion type. It confirms that `check_assertion` returns success when the specified substring is absent from the input text and failure when it is present.*


### test_passes_when_absent (method, L88-L91, parent: TestNotContainsAssertion)

> *Summary: Verifies that an assertion checking for the absence of a specific substring passes when the input string does not contain it. It calls `check_assertion` with a "not\_contains" type and asserts the returned result indicates success.*


### test_fails_when_present (method, L93-L96, parent: TestNotContainsAssertion)

> *Summary: When an assertion expecting a string *not* to contain "error" is run against the input "An error occurred.", the resulting evaluation object correctly indicates that the test failed.*


### TestRegexAssertion (class, L99-L113)

> *Summary: This test suite verifies the behavior of regex assertions by checking if `check_assertion` correctly determines success or failure based on pattern matching against input strings. It specifically tests cases where a match occurs, no match occurs, and when the assertion uses an input value as a fallback pattern.*


### test_passes_on_match (method, L100-L103, parent: TestRegexAssertion)

> *Summary: Verifies that an assertion using a regex pattern matching four digits passes when applied to the string "The year is 2026.". The function confirms the `passed` attribute of the result object is true.*


### test_fails_on_no_match (method, L105-L108, parent: TestRegexAssertion)

> *Summary: When checking a regex assertion against text containing no matches, the function correctly returns an evaluation result indicating failure. This test verifies that `check_assertion` yields `False` for the `passed` status when the pattern does not appear in the input string.*


### test_uses_value_as_fallback_pattern (method, L110-L113, parent: TestRegexAssertion)

> *Summary: This test verifies that a regex assertion correctly matches a string containing multiple spaces between words. It asserts the result of checking an `EvalAssertion` configured with a specific regular expression against a sample input string.*


### TestLengthAssertions (class, L116-L135)

> *Summary: These tests verify the behavior of length assertions by checking if a given string meets minimum or maximum length requirements defined in an `EvalAssertion`. It takes an assertion object and a string as input, returning a result indicating whether the condition passed or failed.*


### test_min_length_passes (method, L117-L120, parent: TestLengthAssertions)

> *Summary: Verifies that an assertion checking for a minimum string length of 5 passes when given the input "Hello World". The function confirms the `passed` status of the returned result object is true.*


### test_min_length_fails (method, L122-L125, parent: TestLengthAssertions)

> *Summary: This test verifies that an assertion requiring a minimum length of 100 fails when provided with the input string "Short". It asserts that the resulting evaluation object indicates failure.*


### test_max_length_passes (method, L127-L130, parent: TestLengthAssertions)

> *Summary: Verifies that an assertion checking for a maximum length of 100 passes when given the input string "Short text". The function confirms the `passed` status of the returned result object.*


### test_max_length_fails (method, L132-L135, parent: TestLengthAssertions)

> *Summary: Verifies that an assertion checking for a maximum length of 5 fails when provided with the string "This is too long". The function confirms the resulting evaluation object indicates failure.*


### TestMaxTurnsAssertion (class, L138-L152)

> *Summary: This test suite verifies the behavior of a maximum turn assertion by checking if an evaluation passes or fails based on a specified limit. It takes an `EvalAssertion` object defining the max turns and an output containing the actual number of turns, returning a result indicating success or failure.*


### test_passes_within_limit (method, L139-L142, parent: TestMaxTurnsAssertion)

> *Summary: Verifies that an evaluation assertion checking for a maximum turn limit passes when the actual output meets the specified constraint. It calls `check_assertion` with a defined `max_turns` value and asserts the returned result indicates success.*


### test_fails_over_limit (method, L144-L147, parent: TestMaxTurnsAssertion)

> *Summary: This test verifies that an evaluation assertion configured with a maximum turn limit of 2 fails when the actual output contains 5 turns. It calls `check_assertion` with the limit and checks if the returned result indicates failure.*


### test_exact_limit_passes (method, L149-L152, parent: TestMaxTurnsAssertion)

> *Summary: This test verifies that an assertion checking for a maximum turn limit passes when the actual output matches the specified limit exactly. It calls `check_assertion` with a `max_turns` assertion set to 3 and asserts the result indicates success.*


### TestNoErrorAssertion (class, L155-L164)

> *Summary: This test suite verifies the behavior of a "no\_error" assertion type when checking results. It confirms that the assertion passes if no errors are provided and fails if any errors are present in the input list.*


### test_passes_with_no_errors (method, L156-L159, parent: TestNoErrorAssertion)

> *Summary: Verifies that the `check_assertion` function correctly reports success when provided with an assertion expecting no errors and an empty list of actual errors. It confirms the returned result object indicates a passed state.*


### test_fails_with_errors (method, L161-L164, parent: TestNoErrorAssertion)

> *Summary: When provided an assertion expecting no errors but given a list of errors, the function returns a result indicating failure. This test verifies that `check_assertion` correctly flags a mismatch between expected and actual error states.*


### TestUnknownAssertion (class, L167-L172)

> *Summary: This test verifies that the `check_assertion` function correctly handles an unknown assertion type provided to it. It asserts that the resulting result indicates failure and contains a specific error message about the unknown type.*


### test_unknown_type_fails (method, L168-L172, parent: TestUnknownAssertion)

> *Summary: This test verifies that the system correctly fails when an `EvalAssertion` is provided with an unrecognized type. It asserts that the resulting check returns a failure status and includes a specific error message indicating an unknown assertion type.*

