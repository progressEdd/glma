# autogen/beta/tools/tool.py

1 class(es): Tool. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Tool | class |  |

## Chunks

### Tool (class, L17-L31)

> *Summary: Defines an abstract base class for tools that must implement methods to set a provider and asynchronously return schema definitions based on a given context. It also provides a registration mechanism accepting middleware and context.*


### set_provider (method, L20-L21, parent: Tool)

> *Summary: This method accepts a `Provider` object and sets it as the current service provider for the instance. It modifies the internal state to use the provided implementation.*


### schemas (method, L23-L23, parent: Tool)

> *Summary: Retrieves a collection of `ToolSchema` objects based on the provided execution context. This method yields all available tool definitions for use within the system.*


### register (method, L25-L31, parent: Tool)

> *Summary: This method registers middleware components onto a provided stack and context. It accepts an iterable of middleware instances to apply during execution.*

