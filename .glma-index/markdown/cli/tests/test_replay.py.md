# cli/tests/test_replay.py

3 function(s): sessions_dir, sample_session, saved_session. 13 class(es): TestSessionEvent, TestSessionMeta, TestSaveAndLoad, TestListSessions, TestDeleteSession, TestCreateSessionId, TestRecordFromRunResult, TestReplayList, TestReplayShow, TestReplayExport, TestReplayDelete, TestReplayClear, TestReplayCompare. 31 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| sessions_dir | function |  |
| sample_session | function |  |
| saved_session | function |  |
| TestSessionEvent | class |  |
| TestSessionMeta | class |  |
| TestSaveAndLoad | class |  |
| TestListSessions | class |  |
| TestDeleteSession | class |  |
| TestCreateSessionId | class |  |
| TestRecordFromRunResult | class |  |
| TestReplayList | class |  |
| TestReplayShow | class |  |
| TestReplayExport | class |  |
| TestReplayDelete | class |  |
| TestReplayClear | class |  |
| TestReplayCompare | class |  |

## Chunks

### sessions_dir (function, L33-L37)

> *Summary: Creates and returns a temporary subdirectory named "sessions" within the provided base path. This function ensures the necessary directory structure exists for session data storage during testing.*


### sample_session (function, L41-L82)

> *Summary: Constructs a complete `Session` object for testing purposes. It takes predefined metadata (like session ID, agent names, and costs) and a list of sequential `SessionEvent` objects detailing user and assistant interactions.*


### saved_session (function, L86-L90)

> *Summary: This function saves a provided `Session` object to the specified directory and then returns the original session object. It temporarily patches the global session directory configuration during the saving process.*


### TestSessionEvent (class, L98-L113)

> *Summary: Verifies the correct initialization and attribute assignment of a `SessionEvent` object, ensuring that basic fields like turn, speaker, and content are set correctly upon creation. It also confirms proper handling when optional metadata, such as tool calls, is provided during instantiation.*


### test_creation (method, L99-L103, parent: TestSessionEvent)

> *Summary: Verifies that a newly instantiated `SessionEvent` object correctly initializes its attributes from provided inputs, specifically checking the turn number, speaker name, and an empty metadata dictionary.*


### test_with_metadata (method, L105-L113, parent: TestSessionEvent)

> *Summary: This test verifies that a `SessionEvent` object correctly stores metadata, specifically checking for the presence of a `"tool_calls"` key within its `metadata` dictionary when initialized with sample data.*


### TestSessionMeta (class, L116-L127)

> *Summary: Verifies that an instance of `SessionMeta` is correctly initialized with provided session details like ID, agent file, and turn count. It asserts the resulting object holds the input values accurately and initializes a zero total cost.*


### test_creation (method, L117-L127, parent: TestSessionMeta)

> *Summary: This test verifies the initialization of a `SessionMeta` object by providing specific session details like ID, agent file, and turn count. It asserts that the resulting metadata correctly stores the provided session ID and initializes the total cost to zero.*


### TestSaveAndLoad (class, L135-L166)

> *Summary: These tests verify the persistence functionality for session data, ensuring that sessions can be successfully saved to disk and subsequently loaded back using either a specific ID or a prefix. The suite confirms that saving creates the expected file structure, loading retrieves the correct session object, and a full roundtrip preserves all original metadata and event content.*


### test_save_creates_file (method, L136-L141, parent: TestSaveAndLoad)

> *Summary: This test verifies that the `save_session` function successfully creates a file containing session data when provided with a sample session object. It asserts both the existence of the saved file and that its contents correctly reflect the original session's ID.*


### test_load_by_id (method, L143-L147, parent: TestSaveAndLoad)

> *Summary: This test verifies that loading a session by its ID successfully retrieves the correct session object. It asserts that the returned session matches the original's ID and contains the same number of events.*


### test_load_by_prefix (method, L149-L152, parent: TestSaveAndLoad)

> *Summary: This test verifies that loading a session using a specific prefix correctly retrieves the intended session object. It asserts that the `session_id` of the loaded session matches the ID from a provided saved session instance.*


### test_load_missing_exits (method, L154-L158, parent: TestSaveAndLoad)

> *Summary: Asserts that attempting to load a session with a non-existent ID raises a `typer.Exit` exception when the session directory is mocked. This verifies the CLI handles missing session files gracefully by exiting.*


### test_roundtrip_preserves_data (method, L160-L166, parent: TestSaveAndLoad)

