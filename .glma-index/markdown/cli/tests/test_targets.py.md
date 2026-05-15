# cli/tests/test_targets.py

1 function(s): _make_item. 7 class(es): TestFormatFrontmatter, TestDirectoryTarget, TestSingleFileTarget, TestClaudeTarget, TestCopilotTarget, TestDetectTargets, TestGetTargetAndGetAllTargets. 19 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_item | function |  |
| TestFormatFrontmatter | class |  |
| TestDirectoryTarget | class |  |
| TestSingleFileTarget | class |  |
| TestClaudeTarget | class |  |
| TestCopilotTarget | class |  |
| TestDetectTargets | class |  |
| TestGetTargetAndGetAllTargets | class |  |

## Chunks

### _make_item (function, L16-L30)

> *Summary: This helper function constructs a `ContentItem` object used specifically for testing purposes. It accepts optional parameters like name, description, category, frontmatter dictionary, and body content to configure the item before returning it.*


### TestFormatFrontmatter (class, L33-L49)

> *Summary: This test suite verifies the `format_frontmatter` utility by checking its behavior with various inputs. It asserts that an empty dictionary yields an empty string, boolean values are correctly formatted as lowercase strings within YAML delimiters, and specific string handling (like quoting) is applied when necessary.*


### test_empty_dict_returns_empty_string (method, L36-L37, parent: TestFormatFrontmatter)

> *Summary: Verifies that when an empty dictionary is provided as input, the formatting function correctly returns an empty string. This confirms expected behavior for handling no metadata.*


### test_booleans_formatted_lowercase (method, L39-L44, parent: TestFormatFrontmatter)

> *Summary: This test verifies that boolean values within frontmatter are correctly formatted as lowercase strings ("true" or "false"). It asserts the resulting string starts and ends with YAML delimiters (`---`) while containing the expected lowercase representations of the input booleans.*


### test_strings_with_special_chars_are_quoted (method, L46-L49, parent: TestFormatFrontmatter)

> *Summary: Verifies that when formatting frontmatter with strings containing special characters, the glob patterns are correctly quoted while plain values remain unquoted. It asserts specific string representations exist within the resulting dictionary structure.*


### TestDirectoryTarget (class, L52-L100)

> *Summary: This test suite verifies the installation and uninstallation logic for a directory target. It confirms that `install` correctly creates prefixed files within a specified rules directory based on input items, and `uninstall` selectively removes only those prefixed files while leaving other existing files untouched.*


### test_install_creates_files_in_correct_directory (method, L55-L77, parent: TestDirectoryTarget)

> *Summary: This test verifies that installing items into a `DirectoryTarget` correctly creates files within the specified rules directory. It asserts that two expected markdown files are generated in the correct location and contain the input content.*


### test_uninstall_removes_files_with_correct_prefix (method, L79-L100, parent: TestDirectoryTarget)

> *Summary: This test verifies that the `uninstall` method of a directory target removes files matching a specific prefix within a rules directory, while leaving unrelated files intact. It asserts that exactly two prefixed files are deleted and one non-prefixed file remains after the uninstallation process.*


### TestSingleFileTarget (class, L103-L193)

> *Summary: These tests verify the installation and uninstallation logic for a single file target, ensuring that new content is correctly injected into or replaces existing sections marked by `AG2_MARKER` within a specified file. The methods confirm proper marker handling during updates, replacement of old sections, and complete removal of the targeted section or file upon uninstallation.*


### test_install_creates_file_with_marker (method, L106-L120, parent: TestSingleFileTarget)

> *Summary: This test verifies that installing a single file target, given a list of items, results in the creation of one output file containing specific markers and the provided item content. It asserts the presence and count of a predefined marker within the resulting file's text.*


### test_install_replaces_existing_ag2_section (method, L122-L140, parent: TestSingleFileTarget)

> *Summary: This test verifies that installing new items into a target correctly replaces any pre-existing AG2 section within the target file. It asserts that the old content is removed, the new item's content is present, and the marker count remains correct after the installation process.*


### test_install_handles_single_marker_corrupted (method, L142-L161, parent: TestSingleFileTarget)

> *Summary: This test verifies that the installation process correctly handles a target file containing only one corrupted marker. It asserts that valid item content is inserted while ensuring the original, incomplete marker structure is entirely removed from the file's contents.*


### test_uninstall_removes_ag2_section (method, L163-L178, parent: TestSingleFileTarget)

