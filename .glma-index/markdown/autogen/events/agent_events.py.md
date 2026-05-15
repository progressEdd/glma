# autogen/events/agent_events.py

1 function(s): create_received_event_model. 35 class(es): BasePrintReceivedEvent, FunctionResponseEvent, ToolResponse, ToolResponseEvent, FunctionCall, FunctionCallEvent, ToolCall, ToolCallEvent, TextEvent, PostCarryoverProcessingEvent, ClearAgentsHistoryEvent, SpeakerAttemptSuccessfulEvent, SpeakerAttemptFailedMultipleAgentsEvent, SpeakerAttemptFailedNoAgentsEvent, GroupChatResumeEvent, GroupChatRunChatEvent, TerminationAndHumanReplyNoInputEvent, UsingAutoReplyEvent, TerminationEvent, ExecuteCodeBlockEvent, ExecuteFunctionEvent, ExecutedFunctionEvent, SelectSpeakerEvent, SelectSpeakerTryCountExceededEvent, SelectSpeakerInvalidInputEvent, ClearConversableAgentHistoryEvent, ClearConversableAgentHistoryWarningEvent, GenerateCodeExecutionReplyEvent, ConversableAgentUsageSummaryNoCostIncurredEvent, ConversableAgentUsageSummaryEvent, InputRequestEvent, AsyncInputRequestEvent, InputResponseEvent, ErrorEvent, RunCompletionEvent. 62 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BasePrintReceivedEvent | class |  |
| FunctionResponseEvent | class |  |
| ToolResponse | class |  |
| ToolResponseEvent | class |  |
| FunctionCall | class |  |
| FunctionCallEvent | class |  |
| ToolCall | class |  |
| ToolCallEvent | class |  |
| TextEvent | class |  |
| create_received_event_model | function |  |
| PostCarryoverProcessingEvent | class |  |
| ClearAgentsHistoryEvent | class |  |
| SpeakerAttemptSuccessfulEvent | class |  |
| SpeakerAttemptFailedMultipleAgentsEvent | class |  |
| SpeakerAttemptFailedNoAgentsEvent | class |  |
| GroupChatResumeEvent | class |  |
| GroupChatRunChatEvent | class |  |
| TerminationAndHumanReplyNoInputEvent | class |  |
| UsingAutoReplyEvent | class |  |
| TerminationEvent | class |  |
| ExecuteCodeBlockEvent | class |  |
| ExecuteFunctionEvent | class |  |
| ExecutedFunctionEvent | class |  |
| SelectSpeakerEvent | class |  |
| SelectSpeakerTryCountExceededEvent | class |  |
| SelectSpeakerInvalidInputEvent | class |  |
| ClearConversableAgentHistoryEvent | class |  |
| ClearConversableAgentHistoryWarningEvent | class |  |
| GenerateCodeExecutionReplyEvent | class |  |
| ConversableAgentUsageSummaryNoCostIncurredEvent | class |  |
| ConversableAgentUsageSummaryEvent | class |  |
| InputRequestEvent | class |  |
| AsyncInputRequestEvent | class |  |
| InputResponseEvent | class |  |
| ErrorEvent | class |  |
| RunCompletionEvent | class |  |

## Chunks

### BasePrintReceivedEvent (class, L59-L66)

> *Summary: Represents an event signaling that a print message has been received from a sender to a recipient. It outputs a formatted string containing the sender and recipient information when its `print` method is called.*


### print (method, L64-L66, parent: BasePrintReceivedEvent)

> *Summary: This method formats and outputs an event message to a specified recipient using a provided callable function. It prepends the sender's name in yellow color before sending the formatted string.*


### FunctionResponseEvent (class, L70-L85)

> *Summary: Represents a response received after executing a function call. It takes the function's name and content as input and prints a formatted block to the provided callable, clearly indicating it is a function role response.*


### print (method, L75-L85, parent: FunctionResponseEvent)

> *Summary: This method formats and outputs the agent's response to a provided callable stream. It prepends a header indicating the role and ID of the calling agent, followed by its content, and concludes with a separator line.*


