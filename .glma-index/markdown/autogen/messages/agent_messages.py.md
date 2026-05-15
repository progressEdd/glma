# autogen/messages/agent_messages.py

1 function(s): create_received_message_model. 30 class(es): BasePrintReceivedMessage, FunctionResponseMessage, ToolResponse, ToolResponseMessage, FunctionCall, FunctionCallMessage, ToolCall, ToolCallMessage, TextMessage, PostCarryoverProcessingMessage, ClearAgentsHistoryMessage, SpeakerAttemptSuccessfulMessage, SpeakerAttemptFailedMultipleAgentsMessage, SpeakerAttemptFailedNoAgentsMessage, GroupChatResumeMessage, GroupChatRunChatMessage, TerminationAndHumanReplyNoInputMessage, UsingAutoReplyMessage, TerminationMessage, ExecuteCodeBlockMessage, ExecuteFunctionMessage, ExecutedFunctionMessage, SelectSpeakerMessage, SelectSpeakerTryCountExceededMessage, SelectSpeakerInvalidInputMessage, ClearConversableAgentHistoryMessage, ClearConversableAgentHistoryWarningMessage, GenerateCodeExecutionReplyMessage, ConversableAgentUsageSummaryNoCostIncurredMessage, ConversableAgentUsageSummaryMessage. 54 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| BasePrintReceivedMessage | class |  |
| FunctionResponseMessage | class |  |
| ToolResponse | class |  |
| ToolResponseMessage | class |  |
| FunctionCall | class |  |
| FunctionCallMessage | class |  |
| ToolCall | class |  |
| ToolCallMessage | class |  |
| TextMessage | class |  |
| create_received_message_model | function |  |
| PostCarryoverProcessingMessage | class |  |
| ClearAgentsHistoryMessage | class |  |
| SpeakerAttemptSuccessfulMessage | class |  |
| SpeakerAttemptFailedMultipleAgentsMessage | class |  |
| SpeakerAttemptFailedNoAgentsMessage | class |  |
| GroupChatResumeMessage | class |  |
| GroupChatRunChatMessage | class |  |
| TerminationAndHumanReplyNoInputMessage | class |  |
| UsingAutoReplyMessage | class |  |
| TerminationMessage | class |  |
| ExecuteCodeBlockMessage | class |  |
| ExecuteFunctionMessage | class |  |
| ExecutedFunctionMessage | class |  |
| SelectSpeakerMessage | class |  |
| SelectSpeakerTryCountExceededMessage | class |  |
| SelectSpeakerInvalidInputMessage | class |  |
| ClearConversableAgentHistoryMessage | class |  |
| ClearConversableAgentHistoryWarningMessage | class |  |
| GenerateCodeExecutionReplyMessage | class |  |
| ConversableAgentUsageSummaryNoCostIncurredMessage | class |  |
| ConversableAgentUsageSummaryMessage | class |  |

## Chunks

### BasePrintReceivedMessage (class, L86-L93)

> *Summary: Represents a message received from another agent containing content and sender/recipient names. Its `print` method outputs the message to a specified or default stream, highlighting the sender's name in yellow.*


### print (method, L91-L93, parent: BasePrintReceivedMessage)

> *Summary: This method outputs a formatted message to the console, prepending it with the sender's name in yellow and indicating the recipient. It uses an optional callable function to handle the actual printing mechanism.*


### FunctionResponseMessage (class, L98-L113)

> *Summary: Represents a response received from a function call, containing the function's name and content. It prints a formatted output to the provided stream, clearly demarcating the function response with green coloring.*


### print (method, L103-L113, parent: FunctionResponseMessage)

> *Summary: This method formats and outputs the agent's response to a provided callable stream. It prepends a colored header indicating the role and name of the sender, followed by the content, and concludes with a separator line.*


### ToolResponse (class, L116-L127)

> *Summary: Represents the output from a tool execution, containing an optional `tool_call_id`, a fixed `"tool"` role, and the result content. It provides a helper method to print this response in a formatted, green-colored manner to a specified stream or standard output.*


