# website/mkdocs/_website/generate_mkdocs.py

36 function(s): filter_excluded_files, copy_file, transform_tab_component, transform_card_grp_component, fix_asset_path, fix_internal_references, absolute_to_relative, _ensure_md_extension, _transform_api_anchor, fix_internal_links and 26 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| filter_excluded_files | function |  |
| copy_file | function |  |
| transform_tab_component | function |  |
| transform_card_grp_component | function |  |
| fix_asset_path | function |  |
| fix_internal_references | function |  |
| absolute_to_relative | function |  |
| _ensure_md_extension | function |  |
| _transform_api_anchor | function |  |
| fix_internal_links | function |  |
| transform_content_for_mkdocs | function |  |
| rename_user_story | function |  |
| process_and_copy_files | function |  |
| format_title | function |  |
| format_page_entry | function |  |
| format_navigation | function |  |
| add_api_ref_to_mkdocs_template | function |  |
| generate_mkdocs_navigation | function |  |
| copy_assets | function |  |
| add_excerpt_marker | function |  |
| generate_url_slug | function |  |
| process_blog_contents | function |  |
| fix_snippet_imports | function |  |
| process_blog_files | function |  |
| add_front_matter_to_metadata_yml | function |  |
| transform_admonition_blocks | function |  |
| remove_mdx_code_blocks | function |  |
| remove_quarto_raw_html_wrappers | function |  |
| post_process_func | function |  |
| target_dir_func | function |  |
| inject_gallery_html | function |  |
| add_notebooks_nav | function |  |
| _generate_navigation_entries | function |  |
| generate_community_insights_nav | function |  |
| add_authors_info_to_user_stories | function |  |
| main | function |  |

## Chunks

### filter_excluded_files (function, L46-L51)

> *Summary: Filters a list of file paths, retaining only those that do not start with any path specified in the `exclusion_list` relative to the given website directory. It takes a list of files, an exclusion list of strings, and a base directory as input, returning a filtered list of `Path` objects.*


### copy_file (function, L54-L57)

> *Summary: Copies a source file to the specified MkDocs output directory, preserving its relative structure within the destination folder. It ensures the necessary parent directories exist before performing the copy operation.*


### transform_tab_component (function, L60-L135)

> *Summary: Converts React-style `<Tabs>` components within a string into MkDocs Markdown format. It parses the input to extract tab titles and contents, then transforms them into `=== "Title"` headers followed by indented content blocks.*


### transform_card_grp_component (function, L138-L152)

> *Summary: This function transforms raw Markdown content by stripping `<CardGroup>` tags and converting various `<Card>` structures into HTML anchor elements (`<a>`) or simple `<div>` containers, based on the input tag structure. It takes a string of content and returns the processed string with these structural replacements applied.*


### fix_asset_path (function, L155-L163)

> *Summary: This function modifies string content by replacing specific asset and documentation path references. It substitutes instances of `/static/img/` with `/assets/img/` in both `src` attributes and image markdown syntax, while also ensuring all `/docs/` links are correctly formatted as `/docs/`.*


### fix_internal_references (function, L166-L186)

> *Summary: This function resolves internal documentation links by checking if a given absolute URL corresponds to an existing Markdown file or directory within the specified docs folder. If it's not found directly, it attempts to return the URL pointing to the first `.md` file discovered in the corresponding directory.*


### absolute_to_relative (function, L189-L219)

> *Summary: Calculates the path needed to navigate from a source file's directory to a destination file, taking absolute paths as input and returning a relative string. It primarily uses `pathlib` for calculation but falls back to `os.path.relpath`, adding special logic for blog directories if necessary.*


### _ensure_md_extension (function, L222-L261)

> *Summary: This utility ensures that relative links intended for MkDocs include the `.md` extension if one is missing. It correctly handles both file paths and those containing fragment identifiers (`#`) by inserting `.md` before the fragment when necessary.*


