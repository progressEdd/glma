# cli/tests/test_arena.py

5 function(s): _mock_autogen, two_agent_files, agents_dir, eval_file, leaderboard_dir. 10 class(es): TestCaseResult, TestContenderResult, TestDetermineWinner, TestELO, TestLeaderboard, TestResolveContenderFiles, TestFlatCases, TestArenaCompare, TestArenaLeaderboard, TestArenaReset. 28 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _mock_autogen | function |  |
| two_agent_files | function |  |
| agents_dir | function |  |
| eval_file | function |  |
| leaderboard_dir | function |  |
| TestCaseResult | class |  |
| TestContenderResult | class |  |
| TestDetermineWinner | class |  |
| TestELO | class |  |
| TestLeaderboard | class |  |
| TestResolveContenderFiles | class |  |
| TestFlatCases | class |  |
| TestArenaCompare | class |  |
| TestArenaLeaderboard | class |  |
| TestArenaReset | class |  |

## Chunks

### _mock_autogen (function, L36-L42)

> *Summary: This function temporarily patches `sys.modules` to inject a mock `autogen` module into the Python environment. This allows tests requiring arena commands to run even when the actual `ag2` package is not installed.*


### two_agent_files (function, L51-L67)

> *Summary: Generates two distinct Python files within a temporary directory, each containing a `main` function with unique return strings. It returns tuples containing the paths to these newly created agent files for testing purposes.*


### agents_dir (function, L71-L78)

> *Summary: Creates a directory named "agents" within the provided temporary path and populates it with three Python files, each containing a simple `main` function definition. Returns the path to this newly created agents directory.*


### eval_file (function, L82-L106)

> *Summary: Generates a temporary YAML file containing predefined test cases for an arena evaluation. It takes a base path as input and returns the full `Path` object pointing to the created `cases.yaml`.*


### leaderboard_dir (function, L110-L114)

> *Summary: Creates and returns a temporary path for the arena leaderboard within a provided base directory. It ensures the necessary nested directories exist before returning the final location.*


### TestCaseResult (class, L122-L147)

> *Summary: This class provides unit tests to verify the behavior of `CaseResult` objects, specifically how they calculate a pass status and score based on an array of assertion results. It demonstrates scenarios where all assertions pass (resulting in a 1.0 score), some fail (resulting in a partial score like 0.5), or when no assertions are present (resulting in a 0.0 score).*


### test_passed_all_assertions_pass (method, L123-L132, parent: TestCaseResult)

> *Summary: This test verifies that a `CaseResult` object correctly reflects success when all contained assertions pass. It asserts the result's overall `passed` status is true and its calculated score is $1.0$.*


### test_passed_some_assertions_fail (method, L134-L143, parent: TestCaseResult)

> *Summary: This test verifies that a `CaseResult` object correctly reflects partial success; specifically, it asserts the overall result is marked as failed and the score is set to 0.5 when some assertions pass while others fail.*


### test_score_empty_assertions (method, L145-L147, parent: TestCaseResult)

> *Summary: When given a `CaseResult` initialized with an evaluation case, this test asserts that the resulting score is exactly $0.0$.*


### TestContenderResult (class, L150-L170)

> *Summary: Verifies the calculation of a contender's pass rate and aggregate metrics based on provided test case results. It asserts that the calculated `pass_rate` is correct for mixed success/failure cases, and that all metrics default to zero when no results are present.*


### test_pass_rate (method, L151-L163, parent: TestContenderResult)

> *Summary: This test verifies that a `ContenderResult` correctly calculates its pass rate based on provided `CaseResult` objects. It asserts the calculated pass rate is $0.5$ when one out of two cases passes.*


### test_empty_results (method, L165-L170, parent: TestContenderResult)

> *Summary: Verifies that a `ContenderResult` initialized with minimal data correctly reports zero values for pass rate, average score, elapsed time, and total cost. This test ensures the default state of the result object is accurate when no results are present.*


### TestDetermineWinner (class, L178-L222)

> *Summary: This test suite verifies the logic for determining a case winner from a dictionary of `CaseResult` objects. It asserts that the function correctly identifies a single winner based on passing status and scores, returns `None` for ties or empty inputs, and handles various combinations of pass/fail results.*