### ToolResponse (class, L88-L99)

> *Summary: Represents the output from a tool execution, containing an optional `tool_call_id`, a fixed role of `"tool"`, and the result content. It provides a method to print this response in a formatted, colored manner to a specified stream or function.*


### print (method, L93-L99, parent: ToolResponse)

> *Summary: This method outputs a structured log to a provided callable stream. It prepends and appends formatted markers around the agent's content, including its role and tool call ID, ensuring immediate flushing of all output.*


### ToolResponseEvent (class, L103-L114)

> *Summary: Represents an event containing responses from tools executed by an agent. It accepts a list of `ToolResponse` objects and optional content, then prints the tool responses sequentially to a specified output stream.*


### print (method, L108-L114, parent: ToolResponseEvent)

> *Summary: This method forwards a printing function to itself and all associated `tool_responses`. It then iterates through these responses, calling their respective print methods before outputting a separator line.*


### FunctionCall (class, L117-L135)

> *Summary: Represents a suggested function call containing a name and arguments. It prints this structured information to a provided callable stream, highlighting the function name in green.*


### print (method, L121-L135, parent: FunctionCall)

> *Summary: This method formats and outputs a suggested function call to a provided callable stream. It constructs a string detailing the function's name and arguments, then prints this information in green formatting to the output stream.*


### FunctionCallEvent (class, L139-L152)

> *Summary: Represents an event triggered by a function call, holding the associated `FunctionCall` object and optional content data. It prints the provided content first, followed by the details of the function call, and concludes with a separator line.*


### print (method, L143-L152, parent: FunctionCallEvent)

> *Summary: This method executes a provided callable with the agent's content and then calls a print method on the function call object, finally printing a separator line. It ensures that any custom formatting or logging defined by `resolve_print_callable` is utilized during output.*


### ToolCall (class, L155-L176)

> *Summary: Represents a suggested tool invocation containing an ID, the function to call, and its type. It provides a `print` method that formats and outputs this information—including the function name and arguments—to a specified output stream or callable.*


### print (method, L160-L176, parent: ToolCall)

> *Summary: This method formats and outputs a suggested tool call to a provided callable stream. It constructs a detailed string including the event's ID, function name, and arguments before printing it in green color.*


### ToolCallEvent (class, L180-L198)

> *Summary: Represents an event signaling a tool invocation, carrying details like the role, content, and a list of specific `ToolCall` objects. It prints its contents by first calling the base print method, then outputting its main content if present, followed by printing each contained tool call.*


### print (method, L188-L198, parent: ToolCallEvent)

> *Summary: This method handles the display of an agent's content and associated tool calls by first resolving a provided callable function. It then executes this function with the agent's content and iterates through all registered tool calls to print their details before concluding with a separator line.*


### TextEvent (class, L202-L235)

> *Summary: Represents a text-based event containing various data types, including structured lists that might hold image references. It validates and replaces PIL image objects within the content with placeholders before printing the entire event structure to a provided callable.*


### _replace_pil_image_with_placeholder (method, L207-L209, parent: TextEvent)

> *Summary: If an input dictionary contains a PIL `Image` object under the `"url"` key, this method replaces that image object with the string placeholder `"<image>"`. This modifies the input dictionary in place.*


### validate_and_encode_content (method, L213-L226, parent: TextEvent)

> *Summary: If PIL is available, this method iterates through a list of dictionaries to replace image URLs specified as nested dictionaries with placeholders. It returns the modified list if it was a list, otherwise it returns the input content unchanged.*


### print (method, L228-L235, parent: TextEvent)

> *Summary: This method executes a provided callable with the agent's content string and then prints a separator line. It first resolves the input function before invoking it to display the current state of the agent.*


### create_received_event_model (function, L238-L282)

> *Summary: Constructs a specific event model based on the `role` and content of an input dictionary (`event`), using provided sender and recipient agent objects. It returns one of several specialized event types—like `FunctionResponseEvent`, `ToolCallEvent`, or `TextEvent`—after potentially processing the message content with context if it's a text-based event.*


