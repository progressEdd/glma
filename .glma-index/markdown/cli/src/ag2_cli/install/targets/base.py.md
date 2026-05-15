# cli/src/ag2_cli/install/targets/base.py

2 function(s): _needs_quoting, format_frontmatter. 3 class(es): Target, DirectoryTarget, SingleFileTarget. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _needs_quoting | function |  |
| format_frontmatter | function |  |
| Target | class |  |
| DirectoryTarget | class |  |
| SingleFileTarget | class |  |

## Chunks

### _needs_quoting (function, L26-L39)

> *Summary: Determines if a given string value requires quoting when parsed as YAML. It returns true if the string is empty, matches a special YAML keyword, resembles a number, or contains spaces or specific reserved characters.*


### format_frontmatter (function, L42-L61)

> *Summary: Converts a Python dictionary into a YAML frontmatter string, wrapping it between `---` delimiters. It handles various data types (booleans, lists, numbers, strings) by applying specific formatting rules like quoting or list notation based on the value type.*


### Target (class, L64-L81)

> *Summary: Provides an abstract base for installation targets, requiring subclasses to implement logic for detecting their presence in a project directory and performing both installation and uninstallation operations on provided content items. It accepts the project directory as input and returns lists of file paths corresponding to created or removed files.*


### detect (method, L71-L73, parent: Target)

> *Summary: Determines if a specific build target is present within a given project directory by checking for the existence of predefined paths relative to that directory. Returns `True` if any expected path exists, indicating the target is in use.*


### install (method, L76-L77, parent: Target)

> *Summary: This method takes a project directory and a list of content items as input to perform an installation process. It returns a list containing the absolute paths of all files that were successfully created during the operation.*


### uninstall (method, L80-L81, parent: Target)

> *Summary: Removes previously installed AG2 components from a specified project directory and returns a list containing the paths that were deleted.*


### DirectoryTarget (class, L84-L133)

> *Summary: This class generates individual rule files within a specified directory based on provided content items. It takes configuration like file extensions and prefixes, transforms item metadata into frontmatter, writes the combined content to disk during installation, and cleans up these generated files upon uninstallation.*


### __init__ (method, L87-L103, parent: DirectoryTarget)

> *Summary: Initializes a target configuration by storing metadata such as its name, display name, and rules directory. It accepts optional parameters for file extensions, path detection lists, prefixes, and a frontmatter transformation function.*


### _filename (method, L105-L106, parent: DirectoryTarget)

> *Summary: Constructs a full file path by prepending a configured prefix and appending a configured extension to the provided content item's name. This method returns the complete string representing the target filename.*


### _transform (method, L108-L111, parent: DirectoryTarget)

> *Summary: If a transformation function is configured, it applies that custom logic to the input `ContentItem`; otherwise, it returns a dictionary containing only the item's description.*


### install (method, L113-L123, parent: DirectoryTarget)

> *Summary: This method takes a project directory and a list of content items, then writes each item to a specific subdirectory within the project. It transforms the input items, prepends frontmatter, combines it with the body, and saves the resulting file path for every processed item.*


### uninstall (method, L125-L133, parent: DirectoryTarget)

> *Summary: Removes all files matching a specific pattern within the project's rules directory, returning a list of paths for the deleted files. It takes the project directory as input and operates based on instance attributes like `rules_dir`, `prefix`, and `file_ext`.*


### SingleFileTarget (class, L136-L196)

> *Summary: This class manages the installation and uninstallation of structured content into a single specified file within a project directory. It takes a list of `ContentItem`s, formats them with section headers, and intelligently merges or replaces existing content marked by `AG2_MARKER` to ensure idempotency during updates.*


### __init__ (method, L139-L149, parent: SingleFileTarget)

> *Summary: Initializes a target object by storing its unique name, user-friendly display name, and the primary file path. It optionally accepts a list of paths to check for detection purposes.*


### _format_section (method, L151-L152, parent: SingleFileTarget)

> *Summary: Formats a content item into a Markdown section string by prepending a header with the "AG2:" prefix to the item's name and appending its body content. It takes a `ContentItem` object as input and returns a formatted string.*


### install (method, L154-L176, parent: SingleFileTarget)

> *Summary: This method injects a structured content block into a specified file within a project directory. It reads the existing file to find and replace an existing marker section, or creates the file entirely if it doesn't exist, finally writing the updated content back to disk.*


### uninstall (method, L178-L196, parent: SingleFileTarget)

> *Summary: Removes a specific block of text from a file within a project directory if it contains the designated marker. It finds the content between two markers (or to the end if only one is present), replaces it with the surrounding text, and deletes the file entirely if nothing remains.*

