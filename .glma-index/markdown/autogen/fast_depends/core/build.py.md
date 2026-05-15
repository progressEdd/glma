# autogen/fast_depends/core/build.py

1 function(s): build_call_model.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| build_call_model | function |  |

## Chunks

### build_call_model (function, L33-L206)

> *Summary: Constructs a `CallModel` by introspecting a callable to define its structure, dependencies, and return type. It processes parameters, resolving annotations for standard types, `Annotated` fields (which can include `Depends` or custom logic), and default values to build Pydantic models for inputs and outputs.*

