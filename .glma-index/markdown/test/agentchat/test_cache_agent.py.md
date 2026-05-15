# test/agentchat/test_cache_agent.py

8 function(s): test_legacy_disk_cache, _test_redis_cache, test_redis_cache, test_redis_cache_gemini, test_redis_cache_anthropic, test_disk_cache, run_conversation, run_groupchat_conversation.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_legacy_disk_cache | function |  |
| _test_redis_cache | function |  |
| test_redis_cache | function |  |
| test_redis_cache_gemini | function |  |
| test_redis_cache_anthropic | function |  |
| test_disk_cache | function |  |
| run_conversation | function |  |
| run_groupchat_conversation | function |  |

## Chunks

### test_legacy_disk_cache (function, L30-L48)

> *Summary: This test verifies the performance benefit of disk caching by running a conversation twice with the same seed. It asserts that the resulting messages are identical and that the second run, utilizing the cache, completes faster than the first "cold" run.*


### _test_redis_cache (function, L51-L78)

> *Summary: This function tests the performance benefit of caching by running conversations twice against a Redis instance. It asserts that the results are identical and that subsequent runs (warm cache) complete faster than initial runs (cold cache) for both single and group chats.*


### test_redis_cache (function, L85-L86)

> *Summary: This test function executes a dedicated Redis caching test using provided OpenAI credentials. It serves to validate the functionality of the caching mechanism within the agent chat system.*


### test_redis_cache_gemini (function, L94-L95)

> *Summary: This test function verifies the Redis caching mechanism specifically for Gemini Flash credentials by calling a shared testing utility. It takes `Credentials` object containing Gemini flash configuration as input and performs internal tests against it.*


### test_redis_cache_anthropic (function, L102-L103)

> *Summary: This test function verifies the caching mechanism for Anthropic Claude Sonnet interactions by calling a shared testing utility with provided credentials. It ensures that the Redis caching layer functions correctly when interacting with the specified AI model.*


### test_disk_cache (function, L109-L135)

> *Summary: This test verifies the performance benefit of disk caching by running conversations both with and without a cache. It asserts that the results remain identical while confirming that subsequent runs using the populated cache execute significantly faster than initial "cold" runs for both single and group chats.*


### run_conversation (function, L138-L176)

> *Summary: This function orchestrates an agent conversation by initializing and running a chat between an `AssistantAgent` and a `UserProxyAgent`. It takes credentials, a cache seed, and configuration options to execute tasks, ultimately returning the message history from the assistant for the last executed task.*


### run_groupchat_conversation (function, L179-L225)

> *Summary: This function orchestrates a multi-agent group chat simulation using an `AssistantAgent`, a `Planner` agent, and a `UserProxyAgent`. It initializes these agents with provided credentials and runs them through a predefined coding task, returning the final message from the user proxy.*

