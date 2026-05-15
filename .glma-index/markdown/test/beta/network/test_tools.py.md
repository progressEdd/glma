# test/beta/network/test_tools.py

11 function(s): _agent, _invoke, test_peers_find_returns_other_peers_summary, test_peers_find_filters_by_capability, test_peers_describe_returns_skill_md_or_fallback, test_channels_open_and_list_and_close, test_context_search_finds_substring_in_channel_wal, test_context_quote_returns_recent_n_from_speaker, test_tasks_status_and_list_and_wait, test_tasks_status_unknown_task_returns_error and 1 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| _invoke | function |  |
| test_peers_find_returns_other_peers_summary | function |  |
| test_peers_find_filters_by_capability | function |  |
| test_peers_describe_returns_skill_md_or_fallback | function |  |
| test_channels_open_and_list_and_close | function |  |
| test_context_search_finds_substring_in_channel_wal | function |  |
| test_context_quote_returns_recent_n_from_speaker | function |  |
| test_tasks_status_and_list_and_wait | function |  |
| test_tasks_status_unknown_task_returns_error | function |  |
| test_network_plugin_attaches_identity_level_tools | function |  |

## Chunks

### _agent (function, L42-L43)

> *Summary: Creates and returns an `Agent` instance, configuring it using a provided name and a set of event objects passed as variable arguments.*


### _invoke (function, L46-L68)

> *Summary: This asynchronous helper executes a provided tool with specific arguments and dependencies, then unwraps the resulting `ToolResult` to return the raw underlying value. It handles cases where the result is text content or structured data from the tool's output parts.*


### test_peers_find_returns_other_peers_summary (function, L75-L108)

> *Summary: This test verifies that a peer-finding tool correctly returns summaries of other registered agents in the network. It initializes three clients, registers them with specific profiles, and then asserts that the result from the calling agent includes all other registered agents but excludes itself.*


### test_peers_find_filters_by_capability (function, L112-L137)

> *Summary: This test verifies that a peer tool correctly identifies other registered agents possessing a specific capability. It registers two agents, one with the "coding" capability, and then invokes the tool to confirm it returns only the agent matching that capability when queried for "coding," while returning nothing for a missing capability.*


### test_peers_describe_returns_skill_md_or_fallback (function, L141-L179)

> *Summary: This test verifies that a peer description tool correctly retrieves skill metadata from registered agents via a Hub. It asserts that an agent explicitly providing `skill_md` returns it, while another agent without explicit markdown falls back to using rendered resume information in the output.*


### test_channels_open_and_list_and_close (function, L186-L223)

> *Summary: This test verifies the lifecycle of communication channels by first opening a conversation channel between two registered agents, then confirming its presence via listing and retrieving detailed metadata, before finally closing it. It utilizes an in-memory store to manage the hub connections for testing purposes.*


### test_context_search_finds_substring_in_channel_wal (function, L230-L252)

> *Summary: This test verifies that a context search tool correctly extracts relevant text from a channel's write-ahead log (WAL). It simulates two agents communicating in a channel and then queries the system for substrings within the exchanged messages, asserting the correct excerpt is returned.*


### test_context_quote_returns_recent_n_from_speaker (function, L256-L297)

> *Summary: This test verifies that a context quoting tool correctly retrieves the $N$ most recent messages from a specified speaker within an active conversation channel. It sets up two agents, initiates a conversation with three messages from one agent, and then asserts that the tool returns the correct subset of those recent messages based on the input parameters.*


### test_tasks_status_and_list_and_wait (function, L304-L345)

> *Summary: This test verifies task management functionality by first creating and completing a task via a `TaskMirror` attached to a specific agent's stream within a shared Hub environment. It then uses a tasks tool to confirm the task appears in a list, check its final status as "completed," and successfully wait for its completion.*


### test_tasks_status_unknown_task_returns_error (function, L349-L364)

> *Summary: This test verifies that invoking a tasks tool with an unknown task ID returns an error message containing "not found". It sets up a local knowledge store and agent environment to execute the invocation against the registered agent client.*


### test_network_plugin_attaches_identity_level_tools (function, L371-L390)

> *Summary: This test verifies that a network plugin correctly attaches only identity-level cross-cutting tools to an agent upon registration. It asserts that specific core tools are present while ensuring the "say" tool, which is channel-shaped, is absent from the agent's accessible tools.*

