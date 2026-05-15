# autogen/logger/sqlite_logger.py

1 function(s): safe_serialize. 1 class(es): SqliteLogger. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| safe_serialize | function |  |
| SqliteLogger | class |  |

## Chunks

### safe_serialize (function, L46-L62)

> *Summary: Converts any Python object into a JSON string, using a custom encoder to handle objects with a `to_json` method or marking non-serializable types with a specific placeholder string. This ensures robust serialization even when encountering complex data structures.*


### SqliteLogger (class, L66-L498)

> *Summary: This class manages persistent logging to an SQLite database, initializing tables for various entities like chat completions, agents, and clients upon startup. It provides methods to record specific events—such as logging a completion, creating a new agent, or recording function calls—by executing parameterized SQL queries against the configured database file.*


### __init__ (method, L71-L85, parent: SqliteLogger)

> *Summary: Establishes a connection to an SQLite database using configuration settings, defaulting the filename if none is provided. It initializes internal state including the database name, cursor, and a unique session ID upon successful connection.*


### start (method, L87-L188, parent: SqliteLogger)

> *Summary: Initializes the SQLite logger by creating several tables (`chat_completions`, `agents`, `oai_wrappers`, etc.) to persist conversation data and system state. It then checks for and applies database migrations before returning the session ID.*


### _get_current_db_version (method, L190-L193, parent: SqliteLogger)

> *Summary: Retrieves the latest database schema version by querying the `version` table, returning the version number as an integer or `None` if no records exist.*


### _apply_migration (method, L196-L216, parent: SqliteLogger)

> *Summary: This method checks for and applies database schema migrations found in a specified directory. It compares the current database version against available migration scripts, executes necessary SQL changes sequentially, and updates the stored version number after each successful script application.*


### _run_query (method, L218-L230, parent: SqliteLogger)

> *Summary: Executes a provided SQL query string along with optional arguments within a thread lock to ensure data integrity. It commits the transaction upon success or logs any encountered exceptions during execution.*


### _run_query_script (method, L232-L243, parent: SqliteLogger)

> *Summary: Executes a provided SQL script against the database connection within a lock to ensure thread safety. It commits the changes upon success and logs any exceptions encountered during execution.*


### log_chat_completion (method, L245-L307, parent: SqliteLogger)

> *Summary: This method persists a chat completion record to an SQLite database if the connection is active. It accepts various inputs including IDs, request/response data, cost, and timestamps, serializes them appropriately, and executes an `INSERT` query into the `chat_completions` table.*


### log_new_agent (method, L309-L346, parent: SqliteLogger)

> *Summary: This method records a newly created agent into the SQLite database using an upsert operation to prevent duplicates based on `agent_id` and `session_id`. It takes a `ConversableAgent` instance and its initialization arguments as input, storing details like name, class, and serialized configuration in the output.*


### log_event (method, L348-L388, parent: SqliteLogger)

> *Summary: Records an event into the SQLite database, differentiating between events originating from a string source and those from an `Agent` object. It serializes provided keyword arguments after redacting sensitive data before executing the appropriate SQL insertion query.*


### log_new_wrapper (method, L390-L415, parent: SqliteLogger)

> *Summary: This method records a new wrapper's details into an SQLite database if the connection exists. It serializes the wrapper's initialization arguments (excluding sensitive keys) and inserts them along with the wrapper ID and session ID.*


### log_function_use (method, L417-L440, parent: SqliteLogger)

> *Summary: Records the execution details of a function call into an SQLite database. It takes the source identifier, the function object, its arguments, and its return value as input to persist them with a timestamp.*


### log_new_client (method, L442-L487, parent: SqliteLogger)

> *Summary: Records a new client connection into the SQLite database if the logger is initialized. It takes various AI clients, their wrapper, and initialization arguments as input to insert a record containing IDs, class name, serialized arguments, and a timestamp.*


### stop (method, L489-L492, parent: SqliteLogger)

> *Summary: Closes the underlying database connection if one exists, effectively shutting down the logging mechanism. This method takes no input and returns nothing.*


### get_connection (method, L494-L498, parent: SqliteLogger)

> *Summary: Retrieves the existing SQLite database connection if it has been established; otherwise, it returns `None`. This method acts as a getter for the internal connection object.*