### _transform_api_anchor (function, L264-L294)

> *Summary: Converts kebab-case API anchors from source documentation to the dotted Python path format required by `mkdocstrings`. It takes an absolute link and a fragment, returning either the original fragment or a fully qualified path like `module.Class.method` based on whether the anchor refers to a class or a method within the specified API reference section.*


### fix_internal_links (function, L297-L411)

> *Summary: This function scans document content (HTML/Markdown) to convert absolute internal links starting with `/docs` into relative paths based on the source file's location. It handles special cases for blog URLs and ensures correct path formatting, including appending `.md` extensions where appropriate.*


### transform_content_for_mkdocs (function, L414-L502)

> *Summary: Converts raw HTML content into a format suitable for MkDocs by transforming admonition tags, escaping JSX curly braces within code blocks to prevent Jinja parsing errors, and applying several other structural cleanups like fixing asset paths and internal links. It takes the input string content and its relative file path as inputs, returning the fully processed string.*


### rename_user_story (function, L505-L507)

> *Summary: This function renames a file by extracting parts of its parent directory's name, joining them with underscores, and appending the original file extension. It takes a `Path` object as input and returns a new `Path` object representing the renamed file.*


### process_and_copy_files (function, L510-L539)

> *Summary: This function copies files from an input directory to an output directory, converting `.mdx` files to `.md`. It then iterates over these newly created Markdown files, transforming their content based on their relative path before saving the changes back to the destination.*


### format_title (function, L542-L562)

> *Summary: This function generates a display title for a documentation page by first checking the YAML front matter of the specified file path for a `sidebarTitle`. If that fails, it formats the filename stem using provided keywords to create a capitalized and keyword-substituted title.*


### format_page_entry (function, L565-L569)

> *Summary: Constructs a formatted string representing a single page entry for navigation. It takes the page location, indentation level, metadata keywords, and documentation directory to generate a markdown link structure.*


### format_navigation (function, L572-L623)

> *Summary: Recursively transforms a list of navigation groups and pages into a markdown-style nested list string, using an optional keyword map for specific text formatting. It handles nesting by calling itself for sub-groups and applies several hardcoded replacements to adjust the final output structure.*


### add_api_ref_to_mkdocs_template (function, L626-L635)

> *Summary: Inserts an "API References" section into the existing MkDocs navigation string immediately following a specified section marker. It takes the current navigation structure and the target section name as input, returning the modified navigation string.*


### generate_mkdocs_navigation (function, L639-L656)

> *Summary: This function processes a navigation template from a website directory, filters out specified groups, and then generates content for both `navigation_template.txt` and `SUMMARY.md` files within the MkDocs root. It constructs the final Markdown structure by incorporating the filtered navigation and adding a fixed blog link section.*


### copy_assets (function, L659-L664)

> *Summary: Copies image assets from the source `static/img` directory to a specific location within the generated documentation structure. It uses a helper function to determine which files in the source directory are tracked by Git before performing the copy operation.*


### add_excerpt_marker (function, L667-L693)

> *Summary: Inserts an `<!-- more -->` marker into markdown content, specifically before the second heading if two or more exist. If fewer than two headings are found, it appends the marker to the end of the content.*


### generate_url_slug (function, L696-L699)

> *Summary: This function takes a file path and extracts a URL-friendly slug from its parent directory name. It splits the parent directory by hyphens and joins all parts after the third element to form the resulting string, which is then prefixed with "slug: ".*


### process_blog_contents (function, L702-L739)

> *Summary: Parses blog content separated by "---" to extract metadata like tags and a date from the file path. It then reconstructs the content, injecting structured YAML blocks for tags, categories, date, and URL slug before returning the fully processed string.*


### fix_snippet_imports (function, L742-L780)

> *Summary: This function transforms MDX content by finding specific `import` statements referencing files in a snippets directory. It replaces each matched import with the actual content of the corresponding snippet file, returning the modified string.*