### print (method, L121-L127, parent: ToolResponse)

> *Summary: This method outputs a structured message to a provided stream or the standard output if none is given. It prepends and appends formatted markers around the agent's content, clearly indicating the source role and tool call ID.*


### ToolResponseMessage (class, L132-L143)

> *Summary: Represents a message containing results from executed tools. It accepts a list of `ToolResponse` objects and optional content, then prints itself and all contained tool responses to the specified output stream.*


### print (method, L137-L143, parent: ToolResponseMessage)

> *Summary: This method recursively prints the agent's message and all associated tool responses using a provided formatting function. It ensures that after printing each tool response, a separator line is outputted to maintain visual separation in the console.*


### FunctionCall (class, L146-L164)

> *Summary: Represents a suggested function call containing a name and arguments. It prints this structured information to the provided output stream or standard print if none is given, highlighting the suggestion in green.*


### print (method, L150-L164, parent: FunctionCall)

> *Summary: This method formats and outputs a suggested function call to a provided callable stream. It constructs a formatted string including the function's name and arguments, then prints these components using colorized output.*


### FunctionCallMessage (class, L169-L182)

> *Summary: Represents a message containing both content and a function call request. It prints the provided content followed by the details of the requested function call to the specified output stream.*


### print (method, L173-L182, parent: FunctionCallMessage)

> *Summary: This method outputs the agent's content and any associated function call to a provided callable or standard output stream. It ensures both the message content and the function call details are printed sequentially before drawing a separator line.*


### ToolCall (class, L185-L206)

> *Summary: Represents a suggested tool invocation containing an ID, the function to call, and its arguments. It provides a `print` method to format and output this structured tool call information to a specified stream or the console.*


### print (method, L190-L206, parent: ToolCall)

> *Summary: This method formats and outputs a suggested tool call to a provided callable stream. It constructs a detailed string including the agent ID, function name, and arguments before printing it in green color.*


### ToolCallMessage (class, L211-L229)

> *Summary: Represents a message containing instructions for an external tool execution. It holds the function call details and a list of specific `ToolCall` objects to be processed by a provided printing function.*


### print (method, L219-L229, parent: ToolCallMessage)

> *Summary: This method outputs the message's content and any associated tool calls to a specified callable function. It ensures proper formatting by printing a separator line after all contents are displayed.*


### TextMessage (class, L234-L267)

> *Summary: Represents a message containing various data types, including text and structured content that may hold image references. It validates the `content` field before serialization, replacing PIL Image objects with placeholders if available, and prints the content to a provided function or standard output.*


### _replace_pil_image_with_placeholder (method, L239-L241, parent: TextMessage)

> *Summary: Replaces a PIL `Image` object within an input dictionary with the string placeholder `"<image>"` if a URL key exists. This modifies the provided image data structure in place.*


### validate_and_encode_content (method, L245-L258, parent: TextMessage)

> *Summary: If PIL is available, this method iterates through a list of message contents to replace image URLs specified as dictionaries with placeholders. It returns the modified content structure if it's a list, otherwise returning the input unchanged.*


### print (method, L260-L267, parent: TextMessage)

> *Summary: This method outputs the message's content to a provided callable function, defaulting to standard output if none is given. It first calls its parent's print method and then writes the formatted content followed by a separator line.*


### create_received_message_model (function, L270-L314)

> *Summary: Constructs a specific message object based on the input dictionary's role and content structure. It takes an optional UUID, a message dict, and sender/recipient agent objects to return one of several typed messages (e.g., `FunctionResponseMessage`, `TextMessage`).*


### PostCarryoverProcessingMessage (class, L319-L398)

> *Summary: This message structure encapsulates chat context, including carryover data, a primary message, and metadata like sender/recipient names. It processes the `carryover` field into a readable string format and provides a method to print the entire message content with visual formatting based on verbosity settings.*


### __init__ (method, L330-L365, parent: PostCarryoverProcessingMessage)

