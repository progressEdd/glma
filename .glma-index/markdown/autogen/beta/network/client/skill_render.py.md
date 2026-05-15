# autogen/beta/network/client/skill_render.py

2 function(s): parse_skill_frontmatter, render_fallback_skill. 1 class(es): ParsedSkill. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ParsedSkill | class |  |
| parse_skill_frontmatter | function |  |
| render_fallback_skill | function |  |

## Chunks

### ParsedSkill (class, L45-L58)

> *Summary: This class inherits from `dict` to represent a skill structure containing metadata and content. It provides convenient properties (`frontmatter` and `body`) for accessing the parsed dictionary's components while maintaining JSON serialization compatibility.*


### frontmatter (method, L53-L54, parent: ParsedSkill)

> *Summary: Retrieves the metadata dictionary stored within the object's internal state and returns it as a standard Python dictionary.*


### body (method, L57-L58, parent: ParsedSkill)

> *Summary: Retrieves the stored content from the object's internal dictionary under the key "body" and returns it as a string.*


### parse_skill_frontmatter (function, L64-L95)

> *Summary: This function parses a Markdown string to separate its YAML frontmatter from the main content body. It returns a `ParsedSkill` object containing a dictionary of parsed key-value pairs for the frontmatter and the remaining text as the body, handling cases where fences are missing or malformed by treating everything as the body.*


### render_fallback_skill (function, L98-L138)

> *Summary: Generates a structured, Markdown-like string representation of an agent's profile when no specific skill document exists. It takes `Passport` and `Resume` objects as input and outputs a single string containing sections for name, description, capabilities, domains, track record, and examples.*

