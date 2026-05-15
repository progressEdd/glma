# test/beta/providers/gemini/test_session_smoke.py

7 function(s): gemini_config, _agent, _wait_text_count, _wait_for_terminal, test_persisted_consulting_survives_hub_restart, test_concurrent_consultings_isolated, test_close_during_llm_turn_rejects_late_reply.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| gemini_config | function |  |
| _agent | function |  |
| _wait_text_count | function |  |
| _wait_for_terminal | function |  |
| test_persisted_consulting_survives_hub_restart | function |  |
| test_concurrent_consultings_isolated | function |  |
| test_close_during_llm_turn_rejects_late_reply | function |  |

## Chunks

### gemini_config (function, L52-L56)

> *Summary: Retrieves the necessary configuration for Gemini interactions by reading the `GEMINI_API_KEY` environment variable. If the key is missing, it skips testing; otherwise, it returns a configured `GeminiConfig` object using "gemini-3-flash-preview" and a temperature of 0.*


### _agent (function, L59-L60)

> *Summary: Creates and returns a new `Agent` instance using the provided name, prompt string, and configuration object. This helper function abstracts the instantiation process for agent objects.*


### _wait_text_count (function, L63-L70)

> *Summary: This asynchronous function polls a channel's write-ahead log until the count of `EV_TEXT` events meets or exceeds an expected number, respecting a specified timeout. It returns the collected log entries upon success or raises a `TimeoutError` if the condition is not met within the allotted time.*


### _wait_for_terminal (function, L73-L80)

> *Summary: This asynchronous function polls a communication channel periodically until it reports a terminal state or a specified timeout is reached. If the channel does not become terminal within the allotted time, it raises an `asyncio.TimeoutError`.*


### test_persisted_consulting_survives_hub_restart (function, L85-L157)

> *Summary: This test verifies that a consulting session, including its state (WAL, capabilities, audit log), persists correctly to disk and can be fully reconstructed after the main hub process is restarted. It initializes two agents, conducts a conversation, closes the system, reopens it using the same persistent store, and then asserts that all prior data structures are intact and consistent with the initial run.*


### test_concurrent_consultings_isolated (function, L162-L230)

> *Summary: This test verifies that concurrent, isolated communication channels between agents do not leak information across different conversations. It initiates two simultaneous consulting sessions and asserts that each agent's message log (WAL) only contains data relevant to its specific channel.*


### test_close_during_llm_turn_rejects_late_reply (function, L235-L286)

> *Summary: When a channel is abruptly closed while an LLM is generating a response, this test verifies that the system remains consistent by ensuring only the initial prompt from the sender is recorded in the Write-Ahead Log (WAL), and no corrupted late replies are present. It confirms the channel terminates cleanly with the specified abort reason.*

