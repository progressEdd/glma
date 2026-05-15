# cli/tests/test_run.py

3 function(s): _mock_ag2, _make_discovered_main, _make_result. 3 class(es): TestRunCmd, TestChatCmd, TestHelpers. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _mock_ag2 | function |  |
| _make_discovered_main | function |  |
| _make_result | function |  |
| TestRunCmd | class |  |
| TestChatCmd | class |  |
| TestHelpers | class |  |

## Chunks

### _mock_ag2 (function, L21-L25)

> *Summary: Provides a lightweight mock object simulating the `autogen` package structure, specifically setting up a return value for `UserProxyAgent`. This mock is used to isolate tests from external dependencies within the testing environment.*


### _make_discovered_main (function, L28-L34)

> *Summary: Creates a `DiscoveredAgent` instance representing the program's main entry point. It takes a source file path and an optional function, defaulting to a simple echo lambda if none is provided.*


### _make_result (function, L37-L49)

> *Summary: Creates a `RunResult` object by merging predefined default values with any provided keyword arguments. It serves as a factory to construct test results for agent runs, allowing customization of metrics like output, turns, and cost.*


### TestRunCmd (class, L57-L135)

> *Summary: This test suite verifies the behavior of the `ag2 run` command by invoking it with various inputs and mocking its execution logic. It asserts correct error handling for missing files, validates JSON output when the `--json` flag is used, and confirms that standard outputs and errors are correctly propagated from the underlying execution result.*


### test_run_requires_message_when_stdin_is_tty (method, L62-L79, parent: TestRunCmd)

> *Summary: This test verifies that a command execution fails with an error if no message is provided and standard input is a terminal (TTY). It achieves this by mocking `sys.stdin` to report itself as a TTY while providing no input to the runner.*


### test_run_exits_on_file_not_found (method, L82-L87, parent: TestRunCmd)

> *Summary: Verifies that the command execution fails and returns a non-zero exit code when provided with a nonexistent agent file path. It asserts that the output message contains indicators of an error or file not found status.*


### test_run_json_outputs_valid_json (method, L91-L107, parent: TestRunCmd)

> *Summary: This test verifies that invoking the `run` command with a `--json` flag produces valid, parsable JSON output. It asserts that the resulting JSON structure contains expected fields like `"output"` and `"turns"`, based on mocked execution results.*


### test_run_with_main_agent_produces_output (method, L111-L121, parent: TestRunCmd)

> *Summary: This test verifies that invoking the `run` command with a main agent successfully executes and captures its output. It asserts that the execution returns an exit code of zero and contains the expected string from the mocked agent's result.*


### test_run_shows_errors (method, L125-L135, parent: TestRunCmd)

> *Summary: This test verifies that the `runner` correctly signals failure when a command execution returns errors. It asserts that the invocation's exit code is non-zero and that the output contains the expected error message from the mocked result.*


### TestChatCmd (class, L143-L159)

> *Summary: These tests verify the behavior of the `chat` command, ensuring it exits with an error code and provides guidance when neither an agent file nor a `--model` argument is supplied during invocation. The tests use mocking to simulate the requirement for an AG2 context before checking the output messages.*


### test_chat_requires_agent_file_or_model (method, L147-L151, parent: TestChatCmd)

> *Summary: Verifies that the `chat` command fails if no agent file path or `--model` argument is provided to the application runner. It asserts a non-zero exit code and checks that the output message indicates either a missing agent file or model specification.*


### test_chat_errors_no_file_no_model (method, L154-L159, parent: TestChatCmd)

> *Summary: When invoked with no arguments, this test verifies that the `chat` command fails and outputs guidance suggesting the user must specify either a `--model` or provide an input file. The assertion checks for specific keywords within the output to confirm helpful error messaging is displayed.*


### TestHelpers (class, L167-L282)

> *Summary: This test suite verifies the functionality of private helper functions within the `run` module by testing header display for different agent configurations (`main`, `agents`, `agent`), summary rendering with and without cost/errors, and file discovery logic. It ensures that the discovery function correctly delegates to YAML loaders or Python file scanners based on the input file type, while also confirming it exits when a specified file is missing.*


### test_display_header_main (method, L170-L181, parent: TestHelpers)

> *Summary: This test verifies that the header display function executes without errors when provided with a `DiscoveredAgent` configured for the 'main' kind. It calls the internal rendering logic using a mock agent setup to confirm stability.*


### test_display_header_agents (method, L183-L193, parent: TestHelpers)

> *Summary: This test verifies that the header rendering function handles a specific agent configuration without raising an error. It passes a `DiscoveredAgent` object, configured with `kind="agents"` and mock agents, to the display utility.*


### test_display_header_agent (method, L195-L205, parent: TestHelpers)

> *Summary: This test verifies that the header display function executes without errors when provided with a `DiscoveredAgent` instance configured for an 'agent' kind. It calls the internal rendering logic using mock data representing an agent discovery.*


### test_display_summary_with_cost_and_errors (method, L207-L226, parent: TestHelpers)

> *Summary: This test verifies that the summary display function correctly renders a `RunResult` object containing both associated costs and reported errors. It passes a mock result structure, including specific token usage and an error list, to ensure no exceptions are raised during rendering.*


### test_display_summary_minimal (method, L228-L233, parent: TestHelpers)

> *Summary: This test verifies the rendering of a minimal `RunResult` by calling `_display_summary` with a result object lacking cost and errors. It ensures the summary output is generated correctly under these basic conditions.*


### test_discover_dispatches_yaml (method, L237-L256, parent: TestHelpers)

> *Summary: This test verifies that the discovery mechanism correctly processes YAML files by mocking file loading and building agent structures. It asserts that the loader is called with the correct file path and the builder receives the parsed data, ultimately confirming the returned discovered agent matches expectations.*


### test_discover_dispatches_py (method, L259-L272, parent: TestHelpers)

> *Summary: This test verifies that the `_discover` function correctly delegates discovery for Python files by calling a mocked `discover()` method with the resolved path of the input agent file. It asserts that the returned value from `_discover` matches the expected structure generated based on the provided file.*


### test_discover_exits_for_missing_file (method, L274-L282, parent: TestHelpers)

> *Summary: This test verifies that the `_discover` function raises a `typer.Exit` (or `SystemExit`) when provided with a file path that does not exist. It asserts this expected failure behavior using `pytest.raises`.*

