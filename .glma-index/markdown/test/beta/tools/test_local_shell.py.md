# test/beta/tools/test_local_shell.py

4 class(es): TestMatches, TestCheckIgnore, TestLocalShellToolConstruction, TestShellExecution. 38 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMatches | class |  |
| TestCheckIgnore | class |  |
| TestLocalShellToolConstruction | class |  |
| TestShellExecution | class |  |

## Chunks

### TestMatches (class, L19-L45)

> *Summary: This test suite verifies the behavior of a `matches` function, ensuring it correctly identifies when a given prefix string matches the beginning of another command line input. It specifically tests for exact prefix matching, multi-word prefixes, handling of leading whitespace, and preventing false positives by enforcing word boundaries.*


### test_plain_prefix_matches (method, L20-L21, parent: TestMatches)

> *Summary: Verifies that a simple prefix match function correctly identifies when the input string starts with the provided prefix. It asserts `True` for the case where `"git"` is a prefix of `"git status"`.*


### test_plain_prefix_no_match (method, L23-L24, parent: TestMatches)

> *Summary: Verifies that the `matches` function correctly returns `False` when a simple prefix ("git") does not match the provided command string ("rm -rf /"). This tests the negative matching behavior of the utility.*


### test_multi_word_prefix (method, L26-L28, parent: TestMatches)

> *Summary: This test verifies that a prefix matching function correctly identifies when the input string starts with a multi-word phrase. It asserts true for `"uv run"` matching `"uv run pytest"`, but false for it matching `"uv add requests"`.*


### test_rm_rf_blocked (method, L30-L32, parent: TestMatches)

> *Summary: This test verifies that the `matches` function correctly identifies when a command string contains the dangerous pattern `"rm -rf"` followed by an absolute path, while rejecting it if only a relative or simple filename follows. It asserts specific boolean outcomes based on input strings.*


### test_leading_whitespace_stripped (method, L34-L35, parent: TestMatches)

> *Summary: Verifies that a matching function correctly identifies a command even when it has leading whitespace. It asserts that the string `"  git status"` successfully matches the pattern `"git"`.*


### test_exact_command_matches (method, L37-L39, parent: TestMatches)

> *Summary: Verifies that a command string exactly matching the provided input, such as `"git"` against `"git"`, correctly returns `True`. This test confirms precise command recognition without any arguments.*


### test_word_boundary_no_false_positive (method, L41-L45, parent: TestMatches)

> *Summary: This test verifies that a matching function correctly identifies word boundaries, ensuring that searching for a term like "git" does not incorrectly match substrings within other words such as "gitconfig" or "catchphrase". It asserts `False` when the search term appears embedded within another string.*


### TestCheckIgnore (class, L48-L93)

> *Summary: This test suite verifies the behavior of a file checking function by simulating shell commands against various file paths. It asserts that the function correctly blocks access to sensitive files matching specific patterns (like `.env` or `*.key`) while allowing safe files, and it also validates security checks for path traversal and absolute paths.*


### test_env_file_blocked (method, L49-L52, parent: TestCheckIgnore)

> *Summary: This test verifies that the ignore mechanism correctly blocks access to a `.env` file when using `check_ignore`. It asserts that the check returns a non-null result containing the filename.*


### test_key_file_blocked (method, L54-L57, parent: TestCheckIgnore)

> *Summary: This test verifies that the ignore mechanism correctly blocks access to a specific key file when configured with a pattern matching `*.key`. It asserts that the check function returns a non-null result containing the blocked filename.*


### test_secrets_dir_blocked (method, L59-L62, parent: TestCheckIgnore)

> *Summary: Verifies that the ignore mechanism correctly blocks access to files within a specified directory pattern when running shell commands. It checks if the output from attempting to `cat` a file inside the blocked directory contains the expected path segment.*


### test_safe_file_allowed (method, L64-L66, parent: TestCheckIgnore)

> *Summary: This test verifies that a command execution function correctly allows access to a specific file (`app.py`) when filtering rules are in place. It calls `check_ignore` with the command and allowed paths, asserting that no errors or restrictions were returned.*


### test_quoted_path_handled (method, L68-L70, parent: TestCheckIgnore)

