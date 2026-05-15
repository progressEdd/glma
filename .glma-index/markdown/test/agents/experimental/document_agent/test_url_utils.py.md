# test/agents/experimental/document_agent/test_url_utils.py

4 class(es): TestValidateUrl, TestAnalyzerSSRFGuard, TestFormatMapping, TestURLAnalyzer. 38 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestValidateUrl | class |  |
| TestAnalyzerSSRFGuard | class |  |
| TestFormatMapping | class |  |
| TestURLAnalyzer | class |  |

## Chunks

### TestValidateUrl (class, L19-L105)

> *Summary: This test suite validates a URL sanitization function by mocking DNS resolution to control IP addresses returned for given hosts. It asserts that the function correctly allows public URLs while rejecting those using disallowed schemes, private/loopback IPs, or when hostname resolution yields mixed public and non-public IPs.*


### _resolve_public (method, L21-L25, parent: TestValidateUrl)

> *Summary: This method mocks the `socket.getaddrinfo` function using `pytest.MonkeyPatch`. It forces any DNS resolution request to return a hardcoded IP address (`93.184.216.34`), simulating a public endpoint for testing purposes.*


### test_https_public_ok (method, L27-L28, parent: TestValidateUrl)

> *Summary: This test verifies that a specific HTTPS URL, `https://example.com/file.pdf`, is correctly validated by the `validate_url` function. It asserts successful validation for a standard public document link.*


### test_http_public_ok (method, L30-L31, parent: TestValidateUrl)

> *Summary: This test verifies that a specific URL string, "http://example.com/file.pdf", passes validation using the `validate_url` function. It confirms the utility correctly handles standard HTTP public URLs.*


### test_url_with_whitespace_is_stripped (method, L33-L34, parent: TestValidateUrl)

> *Summary: This test verifies that the `validate_url` function correctly strips leading and trailing whitespace from a provided URL string, ensuring only valid URLs pass validation. It takes a string containing surrounding spaces as input and asserts successful execution without error.*


### test_disallowed_scheme (method, L47-L49, parent: TestValidateUrl)

> *Summary: Asserts that calling `validate_url` with a URL using a disallowed scheme raises an `UnsafeURLError` containing the specific message "scheme not allowed". This tests the input validation logic for URL schemes.*


### test_missing_hostname_is_value_error_not_ssrf (method, L51-L55, parent: TestValidateUrl)

> *Summary: This test verifies that providing a URL with only a scheme (like "https://") raises a standard `ValueError` instead of an `UnsafeURLError`. It confirms the validation logic correctly identifies missing hostnames as a basic input error rather than a security vulnerability.*


### test_rejects_non_public_ip (method, L75-L81, parent: TestValidateUrl)

> *Summary: This test verifies that the URL validation rejects addresses using non-public IP addresses. It mocks `getaddrinfo` to return a specific private IP and asserts that calling `validate_url` with an associated label raises an `UnsafeURLError`.*


### test_rejects_when_any_resolved_ip_is_private (method, L83-L93, parent: TestValidateUrl)

> *Summary: This test verifies that a URL is rejected if its resolved IP addresses include any private ranges. It mocks the DNS resolution to return both a public and a private IP address when validating "https://mixed.example.com/".*


### test_dns_failure_is_value_error_not_ssrf (method, L95-L105, parent: TestValidateUrl)

> *Summary: This test verifies that a DNS lookup failure during URL validation raises a `ValueError` instead of an `UnsafeURLError`. It achieves this by mocking the socket's `getaddrinfo` function to simulate a name resolution error when validating a non-existent host.*


### TestAnalyzerSSRFGuard (class, L108-L154)

> *Summary: This test suite verifies that the `URLAnalyzer` correctly prevents access to private or loopback URLs during network requests. It uses mocking to simulate DNS resolution and HTTP responses, asserting that an `UnsafeURLError` is raised when attempting to fetch restricted addresses, even across redirects.*


### _resolve_loopback (method, L112-L116, parent: TestAnalyzerSSRFGuard)

> *Summary: This method uses `pytest.MonkeyPatch` to temporarily override the `getaddrinfo` function within URL utilities. It forces this function to always return a specific tuple representing the loopback address (`127.0.0.1`), effectively mocking network resolution for testing purposes.*


### test_analyze_by_request_blocks_initial_loopback (method, L118-L121, parent: TestAnalyzerSSRFGuard)