> *Summary: Initializes an agent message by extracting core communication details like sender/recipient names, chat history (`carryover`), and the primary content (`message`) from a provided `chat_info` dictionary. It processes the input message to ensure it's represented as a string before passing all configuration parameters up to the parent class constructor.*


### _process_carryover (method, L367-L380, parent: PostCarryoverProcessingMessage)

> *Summary: This method converts the internal `carryover` attribute into a single string representation. It iterates through the list, ensuring each item is converted to a string—either directly or by extracting content from dictionaries—and joins them with newlines.*


### print (method, L382-L398, parent: PostCarryoverProcessingMessage)

> *Summary: This method outputs a formatted header indicating the start of a new chat session. It prints separator lines and displays the message content and any carryover data if verbose mode is enabled.*


### ClearAgentsHistoryMessage (class, L403-L430)

> *Summary: Represents a command to clear conversation history, accepting an optional agent name and the number of recent messages to keep. It outputs descriptive strings indicating which agent's history is being cleared and whether any messages should be preserved.*


### __init__ (method, L407-L416, parent: ClearAgentsHistoryMessage)

> *Summary: Initializes a message object by optionally accepting a UUID, an Agent instance, and a count for preserving messages. It passes the provided agent's name to the parent constructor if an agent is supplied.*


### print (method, L418-L430, parent: ClearAgentsHistoryMessage)

> *Summary: This method outputs a message indicating the agent's history is being cleared, optionally specifying how many recent messages to keep. It uses a provided callable or defaults to standard printing based on whether an agent name and preservation count are set.*


### SpeakerAttemptSuccessfulMessage (class, L436-L469)

> *Summary: Represents a successful selection of a speaker during an agent interaction process. It stores the counts of mentions, the current attempt number, remaining attempts, and optionally verbose settings, printing a success message upon invocation.*


### __init__ (method, L442-L457, parent: SpeakerAttemptSuccessfulMessage)

> *Summary: Initializes an agent message object by accepting a UUID, mention counts, current and remaining attempt numbers, and an optional verbosity flag. It stores these parameters internally after performing a deep copy of the provided mentions dictionary.*


### print (method, L459-L469, parent: SpeakerAttemptSuccessfulMessage)

> *Summary: This method displays a success message indicating which agent was chosen during an attempt. It takes an optional callable to handle the output and prints a green-colored confirmation string to standard output.*


### SpeakerAttemptFailedMultipleAgentsMessage (class, L474-L506)

> *Summary: Represents a message indicating that an attempt to select a single speaker failed because the input involved multiple agents. It stores details like which agents were mentioned, the current attempt number, and remaining attempts, and prints a prominent failure notification upon calling its `print` method.*


### __init__ (method, L480-L495, parent: SpeakerAttemptFailedMultipleAgentsMessage)

> *Summary: Initializes an agent message by accepting optional UUID, a dictionary of mentions, and counters for the current and remaining attempts. It passes these parameters to the parent class constructor while deep-copying the `mentions` dictionary.*


### print (method, L497-L506, parent: SpeakerAttemptFailedMultipleAgentsMessage)

> *Summary: This method outputs a formatted error message to the console when an agent selection attempt fails due to containing multiple agent names. It uses a provided callable or defaults to the built-in `print` function for outputting the colored failure notification.*


### SpeakerAttemptFailedNoAgentsMessage (class, L511-L543)

> *Summary: Represents a message indicating that an attempt to select a speaker failed because no agents were included in the request. It stores details like the current attempt number, remaining attempts, and mentions of involved entities, and prints a prominent failure notification upon calling its `print` method.*


### __init__ (method, L517-L532, parent: SpeakerAttemptFailedNoAgentsMessage)

> *Summary: Initializes an agent message by accepting a UUID, mention counts, current and remaining attempt numbers, and an optional verbosity flag. It stores these parameters internally after deep-copying the mentions dictionary.*


### print (method, L534-L543, parent: SpeakerAttemptFailedNoAgentsMessage)

> *Summary: This method outputs a formatted error message to the console indicating that a speaker selection attempt failed because no agent names were included. It uses an optional callable `f` to direct the output, which is otherwise defaulted to the standard `print`.*


