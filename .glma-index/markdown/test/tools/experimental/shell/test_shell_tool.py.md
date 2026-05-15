# test/tools/experimental/shell/test_shell_tool.py

8 class(es): TestCmdResult, TestShellExecutorInit, TestShellExecutorValidatePath, TestShellExecutorValidateCommand, TestShellExecutorRun, TestShellExecutorRunCommands, TestShellExecutorIntegration, TestShellInjectionPrevention. 60 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestCmdResult | class |  |
| TestShellExecutorInit | class |  |
| TestShellExecutorValidatePath | class |  |
| TestShellExecutorValidateCommand | class |  |
| TestShellExecutorRun | class |  |
| TestShellExecutorRunCommands | class |  |
| TestShellExecutorIntegration | class |  |
| TestShellInjectionPrevention | class |  |

## Chunks

### TestCmdResult (class, L17-L52)

> *Summary: This class provides unit tests to verify the correct initialization and behavior of a `CmdResult` object. It validates that instances can be created with various combinations of standard output, standard error, exit code (including `None`), and timeout status.*


### test_cmd_result_initialization (method, L20-L32, parent: TestCmdResult)

> *Summary: Verifies that an instance of `CmdResult` correctly stores provided values for standard output, standard error, exit code, and timeout status upon initialization. It confirms the object's internal state matches the input parameters.*


### test_cmd_result_with_none_exit_code (method, L34-L44, parent: TestCmdResult)

> *Summary: Verifies that a `CmdResult` object correctly stores and exposes `None` for the exit code while indicating a timeout occurred. It asserts the state of an instance initialized with specific values, including `stdout`, empty `stderr`, `exit_code=None`, and `timed_out=True`.*


### test_cmd_result_empty_strings (method, L46-L52, parent: TestCmdResult)

> *Summary: Verifies that a `CmdResult` object correctly stores and exposes empty strings for standard output and error when initialized with them, alongside a specific exit code. It confirms the internal state matches the provided input values.*


### TestShellExecutorInit (class, L60-L175)

> *Summary: This test suite verifies the initialization behavior of a shell execution object by testing various configurations. It confirms that default values are correctly applied, and that custom inputs for timeout, workspace directory, path/command whitelists/blacklists, and dangerous patterns are properly set on the resulting instance.*


### test_init_with_defaults (method, L63-L73, parent: TestShellExecutorInit)

> *Summary: Verifies that a newly instantiated `ShellExecutor` object correctly initializes with predefined default settings for timeout, workspace directory, allowed paths, and command filtering configurations. It asserts specific values for these attributes against expected defaults.*


### test_init_with_custom_timeout (method, L75-L79, parent: TestShellExecutorInit)

> *Summary: Verifies that the `ShellExecutor` correctly initializes and stores a specified custom default timeout value upon instantiation. It confirms the internal state matches the provided input argument.*


### test_init_with_workspace_dir_string (method, L81-L86, parent: TestShellExecutorInit)

> *Summary: Verifies that initializing a `ShellExecutor` with a temporary directory string correctly sets the internal workspace path to its resolved, absolute form. The test uses a `tempfile.TemporaryDirectory` context manager as input and asserts the resulting `workspace_dir` attribute matches the expected absolute path.*


### test_init_with_workspace_dir_path (method, L88-L93, parent: TestShellExecutorInit)

> *Summary: Verifies that the `ShellExecutor` correctly initializes its workspace directory when provided a `pathlib.Path` object pointing to a temporary directory. It confirms the internal `workspace_dir` attribute matches the resolved path of the input temporary directory.*


### test_init_with_nonexistent_workspace_dir (method, L95-L102, parent: TestShellExecutorInit)

> *Summary: Verifies that the `ShellExecutor` correctly initializes its internal workspace directory even when provided a path to a non-existent location. It confirms the executor stores the resolved path and that the initial temporary directory structure remains intact.*


### test_init_with_allowed_paths (method, L104-L108, parent: TestShellExecutorInit)

> *Summary: Verifies that a `ShellExecutor` instance correctly initializes and stores the provided list of allowed file paths, in this case, `"src/**"` and `"tests/**"`. The method confirms the internal state matches the input configuration.*


### test_init_with_none_allowed_paths (method, L110-L114, parent: TestShellExecutorInit)

