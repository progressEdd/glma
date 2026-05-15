# autogen/interop/langchain/langchain_tool.py

1 class(es): LangChainInteroperability. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LangChainInteroperability | class |  |

## Chunks

### LangChainInteroperability (class, L20-L78)

> *Summary: This class provides a mechanism to convert an instance of a LangChain tool into a standardized `Tool` object. It accepts any input that is a `LangchainTool`, extracts its name and description, wraps its execution logic in a function, and returns the compatible `Tool`.*


### convert_tool (method, L31-L66, parent: LangChainInteroperability)

> *Summary: This method transforms a `LangchainTool` instance into a standardized `Tool` object by extracting its name and description. It wraps the original tool's execution logic within a new function that accepts structured input from the target `Tool`.*


### get_unsupported_reason (method, L69-L78, parent: LangChainInteroperability)

> *Summary: Checks if the necessary LangChain components are available by attempting an optional import. If the import fails, it returns a specific installation instruction string; otherwise, it returns `None`.*