### GroupChatResumeMessage (class, L548-L570)

> *Summary: Represents a state for resuming a group chat session by encapsulating the name of the last participant and a history of prior messages. It provides a `print` method to log this resumption context, indicating how many messages are present and who spoke last.*


### __init__ (method, L553-L561, parent: GroupChatResumeMessage)

> *Summary: Initializes a message object by accepting an optional UUID, the name of the last speaker, a list of LLM message types, and an optional silence flag. It passes these arguments to the parent constructor, using the `silent` flag to determine verbosity.*


### print (method, L563-L570, parent: GroupChatResumeMessage)

> *Summary: This method outputs a formatted string indicating the number of messages and the name of the last speaker in the group chat. It uses an optional callable to control where the output is directed, defaulting to standard printing.*


### GroupChatRunChatMessage (class, L575-L585)

> *Summary: Represents a message within a group chat, storing the name of the speaking agent and an optional verbosity flag. It initializes by setting the speaker's name from an Agent object and can print its content to a specified output stream with colorized formatting.*


### __init__ (method, L579-L580, parent: GroupChatRunChatMessage)

> *Summary: Initializes a message object by accepting an optional unique identifier, the sender agent, and a silence flag. It passes these values to the parent class, setting verbosity based on the `silent` parameter.*


### print (method, L582-L585, parent: GroupChatRunChatMessage)

> *Summary: This method outputs a formatted message to the console, prepending it with the current agent's name in green text. It accepts an optional callable function to handle the output stream.*


### TerminationAndHumanReplyNoInputMessage (class, L592-L617)

> *Summary: Represents a message sent when a human-in-the-loop is prompted but offers no response. It stores the prompt message, sender, and recipient names, and prints itself in red upon invocation.*


### __init__ (method, L599-L612, parent: TerminationAndHumanReplyNoInputMessage)

> *Summary: Initializes a message object by setting its unique identifier (optional), the content for when no human input is needed, and specifying the sending and receiving agents. It uses the provided agent names to populate the underlying message structure.*


### print (method, L614-L617, parent: TerminationAndHumanReplyNoInputMessage)

> *Summary: This method outputs a formatted message to the console, prepending it with a red-colored header indicating no human input was required. It uses an optional callable `f` for outputting, defaulting to the standard `print`.*


### UsingAutoReplyMessage (class, L622-L645)

> *Summary: Represents a message indicating an automated reply is active. It stores the mode of human input, sender's name, and recipient's name, and prints a distinct red header when displayed.*


### __init__ (method, L627-L640, parent: UsingAutoReplyMessage)

> *Summary: Initializes a message object by setting its UUID (optional), the mode for human interaction, and specifying the sending and receiving agents. It delegates core setup to the parent class while capturing agent names from the provided `sender` and `recipient`.*


### print (method, L642-L645, parent: UsingAutoReplyMessage)

> *Summary: This method outputs a formatted message indicating the use of an auto-reply. It accepts an optional callable function to handle the output, defaulting to the standard `print` function if none is provided.*


### TerminationMessage (class, L650-L669)

> *Summary: Represents a signal that a workflow has ended, carrying a specific `termination_reason`. It outputs a prominently colored message indicating the run's termination reason and UUID when printed.*


### __init__ (method, L655-L664, parent: TerminationMessage)

> *Summary: Initializes a message object by accepting an optional unique identifier and a required string detailing the termination reason. It passes these values up to the parent class constructor for state management.*


### print (method, L666-L669, parent: TerminationMessage)

> *Summary: This method outputs a formatted termination message to the console, including the agent's UUID and reason for stopping. It uses an optional callable `f` to direct the output, defaulting to standard printing with red coloring.*


### ExecuteCodeBlockMessage (class, L674-L696)

> *Summary: Represents a message instructing an agent to execute a specific block of code. It takes the code string, programming language, block count, and recipient name as input, and its primary behavior is to print a formatted execution notification to standard output or a provided function.*


