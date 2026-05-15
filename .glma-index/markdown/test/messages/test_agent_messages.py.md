# test/messages/test_agent_messages.py

3 function(s): enable_color_in_tests, sender, recipient. 26 class(es): TestToolResponseMessage, TestFunctionResponseMessage, TestFunctionCallMessage, TestToolCallMessage, TestTextMessage, TestPostCarryoverProcessingMessage, TestClearAgentsHistoryMessage, TestSpeakerAttemptSuccessfulMessage, TestSpeakerAttemptFailedMultipleAgentsMessage, TestSpeakerAttemptFailedNoAgentsMessage, TestGroupChatResumeMessage, TestGroupChatRunChatMessage, TestTerminationAndHumanReplyMessage, TestTerminationMessage, TestUsingAutoReplyMessage, TestExecuteCodeBlockMessage, TestExecuteFunctionMessage, TestExecutedFunctionMessage, TestSelectSpeakerMessage, TestSelectSpeakerTryCountExceededMessage, TestSelectSpeakerInvalidInputMessage, TestClearConversableAgentHistoryMessage, TestClearConversableAgentHistoryWarningMessage, TestGenerateCodeExecutionReplyMessage, TestConversableAgentUsageSummaryNoCostIncurredMessage, TestConversableAgentUsageSummaryMessage. 26 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| enable_color_in_tests | function |  |
| sender | function |  |
| recipient | function |  |
| TestToolResponseMessage | class |  |
| TestFunctionResponseMessage | class |  |
| TestFunctionCallMessage | class |  |
| TestToolCallMessage | class |  |
| TestTextMessage | class |  |
| TestPostCarryoverProcessingMessage | class |  |
| TestClearAgentsHistoryMessage | class |  |
| TestSpeakerAttemptSuccessfulMessage | class |  |
| TestSpeakerAttemptFailedMultipleAgentsMessage | class |  |
| TestSpeakerAttemptFailedNoAgentsMessage | class |  |
| TestGroupChatResumeMessage | class |  |
| TestGroupChatRunChatMessage | class |  |
| TestTerminationAndHumanReplyMessage | class |  |
| TestTerminationMessage | class |  |
| TestUsingAutoReplyMessage | class |  |
| TestExecuteCodeBlockMessage | class |  |
| TestExecuteFunctionMessage | class |  |
| TestExecutedFunctionMessage | class |  |
| TestSelectSpeakerMessage | class |  |
| TestSelectSpeakerTryCountExceededMessage | class |  |
| TestSelectSpeakerInvalidInputMessage | class |  |
| TestClearConversableAgentHistoryMessage | class |  |
| TestClearConversableAgentHistoryWarningMessage | class |  |
| TestGenerateCodeExecutionReplyMessage | class |  |
| TestConversableAgentUsageSummaryNoCostIncurredMessage | class |  |
| TestConversableAgentUsageSummaryMessage | class |  |

## Chunks

### enable_color_in_tests (function, L72-L76)

> *Summary: This function patches the `termcolor` module to force color support during tests by overriding the `_can_do_colour` method to always return `True`. It accepts a `pytest.MonkeyPatch` object to perform this modification on the testing environment.*


### sender (function, L80-L81)

> *Summary: Creates and returns a `ConversableAgent` instance configured to never accept human input. This agent is initialized with the name "sender" and has no automatic replies enabled.*


### recipient (function, L85-L86)

> *Summary: Creates and returns a `ConversableAgent` instance configured to never accept automatic replies. This agent is initialized with the name "recipient" and disabled LLM configuration.*


### TestToolResponseMessage (class, L89-L100)

> *Summary: This method constructs a `ToolResponseEvent` by creating a specific dictionary structure containing multiple tool responses and associated content. It validates that the resulting object is an instance of `ToolResponseEvent`.*


### test_print (method, L90-L100, parent: TestToolResponseMessage)

