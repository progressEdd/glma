# test/agentchat/test_agent_file_logging.py

9 function(s): dummy_function, logger, test_start, test_log_chat_completion, test_log_function_use, test_log_new_agent, test_log_event, test_log_new_wrapper, test_log_new_client. 1 class(es): TestWrapper. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| dummy_function | function |  |
| logger | function |  |
| test_start | function |  |
| test_log_chat_completion | function |  |
| test_log_function_use | function |  |
| TestWrapper | class |  |
| test_log_new_agent | function |  |
| test_log_event | function |  |
| test_log_new_wrapper | function |  |
| test_log_new_client | function |  |

## Chunks

### dummy_function (function, L23-L24)

> *Summary: This function takes a string and an integer as input and returns the string repeated by the value of the integer. It serves as a simple test utility for logging purposes.*


### logger (function, L28-L36)

> *Summary: This generator yields a `FileLogger` instance configured to write logs to a temporary file within the current directory. It ensures proper cleanup by stopping and deleting the temporary directory after yielding the logger.*


### test_start (function, L40-L43)

> *Summary: This test verifies that calling the `start()` method on a `FileLogger` instance returns a string session ID of exactly 36 characters. It ensures the logger successfully initializes a new logging session.*


### test_log_chat_completion (function, L47-L82)

> *Summary: This test verifies that a `FileLogger` correctly records chat completion details by calling its logging method with various inputs like IDs, request/response data, and timing. It then asserts that the resulting log file contains exactly one JSON entry matching all provided parameters.*


### test_log_function_use (function, L86-L101)

> *Summary: This test verifies that the logger correctly records function usage by writing a JSON entry to its log file. It passes an agent, a callable function, input arguments, and a return status to `log_function_use` and then asserts the resulting log file contains one entry with matching details.*


### TestWrapper (class, L104-L106)

> *Summary: This class initializes itself by accepting a dictionary of arguments (`init_args`) to store for later use during testing. It serves as a wrapper structure for test setup.*


### __init__ (method, L105-L106, parent: TestWrapper)

> *Summary: Initializes the object by storing a provided dictionary of configuration arguments. This sets up the necessary parameters for subsequent operations within the class instance.*


### test_log_new_agent (function, L110-L117)

> *Summary: This test verifies that a new agent, instantiated as `UserProxyAgent`, is correctly logged by writing its name to the logger's file. It asserts that the first line of the log file contains a JSON object confirming the registered agent's name matches the input.*


### test_log_event (function, L121-L133)

> *Summary: This test verifies that an event is correctly recorded by a `FileLogger`. It calls the logger with an agent, event name, and keyword arguments, then asserts that the resulting log file contains the expected source name, event name, and serialized state data.*


### test_log_new_wrapper (function, L137-L146)

> *Summary: This test verifies that a logger correctly records the initialization arguments and unique ID of a wrapper object. It asserts that the logged JSON data contains the correct `wrapper_id` (based on object identity), serialized initial state, and an integer thread ID.*


### test_log_new_client (function, L150-L162)

> *Summary: This test verifies that a logger correctly records details when a new client is registered. It passes an `UserProxyAgent`, a `TestWrapper`, and initialization arguments to the logging method, then asserts that the resulting log file contains the correct IDs for the client and wrapper, along with the serialized initial state.*

