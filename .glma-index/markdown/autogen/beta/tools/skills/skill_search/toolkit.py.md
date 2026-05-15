# autogen/beta/tools/skills/skill_search/toolkit.py

1 class(es): SkillSearchToolkit. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SkillSearchToolkit | class |  |

## Chunks

### SkillSearchToolkit (class, L24-L219)

> *Summary: Provides a toolkit to dynamically search for and install skills from the `skills.sh` ecosystem using HTTP/GitHub APIs, bypassing Node.js dependencies. It exposes methods to search for skills based on a query, download and install a specific skill ID into a local runtime environment, and remove installed skills.*


### __init__ (method, L79-L104, parent: SkillSearchToolkit)

> *Summary: Initializes a toolkit by setting up a local runtime environment and configuring a client connection to the skills service. It then delegates initialization to the parent `Toolkit` class, providing methods for listing, loading, running, searching, installing, and removing skills.*


### search_skills (method, L106-L146, parent: SkillSearchToolkit)

> *Summary: Provides a callable tool that queries an external skill database using a search query and optional limit. It returns a formatted string listing matching skills, their install counts, and the corresponding `install_skill` command for each result.*


### install_skill (method, L148-L192, parent: SkillSearchToolkit)

> *Summary: Creates a callable tool that downloads and installs a specified skill based on its ID. It parses the `skill_id` to determine the source and skill identifier, then uses the client and runtime to fetch and register the skill before returning an installation result string or an error message.*


### remove_skill (method, L194-L219, parent: SkillSearchToolkit)

> *Summary: This method generates a callable tool that removes an installed skill from the system's runtime based on the provided skill name. It attempts to remove the skill and then invalidates the runtime state, returning a success message or an error string if removal fails.*

