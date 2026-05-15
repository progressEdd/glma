# autogen/beta/tools/skills/skill_search/extractor.py

3 function(s): _find_target_prefix, extract_skill, format_install_result.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _find_target_prefix | function |  |
| extract_skill | function |  |
| format_install_result | function |  |

## Chunks

### _find_target_prefix (function, L18-L59)

> *Summary: Determines the correct archive prefix for a given `skill_id` by checking several hierarchical patterns within a `tarfile`. It prioritizes specific directory structures, then scans all `SKILL.md` files to match based on frontmatter name, finally defaulting to the root directory if no match is found.*


### extract_skill (function, L62-L131)

> *Summary: Unpacks a compressed archive (`tar_path`) containing a specific skill identified by `skill_id` into a destination directory (`dest`). It searches for and extracts the skill's content, validates its metadata from `SKILL.md`, and returns a validated `SkillMetadata` object upon success.*


### format_install_result (function, L134-L145)

> *Summary: Generates a human-readable string summary detailing the installation of a skill based on its metadata and installation directory. It includes the skill name, description, version (if present), and a list of associated script names if they exist in the designated path.*

