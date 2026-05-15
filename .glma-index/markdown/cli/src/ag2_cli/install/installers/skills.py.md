# cli/src/ag2_cli/install/installers/skills.py

1 function(s): load_skills_from_artifact. 1 class(es): SkillsInstaller. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| load_skills_from_artifact | function |  |
| SkillsInstaller | class |  |

## Chunks

### load_skills_from_artifact (function, L15-L76)

> *Summary: Reads skill definitions from an `Artifact` by checking specific subdirectories within its source path. It supports two formats—a directory structure containing `SKILL.md` files or a flat `.md` file format—and returns a list of parsed `ContentItem` objects.*


### SkillsInstaller (class, L79-L180)

> *Summary: Installs specified skill packs by fetching them either from local bundles or a remote client, then applies the contents to designated IDE targets within a project directory. It records the installation details in a lockfile upon successful completion, returning a list of results detailing created files and used targets.*


### __init__ (method, L82-L85, parent: SkillsInstaller)

> *Summary: Initializes the installer with necessary dependencies: an `ArtifactClient` for artifact management, a `Lockfile` to manage package versions, and a `DependencyResolver` to handle dependency resolution logic. These components are stored as instance attributes for later use in installation processes.*


### install (method, L87-L103, parent: SkillsInstaller)

> *Summary: This method installs multiple skill packs by iterating over a list of provided pack identifiers. It takes target configurations and a project directory as input, returning a list of installation results for each requested pack.*


### _install_one (method, L105-L137, parent: SkillsInstaller)

> *Summary: This method installs a single skill pack by loading the artifact and filtering its items based on an optional name filter. It then applies these items to specified targets within a project directory, recording the installation details in a lockfile before returning the results.*


### _load_skills (method, L139-L180, parent: SkillsInstaller)

> *Summary: Retrieves skill data by first checking a hardcoded bundle for specific legacy owners/names, then attempting to fetch from a remote cache; if both fail, it tries loading the requested pack by exact name before raising an error. It returns an `Artifact` object representing the skills and a list of associated `ContentItem`s.*

