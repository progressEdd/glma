# test/test_retrieve_utils.py

1 class(es): TestRetrieveUtils. 14 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestRetrieveUtils | class |  |

## Chunks

### TestRetrieveUtils (class, L40-L270)

> *Summary: Contains various unit tests for utility functions related to document retrieval and text processing. It verifies chunking logic (with overlap/mode checks), PDF extraction, file splitting from directories/URLs, vector database interaction with ChromaDB, URL validation, and HTML-to-Markdown conversion.*


### test_split_text_to_chunks (method, L41-L44, parent: TestRetrieveUtils)

> *Summary: This test verifies that a given long string is correctly segmented into smaller pieces. It asserts that every resulting chunk adheres to the specified maximum token limit of 1000.*


### test_split_text_to_chunks_raises_on_invalid_chunk_mode (method, L46-L48, parent: TestRetrieveUtils)

> *Summary: Asserts that calling the text splitting utility with an unrecognized `chunk_mode` raises an `AssertionError`. It tests this behavior by passing a sample string and an invalid mode string to the function.*


### test_split_text_to_chunks_overlapping (method, L50-L60, parent: TestRetrieveUtils)

> *Summary: This test verifies the `split_text_to_chunks` utility by asserting correct text segmentation for both overlapping and non-overlapping scenarios. It takes a long string as input and confirms the resulting list of chunks matches expected outputs based on specified token limits and overlap values.*


### test_extract_text_from_pdf (method, L62-L64, parent: TestRetrieveUtils)

> *Summary: This test verifies that the `extract_text_from_pdf` function correctly retrieves text from a specified PDF file path. It asserts equality between the expected text and the stripped, space-normalized output returned by the extraction utility.*


### test_split_files_to_chunks (method, L66-L73, parent: TestRetrieveUtils)

> *Summary: This test verifies that a function correctly splits provided file paths (PDF and TXT) into string chunks. It asserts that every resulting chunk contains the specific phrase "AutoGen is an advanced tool designed to assist developers".*


### test_get_files_from_dir (method, L75-L103, parent: TestRetrieveUtils)

> *Summary: This test verifies the `get_files_from_dir` utility by asserting its correct behavior when provided with directories, lists of paths (including local and remote URLs), and specific file type filters. It confirms that the function returns valid file paths based on the input configuration.*


### test_is_url (method, L105-L107, parent: TestRetrieveUtils)

> *Summary: This test verifies the `is_url` function by asserting that a valid URL string returns true, while an invalid string returns false. It confirms the function correctly distinguishes between well-formed and malformed URLs.*


### test_create_vector_db_from_dir (method, L109-L117, parent: TestRetrieveUtils)

> *Summary: This test verifies the creation of a ChromaDB vector store from a specified directory if it doesn't already exist at a given path. It initializes or retrieves a persistent client and asserts that the "all-my-documents" collection is present in the database.*


### test_query_vector_db (method, L119-L128, parent: TestRetrieveUtils)

> *Summary: This test verifies the functionality of querying a ChromaDB vector store. It initializes or loads a persistent database, then queries it with the input "autogen" and asserts that the returned results are a dictionary containing documents mentioning "autogen".*


### test_custom_vector_db (method, L134-L194, parent: TestRetrieveUtils)

> *Summary: Tests the functionality of a custom agent proxy that interfaces with LanceDB for retrieval. It initializes a local vector database, then calls `retrieve_docs` to query it using a specific vector and filter string, asserting the returned document IDs match expected results.*


### test_custom_text_split_function (method, L196-L214, parent: TestRetrieveUtils)

> *Summary: This test verifies a custom text splitting utility by creating a ChromaDB collection from a file using a function that splits input text exactly in half. It then queries this database and asserts that the retrieved document contains specific expected content related to "AutoGen."*


### test_retrieve_utils (method, L216-L235, parent: TestRetrieveUtils)

> *Summary: This test verifies the functionality of vector database retrieval by first creating a ChromaDB collection from local documentation files. It then queries this collection with a specific text prompt and asserts that the returned results contain at least one matching ID.*


### test_unstructured (method, L241-L249, parent: TestRetrieveUtils)

> *Summary: This test verifies that a list of file paths (PDF, TXT, DOCX) correctly yields string chunks containing specific text content after being processed by `split_files_to_chunks`. It asserts that every resulting chunk is a string and includes the phrase "AutoGen is an advanced tool designed to assist developers".*


### test_parse_html_to_markdown (method, L251-L270, parent: TestRetrieveUtils)

> *Summary: Tests the `parse_html_to_markdown` utility by providing a sample HTML string as input. It asserts that the function correctly converts this HTML into a specific expected Markdown format.*