### PostCarryoverProcessingEvent (class, L286-L381)

> *Summary: This event object encapsulates data from a chat session, including carryover context, messages, and participant details. It processes the `carryover` content into a printable string and provides methods to serialize its state or print a formatted summary of the event using a provided output function.*


### __init__ (method, L297-L332, parent: PostCarryoverProcessingEvent)

> *Summary: Initializes an event object by extracting and normalizing various parameters from a `chat_info` dictionary. It processes inputs like sender/recipient identifiers, message content (handling strings, callables, or dicts), and configuration settings for summarization and turn limits before passing them to the parent constructor.*


### serialize_model (method, L335-L348, parent: PostCarryoverProcessingEvent)

> *Summary: This method converts the agent's current state into a serializable dictionary representation. It packages essential information like its unique ID and detailed chat context (messages, sender/recipient, configuration) for persistence or transfer.*


### _process_carryover (method, L350-L363, parent: PostCarryoverProcessingEvent)

> *Summary: Converts the internal `carryover` attribute into a single string representation. It iterates through the list, ensuring each item is converted to a string—either directly or by extracting content from dictionaries—and joins them with newlines.*


### print (method, L365-L381, parent: PostCarryoverProcessingEvent)

> *Summary: This method displays a formatted event log by first resolving the provided callable and processing any carryover data. It outputs a header, then prints a starting message, followed by verbose details (message and carryover) if enabled, concluding with a footer.*


### ClearAgentsHistoryEvent (class, L385-L414)

> *Summary: This event signals the intent to clear agent interaction histories, optionally specifying a target agent and a number of recent events to keep. It outputs descriptive messages indicating whether the clearing applies to a specific agent or all agents, and if any preservation limit is set.*


### __init__ (method, L389-L400, parent: ClearAgentsHistoryEvent)

> *Summary: Initializes an event object by accepting optional UUID, an agent identifier (either an Agent instance or its name), and a count for preserved events. It passes these values up to the parent class constructor after resolving the agent input to ensure it's a string name if an object was provided.*


### print (method, L402-L414, parent: ClearAgentsHistoryEvent)

> *Summary: This method logs a message indicating the clearing of event history, either for a specific agent or all agents. It accepts an optional callable to handle the output and adjusts the log message based on whether an agent is present and how many events should be preserved.*


### SpeakerAttemptSuccessfulEvent (class, L419-L462)

> *Summary: Represents a successful selection event during a speaker choice process, carrying data on agent mentions, the current attempt number, and remaining attempts. It can be serialized to a dictionary format or printed to output with colored status messages.*


### __init__ (method, L425-L440, parent: SpeakerAttemptSuccessfulEvent)

> *Summary: Initializes an event object by accepting a unique identifier, a dictionary of mentions with counts, current and remaining attempt numbers, and an optional verbosity flag. It passes these parameters to the parent class constructor while deep-copying the `mentions` dictionary for immutability.*


### serialize_model (method, L443-L450, parent: SpeakerAttemptSuccessfulEvent)

> *Summary: Converts the agent's current state into a serializable dictionary representation. It packages essential attributes like UUID, mentions, attempt counts, and verbosity settings for persistence or transmission.*


### print (method, L452-L462, parent: SpeakerAttemptSuccessfulEvent)

> *Summary: This method displays a selection confirmation message to the console using a provided callable function. It retrieves the name of the first mentioned agent and prints a formatted string indicating the successful speaker selection attempt.*


### SpeakerAttemptFailedMultipleAgentsEvent (class, L466-L508)

> *Summary: Represents an event signaling that a speaker selection attempt involving multiple agents has failed. It stores the counts of mentioned agents, the current attempt number, remaining attempts, and verbosity settings, providing methods to serialize its state and print a failure notification.*


### __init__ (method, L472-L487, parent: SpeakerAttemptFailedMultipleAgentsEvent)

