# website/mkdocs/_website/process_notebooks.py

20 function(s): notebooks_target_dir, add_front_matter_to_metadata_mdx, convert_callout_blocks, convert_mdx_image_blocks, extract_img_tag_from_figure_tag, post_process_mdx, get_sorted_files, generate_nav_group, extract_example_group, update_group_pages and 10 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| notebooks_target_dir | function |  |
| add_front_matter_to_metadata_mdx | function |  |
| convert_callout_blocks | function |  |
| convert_mdx_image_blocks | function |  |
| extract_img_tag_from_figure_tag | function |  |
| post_process_mdx | function |  |
| get_sorted_files | function |  |
| generate_nav_group | function |  |
| extract_example_group | function |  |
| update_group_pages | function |  |
| add_notebooks_blogs_and_user_stories_to_nav | function |  |
| fix_internal_references | function |  |
| fix_internal_references_in_mdx_files | function |  |
| add_authors_and_social_img_to_blog_and_user_stories | function |  |
| ensure_mint_json_exists | function |  |
| cleanup_tmp_dirs | function |  |
| get_files_path_from_navigation | function |  |
| add_edit_urls_and_remove_mkdocs_markers | function |  |
| copy_images_from_notebooks_dir_to_target_dir | function |  |
| main | function |  |

## Chunks

### notebooks_target_dir (function, L39-L41)

> *Summary: Calculates and returns a specific subdirectory path within the main website build directory. This path is designated as the final destination for processed notebook files.*


### add_front_matter_to_metadata_mdx (function, L44-L92)

> *Summary: This function updates a central JavaScript metadata file (`NotebooksMetadata.mdx`) by adding or updating an entry for the current notebook based on its provided front matter. It reads existing metadata from the build directory, constructs a new entry using inputs like title and source, merges it into the list, and then overwrites the metadata file with the updated JSON structure.*


### convert_callout_blocks (function, L95-L177)

> *Summary: This function parses input string content to find two formats of Markdown callout blocks (plain `:::` or those prefixed with backticks/MDX markers). It replaces these structured blocks with corresponding custom HTML components based on a predefined type mapping.*


### convert_mdx_image_blocks (function, L180-L203)

> *Summary: This function transforms image syntax embedded within MDX code blocks into standard Markdown image format. It takes the raw content and paths to determine the correct absolute path for each image before substituting the specialized block with a regular markdown link.*


### extract_img_tag_from_figure_tag (function, L206-L235)

> *Summary: This function scans file content to find `<figure>` tags containing an embedded `<img>` tag. It extracts the image source and rewrites the HTML to ensure local images are correctly prefixed with a path relative to a specified directory, fixing rendering issues in certain documentation platforms.*


### post_process_mdx (function, L240-L330)

> *Summary: This function processes a rendered MDX file by extracting and merging front matter, cleaning heading IDs, and injecting GitHub/Colab badges into the content. It then performs several transformations—like converting callout blocks and image syntax—before rewriting the file with updated metadata and content.*


### get_sorted_files (function, L333-L341)

> *Summary: Retrieves and sorts all `index.mdx` files within a specified directory structure, then returns a list of paths prefixed with the provided string, ordered from newest to oldest based on file date. It raises an error if the input directory does not exist.*


### generate_nav_group (function, L344-L354)

> *Summary: Creates a navigation structure dictionary by taking an input directory path, a header string, and a file path prefix. It returns a dictionary containing the specified group header and a list of sorted file paths found within that directory.*


### extract_example_group (function, L357-L381)

> *Summary: Reads a metadata file to parse a JSON array containing notebook source paths. It then transforms these paths into a list of relative file system paths, excluding any that originate from the build directory.*


### update_group_pages (function, L384-L406)

> *Summary: This function recursively traverses a nested navigation structure to find and replace the `pages` content of any group matching a specified target. It takes the existing navigation, the target group name, and the new page data as input, returning the modified navigation structure.*


### add_notebooks_blogs_and_user_stories_to_nav (function, L409-L465)

> *Summary: This function modifies the `mint.json` configuration file within a website's build directory by programmatically adding sections for User Stories and Blogs to the main navigation structure. It also reads notebook metadata from an MDX file to dynamically inject notebooks into the existing navigation groups before writing the updated JSON back to disk.*


### fix_internal_references (function, L468-L492)

> *Summary: This function rewrites internal markdown links within a given string by resolving relative paths against a specified root directory and the current file's location. It takes the content, root path, and current file path as input, returning the content with all internal references correctly formatted for web linking.*


### fix_internal_references_in_mdx_files (function, L495-L510)

> *Summary: Iterates through all `.mdx` files within a specified build directory, reading their content to resolve internal references using an external function. If modifications are made, it overwrites the original file with the corrected content, exiting on any processing error.*


### add_authors_and_social_img_to_blog_and_user_stories (function, L513-L534)

> *Summary: This function processes blog and user story content within the build directory by copying existing structures. It then injects author information and social media images into these documents using data loaded from a YAML file.*


### ensure_mint_json_exists (function, L537-L542)

> *Summary: Checks if a required `mint.json` file exists within the specified build directory. If it is missing, it prints an error message and terminates the process, indicating that another script must be run first.*


### cleanup_tmp_dirs (function, L545-L560)

> *Summary: If `NotebooksMetadata.mdx` is missing from the build directory or if regeneration is requested, this function removes the temporary notebooks directory to guarantee a fresh build state. It takes the website's build path and a boolean flag indicating whether to regenerate content as input.*


### get_files_path_from_navigation (function, L563-L582)

> *Summary: This function traverses a nested list of navigation groups to extract all corresponding file paths. It recursively processes string entries as direct file paths and dictionary entries containing sub-page lists.*


### add_edit_urls_and_remove_mkdocs_markers (function, L586-L606)

> *Summary: This function processes generated MDX files within the build directory by injecting edit URLs and stripping specific MkDocs markers. It reads navigation data to locate relevant files, modifies their content in place, and overwrites them with the cleaned versions.*


### copy_images_from_notebooks_dir_to_target_dir (function, L609-L618)

> *Summary: This function copies all PNG and JPG files found within a specified source directory to a designated destination directory. It iterates over the contents of the input notebook directory and uses `shutil.copy` to transfer matching image files.*


### main (function, L621-L655)

> *Summary: Initializes the build environment by ensuring necessary directories exist and parses command-line arguments to configure processing paths. It then executes core notebook processing, followed by several post-processing steps like copying assets, updating navigation, fixing references, and cleaning up metadata within the target website directory.*

