# cli/src/ag2_cli/install/targets/claude.py

1 class(es): ClaudeTarget. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ClaudeTarget | class |  |

## Chunks

### ClaudeTarget (class, L11-L67)

> *Summary: This class manages the installation and uninstallation of Claude-specific content within a project directory. It takes a list of `ContentItem`s, installing them as either skills (with frontmatter metadata) or commands into designated `.claude` subdirectories, and provides a method to recursively remove these installed files upon uninstallation.*


### install (method, L16-L23, parent: ClaudeTarget)

> *Summary: This method iterates over a list of content items and installs each one based on its category. It delegates the installation to either a command installer or a skill installer, returning a list of resulting file paths.*


### _install_skill (method, L25-L39, parent: ClaudeTarget)

> *Summary: Creates a dedicated directory structure within the project for a specific skill, then writes a `SKILL.md` file containing metadata (including auto/user invocability based on category) and the item's body content to that location. It returns the full path to the newly created skill file.*


### _install_command (method, L41-L47, parent: ClaudeTarget)

> *Summary: Creates a specific markdown file within the project's `.claude/commands` directory. It takes a project path and content item, generating a file containing the item's name, description, and body as its content.*


### uninstall (method, L49-L67, parent: ClaudeTarget)

> *Summary: Removes Claude-related files and directories from a given project path, specifically targeting skill folders prefixed with "ag2-" and markdown command files matching the pattern. It returns a list of all file paths that were successfully deleted during the uninstallation process.*