> *Summary: This test constructs a specific `ToolResponseEvent` by creating a dictionary containing tool responses and content. It then asserts that the resulting object is an instance of `ToolResponseEvent`.*


### TestFunctionResponseMessage (class, L103-L107)

> *Summary: This test verifies the creation of a `FunctionResponseEvent` by simulating an incoming function response. It constructs a dictionary representing the function call result and asserts that the resulting model is correctly typed as `FunctionResponseEvent`.*


### test_deprecated (method, L104-L107, parent: TestFunctionResponseMessage)

> *Summary: This test verifies the creation of a `FunctionResponseEvent` by simulating an incoming function response. It takes a UUID, two agents, and a dictionary representing the message content to construct and assert the resulting event type.*


### TestFunctionCallMessage (class, L110-L119)

> *Summary: This test verifies the creation of a `FunctionCallEvent` by constructing a dictionary representing a function call message. It takes a UUID and two agents as input to assert that the resulting message object is correctly typed.*


### test_deprecated (method, L111-L119, parent: TestFunctionCallMessage)

> *Summary: This test verifies the creation of a `FunctionCallEvent` by constructing a received message model. It takes a UUID, two agents, and a dictionary containing content and a function call request as input to assert the resulting object type.*


### TestToolCallMessage (class, L122-L145)

> *Summary: This test verifies the creation of a `ToolCallEvent` by constructing a specific message structure containing multiple tool calls. It asserts that the resulting object correctly inherits from `ToolCallEvent`.*


### test_deprecated (method, L123-L145, parent: TestToolCallMessage)

> *Summary: This test verifies that a specific dictionary structure, containing predefined tool calls, correctly instantiates as a `ToolCallEvent` when passed to the message creation utility. It uses provided UUIDs and agent objects as inputs to assert the resulting object type.*


### TestTextMessage (class, L148-L159)

> *Summary: This test verifies the creation of a `TextEvent` by simulating an incoming text message. It constructs a message dictionary containing dynamic content based on context and asserts that the resulting object is an instance of `TextEvent`.*


### test_deprecated (method, L149-L159, parent: TestTextMessage)

> *Summary: This test verifies the creation of a received message model using specific inputs. It asserts that the resulting object is an instance of `TextEvent` after constructing it with a predefined message structure and agent participants.*


### TestPostCarryoverProcessingMessage (class, L162-L175)

> *Summary: This test verifies that instantiating a `PostCarryoverProcessingMessage` with specific chat data results in an object of type `PostCarryoverProcessingEvent`. It uses provided UUIDs and agent objects as inputs to confirm the correct event type is produced.*


### test_deprecated (method, L163-L175, parent: TestPostCarryoverProcessingMessage)

> *Summary: This test verifies that creating a `PostCarryoverProcessingMessage` instance with specific chat details results in an object of type `PostCarryoverProcessingEvent`. It uses provided UUIDs and agent objects as inputs to assert the correct event type is produced.*


### TestClearAgentsHistoryMessage (class, L178-L181)

> *Summary: This test verifies that an instance created with a `UUID` and default values for other parameters correctly inherits from `ClearAgentsHistoryEvent`. It confirms the message object is instantiated as expected.*


### test_deprecated (method, L179-L181, parent: TestClearAgentsHistoryMessage)

> *Summary: Verifies that an instance created with `ClearAgentsHistoryMessage` parameters is correctly recognized as a `ClearAgentsHistoryEvent`. It takes a UUID as input and asserts the resulting object's type.*


### TestSpeakerAttemptSuccessfulMessage (class, L184-L198)

> *Summary: This test verifies that an instance created with specific parameters for a successful speaker attempt correctly inherits from `SpeakerAttemptSuccessfulEvent`. It constructs the message using predefined values for UUID, mentions, and attempt counts.*


### test_deprecated (method, L185-L198, parent: TestSpeakerAttemptSuccessfulMessage)

