# test/mcp/test_resource_path_traversal.py

1 class(es): TestMCPResourcePathSanitization. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMCPResourcePathSanitization | class |  |

## Chunks

### TestMCPResourcePathSanitization (class, L18-L85)

> *Summary: This test suite verifies that resource URI paths are correctly sanitized to prevent directory traversal attacks when resolving filenames within a designated download folder. It asserts that malicious inputs like `../` or absolute file URIs are stripped down to safe, basename-only files, while valid URIs resolve cleanly inside the provided temporary path.*


### test_absolute_file_uri_sanitized_to_flat_filename (method, L25-L30, parent: TestMCPResourcePathSanitization)

> *Summary: This test verifies that an absolute file URI input is safely sanitized to a flat filename within the provided temporary directory. It asserts that the resulting path resides inside the temporary folder and does not contain sensitive system directories like "etc".*


### test_relative_traversal_uri_sanitized (method, L32-L37, parent: TestMCPResourcePathSanitization)

> *Summary: This test verifies that a resource URI containing path traversal sequences (`../../`) is correctly sanitized by the `_sanitize_resource_filename` function. It asserts that the resulting file's parent directory remains within the provided temporary path and that its name starts with a specific prefix, indicating successful sanitization.*


### test_windows_backslash_traversal_sanitized (method, L39-L42, parent: TestMCPResourcePathSanitization)

> *Summary: This test verifies that a Windows-style backslash traversal attempt is correctly sanitized by the resource filename function. It asserts that after sanitization, the resulting path's parent directory remains within the provided temporary path context.*


### test_nested_path_stripped_to_basename (method, L44-L48, parent: TestMCPResourcePathSanitization)

> *Summary: When provided with a deeply nested URI path and a timestamp, this test verifies that the sanitization process strips all directory components, leaving only the base filename prefixed by a timestamp. The function returns a file-like object whose parent is the temporary directory and whose name starts with the expected prefix.*


### test_empty_path_component_uses_fallback_name (method, L50-L54, parent: TestMCPResourcePathSanitization)

> *Summary: When provided with a URI lacking a path component, this test verifies that the sanitization process defaults to using a fallback name prefixed with "resource\_". It asserts that the resulting file resides in the base temporary directory and starts with the expected fallback naming convention.*


### test_normal_flat_filename_uri_works (method, L60-L64, parent: TestMCPResourcePathSanitization)

> *Summary: This test verifies that a standard, flat resource URI resolves correctly within a temporary directory structure. It asserts that the resulting file path is directly under the provided temporary path and contains the expected filename.*


### test_simple_filename_uri_works (method, L66-L70, parent: TestMCPResourcePathSanitization)

> *Summary: Verifies that a simple `file://` URI without directory components is correctly sanitized to point within the provided temporary path. It asserts that the resulting resource's parent matches the input temporary path and its name contains the expected filename.*


### test_timestamp_appended_to_filename (method, L72-L75, parent: TestMCPResourcePathSanitization)

> *Summary: This test verifies that a provided timestamp is correctly appended as a suffix to the sanitized resource filename. It takes a base path and a specific timestamp string as input, asserting the resulting file name includes both the original name and the timestamp.*


### test_result_is_absolute_path (method, L77-L80, parent: TestMCPResourcePathSanitization)

> *Summary: This test verifies that the output of sanitizing a resource filename results in an absolute path. It takes a temporary directory path as input and asserts that the returned path object is fully resolved.*


### test_result_is_relative_to_download_folder (method, L82-L85, parent: TestMCPResourcePathSanitization)

> *Summary: This test verifies that the sanitized resource path returned by `_sanitize_resource_filename` is always located within the provided temporary directory. It asserts that the resulting path is a descendant of the base download folder.*

