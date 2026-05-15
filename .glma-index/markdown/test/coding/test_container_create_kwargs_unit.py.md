# test/coding/test_container_create_kwargs_unit.py

1 function(s): test_container_create_kwargs_merge_logic.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_container_create_kwargs_merge_logic | function |  |

## Chunks

### test_container_create_kwargs_merge_logic (function, L21-L50)

> *Summary: This test verifies that user-provided keyword arguments for container creation are passed directly and unmodified to the underlying Docker client's `create` method. It mocks the Docker SDK interaction to assert that specific environment variables and entrypoints reach the expected API call.*

