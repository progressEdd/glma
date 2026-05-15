# autogen/beta/tools/skills/runtime/local.py

1 class(es): LocalRuntime. 12 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LocalRuntime | class |  |

## Chunks

### LocalRuntime (class, L21-L115)

> *Summary: This class manages skill execution by providing local filesystem storage and subprocess capabilities. It accepts configuration for installation directories, timeouts, and blocked commands to discover, load, install, and remove skills from a specified location. The `shell` method allows it to spawn an environment for running external scripts using configured constraints.*


### __post_init__ (method, L57-L62, parent: LocalRuntime)

> *Summary: Initializes the skill runtime by setting up installation and extra path directories from provided configuration. It then creates a `SkillLoader` instance using these paths and registers a cleanup hook if destruction is requested.*


### install_dir (method, L65-L67, parent: LocalRuntime)

> *Summary: Retrieves the resolved installation directory path from the instance's internal state. This method returns a `Path` object representing where the software is installed.*


### lock_dir (method, L70-L71, parent: LocalRuntime)

> *Summary: Returns the path to the installation directory, which is used as a lock location for this instance.*


### discover (method, L73-L74, parent: LocalRuntime)

> *Summary: Retrieves a list of `SkillMetadata` objects by delegating the discovery process to an internal loader component. This method acts as a simple pass-through to expose available skills.*


### load (method, L76-L77, parent: LocalRuntime)

> *Summary: Retrieves a resource by its given string identifier from an internal loader mechanism. It acts as a simple pass-through to the underlying loading functionality.*


### get_path (method, L79-L80, parent: LocalRuntime)

> *Summary: Retrieves a file path based on a given string identifier by delegating the request to an internal loader object. It returns the resolved `Path` object corresponding to the input name.*


### invalidate (method, L82-L83, parent: LocalRuntime)

> *Summary: Triggers the invalidation process within the associated loader object. This method performs no external input and returns nothing upon execution.*


### ensure_runtime (method, L86-L89, parent: LocalRuntime)

> *Summary: If the provided runtime is already a `SkillRuntime` instance, it is returned directly; otherwise, a new `SkillRuntime` object is instantiated using the input path or string as its directory.*


### ensure_storage (method, L91-L92, parent: LocalRuntime)

> *Summary: This method guarantees the existence of the designated installation directory by creating it and any necessary parent directories if they do not already exist. It takes no inputs and performs an in-place modification to ensure proper storage setup.*


### install (method, L94-L98, parent: LocalRuntime)

> *Summary: Copies the contents of a specified `source` directory into a target location within the installation directory, overwriting any existing content at that destination path.*


### remove (method, L100-L106, parent: LocalRuntime)

> *Summary: Deletes a specified directory within the installation path if it exists and is safely contained within that path. It raises errors for path traversal attempts or when the target skill directory is missing.*


### shell (method, L108-L115, parent: LocalRuntime)

> *Summary: Creates and returns a `LocalShellEnvironment` instance configured with the provided scripts directory and various runtime constraints like timeout and output limits. This method encapsulates local shell execution capabilities for subsequent use within the agent framework.*

