# autogen/exception_utils.py

6 class(es): AgentNameConflictError, NoEligibleSpeakerError, SenderRequiredError, InvalidCarryOverTypeError, UndefinedNextAgentError, ModelToolNotSupportedError. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AgentNameConflictError | class |  |
| NoEligibleSpeakerError | class |  |
| SenderRequiredError | class |  |
| InvalidCarryOverTypeError | class |  |
| UndefinedNextAgentError | class |  |
| ModelToolNotSupportedError | class |  |

## Chunks

### AgentNameConflictError (class, L22-L24)

> *Summary: This custom exception signals when two or more agents share an identical name. It initializes with a default message indicating the conflict and accepts optional arguments for further context.*


### __init__ (method, L23-L24, parent: AgentNameConflictError)

> *Summary: Initializes an exception instance, defaulting to a message indicating duplicate agent names if no specific message is provided. It accepts optional positional and keyword arguments to pass up to the parent constructor.*


### NoEligibleSpeakerError (class, L28-L33)

> *Summary: Signals an error when a group chat cannot proceed because no suitable participants are available. It initializes with an optional custom message detailing the reason for early termination.*


### __init__ (method, L31-L33, parent: NoEligibleSpeakerError)

> *Summary: Initializes an exception with a customizable error message, defaulting to "No eligible speakers." The provided message is then passed up to the parent class constructor.*


### SenderRequiredError (class, L37-L42)

> *Summary: This custom exception signals that a necessary sender entity was missing during an operation. It accepts an optional message to customize the error description upon raising.*


### __init__ (method, L40-L42, parent: SenderRequiredError)

> *Summary: Initializes an exception instance with a customizable error message, defaulting to a specific sender requirement warning if none is provided. This sets the internal state for subsequent error handling.*


### InvalidCarryOverTypeError (class, L46-L53)

> *Summary: This custom exception signals an error when the provided carryover type is incorrect. It initializes with a default message indicating that the carryover must be a string or list of strings, preventing message modification.*


### __init__ (method, L49-L53, parent: InvalidCarryOverTypeError)

> *Summary: Initializes an exception with a customizable error message, defaulting to a specific warning about expected data types for carryover. This sets up the instance's primary descriptive content for later use in error handling.*


### UndefinedNextAgentError (class, L57-L62)

> *Summary: This custom exception signals an error when a specified list of subsequent agents has no members in common with the current agent group. It inherits from `Exception` and allows for a customizable error message upon instantiation.*


### __init__ (method, L60-L62, parent: UndefinedNextAgentError)

> *Summary: Initializes an exception object, setting a default or custom error message indicating a lack of agent overlap between a provided list and a defined group. This constructor stores the message internally for later use by the parent class.*


### ModelToolNotSupportedError (class, L65-L73)

> *Summary: This exception signals that a requested tool is incompatible with the specified model. It initializes with the model name and sets a descriptive error message pointing to relevant documentation.*


### __init__ (method, L68-L73, parent: ModelToolNotSupportedError)

> *Summary: Initializes an exception object, setting a predefined error message that warns users about tool incompatibility for a specified model. This message directs them to OpenAI documentation regarding model limitations.*

