# cli/tests/test_test_cmd.py

2 function(s): _fake_autogen, _make_case_result. 3 class(es): TestTestEval, TestTestBench, TestCaseResult. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _fake_autogen | function |  |
| _make_case_result | function |  |
| TestTestEval | class |  |
| TestTestBench | class |  |
| TestCaseResult | class |  |

## Chunks

### _fake_autogen (function, L26-L29)

> *Summary: This helper function temporarily mocks the `autogen` module within `sys.modules` to ensure that importing it succeeds during tests for the `test_eval` command. It yields once to allow the test execution to proceed with the mocked dependency in place.*


### _make_case_result (function, L32-L46)

> *Summary: Constructs a `CaseResult` object by packaging an evaluation case, its output string, a list of assertion outcomes, and optional timing/turn metadata. This helper function provides a standardized way to create test results for internal use.*


### TestTestEval (class, L49-L268)

> *Summary: This test suite verifies the behavior of the `ag2 test eval` subcommand by simulating various execution scenarios. It checks that dry-run mode reports counts without running tests, validates JSON output structure when requested, and correctly sets exit codes (0 for all passing, 1 if any assertion fails).*


### test_dry_run_shows_cases_without_running (method, L52-L81, parent: TestTestEval)

> *Summary: This test verifies that when the `--dry-run` flag is used with the `test eval` command, the CLI exits successfully (code 0) and displays summary counts without executing any actual test cases. It asserts that the core execution function remains uncalled during this dry run mode.*


### test_json_output_is_valid_json (method, L83-L155, parent: TestTestEval)

> *Summary: This test verifies that running the `test` command with JSON output produces a valid, structured JSON array. It mocks case execution results and asserts that the captured standard output contains a list containing one suite with two specific test cases, confirming correct serialization.*


### test_exits_1_when_assertions_fail (method, L157-L214, parent: TestTestEval)

> *Summary: This test verifies that the command exits with code 1 if any evaluation assertion fails across multiple cases. It simulates a scenario where one case fails an assertion while another passes, asserting the overall process returns a non-zero exit code.*


### test_exits_0_when_all_assertions_pass (method, L216-L268, parent: TestTestEval)

> *Summary: This test verifies that the CLI exits with code 0 when all defined evaluation cases pass their assertions. It mocks the case runner to return successful results for two predefined test scenarios before invoking the main `test eval` command.*


### TestTestBench (class, L271-L282)

> *Summary: Verifies that invoking the `test bench` subcommand with specific arguments results in an exit code of zero and outputs the string "coming soon". This test confirms the expected behavior for the unimplemented benchmarking feature.*


### test_bench_shows_coming_soon (method, L274-L282, parent: TestTestBench)

> *Summary: This test verifies that invoking the `test bench` subcommand with specific arguments results in an exit code of zero and prints the string "coming soon" to standard output. It uses a runner object to execute the application command line interface.*


### TestCaseResult (class, L285-L324)

> *Summary: These tests verify the `CaseResult` structure by instantiating it with various sets of assertion results. It confirms that the overall `passed` status is determined by any failing assertions, and validates that `passed_count` and `total_count` accurately reflect the number of successful and total assertions provided.*


### test_passed_returns_true_when_all_assertions_pass (method, L288-L298, parent: TestCaseResult)

> *Summary: Verifies that a `CaseResult` object returns `True` for its `passed` attribute when all contained `AssertionResult` objects indicate success. It constructs a result with multiple passing assertions to confirm this behavior.*


### test_passed_returns_false_when_any_assertion_fails (method, L300-L310, parent: TestCaseResult)

> *Summary: When provided with a `CaseResult` containing at least one failed assertion, the resulting `passed` status should be set to `False`. This test verifies that failure in any single assertion dictates the overall outcome as unsuccessful.*


### test_passed_count_counts_passing_assertions (method, L312-L324, parent: TestCaseResult)

> *Summary: This test verifies that a `CaseResult` correctly aggregates the number of successful and total assertions from its list of results. It asserts that for a given result set containing two passes and two failures, the passed count is 2 and the total count is 4.*

