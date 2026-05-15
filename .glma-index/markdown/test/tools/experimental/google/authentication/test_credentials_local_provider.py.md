# test/tools/experimental/google/authentication/test_credentials_local_provider.py

1 class(es): TestGoogleCredentialsLocalProvider. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestGoogleCredentialsLocalProvider | class |  |

## Chunks

### TestGoogleCredentialsLocalProvider (class, L29-L88)

> *Summary: This test suite verifies the functionality of a local provider for Google credentials, ensuring correct initialization and credential retrieval from mocked sources. It also includes an end-to-end test that uses real credentials to interact with the Google Sheets API.*


### test_init (method, L30-L37, parent: TestGoogleCredentialsLocalProvider)

> *Summary: This test verifies the initialization of a local credentials provider using a provided client secret file and specific scopes. It asserts that the resulting object is an instance of `GoogleCredentialsProvider` and correctly sets its host to "localhost" and port to 8080.*


### test_get_credentials_from_db (method, L39-L57, parent: TestGoogleCredentialsLocalProvider)

> *Summary: This test verifies that retrieving credentials from the database mechanism correctly returns a mocked credential object when using a local Google provider configured with a client secret file. It asserts that the underlying refresh/get method was called exactly once and that the returned value matches the mock setup.*


### test_end2end (method, L60-L88, parent: TestGoogleCredentialsLocalProvider)

> *Summary: This test method demonstrates basic Sheets API usage by obtaining credentials from a local client secret file and then fetching all data within a specified range of a sample spreadsheet. It executes the read operation and prints each retrieved row to standard output if data is present.*

