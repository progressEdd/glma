# test/beta/events/test_document_input.py

2 function(s): test_url_returns_document_url_input, test_no_args_raises. 3 class(es): TestFileId, TestData, TestPath. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_url_returns_document_url_input | function |  |
| TestFileId | class |  |
| TestData | class |  |
| TestPath | class |  |
| test_no_args_raises | function |  |

## Chunks

### test_url_returns_document_url_input (function, L12-L16)

> *Summary: When provided a URL string as input to `DocumentInput`, it returns an object of type `UrlInput` that retains the original URL value. This test verifies that the input is correctly wrapped and preserved in the output structure.*


### TestFileId (class, L19-L32)

> *Summary: This test suite verifies the `DocumentInput` constructor's behavior when initializing file identifiers. It confirms that providing a `file_id` results in a `FileIdInput`, and correctly sets both `file_id` and an optional `filename`.*


### test_returns_document_file_id_input (method, L20-L25, parent: TestFileId)

> *Summary: When initialized with a `file_id` string, this method creates an instance of `FileIdInput`, asserting that the resulting object is of the correct type and holds the provided ID while having no filename.*


### test_with_filename (method, L27-L32, parent: TestFileId)

> *Summary: This test verifies that instantiating `DocumentInput` with a file ID and filename correctly produces an object of type `FileIdInput`, while also asserting the correct storage of both input parameters.*


### TestData (class, L35-L45)

> *Summary: This class contains tests verifying the `DocumentInput` constructor's behavior. It asserts that providing binary data and a media type results in a `BinaryInput` object with correct values, while also confirming that omitting the media type raises a `ValueError`.*


### test_returns_binary_input (method, L36-L41, parent: TestData)

> *Summary: This test verifies that the `DocumentInput` constructor correctly wraps binary data and a media type into a `BinaryInput` object. It asserts that the resulting object is of type `BinaryInput` and retains the original byte string and MIME type.*


### test_missing_media_type_raises (method, L43-L45, parent: TestData)

> *Summary: Asserts that instantiating `DocumentInput` with raw byte data lacking a specified media type raises a `ValueError`. This test verifies the input validation mechanism for document processing.*


### TestPath (class, L48-L98)

> *Summary: These tests verify the `DocumentInput` constructor's ability to infer file types from paths, handling specific formats like PDF, CSV, and DOCX based on extensions. It also confirms error handling for unknown extensions and allows overriding type inference by accepting an explicit media type or a string path.*


### test_infers_pdf (method, L49-L58, parent: TestPath)

> *Summary: When provided with a PDF file path, this test verifies that the `DocumentInput` object correctly identifies it as binary data, extracts the raw bytes, and sets the appropriate MIME type and filename metadata. It confirms the resulting input object inherits from `BinaryInput`.*


### test_infers_csv (method, L60-L66, parent: TestPath)

> *Summary: This test verifies that the `DocumentInput` object correctly infers the media type as `"text/csv"` when initialized with a file containing CSV data. It achieves this by writing sample CSV content to a temporary file and passing its path to the constructor.*


### test_infers_docx (method, L68-L74, parent: TestPath)

> *Summary: When provided with a file path pointing to a `.docx` file, the input object correctly infers and sets its media type to the standard OpenXML document format. This test verifies that the `DocumentInput` constructor accurately identifies Word documents based on the file content or extension.*


### test_unknown_extension_raises (method, L76-L81, parent: TestPath)

> *Summary: This test verifies that attempting to process a file with an unrecognized extension raises a `ValueError` containing the message "Cannot infer". It achieves this by creating a temporary file named "file.xyz" and passing its path to the `DocumentInput` constructor.*


### test_unknown_extension_with_explicit_media_type (method, L83-L90, parent: TestPath)

> *Summary: When provided a file with an unknown extension but an explicit `application/pdf` media type, the input object is correctly instantiated as a `BinaryInput`, preserving the specified media type.*


### test_accepts_string_path (method, L92-L98, parent: TestPath)

> *Summary: This test verifies that the `DocumentInput` constructor correctly processes a file path provided as a string input. It asserts that when initialized with a valid markdown file path, the resulting object has the expected `"text/markdown"` media type.*


### test_no_args_raises (function, L101-L103)

> *Summary: Asserts that instantiating the `DocumentInput` class without any arguments raises a `ValueError` containing the specific message "requires one of". This verifies the constructor enforces required input parameters.*