### process_blog_files (function, L783-L820)

> *Summary: This function processes source blog Markdown files by reading them from `_blogs`, enriching their content using metadata and snippet imports, and then overwriting the original files with the processed versions. Finally, it copies all processed blog assets and related configuration (like authors YAML and snippets) into the final `blog` directory structure for MkDocs consumption.*


### add_front_matter_to_metadata_yml (function, L826-L880)

> *Summary: Appends notebook metadata, derived from a front matter dictionary and rendered Markdown path, into a central `notebooks_metadata.yml` file within the build directory structure. It manages file creation by deleting an existing file only on the first invocation.*


### transform_admonition_blocks (function, L883-L1008)

> *Summary: Converts custom `:::` syntax blocks within content strings into the Material for MkDocs admonition format (`!!! type "Title"`). It parses the input line-by-line, handles block boundaries, maps specific types (like "Tip" to "tip"), and adjusts indentation before returning the fully transformed string.*


### remove_mdx_code_blocks (function, L1011-L1029)

> *Summary: This function strips specific `mdx-code-block` delimiters from a string while retaining the enclosed code content. It takes raw markdown content as input and returns the modified string with the markers removed.*


### remove_quarto_raw_html_wrappers (function, L1032-L1074)

> *Summary: Extracts raw HTML from a string by parsing and removing Quarto's JavaScript wrappers (`quartoRawHtml` declarations). It finds all declared HTML blocks, then replaces instances where these blocks are referenced in `dangerouslySetInnerHTML` with the actual extracted HTML content.*


### post_process_func (function, L1078-L1168)

> *Summary: This function processes a rendered MDX file by extracting and merging front matter, cleaning heading IDs, injecting GitHub and Colab badges based on source notebook location, and transforming content for MkDocs compatibility. It ultimately rewrites the file as a standard Markdown (`.md`) document containing updated metadata and processed body content.*


### target_dir_func (function, L1171-L1173)

> *Summary: Calculates and returns a specific subdirectory path within the provided build directory, structured as `website_build_directory/use-cases/notebooks/notebooks`. This function defines the intended location for notebook assets during website generation.*


### inject_gallery_html (function, L1176-L1185)

> *Summary: Reads the Markdown content from a specified notebooks path and generates HTML for a gallery based on metadata. It then replaces a placeholder in the Markdown file with the generated HTML before overwriting the original file.*


### add_notebooks_nav (function, L1189-L1221)

> *Summary: This function reads notebook metadata from a YAML file and injects navigation links for each notebook into a specified Markdown template. It locates a predefined "All Notebooks" entry in the target file and inserts all generated notebook links immediately following it, then overwrites the original file with the updated content.*


### _generate_navigation_entries (function, L1224-L1261)

> *Summary: Reads Markdown files from a specified directory, sorts them by date (newest first), and extracts titles from their YAML frontmatter to generate formatted navigation list strings for MkDocs. It returns a list of these string entries, ensuring paths are correctly relative to the output directory.*


### generate_community_insights_nav (function, L1264-L1284)

> *Summary: This function constructs a combined navigation structure from user stories and community talks directories. It then reads an existing Markdown navigation file, replaces a specific marker ("- Blog") with the newly generated content, and writes the updated navigation back to the specified path.*


### add_authors_info_to_user_stories (function, L1287-L1300)

> *Summary: Reads author data from a YAML file and then iterates through all Markdown files in the user stories directory to inject author information into their content before saving the modified files back. This process ensures that documentation rendered by MkDocs includes necessary author details.*


### main (function, L1303-L1368)

> *Summary: This function orchestrates the entire documentation build process by copying source files, processing content from various directories (including notebooks and blogs), generating navigation structures, and injecting metadata into Markdown files for MkDocs rendering. It takes a boolean `force` flag to optionally clean up previous output before starting the generation pipeline.*

