# test/beta/config/dashscope/test_dashscope_config.py

5 function(s): test_copy_without_overrides_returns_new_equal_instance, test_copy_applies_overrides_without_mutating_original, test_create_returns_dashscope_client, test_defaults, test_base_url_can_be_overridden.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_copy_without_overrides_returns_new_equal_instance | function |  |
| test_copy_applies_overrides_without_mutating_original | function |  |
| test_create_returns_dashscope_client | function |  |
| test_defaults | function |  |
| test_base_url_can_be_overridden | function |  |

## Chunks

### test_copy_without_overrides_returns_new_equal_instance (function, L9-L15)

> *Summary: Verifies that calling the `copy()` method on a configuration object produces a new instance that is structurally equal to the original but is not the same object in memory. This confirms proper shallow or deep copying behavior without any overrides being applied.*


### test_copy_applies_overrides_without_mutating_original (function, L18-L29)

> *Summary: Verifies that calling a copy method on a configuration object creates a new instance with specified overrides while leaving the original object completely unchanged. It confirms that the copied object reflects the new values, and the source object retains its initial state.*


### test_create_returns_dashscope_client (function, L32-L36)

> *Summary: This test verifies that instantiating a configuration object with specific model and API key parameters successfully produces an instance of `DashScopeClient`. It confirms the correct type is returned upon calling the creation method on the configuration object.*


### test_defaults (function, L39-L45)

> *Summary: Verifies that a `DashScopeConfig` initialized with only a model name defaults to specific values, including a predefined base URL and `None` or `False` for API key, temperature, max tokens, and streaming status. This test ensures the configuration object behaves as expected when minimal parameters are provided.*


### test_base_url_can_be_overridden (function, L48-L50)

> *Summary: Verifies that the `DashScopeConfig` object correctly initializes and stores a provided base URL during instantiation. It asserts that the configured `base_url` matches the input value.*

