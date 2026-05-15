# autogen/events/helpers.py

1 function(s): deprecated_by.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| deprecated_by | function |  |

## Chunks

### deprecated_by (function, L13-L44)

> *Summary: This function generates a decorator that marks an old model as deprecated in favor of a newer one. It intercepts calls to the decorated (old) class, logs a warning, translates input parameters using a provided map, applies default values, and finally instantiates and returns an instance of the new class.*