> *Summary: When initialized with `allowed_paths=None`, the executor automatically sets its internal `allowed_paths` attribute to `["**"]`. This test verifies that this default behavior is correctly implemented for path restrictions.*


### test_init_with_allowed_commands (method, L116-L120, parent: TestShellExecutorInit)

> *Summary: Verifies that a `ShellExecutor` instance correctly initializes and stores the provided list of permitted shell commands. It confirms the internal state matches the input whitelist during object creation.*


### test_init_with_denied_commands (method, L122-L126, parent: TestShellExecutorInit)

> *Summary: Verifies that a `ShellExecutor` instance correctly initializes and stores a provided list of forbidden commands. It confirms the internal `denied_commands` attribute matches the input blacklist.*


### test_init_with_none_denied_commands (method, L128-L132, parent: TestShellExecutorInit)

> *Summary: When initialized with `None` for `denied_commands`, the executor sets its internal list of forbidden commands to an empty list. This test verifies that passing `None` results in a default, empty configuration for denied commands.*


### test_init_with_disable_command_filtering (method, L134-L138, parent: TestShellExecutorInit)

> *Summary: Verifies that initializing a `ShellExecutor` with `enable_command_filtering=False` correctly sets the internal filtering state to false. This test confirms the constructor's behavior when command filtering is explicitly disabled upon instantiation.*


### test_init_with_custom_dangerous_patterns (method, L140-L147, parent: TestShellExecutorInit)

> *Summary: Verifies that a `ShellExecutor` instance correctly initializes with a provided list of custom dangerous patterns, specifically checking the internal storage matches the input configuration.*


### test_init_with_none_dangerous_patterns (method, L149-L153, parent: TestShellExecutorInit)

> *Summary: When initialized with `None` for `dangerous_patterns`, the executor automatically adopts the predefined default set of dangerous patterns. This test verifies that passing `None` correctly triggers the use of the class's standard configuration.*


### test_init_with_all_parameters (method, L155-L175, parent: TestShellExecutorInit)

> *Summary: Verifies that a `ShellExecutor` instance correctly initializes and stores all provided configuration parameters, including timeouts, directory paths, allowed/denied commands, and custom pattern lists. It uses a temporary directory to ensure the executor is set up with a valid workspace during testing.*


### TestShellExecutorValidatePath (class, L183-L254)

> *Summary: This test suite validates the path validation logic of a shell executor by testing various scenarios for `_validate_path`. It confirms that paths are correctly allowed or rejected based on wildcard matching, containment within a specified workspace directory, and handling of absolute versus relative inputs.*


### test_validate_path_with_wildcard_allows_all (method, L186-L192, parent: TestShellExecutorValidatePath)

> *Summary: This test verifies that the path validation mechanism accepts any input when `allowed_paths` is set to `"**"`. It asserts that various absolute and relative paths return `True` from the internal validation method.*


### test_validate_path_within_workspace (method, L194-L203, parent: TestShellExecutorValidatePath)

> *Summary: This test verifies that the internal path validation method correctly permits paths located inside a designated workspace directory, both when provided as an absolute and relative path string. It uses a temporary directory to simulate the execution environment for testing this boundary condition.*


### test_validate_path_outside_workspace (method, L205-L213, parent: TestShellExecutorValidatePath)

> *Summary: This test verifies that the path validation mechanism correctly rejects file paths located outside the designated workspace directory. It uses temporary directories to simulate an external location and asserts that `_validate_path` returns `False` for such a path.*


### test_validate_path_with_pattern_matching (method, L215-L236, parent: TestShellExecutorValidatePath)

> *Summary: This test verifies that a path validation mechanism correctly allows files matching predefined patterns (`src/**`, `tests/*.py`) within a temporary workspace while rejecting others. It confirms the internal method returns `True` for allowed paths and `False` for disallowed ones.*


### test_validate_path_absolute_path (method, L238-L246, parent: TestShellExecutorValidatePath)

> *Summary: This test verifies that the path validation mechanism correctly accepts absolute paths. It creates a temporary directory, sets up an executor with broad path permissions, and asserts that a fully resolved absolute file path passes validation.*


### test_validate_path_relative_path (method, L248-L254, parent: TestShellExecutorValidatePath)

