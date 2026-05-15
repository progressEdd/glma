# test/tools/experimental/google_search/test_youtube_search.py

1 class(es): TestYoutubeSearchTool. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestYoutubeSearchTool | class |  |

## Chunks

### TestYoutubeSearchTool (class, L19-L200)

> *Summary: This test suite verifies the functionality of a YouTube search tool by testing its initialization, basic search capabilities (with and without video details), and end-to-end integration with LLM agents using both OpenAI and Gemini credentials. It uses mocking extensively to simulate API responses for isolated unit and integration testing.*


### test_init (method, L20-L28, parent: TestYoutubeSearchTool)

> *Summary: This test verifies the correct initialization of a `YoutubeSearchTool` instance using a provided API key. It asserts that the resulting object has the expected name, description, and stores the input API key correctly.*


### test_init_no_api_key (method, L30-L32, parent: TestYoutubeSearchTool)

> *Summary: Asserts that instantiating the search tool without providing a `youtube_api_key` raises a `ValueError`. This verifies the required input validation for API key presence.*


### mock_search_response (method, L35-L57, parent: TestYoutubeSearchTool)

> *Summary: Provides a hardcoded dictionary structure simulating a YouTube search API response. This mock returns a list of two video items, each containing title, description, and channel information for testing purposes.*


### mock_video_details (method, L60-L86, parent: TestYoutubeSearchTool)

> *Summary: Returns a mock dictionary simulating the response from a YouTube video details API call. This structure contains an array of two sample videos, each with predefined metadata like title, view counts, and duration.*


### test_youtube_search_basic (method, L88-L110, parent: TestYoutubeSearchTool)

> *Summary: This test verifies the basic functionality of a YouTube search utility by mocking external API calls to simulate successful responses. It asserts that the function returns exactly two structured results matching predefined titles, descriptions, and URLs for a given query.*


### test_youtube_search_with_details (method, L112-L136, parent: TestYoutubeSearchTool)

> *Summary: This test verifies the functionality of a YouTube search wrapper by mocking both the initial search response and subsequent video detail retrieval. It asserts that the function correctly processes the mocked data, returning a list containing two items with specific details like title, view count, likes, and duration.*


### _test_end_to_end (method, L138-L170, parent: TestYoutubeSearchTool)

> *Summary: This test verifies the end-to-end functionality of a YouTube search tool by mocking its underlying search and details retrieval methods. It runs an assistant with a specific prompt, asserting that both mocked search and detail functions were called during execution.*


### test_end_to_end_openai (method, L173-L185, parent: TestYoutubeSearchTool)

> *Summary: This test verifies the complete workflow by using a `YoutubeSearchTool` with provided API credentials. It executes an end-to-end check against mocked search and video detail responses to validate system behavior.*


### test_end_to_end_gemini (method, L188-L200, parent: TestYoutubeSearchTool)

> *Summary: This test verifies the end-to-end functionality of a YouTube search tool by simulating interactions with Gemini. It uses provided mock responses for both search results and video details to assert correct behavior within the testing framework.*

