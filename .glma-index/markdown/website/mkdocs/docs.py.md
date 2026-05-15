# website/mkdocs/docs.py

14 function(s): get_missing_translation, get_in_progress, get_default_title, join_nested, _touch_file, preview, live, build, add, rm and 4 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| get_missing_translation | function |  |
| get_in_progress | function |  |
| get_default_title | function |  |
| join_nested | function |  |
| _touch_file | function |  |
| preview | function |  |
| live | function |  |
| build | function |  |
| add | function |  |
| rm | function |  |
| mv | function |  |
| update_readme | function |  |
| build_api_docs | function |  |
| _build | function |  |

## Chunks

### get_missing_translation (function, L43-L44)

> *Summary: Constructs and returns the absolute path to a standard "missing translation" markdown file within a specified language directory structure. It takes a language code string as input to locate the correct resource file.*


### get_in_progress (function, L47-L48)

> *Summary: Constructs and returns a `Path` object pointing to the "in-progress.md" file within a specified language directory structure. It takes a language code string as input to locate the correct documentation path.*


### get_default_title (function, L54-L58)

> *Summary: Generates a default, uppercase title from a given file path by using the filename stem and replacing hyphens with spaces. If the resulting title is "INDEX", it recursively calls itself on the parent directory to find a more appropriate title.*


### join_nested (function, L61-L64)

> *Summary: This function constructs a target file path by iteratively joining directory segments from the input string onto a starting `Path` object. It then ensures this resulting path exists on the filesystem via a helper call before returning it.*


### _touch_file (function, L67-L72)

> *Summary: Ensures the directory structure for a given file path exists by creating necessary parent directories if they are missing. It accepts a `Path` object and returns that same `Path` object after ensuring its location is valid on the filesystem.*


### preview (function, L76-L90)

> *Summary: This function builds the site first and then starts a basic HTTP server to serve the pre-built content from the designated build directory. It warns the user that this is for previewing only, recommending `mkdocs live` for active development.*


### live (function, L94-L109)

> *Summary: This function starts a local development server for MkDocs, optionally skipping pre-processing steps like API documentation generation if the `--skip-build` flag is used. It accepts an optional port argument and outputs by launching the serving process on the specified address.*


### build (function, L113-L114)

> *Summary: This function acts as a wrapper to initiate the documentation build process, accepting an optional boolean flag via CLI for forcing a rebuild. It delegates the actual building logic to an internal `_build` method.*


### add (function, L118-L143)

> *Summary: This function scans specified language directories to check for the existence of a given path, categorizing directories into those that exist and those that do not. It writes placeholder content indicating "in progress" or "missing translation" to non-existent files based on whether any existing file provided a title.*


### rm (function, L147-L164)

> *Summary: This function deletes a specified path, prompting the user for confirmation first. It recursively removes directories or unlinks files within predefined language directories and cleans up empty parent directories afterward.*


### mv (function, L168-L173)

> *Summary: Moves a specified file from its original location to a new destination within various language directories. It takes the source path and target path as command-line arguments, renaming the existing file if found in any configured directory.*


### update_readme (function, L177-L192)

> *Summary: This function is intended to update `README.md` by incorporating embeddings from the main documentation index file (`docs/docs/en/index.md`). Currently, it skips this operation and prints a message indicating that the feature is incomplete.*


### build_api_docs (function, L222-L225)

> *Summary: This function initiates the process of generating API documentation specifically for the `autogen` module. It prints a status message and then calls another function to perform the actual document creation using the base directory as input.*


### _build (function, L228-L237)

> *Summary: This function orchestrates the documentation build process by first generating necessary files for MkDocs and building API documentation. It then executes the `mkdocs build` command to compile the final website output into the specified build directory.*

