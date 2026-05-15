# test/agents/experimental/document_agent/test_parser_utils.py

1 class(es): TestDoclingParseDocs. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestDoclingParseDocs | class |  |

## Chunks

### TestDoclingParseDocs (class, L22-L233)

> *Summary: This test class verifies the functionality of a document parsing utility by mocking external dependencies like input handling and conversion results. It tests various scenarios, including error handling for missing documents or invalid paths, successful output generation in markdown/JSON formats, logging verification, and proper registration as an LLM tool within an AutoGen agent setup.*


### mock_document_input (method, L24-L27, parent: TestDoclingParseDocs)

> *Summary: Creates and returns a mocked `InputDocument` object, pre-setting its `file` attribute to a specific path string for testing purposes.*


### mock_conversion_result (method, L30-L38, parent: TestDoclingParseDocs)

> *Summary: Creates a mocked `ConversionResult` object configured to simulate document processing outcomes. It sets up the mock to return specific markdown, dictionary data, and an HTML table structure when its methods are called.*


### test_no_documents_found (method, L40-L44, parent: TestDoclingParseDocs)

> *Summary: Verifies that calling `docling_parse_docs` with no input documents results in a `ValueError` containing the message "No documents found." by mocking the document handling utility to return an empty list.*


### test_returns_iterator_of_conversion_results (method, L46-L61, parent: TestDoclingParseDocs)

> *Summary: Verifies that the parsing function yields an iterator of conversion results when provided with input and output paths. It mocks internal dependencies to ensure the returned collection contains path objects representing the conversion outcomes.*


### test_exports_converted_documents (method, L63-L99, parent: TestDoclingParseDocs)

> *Summary: Verifies that a document processing function correctly exports converted documents to a specified output directory, asserting the existence and specific content of generated Markdown and JSON files based on mocked conversion results. It takes an input path and output directory as inputs and confirms the resulting file structure and data integrity in the outputs.*


### test_logs_conversion_time_and_document_conversion_info (method, L101-L125, parent: TestDoclingParseDocs)

> *Summary: This test verifies that a document parsing function logs both the conversion duration and specific document processing details at the INFO level. It mocks input handling and document conversion results to assert the presence of expected log messages in the captured output.*


### test_handles_invalid_input_file_paths_and_output_directory_paths (method, L127-L137, parent: TestDoclingParseDocs)

> *Summary: Verifies that the parsing utility correctly throws a `ValueError` when given a non-existent input file path. It specifically tests this failure mode using an invalid file path while providing a valid output directory.*


### test_register_docling_parse_docs_as_a_tool (method, L139-L207, parent: TestDoclingParseDocs)

> *Summary: This test verifies that a specific parsing tool is correctly registered for both human-driven execution via `UserProxyAgent` and LLM invocation via `AssistantAgent`. It asserts the structure of the function definition provided to the assistant's configuration matches expectations.*


### test_default_output_dir_path (method, L209-L233, parent: TestDoclingParseDocs)

> *Summary: This test verifies that the parsing utility defaults to using `./output` as the output directory when no path is specified. It mocks input handling and document conversion, then asserts that `mkdir` was called for this default path and subsequent file operations use it.*

