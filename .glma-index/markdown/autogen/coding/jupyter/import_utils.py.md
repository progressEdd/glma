# autogen/coding/jupyter/import_utils.py

3 function(s): is_jupyter_kernel_gateway_installed, require_jupyter_kernel_gateway_installed, skip_on_missing_jupyter_kernel_gateway.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| is_jupyter_kernel_gateway_installed | function |  |
| require_jupyter_kernel_gateway_installed | function |  |
| skip_on_missing_jupyter_kernel_gateway | function |  |

## Chunks

### is_jupyter_kernel_gateway_installed (function, L19-L32)

> *Summary: Determines if the `jupyter-kernel-gateway` package is available by attempting to run its version command via subprocess. Returns `True` if the command executes successfully, and logs a warning while returning `False` otherwise.*


### require_jupyter_kernel_gateway_installed (function, L38-L56)

> *Summary: This function returns a decorator that conditionally wraps another function based on the presence of `jupyter-kernel-gateway`. If the dependency is present, it passes the original function through; otherwise, it patches the function to raise an error upon execution if the required module is missing.*


### skip_on_missing_jupyter_kernel_gateway (function, L59-L82)

> *Summary: This function returns a decorator that conditionally skips tests based on the presence of the `jupyter-kernel-gateway` module. If the gateway is installed, it applies a specific executor marker; otherwise, it wraps the decorated test with a skip marker providing installation instructions.*