> *Summary: This test verifies that an instance of `SpeakerAttemptSuccessfulMessage` correctly inherits from `SpeakerAttemptSuccessfulEvent`. It constructs the message with specific initial values for attempt count, remaining attempts, verbosity, and mentions.*


### TestSpeakerAttemptFailedMultipleAgentsMessage (class, L201-L215)

> *Summary: This test verifies the instantiation of a `SpeakerAttemptFailedMultipleAgentsMessage` by creating an instance with specific parameters like agent mentions and attempt counts. It asserts that the resulting object is correctly typed as a `SpeakerAttemptFailedMultipleAgentsEvent`.*


### test_deprecated (method, L202-L215, parent: TestSpeakerAttemptFailedMultipleAgentsMessage)

> *Summary: This test verifies that an instance of `SpeakerAttemptFailedMultipleAgentsMessage` correctly inherits from `SpeakerAttemptFailedMultipleAgentsEvent`. It constructs the message using predefined values for UUID, mentions, attempt count, remaining attempts, and verbosity.*


### TestSpeakerAttemptFailedNoAgentsMessage (class, L218-L232)

> *Summary: This test verifies that an instance created with specific parameters for speaker attempt failure correctly inherits from the `SpeakerAttemptFailedNoAgentsEvent` type. It initializes and asserts the type of a message object using predefined values for UUID, mentions, attempts, and verbosity settings.*


### test_deprecated (method, L219-L232, parent: TestSpeakerAttemptFailedNoAgentsMessage)

> *Summary: This test verifies that an instance of `SpeakerAttemptFailedNoAgentsMessage` correctly inherits from `SpeakerAttemptFailedNoAgentsEvent`. It constructs the message with predefined values for UUID, mentions, attempt count, remaining attempts, and verbosity.*


### TestGroupChatResumeMessage (class, L235-L247)

> *Summary: This test verifies that an instance created with specific group chat resumption parameters correctly inherits from `GroupChatResumeEvent`. It uses a provided UUID and initial message history to construct the object for assertion.*


### test_deprecated (method, L236-L247, parent: TestGroupChatResumeMessage)

> *Summary: This test verifies that constructing a `GroupChatResumeMessage` object results in an instance of `GroupChatResumeEvent`. It initializes the message with predefined system and assistant role content, a specific UUID, and sets silent status to false.*


### TestGroupChatRunChatMessage (class, L250-L258)

> *Summary: This test verifies that an instance created with `GroupChatRunChatMessage` correctly inherits from `GroupChatRunChatEvent`. It initializes a conversational agent and constructs the message object using a provided UUID.*


### test_deprecated (method, L251-L258, parent: TestGroupChatRunChatMessage)

> *Summary: This test verifies that an instance of `GroupChatRunChatMessage`, constructed with a provided UUID and agent, correctly inherits from `GroupChatRunChatEvent`. It asserts the type correctness of the created message object.*


### TestTerminationAndHumanReplyMessage (class, L261-L271)

> *Summary: This test verifies that an instance created with a specific "NO HUMAN INPUT RECEIVED" message correctly instantiates as a `TerminationAndHumanReplyNoInputEvent`. It takes a UUID, two agents (sender and recipient), and asserts the resulting object type.*


### test_deprecated (method, L262-L271, parent: TestTerminationAndHumanReplyMessage)

> *Summary: This test verifies that an instance of `TerminationAndHumanReplyNoInputMessage` correctly instantiates as a `TerminationAndHumanReplyNoInputEvent`. It uses provided UUIDs and agent objects to construct and assert the type of the resulting message event.*


### TestTerminationMessage (class, L274-L282)

> *Summary: This test verifies that an instance created using a specific termination reason and UUID correctly inherits from `TerminationEvent`. It confirms the structure of a message signaling the end of a conversation.*


### test_deprecated (method, L275-L282, parent: TestTerminationMessage)

