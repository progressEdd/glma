# test/test_logging.py

12 function(s): dummy_function, db_connection, get_sample_chat_completion, test_log_completion, test_log_function_use, test_log_new_agent, test_log_oai_wrapper, test_log_oai_client, test_to_dict, test_logging_exception_will_not_crash_only_print_error and 2 more. 1 class(es): _RecordingHandler. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| dummy_function | function |  |
| db_connection | function |  |
| get_sample_chat_completion | function |  |
| test_log_completion | function |  |
| test_log_function_use | function |  |
| test_log_new_agent | function |  |
| test_log_oai_wrapper | function |  |
| test_log_oai_client | function |  |
| test_to_dict | function |  |
| test_logging_exception_will_not_crash_only_print_error | function |  |
| _RecordingHandler | class |  |
| test_event_print_with_custom_logger_and_handler | function |  |
| test_event_print_default_logger_respects_end_and_flush | function |  |

## Chunks

### dummy_function (function, L83-L84)

> *Summary: This function takes a string and an integer as input and returns the string repeated by the value of the integer. It serves as a simple test utility for logging purposes.*


### db_connection (function, L91-L97)

> *Summary: This generator establishes and yields a database connection configured for an in-memory SQLite database, ensuring logging is started before use and stopped afterward. It also configures the connection to return rows as dictionary-like objects using `sqlite3.Row`.*


### get_sample_chat_completion (function, L100-L111)

> *Summary: Constructs a standardized log entry dictionary using a provided response object and predefined constants. It populates the structure with unique identifiers, request details, cost metrics, and an initialized test agent instance.*


### test_log_completion (function, L122-L142)

> *Summary: This test verifies that a chat completion is correctly logged to the database after being processed. It takes a response, expected log data, and a DB connection as input, asserting that the recorded `chat_completions` row matches all details from the sample completion and the expected output.*


### test_log_function_use (function, L145-L163)

> *Summary: This test verifies that calling `log_function_use` correctly records the agent, function details, arguments, and return status into a database table. It asserts that the retrieved rows match the input parameters provided to the logging function.*


### test_log_new_agent (function, L167-L189)

> *Summary: This test verifies that a newly created `AssistantAgent` is correctly logged into the database. It asserts that the stored record contains the correct agent name, class type, and serialized initialization arguments (`init_args`).*


### test_log_oai_wrapper (function, L193-L216)

> *Summary: This test verifies that an `OpenAIWrapper` instance, when logged via `autogen.runtime_logging`, correctly persists its configuration to a database. It asserts that the stored data contains expected structure (like `config_list` and `base_config`) while ensuring sensitive information like the API key is omitted from the saved arguments.*


### test_log_oai_client (function, L220-L244)

> *Summary: This test verifies that the logging mechanism correctly saves configuration for an `AzureOpenAI` client to a database. It asserts that retrieved records contain valid UUIDs, specify the correct class type, and store initialization arguments while omitting sensitive data like the API key.*


### test_to_dict (function, L247-L312)

> *Summary: This test verifies a serialization utility by converting an instance of `Bar` into a dictionary, excluding specified keys and recursively handling agents. It asserts that the resulting structure correctly maps object attributes while transforming complex types like functions and paths according to predefined expectations.*


### test_logging_exception_will_not_crash_only_print_error (function, L316-L324)

> *Summary: This test verifies that logging an exception during chat completion does not crash the application. It calls a logging function with sample data and asserts that the mock logger was called with an error message starting with a specific SQLite prefix.*


### _RecordingHandler (class, L327-L333)

> *Summary: This handler intercepts log records and stores them internally in a list. It accepts any `logging.LogRecord` via its `emit` method and appends it to the internal collection.*


### __init__ (method, L328-L330, parent: _RecordingHandler)

> *Summary: Initializes the object by calling the parent constructor and setting up an empty list named `records` to store `logging.LogRecord` objects. This structure is used internally for capturing log events during testing.*


### emit (method, L332-L333, parent: _RecordingHandler)

> *Summary: This method appends an incoming `logging.LogRecord` object to the internal list of records maintained by the logger instance. It serves as a basic mechanism for capturing log events.*


### test_event_print_with_custom_logger_and_handler (function, L336-L349)

> *Summary: This test verifies that `event_print` correctly logs a message using a custom handler and logger configuration. It asserts that the handler captures exactly one record containing the expected formatted string, level, and specific flags passed to the function call.*


### test_event_print_default_logger_respects_end_and_flush (function, L352-L374)

> *Summary: This test verifies that the `event_print` function correctly outputs data to a stream when explicitly setting `end="END"` and `flush=True`. It temporarily configures a logger with a custom handler writing to an in-memory buffer to assert the exact string output.*

