# autogen/agentchat/contrib/nlip_agent.py

4 function(s): request_message_to_nlip, request_message_from_nlip, response_message_to_nlip, response_message_from_nlip. 7 class(es): NlipClientError, NlipConnectionError, NlipTimeoutError, NlipAgentNotFoundError, AG2NlipSession, AG2NlipApplication, NlipRemoteAgent. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| NlipClientError | class |  |
| NlipConnectionError | class |  |
| NlipTimeoutError | class |  |
| NlipAgentNotFoundError | class |  |
| request_message_to_nlip | function |  |
| request_message_from_nlip | function |  |
| response_message_to_nlip | function |  |
| response_message_from_nlip | function |  |
| AG2NlipSession | class |  |
| AG2NlipApplication | class |  |
| NlipRemoteAgent | class |  |

## Chunks

### NlipClientError (class, L30-L33)

> *Summary: This class serves as the base exception specifically for errors encountered when interacting with an NLIP client. It inherits from `RemoteAgentError` to signal issues during remote agent communication.*


### NlipConnectionError (class, L36-L39)

> *Summary: This custom exception signals a failure in establishing or maintaining a connection with the NLIP server. It inherits from `NlipClientError` and is raised specifically when connectivity issues occur.*


### NlipTimeoutError (class, L42-L45)

> *Summary: This custom exception signals that a Natural Language Interface Protocol (NLIP) request failed due to exceeding the allotted time limit. It inherits from `NlipClientError` and is raised specifically upon timeout during an NLIP interaction.*


### NlipAgentNotFoundError (class, L48-L51)

> *Summary: This exception signals that a requested NLIP agent could not be located at the provided endpoint. It inherits from both `NlipClientError` and `RemoteAgentNotFoundError`.*


### request_message_to_nlip (function, L55-L114)

> *Summary: Transforms an internal `RequestMessage` into a stateless `NLIP_Message` suitable for remote agents. It extracts the last user-directed text as the primary content and attaches the full chat history, context, and client tools as labeled JSON submessages.*


### request_message_from_nlip (function, L118-L160)

> *Summary: Transforms an incoming `NLIP_Message` into a standardized `RequestMessage`, prioritizing structured data from submessages like `ag2_chat_history`. If no structured messages are present, it defaults to treating the entire message content as a single user query.*


### response_message_to_nlip (function, L164-L200)

> *Summary: Transforms an `ResponseMessage` into a standardized `NLIP_Message`, prioritizing the content of the last assistant message for plain text output. It optionally includes context data and appends an `INPUT_REQUIRED` error sub-message if the original response indicates human input is needed.*


### response_message_from_nlip (function, L204-L236)

> *Summary: Parses a received `NLIP_Message` from a server into a structured response. It extracts the main text as the assistant's reply and checks submessages for an `ag2_context` dictionary or an "INPUT\_REQUIRED" error flag to populate the output `ResponseMessage`.*


### AG2NlipSession (class, L240-L309)

> *Summary: This class wraps a `ConversableAgent` to handle communication via the NLIP protocol. It takes an incoming `NLIP_Message`, converts it into a request, executes the agent through an `AgentService`, and returns the resulting response as an `NLIP_Message`. The execution flow handles intermediate input requests from the agent during processing.*


### __init__ (method, L243-L246, parent: AG2NlipSession)

> *Summary: Initializes the class by storing a reference to an existing `ConversableAgent` and creating an associated `AgentService` instance from it. This sets up the necessary components for interaction with the provided agent.*


### start (method, L248-L251, parent: AG2NlipSession)

> *Summary: Initializes the agent's session, logging a message indicating that the NLIP session has begun for the associated agent. This method calls the parent class's start method before logging its own initialization status.*


### execute (method, L253-L300, parent: AG2NlipSession)

> *Summary: Takes an incoming `NLIP_Message` and processes it by converting it to a request for the underlying agent service. It yields back an input-required message if the agent needs user input, otherwise, it returns the final response wrapped in an `NLIP_Message`.*


### correlated_execute (method, L302-L304, parent: AG2NlipSession)

> *Summary: This method forwards an incoming `NLIP_Message` to the parent class's execution logic and then returns a dictionary representation of the resulting message, excluding any fields with null values.*


### stop (method, L306-L309, parent: AG2NlipSession)

> *Summary: This method handles the graceful shutdown of an NLIP session by logging a stopping message and calling the parent class's stop mechanism to clean up resources. It takes no inputs and performs asynchronous cleanup operations.*


### AG2NlipApplication (class, L313-L363)

> *Summary: This class wraps an `autogen.ConversableAgent` to function as both an NLIP server application and an ASGI callable. It initializes a FastAPI backend eagerly upon instantiation, allowing it to be directly served by ASGI servers like Uvicorn while providing methods for session creation and lifecycle management.*


### __init__ (method, L336-L339, parent: AG2NlipApplication)

> *Summary: Initializes the class by storing a reference to an existing `ConversableAgent` and setting up an ASGI application server instance for it.*


### asgi_app (method, L342-L343, parent: AG2NlipApplication)

> *Summary: Returns the underlying ASGI application instance from the agent object, allowing it to be used directly in an ASGI server.*


### __call__ (method, L345-L347, parent: AG2NlipApplication)

> *Summary: This method serves as an ASGI entry point, delegating incoming requests to the underlying FastAPI application instance. It accepts standard ASGI scope, receive, and send objects to process asynchronous communication.*


### startup (method, L349-L351, parent: AG2NlipApplication)

> *Summary: Logs an informational message indicating the start of the NLIP application, specifying the name of the associated agent. This method executes upon application initialization.*


### shutdown (method, L353-L355, parent: AG2NlipApplication)

> *Summary: This method serves as an application shutdown hook, logging a message indicating the termination of the NLIP application associated with the agent's name. It performs no complex operations but signals the graceful exit process.*


### create_session (method, L357-L363, parent: AG2NlipApplication)

> *Summary: Instantiates and returns a new `AG2NlipSession` object, using the agent's context to establish a fresh session for each incoming request.*


### NlipRemoteAgent (class, L367-L539)

> *Summary: This class acts as a remote client to connect an agent within AG2 workflows to an external NLIP endpoint. It takes a server URL and name upon initialization, then uses asynchronous HTTP requests with built-in retry logic to send messages and receive replies from the remote service. The primary method handles message exchange, including prompting the user for input if the remote service requires it.*


### __init__ (method, L378-L412, parent: NlipRemoteAgent)

> *Summary: Sets up a remote agent by configuring its connection URL and retry limits. It then overrides the standard reply generation methods to route responses through a remote NLIP server instead of local OpenAI calls.*


### generate_remote_reply (method, L414-L429, parent: NlipRemoteAgent)

> *Summary: This method explicitly prevents synchronous remote reply generation by always raising a `NotImplementedError`. It requires message history, a sender agent, and an OpenAI configuration but offers no functional output due to its design constraint.*


### a_generate_remote_reply (method, L431-L525, parent: NlipRemoteAgent)

> *Summary: This method sends a request containing conversation history and context to a remote NLIP endpoint via HTTP. It handles potential network errors, iteratively prompts the user for required input if necessary, updates shared context variables upon success, and returns a boolean indicating finality along with the generated reply content.*


### update_tool_signature (method, L527-L539, parent: NlipRemoteAgent)

> *Summary: Modifies the agent's LLM configuration by updating or removing a specific tool signature. It accepts the tool signature (as a string or dictionary), a boolean indicating removal, and an optional flag to suppress overrides.*

