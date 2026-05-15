# test/fast_depends/test_params.py

2 function(s): test_params, test_args_kwargs_params.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_params | function |  |
| test_args_kwargs_params | function |  |

## Chunks

### test_params (function, L13-L28)

> *Summary: This test constructs a call model by injecting dependencies into a main function, asserting that the resulting parameters correctly reflect both direct inputs and resolved dependency values. It verifies the structure of the input parameters (`params`) versus the fully flattened set of required arguments (`flat_params`).*


### test_args_kwargs_params (function, L31-L58)

> *Summary: This test verifies how a model builder correctly identifies parameters from function signatures, including positional arguments (`*args`), keyword arguments (`**kwargs`), and dependencies. It asserts that the resulting parameter sets accurately reflect both the direct signature names and all resolved dependency names.*

