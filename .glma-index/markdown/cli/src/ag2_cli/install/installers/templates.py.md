# cli/src/ag2_cli/install/installers/templates.py

3 function(s): _substitute, _slugify, _matches_ignore. 1 class(es): TemplateInstaller. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TemplateInstaller | class |  |
| _substitute | function |  |
| _slugify | function |  |
| _matches_ignore | function |  |

## Chunks

### TemplateInstaller (class, L20-L253)

> *Summary: Handles the installation of project templates by fetching artifacts, resolving user-provided and default variables, copying scaffold files with substitution, installing bundled skills, and executing post-install commands. It accepts a template name, target directories, optional variables, and a preview flag to return an `InstallResult` detailing created files and dependencies.*


### __init__ (method, L23-L33, parent: TemplateInstaller)

> *Summary: Initializes the installer by accepting and storing instances of an `ArtifactClient`, `Lockfile`, `DependencyResolver`, and `SkillsInstaller`. These dependencies are used to manage artifact retrieval, dependency resolution, and skill installation during the setup process.*


### install (method, L35-L107, parent: TemplateInstaller)

> *Summary: Fetches a template artifact based on a name and installs it into a specified project directory. It processes the artifact by copying scaffolds, installing bundled skills for given targets, resolving dependencies, and running post-install commands before recording the installation in a lockfile. The method accepts an optional dictionary of variables and a boolean flag to enable preview mode, returning an `InstallResult` detailing the installation outcome.*


### _resolve_variables (method, L109-L141, parent: TemplateInstaller)

> *Summary: This method merges user-provided configuration values with defaults from a template specification, prompting interactively for any missing required variables. It then applies transformations, such as slugifying the value, before returning the complete dictionary of resolved variables.*


### _copy_scaffold (method, L143-L190, parent: TemplateInstaller)

> *Summary: Copies files from a source directory to a destination, substituting placeholders in `.tmpl` files using provided variables. It recursively traverses the source, skips ignored paths, and ensures path safety before creating or copying content to the target location.*


### _preview (method, L192-L215, parent: TemplateInstaller)

> *Summary: Generates a preview of the installation by scanning template files within a specified scaffold directory. It substitutes variables into file paths and returns an `InstallResult` containing the list of intended output files without actually writing them to disk.*


### _run_post_install (method, L217-L253, parent: TemplateInstaller)

> *Summary: Executes a list of shell commands in the specified directory after prompting the user for confirmation. It handles execution errors, timeouts, and displays success or failure status for each command run.*


### _substitute (function, L256-L261)

> *Summary: Replaces placeholders like `{{ var }}` and `{{var}}` within a string using provided key-value pairs. It takes the template text and a dictionary of substitutions as input, returning the fully rendered string.*


### _slugify (function, L264-L270)

> *Summary: Transforms an input string into a URL or filesystem-safe slug by converting it to lowercase, removing special characters, and replacing whitespace with hyphens. It ensures the resulting string is clean and free of leading/trailing hyphens.*


### _matches_ignore (function, L273-L277)

> *Summary: Determines if a given file path matches a specified ignore pattern using simple glob matching against both the full path and just the filename component. Returns `True` if either match is found.*

