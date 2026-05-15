# cli/tests/test_install_cmd.py

8 class(es): TestResolveTargets, TestListCmd, TestSearchCmd, TestUninstallCmd, TestInstallSkillsCmd, TestInstallFromCmd, TestUpdateCmd, TestIsInteractive. 24 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestResolveTargets | class |  |
| TestListCmd | class |  |
| TestSearchCmd | class |  |
| TestUninstallCmd | class |  |
| TestInstallSkillsCmd | class |  |
| TestInstallFromCmd | class |  |
| TestUpdateCmd | class |  |
| TestIsInteractive | class |  |

## Chunks

### TestResolveTargets (class, L29-L68)

> *Summary: These tests verify the `_resolve_targets` function's behavior when determining which targets to install. It accepts a target string (or `None`) and a temporary path, returning a list of resolved target objects based on whether specific names are provided, if "all" is requested, or by detecting available targets in non-interactive mode.*


### test_target_all_returns_all_targets (method, L30-L32, parent: TestResolveTargets)

> *Summary: This test verifies that resolving targets with the "all" argument successfully returns a non-empty list of targets. It calls `_resolve_targets` using "all" and asserts the resulting collection has at least one element.*


### test_target_claude_returns_claude (method, L34-L37, parent: TestResolveTargets)

> *Summary: This test verifies that resolving targets for the name "claude" yields exactly one result, and confirms that this single target is named "claude". It takes a temporary path as input to perform the resolution.*


### test_comma_separated_targets (method, L39-L44, parent: TestResolveTargets)

> *Summary: Verifies that a function correctly resolves multiple target names provided as a comma-separated string input, ensuring the resulting list contains all expected individual targets. It asserts the count and presence of specific named targets within the resolved set.*


### test_unknown_target_exits (method, L46-L48, parent: TestResolveTargets)

> *Summary: Asserts that attempting to resolve targets with an unknown name causes the application to exit gracefully. It calls `_resolve_targets` with a non-existent target string and expects a `typer.Exit` exception.*


### test_no_target_no_detection_exits_noninteractive (method, L50-L57, parent: TestResolveTargets)

> *Summary: When running in non-interactive mode and no targets are detected, the function is expected to raise a `typer.Exit`. This test verifies that the installation command correctly exits under these specific conditions by mocking interactivity and target detection.*


### test_no_target_with_detection_returns_detected (method, L59-L68, parent: TestResolveTargets)

> *Summary: When no explicit targets are provided and target detection is mocked to find one instance named "claude," the function resolves and returns a list containing that single detected target. This confirms that automatic target discovery takes precedence when available.*


### TestListCmd (class, L76-L141)

> *Summary: This test suite verifies the functionality of listing artifacts via CLI commands by invoking the application with various arguments like `targets`, `installed`, and specific types. It uses mocking to simulate registry responses for testing successful listings, filtering by type, and graceful error handling during network failures.*


### test_list_targets (method, L77-L80, parent: TestListCmd)

> *Summary: Verifies that invoking the `list targets` command successfully returns an exit code of zero and includes the string "claude" in its output. This test confirms the expected behavior when listing available targets via the CLI runner.*


### test_list_installed_empty (method, L82-L85, parent: TestListCmd)

> *Summary: Verifies that invoking the `list installed` command returns a successful exit code (0) when no artifacts are present in the temporary directory. This test confirms the expected behavior for an empty installation state.*


### test_list_all_remote (method, L87-L112, parent: TestListCmd)

> *Summary: This test verifies that listing all remote artifacts succeeds by mocking the `ArtifactClient` to return a predefined list of skills and tools from a mock registry. It asserts that invoking the `list all` command results in an exit code of zero, confirming graceful operation.*


### test_list_specific_type (method, L114-L131, parent: TestListCmd)

> *Summary: This test verifies the CLI's ability to list artifacts of a specific type by mocking the artifact client and registry response. It asserts that invoking `list tools` returns an exit code of zero when the mocked data is successfully retrieved.*


### test_list_registry_failure_handled (method, L133-L141, parent: TestListCmd)

> *Summary: This test verifies that the CLI handles a `FetchError` during registry listing without crashing. It mocks the artifact client to simulate a network failure and asserts that the command exits successfully with code 0.*


### TestSearchCmd (class, L149-L186)

> *Summary: These tests verify the `search` command's behavior by mocking an artifact client to simulate different registry responses. It checks for successful retrieval of matching artifacts, proper handling when no results are found, and correct error reporting upon a network failure during registry fetching.*


### test_search_returns_results (method, L150-L168, parent: TestSearchCmd)

> *Summary: This test verifies that the search command correctly returns results when querying an artifact registry. It mocks the client to return a predefined list of artifacts and asserts that invoking `search fastapi` yields an exit code of zero and includes "fastapi" in the output.*


