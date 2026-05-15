# autogen/beta/tools/skills/local_skills/loader.py

1 function(s): parse_frontmatter. 1 class(es): SkillLoader. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| parse_frontmatter | function |  |
| SkillLoader | class |  |

## Chunks

### parse_frontmatter (function, L15-L27)

> *Summary: Extracts metadata from the YAML frontmatter block (delimited by `---`) found at the beginning of a string input. It returns a dictionary containing the parsed key-value pairs, or an empty dictionary if no valid frontmatter is present.*


### SkillLoader (class, L30-L168)

> *Summary: Scans configured filesystem paths to discover skills by reading `SKILL.md` files, prioritizing paths based on a defined order. It returns a list of skill metadata objects, caching results after the first scan, and provides methods to retrieve full content or directory paths for specific named skills.*


### __init__ (method, L54-L61, parent: SkillLoader)

> *Summary: Initializes the loader by accepting one or more file paths to load skills from, defaulting to predefined paths if none are provided. It stores these paths and a strict mode flag, initializing an internal cache for skill metadata.*


### invalidate (method, L63-L68, parent: SkillLoader)

> *Summary: Clears the internal cache of skill metadata, forcing a complete filesystem scan on the subsequent discovery operation. This method ensures that outdated or newly added skills are detected upon the next invocation.*


### discover (method, L70-L109, parent: SkillLoader)

> *Summary: Scans configured directories to find and load metadata for all available skills, prioritizing the first encountered skill name if duplicates exist across paths. It returns a sorted list of `SkillMetadata` objects, caching results unless explicitly invalidated.*


### load (method, L111-L118, parent: SkillLoader)

> *Summary: Retrieves the complete content of a specified skill's `SKILL.md` file, using the provided skill name as input. It returns the file's text content or raises a `KeyError` if the skill cannot be located.*


### get_path (method, L120-L126, parent: SkillLoader)

> *Summary: Retrieves the file system directory path for a specified skill name. It delegates the actual search to an internal method and raises a `KeyError` if the requested skill does not exist.*


### _find_dir (method, L128-L136, parent: SkillLoader)

> *Summary: This method locates the directory path for a given skill name by iterating through all discovered metadata. It validates that the input name is non-empty and contains no path separators before returning the corresponding `Path` object or raising an error if the skill isn't found.*


### validate_skill_metadata (method, L139-L168, parent: SkillLoader)

> *Summary: Checks if a skill's metadata, provided via frontmatter and an `SkillMetadata` object, adheres to predefined constraints. It validates the presence, length, format (regex), and consistency of fields like name, description, compatibility, and tool definitions against the input directory structure.*