### test_one_passes_one_fails (method, L179-L189, parent: TestDetermineWinner)

> *Summary: This test verifies that a function correctly identifies the winner when provided with mixed results. It inputs a dictionary containing one passing and one failing `CaseResult` and asserts that the key corresponding to the passing result is returned.*


### test_both_pass_same_score_is_tie (method, L191-L198, parent: TestDetermineWinner)

> *Summary: When two cases yield identical results (e.g., both pass with the same score), this test asserts that the winner determination logic correctly returns `None`, indicating a tie. It uses mock `CaseResult` objects to simulate this scenario for evaluation.*


### test_both_pass_different_score (method, L200-L219, parent: TestDetermineWinner)

> *Summary: Given two `CaseResult` objects with different assertion outcomes and scores, this test verifies that the function correctly selects the result with a higher score if one of the results is not entirely successful. Specifically, it confirms the result with all passing assertions wins over one where some fail, even if the failing result has a lower score.*


### test_empty_results (method, L221-L222, parent: TestDetermineWinner)

> *Summary: Verifies that when provided with an empty dictionary, the case winner determination function returns `None`. This confirms correct handling of zero input data.*


### TestELO (class, L230-L250)

> *Summary: These tests verify the core logic of ELO rating adjustments by calling a helper function with initial ratings and specifying the winner. They confirm that winners gain points, losers lose points, draws result in no change when ratings are equal, and upsets yield greater rating gains for the lower-rated victor.*


### test_winner_gains_rating (method, L231-L234, parent: TestELO)

> *Summary: This test verifies that the winner of a match gains rating points while the loser loses them. It calls an Elo calculation function with two equal starting ratings and asserts the resulting ratings reflect this gain/loss.*


### test_draw_no_change_when_equal (method, L236-L239, parent: TestELO)

> *Summary: When two players have equal ratings (e.g., 1500 vs 1500), the Elo calculation results in no change to either player's rating, returning the original scores.*


### test_upset_gives_more_points (method, L241-L246, parent: TestELO)

> *Summary: This test verifies that an upset victory yields a greater Elo point gain than a standard win. It compares the resulting Elo change when a lower-rated player defeats a higher-rated one versus when players of equal rating compete.*


### test_loser_loses_rating (method, L248-L250, parent: TestELO)

> *Summary: This test verifies that a player who loses an Elo match experiences a rating decrease. It calls `_compute_elo` with two equal starting ratings and a loss outcome ("a"), asserting the resulting new rating is lower than the initial value.*


### TestLeaderboard (class, L253-L266)

> *Summary: Verifies the persistence logic for a leaderboard by testing saving and subsequently loading data from a specified file path. It also confirms that attempting to load a non-existent leaderboard returns an empty structure.*


### test_save_and_load (method, L254-L260, parent: TestLeaderboard)

> *Summary: This test verifies the persistence mechanism by saving a predefined leaderboard structure to a temporary file and then immediately loading it back. It asserts that the loaded data accurately reflects the initial state, confirming successful serialization and deserialization.*


### test_load_missing_returns_empty (method, L262-L266, parent: TestLeaderboard)

> *Summary: When attempting to load a leaderboard from a non-existent file path, the function returns an empty dictionary structure containing an empty agents map. This test verifies that missing files are handled gracefully by returning default, empty data.*


### TestResolveContenderFiles (class, L274-L287)

> *Summary: This test suite verifies the `_resolve_contender_files` utility function's behavior when resolving file paths. It asserts correct file expansion from directories, handles lists of individual files, and ensures an exit is raised if a specified file does not exist.*


### test_expands_directory (method, L275-L278, parent: TestResolveContenderFiles)

> *Summary: This test verifies that a provided directory resolves to exactly three Python files. It asserts the count and file extensions of the resolved paths returned by `_resolve_contender_files`.*


### test_single_files (method, L280-L283, parent: TestResolveContenderFiles)

> *Summary: Given a tuple of two file paths, this test verifies that the internal function correctly resolves and returns exactly those two files. It asserts the resulting list contains both input files.*


### test_missing_file_exits (method, L285-L287, parent: TestResolveContenderFiles)

