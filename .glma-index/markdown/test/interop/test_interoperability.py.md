# test/interop/test_interoperability.py

1 class(es): TestInteroperability. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestInteroperability | class |  |

## Chunks

### TestInteroperability (class, L19-L70)

> *Summary: Verifies the supported interoperability types based on the current Python version, and tests the conversion of a `crewai` tool into an interoperable format. It also checks that attempting to retrieve an unsupported type raises a specific `ValueError`.*


### test_supported_types (method, L20-L30, parent: TestInteroperability)

> *Summary: This test verifies the list of supported types returned by `Interoperability.get_supported_types()` against expected values based on the current Python version. It asserts different sets of supported types depending on whether the interpreter is running Python 3.9-3.10, 3.10-3.12, or 3.13+.*


### test_crewai (method, L36-L55, parent: TestInteroperability)

> *Summary: This test verifies the interoperability conversion of a `FileReadTool` from CrewAI format to a standardized tool structure. It mocks the OpenAI API key, creates a temporary file, and asserts that the converted tool correctly reads and returns the content of that file when executed with the appropriate arguments.*


### test_unsupported_type_error_message (method, L57-L65, parent: TestInteroperability)

> *Summary: This test verifies that when an unsupported type is requested via the `Interoperability` class, a `ValueError` is raised containing the name of one of the supported types from the mocked registry. It ensures the error message correctly references the available options.*


### test_langchain (method, L69-L70, parent: TestInteroperability)

> *Summary: This method currently serves as a placeholder for testing LangChain interoperability. It explicitly raises a `NotImplementedError`, indicating that the actual test logic has not been written yet.*

