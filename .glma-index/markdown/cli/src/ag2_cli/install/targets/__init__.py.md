# cli/src/ag2_cli/install/targets/__init__.py

8 function(s): _cursor_fm, _windsurf_fm, _continue_fm, _openhands_fm, _cline_fm, get_target, get_all_targets, detect_targets.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _cursor_fm | function |  |
| _windsurf_fm | function |  |
| _continue_fm | function |  |
| _openhands_fm | function |  |
| _cline_fm | function |  |
| get_target | function |  |
| get_all_targets | function |  |
| detect_targets | function |  |

## Chunks

### _cursor_fm (function, L15-L20)

> *Summary: Constructs a metadata dictionary from a `ContentItem`, including its description and optional glob patterns or an `alwaysApply` flag found in the item's frontmatter. This function transforms content item data into a structured format suitable for further processing.*


### _windsurf_fm (function, L23-L27)

> *Summary: Extracts metadata from a `ContentItem`, specifically including its description and any defined glob patterns from the frontmatter. It returns a dictionary containing this extracted information.*


### _continue_fm (function, L30-L35)

> *Summary: Transforms a `ContentItem` into a dictionary suitable for front matter by prepending "ag2-" to the name and including glob patterns or an `alwaysApply` flag if present in the item's metadata. This function returns a structured dictionary containing the processed item details.*


### _openhands_fm (function, L38-L43)

> *Summary: Transforms a `ContentItem` into a dictionary representing an installation target configuration. It constructs the target name by prefixing the item's name with "ag2-" and sets fixed trigger type and keyword values.*


### _cline_fm (function, L46-L50)

> *Summary: Constructs a metadata dictionary from a `ContentItem`, including its description and any specified glob patterns found within the item's frontmatter. This function extracts key configuration details for processing.*


### get_target (function, L167-L169)

> *Summary: Retrieves a specific `Target` object from an internal map using the provided string name as input, returning the corresponding target or `None` if not found.*


### get_all_targets (function, L172-L174)

> *Summary: Retrieves a complete list of all currently registered `Target` objects from the global registry. It returns this collection as a standard Python list.*


### detect_targets (function, L177-L179)

> *Summary: This function scans a given project directory to automatically identify all available build targets. It returns a list containing only those `Target` objects that successfully detect their presence within the provided path.*

