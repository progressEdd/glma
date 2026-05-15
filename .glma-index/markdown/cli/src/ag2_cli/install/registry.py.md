# cli/src/ag2_cli/install/registry.py

3 function(s): parse_frontmatter, load_pack, list_packs. 2 class(es): ContentItem, Pack.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ContentItem | class |  |
| Pack | class |  |
| parse_frontmatter | function |  |
| load_pack | function |  |
| list_packs | function |  |

## Chunks

### ContentItem (class, L13-L18)

> *Summary: Represents a piece of content with metadata including a name, description, category (e.g., 'rule', 'skill'), and structured frontmatter. It stores the main textual content in its `body` attribute.*


### Pack (class, L22-L27)

> *Summary: Represents a collection of content items, holding metadata such as name, display name, description, and version. It is initialized with a string name and can contain a list of `ContentItem` objects.*


### parse_frontmatter (function, L30-L56)

> *Summary: Extracts metadata from YAML frontmatter located between `---` delimiters at the start of a string. It returns a dictionary containing the parsed key-value pairs and the remaining markdown body text.*


### load_pack (function, L59-L94)

> *Summary: Reads a content pack directory specified by name, validates its manifest, and then parses all Markdown files within predefined subdirectories to construct and return a `Pack` object containing various `ContentItem`s. If the directory or manifest is missing, it returns `None`.*


### list_packs (function, L97-L101)

> *Summary: Retrieves a list of available pack names by scanning the `CONTENT_DIR`. It returns an empty list if the directory doesn't exist, otherwise it lists sorted subdirectory names that contain a `manifest.json` file.*

