# autogen/beta/config/config.py

1 class(es): ModelConfig. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ModelConfig | class |  |

## Chunks

### ModelConfig (class, L15-L21)

> *Summary: Defines a protocol requiring implementations to provide methods for cloning the configuration, instantiating an `LLMClient`, and optionally creating a `FilesClient`. It enforces that any conforming type must define these specific interface behaviors.*


### copy (method, L16-L16, parent: ModelConfig)

> *Summary: Creates a shallow copy of the current configuration object, allowing for independent modification of settings without affecting the original instance.*


### create (method, L18-L18, parent: ModelConfig)

> *Summary: Instantiates and returns a new `LLMClient` object based on the configuration of the current instance. This method is responsible for setting up the necessary client connection or structure.*


### create_files_client (method, L20-L21, parent: ModelConfig)

> *Summary: This method raises an error if the current object type doesn't implement file client functionality. It serves as a placeholder to enforce that subclasses must provide their own implementation for creating files.*