> *Summary: This test verifies that an instance of `TerminationMessage`, created with a specific UUID and termination reason, correctly inherits from the `TerminationEvent` base class. It confirms the structure and type correctness of the generated message object.*


### TestUsingAutoReplyMessage (class, L285-L295)

> *Summary: This test verifies that instantiating a `UsingAutoReplyMessage` with specific parameters results in an object of type `UsingAutoReplyEvent`. It uses provided UUIDs and agent objects as inputs to confirm the correct event type is produced.*


### test_deprecated (method, L286-L295, parent: TestUsingAutoReplyMessage)

> *Summary: This test verifies that an instance created with `UsingAutoReplyMessage` correctly inherits from `UsingAutoReplyEvent`. It takes a UUID and two agents as input to construct and assert the type of the resulting message object.*


### TestExecuteCodeBlockMessage (class, L298-L307)

> *Summary: This test verifies that an instance created from a `TestExecuteCodeBlockMessage` correctly produces an `ExecuteCodeBlockEvent`. It constructs the event using hardcoded Python code and zero code block count for validation.*


### test_deprecated (method, L299-L307, parent: TestExecuteCodeBlockMessage)

> *Summary: This test verifies that an `ExecuteCodeBlockMessage` object correctly transforms into an `ExecuteCodeBlockEvent`. It takes a UUID, sender agent, and recipient agent as input to assert the resulting event type.*


### TestExecuteFunctionMessage (class, L310-L319)

> *Summary: This test verifies that constructing an `ExecuteFunctionMessage` results in an object of type `ExecuteFunctionEvent`. It simulates sending a message to execute the function "add\_num" with specific arguments.*


### test_deprecated (method, L311-L319, parent: TestExecuteFunctionMessage)

> *Summary: This test verifies that an `ExecuteFunctionMessage` object correctly transforms into an `ExecuteFunctionEvent`. It constructs the message with specific inputs like a UUID, function name, and arguments before asserting the resulting type.*


### TestExecutedFunctionMessage (class, L322-L332)

> *Summary: This test verifies that an instance of `ExecutedFunctionMessage` correctly inherits from `ExecutedFunctionEvent`. It constructs a message with predefined function execution details and asserts its type.*


### test_deprecated (method, L323-L332, parent: TestExecutedFunctionMessage)

> *Summary: This test verifies that an `ExecutedFunctionMessage` object correctly instantiates as an `ExecutedFunctionEvent`. It constructs the message using predefined inputs like a UUID, function name, arguments, and content to assert the resulting type.*


### TestSelectSpeakerMessage (class, L335-L343)

> *Summary: This test verifies that an instance created using `SelectSpeakerMessage` correctly inherits from `SelectSpeakerEvent`. It initializes the message with a provided UUID and a list of two predefined conversational agents.*


### test_deprecated (method, L336-L343, parent: TestSelectSpeakerMessage)

> *Summary: This test verifies that creating a `SelectSpeakerMessage` instance with provided agents results in an object of type `SelectSpeakerEvent`. It uses two pre-configured `ConversableAgent` instances as input to construct and assert the resulting message type.*


### TestSelectSpeakerTryCountExceededMessage (class, L346-L355)

> *Summary: This test verifies that an instance of `TestSelectSpeakerTryCountExceededMessage` correctly inherits from `SelectSpeakerTryCountExceededEvent`. It initializes the message with a specific UUID, a try count of 3, and two predefined conversational agents.*


### test_deprecated (method, L347-L355, parent: TestSelectSpeakerTryCountExceededMessage)

> *Summary: This test verifies that creating a `SelectSpeakerTryCountExceededMessage` instance correctly results in an object of type `SelectSpeakerTryCountExceededEvent`. It initializes two agents and passes them along with a specified try count to the message constructor.*


### TestSelectSpeakerInvalidInputMessage (class, L358-L366)

