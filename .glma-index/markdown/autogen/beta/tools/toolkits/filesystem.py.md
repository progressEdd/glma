# autogen/beta/tools/toolkits/filesystem.py

4 function(s): _resolve_dir, _resolve_path, _glob, _glob. 1 class(es): FilesystemToolkit. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FilesystemToolkit | class |  |
| _resolve_dir | function |  |
| _resolve_path | function |  |
| _glob | function |  |
| _glob | function |  |

## Chunks

### FilesystemToolkit (class, L20-L214)

> *Summary: Provides a set of function tools for interacting with the local filesystem, operating within a specified base directory and enforcing path traversal guards. It exposes methods to read (text or binary), find files via glob patterns, write/overwrite content, update specific text occurrences, and delete files or directories.*


### __init__ (method, L47-L72, parent: FilesystemToolkit)

> *Summary: Initializes a filesystem toolkit by setting a base directory and dynamically assembling a set of available file system operations. It includes read-only tools by default, adding write, update, and delete capabilities only if `read_only` is false.*


### read_file (method, L74-L100, parent: FilesystemToolkit)

> *Summary: Provides a callable tool that reads the content of a specified file within a given directory context. It accepts a relative path and an optional boolean flag to return either decoded text or base64-encoded binary data.*


### find_files (method, L102-L126, parent: FilesystemToolkit)

> *Summary: Generates a callable tool that searches for files matching a glob pattern within a specified directory structure. It takes a file pattern and an optional starting path as input, returning a sorted list of relative paths to the found files.*


### write_file (method, L128-L154, parent: FilesystemToolkit)

> *Summary: This method generates a callable tool that writes string content to a specified file path within a base directory. It automatically creates necessary parent directories and returns a success message indicating the written character count and file location.*


### update_file (method, L156-L188, parent: FilesystemToolkit)

> *Summary: This method generates a tool that modifies a file by replacing only the first instance of specified text within it. It takes a relative path, the content to find, and the replacement content as inputs, returning a success message upon modification.*


### delete_file (method, L190-L214, parent: FilesystemToolkit)

> *Summary: This method generates a tool that deletes a specified file or directory within a configured base path. It takes a relative path as input and returns a success message upon completion of the deletion operation.*


### _resolve_dir (function, L217-L224)

> *Summary: Resolves an input path to an absolute, canonical directory path. If the provided argument is null, it defaults to using the specified toolkit path; otherwise, it validates that the resulting path exists and is a directory before returning it.*


### _resolve_path (function, L227-L232)

> *Summary: This utility resolves a given string path relative to a specified base directory, ensuring the resulting absolute path remains strictly within the confines of that base directory. It raises a `PermissionError` if the resolution attempts to escape the designated base folder.*


### _glob (function, L237-L239)

> *Summary: This helper function yields file paths found within a specified directory that match a given glob pattern, ensuring consistent cross-version behavior. It takes a `Path` object and a string pattern as input and returns an iterable of matching `Path` objects.*


### _glob (function, L243-L260)

> *Summary: This utility yields file paths matching a given pattern within a target directory, providing compatibility for older Python versions lacking full `**` globbing support. It specifically handles patterns containing `**` by manually expanding them to find all matching files recursively or at the root level.*

