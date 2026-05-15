# test/beta/config/gemini/test_gemini_config.py

12 function(s): test_copy_without_overrides_returns_new_equal_instance, test_copy_applies_overrides_without_mutating_original, test_create_returns_gemini_client, test_vertex_config_create_returns_gemini_client, test_defaults, test_vertex_config_defaults, test_max_output_tokens_can_be_set, test_gemini_config_forces_vertexai_false, test_vertex_config_forces_vertexai_true, test_credentials_string_loads_service_account_file and 2 more. 1 class(es): TestThinkingConfig. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_copy_without_overrides_returns_new_equal_instance | function |  |
| test_copy_applies_overrides_without_mutating_original | function |  |
| test_create_returns_gemini_client | function |  |
| test_vertex_config_create_returns_gemini_client | function |  |
| test_defaults | function |  |
| test_vertex_config_defaults | function |  |
| test_max_output_tokens_can_be_set | function |  |
| test_gemini_config_forces_vertexai_false | function |  |
| test_vertex_config_forces_vertexai_true | function |  |
| test_credentials_string_loads_service_account_file | function |  |
| test_credentials_object_passed_through_unchanged | function |  |
| test_credentials_none_passes_through | function |  |
| TestThinkingConfig | class |  |

## Chunks

### test_copy_without_overrides_returns_new_equal_instance (function, L14-L20)

> *Summary: Verifies that calling the `copy()` method on a configuration object produces a new instance that is structurally equal to the original but is not the same object in memory. This confirms proper shallow or deep copying behavior without any overrides being applied.*


### test_copy_applies_overrides_without_mutating_original (function, L23-L36)

> *Summary: Verifies that calling a `copy()` method on a configuration object creates a new instance with specified overrides while leaving the original object completely unchanged. It tests this by comparing the state of the copied object against the input parameters and ensuring the source object retains its initial values.*


### test_create_returns_gemini_client (function, L39-L43)

> *Summary: This test verifies that instantiating a `GeminiConfig` with specific model and API key parameters successfully produces an object of type `GeminiClient`. It confirms the configuration correctly initializes and returns the expected client instance.*


### test_vertex_config_create_returns_gemini_client (function, L46-L50)

> *Summary: When initialized with specific model, project, and location details, this test verifies that the configuration object correctly produces an instance of `GeminiClient`. The function asserts the type of the returned client object matches `GeminiClient`.*


### test_defaults (function, L53-L58)

> *Summary: Verifies that a `GeminiConfig` initialized with a default model exhibits specific unset or default values for streaming, temperature, token limits, and API key. It confirms the initial state of configuration parameters when no explicit settings are provided.*


### test_vertex_config_defaults (function, L61-L66)

> *Summary: Verifies that a default `VertexAIConfig` initialized with a specific model has streaming disabled and lacks project, location, or credentials settings. This test confirms the baseline state of configuration parameters when no explicit values are provided.*


### test_max_output_tokens_can_be_set (function, L69-L71)

> *Summary: Verifies that the `GeminiConfig` object correctly stores and exposes a specified maximum output token limit when initialized with it. It confirms the input value matches the stored attribute.*


### test_gemini_config_forces_vertexai_false (function, L75-L83)

> *Summary: This test verifies that when initializing `GeminiConfig` with a specific model and API key, the underlying client call correctly sets `vertexai` to `False`, while also asserting the provided `api_key` matches. It confirms that project, location, and credentials are not passed during this configuration setup.*


### test_vertex_config_forces_vertexai_true (function, L87-L98)

> *Summary: This test verifies that when creating a `VertexAIConfig` with specific parameters, the underlying mock client receives the correct configuration values. It asserts that the `vertexai` flag is set to `True`, along with matching project and location identifiers.*


### test_credentials_string_loads_service_account_file (function, L103-L119)

> *Summary: This test verifies that when initializing `VertexAIConfig` with a file path, the underlying credential loading mechanism is called correctly with the specified file and required scopes. It further asserts that the resulting credentials object is passed to the client upon configuration creation.*


