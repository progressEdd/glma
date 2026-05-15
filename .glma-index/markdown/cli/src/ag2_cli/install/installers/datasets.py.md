# cli/src/ag2_cli/install/installers/datasets.py

1 function(s): _copy_data. 1 class(es): DatasetInstaller. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| DatasetInstaller | class |  |
| _copy_data | function |  |

## Chunks

### DatasetInstaller (class, L16-L129)

> *Summary: This class manages the installation of dataset artifacts by fetching metadata and content from a client. It copies inline data, optionally downloads remote files based on a `full` flag, writes schema information, installs bundled skills, and resolves dependencies before recording the successful installation in a lockfile.*


### __init__ (method, L19-L29, parent: DatasetInstaller)

> *Summary: Initializes the dataset installer by accepting and storing instances of an `ArtifactClient`, `Lockfile`, `DependencyResolver`, and `SkillsInstaller`. These dependencies are used to manage artifact retrieval, dependency resolution, and skill installation during setup.*


### install (method, L31-L129, parent: DatasetInstaller)

> *Summary: This method installs a specified dataset artifact into a project directory by first fetching its metadata. It copies inline data, optionally downloads remote files based on the `full` flag, writes schema information, and installs any bundled skills or resolves dependencies before recording the installation in a lockfile.*


### _copy_data (function, L132-L144)

> *Summary: This function recursively copies all files from a source directory to a destination directory, ensuring the destination structure is created as needed. It returns a list of paths corresponding to the newly copied files.*