> *Summary: Verifies that the internal path validation correctly resolves a simple relative path like "test.txt" against a temporary working directory provided to the shell executor. The test asserts that this resolution succeeds when using `**` as an allowed path pattern.*


### TestShellExecutorValidateCommand (class, L262-L404)

> *Summary: This test suite verifies the command validation logic of a shell executor by testing various security constraints. It ensures that commands are rejected if they are empty, use disallowed binaries (via whitelists/blacklists), contain dangerous patterns, or attempt to access unauthorized file paths based on configured workspace rules.*


### test_validate_command_empty_command (method, L265-L273, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that the `_validate_command` method throws a `ValueError` when provided with an empty string or a string containing only whitespace. It ensures the executor rejects commands lacking actual content.*


### test_validate_command_with_allowed_commands_whitelist (method, L275-L289, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that a command validation mechanism correctly permits execution only if the primary command is present in a predefined whitelist. It asserts that valid inputs pass while invalid commands raise a `ValueError` indicating they are not permitted.*


### test_validate_command_with_denied_commands_blacklist (method, L291-L304, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that the command validation mechanism correctly rejects inputs containing specific blacklisted commands like "rm" and "dd". It asserts that attempting to execute these denied commands raises a `ValueError`, while allowing safe commands such as "ls -la" to pass validation.*


### test_validate_command_with_full_path (method, L306-L316, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that a command validation utility correctly extracts the base command name from a full path input and enforces restrictions based on allowed or denied command lists. It asserts successful extraction for `/usr/bin/ls` while expecting a `ValueError` when an explicitly denied command like `rm` is used.*


### test_validate_command_dangerous_patterns (method, L318-L333, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that the `ShellExecutor` correctly rejects predefined malicious shell commands when command filtering is enabled. It iterates through a list of destructive commands and asserts that calling `_validate_command` raises a `ValueError` for each one.*


### test_validate_command_with_filtering_disabled (method, L335-L341, parent: TestShellExecutorValidateCommand)

> *Summary: When command filtering is explicitly disabled, the validation process bypasses pattern matching for commands. This test confirms that a potentially dangerous command like `rm -rf /tmp/test` passes validation under these specific conditions.*


### test_validate_command_path_validation (method, L343-L371, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that the command execution tool correctly restricts file access based on predefined allowed paths. It asserts that commands referencing files within the designated `src/**` pattern succeed, while commands attempting to access external or parent directories fail with a specific `ValueError`.*


### test_validate_command_path_validation_with_wildcard (method, L373-L380, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that the command path validation mechanism bypasses checks when `allowed_paths` is set to `"**"`. It confirms that executing commands with arbitrary paths, like `cat /any/path/file.txt`, succeeds without triggering path restrictions.*


### test_validate_command_with_tilde_path (method, L382-L388, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that the command validation mechanism correctly expands tilde (`~`) paths within a shell command string. It initializes an executor in a temporary directory and asserts successful validation when provided with a path like `~/file.txt`.*


### test_validate_command_path_validation_windows_style (method, L390-L404, parent: TestShellExecutorValidateCommand)

> *Summary: This test verifies that the command validation mechanism correctly rejects Windows-style absolute paths when they fall outside predefined allowed directories. It asserts that attempting to execute commands referencing system or user paths like `C:\Windows\...` raises a `ValueError`.*


### TestShellExecutorRun (class, L412-L511)

> *Summary: This suite of tests verifies the `ShellExecutor`'s execution capabilities by running various shell commands. It validates successful command execution, capturing standard error and non-zero exit codes, handling custom timeouts, operating within a specified directory, and enforcing security restrictions via whitelisting/blacklisting dangerous or denied commands.*


### test_run_simple_command (method, L415-L424, parent: TestShellExecutorRun)

> *Summary: This test verifies that executing a basic shell command, like `echo hello`, succeeds correctly. It asserts the standard output matches "hello", there is no error output, and the process exits with code zero without timing out.*


### test_run_command_with_stderr (method, L426-L437, parent: TestShellExecutorRun)

> *Summary: This test verifies that the shell execution tool correctly captures output written to standard error (`stderr`). It executes a Python command designed to print "hello" to stderr and asserts that the resulting object contains this string in its `stderr` attribute with an exit code of zero.*