### test_credentials_object_passed_through_unchanged (function, L124-L136)

> *Summary: This test verifies that a provided credentials object is passed directly and unmodified when initializing and calling the `VertexAIConfig`'s creation method. It asserts that no file reading occurs and confirms the exact same credential object is present in the mock client's arguments.*


### test_credentials_none_passes_through (function, L141-L146)

> *Summary: This test verifies that when no credentials are provided, the configuration object successfully initializes and passes `None` for the credentials argument to the underlying client call. It asserts that credential loading from a file was not attempted during this process.*


### TestThinkingConfig (class, L149-L219)

> *Summary: These tests verify how `GeminiConfig` and `VertexAIConfig` construct the final configuration object, specifically focusing on the `thinking_config`. They confirm that explicit configurations override shorthand inputs (like setting `thinking_level`), and demonstrate correct handling when no thinking parameters are provided.*


### test_default_omits_thinking_config (method, L150-L152, parent: TestThinkingConfig)

> *Summary: When initialized with a specific model, this test asserts that the resulting configuration object does not contain any `thinking_config` when its creation method is called. It verifies the default behavior of omitting thinking configurations for the specified Gemini model.*


### test_explicit_thinking_config_passes_through (method, L154-L157, parent: TestThinkingConfig)

> *Summary: This test verifies that a provided `ThinkingConfig` object, set to "low" level, is correctly embedded within the final configuration when creating a `GeminiConfig`. It asserts that the internal representation of the configuration retains the original `thinking` instance.*


### test_thinking_level_shorthand_builds_config (method, L159-L164, parent: TestThinkingConfig)

> *Summary: This test verifies that a `GeminiConfig` initialized with `"low"` thinking level correctly constructs a `ThinkingConfig` object where the level is set to `LOW` and the budget remains unset (`None`). It confirms the internal configuration structure matches expectations for low-level thinking.*


### test_thinking_budget_shorthand_builds_config (method, L166-L171, parent: TestThinkingConfig)

> *Summary: This test verifies that a `GeminiConfig` initialized with a specific thinking budget correctly constructs its internal configuration. It asserts that the resulting `ThinkingConfig` object has the expected budget and that the thinking level defaults to `None`.*


### test_thinking_level_and_budget_combined (method, L173-L182, parent: TestThinkingConfig)

> *Summary: This test verifies that a `GeminiConfig` object correctly translates specified thinking level and budget into the expected internal structure. It asserts that the resulting configuration contains a `ThinkingConfig` instance with the correct enum value for the level and the exact integer for the budget.*


### test_explicit_thinking_config_wins_over_shorthand (method, L184-L191, parent: TestThinkingConfig)

> *Summary: This test verifies that an explicitly defined `ThinkingConfig` overrides a shorthand setting when constructing the final Gemini configuration. It asserts that the resulting configuration uses the detailed, high-level thinking settings provided in the input object.*


### test_vertex_ai_thinking_level_shorthand_builds_config (method, L193-L202, parent: TestThinkingConfig)

> *Summary: This test verifies that a `VertexAIConfig` initialized with `"low"` thinking level correctly constructs the internal configuration object. It asserts that the resulting `thinking_config` is of type `ThinkingConfig` and its `thinking_level` matches the expected `ThinkingLevel.LOW`.*


### test_vertex_ai_explicit_thinking_config_passes_through (method, L204-L212, parent: TestThinkingConfig)

> *Summary: This test verifies that a `ThinkingConfig` object with a specified budget is correctly passed through and retained within the final configuration structure when initializing a `VertexAIConfig`. It asserts that the internal representation of the configuration matches the input `thinking` object.*


### test_copy_overrides_thinking_level (method, L214-L219, parent: TestThinkingConfig)

> *Summary: Verifies that calling `copy()` on a configuration object correctly overrides the original instance's state, resulting in a new object with the specified value while leaving the source object unchanged. It tests this by setting an initial low thinking level and copying it over to a high one.*