> *Summary: Initializes an event object by accepting optional UUID, a dictionary of mentions, current and remaining attempt counts, and a verbose flag. It passes these parameters to the parent class constructor after deep-copying the `mentions` dictionary.*


### serialize_model (method, L490-L497, parent: SpeakerAttemptFailedMultipleAgentsEvent)

> *Summary: Converts the agent's current state into a serializable dictionary representation. It packages essential attributes like UUID, mentions, attempt counts, and verbosity settings for persistence or transmission.*


### print (method, L499-L508, parent: SpeakerAttemptFailedMultipleAgentsEvent)

> *Summary: This method formats and outputs a failure message indicating that an agent selection attempt contained multiple agent names. It takes an optional callable for formatting and uses `resolve_print_callable` before printing the colored error string to standard output.*


### SpeakerAttemptFailedNoAgentsEvent (class, L512-L554)

> *Summary: Represents an event signaling that a speaker selection attempt failed because no agents were mentioned. It stores the current attempt number, remaining attempts, and mentions data, providing methods to serialize its state or print a failure notification.*


### __init__ (method, L518-L533, parent: SpeakerAttemptFailedNoAgentsEvent)

> *Summary: Initializes an event object by accepting a UUID, a dictionary of mentions, current and remaining attempt counts, and an optional verbosity flag. It passes these parameters to the parent class constructor while deep-copying the `mentions` dictionary for immutability.*


### serialize_model (method, L536-L543, parent: SpeakerAttemptFailedNoAgentsEvent)

> *Summary: Converts the agent's current state into a serializable dictionary representation. It packages essential attributes like UUID, mentions, attempt counts, and verbosity settings for external use or storage.*


### print (method, L545-L554, parent: SpeakerAttemptFailedNoAgentsEvent)

> *Summary: This method formats and outputs a failure message indicating that the current selection attempt lacked agent names. It takes an optional callable for formatting and uses `resolve_print_callable` before displaying the colored error string to standard output.*


### GroupChatResumeEvent (class, L558-L589)

> *Summary: Represents a state where a group chat session is resuming, carrying the name of the last participant and a list of preceding message events. It serializes this information into a dictionary format for persistence or transmission.*


### __init__ (method, L563-L571, parent: GroupChatResumeEvent)

> *Summary: Initializes an event object by accepting a unique identifier (optional), the name of the last speaker, a list of message types, and an optional silence flag. It passes these parameters to the parent constructor, using the `silent` flag to determine verbosity.*


### serialize_model (method, L574-L580, parent: GroupChatResumeEvent)

> *Summary: Converts the agent's current state into a serializable dictionary representation. It packages essential data like its unique ID, last speaker, event history, and verbose status for external use.*


### print (method, L582-L589, parent: GroupChatResumeEvent)

> *Summary: This method formats and displays a summary of prepared group chat events to the console. It takes an optional callable for output and prints a message indicating the number of events and the name of the last speaker.*


### GroupChatRunChatEvent (class, L593-L607)

> *Summary: Represents an event signaling the next speaker in a group chat session, capturing who is speaking and whether verbose output is enabled. It serializes its state including UUID, speaker identity, and silent status for external use.*


### __init__ (method, L597-L598, parent: GroupChatRunChatEvent)

> *Summary: Initializes an event with optional unique identifiers and specifies the source agent or a string identifier; it sets verbosity based on the `silent` flag.*


### serialize_model (method, L601-L602, parent: GroupChatRunChatEvent)

> *Summary: Converts the agent's state into a dictionary representation containing its unique ID, speaker designation, and whether it is currently silent based on verbosity settings. This serialization allows for easy persistence or transmission of the agent's current configuration.*


### print (method, L604-L607, parent: GroupChatRunChatEvent)

> *Summary: This method executes a provided callable, after resolving it, to output the current agent's speaker information in green text to standard output. It ensures immediate display of the message by setting `flush=True`.*


### TerminationAndHumanReplyNoInputEvent (class, L611-L637)

> *Summary: Represents an event triggered when a human-in-the-loop is prompted but offers no response. It stores the message prompting for input, the sender, and the recipient, and can be printed to standard output in red text.*