> *Summary: Asserts that attempting to resolve contender files when a specified file is missing causes the application to exit gracefully via `typer.Exit`. It tests this behavior by passing a path to a non-existent file into the resolution function.*


### TestFlatCases (class, L290-L305)

> *Summary: This test verifies that a list of `EvalSuite` objects is correctly flattened into a single sequence of individual `EvalCase` instances. It asserts that the resulting list contains all cases from the input suites in order and maintains the correct count.*


### test_flattens_suites (method, L291-L305, parent: TestFlatCases)

> *Summary: This test verifies that a function correctly flattens a list of `EvalSuite` objects into a single, ordered list of individual `EvalCase` instances. It takes multiple suites as input and asserts the resulting flattened list contains all cases from the original suites in sequence.*


### TestArenaCompare (class, L313-L381)

> *Summary: These tests validate the `arena compare` command's behavior by invoking it with various inputs, such as single or multiple agent files and an evaluation script. The assertions verify expected exit codes, output content (like "Dry run" or "Summary"), and successful JSON parsing when requested.*


### test_compare_needs_two_contenders (method, L314-L318, parent: TestArenaCompare)

> *Summary: This test verifies that the comparison command fails when only one contender file is provided as input to the arena runner. It sets up a single Python file and invokes the `arena compare` command, asserting a non-zero exit code.*


### test_compare_dry_run (method, L320-L327, parent: TestArenaCompare)

> *Summary: This test verifies that invoking the `arena compare` command with a `--dry-run` flag executes successfully and outputs a confirmation message indicating it was a dry run. It takes two agent file paths and an evaluation file path as input to simulate this comparison process.*


### test_compare_runs_eval (method, L329-L339, parent: TestArenaCompare)

> *Summary: This test verifies the CLI command for comparing two agent runs against an evaluation file. It invokes the `arena compare` command with two agent files and an eval file, asserting that the execution succeeds (exit code 0) and the output contains expected summary information.*


### test_compare_json_output (method, L341-L371, parent: TestArenaCompare)

> *Summary: This test verifies the `arena compare` command by invoking it with two agent files and an evaluation file, expecting a successful exit code. It then parses the resulting JSON output to assert that key metrics like "contenders" and "wins" are present in the data structure.*


### test_compare_tournament (method, L373-L381, parent: TestArenaCompare)

> *Summary: This test verifies the `arena compare` command by invoking it with specified agent and evaluation file paths, asserting that the execution succeeds (exit code 0) and the output contains the string "Arena".*


### TestArenaLeaderboard (class, L384-L407)

> *Summary: These tests verify the CLI's leaderboard functionality by simulating different JSON file states. It checks that an empty leaderboard returns a specific message, while a populated one correctly displays agent data from the provided input file.*


### test_empty_leaderboard (method, L385-L390, parent: TestArenaLeaderboard)

> *Summary: This test verifies the CLI's behavior when accessing an empty leaderboard file. It asserts that invoking the `arena leaderboard` command with a specified empty JSON path returns an exit code of zero and displays the message "No arena results".*


### test_leaderboard_with_data (method, L392-L407, parent: TestArenaLeaderboard)

> *Summary: This test verifies the leaderboard command by providing a mock JSON file containing agent data. It asserts that invoking the `arena leaderboard` command successfully reads this data and outputs both specified agents' names.*


### TestArenaReset (class, L410-L424)

> *Summary: This test suite verifies the `arena reset` command's behavior when interacting with a leaderboard file. It asserts that resetting an existing leaderboard deletes the file and returns success, while also confirming successful execution when no such file exists.*


### test_reset_existing (method, L411-L418, parent: TestArenaReset)

> *Summary: This test verifies that the `arena reset` command successfully clears an existing leaderboard file. It writes a placeholder JSON to a temporary path, invokes the command while mocking the leaderboard path, and asserts that the process exits cleanly and the original file is deleted.*


### test_reset_nonexistent (method, L420-L424, parent: TestArenaReset)

> *Summary: When the leaderboard file path is set to a non-existent location, this test verifies that invoking the `arena reset` command successfully exits with code 0. It achieves this by patching the global leaderboard path variable before execution.*

