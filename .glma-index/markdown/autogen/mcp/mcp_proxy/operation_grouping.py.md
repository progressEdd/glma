# autogen/mcp/mcp_proxy/operation_grouping.py

6 function(s): set_llm_config, chunk_list, discover_groups, assign_operation_to_group, refine_group_names, custom_visitor. 3 class(es): Group, GroupSuggestions, GroupNames.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| set_llm_config | function |  |
| Group | class |  |
| GroupSuggestions | class |  |
| GroupNames | class |  |
| chunk_list | function |  |
| discover_groups | function |  |
| assign_operation_to_group | function |  |
| refine_group_names | function |  |
| custom_visitor | function |  |

## Chunks

### set_llm_config (function, L23-L26)

> *Summary: Updates a global configuration object with provided `LLMConfig` settings. This function stores the input configuration to be used throughout the module's operation grouping logic.*


### Group (class, L29-L31)

> *Summary: Represents a logical grouping with a name and a descriptive string. It serves as a data structure to categorize related items or operations.*


### GroupSuggestions (class, L34-L35)

> *Summary: This data structure holds a list of `Group` objects, representing suggested groupings for an operation. It serves as the standardized output format for grouping suggestions.*


### GroupNames (class, L38-L39)

> *Summary: This data model holds a list of strings representing predefined group names. It serves as a structured container for passing or receiving these group identifiers within the system.*


### chunk_list (function, L68-L69)

> *Summary: This function divides a given list into smaller sublists of a specified maximum size. It takes an input list and an integer size, returning a new list containing these chunks.*


### discover_groups (function, L72-L118)

> *Summary: This function groups a list of operations by iteratively sending chunks of their descriptions to an LLM agent for initial suggestions, then refines those suggested groups using a second LLM interaction. It takes a list of `Operation` objects and returns a dictionary containing the final, unique group names and descriptions.*


### assign_operation_to_group (function, L121-L150)

> *Summary: This function uses a configured conversational agent to determine the appropriate group for a given operation based on its summary and arguments, considering a list of available groups. It takes an `Operation` object and a dictionary of `groups` as input, returning a string representing the assigned group name(s).*


### refine_group_names (function, L153-L156)

> *Summary: This function takes a dictionary mapping group identifiers to their names and returns it unchanged as a placeholder. It is intended to optionally refine or merge group names based on similarity metrics like embeddings.*


### custom_visitor (function, L159-L175)

> *Summary: This function processes parsed OpenAPI operations to organize them into logical groups based on their paths and associated metadata. It first discovers potential operation groupings and then iterates through all operations, assigning each one to the appropriate group(s) before returning a dictionary containing the fully annotated list of operations.*