### __init__ (method, L618-L632, parent: TerminationAndHumanReplyNoInputEvent)

> *Summary: Initializes an event object by setting its unique identifier, a message for when no human input is present, and the sender and recipient entities. It normalizes the sender and recipient inputs to ensure they are strings representing names before passing them up to the parent class constructor.*


### print (method, L634-L637, parent: TerminationAndHumanReplyNoInputEvent)

> *Summary: This method executes a provided callable, after resolving it, to output a specific message prefixed with `\n>>>>>>>>` in red color and immediately flushes the output stream. It takes an optional callable as input and returns nothing.*


### UsingAutoReplyEvent (class, L641-L665)

> *Summary: Represents an event signaling that an auto-reply mechanism is active, capturing the input mode and the sender/recipient identities. It initializes with these details and provides a `print` method to log this state prominently.*


### __init__ (method, L646-L660, parent: UsingAutoReplyEvent)

> *Summary: Initializes an event object by setting its UUID, human input mode, and defining the sender and recipient. It normalizes the `sender` and `recipient` inputs to ensure they are strings representing names or identifiers before passing them up to the parent class constructor.*


### print (method, L662-L665, parent: UsingAutoReplyEvent)

> *Summary: This method executes a provided callable function after resolving it, printing a distinct "USING AUTO REPLY..." message in red color to the output stream. It takes an optional callable as input and returns nothing.*


### TerminationEvent (class, L669-L694)

> *Summary: Represents the end of a workflow by encapsulating the reason for termination, who sent the event, and who received it. It provides a method to print a highly visible, colored notification indicating the run's conclusion.*


### __init__ (method, L676-L689, parent: TerminationEvent)

> *Summary: Initializes an event by setting a unique identifier (optional), the originating agent or string, the target agent or string (optional), and a mandatory reason for termination. It normalizes sender and recipient inputs to ensure they are either names or `None` before passing them up the inheritance chain.*


### print (method, L691-L694, parent: TerminationEvent)

> *Summary: This method executes a provided callable, after resolving it, to output a formatted termination message including the agent's UUID and reason. It ensures the output is flushed immediately upon execution.*


### ExecuteCodeBlockEvent (class, L698-L730)

> *Summary: Represents an event signaling the execution of a code block, carrying the code string, programming language, count, and intended recipient. It formats and prints a notification indicating which code block is about to run.*


### __init__ (method, L704-L719, parent: ExecuteCodeBlockEvent)

> *Summary: Initializes an event object by accepting a unique identifier, code content, programming language, count of code blocks, and the intended recipient. It ensures the recipient is represented as a string name if it's an Agent instance.*


### print (method, L721-L730, parent: ExecuteCodeBlockEvent)

> *Summary: This method executes a provided callable function after formatting a descriptive message indicating the start of a code block, including its count and inferred language. It ensures the output is flushed immediately to the stream.*


### ExecuteFunctionEvent (class, L734-L766)

> *Summary: Represents an event signaling the execution of a specific function by another agent. It takes the function name, input arguments, and the intended recipient as inputs, and its primary behavior is to log this execution request with colored output.*


### __init__ (method, L740-L755, parent: ExecuteFunctionEvent)

> *Summary: Initializes an event object by accepting a function name, arguments dictionary, and a recipient (either an Agent instance or a string). It stores these details along with optional UUID and call ID information for tracking the event.*


### print (method, L757-L766, parent: ExecuteFunctionEvent)

> *Summary: This method executes a provided callable to log the execution of a function. It formats and outputs details including the function name, call ID, and input arguments using magenta coloring.*


### ExecutedFunctionEvent (class, L770-L808)

> *Summary: Represents an event signaling that a function has been executed, carrying details like the function name, input arguments, and the resulting content. It can be initialized with success status and provides a `print` method to log this execution information in a colored format.*


### __init__ (method, L778-L797, parent: ExecutedFunctionEvent)

> *Summary: Initializes an event object by storing details about a function call, including its name, arguments, content, and the intended recipient. It sets a flag to indicate whether the execution of the called function was successful.*


