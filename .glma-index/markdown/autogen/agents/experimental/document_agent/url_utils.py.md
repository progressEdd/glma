# autogen/agents/experimental/document_agent/url_utils.py

1 function(s): validate_url. 3 class(es): UnsafeURLError, InputFormat, URLAnalyzer. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| UnsafeURLError | class |  |
| validate_url | function |  |
| InputFormat | class |  |
| URLAnalyzer | class |  |

## Chunks

### UnsafeURLError (class, L20-L21)

> *Summary: This custom exception inherits from `ValueError` and signals that a provided URL has been blocked by the Server-Side Request Forgery (SSRF) protection mechanism. It serves as an error indicator for invalid or disallowed URLs during network operations.*


### validate_url (function, L24-L70)

> *Summary: This function validates a provided URL string against security risks like SSRF by checking its scheme and resolving its hostname. It raises `ValueError` for malformed URLs or DNS resolution failures, while raising `UnsafeURLError` if the URL uses disallowed schemes or resolves to non-public IP addresses (e.g., loopback or private ranges).*


### InputFormat (class, L73-L87)

> *Summary: Defines an enumeration of supported file formats for input processing. It lists various types like DOCX, HTML, PDF, and JSON, alongside an `INVALID` state for error handling.*


### URLAnalyzer (class, L144-L502)

> *Summary: This class analyzes a given URL to determine if it points to a web page or a specific file type by checking both its extension and optionally making HTTP requests. It provides methods to analyze based on extension, perform network checks (including handling redirects), and retrieve detailed results about the analysis process.*


### __init__ (method, L183-L192, parent: URLAnalyzer)

> *Summary: Initializes an analyzer object by storing a provided URL string and setting up internal state variables for the analysis result, final destination, and redirect history. These attributes will be populated during subsequent processing of the input URL.*


### analyze (method, L194-L267, parent: URLAnalyzer)

> *Summary: Determines if a URL points to a file or webpage by first analyzing its extension, and optionally performing an HTTP request to confirm or refine the classification. It returns a dictionary containing the determined status (`is_file`), type information (extension/MIME), and details about any redirects encountered during testing.*


### _analyze_by_extension (method, L269-L300, parent: URLAnalyzer)

> *Summary: Determines if a given URL points to a file by inspecting its path extension. It returns a dictionary indicating if it's a file, its type based on predefined mappings, and the specific extension found, or defaults to assuming it's a webpage otherwise.*


### _analyze_by_request (method, L303-L411, parent: URLAnalyzer)

> *Summary: Performs an HTTP HEAD (or GET if 405) request to analyze a given URL's content type while enforcing SSRF security checks on the initial and all redirected URLs. It returns a dictionary detailing whether the resource is a file, its determined format/MIME type, or an error object upon failure.*


### get_result (method, L413-L419, parent: URLAnalyzer)

> *Summary: Retrieves the stored analysis outcome from the agent instance; returns a dictionary containing the results if an analysis has occurred, otherwise returns `None`.*


### get_redirect_info (method, L421-L442, parent: URLAnalyzer)

> *Summary: Retrieves details about HTTP redirects from the agent's state after a request completes. It returns a dictionary containing boolean status, count, and lists of the original URL, final URL, and the full redirect chain.*


### follow_redirects (method, L445-L487, parent: URLAnalyzer)

> *Summary: This method fetches a URL by following HTTP redirects using `requests.head` (falling back to GET if a 405 is encountered), while strictly validating all URLs against SSRF risks. It returns a tuple containing the final resolved URL and a list detailing the entire redirect chain, or the original URL and an empty list upon request failure.*


### get_supported_formats (method, L490-L492, parent: URLAnalyzer)

> *Summary: Retrieves all supported input file formats by extracting the keys from the class's `FormatToMimeType` mapping. This returns a list of `InputFormat` enums that the agent can process.*


### get_supported_mime_types (method, L495-L497, parent: URLAnalyzer)

> *Summary: Retrieves a list of all recognized MIME types by accessing the keys of the class's `MimeTypeToFormat` mapping. This function serves to expose the set of file formats the agent can handle.*


### get_supported_extensions (method, L500-L502, parent: URLAnalyzer)

> *Summary: Retrieves all recognized file extensions by returning the keys from the `ExtensionToFormat` mapping. This provides a definitive list of formats the agent can handle based on its internal configuration.*