> *Summary: This test verifies that the ignore mechanism correctly handles paths containing quotes by executing `cat ".env"` against a temporary directory and asserting a non-null result. It confirms proper parsing of quoted arguments within shell commands.*


### test_plain_filename_blocked (method, L72-L73, parent: TestCheckIgnore)

> *Summary: Asserts that attempting to execute a command using a plain filename like `.env` within the ignore mechanism returns a non-null result. This tests the blocking behavior for specific file patterns provided in the input list.*


### test_plain_dirname_blocks_contents (method, L75-L78, parent: TestCheckIgnore)

> *Summary: This test verifies that a specified directory correctly blocks file content when using an ignore mechanism. It asserts that commands attempting to access files within the ignored "secrets" directory return results, while accessing non-ignored files returns nothing.*


### test_no_patterns_returns_none (method, L80-L81, parent: TestCheckIgnore)

> *Summary: Asserts that the `check_ignore` function returns `None` when provided with a command and an empty list of ignore patterns. This verifies correct behavior for scenarios lacking specific exclusion rules.*


### test_path_traversal_blocked (method, L83-L87, parent: TestCheckIgnore)

> *Summary: Verifies that attempting to access files outside the designated working directory using path traversal sequences like `../../../etc/passwd` results in an explicit "Access denied" response. It calls a checking function with a malicious input and asserts the denial message is present in the output.*


### test_absolute_path_outside_workdir_blocked (method, L89-L93, parent: TestCheckIgnore)

> *Summary: This test verifies that attempting to access an absolute path outside the designated working directory results in a denial. It calls `check_ignore` with an external file path and asserts that the returned result contains an "Access denied" message.*


### TestLocalShellToolConstruction (class, L96-L111)

> *Summary: This test suite verifies the initialization and behavior of a local shell tool, ensuring its working directory is correctly created either automatically or via an explicit path provided during instantiation. It also confirms that the `workdir` attribute is read-only after construction.*


### test_auto_tempdir_created (method, L97-L100, parent: TestLocalShellToolConstruction)

> *Summary: Verifies that the `LocalShellTool` automatically creates a working directory upon instantiation. It asserts that this created path exists and is indeed a directory.*


### test_explicit_path_created (method, L102-L106, parent: TestLocalShellToolConstruction)

> *Summary: This test verifies that a `LocalShellTool` correctly sets its working directory to an explicitly provided path within a temporary directory structure. It asserts that the tool's internal `workdir` matches the input and that the specified directory actually exists on disk.*


### test_workdir_is_readonly_property (method, L108-L111, parent: TestLocalShellToolConstruction)

> *Summary: This test verifies that the `workdir` attribute of a `LocalShellTool` instance is read-only. It asserts an `AttributeError` when attempting to assign a new value to this property.*


### TestShellExecution (class, L114-L405)

> *Summary: This test suite verifies the behavior of a local shell execution tool by simulating agent interactions with various configurations. It tests features like command whitelisting/blacklisting, environment variable merging, timeouts, file system permissions (read-only), output truncation, and exit code reporting.*


### _make_tool_call (method, L117-L121, parent: TestShellExecution)

> *Summary: Constructs a `ToolCallEvent` object to invoke the "run\_shell\_command" tool, serializing the input string as the `command` argument within JSON. This method takes a shell command string and returns a structured event ready for execution by an external system.*


### _make_config (method, L123-L127, parent: TestShellExecution)

> *Summary: Constructs a `TestConfig` object by wrapping the provided command into a `ToolCall` event and pairing it with an optional final reply string. This method prepares configuration data for testing tool execution scenarios.*


### test_allowed_permits_matching_command (method, L130-L137, parent: TestShellExecution)

> *Summary: This test verifies that an agent successfully executes a permitted shell command (`echo hello > out.txt`) using a local shell tool configured with specific allowances. It asserts the existence and correct content of the resulting file written by the executed command.*


### test_allowed_blocks_non_matching_command (method, L140-L146, parent: TestShellExecution)

> *Summary: This test verifies that a shell tool correctly blocks execution of unauthorized commands. It runs an agent configured with a restricted environment (only allowing `echo`) and asserts that the specified command (`touch`) fails to create a target file.*