### test_run_command_with_nonzero_exit (method, L439-L447, parent: TestShellExecutorRun)

> *Summary: This test verifies that the shell execution tool correctly captures non-zero exit codes from a failing command. It executes `"false"` and asserts that the returned result's `exit_code` is 1 while confirming no timeout occurred.*


### test_run_with_custom_timeout (method, L449-L457, parent: TestShellExecutorRun)

> *Summary: Verifies that a shell execution can successfully complete when provided with a short, custom `timeout` parameter, even if the executor has a longer default timeout configured. It asserts the command output matches expectations and confirms no timeout occurred.*


### test_run_with_default_timeout (method, L459-L466, parent: TestShellExecutorRun)

> *Summary: Verifies that the `ShellExecutor` uses its configured default timeout when no specific timeout is provided during execution. It runs a simple command and asserts that the output is correct and no timeout occurred.*


### test_run_in_workspace_directory (method, L468-L481, parent: TestShellExecutorRun)

> *Summary: This test verifies that shell commands executed by `ShellExecutor` operate within a specified workspace directory. It creates a file in the temporary directory and asserts that running `cat test.txt` successfully reads and outputs the file's content with an exit code of zero.*


### test_run_blocks_dangerous_command (method, L483-L488, parent: TestShellExecutorRun)

> *Summary: This test verifies that the shell executor prevents execution of harmful commands by asserting a `ValueError` is raised when attempting to run `"rm -rf /"`. It uses an instance of `ShellExecutor` to trigger this safety check.*


### test_run_blocks_denied_command (method, L490-L495, parent: TestShellExecutorRun)

> *Summary: This test verifies that attempting to execute a command listed in `denied_commands` raises a `ValueError`. It initializes an executor with `"rm"` as a forbidden command and asserts that running `"rm file.txt"` triggers the expected exception.*


### test_run_blocks_command_not_in_whitelist (method, L497-L502, parent: TestShellExecutorRun)

> *Summary: This test verifies that attempting to execute a command not present in the predefined whitelist raises a `ValueError`. It initializes an executor with specific allowed commands and asserts failure when running an unauthorized command like "rm".*


### test_run_allows_command_in_whitelist (method, L504-L511, parent: TestShellExecutorRun)

> *Summary: Verifies that the shell execution allows commands listed in a predefined whitelist; it runs `"echo test"` through an executor configured with `["echo", "ls"]` and asserts the output is `"test"` with a zero exit code.*


### TestShellExecutorRunCommands (class, L519-L624)

> *Summary: These tests verify the `run_commands` method of a shell executor by providing various command lists as input and asserting correct outputs, exit codes, and error handling for scenarios like timeouts, failures, security restrictions, and dangerous patterns. The function returns a list of results objects detailing the outcome of each executed command.*


### test_run_commands_single_command (method, L522-L532, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies the `run_commands` functionality when provided with a single command string, expecting one result object containing standard output matching the command's echo and a successful exit code of zero.*


### test_run_commands_multiple_commands (method, L534-L544, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies that the `ShellExecutor` correctly executes a list of multiple shell commands sequentially. It asserts that each command runs successfully, produces the expected standard output, and exits with code zero.*


### test_run_commands_with_timeout_ms (method, L546-L554, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies the `run_commands` method by executing a simple shell command with a specified timeout. It asserts that the execution completes successfully, returns one result, and captures the expected standard output.*


### test_run_commands_with_failing_command (method, L556-L564, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies that the command execution utility correctly processes a failing shell command. It executes `false` and asserts that the resulting output contains one result object indicating an exit type with a code of 1.*


### test_run_commands_mixed_success_and_failure (method, L566-L577, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies that a shell executor correctly processes a sequence of commands containing both successful and failing executions. It asserts the resulting list contains three outcomes, checking stdout content and exit codes for each command in order.*


### test_run_commands_handles_security_violation (method, L579-L595, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies that a shell executor gracefully handles security violations by blocking specified commands while allowing others to execute normally. It inputs a list of mixed commands (one allowed, one denied, one allowed) and asserts the output reflects successful execution for permitted commands and failure/blocking for restricted ones.*


