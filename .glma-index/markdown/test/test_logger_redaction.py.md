# test/test_logger_redaction.py

18 function(s): _make_request, _dummy_fn, db_connection, file_logger, test_file_logger_chat_completion_redacts_api_key, test_sqlite_logger_event_redacts_api_key, test_sqlite_logger_function_use_redacts_api_key, test_sqlite_logger_chat_completion_redacts_api_key, test_file_logger_event_already_redacts, test_sqlite_logger_new_wrapper_already_excludes and 8 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _make_request | function |  |
| _dummy_fn | function |  |
| db_connection | function |  |
| file_logger | function |  |
| test_file_logger_chat_completion_redacts_api_key | function |  |
| test_sqlite_logger_event_redacts_api_key | function |  |
| test_sqlite_logger_function_use_redacts_api_key | function |  |
| test_sqlite_logger_chat_completion_redacts_api_key | function |  |
| test_file_logger_event_already_redacts | function |  |
| test_sqlite_logger_new_wrapper_already_excludes | function |  |
| test_file_logger_chat_completion_redacts_nested_api_key | function |  |
| test_sqlite_logger_event_redacts_nested_api_key | function |  |
| test_sqlite_logger_event_redacts_api_key_in_list | function |  |
| test_file_logger_new_agent_redacts_api_key | function |  |
| test_sqlite_logger_function_use_non_dict_args_no_crash | function |  |
| test_file_logger_function_use_non_dict_args_no_crash | function |  |
| test_redact_handles_case_variations | function |  |
| test_sqlite_logger_event_empty_kwargs_no_crash | function |  |

## Chunks

### _make_request (function, L28-L36)

> *Summary: Constructs a base API request dictionary for an LLM call, initializing it with default parameters like the model and user message. It optionally merges any provided `extra` dictionary into this base structure before returning the complete request payload.*


### _dummy_fn (function, L39-L40)

> *Summary: This helper function takes an integer input and returns that value multiplied by two. It serves as a simple, predictable operation for testing purposes.*


### db_connection (function, L49-L54)

> *Summary: Establishes an in-memory SQLite database connection, configures it to return rows as dictionary-like objects, and yields the active connection for use within a context manager before stopping logging.*


### file_logger (function, L58-L63)

> *Summary: Sets up a temporary logging environment by changing the current working directory and initializing a `FileLogger` instance configured to write to "test.log". It yields the active logger object for testing purposes, ensuring it is properly stopped afterward.*


### test_file_logger_chat_completion_redacts_api_key (function, L71-L92)

> *Summary: This test verifies that sensitive API keys are properly redacted when logging a chat completion. It calls the logger with a request containing an API key and asserts that the resulting log file content does not contain the plaintext key but instead includes a redaction marker.*


### test_sqlite_logger_event_redacts_api_key (function, L100-L117)

> *Summary: This test verifies that sensitive data like an `api_key` passed to the logging system is correctly redacted before being persisted to the SQLite database. It asserts that the retrieved JSON state from the `events` table contains the expected redaction marker instead of the original secret value.*


### test_sqlite_logger_function_use_redacts_api_key (function, L125-L153)

> *Summary: This test verifies that sensitive data like API keys passed as arguments or returned from a function are correctly redacted before being persisted to the `function_calls` table in SQLite. It asserts that the stored JSON representations of arguments and returns contain the designated redaction marker instead of the original secret key.*


### test_sqlite_logger_chat_completion_redacts_api_key (function, L161-L188)

> *Summary: This test verifies that the `sqlite_logger` correctly redacts sensitive API keys when logging a chat completion request to an SQLite database. It mocks a request containing an API key, logs it via `log_chat_completion`, and then asserts that the stored record in the database contains the redacted placeholder instead of the actual key.*


### test_file_logger_event_already_redacts (function, L196-L211)

> *Summary: This test verifies that the `log_event` method automatically redacts sensitive data like API keys when logging to a file. It logs an event containing a secret key and asserts that the key is replaced with a redaction marker in the resulting log content.*


### test_sqlite_logger_new_wrapper_already_excludes (function, L219-L236)

> *Summary: This test verifies that the `log_new_wrapper` function correctly redacts sensitive keys from configuration arguments before storing them in an SQLite database. It mocks a wrapper, passes it initialization arguments containing a sentinel API key, and asserts that the stored JSON data does not contain that secret key.*


### test_file_logger_chat_completion_redacts_nested_api_key (function, L244-L264)

> *Summary: This test verifies that an API key nested within a configuration list inside the request payload is successfully redacted when logging chat completion data. It passes a sample request containing the sensitive key to the logger and asserts that the sentinel value does not appear in the resulting log file content.*


### test_sqlite_logger_event_redacts_nested_api_key (function, L267-L278)

> *Summary: This test verifies that the logging mechanism redacts sensitive data, specifically a nested `api_key`, when an event is logged to SQLite. It asserts that the sentinel API key does not appear in the JSON state retrieved from the database after logging.*


### test_sqlite_logger_event_redacts_api_key_in_list (function, L286-L297)

> *Summary: This test verifies that an API key provided within a list of dictionaries during event logging is successfully redacted before being stored in the SQLite database. It logs an event containing the sensitive key and asserts that the sentinel value does not appear in the retrieved JSON state from the `events` table.*


### test_file_logger_new_agent_redacts_api_key (function, L305-L315)

> *Summary: This test verifies that the logger redacts sensitive API keys when logging a new agent's initialization arguments. It passes an agent mock and configuration containing a sentinel key to `file_logger.log_new_agent` and asserts the key is absent from the resulting log file content.*


### test_sqlite_logger_function_use_non_dict_args_no_crash (function, L323-L335)

> *Summary: This test verifies that the logging mechanism handles non-dictionary arguments (like strings, lists, or `None`) passed to a logged function without crashing. It asserts that four entries corresponding to these varied inputs are successfully recorded in the database.*


### test_file_logger_function_use_non_dict_args_no_crash (function, L338-L349)

> *Summary: This test verifies that the `file_logger` can handle non-dictionary arguments passed to its `log_function_use` method without crashing. It iterates through various types of inputs (string, list, None) and asserts that the resulting log file contains content.*


### test_redact_handles_case_variations (function, L357-L370)

> *Summary: This test verifies that the logging mechanism correctly redacts API keys regardless of case variations. It logs events using different casing for the `api_key` field and asserts that the sentinel key is absent from the stored JSON data in the database.*


### test_sqlite_logger_event_empty_kwargs_no_crash (function, L378-L386)

> *Summary: Verifies that calling `log_event` with no keyword arguments does not cause a crash and correctly records an empty JSON object in the database. It asserts that the most recent event stored reflects this empty input.*

