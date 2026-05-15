# test/beta/config/ollama/test_ollama_config.py

5 function(s): test_copy_without_overrides_returns_new_equal_instance, test_copy_applies_overrides_without_mutating_original, test_create_returns_ollama_client, test_defaults, test_host_can_be_overridden.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_copy_without_overrides_returns_new_equal_instance | function |  |
| test_copy_applies_overrides_without_mutating_original | function |  |
| test_create_returns_ollama_client | function |  |
| test_defaults | function |  |
| test_host_can_be_overridden | function |  |

## Chunks

### test_copy_without_overrides_returns_new_equal_instance (function, L9-L15)

> *Summary: Verifies that calling the `copy()` method on an existing configuration object produces a new instance that is structurally equal to the original but is not the same object in memory. This confirms proper shallow or deep copying behavior without any overrides applied.*


### test_copy_applies_overrides_without_mutating_original (function, L18-L29)

> *Summary: This test verifies that calling a copy method on an `OllamaConfig` object creates a new instance with specified overrides while leaving the original configuration completely unchanged. It asserts that the copied object reflects the new values, and the source object retains its initial state.*


### test_create_returns_ollama_client (function, L32-L36)

> *Summary: This test verifies that instantiating an `OllamaConfig` with a specified model and calling its `create()` method successfully returns an instance of `OllamaClient`. It confirms the correct type is returned upon client creation.*


### test_defaults (function, L39-L44)

> *Summary: Verifies that an `OllamaConfig` initialized with a specific model defaults to standard settings, including a local host address and disabled streaming. It confirms default values for temperature and token limits are unset (`None`).*


### test_host_can_be_overridden (function, L47-L49)

> *Summary: Verifies that the `OllamaConfig` object correctly stores a specified remote host URL when initialized with it. It asserts that the configured host matches the input value provided during instantiation.*

