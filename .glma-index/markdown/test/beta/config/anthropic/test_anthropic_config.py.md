# test/beta/config/anthropic/test_anthropic_config.py

9 function(s): test_copy_without_overrides_returns_new_equal_instance, test_copy_applies_overrides_without_mutating_original, test_create_returns_anthropic_client, test_max_tokens_defaults_to_4096, test_max_tokens_can_be_overridden, test_extra_body_defaults_to_none, test_extra_body_can_be_set, test_extra_body_passed_to_client, test_copy_with_extra_body.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_copy_without_overrides_returns_new_equal_instance | function |  |
| test_copy_applies_overrides_without_mutating_original | function |  |
| test_create_returns_anthropic_client | function |  |
| test_max_tokens_defaults_to_4096 | function |  |
| test_max_tokens_can_be_overridden | function |  |
| test_extra_body_defaults_to_none | function |  |
| test_extra_body_can_be_set | function |  |
| test_extra_body_passed_to_client | function |  |
| test_copy_with_extra_body | function |  |

## Chunks

### test_copy_without_overrides_returns_new_equal_instance (function, L9-L15)

> *Summary: Verifies that calling the `copy()` method on an existing configuration object produces a new instance that is structurally equal to the original but is not the same object in memory. This confirms proper shallow or deep copying behavior without any overrides being applied.*


### test_copy_applies_overrides_without_mutating_original (function, L18-L31)

> *Summary: Verifies that calling the `copy()` method on a configuration object creates a new instance with specified overrides while leaving the original object completely unchanged. It tests setting different values for model, temperature, streaming status, and API key in the copied version against the originals.*


### test_create_returns_anthropic_client (function, L34-L38)

> *Summary: This test verifies that instantiating an `AnthropicConfig` with a model and API key successfully produces an object of type `AnthropicClient`. It confirms the configuration correctly initializes the client interface.*


### test_max_tokens_defaults_to_4096 (function, L41-L43)

> *Summary: Verifies that the `AnthropicConfig` object, when initialized with a specific model name, defaults its `max_tokens` attribute to 4096. This test confirms the expected default value for token limits in the configuration.*


### test_max_tokens_can_be_overridden (function, L46-L48)

> *Summary: Verifies that the `max_tokens` attribute of an `AnthropicConfig` instance correctly stores and reflects the provided value during initialization. It confirms the configuration object retains the specified token limit for a given model.*


### test_extra_body_defaults_to_none (function, L51-L53)

> *Summary: Verifies that the `extra_body` attribute defaults to `None` when initializing an `AnthropicConfig` instance with a specified model name. This test confirms the default state of this configuration field.*


### test_extra_body_can_be_set (function, L56-L60)

> *Summary: Verifies that an `AnthropicConfig` instance correctly stores and exposes a custom dictionary provided in the `extra_body` argument during initialization. It confirms the internal state matches the input configuration data.*


### test_extra_body_passed_to_client (function, L63-L69)

> *Summary: This test verifies that an optional `extra_body` dictionary provided during configuration is correctly passed to the underlying API client instance. It asserts that the created client object holds a reference to the input extra body.*


### test_copy_with_extra_body (function, L72-L79)

> *Summary: This test verifies that copying a configuration object with an additional body correctly merges the provided extras into the new instance while leaving the original unchanged. It confirms the `copy` method accepts and applies an optional `extra_body`.*