> *Summary: This test verifies that attempting to analyze a local loopback URL using `URLAnalyzer` raises an `UnsafeURLError`. It initializes the analyzer with `"http://localhost.evil.example/"` and asserts the expected exception during the analysis call.*


### test_follow_redirects_blocks_initial_loopback (method, L123-L126, parent: TestAnalyzerSSRFGuard)

> *Summary: When provided with a local loopback URL like `http://localhost.evil.example/`, the function asserts that attempting to follow redirects will raise an `UnsafeURLError`. This tests the security mechanism preventing infinite redirection loops on local hosts.*


### test_analyze_by_request_blocks_redirect_to_metadata (method, L129-L154, parent: TestAnalyzerSSRFGuard)

> *Summary: This test verifies that the URL analyzer rejects requests that redirect to AWS metadata IPs. It mocks network responses to simulate an initial public request followed by a hop to `169.254.169.254`, expecting an `UnsafeURLError` due to the non-public IP.*


### TestFormatMapping (class, L158-L194)

> *Summary: Verifies that the `InputFormat` enum contains all expected values and confirms the correctness of the `ExtensionToFormat` mapping dictionary by checking various file extensions against their corresponding format enums. It specifically tests mappings for common document, image, and unsupported file types.*


### test_input_format_enum (method, L159-L172, parent: TestFormatMapping)

> *Summary: Verifies that the `InputFormat` enumeration correctly maps each defined format (like DOCX, HTML, PDF) to its expected string value. This test ensures data consistency across all possible input types recognized by the system.*


### test_extension_to_format_mapping (method, L174-L194, parent: TestFormatMapping)

> *Summary: Verifies the `ExtensionToFormat` mapping dictionary by asserting that specific file extensions correctly map to predefined input formats, including handling both supported and unsupported types. It checks mappings for common document, image, and data file extensions against expected enum values.*


### TestURLAnalyzer (class, L198-L492)

> *Summary: This test suite verifies the functionality of a URL analyzer class by testing various scenarios for determining file type and content. It covers analysis based on URL extension, HTTP request headers (MIME type), error handling during network requests, redirect following, and prioritization logic between extension-based and request-based analysis.*


### _disable_ssrf_guard (method, L200-L204, parent: TestURLAnalyzer)

> *Summary: This method temporarily bypasses URL validation by patching the `validate_url` function within the document agent's utility module. It accepts a `pytest.MonkeyPatch` object to perform this monkeypatching operation.*


### pdf_url (method, L207-L208, parent: TestURLAnalyzer)

> *Summary: Returns a hardcoded string representing the URL for a PDF document. This method provides a static endpoint reference without taking any inputs.*


### html_url (method, L211-L212, parent: TestURLAnalyzer)

> *Summary: Returns a hardcoded string representing an HTML URL from the agent's configuration or state. This method provides a default web resource link for testing purposes.*


### no_extension_url (method, L215-L216, parent: TestURLAnalyzer)

> *Summary: Returns a hardcoded string representing a URL without any file extension. This method serves as a placeholder or default return value for testing purposes.*


### mock_response (method, L219-L225, parent: TestURLAnalyzer)

> *Summary: Creates and returns a `MagicMock` object simulating an HTTP response with a 200 status code, PDF content type headers, no history, and a predefined URL. This mock is used to simulate successful API responses for testing purposes.*


### test_init (method, L227-L233, parent: TestURLAnalyzer)

> *Summary: Verifies that the `URLAnalyzer` correctly initializes with a provided PDF URL, ensuring its internal state reflects the input and has no initial analysis results or redirect history. It confirms the stored URL matches the input and that other attributes are set to default empty states.*


### test_analyze_by_extension_pdf (method, L235-L241, parent: TestURLAnalyzer)

> *Summary: This test verifies that a PDF URL correctly identifies itself as a file with the `.pdf` extension and the `InputFormat.PDF` type when analyzed by extension. It takes a string URL as input and asserts the resulting analysis dictionary contains specific expected values.*


### test_analyze_by_extension_html (method, L243-L249, parent: TestURLAnalyzer)

> *Summary: This test verifies that the URL analysis correctly identifies an HTML file when provided with an HTML URL string. It asserts that the resulting data confirms the input is a file, its type is HTML, and its extension is "html".*


### test_analyze_by_extension_no_extension (method, L251-L257, parent: TestURLAnalyzer)

> *Summary: When provided a URL string lacking an extension, this test verifies that the analysis correctly identifies it as not being a file and returns `None` for both its type and extension. It confirms the internal analyzer method behaves as expected for such inputs.*


