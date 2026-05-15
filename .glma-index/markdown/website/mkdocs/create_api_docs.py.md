# website/mkdocs/create_api_docs.py

12 function(s): _is_private, _merge_lists, _add_all_submodules, _resolve_case_collisions, _get_api_summary_item, _get_api_summary, _generate_api_doc, _generate_api_docs, _filter_submodules_by_export_path, _generate_api_docs_for_module and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_private | function |  |
| _merge_lists | function |  |
| _add_all_submodules | function |  |
| _resolve_case_collisions | function |  |
| _get_api_summary_item | function |  |
| _get_api_summary | function |  |
| _generate_api_doc | function |  |
| _generate_api_docs | function |  |
| _filter_submodules_by_export_path | function |  |
| _generate_api_docs_for_module | function |  |
| create_api_docs | function |  |
| on_page_markdown | function |  |

## Chunks

### _is_private (function, L19-L21)

> *Summary: Checks if a given string, representing a qualified name, is considered private by inspecting its components for leading underscores. Returns `True` if any segment of the name starts with an underscore, otherwise returns `False`.*


### _merge_lists (function, L24-L31)

> *Summary: This utility function integrates submodule names into a list of existing members by inserting the submodule name immediately before any member whose name starts with that submodule. It takes two lists of strings as input and returns a new, merged list.*


### _add_all_submodules (function, L34-L47)

> *Summary: This function expands a list of module names to include all their parent submodules. It processes the input members by generating prefixes for each, merges these with the original list, and returns a unique, sorted list based on a custom hierarchical sorting key.*


### _resolve_case_collisions (function, L50-L80)

> *Summary: This function processes a list of member names to create a mapping from each name to its corresponding file path, handling case-insensitive filesystem collisions. When two members map to the same lowercase path, it disambiguates them by appending `_func` to one or both names based on their original casing.*


### _get_api_summary_item (function, L87-L95)

> *Summary: This helper function generates a formatted string item for an API summary based on a dot-separated input path. It determines the indentation and output format—either a simple link or a nested list item—depending on whether the input string ends with a period.*


### _get_api_summary (function, L98-L101)

> *Summary: This function processes a list of member names, resolves any path collisions using a global map, and then returns a newline-separated string containing the summary details for each provided member.*


### _generate_api_doc (function, L104-L115)

> *Summary: This function constructs and writes a Markdown documentation file for a given API member name into the specified directory. It parses the input name to determine module and member details, generates metadata content, and saves the resulting `.md` file at the calculated path.*


### _generate_api_docs (function, L118-L119)

> *Summary: This function iterates over a list of member names and generates API documentation for each one that does not end with a dot. It returns a list containing the `Path` objects pointing to the newly created documentation files.*


### _filter_submodules_by_export_path (function, L122-L154)

> *Summary: Filters a list of submodules to return fully qualified names of public members belonging to a specific package. It imports each submodule, checks against an `__all__` definition if present, and includes the member's name only if it belongs to or is part of the target module structure.*


### _generate_api_docs_for_module (function, L157-L182)

> *Summary: This function compiles API documentation for a given module by recursively gathering its submodules and members. It cleans up and creates an `api-reference` directory within the provided docs path before generating and writing the final documentation structure, returning a summary string.*


### create_api_docs (function, L185-L207)

> *Summary: This function generates API documentation by first calling a helper to create module-specific documentation within the project's `docs` directory. It then reads a navigation template, formats it using the generated API data, cleans up empty lines, and writes the final summary to `SUMMARY.md`.*


### on_page_markdown (function, L210-L213)

> *Summary: This hook modifies the edit URL for any Markdown page whose current URL contains "public\_api". It replaces this segment with "api-reference" to align the editing view with a new API reference structure.*

