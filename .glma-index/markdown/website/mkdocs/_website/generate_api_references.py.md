# website/mkdocs/_website/generate_api_references.py

14 function(s): import_submodules, build_pdoc_dict, process_modules, generate_markdown, generate, fix_api_reference_links, convert_md_to_mdx, get_mdx_files, add_prefix, create_nav_structure and 4 more. 1 class(es): SplitReferenceFilesBySymbols. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| import_submodules | function |  |
| build_pdoc_dict | function |  |
| process_modules | function |  |
| generate_markdown | function |  |
| generate | function |  |
| fix_api_reference_links | function |  |
| convert_md_to_mdx | function |  |
| get_mdx_files | function |  |
| add_prefix | function |  |
| create_nav_structure | function |  |
| update_nav | function |  |
| update_mint_json_with_api_nav | function |  |
| generate_mint_json_from_template | function |  |
| SplitReferenceFilesBySymbols | class |  |
| main | function |  |

## Chunks

### import_submodules (function, L30-L60)

> *Summary: Recursively traverses a given module's path to discover all its nested submodules. It accepts a module name and an optional flag to control whether the root module itself is included in the returned list of strings.*


### build_pdoc_dict (function, L64-L79)

> *Summary: This function populates a `__pdoc__` dictionary on a given module object, filtering its contents based on an optional `__all__` list. It selectively adds public members to this dictionary only if they belong to a different target module than the current one.*


### process_modules (function, L83-L90)

> *Summary: Iterates through a list of provided submodules to build documentation data structures. It dynamically imports each module and calls `build_pdoc_dict` for every one found.*


### generate_markdown (function, L94-L113)

> *Summary: This function recursively traverses specified Python modules and generates Markdown files for each module and its submodules. It takes a base path as input and outputs `.md` files containing the documentation text for every discovered module structure within that path.*


### generate (function, L117-L126)

> *Summary: This function processes imported submodules from the "autogen" package, injecting a custom template directory into pdoc's lookup mechanism. It then generates Markdown documentation and outputs it to the specified target directory.*


### fix_api_reference_links (function, L129-L144)

> *Summary: This function modifies input string content by finding specific API reference link patterns and rewriting them. It replaces the matched pattern with a URL segment followed only by the final component of the referenced object's name.*


### convert_md_to_mdx (function, L147-L171)

> *Summary: This function recursively scans a given directory for all `.md` files and converts them to `.mdx`. It reads the content, modifies internal API references using `fix_api_reference_links`, writes the result to a new `.mdx` file, and then deletes the original Markdown source.*


### get_mdx_files (function, L174-L176)

> *Summary: Scans a given directory recursively to find all `.mdx` files. It returns a list of strings representing the paths to these files, with the `.mdx` extension removed and platform-specific separators normalized to forward slashes.*


### add_prefix (function, L179-L182)

> *Summary: Constructs a complete documentation path by prepending the string `"docs/api-reference/"` to the provided `path`, incorporating any specified `parent_groups`. The function takes a file path and an optional list of group names, returning the fully qualified API reference URL segment.*


### create_nav_structure (function, L185-L219)

> *Summary: Transforms a list of file paths into a hierarchical navigation structure suitable for documentation menus. It groups paths by their initial directory segment and recursively builds nested structures, ensuring that any "overview" pages are placed at the beginning of their respective sections.*


### update_nav (function, L222-L245)

> *Summary: This function modifies a configuration file by injecting a new navigation structure into the "API Reference" section of `mint.json`. It reads the existing JSON, appends the provided page list under the specified group, and then writes the updated configuration back to the file.*


### update_mint_json_with_api_nav (function, L248-L262)

> *Summary: This function reads all MDX files from a specified API directory and constructs a navigation structure from them. It then updates the `mint.json` file within the website build directory to incorporate this new API navigation data.*


### generate_mint_json_from_template (function, L266-L280)

> *Summary: This function takes a JSON template path and an output path to generate a final JSON file. It reads the template, renders it using provided context, parses the resulting string into Python data, and then writes the structured data to the specified output file, overwriting any existing content.*


### SplitReferenceFilesBySymbols (class, L283-L368)

> *Summary: This class parses Markdown files within a specified API directory to extract individual symbol content (classes and functions). It generates an overview page, splits the source content into separate Markdown files per symbol, and then moves these generated files from a temporary location into the final API reference structure.*


### __init__ (method, L284-L286, parent: SplitReferenceFilesBySymbols)

> *Summary: Initializes the object by storing a provided directory path for API sources and creating a temporary working directory named "tmp". This sets up the necessary locations for processing API documentation.*


### _generate_overview (method, L288-L308, parent: SplitReferenceFilesBySymbols)

> *Summary: Constructs an API reference overview Markdown string by listing provided class and function names. It generates links pointing to the respective documentation files within a specified output directory structure.*


### _extract_symbol_content (method, L310-L327, parent: SplitReferenceFilesBySymbols)

> *Summary: Parses raw documentation string content to extract individual symbols and categorize them as classes or functions based on specific markers within the text. It returns a dictionary mapping each symbol name to its extracted content, along with an "overview" section generated from the identified symbols.*


### _split_content_by_symbols (method, L329-L333, parent: SplitReferenceFilesBySymbols)

> *Summary: Parses a string of content to extract structured data based on specific markers. It checks for the `**** SYMBOL_START ****` delimiter and calls another method to populate a dictionary mapping symbol names to their associated content.*


### _process_files (method, L335-L340, parent: SplitReferenceFilesBySymbols)

> *Summary: Iterates through all Markdown files in the API directory, creating corresponding temporary subdirectories for each file's parent. It yields a tuple containing the target output directory and a dictionary mapping symbols found within the file's content to their locations.*


### _clean_directory (method, L342-L347, parent: SplitReferenceFilesBySymbols)

> *Summary: This method recursively removes all contents within a specified directory path. It iterates through the directory, deleting subdirectories entirely and removing individual files found inside.*


### _move_generated_files_to_api_dir (method, L349-L356, parent: SplitReferenceFilesBySymbols)

> *Summary: Cleans the API directory and then copies all contents from a temporary directory into the designated API directory. It uses `shutil.copytree` for directories and `shutil.copy2` for files during the transfer.*


### generate (method, L358-L368, parent: SplitReferenceFilesBySymbols)

> *Summary: This method processes source files to generate API reference Markdown content into a temporary directory. It then moves the generated files to the final API output location before cleaning up the temporary directory.*


### main (function, L371-L427)

> *Summary: This script processes API documentation by taking an optional input directory to generate structured references using templates and then converts Markdown files to MDX format. It also finalizes the process by creating and updating a `mint.json` configuration file based on the generated content.*

