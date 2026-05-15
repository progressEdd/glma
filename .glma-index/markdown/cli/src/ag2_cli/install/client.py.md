# cli/src/ag2_cli/install/client.py

2 class(es): FetchError, ArtifactClient. 15 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| FetchError | class |  |
| ArtifactClient | class |  |

## Chunks

### FetchError (class, L18-L19)

> *Summary: This custom exception signals that an operation to retrieve data from a remote source has failed. It inherits from the base `Exception` class for error handling purposes.*


### ArtifactClient (class, L22-L265)

> *Summary: This class manages artifact retrieval from a GitHub registry, caching metadata and files locally for fast access. It fetches the overall registry manifest, downloads specific artifacts by recursively listing directory contents via the Contents API, and provides search/listing capabilities over cached entries.*


### __init__ (method, L35-L45, parent: ArtifactClient)

> *Summary: Initializes the client with repository URL, a local cache directory, and a default branch name. It sets up necessary HTTP headers for GitHub API interaction and immediately calls an authentication setup method.*


### _init_auth (method, L47-L53, parent: ArtifactClient)

> *Summary: Checks environment variables for `GH_TOKEN` or `GITHUB_TOKEN`; if found, it sets the request headers to include a bearer token for authenticated API calls.*


### _raw_url (method, L55-L56, parent: ArtifactClient)

> *Summary: Constructs a full raw URL for a given file path by prepending the base GitHub raw URL, repository name, and branch information. It takes a local file path string as input and returns the complete remote URL string.*


### _api_url (method, L58-L59, parent: ArtifactClient)

> *Summary: Constructs the full API endpoint URL by prepending a base GitHub API address to a provided repository and path segment. It takes a string `path` as input and returns the complete URL string.*


### fetch_registry (method, L63-L79, parent: ArtifactClient)

> *Summary: Retrieves the registry data from a remote source, prioritizing a local cache if it exists and hasn't expired based on `REGISTRY_TTL`. If fetching is forced or the cache is stale, it downloads the latest JSON content, saves it to disk along with metadata, and returns the retrieved dictionary.*


### _type_dir (method, L84-L95, parent: ArtifactClient)

> *Summary: This method maps a given `artifact_type` string to its corresponding directory name within the repository structure. It returns the mapped directory name or defaults to using the input type if no specific mapping exists.*


### fetch_artifact_manifest (method, L97-L101, parent: ArtifactClient)

> *Summary: Retrieves the `artifact.json` manifest for a specified artifact type and name from a remote location. It constructs the full path based on the provided inputs and returns the parsed JSON content as a dictionary.*


### fetch_artifact_dir (method, L103-L144, parent: ArtifactClient)

> *Summary: Downloads a specified artifact directory from GitHub to the local cache, using the Contents API for targeted retrieval. It accepts an `artifact_type`, `name`, and optional `owner`/`version`, returning the absolute path to the cached directory or raising an error if the artifact is not found.*


### _list_contents_recursive (method, L146-L168, parent: ArtifactClient)

> *Summary: Recursively traverses a repository path by querying the GitHub Contents API for each directory level. It takes a `repo_path` string as input and returns a list of full file paths found within that directory structure.*


### fetch_file (method, L170-L196, parent: ArtifactClient)

> *Summary: Downloads a file from a given URL to a specified destination path, handling HTTP requests and streaming content. Optionally verifies the integrity of the downloaded file against a provided SHA256 checksum before returning the final `Path` object.*


### search (method, L200-L216, parent: ArtifactClient)

> *Summary: Filters a collection of registry artifacts based on a keyword search across owner, name, description, and tags. It optionally restricts the search to a specific artifact type provided as input.*


### list_artifacts (method, L218-L223, parent: ArtifactClient)

> *Summary: Retrieves a list of artifact dictionaries from the provided registry, optionally filtering the results based on a specified `artifact_type`. It returns a list containing only the matching or all artifacts found within the registry's "artifacts" key.*


### _get_json (method, L227-L239, parent: ArtifactClient)

> *Summary: Fetches JSON data from a specified URL using an HTTP client configured with existing headers and redirects. It validates the response status code, raising specific errors for 404 (Not Found), 403 (Rate Limit Exceeded), or any other non-200 status.*


### _get_json_list (method, L241-L258, parent: ArtifactClient)

> *Summary: Fetches data from a specified URL using HTTP GET and handles common errors like 404 or rate limiting. It specifically expects the response to be a JSON array, returning it as a Python list, but wraps single-object responses into a list for consistency.*


### _get_bytes (method, L260-L265, parent: ArtifactClient)

> *Summary: Fetches the raw byte content from a specified URL using an HTTP client configured with existing headers and redirects. It raises a `FetchError` if the HTTP response status code is not 200.*

