# cli/src/ag2_cli/commands/publish.py

3 function(s): _validate_artifact, _run_gh, publish_artifact. 1 class(es): ValidationError. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ValidationError | class |  |
| _validate_artifact | function |  |
| _run_gh | function |  |
| publish_artifact | function |  |

## Chunks

### ValidationError (class, L56-L61)

> *Summary: Represents a single validation problem containing a severity level ("error" or "warning") and an associated descriptive message. This class is used to encapsulate specific issues found during data validation processes.*


### __init__ (method, L59-L61, parent: ValidationError)

> *Summary: Initializes an object to hold a logging severity level (either "error" or "warning") and the associated text message. It stores these two string inputs as instance attributes for later use in publishing logic.*


### _validate_artifact (function, L64-L139)

> *Summary: This function validates an artifact directory by reading and parsing its `artifact.json` manifest against predefined rules for required fields, types, and directory structures. It returns the parsed manifest dictionary along with a list of validation errors or warnings encountered during the process.*


### _run_gh (function, L142-L150)

> *Summary: Executes an external `gh` command using the system's shell. It takes a variable list of arguments and returns a `CompletedProcess` object containing stdout, stderr, and return code after a 120-second timeout.*


### publish_artifact (function, L154-L332)

> *Summary: This function validates an artifact structure from a specified directory, then conditionally forks and clones a target repository. If not in dry-run mode, it copies the validated artifact into the correct location within the cloned repo, commits the changes, pushes the new branch, and finally creates a pull request against the remote repository.*