> *Summary: This test verifies that calling the `uninstall` method on a target removes specific sections marked by `AG2_MARKER` from an input file. It asserts that exactly one item is removed and that the marker content is absent from the resulting file while preserving other original text.*


### test_uninstall_deletes_file_if_only_ag2_content (method, L180-L193, parent: TestSingleFileTarget)

> *Summary: This test verifies that uninstalling a single file target removes the associated file when its content exclusively contains AG2 markers. It asserts that exactly one item is reported as removed and that the original file no longer exists after the operation.*


### TestClaudeTarget (class, L196-L269)

> *Summary: This test suite verifies the installation and uninstallation logic of a target component. It asserts that installing items correctly creates structured skill and command files within a temporary directory, and that uninstalling removes only those prefixed with "ag2-" while preserving user-defined content.*


### test_install_creates_skill_directory_structure (method, L199-L211, parent: TestClaudeTarget)

> *Summary: When provided with a target instance and a list of skill items, this test verifies that the `install` method correctly creates the expected directory structure within a temporary path. It asserts the existence and content of the generated skill markdown file, confirming proper configuration for invocation.*


### test_install_creates_command_files (method, L213-L227, parent: TestClaudeTarget)

> *Summary: This test verifies that installing a defined target creates corresponding command files within the specified temporary directory structure. It asserts the existence and correct content of the generated Markdown file based on the input item's metadata.*


### test_uninstall_removes_ag2_prefixed_skill_dirs (method, L229-L269, parent: TestClaudeTarget)

> *Summary: This test verifies that the `uninstall` method correctly removes directories and files prefixed with "ag2-" from specified locations, while leaving non-prefixed items untouched. It asserts that specific AG2 skill directories, other AG2 directories, and an AG2 command file are deleted after calling `target.uninstall(tmp_path)`.*


### TestCopilotTarget (class, L272-L310)

> *Summary: This test suite verifies the installation and uninstallation logic for a Copilot target. It asserts that installing items creates specific instruction files with correct content, and uninstalling removes only the relevant generated files while preserving others.*


### test_install_creates_instruction_files (method, L275-L294, parent: TestCopilotTarget)

> *Summary: When provided with a list of target items, this test verifies that the `install` method generates specific instruction files within a temporary directory structure. It asserts the existence and correct content of these generated markdown files based on the input item data.*


### test_uninstall_removes_instruction_files (method, L296-L310, parent: TestCopilotTarget)

> *Summary: This test verifies that the `uninstall` method removes specific instruction files from a temporary directory while preserving others. It asserts that exactly two designated instruction files are deleted after calling `target.uninstall(tmp_path)`.*


### TestDetectTargets (class, L313-L329)

> *Summary: This test verifies that a target detection function correctly identifies specific markers within a given project directory. It asserts that targets like "claude" and "copilot" are found while ensuring an unrelated target, "cursor," is absent from the results.*


### test_detects_correct_targets (method, L316-L329, parent: TestDetectTargets)

> *Summary: This test verifies that a target detection function correctly identifies specific markers within a temporary directory structure. It asserts that targets named "claude" and "copilot" are found, while ensuring an unrelated target like "cursor" is absent from the results.*


### TestGetTargetAndGetAllTargets (class, L332-L356)

> *Summary: These tests verify the functionality of target retrieval utilities, ensuring `get_target` correctly returns a specific target object or `None` if the name is unknown. Additionally, they confirm that `get_all_targets` successfully retrieves and includes expected targets like "claude," "copilot," and "cursor."*


### test_get_target_returns_known_target (method, L335-L341, parent: TestGetTargetAndGetAllTargets)

> *Summary: This test verifies that the `get_target` function correctly retrieves a predefined target when given the input string `"claude"`. It asserts that the returned object is not null and matches the expected name and display name for Claude.*


### test_get_target_returns_none_for_unknown (method, L343-L346, parent: TestGetTargetAndGetAllTargets)

> *Summary: This test verifies that the `get_target` function returns `None` when provided with an unknown target name string. It asserts this behavior by calling the function with `"nonexistent-target"`.*


### test_get_all_targets_returns_all (method, L348-L356, parent: TestGetTargetAndGetAllTargets)

> *Summary: This test verifies that the `get_all_targets` function successfully retrieves a non-empty list of installation targets, ensuring specific targets like "claude," "copilot," and "cursor" are present in the returned collection.*

