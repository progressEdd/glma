# test/cache/test_in_memory_cache.py

8 function(s): test_prefixed_key, test_get_with_default_value, test_get_without_default_value, test_get_with_set_value, test_get_with_set_value_and_seed, test_set, test_set_with_seed, test_context_manager.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_prefixed_key | function |  |
| test_get_with_default_value | function |  |
| test_get_without_default_value | function |  |
| test_get_with_set_value | function |  |
| test_get_with_set_value_and_seed | function |  |
| test_set | function |  |
| test_set_with_seed | function |  |
| test_context_manager | function |  |

## Chunks

### test_prefixed_key (function, L10-L12)

> *Summary: This test verifies that the `InMemoryCache` correctly prepends a specified seed to input keys. It asserts that calling `_prefixed_key` with `"key"` on an initialized cache returns `"test_key"`.*


### test_get_with_default_value (function, L15-L17)

> *Summary: Verifies that retrieving a non-existent key from the in-memory cache returns the specified default value. It initializes an `InMemoryCache` and asserts the result of calling `.get()` with a missing key and a fallback string.*


### test_get_without_default_value (function, L20-L22)

> *Summary: Verifies that retrieving a non-existent key from the in-memory cache returns `None`. It initializes an instance of `InMemoryCache` and asserts the result of calling `.get()` with a missing key.*


### test_get_with_set_value (function, L25-L28)

> *Summary: This test verifies that an in-memory cache correctly stores and retrieves a value. It initializes the cache, sets a key-value pair, and asserts that retrieving the key returns the exact stored value.*


### test_get_with_set_value_and_seed (function, L31-L34)

> *Summary: This test verifies that an in-memory cache correctly stores and retrieves a value using a specific seed for initialization. It sets a key-value pair and asserts the retrieved value matches the stored input.*


### test_set (function, L37-L40)

> *Summary: This test verifies the `set` operation of an in-memory cache by initializing it, storing a key-value pair, and asserting that the internal storage reflects the correct value.*


### test_set_with_seed (function, L43-L46)

> *Summary: This test verifies that an `InMemoryCache` correctly stores data when initialized with a specific seed. It sets a key-value pair and asserts the value is retrievable using a derived internal key.*


### test_context_manager (function, L49-L52)

> *Summary: This test verifies the functionality of an in-memory cache by using it within a context manager. It sets a key-value pair and then asserts that retrieving the same key returns the stored value.*

