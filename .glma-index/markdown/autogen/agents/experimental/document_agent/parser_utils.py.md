# autogen/agents/experimental/document_agent/parser_utils.py

1 function(s): docling_parse_docs.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| docling_parse_docs | function |  |

## Chunks

### docling_parse_docs (function, L33-L134)

> *Summary: Converts various document types (PDF, DOCX, etc.) into a structured Deep Search format using EasyOCR for PDF processing, while explicitly disabling GPU usage. It takes an input file path and optional output settings, returning a list of paths to the generated Markdown or JSON files, alongside exporting tables as HTML if requested.*

