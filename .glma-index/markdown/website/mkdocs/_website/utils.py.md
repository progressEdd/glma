# website/mkdocs/_website/utils.py

11 function(s): get_git_tracked_and_untracked_files_in_directory, copy_files, copy_only_git_tracked_and_untracked_files, remove_marker_blocks, sort_files_by_date, construct_authors_html, separate_front_matter_and_content, ensure_edit_url, add_authors_and_social_preview, get_authors_info and 1 more. 1 class(es): NavigationGroup.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NavigationGroup | class |  |
| get_git_tracked_and_untracked_files_in_directory | function |  |
| copy_files | function |  |
| copy_only_git_tracked_and_untracked_files | function |  |
| remove_marker_blocks | function |  |
| sort_files_by_date | function |  |
| construct_authors_html | function |  |
| separate_front_matter_and_content | function |  |
| ensure_edit_url | function |  |
| add_authors_and_social_preview | function |  |
| get_authors_info | function |  |
| render_gallery_html | function |  |

## Chunks

### NavigationGroup (class, L29-L31)

> *Summary: Defines a structure for organizing website navigation, holding a group name and a list of page identifiers or nested `NavigationGroup` structures. This dictionary type allows for hierarchical organization of links within the site's navigation tree.*


### get_git_tracked_and_untracked_files_in_directory (function, L34-L42)

> *Summary: Executes a `git ls-files` command within the specified directory to retrieve paths of both tracked and untracked files. It returns a list of `Path` objects representing these files found by Git.*


### copy_files (function, L45-L51)

> *Summary: Copies a specified list of files from a source directory to a destination directory while preserving their relative structure. It ensures the necessary parent directories exist in the destination before performing the copy operation.*


### copy_only_git_tracked_and_untracked_files (function, L54-L65)

> *Summary: This utility copies files from a source directory to a destination directory, specifically including only those files that are currently tracked by Git or are new additions. It optionally filters out any files residing within a specified ignored subdirectory before performing the copy operation.*


### remove_marker_blocks (function, L68-L101)

> *Summary: This function strips specific code blocks from a string based on a provided marker prefix. It first removes complete blocks matching the primary marker, then cleans up any remaining start and end markers associated with an alternative prefix before normalizing excessive newlines in the resulting content.*


### sort_files_by_date (function, L105-L113)

> *Summary: This utility extracts a date and the directory name from a given file path by parsing the first three hyphen-separated segments of its parent directory's name. It returns a tuple containing the parsed `datetime` object or `datetime.min` if parsing fails, along with the original directory name string.*


### construct_authors_html (function, L116-L186)

> *Summary: Generates an HTML string of author cards based on a list of author IDs and their associated data. It selects the appropriate markup structure (Mintlify or MkDocs) depending on the provided build system to render the final output.*


### separate_front_matter_and_content (function, L189-L203)

> *Summary: Parses a markdown file's text to isolate metadata from the main body. It checks for YAML front matter delimited by "---" at the start of the file and returns a tuple containing the extracted front matter string and the remaining content string.*


### ensure_edit_url (function, L206-L217)

> *Summary: Checks if a specific HTML placeholder exists within the provided file content; if not found, it appends the necessary edit URL markup formatted with the given file path to the end of the content string.*


### add_authors_and_social_preview (function, L221-L280)

> *Summary: This function injects author information and a social share image into MDX or MD files within a specified directory. It reads existing front matter, constructs HTML for authors based on provided data, combines this with the file content, and writes the modified content back to disk, handling build system-specific logic like edit URL insertion.*


### get_authors_info (function, L284-L291)

> *Summary: Reads author data from a specified YAML file path and parses the "authors" section. It returns a dictionary containing structured information about all authors, exiting if reading or parsing fails.*


### render_gallery_html (function, L295-L414)

> *Summary: Reads a YAML file containing gallery items and generates a complete HTML string for displaying them. It parses item details, extracts unique tags to build a filter dropdown, and constructs individual card HTML elements including images, titles, badges (like Colab/GitHub links), and associated tags.*

