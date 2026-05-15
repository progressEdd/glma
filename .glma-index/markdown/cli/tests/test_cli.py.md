# cli/tests/test_cli.py

7 class(es): TestCLIBasics, TestCreateSubcommands, TestInstallSubcommands, TestTestSubcommands, TestRunCommand, TestChatCommand, TestServeCommand. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestCLIBasics | class |  |
| TestCreateSubcommands | class |  |
| TestInstallSubcommands | class |  |
| TestTestSubcommands | class |  |
| TestRunCommand | class |  |
| TestChatCommand | class |  |
| TestServeCommand | class |  |

## Chunks

### TestCLIBasics (class, L11-L30)

> *Summary: This test suite verifies the basic functionality of a CLI application by invoking it with specific arguments. It asserts that `--help` displays all registered commands, `--version` outputs the correct version string, and running without arguments shows the main banner.*


### test_help_shows_all_commands (method, L12-L20, parent: TestCLIBasics)

> *Summary: Verifies that invoking the application with `--help` returns a successful exit code and includes documentation for all defined commands (`install`, `create`, `run`, `chat`, `serve`, `test`) in its output.*


### test_version_flag (method, L22-L25, parent: TestCLIBasics)

> *Summary: Verifies that invoking the application with the `--version` flag executes successfully and outputs a string containing "ag2-cli". This test confirms correct behavior for version querying via the CLI runner.*


### test_no_args_shows_banner (method, L27-L30, parent: TestCLIBasics)

> *Summary: When invoked with no arguments, this test verifies that the application exits successfully and displays a banner containing the string "ag2".*


### TestCreateSubcommands (class, L33-L45)

> *Summary: This test suite verifies the help output for a `create` subcommand and its nested `project` subcommand. It asserts that invoking `--help` on these commands displays relevant options like project, agent, tool, team, and template.*


### test_create_help (method, L34-L40, parent: TestCreateSubcommands)

> *Summary: Verifies that invoking the `create --help` command successfully returns an exit code of 0 and includes documentation for 'project', 'agent', 'tool', and 'team' in its output.*


### test_create_project_help (method, L42-L45, parent: TestCreateSubcommands)

> *Summary: Verifies that invoking the `create project --help` command successfully returns an exit code of zero and includes the word "template" in its output. This tests the help message generation for the project creation subcommand.*


### TestInstallSubcommands (class, L48-L59)

> *Summary: This test suite verifies the functionality of installation subcommands by invoking the application with specific arguments. It asserts that help output contains expected sections and that listing targets correctly identifies known entities like "Cursor".*


### test_install_help (method, L49-L54, parent: TestInstallSubcommands)

> *Summary: Verifies that invoking the `install --help` command successfully returns an exit code of zero and includes expected help text like "skills," "list," and "uninstall" in its output.*


### test_install_list_targets (method, L56-L59, parent: TestInstallSubcommands)

> *Summary: Verifies that invoking the `install list targets` command successfully returns an exit code of zero and includes the string "Cursor" (case-insensitive) in its output. This tests the CLI's ability to correctly list available installation targets.*


### TestTestSubcommands (class, L62-L72)

> *Summary: This test suite verifies the CLI's subcommand behavior by invoking specific commands against an application instance. It asserts that requesting help for a command displays relevant sections and confirms that a "bench" subcommand currently outputs a "coming soon" message.*


### test_test_help (method, L63-L67, parent: TestTestSubcommands)

> *Summary: This test verifies the help output for a specific command by invoking it with `--help`. It asserts that the execution succeeds (exit code 0) and that the resulting output contains both "eval" and "bench".*


### test_bench_coming_soon (method, L69-L72, parent: TestTestSubcommands)

> *Summary: Invokes the application with specific arguments to run a benchmark test suite and asserts that the process exits successfully while confirming the output contains a "coming soon" message.*


### TestRunCommand (class, L75-L83)

> *Summary: This class tests the CLI's `run` command behavior by invoking it with various arguments. It asserts that running with a missing file results in a non-zero exit code, while running with `--help` succeeds and outputs a specific message.*


### test_run_missing_file (method, L76-L78, parent: TestRunCommand)

> *Summary: Asserts that invoking the application with a non-existent file path results in a non-zero exit code, confirming proper error handling for missing inputs.*


### test_run_help (method, L80-L83, parent: TestRunCommand)

> *Summary: This test verifies that invoking the `run` command with `--help` returns a successful exit code and contains specific help message text in its output. It uses an existing runner instance to execute the application command.*


### TestChatCommand (class, L86-L94)

> *Summary: This test suite verifies the command-line interface behavior for the `chat` subcommand. It asserts that invoking `chat` without arguments results in a non-zero exit code (an error), while invoking it with `--help` succeeds and displays model information.*


### test_chat_no_args_shows_error (method, L87-L89, parent: TestChatCommand)

> *Summary: This test verifies that invoking the chat command without any arguments results in a non-zero exit code, indicating an expected error state. It uses a provided `runner` to execute the application with only the "chat" argument.*


### test_chat_help (method, L91-L94, parent: TestChatCommand)

> *Summary: Verifies that invoking the `chat --help` command successfully returns an exit code of zero and includes the word "model" in its output. This tests the help message functionality for the chat feature.*


### TestServeCommand (class, L97-L107)

> *Summary: Tests verify the behavior of the `serve` command-line interface. Specifically, it checks that `--help` displays relevant options like port and protocol, and asserts that using the "mcp" protocol without a valid input file results in an error exit code.*


### test_serve_help (method, L98-L102, parent: TestServeCommand)

> *Summary: This test verifies that invoking the `serve --help` command successfully returns an exit code of zero and includes expected help text like "port" and "protocol" in its output. It confirms the CLI correctly displays usage information when requested.*


### test_serve_mcp_requires_file (method, L104-L107, parent: TestServeCommand)

> *Summary: When invoking the `serve` command with the `--protocol mcp` flag, this test asserts that the application correctly exits with a non-zero code if no required input file is provided. This verifies the dependency check for MCP protocol functionality.*

