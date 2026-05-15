# autogen/agents/experimental/a2ui/a2ui_agent.py

1 class(es): A2UIAgent. 13 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2UIAgent | class |  |

## Chunks

### A2UIAgent (class, L24-L279)

> *Summary: This agent generates rich, structured UI output adhering to the A2UI protocol (v0.9), supporting custom catalogs and schema validation. It automatically handles response parsing and retries generation if the LLM's output fails schema validation, gracefully degrading to text-only responses upon exhaustion of retries.*


### __init__ (method, L53-L138, parent: A2UIAgent)

> *Summary: Initializes an agent configured to interact using the A2UI protocol by setting up schema management and response parsing based on provided catalogs and validation settings. It constructs a comprehensive system message incorporating custom instructions, schemas, rules, and defined actions before inheriting from the base agent class.*


### _validate_a2ui_response (method, L140-L159, parent: A2UIAgent)

> *Summary: Parses and validates an A2UI response string by first attempting to extract structured data. It returns the parsed result along with a list of errors if parsing failed or if the extracted operations do not meet validation criteria.*


### _build_retry_messages (method, L161-L175, parent: A2UIAgent)

> *Summary: This method constructs a message history for retrying an operation by appending the original assistant response and detailed validation error feedback to the provided working messages. It takes the current conversation, the raw response text, parsing results, and any validation errors as input, returning the augmented list of messages.*


### _a2ui_validating_reply (method, L177-L223, parent: A2UIAgent)

> *Summary: This method attempts to validate an LLM's output against A2UI specifications by iteratively generating and checking responses. It takes messages, a sender agent, and configuration as input, returning a tuple indicating success and either the validated response or a fallback text string upon failure.*


### update_system_message (method, L225-L237, parent: A2UIAgent)

> *Summary: This method modifies the provided system message by automatically appending a predefined A2UI prompt section if it's missing. It then passes this potentially augmented message to the parent class's update function.*


### a2ui_prompt_section (method, L240-L242, parent: A2UIAgent)

> *Summary: Returns a string containing the specific prompt segment for the A2UI agent, which is intended to be appended to the overall system message. This method accesses and returns a pre-defined internal attribute.*


### schema_manager (method, L245-L247, parent: A2UIAgent)

> *Summary: Returns the internal `A2UISchemaManager` instance associated with the agent. This provides access to the component responsible for managing schemas within the agent's context.*


### response_parser (method, L250-L252, parent: A2UIAgent)

> *Summary: Returns the configured `A2UIResponseParser` instance associated with the agent. This method provides access to the component responsible for interpreting the agent's output.*


### protocol_version (method, L255-L257, parent: A2UIAgent)

> *Summary: Returns the specific A2UI protocol version string that the agent is configured to use, sourced from its schema manager.*


### catalog_id (method, L260-L262, parent: A2UIAgent)

> *Summary: Retrieves the unique identifier for the agent's associated catalog from the internal schema manager. This method returns a string representing that specific catalog ID.*


### actions (method, L265-L267, parent: A2UIAgent)

> *Summary: Returns a list of predefined `A2UIAction` objects that the agent can execute. This method provides access to the agent's available operational capabilities.*


### get_action (method, L269-L274, parent: A2UIAgent)

> *Summary: Retrieves a specific action object from the agent's internal registry based on the provided string name. It iterates through all registered actions and returns the matching one, or `None` if no action with that name is found.*


### validation_retries (method, L277-L279, parent: A2UIAgent)

> *Summary: Returns the configured maximum count for retrying validation checks. This value is stored internally within the agent instance.*