### test_analyze_by_request_pdf (method, L260-L268, parent: TestURLAnalyzer)

> *Summary: This test verifies that the `URLAnalyzer` correctly identifies a PDF file when analyzing a provided URL via an HTTP HEAD request. It asserts that the resulting analysis dictionary confirms the input is a file and specifically matches the PDF format and MIME type.*


### test_analyze_by_request_method_not_allowed (method, L271-L291, parent: TestURLAnalyzer)

> *Summary: This test verifies that if an initial `HEAD` request to a PDF URL returns a 405 error, the system correctly falls back and successfully analyzes the content using a subsequent `GET` request. It asserts that the final analysis result confirms the input is a valid PDF file.*


### test_analyze_by_request_connection_error (method, L294-L302, parent: TestURLAnalyzer)

> *Summary: This test verifies how the URL analyzer handles a `requests.exceptions.ConnectionError` during analysis by mocking an HTTP head request to fail. It asserts that the resulting output correctly identifies the input as invalid and includes a specific connection error message.*


### test_analyze_by_request_timeout (method, L305-L313, parent: TestURLAnalyzer)

> *Summary: This test verifies the agent's behavior when an HTTP request times out during URL analysis. By mocking a timeout exception on the HEAD request, it asserts that the resulting analysis correctly identifies the input as invalid and reports the timeout error.*


### test_analyze_by_request_too_many_redirects (method, L316-L325, parent: TestURLAnalyzer)

> *Summary: When the underlying HTTP request encounters too many redirects, this test verifies that the URL analyzer correctly captures the error state. It asserts that the analysis returns an invalid file type, flags a redirect issue, and includes the specific "Too many redirects" message in the result's error field.*


### test_analyze_by_request_with_redirects (method, L328-L352, parent: TestURLAnalyzer)

> *Summary: This test verifies that the URL analysis correctly processes HTTP redirects when fetching a PDF. It simulates a request chain with two redirects, asserting that the resulting analysis identifies the content as a PDF and captures the full redirect history and final URL.*


### test_analyze_prioritize_extension (method, L356-L377, parent: TestURLAnalyzer)

> *Summary: This test verifies that the URL analyzer prioritizes file type derived from an explicit extension over the MIME type reported by a network request when configured to do so. It asserts that the resulting analysis correctly uses the PDF type from the mock extension while retaining the HTML MIME type from the mock request.*


### test_analyze_prioritize_request (method, L381-L396, parent: TestURLAnalyzer)

> *Summary: When testing URL analysis, this method verifies that the analyzer prioritizes MIME type from a mock request over file extension when `prioritize_extension` is set to false. It asserts that the resulting analysis correctly reflects the HTML content provided by the mocked request.*


### test_get_result_before_analyze (method, L398-L401, parent: TestURLAnalyzer)

> *Summary: When provided with a PDF URL, this test verifies that calling the `get_result()` method on an initialized `URLAnalyzer` returns `None` before any analysis has been performed.*


### test_get_result_after_analyze (method, L405-L417, parent: TestURLAnalyzer)

> *Summary: This test verifies that the `get_result()` method returns a valid dictionary after an analyzer has processed a PDF URL. It mocks file extension detection and asserts the returned structure contains correct metadata like `"is_file": True` and `"file_type": PDF`.*


### test_get_redirect_info_no_redirects (method, L419-L428, parent: TestURLAnalyzer)

> *Summary: This test verifies the `get_redirect_info` method when a provided URL has no redirects. It asserts that the returned information indicates zero redirects, matches the original and final URLs to the input, and contains an empty redirect chain.*


### test_follow_redirects (method, L431-L453, parent: TestURLAnalyzer)

> *Summary: This test verifies that the `follow_redirects` method correctly processes a mock HTTP response containing multiple redirects. It asserts that the returned final URL and the captured redirect chain match the expected sequence from the mocked response history.*


### test_follow_redirects_error (method, L456-L465, parent: TestURLAnalyzer)

> *Summary: When the underlying HTTP request fails during redirection following, this test asserts that the utility returns the initial input URL and an empty list for the redirect chain. It achieves this by mocking a connection error on the HEAD request.*


### test_class_methods_for_formats (method, L467-L492, parent: TestURLAnalyzer)

> *Summary: This test verifies that a utility class correctly exposes lists of supported input formats, MIME types, and file extensions. It asserts the presence of expected values like PDF, DOCX, HTML, and various corresponding MIME types and extensions within these returned collections.*

