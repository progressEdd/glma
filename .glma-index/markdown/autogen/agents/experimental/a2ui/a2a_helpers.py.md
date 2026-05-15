# autogen/agents/experimental/a2ui/a2a_helpers.py

5 function(s): create_a2ui_part, is_a2ui_part, get_a2ui_datapart, get_a2ui_agent_extension, try_activate_a2ui_extension.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| create_a2ui_part | function |  |
| is_a2ui_part | function |  |
| get_a2ui_datapart | function |  |
| get_a2ui_agent_extension | function |  |
| try_activate_a2ui_extension | function |  |

## Chunks

### create_a2ui_part (function, L31-L59)

> *Summary: Transforms raw A2UI operation data, which can be a single dictionary or a list of dictionaries, into one or more `Part` objects. Each input operation is wrapped in a `DataPart` tagged with the specific A2UI MIME type for agent consumption.*


### is_a2ui_part (function, L62-L75)

> *Summary: Determines if a given `Part` object contains specific A2UI data by checking if its root element is a `DataPart`, has metadata, and that metadata specifies the required A2UI MIME type. Returns a boolean indicating this condition.*


### get_a2ui_datapart (function, L78-L89)

> *Summary: This function extracts an `A2UI DataPart` from a given `A2A Part`. It returns the root of the part if it is identified as an A2UI part, otherwise it returns `None`.*


### get_a2ui_agent_extension (function, L93-L116)

> *Summary: Constructs an `AgentExtension` object declaring support for A2UI v0.9 output by setting a specific URI and description. It optionally configures this extension to accept inline custom catalogs based on the provided boolean flag.*


### try_activate_a2ui_extension (function, L120-L142)

> *Summary: Checks the request context for a specific extension URI; if present, it registers the activation within the context's metadata and returns `True`, otherwise it returns `False`. This function is used to negotiate A2UI support during agent execution.*