### test_search_no_results (method, L170-L177, parent: TestSearchCmd)

> *Summary: This test verifies the CLI's behavior when a search yields no artifacts by mocking the client to return empty lists for both registry fetching and searching. It asserts that the command exits successfully (code 0) and displays a "No results" message in its output.*


### test_search_registry_failure (method, L179-L186, parent: TestSearchCmd)

> *Summary: This test verifies that the CLI correctly handles a failure during registry search by mocking `ArtifactClient` to raise a `FetchError`. It asserts that invoking the `search` command results in a non-zero exit code, indicating an error was propagated.*


### TestUninstallCmd (class, L194-L221)

> *Summary: Tests verify that the uninstall command correctly removes tracked files and updates the lockfile when an entry exists, and also confirms a fallback mechanism for removal based on target when no specific lockfile match is found. The tests use temporary directories to simulate file system operations during uninstallation.*


### test_uninstall_with_lockfile_entry (method, L195-L213, parent: TestUninstallCmd)

> *Summary: This test verifies that the uninstall command successfully removes files previously tracked and recorded in a lockfile. It asserts that the specified file is deleted from the filesystem and the command exits successfully with confirmation output.*


### test_uninstall_no_match_falls_back (method, L215-L221, parent: TestUninstallCmd)

> *Summary: When running the uninstall command with no matching lockfile, this test verifies that the system successfully falls back to a target-based removal process for the specified project directory and skill. It asserts that the execution completes with an exit code of zero upon successful fallback.*


### TestInstallSkillsCmd (class, L229-L253)

> *Summary: These tests verify the functionality of an installation command by invoking it with various arguments against a temporary directory. It checks successful execution with default and filtered targets, as well as verifies that installing a non-existent package results in a failure state.*


### test_install_skills_default_target (method, L230-L237, parent: TestInstallSkillsCmd)

> *Summary: This test verifies that installing skills with a specified target, like "claude," executes successfully when provided with a temporary project directory. It asserts the command exits cleanly and confirms the output contains a "Done" message.*


### test_install_skills_with_name_filter (method, L239-L244, parent: TestInstallSkillsCmd)

> *Summary: This test verifies the successful execution of an installation command for skills, specifically targeting "claude" within a temporary project directory and filtering by the name "imports". It asserts that the command exits with a zero status code upon completion.*


### test_install_skills_unknown_pack (method, L246-L253, parent: TestInstallSkillsCmd)

> *Summary: This test verifies that attempting to install a non-existent skills pack results in an error state. It invokes the CLI with a fake pack name and asserts that the command exits with a non-zero code or contains specific error messages in its output.*


### TestInstallFromCmd (class, L261-L279)

> *Summary: Tests verify the installation command's behavior when provided with inputs; specifically, it asserts failure when installing from a directory lacking an `artifact.json` and checks for specific messaging when attempting to install from a remote URL.*


### test_install_from_nonexistent_dir (method, L262-L270, parent: TestInstallFromCmd)

> *Summary: Verifies that attempting to install from a directory lacking an `artifact.json` file results in a non-zero exit code when invoked via the CLI runner. It sets up an empty temporary directory and executes the installation command against it.*


### test_install_from_remote_url_shows_message (method, L272-L279, parent: TestInstallFromCmd)

> *Summary: This test verifies that invoking the `install from` command with a remote URL produces specific output messages. It asserts that the command exits successfully and contains either "coming soon" or "clone" in its standard output.*


### TestUpdateCmd (class, L287-L311)

> *Summary: This test suite verifies the behavior of the `update` command when run against a project directory. It asserts that the command correctly reports "No artifacts" if none are installed, and confirms it reports being "up to date" when existing artifacts match the registry state.*


### test_update_no_installed_artifacts (method, L288-L291, parent: TestUpdateCmd)

> *Summary: Verifies that running the `update` command with a project directory containing no installed artifacts exits successfully and outputs a message indicating the absence of artifacts.*


### test_update_all_up_to_date (method, L293-L311, parent: TestUpdateCmd)

> *Summary: This test verifies that running the `update` command when all registered artifacts are current results in a successful exit code and outputs a confirmation message. It simulates an environment where the artifact registry reports no updates are needed for the specified project directory.*


### TestIsInteractive (class, L319-L322)

> *Summary: Verifies that the `_is_interactive()` function returns a boolean value when called. This test ensures the output type matches expectations for interactivity checks.*


### test_returns_bool (method, L320-L322, parent: TestIsInteractive)

> *Summary: Verifies that the `_is_interactive()` function returns a boolean value. It asserts the type of the returned result is strictly `bool`.*