### test_blocked_rejects_command (method, L151-L156, parent: TestShellExecution)

> *Summary: This test verifies that a command explicitly blocked in the shell environment is rejected by the agent. It runs an agent configured with a restricted `LocalShellTool` and asserts that the expected file creation does not occur when attempting to run the forbidden command.*


### test_env_merged_not_replaced (method, L161-L190, parent: TestShellExecution)

> *Summary: This test verifies that custom environment variables are added to, rather than replacing, the system's existing environment when executing a shell command via `LocalShellTool`. It runs a Python script using an agent and asserts that both the custom variable value and parts of the original `PATH` are present in the output.*


### test_timeout_returns_string_not_exception (method, L195-L211, parent: TestShellExecution)

> *Summary: This test verifies that when a shell command exceeds the configured timeout, the execution returns an error string instead of raising an exception. It runs a long-running `sleep` command via an agent and asserts the resulting reply content is "done" while confirming the expected output file was never created.*


### test_ignore_blocks_env_file (method, L216-L230, parent: TestShellExecution)

> *Summary: This test verifies that a local shell tool respects environment file exclusion patterns. It sets up an agent to attempt reading a `.env` file, asserting that the resulting output explicitly denies access and does not leak any file contents.*


### test_exit_code_included_on_failure (method, L235-L246, parent: TestShellExecution)

> *Summary: This test verifies that when a command fails, the resulting tool output explicitly includes the exit code. It runs an agent using a local shell tool configured to fail with exit code 42 and asserts that "exit code: 42" is present in the captured results.*


### test_exit_code_absent_on_success (method, L249-L260, parent: TestShellExecution)

> *Summary: Verifies that a successful command execution via the local shell does not produce an output containing an explicit exit code. It runs an agent with a configured shell tool and asserts that the captured result string lacks any mention of "exit code".*


### test_files_persist_between_ask_calls (method, L265-L301, parent: TestShellExecution)

> *Summary: This test verifies that files created by a shell tool persist across multiple agent interactions. It executes a command to write data to a file, then subsequently reads the content of that same file in a later call to confirm persistence.*


### test_output_truncated_when_exceeds_limit (method, L306-L322, parent: TestShellExecution)

> *Summary: This test verifies that the shell tool correctly truncates its output when it exceeds a predefined limit (`max_output=20`). It executes a command generating 100 characters and asserts that the resulting captured string contains a truncation note and is exactly 20 characters long.*


### test_output_not_truncated_within_limit (method, L325-L336, parent: TestShellExecution)

> *Summary: This test verifies that when a shell command produces output shorter than the configured limit, the full content is returned without any truncation notification. It executes an agent using a local shell tool and asserts that the captured result string does not contain the word "truncated".*


### test_timeout_returns_exit_code_124 (method, L341-L352, parent: TestShellExecution)

> *Summary: This test verifies that when a command times out within the `LocalShellTool`, the resulting output correctly reports an exit code of 124, adhering to Unix conventions. It achieves this by running a deliberately long-running process via an agent and asserting the captured tool result contains the expected timeout code.*


### test_readonly_blocks_write_commands (method, L357-L363, parent: TestShellExecution)

> *Summary: This test verifies that write operations are prevented when a filesystem is mounted as read-only. It initializes an agent with a shell tool configured for a read-only temporary directory and asserts that attempting to create a file within it fails.*


### test_readonly_allows_read_commands (method, L366-L379, parent: TestShellExecution)

> *Summary: This test verifies that a shell configured as read-only still permits commands like `cat` and `ls`. It executes an agent request against a local shell instance, asserting that the output from reading a file is successfully captured.*


### test_readonly_overridden_by_explicit_allowed (method, L382-L394, parent: TestShellExecution)

> *Summary: This test verifies that an explicit allowance for a specific operation overrides a global read-only restriction within the shell environment. It confirms that if `allowed` is set, the agent can successfully execute commands like `touch`, even when `readonly=True`.*


### test_workdir_in_tool_description (method, L399-L405, parent: TestShellExecution)

> *Summary: This test verifies that the working directory path is correctly included within the function description provided by a local shell tool. It initializes the tool with a temporary path and asserts that this path string appears in the generated schema's description.*

