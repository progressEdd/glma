# autogen/beta/tools/skills/runtime/protocol.py

1 class(es): SkillRuntime. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SkillRuntime | class |  |

## Chunks

### SkillRuntime (class, L13-L95)

> *Summary: Defines a protocol for managing skills, encompassing storage operations like `install` and `remove`, skill discovery methods such as `discover` and `load`, and execution capabilities via the `shell` method. It requires implementations to handle lifecycle events like ensuring storage readiness (`ensure_storage`) and cache invalidation (`invalidate`).*


### cleanup (method, L26-L28, parent: SkillRuntime)

> *Summary: This method is responsible for deleting any runtime storage when the process terminates, returning a boolean indicating success or failure.*


### lock_dir (method, L31-L38, parent: SkillRuntime)

> *Summary: Returns the absolute local `Path` to the directory where the `skills-lock.json` file is stored, which serves as host metadata for locking mechanisms. This path is derived from the runtime's installation directory.*


### discover (method, L40-L42, parent: SkillRuntime)

> *Summary: Retrieves and returns a list of `SkillMetadata` objects representing every skill currently available in the system.*


### load (method, L44-L46, parent: SkillRuntime)

> *Summary: Retrieves and returns the complete Markdown content of a specified skill file by its name. It takes a string representing the skill's identifier as input and outputs the corresponding skill documentation text.*


### get_path (method, L48-L54, parent: SkillRuntime)

> *Summary: Retrieves the filesystem `Path` object corresponding to a given skill name string. It raises a `KeyError` if the specified skill name does not exist within the system.*


### invalidate (method, L56-L58, parent: SkillRuntime)

> *Summary: Clears the internal discovery cache, typically called after an agent skill is installed or removed to ensure up-to-date state. This method takes no arguments and returns nothing.*


### ensure_storage (method, L60-L66, parent: SkillRuntime)

> *Summary: This method guarantees that the necessary persistent storage mechanism is initialized and available for the runtime environment. It handles setup specific to different runtime types, such as creating local directories or Docker volumes.*


### install (method, L68-L75, parent: SkillRuntime)

> *Summary: Moves skill files from a specified local staging path into the system's runtime storage, organizing them under the provided skill name. This operation finalizes the integration of an extracted skill for execution.*


### remove (method, L77-L84, parent: SkillRuntime)

> *Summary: Deletes a specified skill from storage, validating that the removal target remains within the installation directory. It raises errors if the name points outside the allowed scope or if the skill doesn't exist.*


### shell (method, L86-L95, parent: SkillRuntime)

> *Summary: Creates a `ShellEnvironment` object, taking an absolute path to a scripts directory as input. This environment encapsulates the necessary context for executing shell commands within that specified directory.*

