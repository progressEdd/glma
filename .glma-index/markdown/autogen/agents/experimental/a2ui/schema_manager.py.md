# autogen/agents/experimental/a2ui/schema_manager.py

1 class(es): A2UISchemaManager. 21 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2UISchemaManager | class |  |

## Chunks

### A2UISchemaManager (class, L30-L407)

> *Summary: This class manages the loading of A2UI schemas and generates comprehensive system prompts for LLMs. It ingests protocol versions, loads base and optional custom JSON catalogs, and compiles all necessary components, rules, schema definitions, and available actions into a single string prompt.*


### __init__ (method, L53-L118, parent: A2UISchemaManager)

> *Summary: Initializes a schema manager by loading core A2UI specification files based on the provided protocol version. It accepts optional inputs for custom catalogs and rules, which are loaded or merged to define the system's component schemas and catalog ID. The resulting object holds all necessary configuration data for managing API specifications.*


### protocol_version (method, L121-L122, parent: A2UISchemaManager)

> *Summary: Returns the stored string representing the current protocol version of the agent's configuration. This method provides read access to the internal version identifier.*


### catalog_id (method, L125-L126, parent: A2UISchemaManager)

> *Summary: Retrieves the internal catalog identifier string stored within the instance. This method provides read access to a pre-set attribute of the object.*


### server_to_client_schema (method, L129-L130, parent: A2UISchemaManager)

> *Summary: Returns the internal `_server_to_client` dictionary, which represents the schema structure intended for client consumption. This method provides a direct access point to the serialized schema data.*


### basic_catalog_schema (method, L133-L134, parent: A2UISchemaManager)

> *Summary: Returns the internal dictionary representing a fundamental catalog schema. This method provides read access to the pre-defined structure.*


### custom_catalog_schema (method, L137-L138, parent: A2UISchemaManager)

> *Summary: Returns the internal `_custom_catalog` dictionary if it exists, otherwise returns `None`. This method provides access to a user-defined catalog structure.*


### common_types_schema (method, L141-L142, parent: A2UISchemaManager)

> *Summary: Returns a dictionary containing predefined common types from the instance's internal state. This method provides access to standardized type definitions used throughout the system.*


### version_string (method, L145-L147, parent: A2UISchemaManager)

> *Summary: Retrieves the specific version identifier, such as 'v0.9', from a configuration dictionary based on the agent's protocol version. This string is intended for inclusion in A2UI messages.*


### catalog_rules (method, L150-L151, parent: A2UISchemaManager)

> *Summary: Retrieves the internal string containing predefined rules for the catalog. This method takes no input and returns a string representing those rules.*


### custom_catalog_rules (method, L154-L155, parent: A2UISchemaManager)

> *Summary: Retrieves a predefined string containing custom catalog rules from the instance's internal state. This method serves as an accessor for specialized configuration data.*


### _get_active_catalog (method, L157-L159, parent: A2UISchemaManager)

> *Summary: Retrieves and returns either a user-defined custom catalog or falls back to a predefined basic catalog. It checks the `_custom_catalog` attribute; if it's set, that dictionary is returned otherwise.*


### _get_all_components (method, L161-L167, parent: A2UISchemaManager)

> *Summary: Aggregates all available components by merging entries from both the built-in and any provided custom catalogs. It returns a single dictionary containing every component found across these sources.*


### get_component_schemas (method, L169-L183, parent: A2UISchemaManager)

> *Summary: Retrieves a dictionary mapping component type names to their corresponding JSON Schema definitions by iterating through both basic and custom catalogs. It aggregates these schemas, ensuring each unique component name is only added once to the final output.*


### build_schema_registry (method, L185-L223, parent: A2UISchemaManager)

> *Summary: Constructs a `jsonschema` registry by loading and mapping various internal schemas (like catalog, common types, and server-to-client definitions) to their respective URIs. This allows for local resolution of `$ref` pointers across different schema files during validation.*


### _load_spec_json (method, L225-L230, parent: A2UISchemaManager)

> *Summary: Reads and parses a JSON file located within the agent's specification directory using the provided filename. It returns the deserialized content as a Python dictionary.*


### _load_spec_text (method, L232-L238, parent: A2UISchemaManager)

> *Summary: Reads and returns the stripped content of a specified text file located within the agent's specification directory, returning an empty string if the file is not found.*


### _load_version_json (method, L240-L245, parent: A2UISchemaManager)

> *Summary: Reads and parses a JSON file located within the agent's version directory using the provided filename. It returns the deserialized content, which can be either a list or a dictionary.*


### _load_version_text (method, L247-L253, parent: A2UISchemaManager)

> *Summary: Reads and returns the stripped content of a specified text file located within the agent's version directory, returning an empty string if the file does not exist.*


### _build_prompt_example (method, L255-L261, parent: A2UISchemaManager)

> *Summary: Generates a JSON string for a prompt example by serializing an internal structure and then replacing a placeholder with the active catalog ID. This method outputs the final, formatted string ready for use in prompts.*


### generate_prompt_section (method, L263-L390, parent: A2UISchemaManager)

> *Summary: Constructs a comprehensive string detailing the A2UI protocol for an agent's system prompt. It incorporates optional sections for JSON schema, catalog rules, available actions (server events or client functions), and component definitions based on provided configuration. The output is a single formatted string ready to be appended to the main system instructions.*


### _extract_component_description (method, L392-L407, parent: A2UISchemaManager)

> *Summary: This method generates a human-readable description string for a component definition. It first checks for an explicit description; otherwise, it compiles and returns a list of all non-metadata properties found within the component's definitions.*