> *Summary: This test verifies that an instance created with `SelectSpeakerInvalidInputMessage` correctly inherits from `SelectSpeakerInvalidInputEvent`. It initializes the message using a provided UUID and a list of two predefined conversational agents.*


### test_deprecated (method, L359-L366, parent: TestSelectSpeakerInvalidInputMessage)

> *Summary: This test verifies that creating a `SelectSpeakerInvalidInputMessage` with provided agents results in an instance of `SelectSpeakerInvalidInputEvent`. It uses two pre-configured `ConversableAgent` instances as input to the message construction.*


### TestClearConversableAgentHistoryMessage (class, L369-L376)

> *Summary: This test verifies that an instance created with `ClearConversableAgentHistoryMessage` correctly inherits from `ClearConversableAgentHistoryEvent`. It takes a UUID and a recipient agent as input to construct the message object.*


### test_deprecated (method, L370-L376, parent: TestClearConversableAgentHistoryMessage)

> *Summary: Verifies that an instance created with `ClearConversableAgentHistoryMessage` correctly inherits from `ClearConversableAgentHistoryEvent`. It takes a UUID and a recipient agent as input to construct and assert the type of the resulting message object.*


### TestClearConversableAgentHistoryWarningMessage (class, L379-L382)

> *Summary: This test verifies that an instance created with a `UUID` and a `ConversableAgent` correctly inherits from the `ClearConversableAgentHistoryWarningEvent`. It confirms the message object is instantiated as expected.*


### test_deprecated (method, L380-L382, parent: TestClearConversableAgentHistoryWarningMessage)

> *Summary: This test verifies that an instance of `ClearConversableAgentHistoryWarningMessage`, initialized with a UUID and agent, correctly inherits from `ClearConversableAgentHistoryWarningEvent`. It asserts the type of the created message object.*


### TestGenerateCodeExecutionReplyMessage (class, L385-L400)

> *Summary: This test verifies that an instance of `GenerateCodeExecutionReplyMessage`, when constructed with a UUID, sender, recipient, and a code block, correctly inherits from `GenerateCodeExecutionReplyEvent`. It ensures the message object is properly typed as an event.*


### test_deprecated (method, L386-L400, parent: TestGenerateCodeExecutionReplyMessage)

> *Summary: This test verifies that an instance of `GenerateCodeExecutionReplyMessage`, when constructed with specific inputs like a UUID and two agents, correctly inherits from the `GenerateCodeExecutionReplyEvent` type. It confirms the message structure by asserting its class type after instantiation.*


### TestConversableAgentUsageSummaryNoCostIncurredMessage (class, L403-L410)

> *Summary: This test verifies that an instance created with a UUID and a `ConversableAgent` correctly inherits from the `ConversableAgentUsageSummaryNoCostIncurredEvent`. It confirms the expected type relationship for this specific usage summary message.*


### test_deprecation (method, L404-L410, parent: TestConversableAgentUsageSummaryNoCostIncurredMessage)

> *Summary: This test verifies that an instance of `ConversableAgentUsageSummaryNoCostIncurredMessage` correctly inherits from `ConversableAgentUsageSummaryNoCostIncurredEvent`. It takes a UUID and a recipient agent as input to perform this type assertion.*


### TestConversableAgentUsageSummaryMessage (class, L413-L420)

> *Summary: This test verifies that an instance created using `TestConversableAgentUsageSummaryMessage` correctly inherits from `ConversableAgentUsageEvent`. It takes a UUID and a `ConversableAgent` as inputs to instantiate and assert the type of the resulting message.*


### test_deprecation (method, L414-L420, parent: TestConversableAgentUsageSummaryMessage)

> *Summary: Verifies that an instance of `ConversableAgentUsageSummaryMessage`, initialized with a UUID and agent, correctly inherits from `ConversableAgentUsageSummaryEvent`. This test confirms the expected type relationship for usage summary messages.*

