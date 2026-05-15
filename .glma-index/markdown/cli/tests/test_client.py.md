# cli/tests/test_client.py

9 class(es): TestArtifactClientInit, TestInitAuth, TestTypeDir, TestFetchRegistry, TestFetchArtifactDir, TestFetchFile, TestSearch, TestListArtifacts, TestGetJson. 35 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestArtifactClientInit | class |  |
| TestInitAuth | class |  |
| TestTypeDir | class |  |
| TestFetchRegistry | class |  |
| TestFetchArtifactDir | class |  |
| TestFetchFile | class |  |
| TestSearch | class |  |
| TestListArtifacts | class |  |
| TestGetJson | class |  |

## Chunks

### TestArtifactClientInit (class, L44-L66)

> *Summary: This test suite verifies the initialization of an `ArtifactClient` by checking that it correctly sets default or user-provided repository, branch, and cache directory values based on input parameters. It ensures the resulting client object has the expected configuration attributes and includes necessary HTTP headers.*


### test_default_params (method, L47-L54, parent: TestArtifactClientInit)

> *Summary: This test verifies that an `ArtifactClient` initializes with expected default values when no environment variables are set, specifically checking the repository name, branch, cache directory path, and presence of an "Accept" header. It ensures the client correctly uses the provided temporary path for caching.*


### test_custom_params (method, L56-L66, parent: TestArtifactClientInit)

> *Summary: This test verifies that an `ArtifactClient` correctly initializes and stores custom configuration parameters provided during instantiation, such as repository name, branch, and a specific cache directory path. It asserts that the internal attributes match the input values passed to the client constructor.*


### TestInitAuth (class, L69-L98)

> *Summary: These tests verify that the `ArtifactClient` correctly reads authentication tokens from environment variables, prioritizing `GH_TOKEN` over `GITHUB_TOKEN`, and handles cases where no token is present. It asserts that the resulting HTTP headers contain the correct authorization string based on the provided environment setup.*


### test_gh_token (method, L72-L76, parent: TestInitAuth)

> *Summary: This test verifies that the `ArtifactClient` correctly sets the authorization header using a provided GitHub token environment variable. It asserts that the internal headers dictionary contains `"Authorization": "token ghp_abc123"` after initialization with the mocked environment.*


### test_github_token_fallback (method, L78-L82, parent: TestInitAuth)

> *Summary: This test verifies that the `ArtifactClient` correctly uses a provided fallback GitHub token when configured via environment variables. It asserts that the resulting HTTP headers contain the expected authorization token value.*


### test_gh_token_takes_precedence (method, L84-L92, parent: TestInitAuth)

> *Summary: When both `GH_TOKEN` and `GITHUB_TOKEN` environment variables are set, this test verifies that the client prioritizes and uses the value from `GH_TOKEN` for its authorization header. It confirms the correct token is used when multiple authentication sources are available.*


### test_no_token (method, L94-L98, parent: TestInitAuth)

> *Summary: This test verifies that an `ArtifactClient` instance, when initialized without any environment tokens, does not include an "Authorization" header in its internal headers. It achieves this by clearing all existing environment variables before instantiation.*


### TestTypeDir (class, L101-L119)

> *Summary: This test verifies the `ArtifactClient`'s internal mapping logic for artifact types. It asserts that known types map to specific directory names while ensuring unknown types are returned unchanged.*


### test_known_types (method, L115-L116, parent: TestTypeDir)

> *Summary: Verifies that the internal type directory mapping for a given `artifact_type` correctly returns the `expected` string. This test uses predefined inputs to assert against known system behavior.*


### test_unknown_type_returns_as_is (method, L118-L119, parent: TestTypeDir)

> *Summary: Verifies that when an unknown type is passed to `ArtifactClient._type_dir`, the function returns the input string unchanged. This confirms the default behavior for unhandled types within the client's directory lookup mechanism.*


### TestFetchRegistry (class, L122-L184)

> *Summary: These tests verify the caching logic of `ArtifactClient`'s registry fetching mechanism by simulating various cache states. They confirm that data is served from a fresh local cache, fetched remotely when stale or missing, and can be forcibly refreshed regardless of existing cache validity.*


### test_returns_cached_data_when_fresh (method, L125-L139, parent: TestFetchRegistry)

> *Summary: This test verifies that the client retrieves data from its local cache when the cached files are considered fresh. It sets up mock cache files and asserts that the underlying data fetching method is never called, confirming the caching mechanism works correctly.*


### test_fetches_from_remote_when_cache_stale (method, L141-L156, parent: TestFetchRegistry)