### __init__ (method, L680-L685, parent: ExecuteCodeBlockMessage)

> *Summary: Initializes a message object by accepting a unique identifier (optional), the source code string, its programming language, the number of code blocks, and a recipient agent instance. It passes these parameters up to the parent class constructor for storage.*


### print (method, L687-L696, parent: ExecuteCodeBlockMessage)

> *Summary: This method outputs a formatted message indicating the execution of a code block, including its sequential count and inferred programming language. It uses an optional callable to handle the actual printing mechanism.*


### ExecuteFunctionMessage (class, L701-L729)

> *Summary: Represents a message instructing an agent to execute a specific function with provided arguments. It carries the function name, input dictionary, and the intended recipient for execution.*


### __init__ (method, L707-L718, parent: ExecuteFunctionMessage)

> *Summary: Initializes a message object by accepting a function name, arguments dictionary, and a target agent. It stores these details along with optional UUID and call IDs for tracking communication between agents.*


### print (method, L720-L729, parent: ExecuteFunctionMessage)

> *Summary: This method logs the execution of a function by printing a formatted message to the console. It takes an optional callable for output and displays the function name, call ID, and input arguments in magenta color.*


### ExecutedFunctionMessage (class, L734-L769)

> *Summary: Represents a message indicating that a function has been executed, carrying the function's name, input arguments, and the resulting output content. It provides a `print` method to display this execution result in a formatted manner.*


### __init__ (method, L741-L758, parent: ExecutedFunctionMessage)

> *Summary: Initializes a message object by accepting a function name, arguments dictionary, content string, and a recipient agent. It stores these details along with optional UUID and call ID information for later processing.*


### print (method, L760-L769, parent: ExecutedFunctionMessage)

> *Summary: This method outputs a detailed execution log to the console, including the function name, call ID, input arguments, and final content. It uses color formatting for enhanced visibility during runtime tracing.*


### SelectSpeakerMessage (class, L774-L787)

> *Summary: This message type is used to prompt a user for speaker selection from a provided list of agents. It stores the names of available agents and provides a `print` method to display numbered options to the console or a specified file stream.*


### __init__ (method, L777-L779, parent: SelectSpeakerMessage)

> *Summary: Initializes a message object by optionally accepting a UUID and a list of `Agent` instances. It extracts the names from the provided agents to pass up to the parent class constructor.*


### print (method, L781-L787, parent: SelectSpeakerMessage)

> *Summary: Displays a prompt asking the user to select the next speaker, iterating over and printing numbered names from an internal list of agents. It uses a provided callable function for outputting the selection options.*


### SelectSpeakerTryCountExceededMessage (class, L792-L803)

> *Summary: Represents a message indicating that the maximum number of attempts to select a speaker has been reached. It stores the attempt count and the names of agents involved, printing a notification upon invocation.*


### __init__ (method, L796-L798, parent: SelectSpeakerTryCountExceededMessage)

> *Summary: Initializes a message object by accepting an optional UUID, a required retry count, and an optional list of agents. It extracts the names from the provided agents to pass along with the other initialization parameters.*


### print (method, L800-L803, parent: SelectSpeakerTryCountExceededMessage)

> *Summary: This method logs a status message indicating the number of attempts made, using either a provided callable function or the built-in `print` for output. It ensures the specified logging function is called with the formatted attempt count string.*


### SelectSpeakerInvalidInputMessage (class, L808-L818)

> *Summary: Represents an error message indicating invalid user selection for choosing a speaker. It stores the names of available agents and prints a formatted message prompting the user to select a valid index based on the list length.*


### __init__ (method, L811-L813, parent: SelectSpeakerInvalidInputMessage)

> *Summary: Initializes a message object by optionally accepting a UUID and a list of `Agent` instances. It extracts the names from the provided agents to pass up to the parent class constructor.*


### print (method, L815-L818, parent: SelectSpeakerInvalidInputMessage)

> *Summary: This method displays an error message indicating invalid input, specifically requiring a number within the range of available agent names. It uses a provided callable to handle the output, defaulting to standard printing if none is supplied.*


