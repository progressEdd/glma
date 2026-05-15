# test/agents/experimental/document_agent/test_document_utils.py

2 class(es): TestIsUrl, TestDownloadUrl. 29 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestIsUrl | class |  |
| TestDownloadUrl | class |  |

## Chunks

### TestIsUrl (class, L24-L55)

> *Summary: This test suite verifies the `is_url` utility function by asserting correct boolean outputs for various string inputs. It checks cases including valid URLs, malformed strings (missing schemes or network locations), empty/null inputs, and those containing special characters or surrounding whitespace.*


### test_valid_url (method, L25-L27, parent: TestIsUrl)

> *Summary: Verifies that a string containing a standard URL format passes the `is_url` validation function, asserting its truthiness for a known valid input.*


### test_invalid_url_without_scheme (method, L29-L31, parent: TestIsUrl)

> *Summary: Verifies that a string lacking a URL scheme (like `http://`) is correctly identified as invalid by the `is_url` utility function. It asserts that the input `"www.example.com"` returns `False`.*


### test_invalid_url_without_network_location (method, L33-L35, parent: TestIsUrl)

> *Summary: Asserts that a string consisting only of the protocol prefix (`"https://"`) fails validation when checking for a complete URL structure. This test verifies the `is_url` function's behavior with incomplete inputs lacking network location information.*


### test_url_with_invalid_scheme (method, L37-L39, parent: TestIsUrl)

> *Summary: Verifies that a URL string lacking a valid scheme (like `http` or `https`) correctly fails the `is_url` validation check, asserting a `False` return value for the input.*


### test_empty_url_string (method, L41-L43, parent: TestIsUrl)

> *Summary: Verifies that an empty string input fails the URL validation check. It asserts that `is_url("")` returns false for an empty string.*


### test_url_string_with_whitespace (method, L45-L47, parent: TestIsUrl)

> *Summary: Verifies that the `is_url` function correctly identifies a string containing leading and trailing whitespace as a valid URL. It takes a whitespace-padded URL string as input and asserts the output is true.*


### test_url_string_with_special_characters (method, L49-L51, parent: TestIsUrl)

> *Summary: Verifies that a string containing various URL components, including query parameters and fragments, is correctly identified as a valid URL by the `is_url` function. It takes a specific complex URL string as input and asserts the boolean output of the validation check.*


### test_attribute_error (method, L53-L55, parent: TestIsUrl)

> *Summary: Verifies that the `is_url` utility correctly returns false when provided with a `None` input. This test ensures proper handling of null values within URL validation logic.*


### TestDownloadUrl (class, L58-L198)

> *Summary: This test suite verifies the functionality of URL downloading and file handling utilities. It tests various scenarios for fetching content from URLs (valid, invalid, different types) using mocked browser interactions, as well as validating functions that list or process local files given a directory or single file path.*


### _disable_ssrf_guard (method, L60-L63, parent: TestDownloadUrl)

> *Summary: This method temporarily bypasses URL validation checks by patching two specific functions to return `None`. It accepts a `pytest.MonkeyPatch` object to perform the attribute replacement during testing.*


### mock_chrome (method, L66-L68, parent: TestDownloadUrl)

> *Summary: This method yields a mocked version of `selenium.webdriver.Chrome` by patching the actual class, allowing tests to control browser interactions without launching a real instance.*


### mock_chrome_driver_manager (method, L71-L73, parent: TestDownloadUrl)

> *Summary: This method yields a mocked version of `webdriver_manager.chrome.ChromeDriverManager.install` by patching it, allowing tests to control the installation process without actual network calls. It returns an iterable containing this mock object for inspection during testing.*


### test_non_string_input (method, L76-L79, parent: TestDownloadUrl)

> *Summary: This test verifies that passing a non-string input (an integer `123`) to the `download_url` function correctly raises an `InvalidArgumentException` from Selenium. It confirms the utility handles invalid data types as expected by asserting the specific exception and message.*


### test_download_with_valid_url (method, L82-L88, parent: TestDownloadUrl)

> *Summary: This test verifies the `_download_rendered_html` utility by simulating a successful HTTP request to a valid URL. It asserts that the function returns a non-empty string containing the rendered HTML content from the mocked browser interaction.*


