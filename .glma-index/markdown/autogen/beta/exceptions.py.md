# autogen/beta/exceptions.py

2 function(s): missing_additional_dependency, missing_optional_dependency. 15 class(es): AG2Error, ToolConflictError, ToolResolutionError, ToolExecutionError, ToolNotFoundError, UnsupportedToolError, UnsupportedInputError, HumanInputNotProvidedError, ConfigNotProvidedError, SkillError, SkillNotFoundError, InvalidSkillNameError, InvalidSkillError, SkillDownloadError, SkillInstallError. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AG2Error | class |  |
| ToolConflictError | class |  |
| ToolResolutionError | class |  |
| ToolExecutionError | class |  |
| ToolNotFoundError | class |  |
| UnsupportedToolError | class |  |
| UnsupportedInputError | class |  |
| HumanInputNotProvidedError | class |  |
| ConfigNotProvidedError | class |  |
| SkillError | class |  |
| SkillNotFoundError | class |  |
| InvalidSkillNameError | class |  |
| InvalidSkillError | class |  |
| SkillDownloadError | class |  |
| SkillInstallError | class |  |
| missing_additional_dependency | function |  |
| missing_optional_dependency | function |  |

## Chunks

### AG2Error (class, L8-L9)

> *Summary: Serves as the root exception class for all errors encountered within the AG2 beta environment. It inherits from Python's base `Exception` to allow for custom error handling across the system.*


### ToolConflictError (class, L12-L14)

> *Summary: Raised when an attempt is made to register a tool whose name already exists in the system. It accepts the conflicting tool's name as input and signals the conflict via its initialization message.*


### __init__ (method, L13-L14, parent: ToolConflictError)

> *Summary: Initializes an exception instance when attempting to register a tool that already exists. It takes the `tool_name` as input and sets the error message indicating the conflict.*


### ToolResolutionError (class, L17-L23)

> *Summary: This exception signals that an AgentSpec requires tools which are not present in the provided pool. It stores lists of the requested but missing tools and all currently available tools for detailed error reporting.*


### __init__ (method, L20-L23, parent: ToolResolutionError)

> *Summary: Initializes an exception object by storing lists of `missing` and `available` tools, then sets the error message to detail which tools could not be resolved against the available set.*


### ToolExecutionError (class, L26-L27)

> *Summary: Represents a fundamental error encountered during the execution of an external tool. It inherits from `AG2Error` to signify issues specific to tool operations within the system.*


### ToolNotFoundError (class, L30-L34)

> *Summary: This exception signals that a specified tool could not be located during execution. It is initialized with the name of the missing tool to provide context in its error message.*


### __init__ (method, L33-L34, parent: ToolNotFoundError)

> *Summary: Initializes an exception indicating that a specified tool could not be located. It accepts a string representing the missing tool's name and sets the error message accordingly.*


### UnsupportedToolError (class, L37-L41)

> *Summary: This exception signals that a requested tool type is not recognized or supported by the specified service provider. It requires both the unsupported `tool_type` and the relevant `provider` as input to raise.*


### __init__ (method, L40-L41, parent: UnsupportedToolError)

> *Summary: Initializes an exception when a specified `tool_type` is not supported by the given `provider`. It constructs and stores a descriptive error message detailing the unsupported combination.*


### UnsupportedInputError (class, L44-L48)

> *Summary: This exception signals that a provided input type is incompatible with the specified service provider. It requires both the unsupported input type and the name of the provider to be raised.*


### __init__ (method, L47-L48, parent: UnsupportedInputError)

> *Summary: Initializes an exception indicating that a specified `input_type` is not supported by the given `provider`. It constructs and stores a descriptive error message containing both the unsupported type and the provider name.*


### HumanInputNotProvidedError (class, L51-L61)

> *Summary: Signals an error when the system expects human intervention but receives no input. It inherits from a base error and provides a default message guiding the user on how to supply the required input.*


### __init__ (method, L54-L61, parent: HumanInputNotProvidedError)

> *Summary: Initializes an exception, defaulting to a specific message if none is provided. This default message guides the user on how to correctly configure human-in-the-loop interaction for agents.*


### ConfigNotProvidedError (class, L64-L71)

> *Summary: This exception signals that a required model configuration is missing during an agent request. It raises with a default message instructing the user to provide the configuration either during agent instantiation or when calling the ask method.*


### __init__ (method, L67-L71, parent: ConfigNotProvidedError)

> *Summary: Initializes an exception, defaulting to a specific error message if none is provided. This ensures that when no configuration is supplied during agent setup or invocation, a descriptive error is raised.*


### SkillError (class, L74-L75)

> *Summary: Represents a base error specifically for issues encountered while loading local skills, adhering to the agentskills.io standard. It inherits from `AG2Error` to categorize skill-related failures.*


### SkillNotFoundError (class, L78-L79)

> *Summary: This exception signals that a requested skill could not be located within the system's defined search paths. It inherits from `SkillError` and `KeyError`, indicating both a domain-specific error and a missing key issue.*


### InvalidSkillNameError (class, L82-L83)

> *Summary: This exception signals that a provided skill name is either missing or improperly formatted. It inherits from `ValueError`, indicating an issue with the input data itself.*


### InvalidSkillError (class, L86-L87)

> *Summary: This exception signals that provided skill metadata does not conform to the required specifications. It inherits from both `SkillError` and `ValueError`.*


### SkillDownloadError (class, L90-L91)

> *Summary: This exception signals an issue encountered while attempting to fetch a skill from a remote registry. It inherits from `SkillError` and is raised upon download failure.*


### SkillInstallError (class, L94-L95)

> *Summary: This exception signals an issue during the installation process of a downloaded skill. It is raised specifically when the skill archive fails extraction or validation checks.*


### missing_additional_dependency (function, L98-L104)

> *Summary: Creates a mock object that simulates an `ImportError` when called, specifically indicating that a required optional dependency is missing and suggesting the installation command. It takes the component name, the missing dependency name, and the original import error as input.*


### missing_optional_dependency (function, L107-L108)

> *Summary: This function wraps an `ImportError` to signal that a specified optional dependency is absent. It reuses another internal helper to construct and return a mock exception object containing the dependency name and extra requirement.*