### ClearConversableAgentHistoryMessage (class, L826-L846)

> *Summary: This message signals an intent to clear conversation history, specifying the agent and recipient involved. It takes a count of messages to preserve and prints informative messages indicating how many messages will be kept for continuity during tool interactions.*


### __init__ (method, L831-L837, parent: ClearConversableAgentHistoryMessage)

> *Summary: Initializes a message object by accepting an optional UUID and agent instance, setting the sender and recipient to the provided agent's name while optionally controlling message retention count.*


### print (method, L839-L846, parent: ClearConversableAgentHistoryMessage)

> *Summary: This method iterates a number of times specified by `self.no_messages_preserved`, calling the provided function or the built-in `print` with a message indicating that it is preserving agent history to prevent splitting context across tool calls and responses.*


### ClearConversableAgentHistoryWarningMessage (class, L851-L869)

> *Summary: This message class signals a warning to the recipient about ignoring the `nr_preserved_messages` setting when clearing chat history for a specific agent. It prints a yellow-colored warning message indicating this behavior.*


### __init__ (method, L854-L858, parent: ClearConversableAgentHistoryWarningMessage)

> *Summary: Initializes a message object by optionally accepting a unique identifier and requiring an `Agent` instance to determine the recipient. It passes the provided UUID and the agent's name up to the parent class constructor.*


### print (method, L860-L869, parent: ClearConversableAgentHistoryWarningMessage)

> *Summary: This method outputs a yellow warning message to the console if the provided callable is not specified. It alerts the user that `nr_preserved_messages` is disregarded when clearing chat history for a specific agent.*


### GenerateCodeExecutionReplyMessage (class, L877-L918)

> *Summary: Represents a message containing code execution results, holding a list of `CodeBlock` objects and identifying the sender and recipient agents. It formats and prints a descriptive header indicating whether one or multiple code blocks are being executed based on their inferred languages.*


### __init__ (method, L882-L897, parent: GenerateCodeExecutionReplyMessage)

> *Summary: Initializes a message object by accepting optional UUID, a list of code blocks, and specified sender/recipient agents. It extracts the languages from the provided code blocks and passes necessary agent names to the parent constructor.*


### print (method, L899-L918, parent: GenerateCodeExecutionReplyMessage)

> *Summary: This method outputs a header message indicating the execution of one or multiple code blocks. It takes an optional callable function as input and formats the output string to list the inferred languages present in `self.code_block_languages`.*


### ConversableAgentUsageSummaryNoCostIncurredMessage (class, L923-L932)

> *Summary: Represents a message indicating that no usage costs were incurred by an agent. It stores the recipient's name and prints a confirmation message upon invocation.*


### __init__ (method, L926-L927, parent: ConversableAgentUsageSummaryNoCostIncurredMessage)

> *Summary: Initializes a message object by optionally accepting a unique identifier and requiring an `Agent` instance to determine the intended recipient. It passes the provided UUID and the agent's name up to the parent class constructor.*


### print (method, L929-L932, parent: ConversableAgentUsageSummaryNoCostIncurredMessage)

> *Summary: This method logs a message indicating no cost was incurred by the agent to its recipient. It accepts an optional callable function to direct the output, defaulting to the standard `print`.*


### ConversableAgentUsageSummaryMessage (class, L937-L946)

> *Summary: This message structure encapsulates a summary of an agent's usage, storing the recipient's name. It provides a simple method to print this summary to a specified output stream.*


### __init__ (method, L940-L941, parent: ConversableAgentUsageSummaryMessage)

> *Summary: Initializes a message object by optionally accepting a unique identifier and requiring an `Agent` instance to determine the intended recipient. It passes the provided UUID and the agent's name up to the parent class constructor.*


### print (method, L943-L946, parent: ConversableAgentUsageSummaryMessage)

> *Summary: This method outputs a formatted string indicating the recipient's name to a provided callable function, defaulting to standard output if none is supplied. It prepends "Agent '..." to the message before calling the target function with the constructed string.*

