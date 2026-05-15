# test/agents/experimental/a2ui/test_schema_manager.py

1 class(es): TestA2UISchemaManager. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestA2UISchemaManager | class |  |

## Chunks

### TestA2UISchemaManager (class, L10-L100)

> *Summary: This test suite verifies the functionality of a schema management class by instantiating it and asserting various properties, such as default protocol versions, loaded schemas, and component definitions. It also tests methods that generate prompts, allowing configuration to selectively include or exclude schema details and rules.*


### test_default_init (method, L11-L17, parent: TestA2UISchemaManager)

> *Summary: Verifies that a newly instantiated schema manager initializes with expected default values, including a specific protocol version and populated schemas for server-to-client communication and basic/common types. It confirms the catalog ID contains the designated version string.*


### test_unsupported_version_raises (method, L19-L21, parent: TestA2UISchemaManager)

> *Summary: Asserts that instantiating the schema manager with an unsupported protocol version string raises a `ValueError` containing a specific message. This tests the input validation for supported versions during object creation.*


### test_custom_catalog_id_from_catalog (method, L23-L25, parent: TestA2UISchemaManager)

> *Summary: When initialized with a custom catalog dictionary, this test verifies that the schema manager correctly extracts and sets the `$id` from the provided `custom_catalog` as its primary `catalog_id`.*


### test_custom_catalog_without_id_raises (method, L27-L29, parent: TestA2UISchemaManager)

> *Summary: Asserts that initializing the schema manager with a custom catalog lacking an ID raises a `ValueError`. This test verifies input validation for the provided configuration dictionary.*


### test_server_to_client_schema_structure (method, L31-L41, parent: TestA2UISchemaManager)

> *Summary: Verifies that the `A2UISchemaManager` provides a schema structure conforming to JSON Schema Draft 2020-12, ensuring it contains expected definitions for various message types. It checks for the presence of `$schema`, `oneOf`, and specific definition keys like `CreateSurfaceMessage`.*


### test_basic_catalog_has_components (method, L43-L51, parent: TestA2UISchemaManager)

> *Summary: Verifies that the `A2UISchemaManager`'s basic catalog schema contains expected UI component definitions like "Text," "Image," and "Button." It asserts the presence of these specific keys within the retrieved components dictionary.*


### test_catalog_rules_loaded (method, L53-L57, parent: TestA2UISchemaManager)

> *Summary: Verifies that the schema manager successfully loads catalog rules by asserting the presence of specific keys, such as "REQUIRED PROPERTIES" and "Text," within its internal `catalog_rules` attribute.*


### test_generate_prompt_section_includes_format (method, L59-L66, parent: TestA2UISchemaManager)

> *Summary: This test verifies that the generated prompt section from the schema manager contains specific formatting elements, including versioning (`v0.9`), a designated JSON marker (`---a2ui_JSON---`), and references to key operations like `createSurface` and `updateComponents`. It confirms the output structure adheres to expected standards for A2UI interaction.*


### test_generate_prompt_section_includes_components (method, L68-L72, parent: TestA2UISchemaManager)

> *Summary: This test verifies that the generated prompt section from the schema manager contains specific required elements, asserting the presence of "Available Components" and "Text" within the output string. It initializes the manager and calls its generation method to perform this check.*


### test_generate_prompt_section_includes_rules (method, L74-L78, parent: TestA2UISchemaManager)

> *Summary: When called with `include_rules=True`, this test verifies that the generated prompt section from the schema manager contains specific rule-related text, such as "Component Rules" and "REQUIRED PROPERTIES". It confirms the inclusion of detailed constraints within the output prompt.*


### test_generate_prompt_section_excludes_rules (method, L80-L83, parent: TestA2UISchemaManager)

> *Summary: When called with `include_rules=False`, this test verifies that the generated prompt section does not contain any "Component Rules." It instantiates a schema manager and asserts the absence of specific rule text in the resulting output.*


### test_generate_prompt_section_includes_schema (method, L85-L89, parent: TestA2UISchemaManager)

> *Summary: When called with `include_schema=True`, this test verifies that the generated prompt section from the schema manager contains both the "A2UI Message Schema" identifier and the `"$schema"` key. This confirms the inclusion of necessary schema metadata within the output prompt string.*


### test_generate_prompt_section_excludes_schema (method, L91-L94, parent: TestA2UISchemaManager)

> *Summary: When called with `include_schema=False`, this test verifies that the generated prompt section does not contain any references to the A2UI Message Schema. It instantiates a schema manager and asserts the absence of specific schema text in the resulting output.*


### test_custom_delimiter_in_prompt (method, L96-L100, parent: TestA2UISchemaManager)

> *Summary: This test verifies that the schema manager correctly incorporates a user-defined delimiter into the generated prompt section. It asserts that the specified custom delimiter is present and that the default JSON marker is absent from the output.*