> *Summary: This test verifies data integrity by saving a sample session and then reloading it to ensure key attributes like agent file path, event content, and total cost match the original object. It confirms that the serialization/deserialization process preserves all critical session information.*


### TestListSessions (class, L169-L199)

> *Summary: This test suite verifies the `list_sessions` function by simulating different directory states. It asserts that the function correctly returns an empty list when no sessions exist, a single session when one is present, and multiple sessions when several are saved to the specified directory path.*


### test_list_empty (method, L170-L173, parent: TestListSessions)

> *Summary: When provided with a specific directory path for session storage, this test verifies that the `list_sessions` function returns an empty list if no sessions exist in that location.*


### test_list_with_sessions (method, L175-L179, parent: TestListSessions)

> *Summary: This test verifies that the `list_sessions` function correctly returns a list containing exactly one session when provided with a specific directory and a known session object. It asserts that the returned session's ID matches the expected ID from the input session.*


### test_list_multiple (method, L181-L199, parent: TestListSessions)

> *Summary: This test creates and saves three distinct `Session` objects to a specified directory, then calls `list_sessions()` to verify that exactly three sessions are successfully retrieved. It ensures the session listing function correctly enumerates multiple saved instances.*


### TestDeleteSession (class, L202-L216)

> *Summary: These tests verify the `delete_session` function's behavior when removing session files from a specified directory. It confirms successful deletion of an existing session by ID or prefix, and correctly returns false when attempting to delete a non-existent session.*


### test_delete_existing (method, L203-L206, parent: TestDeleteSession)

> *Summary: This test verifies that deleting a session ID which already exists returns `True`. It achieves this by temporarily setting the global session directory before calling the deletion function with a provided `Session` object.*


### test_delete_by_prefix (method, L208-L211, parent: TestDeleteSession)

> *Summary: This test verifies that deleting a session using a prefix successfully returns `True`. It achieves this by patching the global sessions directory to point to a specific temporary location.*


### test_delete_nonexistent (method, L213-L216, parent: TestDeleteSession)

> *Summary: Verifies that attempting to delete a session ID that does not exist returns `False`. This test mocks the session directory path and calls the `delete_session` function with an invalid identifier.*


### TestCreateSessionId (class, L224-L235)

> *Summary: Verifies that the generated session ID adheres to a specific format (three hyphen-separated parts with fixed lengths for date, time, and hex). It also confirms that multiple calls to the generation function produce unique IDs.*


### test_format (method, L225-L231, parent: TestCreateSessionId)

> *Summary: Verifies that a generated session ID, when split by hyphens, results in exactly three parts with specific length constraints for the date (8 chars), time (6 chars), and hexadecimal segment (6 chars). This confirms the expected structure of the session identifier.*


### test_unique (method, L233-L235, parent: TestCreateSessionId)

> *Summary: Verifies that generating ten session IDs results in ten unique identifiers. It creates a set of IDs and asserts the size matches the number generated.*


### TestRecordFromRunResult (class, L243-L275)

> *Summary: This test suite verifies the `record_from_run_result` function by simulating various run result objects. It asserts that the resulting session correctly captures metadata like input messages, agent files, turn counts, and specific cost details from the provided fake results.*


### test_records_from_result (method, L244-L264, parent: TestRecordFromRunResult)

> *Summary: This test verifies that a `record_from_run_result` function correctly extracts and structures conversational data from a mock result object. It asserts that the resulting session contains the correct number of turns, agent file name, input message, and speaker sequence based on the provided fake history.*


### test_records_cost (method, L266-L275, parent: TestRecordFromRunResult)

> *Summary: This test verifies that the cost information from a simulated run result is correctly captured when creating a recording session. It asserts that the `total_cost` attribute of the resulting session matches the predefined cost structure in the fake result object.*


### TestReplayList (class, L283-L294)

> *Summary: Verifies the `replay list` command's behavior by testing two scenarios: when no sessions exist (expecting a specific message) and when one or more sessions are present (expecting the session ID to be listed). It uses dependency injection to control the directory where sessions are searched.*


### test_list_empty (method, L284-L288, parent: TestReplayList)

> *Summary: Verifies that invoking the `replay list` command when no sessions exist returns an exit code of zero and outputs a specific "No recorded sessions" message. This test uses mocking to control the session directory path provided to the application runner.*


### test_list_with_sessions (method, L290-L294, parent: TestReplayList)

