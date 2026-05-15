# test/tools/experimental/google/drive/test_toolkit.py

1 class(es): TestGoogleDriveToolkit. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGoogleDriveToolkit | class |  |

## Chunks

### TestGoogleDriveToolkit (class, L32-L76)

> *Summary: This test suite verifies the functionality of `GoogleDriveToolkit` by mocking its initialization and performing an end-to-end integration test. The tests ensure correct construction using mock credentials and validate that the toolkit can successfully interact with a simulated Google Drive environment during chat execution.*


### test_init (method, L33-L46, parent: TestGoogleDriveToolkit)

> *Summary: This test verifies the initialization of a `GoogleDriveToolkit` instance by mocking its build dependency. It asserts that the toolkit is correctly instantiated as a `Toolkit`, has a specific length (2), and that the underlying build function was called exactly once during setup.*


### test_end2end (method, L50-L76, parent: TestGoogleDriveToolkit)

> *Summary: This test simulates an end-to-end workflow by setting up a `UserProxyAgent` and an `AssistantAgent`. It initializes a `GoogleDriveToolkit` using local credentials to allow the assistant to download all files from a specified Google Drive folder via a chat interaction.*

