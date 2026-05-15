# notebook/mcp/mcp_filesystem.py

2 function(s): list_files, read_file.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| list_files | function |  |
| read_file | function |  |

## Chunks

### list_files (function, L16-L25)

> *Summary: Retrieves the contents of a specified subdirectory within the global context path, returning a list of file and directory names. It enforces security by ensuring the requested path remains within the defined context boundary before listing its contents.*


### read_file (function, L29-L38)

> *Summary: Retrieves the text content of a specified file relative to a predefined context path. It validates that the requested path is within the allowed context and exists as a file before returning its contents or an appropriate error message.*