### print (method, L799-L808, parent: ExecutedFunctionEvent)

> *Summary: This method executes a provided callable to log the execution details of an agent function. It formats and outputs the function name, call ID, input arguments, and resulting content using magenta coloring.*


### SelectSpeakerEvent (class, L812-L825)

> *Summary: Represents an event signaling a request to choose the next speaker among a provided list of agents. It takes optional UUID and a list of agents as input, and its `print` method outputs a numbered selection prompt listing all available speakers.*


### __init__ (method, L815-L817, parent: SelectSpeakerEvent)

> *Summary: Initializes an event object by optionally accepting a UUID and a list of agents. It processes the input `agents` list to ensure all entries are represented as names before passing them up to the parent constructor.*


### print (method, L819-L825, parent: SelectSpeakerEvent)

> *Summary: This method displays a prompt asking the user to select the next speaker and then iterates through available agents to print numbered options to the provided callable function. It resolves any input callable before rendering the selection list.*


### SelectSpeakerTryCountExceededEvent (class, L829-L840)

> *Summary: Represents an event signaling that the maximum number of attempts to select a speaker has been reached. It stores the attempt count and a list of involved agents, printing a notification upon invocation.*


### __init__ (method, L833-L835, parent: SelectSpeakerTryCountExceededEvent)

> *Summary: Initializes an event object by accepting optional UUID, a required retry count, and a list of agents. It processes the input `agents` list to ensure all elements are agent names before passing them up to the parent constructor.*


### print (method, L837-L840, parent: SelectSpeakerTryCountExceededEvent)

> *Summary: Executes a provided callable, after resolving it, to log a message indicating the current attempt count and automatic selection of the next speaker. It takes an optional function as input and returns nothing.*


### SelectSpeakerInvalidInputEvent (class, L844-L854)

> *Summary: Represents an event signaling invalid user input during speaker selection, carrying a list of agent identifiers. It prints a message indicating the required numerical range based on the provided agents.*


### __init__ (method, L847-L849, parent: SelectSpeakerInvalidInputEvent)

> *Summary: Initializes an event object by optionally accepting a UUID and a list of agents. It processes the input `agents` list to ensure all entries are represented as names before passing them up to the parent constructor.*


### print (method, L851-L854, parent: SelectSpeakerInvalidInputEvent)

> *Summary: When called, this method resolves the provided callable and then executes it, passing a formatted error message indicating invalid input based on the agent count. It serves to log or display an error when input constraints are violated.*


### ClearConversableAgentHistoryEvent (class, L858-L883)

> *Summary: This event signals the intent to clear an agent's conversation history, specifying which agent is affected and how many events should be retained. It serializes this information and includes a method to log messages indicating the number of preserved events for debugging purposes.*


### __init__ (method, L863-L869, parent: ClearConversableAgentHistoryEvent)

> *Summary: Initializes an event object by accepting an optional UUID, an agent identifier (which can be an Agent object or a string), and an optional count for events to discard. It extracts the agent's name if provided as an object before passing these values up to the parent constructor.*


### serialize_model (method, L872-L877, parent: ClearConversableAgentHistoryEvent)

> *Summary: This method converts the agent's state into a serializable dictionary format. It returns a dictionary containing the agent's unique ID, associated agent object, and a flag indicating if events were preserved.*


### print (method, L879-L883, parent: ClearConversableAgentHistoryEvent)

> *Summary: This method iterates a number of times determined by `self.no_events_preserved`, calling the resolved callable function with a string indicating that an event is being preserved for the agent's history continuity. It effectively logs or signals the preservation of historical events within the agent context.*


### ClearConversableAgentHistoryWarningEvent (class, L887-L905)

> *Summary: This event signals a warning when clearing an agent's chat history, specifically noting that the `nr_preserved_events` setting is disregarded in this operation. It accepts a recipient identifier and prints a yellow-colored warning message upon invocation.*


### __init__ (method, L890-L894, parent: ClearConversableAgentHistoryWarningEvent)

