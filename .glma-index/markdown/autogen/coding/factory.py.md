# autogen/coding/factory.py

1 class(es): CodeExecutorFactory. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CodeExecutorFactory | class |  |

## Chunks

### CodeExecutorFactory (class, L14-L77)

> *Summary: This factory method constructs and returns a specific `CodeExecutor` instance based on configuration provided in an input dictionary. It supports creating executors like IPython, command-line local, YepCode, Remyx, or Daytona, falling back to a `ValueError` if the specified executor is unrecognized.*


### create (method, L18-L77, parent: CodeExecutorFactory)

> *Summary: Constructs a specific `CodeExecutor` instance based on the configuration provided in an input dictionary. It accepts configurations for various executors (like "ipython-embedded," "commandline-local," etc.) and returns the corresponding initialized executor, raising an error if the specified executor is unknown.*