### test_run_commands_with_dangerous_pattern (method, L597-L607, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies that the `ShellExecutor` blocks commands containing dangerous patterns, such as `rm -rf /`. It asserts that the execution returns three results: one successful output, one error indicating a detected danger with an exit code of 1, and a final successful output.*


### test_run_commands_empty_list (method, L609-L615, parent: TestShellExecutorRunCommands)

> *Summary: When provided an empty list of commands, the execution utility returns an empty list of results. This test verifies that running zero commands yields no output.*


### test_run_commands_with_none_timeout (method, L617-L624, parent: TestShellExecutorRunCommands)

> *Summary: This test verifies that `run_commands` correctly executes shell commands when a `None` timeout is provided. It asserts that the execution returns one result containing the expected standard output from the command `"echo test"`.*


### TestShellExecutorIntegration (class, L632-L700)

> *Summary: This test suite verifies the security and functionality of `ShellExecutor` by running integration tests against a temporary workspace. It validates command execution under various restrictions (whitelisting, blacklisting) and confirms that default dangerous patterns are correctly defined within the executor's configuration.*


### test_full_workflow_with_restrictions (method, L635-L680, parent: TestShellExecutorIntegration)

> *Summary: This test verifies a complete execution workflow for a shell tool, demonstrating how security restrictions interact. It uses an `ShellExecutor` configured with whitelists and blacklists to ensure that only permitted commands accessing authorized paths execute successfully, while blocked operations correctly return errors based on the filtering rules applied.*


### test_default_dangerous_patterns_are_defined (method, L682-L700, parent: TestShellExecutorIntegration)

> *Summary: Verifies that the predefined set of dangerous shell patterns exists and adheres to a specific structure (tuples containing two strings). It further asserts that this collection includes regex patterns capable of matching known destructive commands like `rm -rf /` and `dd`.*


### TestShellInjectionPrevention (class, L708-L770)

> *Summary: This test suite verifies that when shell execution is disabled, special characters like `;`, `|`, `&&`, `$()`, `` ` `` , and `>` are treated as literal arguments rather than active shell operators. It uses a `ShellExecutor` to run commands and asserts that file system modifications or command chaining do not occur when these metacharacters are present in the input string.*


### test_semicolon_does_not_chain_commands (method, L715-L725, parent: TestShellInjectionPrevention)

> *Summary: This test verifies that semicolons within a command string are treated as literal characters rather than shell command separators. It executes `echo hello ; touch pwned.txt` and asserts that the file creation fails, confirming the semicolon's literal interpretation.*


### test_pipe_does_not_chain_commands (method, L727-L736, parent: TestShellInjectionPrevention)

> *Summary: This test verifies that the `ShellExecutor` treats pipe characters (`|`) as literal arguments rather than executing them as shell operators. It runs a command containing a pipe and asserts that the resulting file does not exist, confirming the input is not being chained by the shell.*


### test_and_operator_does_not_chain_commands (method, L738-L747, parent: TestShellInjectionPrevention)

> *Summary: This test verifies that the `ShellExecutor` treats the `&&` sequence within a command string as literal arguments rather than executing it as a shell logical AND operator. It asserts that a file created by the second part of the command does not exist when running `echo hello && touch pwned.txt`.*


### test_subshell_substitution_does_not_execute (method, L749-L753, parent: TestShellInjectionPrevention)

> *Summary: This test verifies that command substitution syntax (`$(...)`) within a shell execution is treated as literal text rather than being evaluated by the shell. It runs `echo $(whoami)` and asserts that the output string still contains the unexecuted `$()` pattern.*


### test_backtick_substitution_does_not_execute (method, L755-L759, parent: TestShellInjectionPrevention)

> *Summary: This test verifies that backtick substitutions within a shell command are treated as literal text rather than being executed by the shell. It runs an `echo` command containing `` `whoami` `` and asserts that the output string includes the exact sequence `` "`whoami`" ``.*


### test_redirect_does_not_write_file (method, L761-L770, parent: TestShellInjectionPrevention)

> *Summary: This test verifies that the `ShellExecutor` treats the `>` character in a command string literally, rather than executing it as a file redirection operator. It runs an `echo` command attempting to write to a temporary file and asserts that the target file does not exist afterward.*