> *Summary: Initializes an event by accepting an optional UUID and a recipient, which is resolved to either the recipient's name or the recipient object itself for internal use. This sets up the core identity and target of the event being created.*


### print (method, L896-L905, parent: ClearConversableAgentHistoryWarningEvent)

> *Summary: This method logs a warning message to the console, indicating that `nr_preserved_events` is disregarded when clearing chat history for a particular agent. It uses a resolved callable function to handle the output, applying yellow coloring to the warning text.*


### GenerateCodeExecutionReplyEvent (class, L909-L953)

> *Summary: This event structure carries a list of code blocks and identifies the sender and recipient of the execution result. It formats and prints a notification indicating whether one or multiple code blocks are being executed based on the contents of `code_blocks`.*


### __init__ (method, L914-L932, parent: GenerateCodeExecutionReplyEvent)

> *Summary: Initializes an event object by processing input code blocks to extract languages and setting default values for the sender if none is provided. It then passes these processed details, including UUID, to the parent class constructor.*


### print (method, L934-L953, parent: GenerateCodeExecutionReplyEvent)

> *Summary: This method outputs a header indicating the execution of one or multiple code blocks. It formats the message to show whether a single block or several blocks are being run, listing their inferred languages if more than one exists.*


### ConversableAgentUsageSummaryNoCostIncurredEvent (class, L957-L966)

> *Summary: Represents an event indicating that no usage costs were incurred by a specific recipient agent. It stores the recipient's identifier and prints a confirmation message upon invocation.*


### __init__ (method, L960-L961, parent: ConversableAgentUsageSummaryNoCostIncurredEvent)

> *Summary: Initializes an event by accepting an optional UUID and a recipient, which is resolved to either the recipient's name or the provided string directly. This sets up the core identity and target for the event object.*


### print (method, L963-L966, parent: ConversableAgentUsageSummaryNoCostIncurredEvent)

> *Summary: This method executes a provided callable function with a fixed string indicating no cost was incurred by the recipient agent. It first resolves the input callable before invoking it.*


### ConversableAgentUsageSummaryEvent (class, L970-L979)

> *Summary: This event object summarizes usage for a specific recipient agent. It stores the recipient's identifier and provides a method to print a formatted summary string containing that recipient's name.*


### __init__ (method, L973-L974, parent: ConversableAgentUsageSummaryEvent)

> *Summary: Initializes an event by accepting an optional UUID and a recipient, which is resolved to either the recipient's name or the provided string directly. This sets up the core identity and target for the event object.*


### print (method, L976-L979, parent: ConversableAgentUsageSummaryEvent)

> *Summary: This method executes a provided callable function with a formatted string indicating the agent and its recipient. It first resolves the input callable before invoking it to log or process the message.*


### InputRequestEvent (class, L983-L988)

> *Summary: Represents a request for user input, carrying the prompt text and an optional callback function to handle the response. It also includes a boolean flag indicating if password-like input is expected.*


### AsyncInputRequestEvent (class, L992-L997)

> *Summary: Represents an asynchronous request for input containing a prompt string and an optional password flag. It defines an asynchronous method to handle the subsequent `InputResponseEvent`.*


### a_respond (method, L996-L997, parent: AsyncInputRequestEvent)

> *Summary: This asynchronous method accepts an `InputResponseEvent` as input and is intended to handle or process the received response event. Currently, it contains no implementation logic.*


### InputResponseEvent (class, L1001-L1002)

> *Summary: Represents an event carrying a string value, typically signaling input or response data within the system. It inherits from `BaseEvent` and stores the relevant text in its `value` attribute.*


### ErrorEvent (class, L1006-L1007)

> *Summary: Represents an error occurrence by storing a generic `Any` type for the associated error details. This class inherits from `BaseEvent` to standardize event handling within the system.*


### RunCompletionEvent (class, L1011-L1016)

> *Summary: Represents the final state of an agent run by encapsulating a summary, the full message history, associated costs, and contextual data. It serves as an output event signaling the completion of a process execution.*

