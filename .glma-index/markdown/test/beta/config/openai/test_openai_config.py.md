# test/beta/config/openai/test_openai_config.py

5 function(s): test_copy_without_overrides_returns_new_equal_instance, test_copy_applies_overrides_without_mutating_original, test_extra_body_defaults_to_none, test_extra_body_passed_to_create_options, test_copy_with_extra_body.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_copy_without_overrides_returns_new_equal_instance | function |  |
| test_copy_applies_overrides_without_mutating_original | function |  |
| test_extra_body_defaults_to_none | function |  |
| test_extra_body_passed_to_create_options | function |  |
| test_copy_with_extra_body | function |  |

## Chunks

### test_copy_without_overrides_returns_new_equal_instance (function, L8-L14)

> *Summary: Verifies that calling the `copy()` method on an existing configuration object produces a new instance that is structurally equal to the original but is not the same object in memory. This confirms proper shallow or deep copying behavior without any overrides applied.*


### test_copy_applies_overrides_without_mutating_original (function, L17-L30)

> *Summary: This test verifies that calling the `copy()` method on an `OpenAIConfig` instance creates a new configuration object with specified overrides, while leaving the original configuration completely unchanged. It asserts that the copied object reflects the provided overrides and that the source object retains its initial state.*


### test_extra_body_defaults_to_none (function, L33-L36)

> *Summary: Verifies that the `extra_body` attribute defaults to `None` when initializing an `OpenAIConfig` instance with a specified model. This test confirms the default state of optional request body data.*


### test_extra_body_passed_to_create_options (function, L39-L45)

> *Summary: This test verifies that an `extra_body` dictionary provided during configuration is correctly passed to the underlying API creation options when initializing the OpenAI client. It asserts that the received options contain the exact input body.*


### test_copy_with_extra_body (function, L48-L55)

> *Summary: This test verifies that the `copy` method correctly merges an optional dictionary into a new configuration instance. It asserts that the newly created copy retains the provided extra body while the original object's extra body remains unset.*

