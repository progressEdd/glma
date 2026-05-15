# test/tools/experimental/google/drive/test_path_traversal.py

2 class(es): TestDriveSubfolderPathTraversal, TestDriveFileNamePathTraversal. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDriveSubfolderPathTraversal | class |  |
| TestDriveFileNamePathTraversal | class |  |

## Chunks

### TestDriveSubfolderPathTraversal (class, L21-L57)

> *Summary: This test suite verifies that a path validation function correctly prevents directory traversal attacks. It asserts that inputs containing sequences like `../` or excessive parent directories will raise a `ValueError`, while legitimate, contained subfolder paths are allowed.*


### test_parent_traversal_blocked (method, L24-L29, parent: TestDriveSubfolderPathTraversal)

> *Summary: This test verifies that path traversal attempts escaping the designated download directory are rejected. It asserts a `ValueError` is raised when attempting to resolve a path like `../../.ssh` within the provided folder structure.*


### test_relative_outside_blocked (method, L31-L36, parent: TestDriveSubfolderPathTraversal)

> *Summary: This test verifies that attempting to resolve a path outside the designated download directory fails validation. It asserts that passing a relative path like `../outside` when validating against a specific folder raises a `ValueError`.*


### test_double_dot_deep_traversal_blocked (method, L38-L43, parent: TestDriveSubfolderPathTraversal)

> *Summary: This test verifies that path traversal attempts using multiple parent directory references (`../..`) are blocked when validating a download path. It asserts that calling `_validate_download_path` with an input path escaping the designated folder raises a `ValueError`.*


### test_normal_subfolder_allowed (method, L45-L50, parent: TestDriveSubfolderPathTraversal)

> *Summary: This test verifies that a path within an allowed subfolder is correctly validated as safe. It calls `_validate_download_path` with a base download directory and a subdirectory, asserting the resulting resolved path remains under the original base folder.*


### test_nested_legitimate_subfolder_allowed (method, L52-L57, parent: TestDriveSubfolderPathTraversal)

> *Summary: This test verifies that paths nested within a designated download folder are permitted. It calls `_validate_download_path` with a base directory and a deeply nested relative path, asserting the resulting resolved path remains under the original download folder.*


### TestDriveFileNamePathTraversal (class, L60-L97)

> *Summary: This test suite validates that a path validation function correctly prevents directory traversal attacks when processing file names intended for download. It asserts that inputs containing `..` sequences are rejected with a `ValueError`, while legitimate filenames and paths within the designated download folder are accepted.*


### test_file_traversal_via_dotdot_blocked (method, L63-L68, parent: TestDriveFileNamePathTraversal)

> *Summary: This test verifies that path traversal attempts using `..` are blocked during download path validation. It asserts that calling the validation function with a malicious input like `"../../.ssh/authorized_keys"` raises a `ValueError`.*


### test_parent_only_traversal_blocked (method, L70-L75, parent: TestDriveFileNamePathTraversal)

> *Summary: Asserts that attempting to use path traversal sequences like `../../../etc/passwd` in a download filename raises a `ValueError`. This test verifies the security mechanism prevents accessing files outside the intended directory structure.*


### test_normal_filename_allowed (method, L77-L82, parent: TestDriveFileNamePathTraversal)

> *Summary: This test verifies that a standard filename like "clip.mp4" is permitted when validating a download path within a temporary directory structure. It calls `_validate_download_path` with a base folder and the target file name, asserting the returned object retains the original filename.*


### test_filename_in_root_download_folder_allowed (method, L84-L89, parent: TestDriveFileNamePathTraversal)

> *Summary: This test verifies that a file placed directly within the root download folder is permitted for download validation. It creates a temporary downloads directory and asserts that a specified filename in that root location passes validation.*


### test_file_and_subfolder_combined_allowed (method, L91-L97, parent: TestDriveFileNamePathTraversal)

> *Summary: Validates that a path combining a legitimate subfolder and a filename is permitted by the download validation logic. It checks if the resulting resolved path remains within the specified base download directory.*

