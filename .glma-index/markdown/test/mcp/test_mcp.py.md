# test/mcp/test_mcp.py

3 function(s): mock_client, session_manager, test_session_manager_initialization. 4 class(es): TestMCPClient, MockClientSession, TestSseConfig, TestMCPStdioConfig. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMCPClient | class |  |
| MockClientSession | class |  |
| mock_client | function |  |
| session_manager | function |  |
| TestSseConfig | class |  |
| TestMCPStdioConfig | class |  |
| test_session_manager_initialization | function |  |

## Chunks

### TestMCPClient (class, L35-L217)

> *Summary: This test suite verifies the functionality of an MCP client by establishing connections to a local math server via standard I/O. It tests various behaviors, including tool schema generation, resource conversion (both direct and file-saved), and end-to-end execution using an LLM agent integrated with the toolkit.*


### server_params (method, L37-L42, parent: TestMCPClient)

> *Summary: Constructs and returns a `StdioServerParameters` object configured to execute the local `math_server.py` script using `python3`. This method provides the necessary parameters for launching an external process as a standard I/O server.*


### test_mcp_issue_with_stdio_client_context_manager (method, L45-L50, parent: TestMCPClient)

> *Summary: This test verifies the behavior of an MCP client when using a standard I/O context manager. It initializes and then immediately exits both the `ClientSession` and the underlying `stdio_client` connection, asserting proper cleanup.*


### test_tools_schema (method, L53-L119, parent: TestMCPClient)

> *Summary: This test verifies that an `AssistantAgent` correctly receives a predefined set of tool schemas when initialized with a toolkit connected to a server session. It asserts that the agent's LLM configuration contains exactly three specific function definitions (`add`, `multiply`, and `echo_resource`).*


### test_convert_resource (method, L122-L139, parent: TestMCPClient)

> *Summary: This test verifies the functionality of an "echo\_resource" tool by establishing a client session with a server, initializing it, and then calling the resource tool with a specific URI. It asserts that the returned `ReadResourceResult` correctly contains the expected echoed text content for the input URI.*


### test_register_for_llm_tool (method, L143-L158, parent: TestMCPClient)

> *Summary: This test verifies that an agent successfully registers with a toolkit after establishing communication via a standard I/O client session. It confirms the registration by asserting that the number of tools on the agent matches the total number of tools available in the toolkit.*


### test_convert_resource_with_download_folder (method, L161-L188, parent: TestMCPClient)

> *Summary: This test verifies resource conversion by initializing a client session and creating a toolkit that uses a temporary download folder. It then executes an "echo\_resource" tool call, asserts the result is saved to a file, reads the content, and validates it against an expected `TextResourceContents` structure.*


### test_with_llm (method, L193-L217, parent: TestMCPClient)

> *Summary: This test simulates an interaction with a language model agent by establishing a client session against a server, creating a toolkit, and running the agent with a specific arithmetic query. It asserts that the final summarized output from the agent contains the correct answer ("6912").*


### MockClientSession (class, L220-L230)

> *Summary: This class simulates an asynchronous client session by accepting a reader and writer during initialization. It provides an async context manager that returns a fully mocked `AsyncMock` object upon entry.*


### __init__ (method, L221-L222, parent: MockClientSession)

> *Summary: Initializes an object by accepting a `reader` and a `writer` as inputs to manage communication streams. It sets up the necessary components for subsequent operations within the class instance.*


### __aenter__ (method, L224-L227, parent: MockClientSession)

> *Summary: When entering an asynchronous context, this method creates and returns a fully mocked session object with an initialized `AsyncMock` for its initialization method. This allows tests to simulate the behavior of an active session within an async block.*


### __aexit__ (method, L229-L230, parent: MockClientSession)

> *Summary: This asynchronous context manager exit method does nothing upon exiting the `async with` block. It accepts exception details (`exc_type`, `exc_val`, `exc_tb`) but passes them through without modification.*


### mock_client (function, L234-L238)

> *Summary: Creates and returns a mock object designed to simulate an asynchronous client interface. This mock is configured with `AsyncMock` implementations for both entering and exiting the context manager protocol.*


### session_manager (function, L242-L243)

> *Summary: Instantiates and returns a new `MCPClientSessionManager` object. This function serves as a factory to provide an initialized session management instance.*


### TestSseConfig (class, L246-L284)

> *Summary: Provides a fixture to instantiate an `SseConfig` object with predefined test values and includes asynchronous tests to verify the configuration's correct initialization and how it is used when creating a session via a mocked client manager. These tests ensure that the configuration parameters are correctly passed during session setup.*


### sse_config (method, L248-L255, parent: TestSseConfig)

> *Summary: Constructs and returns a configured `SseConfig` object with default settings for an SSE connection, including a specific URL, server name, and timeouts. This method provides a standardized configuration instance for testing purposes.*


### test_sse_config_creation (method, L258-L263, parent: TestSseConfig)

> *Summary: This test verifies that an `SseConfig` object is initialized with specific default values, including a fixed URL, server name, and predefined timeouts for HTTP requests and SSE reading. It asserts that the headers attribute remains unset (`None`).*


### test_create_session_mocked (method, L266-L284, parent: TestSseConfig)

> *Summary: This test verifies session creation by mocking the underlying SSE client and session manager. It asserts that `open_session` correctly initializes a connection using the provided configuration parameters and that the resulting session object is properly initialized.*


### TestMCPStdioConfig (class, L287-L335)

> *Summary: This test fixture sets up a predefined `StdioConfig` object with specific parameters like command, arguments, and environment variables. The associated tests verify the correct initialization of this configuration and confirm that opening a session using it correctly calls the underlying client with the expected server parameters.*


### stdio_config (method, L289-L299, parent: TestMCPStdioConfig)

> *Summary: This method constructs and returns a `StdioConfig` object, configuring the execution environment for an external process. It sets up parameters like the command (`python3`), arguments, working directory, and specific session timeouts.*


### test_stdio_config_creation (method, L302-L311, parent: TestMCPStdioConfig)

> *Summary: This test verifies the correct initialization of an `StdioConfig` object by asserting specific values for its properties, including command, arguments, environment variables, and session options. It confirms that the configuration accurately reflects a standard process setup using stdin/stdout communication.*


### test_create_session (method, L314-L335, parent: TestMCPStdioConfig)

> *Summary: This test verifies the session creation process by mocking dependencies and asserting that `open_session` correctly initializes a connection using provided configuration parameters. It further confirms that the resulting session object calls its initialization method exactly once.*


### test_session_manager_initialization (function, L339-L341)

> *Summary: Verifies that a newly initialized `MCPClientSessionManager` instance correctly sets up its internal state, ensuring the exit stack exists and the sessions dictionary starts empty.*

