# autogen/mcp/mcp_proxy/fastapi_code_generator_helpers.py

1 function(s): patch_get_parameter_type.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| patch_get_parameter_type | function |  |

## Chunks

### patch_get_parameter_type (function, L24-L62)

> *Summary: This patch modifies the `OpenAPIParser` to inject parameter descriptions into generated arguments by wrapping the original argument with a custom class that incorporates the description from the input parameters object. It temporarily overrides and restores the `get_parameter_type` method during execution.*

