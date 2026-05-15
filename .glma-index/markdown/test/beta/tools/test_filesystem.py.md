# test/beta/tools/test_filesystem.py

13 function(s): test_path_traversal_blocked, test_absolute_path_blocked, test_allow_only_dir, test_schemas, test_read_only, test_read_file, test_read_file_raw, test_write_file, test_write_creates_parent_dirs, test_update_file and 3 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_path_traversal_blocked | function |  |
| test_absolute_path_blocked | function |  |
| test_allow_only_dir | function |  |
| test_schemas | function |  |
| test_read_only | function |  |
| test_read_file | function |  |
| test_read_file_raw | function |  |
| test_write_file | function |  |
| test_write_creates_parent_dirs | function |  |
| test_update_file | function |  |
| test_delete_file | function |  |
| test_delete_directory | function |  |
| test_find_files | function |  |

## Chunks

### test_path_traversal_blocked (function, L19-L21)

> *Summary: Asserts that attempting to resolve a path traversal sequence like `../../etc/passwd` against a temporary directory raises a `PermissionError`. This verifies the system correctly blocks access outside of the designated base directory.*


### test_absolute_path_blocked (function, L24-L26)

> *Summary: Asserts that attempting to resolve a path using an absolute input like `/etc/passwd` from a temporary directory raises a `PermissionError`. This verifies the system prevents escaping the designated base directory.*


### test_allow_only_dir (function, L29-L31)

> *Summary: Asserts that attempting to initialize the filesystem toolkit with a file path raises a `ValueError` containing "is not a directory". This verifies the tool enforces that only directories can be used for initialization.*


### test_schemas (function, L35-L46)

> *Summary: This test verifies that a `FilesystemToolkit` instance returns all expected file system operation schemas when provided with an asynchronous mock context. It asserts that the set of function names derived from these returned schemas matches a predefined list of core file operations.*


### test_read_only (function, L50-L55)

> *Summary: When initialized with `read_only=True`, the filesystem toolkit is tested to ensure it only exposes specific read-only functions, namely `"read_file"` and `"find_files"`, when queried for available schemas.*


### test_read_file (function, L59-L78)

> *Summary: This test verifies file reading functionality by creating a temporary file, initializing an agent with a filesystem toolkit, and then prompting the agent to read the file. It asserts that the subsequent tool result correctly contains the expected content from the written file.*


### test_read_file_raw (function, L82-L101)

> *Summary: This test verifies the raw file reading capability of a filesystem tool by writing specific binary data to a temporary path. It then executes an agent request to read this file and asserts that the returned, base64-decoded content matches the original input bytes.*


### test_write_file (function, L105-L118)

> *Summary: This test verifies file writing functionality by initializing an agent with a filesystem toolkit and instructing it to write content to a specific path within a temporary directory. It asserts that the resulting file contains the expected string after the agent executes the tool call.*


### test_write_creates_parent_dirs (function, L122-L135)

> *Summary: This test verifies that writing a file to a deeply nested path automatically creates all necessary parent directories. It initializes an agent with a filesystem toolkit and asserts the content of the newly created, nested file after executing a write command.*


### test_update_file (function, L139-L154)

> *Summary: This test verifies that an agent correctly uses a filesystem tool to modify file content. It initializes a toolkit with a temporary directory, configures the agent to call `update_file` on a specific path, and asserts the resulting file content reflects the update.*


### test_delete_file (function, L158-L173)

> *Summary: This test verifies file deletion by creating a temporary file within a directory structure. It then uses an agent configured with a filesystem toolkit to execute the `delete_file` tool call, asserting that the target file no longer exists afterward.*


### test_delete_directory (function, L177-L192)

> *Summary: This test verifies that an agent successfully deletes a directory and its contents using a provided filesystem toolkit. It sets up a temporary structure, instructs the agent to delete a subdirectory, and asserts that the target file within that directory no longer exists afterward.*


### test_find_files (function, L196-L242)

> *Summary: This test sets up a mock filesystem structure and uses an agent with a `FilesystemToolkit` to verify the behavior of its `find_files` tool. It asserts that the tool correctly returns file paths based on different glob patterns, such as recursive (`**/*.py`), non-recursive (`sub/*`), and deep recursive (`sub/**`).*

