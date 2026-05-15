# test/agentchat/test_agent_logging.py

5 function(s): db_connection, _test_two_agents_logging, test_two_agents_logging, _test_groupchat_logging, test_groupchat_logging.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| db_connection | function |  |
| _test_two_agents_logging | function |  |
| test_two_agents_logging | function |  |
| _test_groupchat_logging | function |  |
| test_groupchat_logging | function |  |

## Chunks

### db_connection (function, L48-L54)

> *Summary: Establishes an in-memory SQLite database connection for runtime logging, yielding the configured connection object to consumers. It ensures proper cleanup by stopping the logging mechanism after the generator is exhausted.*


### _test_two_agents_logging (function, L57-L182)

> *Summary: This function tests the logging mechanism by simulating a chat interaction between two agents, then verifies data integrity across several database tables (completions, agents, OAI clients, and wrappers). It asserts that logged records contain correct IDs, message content matches expected system prompts, and configuration details are properly stored.*


### test_two_agents_logging (function, L189-L206)

> *Summary: This test function determines which client classes to use based on pytest markers applied to the current test. It then calls a helper function with credentials, a database connection, and the determined list of client classes to execute logging tests for two agents.*


### _test_groupchat_logging (function, L209-L277)

> *Summary: This test function simulates a group chat interaction between two AI agents, using provided credentials for LLM configuration. It then queries the database to assert that the conversation history, agent registrations, and event logs were correctly recorded after initiating the chat with a specific prompt.*


### test_groupchat_logging (function, L282-L286)

> *Summary: This test verifies group chat logging by calling a helper function with provided credentials and an active database connection. It ensures the logging mechanism functions correctly within the context of a simulated group chat scenario.*