> *Summary: This test verifies that the `replay list` command correctly displays a specific session ID when run against a mocked sessions directory. It asserts successful execution and confirms the target session's ID is present in the command's output.*


### TestReplayShow (class, L297-L308)

> *Summary: Tests verify the CLI's `replay show` command by invoking it with a valid session ID to check for successful output containing specific keywords, and also tests failure when provided with a non-existent session ID. These tests use mocking to control the sessions directory path during execution.*


### test_show_session (method, L298-L303, parent: TestReplayShow)

> *Summary: This test verifies the `replay show` command by invoking it with a specific session ID, asserting that the execution succeeds (exit code 0) and the output contains expected keywords like "researcher" and "Replay". It temporarily mocks the sessions directory to ensure the command operates within a controlled environment.*


### test_show_missing (method, L305-L308, parent: TestReplayShow)

> *Summary: This test verifies that the replay command fails when attempting to show a non-existent session. It invokes the CLI with `"replay show nonexistent"` and asserts that the execution exits with a non-zero status code.*


### TestReplayExport (class, L311-L359)

> *Summary: These tests verify the `replay export` command's functionality by invoking it with various formats (JSON, Markdown, HTML) and an optional output file path. They assert that the command executes successfully and that the resulting output contains expected content or is written to the specified location.*


### test_export_json (method, L312-L320, parent: TestReplayExport)

> *Summary: Verifies that exporting a specific session to JSON format via the CLI succeeds and produces output containing the correct session ID in its metadata. It invokes the `replay export` command, expecting an exit code of zero and parsing the resulting JSON string for validation.*


### test_export_markdown (method, L322-L330, parent: TestReplayExport)

> *Summary: This test verifies that exporting a saved session to Markdown format executes successfully and produces output containing specific markers like the session title and researcher name. It invokes the `replay export` command with the `--format md` flag against a provided session object.*


### test_export_html (method, L332-L339, parent: TestReplayExport)

> *Summary: This test verifies that exporting a saved session to HTML format executes successfully via the CLI. It asserts that the command returns an exit code of zero and that the output contains the HTML tag `<html>`.*


### test_export_to_file (method, L341-L359, parent: TestReplayExport)

> *Summary: This test verifies that exporting a saved session to a JSON file succeeds by invoking the `replay export` command with specific arguments. It asserts that the command exits successfully, creates the expected output file, and that the content of the file contains the correct session ID metadata.*


### TestReplayDelete (class, L362-L372)

> *Summary: Verifies the CLI's ability to delete a saved replay session by invoking the `replay delete` command with a valid ID and asserting success. It also tests the failure case when attempting to delete a non-existent session ID, expecting a non-zero exit code.*


### test_delete_session (method, L363-L367, parent: TestReplayDelete)

> *Summary: This test verifies that invoking the `replay delete` command with a specific session ID successfully removes the session. It asserts that the command exits with code 0 and outputs a confirmation message containing "Deleted".*


### test_delete_missing (method, L369-L372, parent: TestReplayDelete)

> *Summary: Verifies that attempting to delete a non-existent replay session returns a non-zero exit code when the application is invoked with the `replay delete nonexistent` command. This test uses patching to control the sessions directory path during execution.*


### TestReplayClear (class, L375-L387)

> *Summary: Tests verify that invoking the `replay clear` command successfully removes session data from a specified directory, and also confirms correct behavior when the target sessions directory is empty. The tests use mocking to control the session directory path during execution.*


### test_clear_sessions (method, L376-L380, parent: TestReplayClear)

> *Summary: This test verifies that invoking the `replay clear` command successfully clears saved sessions within a specified directory. It asserts that the command exits with code zero and outputs a confirmation message containing "Cleared".*


### test_clear_empty (method, L382-L387, parent: TestReplayClear)

> *Summary: Verifies that the `replay clear` command executes successfully when run against an empty sessions directory. It sets up a temporary, empty directory and asserts the invocation returns an exit code of zero.*


### TestReplayCompare (class, L390-L419)

> *Summary: This test verifies the comparison functionality by creating and saving two distinct session objects to a specified directory. It then invokes the `replay compare` command with these two sessions, asserting that the execution succeeds and the output contains a "Comparison" indicator.*


### test_compare_two_sessions (method, L391-L419, parent: TestReplayCompare)

> *Summary: This test verifies the comparison functionality by first creating and saving two distinct session objects to a specified directory. It then invokes the `replay compare` command with these two sessions, asserting that the execution succeeds and the output contains a "Comparison" indicator.*

