# test/beta/config/anthropic/test_files.py

1 class(es): TestAnthropicFilesClient. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAnthropicFilesClient | class |  |

## Chunks

### TestAnthropicFilesClient (class, L15-L89)

> *Summary: This test suite verifies the functionality of an Anthropic file client by mocking the underlying `AsyncAnthropic` API calls. It asserts correct behavior for uploading, reading, listing, and deleting files, ensuring data transformation matches expected structures.*


### test_upload (method, L17-L37, parent: TestAnthropicFilesClient)

> *Summary: This test verifies the file upload functionality by mocking the Anthropic client and its `upload` method to return a predefined successful response. It asserts that the resulting `UploadedFile` object correctly captures the mocked file ID, filename, size, and creation timestamp from the API call.*


### test_read (method, L40-L51, parent: TestAnthropicFilesClient)

> *Summary: This test verifies the `read` functionality by mocking an Anthropic client to simulate file download and metadata retrieval. It asserts that the returned object correctly combines the downloaded content and retrieved metadata into a `FileContent` structure.*


### test_list (method, L54-L80, parent: TestAnthropicFilesClient)

> *Summary: This test verifies the file listing functionality by mocking an Anthropic client to return a specific list of files. It asserts that the resulting data is correctly transformed into a list of `UploadedFile` objects with accurate metadata.*


### test_delete (method, L83-L89, parent: TestAnthropicFilesClient)

> *Summary: This test verifies the deletion functionality by instantiating a client with provided configuration and calling its `delete` method with a specific file ID. It asserts that the underlying mock client's `beta.files.delete` method was called exactly once with the correct file identifier.*

