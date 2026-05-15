# autogen/tools/experimental/google/drive/drive_functions.py

4 function(s): list_files_and_folders, _get_file_extension, _validate_download_path, download_file.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| list_files_and_folders | function |  |
| _get_file_extension | function |  |
| _validate_download_path | function |  |
| download_file | function |  |

## Chunks

### list_files_and_folders (function, L28-L40)

> *Summary: Retrieves a paginated list of Google Drive files and folders based on an optional parent folder ID. It accepts the service object, page size, and folder ID as input, returning a list of structured `GoogleFileInfo` objects containing IDs, names, and MIME types.*


### _get_file_extension (function, L43-L58)

> *Summary: Maps a provided MIME type string to its corresponding file extension using a predefined dictionary lookup. It returns the appropriate extension (e.g., "docx") or `None` if the input MIME type is not recognized.*


### _validate_download_path (function, L61-L78)

> *Summary: This utility function constructs a safe, absolute file path within a specified root directory. It validates that both any provided subfolder and the final filename do not allow for path traversal outside the designated download folder, creating necessary directories along the way if they don't exist.*


### download_file (function, L87-L137)

> *Summary: Retrieves a Google Drive file using its ID and saves it locally, automatically converting native Google formats (Docs, Sheets, Slides) to standard export types. It accepts the service object, file details, target directory, and returns a status string indicating success or failure with the resulting path.*

