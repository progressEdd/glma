# test/beta/config/openai/test_openai_responses_config.py

5 function(s): test_copy_without_overrides_returns_new_equal_instance, test_copy_applies_overrides_without_mutating_original, test_create_returns_openai_responses_client, test_store_defaults_to_true, test_store_can_be_disabled.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_copy_without_overrides_returns_new_equal_instance | function |  |
| test_copy_applies_overrides_without_mutating_original | function |  |
| test_create_returns_openai_responses_client | function |  |
| test_store_defaults_to_true | function |  |
| test_store_can_be_disabled | function |  |

## Chunks

### test_copy_without_overrides_returns_new_equal_instance (function, L9-L15)

> *Summary: Verifies that calling the `copy()` method on an existing configuration object produces a new instance that is structurally equal to the original but is not the same object in memory. This confirms proper shallow or deep copying behavior without any overrides being applied.*


### test_copy_applies_overrides_without_mutating_original (function, L18-L31)

> *Summary: This test verifies that calling the `copy()` method on a configuration object creates a new instance with specified overrides while leaving the original object completely unchanged. It confirms that input parameters correctly update the copied object's state without affecting the source object's attributes.*


### test_create_returns_openai_responses_client (function, L34-L38)

> *Summary: This test verifies that instantiating an `OpenAIResponsesConfig` with specific model and API key parameters successfully produces an instance of `OpenAIResponsesClient`. It confirms the correct type is returned upon calling the configuration's creation method.*


### test_store_defaults_to_true (function, L41-L43)

> *Summary: Verifies that the `store` attribute defaults to `True` when initializing an `OpenAIResponsesConfig` instance with a specified model. It asserts this default value holds true for the configuration object.*


### test_store_can_be_disabled (function, L46-L48)

> *Summary: Verifies that an `OpenAIResponsesConfig` instance correctly reflects the disabled state when initialized with `store=False`. It asserts that the internal `store` attribute matches the provided boolean input.*

