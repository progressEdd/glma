# test/tools/experimental/tinyfish/test_tinyfish.py

1 class(es): TestTinyFishTool. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTinyFishTool | class |  |

## Chunks

### TestTinyFishTool (class, L13-L124)

> *Summary: This test suite validates the `TinyFishTool` class by checking its initialization logic, parameter validation against expected errors, and schema generation. It further verifies successful execution, error handling, and empty result scenarios when calling the underlying scraping function with mocked responses.*


### mock_response (method, L17-L26, parent: TestTinyFishTool)

> *Summary: Generates a mock object simulating a successful TinyFish API response, setting the status to "COMPLETED" and populating it with predefined company data. This fixture provides a predictable return value for testing purposes.*


### test_initialization (method, L29-L40, parent: TestTinyFishTool)

> *Summary: This test verifies the `TinyFishTool` initialization logic by checking two scenarios: when internal authentication is used, it asserts that providing no API key raises a `ValueError`; otherwise, it confirms the tool object is correctly instantiated with expected attributes and metadata.*


### test_tool_schema (method, L42-L63, parent: TestTinyFishTool)

> *Summary: Verifies that an instance of `TinyFishTool` generates a JSON schema matching the predefined structure for its scraping function. It asserts that the generated schema correctly defines the required parameters (`url` and `goal`) for the `tinyfish_scrape` tool.*


### test_parameter_validation (method, L71-L78, parent: TestTinyFishTool)

> *Summary: This test verifies that the `TinyFishTool` constructor raises a `ValueError` when provided with invalid initialization parameters. It asserts that the resulting exception message contains the expected error string after temporarily removing the API key environment variable.*


### test_execute_scrape_success (method, L81-L100, parent: TestTinyFishTool)

> *Summary: This test verifies that the `TinyFishTool` correctly processes a successful scrape operation by mocking the underlying execution to return predefined data. It asserts that the tool returns a dictionary containing the input URL and goal, along with the expected extracted company information from the mock response.*


### test_execute_scrape_error (method, L103-L113, parent: TestTinyFishTool)

> *Summary: When the underlying execution fails with an exception, this test verifies that the tool returns a dictionary containing the original URL and an error message detailing the failure. It confirms graceful error handling by asserting the structure and content of the returned error object.*


### test_execute_scrape_empty_result (method, L116-L124, parent: TestTinyFishTool)

> *Summary: When the underlying execution returns a "no\_result" status, this test verifies that the tool processes it correctly. It asserts the final output dictionary contains the expected `"no_result"` status within its data structure.*

