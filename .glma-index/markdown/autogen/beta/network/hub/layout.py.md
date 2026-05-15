# autogen/beta/network/hub/layout.py

20 function(s): agents_root, passport_path, resume_path, skill_path, runtime_path, rule_path, inbox_cursor_path, inbox_nacks_path, inbox_overflow_path, registry_root and 10 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| agents_root | function |  |
| passport_path | function |  |
| resume_path | function |  |
| skill_path | function |  |
| runtime_path | function |  |
| rule_path | function |  |
| inbox_cursor_path | function |  |
| inbox_nacks_path | function |  |
| inbox_overflow_path | function |  |
| registry_root | function |  |
| by_name_path | function |  |
| by_capability_path | function |  |
| channels_root | function |  |
| channel_metadata_path | function |  |
| wal_path | function |  |
| channel_tasks_index_path | function |  |
| tasks_root | function |  |
| task_metadata_path | function |  |
| task_events_path | function |  |
| audit_path | function |  |

## Chunks

### agents_root (function, L40-L41)

> *Summary: Returns the base directory path for all agent components, which is hardcoded as `/agents`. This function serves to provide a consistent root location for agent-related files.*


### passport_path (function, L44-L45)

> *Summary: Generates a standardized file path string for an agent's passport data, taking the agent's unique ID as input and returning the full URI.*


### resume_path (function, L48-L49)

> *Summary: Generates a standardized file path string for resuming an agent's state, using the provided `agent_id` to construct the location within the `/agents/` directory structure.*


### skill_path (function, L52-L53)

> *Summary: Generates a file path string for a specific agent's skill documentation. It takes an `agent_id` as input and returns the full relative path to that agent's `SKILL.md` file.*


### runtime_path (function, L56-L57)

> *Summary: Generates a standardized file path string for accessing the runtime configuration of a specific agent, using the provided `agent_id` as input to construct the output path.*


### rule_path (function, L60-L61)

> *Summary: Constructs a standardized file path string for accessing an agent's specific rule configuration. It takes an `agent_id` as input and returns the full JSON path pointing to that agent's rules.*


### inbox_cursor_path (function, L64-L65)

> *Summary: Generates the file path for an agent's inbox cursor, taking a string `agent_id` as input and returning a formatted string representing the resource location.*


### inbox_nacks_path (function, L68-L69)

> *Summary: Generates the file path for an agent's inbox non-acknowledgments by prepending `/agents/` to the provided `agent_id`. The output is a string representing the full JSONL file location.*


### inbox_overflow_path (function, L72-L73)

> *Summary: Generates a file path string for an agent's inbox overflow, taking the agent's ID as input and returning a specific JSONL file location.*


### registry_root (function, L79-L80)

> *Summary: Returns the base path string, which is hardcoded to `"/registry"`, serving as a root directory for network components.*


### by_name_path (function, L83-L84)

> *Summary: Returns the file path string pointing to the registry's "by\_name.json" configuration. This function provides a standardized location for name-based registry lookups.*


### by_capability_path (function, L87-L88)

> *Summary: Returns the file path string pointing to the capability registry, specifically `/registry/by_capability.json`. This function provides a static reference for accessing capabilities organized by their paths.*


### channels_root (function, L94-L95)

> *Summary: Returns the base directory path for all communication channels, which is hardcoded as `/channels`. This function takes no inputs and outputs a string representing the root channel location.*


### channel_metadata_path (function, L98-L99)

> *Summary: Generates the full file path for a channel's metadata by prepending `/channels/` to the provided `channel_id` and appending `/metadata.json`. This function takes a string ID as input and returns a complete URL-like string path.*


### wal_path (function, L102-L103)

> *Summary: Constructs the file path for a channel's Write-Ahead Log (WAL). It takes a `channel_id` string as input and returns the full, formatted JSONL path string.*


### channel_tasks_index_path (function, L106-L107)

> *Summary: Constructs a standardized file path string for accessing task data associated with a given channel ID. It takes a `channel_id` string as input and returns the full JSON path to that channel's tasks.*


### tasks_root (function, L113-L114)

> *Summary: Returns the base directory path for task-related resources, specifically `/tasks`. This function serves as a constant endpoint definition.*


### task_metadata_path (function, L117-L118)

> *Summary: Generates the full file path for a task's metadata by prepending `/tasks/` to the provided `task_id` and appending `/metadata.json`. This function takes a string ID as input and returns a complete string representing the expected location of the metadata file.*


### task_events_path (function, L121-L122)

> *Summary: Generates a standardized file path string for accessing event logs associated with a given task ID. It constructs the path using the provided `task_id` within a `/tasks/` directory structure, resulting in a JSONL file name.*


### audit_path (function, L128-L130)

> *Summary: Returns the fixed string path to a single, append-only JSON Lines file used for logging audits. This function takes no inputs and outputs a `str`.*

