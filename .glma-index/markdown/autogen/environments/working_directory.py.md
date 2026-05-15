# autogen/environments/working_directory.py

1 class(es): WorkingDirectory. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| WorkingDirectory | class |  |

## Chunks

### WorkingDirectory (class, L15-L74)

> *Summary: This context manager allows temporarily changing the process's current working directory to a specified path, automatically restoring the original location upon exiting its scope. It supports creating and managing temporary directories via class methods for controlled cleanup.*


### __init__ (method, L20-L29, parent: WorkingDirectory)

> *Summary: Initializes an environment context by storing a target directory path and setting up internal state variables for tracking the original location, temporary file creation status, and token. This object manages the necessary information to temporarily alter the working directory.*


### __enter__ (method, L31-L41, parent: WorkingDirectory)

> *Summary: When entering a context, it saves the current working directory and changes to the specified path if provided, creating it first if necessary. It then registers itself as the active working directory within the environment's state before returning itself.*


### __exit__ (method, L43-L54, parent: WorkingDirectory)

> *Summary: Upon exiting the context, this method restores the process's working directory to its original location. It also cleans up any temporary directories that were created during the scope if they still exist.*


### create_tmp (method, L57-L62, parent: WorkingDirectory)

> *Summary: Generates a unique temporary directory using `tempfile.mkdtemp` and initializes an instance of the class with this path. It then marks the returned object as having been created from a temporary location.*


### get_current_working_directory (method, L65-L74, parent: WorkingDirectory)

> *Summary: Retrieves a `WorkingDirectory` instance, either returning the one explicitly passed as an argument or fetching the system's current directory if available; otherwise, it returns `None`.*

