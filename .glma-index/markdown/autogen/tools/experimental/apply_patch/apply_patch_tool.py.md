# autogen/tools/experimental/apply_patch/apply_patch_tool.py

1 function(s): apply_diff. 4 class(es): PatchEditor, _V4ADiffApplier, WorkspaceEditor, ApplyPatchTool. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| PatchEditor | class |  |
| _V4ADiffApplier | class |  |
| apply_diff | function |  |
| WorkspaceEditor | class |  |
| ApplyPatchTool | class |  |

## Chunks

### PatchEditor (class, L22-L89)

> *Summary: Defines the interface for performing file system modifications, requiring methods to synchronously and asynchronously create, update, and delete files. It accepts operation dictionaries specifying paths and diffs as input and returns a status dictionary indicating success or failure.*


### create_file (method, L25-L34, parent: PatchEditor)

> *Summary: This method creates a new file synchronously based on the provided operation dictionary, which must contain a file path and its content difference. It returns a status dictionary indicating whether the creation succeeded or failed.*


### a_create_file (method, L36-L45, parent: PatchEditor)

> *Summary: Asynchronously creates a new file based on the provided operation dictionary, which must contain file path and content difference data. It returns a status dictionary indicating whether the creation succeeded or failed.*


### update_file (method, L47-L56, parent: PatchEditor)

> *Summary: This method modifies a specified file by applying a provided difference patch. It accepts an operation dictionary containing the file path and the diff, returning a status indicating success or failure along with any relevant output.*


### a_update_file (method, L58-L67, parent: PatchEditor)

> *Summary: Asynchronously modifies a specified file by applying a provided difference patch. It accepts an operation dictionary containing the file path and the diff, returning a status indicating success or failure along with any relevant output.*


### delete_file (method, L69-L78, parent: PatchEditor)

> *Summary: Removes a specified file based on the path provided in an input dictionary. It returns a status dictionary indicating whether the deletion succeeded or failed, along with any relevant output.*


### a_delete_file (method, L80-L89, parent: PatchEditor)

> *Summary: Asynchronously removes a specified file based on the path provided in an input dictionary. It returns a status dictionary indicating whether the deletion succeeded or failed, along with any relevant output.*


### _V4ADiffApplier (class, L92-L178)

> *Summary: This class interprets a unified diff string against an original text input to produce the resulting file content. It processes hunks, emitting unchanged lines from the original text or applying additions/deletions based on the diff format. If a "create" flag is set, it reconstructs the output solely from the addition lines in the diff.*


### __init__ (method, L98-L101, parent: _V4ADiffApplier)

> *Summary: Initializes the patch application tool by storing the input text as a list of lines and setting up an internal cursor and result buffer for processing. This prepares the object to modify the provided source content line by line.*


### apply (method, L104-L126, parent: _V4ADiffApplier)

> *Summary: This method applies a patch string (`diff`) to an original file content, optionally creating the content if no original is available. It iterates through hunks in the diff, emitting unchanged lines from the original source before applying modifications defined by the hunk headers and consuming corresponding lines from the patch.*


### _reconstruct_from_create (method, L129-L142, parent: _V4ADiffApplier)

> *Summary: This method reconstructs a file's content from a unified diff string by selectively including lines prefixed with `+` and retaining unchanged context lines, while discarding header and removed (`-`) lines. It takes a `diff` string as input and returns the resulting reconstructed source code as a single string.*


### _emit_unchanged_until (method, L144-L147, parent: _V4ADiffApplier)

> *Summary: This method appends lines from the original content to the result buffer until the current cursor position reaches or surpasses a specified target line number. It effectively copies unchanged text preceding the patch application point.*


### _consume_hunk_line (method, L149-L178, parent: _V4ADiffApplier)

> *Summary: This method processes a single line from a patch hunk, determining if it's an addition (`+`), deletion (`-`), or context line. It either appends the content to the result, verifies and advances the internal cursor against the original file for deletions/context, or raises a `ValueError` upon any mismatch.*


### apply_diff (function, L181-L184)

> *Summary: This function applies a V4A diff string to existing file content. It initializes an applier with the current content and returns the resulting modified content after applying the provided diff.*


### WorkspaceEditor (class, L187-L406)

> *Summary: Provides file system editing capabilities for applying patches within a specified workspace directory. It accepts an operation dictionary containing the target path and a diff, returning a status indicating success or failure after validating paths against security patterns. Offers both synchronous and asynchronous methods for creating, updating, deleting files, and their async counterparts.*


### __init__ (method, L193-L216, parent: WorkspaceEditor)

> *Summary: Sets up a workspace editor by establishing the root directory for file operations, defaulting to the current working directory if none is provided. It also configures security constraints using `allowed_paths`, which dictates which filesystem paths are permitted for modification via glob patterns.*


### _validate_path (method, L218-L251, parent: WorkspaceEditor)

> *Summary: Ensures a provided string path is both permitted by predefined patterns and strictly contained within the designated workspace directory. It returns the absolute, resolved `Path` object if validation succeeds, otherwise raising a `ValueError`.*


### create_file (method, L253-L275, parent: WorkspaceEditor)

> *Summary: This method creates a new file at a specified path by applying a provided diff string to generate the content. It ensures the necessary parent directories exist before writing the resulting text content to disk, returning a status indicating success or failure.*


### a_create_file (method, L277-L303, parent: WorkspaceEditor)

> *Summary: This method creates a new file by taking an operation dictionary containing the target path and a diff string. It ensures the parent directory exists, applies the provided diff to generate content, and then asynchronously writes that content to the specified file path.*


### update_file (method, L305-L330, parent: WorkspaceEditor)

> *Summary: This method modifies an existing file by reading its current content, applying a provided diff string to it, and then writing the resulting new content back to the specified path. It returns a status indicating success or failure along with relevant output messages.*


### a_update_file (method, L332-L364, parent: WorkspaceEditor)

> *Summary: This method asynchronously updates an existing file by reading its current content, applying a provided diff string to it, and then writing the resulting new content back to the original path. It requires `aiofiles` for asynchronous I/O operations and returns a status indicating success or failure along with relevant output messages.*


### delete_file (method, L366-L382, parent: WorkspaceEditor)

> *Summary: This method deletes a specified file by taking an operation dictionary containing the file's path. It validates the path, checks for existence, unlinks the file if present, and returns a status indicating success or failure along with relevant output messages.*


### a_delete_file (method, L384-L406, parent: WorkspaceEditor)

> *Summary: This asynchronous method deletes a specified file by first validating the path and checking for its existence using `asyncio.to_thread`. It returns a status dictionary indicating success or failure, along with an output message detailing the operation's result.*


### ApplyPatchTool (class, L414-L550)

> *Summary: This class provides a tool for agents to modify files by applying structured diffs received from an LLM. It accepts an editor and configuration flags like approval requirements and path restrictions, executing file creation, updates, or deletions synchronously or asynchronously based on the input operation.*


### __init__ (method, L446-L550, parent: ApplyPatchTool)

> *Summary: Initializes a patch application utility requiring either an `editor` instance or a `workspace_dir`. It configures behavior like approval requirements and path restrictions before creating an asynchronous or synchronous handler that processes file creation, updates, or deletions based on input operations.*

