# autogen/beta/a2a/transports/_common.py

3 function(s): clone_card_with_capabilities, build_default_handler, build_card_routes_with_legacy.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| clone_card_with_capabilities | function |  |
| build_default_handler | function |  |
| build_card_routes_with_legacy | function |  |

## Chunks

### clone_card_with_capabilities (function, L29-L37)

> *Summary: Creates a deep copy of an input card, ensuring the original remains unchanged. It optionally sets specific capability flags (`extended_agent_card` or `push_notifications`) on the newly created card based on boolean inputs.*


### build_default_handler (function, L40-L59)

> *Summary: Constructs a standardized request handler for SDK transports by accepting various components like an agent executor and configuration stores. It initializes the `DefaultRequestHandlerV2`, providing default implementations (e.g., `InMemoryTaskStore`) if optional inputs are missing.*


### build_card_routes_with_legacy (function, L62-L81)

> *Summary: Generates a list of routing objects for an agent card, incorporating both the primary URL and an optional legacy URL. It calls a helper function to create routes for each provided URL, combining them into a single return list.*