> *Summary: This test verifies that the client fetches data from a remote source when its local cache is expired. It simulates a stale cache by setting an old timestamp and asserts that `fetch_registry` returns the fresh sample data, subsequently updating the local cache file.*


### test_fetches_from_remote_when_cache_missing (method, L158-L167, parent: TestFetchRegistry)

> *Summary: This test verifies that when the local cache is absent, the client successfully fetches data from a mocked remote source and subsequently saves it to disk in both JSON and metadata formats. It asserts that the returned result matches the expected sample data and that the necessary cache files are created.*


### test_force_refresh_bypasses_cache (method, L169-L184, parent: TestFetchRegistry)

> *Summary: This test verifies that setting `force_refresh=True` causes the client to ignore existing cache files and fetch fresh data from the source. It asserts that the returned result matches the expected sample registry, and subsequently confirms the local cache has been updated with the new data.*


### TestFetchArtifactDir (class, L187-L232)

> *Summary: Tests the `fetch_artifact_dir` functionality by verifying caching behavior, error handling for missing artifacts, and successful file download into a specified cache directory when provided with mock dependencies. It ensures that if a `.fetched` marker exists, the cached path is returned, otherwise, it downloads contents and creates the necessary markers/files.*


### test_returns_cached_dir_when_fetched_marker_exists (method, L190-L201, parent: TestFetchArtifactDir)

> *Summary: When a `.fetched` marker exists in the expected cache location, this test verifies that the artifact fetching mechanism returns the pre-existing cached directory path instead of re-downloading or creating new content. It simulates a successful prior fetch by setting up the necessary directory structure and marker file before calling `fetch_artifact_dir`.*


### test_raises_fetch_error_when_artifact_not_found (method, L203-L211, parent: TestFetchArtifactDir)

> *Summary: This test verifies that attempting to fetch a directory when no artifacts are present raises a `FetchError`. It mocks the internal listing function to return an empty list and asserts the expected exception is thrown during the call to `fetch_artifact_dir`.*


### test_downloads_files_to_cache (method, L213-L232, parent: TestFetchArtifactDir)

> *Summary: This test verifies that the client correctly downloads and caches a specified directory's contents to a temporary path. It mocks file listing and content retrieval to assert that the resulting destination directory is created, marked as fetched, and contains all expected files.*


### TestFetchFile (class, L235-L335)

> *Summary: These tests verify the `fetch_file` functionality by mocking HTTP responses to simulate various scenarios. It confirms successful file download and writing, validates SHA256 checksums upon success, raises an error and deletes the file on checksum mismatch, and handles HTTP errors like 500.*


### test_downloads_and_writes_file (method, L238-L261, parent: TestFetchFile)

> *Summary: This test verifies that the client correctly downloads content from a mocked HTTP stream and writes it to a specified destination path. It asserts that the returned path matches the input destination and that the written file content is identical to the mock response data.*


### test_sha256_verification_pass (method, L263-L286, parent: TestFetchFile)

> *Summary: This test verifies successful file retrieval by mocking HTTP responses and asserting that the `ArtifactClient` correctly downloads a file to the specified destination path when provided with a valid SHA-256 checksum. It confirms the client returns the local path upon successful operation.*


### test_sha256_verification_fail_raises_and_deletes (method, L288-L313, parent: TestFetchFile)

> *Summary: This test verifies that when a file download fails due to an incorrect SHA256 checksum, the process raises a `FetchError` and subsequently deletes any partially downloaded file. It mocks HTTP client interactions to simulate a successful retrieval followed by a verification failure.*


### test_fetch_file_http_error (method, L315-L335, parent: TestFetchFile)

> *Summary: This test verifies that attempting to fetch a file when the HTTP response returns a 500 status code correctly raises a `FetchError`. It mocks the underlying HTTP client and response objects to simulate this specific server error condition during the download process.*


### TestSearch (class, L338-L403)

> *Summary: These tests verify the search functionality of an `ArtifactClient` by calling its `search` method with various inputs like keywords, artifact types, and owners. The assertions confirm that the returned list of results correctly reflects filtering based on these criteria, including case-insensitivity and zero matches.*


### test_search_by_keyword (method, L341-L347, parent: TestSearch)

> *Summary: This test verifies the keyword search functionality of an `ArtifactClient` by querying a sample registry for items matching "fastapi". It asserts that exactly one result is returned and that its name matches the search term.*


### test_search_keyword_in_description (method, L349-L355, parent: TestSearch)

> *Summary: This test verifies that searching for the keyword "google" within an artifact's description returns exactly one result named "web-search". It initializes a client instance using a temporary directory and calls the search method against a predefined registry.*


