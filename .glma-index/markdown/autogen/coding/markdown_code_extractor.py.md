# autogen/coding/markdown_code_extractor.py

1 class(es): MarkdownCodeExtractor. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MarkdownCodeExtractor | class |  |

## Chunks

### MarkdownCodeExtractor (class, L18-L44)

> *Summary: This utility parses a message input (string or content parts) to find and extract Markdown-formatted code blocks. It returns a list of `CodeBlock` objects, automatically inferring the programming language if none is specified in the markdown syntax.*


### extract_code_blocks (method, L21-L44, parent: MarkdownCodeExtractor)

> *Summary: Parses a message string or content parts to find and extract structured code blocks using a regex pattern. It returns a list of `CodeBlock` objects, inferring the programming language if it's not explicitly provided in the input.*

