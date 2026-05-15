# test/oai/test_client_utils.py

2 function(s): test_validate_parameter, test_should_hide_tools.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_validate_parameter | function |  |
| test_should_hide_tools | function |  |

## Chunks

### test_validate_parameter (function, L14-L140)

> *Summary: This test suite verifies the `validate_parameter` function's behavior across various scenarios. It asserts that the function correctly validates input parameters against specified types and bounds, returning the original value if valid, applying defaults or rejecting values otherwise.*


### test_should_hide_tools (function, L143-L313)

> *Summary: This test verifies the logic of a function that determines whether to hide available tools based on message history and specified conditions. It inputs conversation histories (with or without tool calls) and a list of defined tools, returning `True` or `False` according to rules like "if\_all\_run" or "if\_any\_run".*

