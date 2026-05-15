# cli/src/ag2_cli/install/lockfile.py

2 class(es): InstalledArtifact, Lockfile. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| InstalledArtifact | class |  |
| Lockfile | class |  |

## Chunks

### InstalledArtifact (class, L14-L19)

> *Summary: Represents a deployed component, storing its reference, version, installation timestamp, and lists of associated targets and file paths. It serves as a structured record for tracking installed software artifacts within the system.*


### Lockfile (class, L22-L98)

> *Summary: Manages the `.ag2-artifacts.lock` file by loading its state from disk, allowing recording of new installations or uninstalls, and persisting changes back to the lockfile. It takes a project directory path as input and outputs a collection of installed artifact records.*


### __init__ (method, L25-L28, parent: Lockfile)

> *Summary: Initializes the lockfile handler by setting the path to a specific lockfile within the provided project directory and loading existing artifact data into an internal dictionary.*


### load (method, L30-L44, parent: Lockfile)

> *Summary: Reads a JSON lockfile from disk to populate the instance's `installed` dictionary. It parses artifact references, versions, and associated metadata into `InstalledArtifact` objects if the file exists; otherwise, it initializes an empty installation state.*


### save (method, L46-L51, parent: Lockfile)

> *Summary: Serializes the current installation state into a dictionary and writes it to the configured file path as formatted JSON. This method persists the tracked package information for later retrieval.*


### record_install (method, L53-L78, parent: Lockfile)

> *Summary: This method records an installed artifact by storing its reference, version, targets, and relative file paths within the instance's state. It takes a reference string, version string, list of target strings, and a list of `Path` objects as input, updating the internal record and persisting changes upon completion.*


### is_installed (method, L80-L85, parent: Lockfile)

> *Summary: Determines if a specified artifact reference exists in the installed set, optionally verifying it matches a given version string. It returns `True` only if the reference is present and either no specific version was requested or the stored version matches the requested one.*


### get_installed (method, L87-L88, parent: Lockfile)

> *Summary: Retrieves an artifact's installation details from the internal state using a provided reference string as input, returning the `InstalledArtifact` object or `None`.*


### record_uninstall (method, L90-L95, parent: Lockfile)

> *Summary: Removes a specified artifact reference from the internal installed list and persists the change if an entry was found. It returns the removed artifact's record, which can then be used for subsequent file cleanup operations.*


### list_installed (method, L97-L98, parent: Lockfile)

> *Summary: Retrieves all currently installed artifacts from the object's internal state and returns them as a list of `InstalledArtifact` objects.*

