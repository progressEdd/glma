# test/beta/config/gemini/test_files.py

1 class(es): TestGeminiFilesClient. 6 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGeminiFilesClient | class |  |

## Chunks

### TestGeminiFilesClient (class, L15-L122)

> *Summary: This test suite verifies the functionality of a client interacting with Gemini's file service by mocking the underlying API calls. It tests operations like uploading files (handling known and unknown MIME types), reading downloadable content, listing existing files, and deleting files, asserting correct inputs and outputs against mocked responses.*


### test_upload (method, L17-L38, parent: TestGeminiFilesClient)

> *Summary: This test verifies the file upload functionality by mocking the Gemini API client and its upload method. It asserts that calling `upload` with audio data correctly returns an `UploadedFile` object containing the expected metadata, while also confirming the correct configuration arguments were passed to the underlying API call.*


### test_upload_unknown_mime_falls_back_to_octet_stream (method, L41-L54, parent: TestGeminiFilesClient)

> *Summary: This test verifies that when an unknown MIME type is provided during file upload, the system correctly defaults to using `application/octet-stream`. It asserts that the underlying client's upload method receives configuration specifying this fallback MIME type.*


### test_read_downloadable (method, L57-L70, parent: TestGeminiFilesClient)

> *Summary: This test verifies the retrieval of content from a mock Gemini file service. It simulates fetching metadata and then downloading binary data, asserting that the returned object correctly contains the filename, downloaded bytes, and MIME type.*


### test_read_uploaded_raises (method, L73-L84, parent: TestGeminiFilesClient)

> *Summary: This test verifies that attempting to read a user-uploaded file via the `GeminiFilesClient` raises a `NotImplementedError`. It mocks the underlying client to simulate fetching a file object without providing a download URI.*


### test_list (method, L87-L113, parent: TestGeminiFilesClient)

> *Summary: This test verifies the `list` method of a Gemini file client by mocking the underlying API calls to return a specific list of files. It asserts that the returned data is correctly transformed into a list of `UploadedFile` objects with accurate metadata.*


### test_delete (method, L116-L122, parent: TestGeminiFilesClient)

> *Summary: This test verifies the deletion functionality by instantiating a client with provided configuration and calling its `delete` method for a specific file path. It asserts that the underlying mock client's asynchronous delete function was called exactly once with the expected file name.*