### test_download_with_invalid_url (method, L91-L95, parent: TestDownloadUrl)

> *Summary: This test verifies that attempting to download content using an invalid URL raises a `ValueError`. It mocks the browser's GET request to simulate this failure and asserts that the expected exception is caught.*


### test_chrome_driver_not_installed (method, L98-L102, parent: TestDownloadUrl)

> *Summary: This test verifies that the `_download_rendered_html` utility correctly raises a `ValueError` when the mock driver manager simulates a missing Chrome driver for a given URL. It asserts that the expected error message is caught during execution.*


### test_chrome_driver_connection_error (method, L105-L109, parent: TestDownloadUrl)

> *Summary: This test verifies that the `_download_rendered_html` utility correctly raises a `ValueError` when the underlying Chrome driver connection fails during an HTTP GET request to a specified URL. It achieves this by mocking the browser's `get` method to intentionally throw a "Connection error."*


### mock_html_value (method, L112-L113, parent: TestDownloadUrl)

> *Summary: Provides a hardcoded string representing an HTML document for testing purposes. This method returns the fixed string `"<html>Example</html>"`.*


### mock_download (method, L116-L119, parent: TestDownloadUrl)

> *Summary: This method simulates an HTML download by patching the actual `_download_rendered_html` function to return a specified string value. It yields the mocked object, allowing tests to assert interactions with the simulated download process.*


### mock_open_file (method, L122-L124, parent: TestDownloadUrl)

> *Summary: This method patches the built-in `open` function to return a mock file object. It yields this mock object, allowing tests to simulate file operations without actual disk I/O.*


### test_download_url_valid_html (method, L127-L133, parent: TestDownloadUrl)

> *Summary: This test verifies that the `download_url` function correctly saves HTML content to a file with the `.html` extension. It asserts that the resulting file's content matches the provided mocked HTML string.*


### test_download_url_non_html (method, L136-L140, parent: TestDownloadUrl)

> *Summary: This test verifies that the `download_url` utility correctly saves a non-HTML resource, specifically an image from a provided URL, and assigns it the appropriate `.jpg` extension in the temporary directory.*


### test_download_url_no_extension (method, L143-L149, parent: TestDownloadUrl)

> *Summary: This test verifies that a provided URL without an extension is correctly downloaded and saved to a file with a `.html` suffix, asserting the resulting content matches the expected HTML value. It takes mocked HTML content and download paths as inputs to confirm the correct file creation and content integrity.*


### test_download_url_no_output_dir (method, L152-L160, parent: TestDownloadUrl)

> *Summary: This test verifies that the `download_url` function correctly generates a file path with an `.html` suffix when no output directory is specified. It further asserts that the resulting file handle is opened in write mode and subsequently written to with the provided HTML content.*


### test_download_url_invalid_url (method, L163-L170, parent: TestDownloadUrl)

> *Summary: This test verifies that the `download_url` function correctly raises an exception when provided with an invalid URL string. It mocks the underlying HTML download utility to simulate a failure and asserts that the expected exception is caught.*


### path_with_two_files (method, L173-L179, parent: TestDownloadUrl)

> *Summary: Creates two distinct text files within a provided temporary directory and writes specific content to each. It then returns the original temporary path containing both newly created files.*


### test_list_files (method, L181-L183, parent: TestDownloadUrl)

> *Summary: This test verifies that a utility function correctly returns a list of filenames present within a specified directory path. It asserts that the returned set of file paths matches the expected files ("file1.txt" and "file2.txt") inside the input directory.*


### test_handle_input_directory (method, L185-L187, parent: TestDownloadUrl)

> *Summary: This test verifies that the `handle_input` function correctly identifies all expected files within a given input directory path. It asserts that the returned list of file paths matches the predefined set of two specific files.*


### test_handle_input_file (method, L189-L194, parent: TestDownloadUrl)

> *Summary: This test verifies that the `handle_input` utility correctly processes a single input file path provided as a string. It writes content to a temporary file and asserts that the function returns a list containing only that specific file object.*


### test_handle_input_invalid_input (method, L196-L198, parent: TestDownloadUrl)

> *Summary: Asserts that passing a non-standard string like "invalid input" to the `handle_input` function raises a `ValueError`. This verifies the input validation mechanism for the document agent's utility functions.*

