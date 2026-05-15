# cli/src/ag2_cli/install/targets/copilot.py

1 class(es): CopilotTarget. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CopilotTarget | class |  |

## Chunks

### CopilotTarget (class, L11-L37)

> *Summary: This class manages the installation and removal of GitHub Copilot configuration files within a project's `.github/instructions` directory. It takes content items as input to generate specific instruction markdown files based on glob patterns, returning the paths of the created files upon installation.*


### install (method, L16-L27, parent: CopilotTarget)

> *Summary: Creates instruction files within a `.github/instructions` directory inside the provided project path. It iterates over input content items, generating Markdown files for each that specify glob patterns and include the item's body content.*


### uninstall (method, L29-L37, parent: CopilotTarget)

> *Summary: Removes specific instruction files matching the pattern `ag2-*.instructions.md` from a designated `.github/instructions` directory within the provided project path. It returns a list of all successfully deleted file paths.*