### test_search_keyword_in_tags (method, L357-L363, parent: TestSearch)

> *Summary: This test verifies that searching for the keyword "rest" within artifact tags returns exactly one result named "fastapi". It initializes an `ArtifactClient` using a temporary directory and calls its search method against a predefined registry.*


### test_search_case_insensitive (method, L365-L371, parent: TestSearch)

> *Summary: This test verifies that the search functionality returns a result regardless of case when querying for "FASTAPI". It initializes an `ArtifactClient` and asserts that the single returned item has the lowercase name "fastapi".*


### test_search_filters_by_type (method, L373-L380, parent: TestSearch)

> *Summary: This test verifies that the client correctly filters search results by specifying an `artifact_type`. It calls the `client.search` method, expecting exactly one result matching the type "tool".*


### test_search_type_filter_excludes_other_types (method, L382-L388, parent: TestSearch)

> *Summary: When querying for artifacts of type "skill" using the search function, this test asserts that results matching a specific term like "search" are excluded if they belong to a different category, such as a tool. It verifies that the `ArtifactClient` correctly filters based on the provided `artifact_type`.*


### test_search_no_matches (method, L390-L395, parent: TestSearch)

> *Summary: This test verifies that the search functionality returns an empty list when no artifacts match the provided query string. It initializes a client instance and calls `client.search` with a known non-existent identifier to assert zero results.*


### test_search_by_owner (method, L397-L403, parent: TestSearch)

> *Summary: This test verifies the `ArtifactClient`'s search functionality by querying a specific registry for items matching "community." It asserts that exactly one result is returned and that its name matches "chatbot."*


### TestListArtifacts (class, L406-L436)

> *Summary: These tests verify the `list_artifacts` method's behavior by asserting correct artifact retrieval from a provided registry. It confirms that the function can list all artifacts, filter results by a specific type, handle cases with no matching types, and correctly return an empty list for an empty input registry.*


### test_list_all (method, L409-L414, parent: TestListArtifacts)

> *Summary: This test verifies that the `ArtifactClient` correctly retrieves all artifacts from a specified registry. It initializes the client in an isolated environment and asserts that the returned list contains exactly three items.*


### test_list_filter_by_type (method, L416-L422, parent: TestListArtifacts)

> *Summary: This test verifies that the `ArtifactClient` correctly filters a list of artifacts by type. It calls `list_artifacts` specifying `"skill"` as the type and asserts that exactly one artifact named `"fastapi"` is returned in the results.*


### test_list_filter_by_type_no_matches (method, L424-L429, parent: TestListArtifacts)

> *Summary: This test verifies that when querying for artifacts of a specific type ("dataset"), the client returns an empty list if no matching artifacts exist in the registry. It initializes the client with a temporary cache directory and asserts the length of the returned results is zero.*


### test_list_empty_registry (method, L431-L436, parent: TestListArtifacts)

> *Summary: When initialized without environment variables, this test verifies that calling `list_artifacts` with an empty artifact list returns an empty result set. It confirms the client correctly handles requests for no artifacts.*


### TestGetJson (class, L439-L513)

> *Summary: This test suite verifies the error handling and successful JSON retrieval of an HTTP GET request made by `ArtifactClient`. It simulates various HTTP status codes (404, 403, 500) to ensure appropriate `FetchError` exceptions are raised, while also confirming correct JSON parsing for a 200 response.*


### test_404_raises_not_found (method, L442-L458, parent: TestGetJson)

> *Summary: This test verifies that attempting to fetch a resource returning an HTTP 404 status code correctly raises a `FetchError` with the message "Not found". It mocks the underlying HTTP client to simulate this specific failure scenario during a JSON retrieval call.*


### test_403_raises_rate_limit (method, L460-L476, parent: TestGetJson)

> *Summary: This test verifies that attempting to fetch data when the HTTP response returns a 403 status code correctly raises a `FetchError` indicating a rate limit issue. It mocks the underlying HTTP client to simulate this specific failure condition during an API call.*


### test_500_raises_http_error (method, L478-L494, parent: TestGetJson)

> *Summary: This test verifies that an `ArtifactClient` raises a `FetchError` when its underlying HTTP client returns a response with a status code of 500. It mocks the HTTP request to simulate this server error condition during a JSON retrieval attempt.*


### test_200_returns_json (method, L496-L513, parent: TestGetJson)

> *Summary: This test verifies that a client method successfully returns JSON data when an HTTP GET request yields a 200 status code. It mocks the underlying HTTP client to simulate a successful response containing predefined JSON, asserting the returned value matches the expected structure.*

