# test/coding/test_remyx_executor.py

2 class(es): TestRemyxCodeExecutor, TestRemyxCodeResult. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestRemyxCodeExecutor | class |  |
| TestRemyxCodeResult | class |  |

## Chunks

### TestRemyxCodeExecutor (class, L28-L421)

> *Summary: This test suite verifies the functionality of `RemyxCodeExecutor` by mocking external dependencies like asset retrieval and Docker initialization. It tests various initialization paths (via arXiv ID or direct image), environment variable handling, metadata extraction, system message generation, agent creation, and result formatting.*


### setup_method (method, L31-L37, parent: TestRemyxCodeExecutor)

> *Summary: Before each test execution, this method ensures a clean state by removing specific API keys (`REMYX_API_KEY` and `REMYXAI_API_KEY`) from the operating system's environment variables. This guarantees tests run in an isolated environment without relying on pre-set credentials.*


### test_init_with_arxiv_id (method, L41-L63, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the `RemyxCodeExecutor` correctly initializes when provided with an arXiv ID. It mocks asset retrieval and parent initialization to confirm the executor stores the correct ID, fetches metadata via the mocked function, and calls the parent constructor.*


### test_init_with_direct_image (method, L66-L74, parent: TestRemyxCodeExecutor)

> *Summary: Verifies that the executor initializes correctly when provided a direct Docker image string as input. It asserts that internal metadata fields remain unset and confirms the parent initialization method was called exactly once.*


### test_init_with_api_key_from_env (method, L78-L91, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the `RemyxCodeExecutor` correctly loads its API key from the environment variables during initialization. It sets a mock environment variable and asserts that the instantiated executor object possesses this value.*


### test_init_with_paper_not_found (method, L94-L99, parent: TestRemyxCodeExecutor)

> *Summary: When the asset retrieval mock returns `None`, this test asserts that instantiating the executor with a specific arXiv ID raises a `ValueError` indicating the paper was not found in the catalog.*


### test_init_with_no_docker_image (method, L102-L110, parent: TestRemyxCodeExecutor)

> *Summary: When initialized with an asset lacking a Docker image (simulated via `mock_get_asset`), the executor raises a `ValueError` indicating the absence of a required Docker image. This test verifies that initialization fails correctly under this specific condition.*


### test_init_with_no_arxiv_or_image (method, L112-L115, parent: TestRemyxCodeExecutor)

> *Summary: Verifies that attempting to instantiate the executor without providing either an `arxiv_id` or an `image` results in a `ValueError`. This test confirms the required input validation during object creation.*


### test_environment_variable_handling (method, L119-L143, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that specified environment variables are correctly passed to the container creation process when initializing a code executor. It mocks asset retrieval and asserts that the `HF_TOKEN` and `WANDB_API_KEY` set in the OS environment end up in the container's environment configuration.*


### test_code_extractor_property (method, L147-L159, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the `code_extractor` property of a `RemyxCodeExecutor` instance correctly returns an instance of `MarkdownCodeExtractor`. It achieves this by mocking asset retrieval and ensuring the executor is initialized with specific mock data.*


### test_paper_info_property (method, L163-L180, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the `paper_info` property correctly retrieves and returns metadata for a specified paper asset. It mocks an asset object with predefined attributes and ensures the resulting dictionary contains the expected title from the mocked data.*


### test_get_paper_context (method, L184-L209, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the `get_paper_context` method correctly constructs and returns a formatted dictionary containing metadata for a specific paper asset. It mocks an asset retrieval process to ensure all expected fields like title, ID, GitHub URL, and reasoning are present in the final output context.*


### test_get_paper_context_no_metadata (method, L213-L220, parent: TestRemyxCodeExecutor)

> *Summary: When called without any associated metadata, this test verifies that the execution returns a specific string indicating no paper information is present. It initializes an executor and asserts the output matches the expected default message.*


### test_build_system_message_default (method, L224-L244, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the internal method constructs a default system message for code execution. It mocks asset retrieval and initializes an executor to assert the resulting message contains expected structural elements like the paper title, mission statement, and phase descriptions.*


### test_build_system_message_with_custom_goal (method, L248-L262, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the internal method constructs a system message containing a specified custom goal when initialized with an asset. It asserts that the resulting message includes the provided goal string but excludes specific boilerplate text, confirming correct message generation logic.*


### test_build_system_message_with_system_message (method, L266-L281, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the internal method correctly incorporates an extra system message into the generated output. It calls the method with a specific string and asserts that both parts of that string are present in the returned message structure.*


### test_repr_with_arxiv_id (method, L285-L297, parent: TestRemyxCodeExecutor)

> *Summary: Verifies that the `__repr__` method correctly formats the executor's string representation when initialized with an `arxiv_id`. It mocks asset retrieval to ensure the representation reflects the provided ID, regardless of complex asset details.*


### test_repr_with_image_only (method, L300-L307, parent: TestRemyxCodeExecutor)

> *Summary: Verifies that the `__repr__` method correctly formats a string representation when only an image is provided to the executor. It asserts the output matches the expected format using the provided image name.*


### test_create_agents (method, L313-L339, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies the `create_agents` method by mocking asset retrieval and agent initialization. It asserts that the method correctly instantiates and returns two specific mocked agents based on the provided goal and configuration.*


### test_create_agents_with_system_message (method, L345-L374, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies that the `create_agents` method correctly passes a specified system message to the generated agents. It mocks asset retrieval and agent initialization, then asserts that the provided system prompt is present in the arguments of the second created agent (the writer).*


### test_format_chat_result (method, L378-L404, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies the `format_chat_result` static method by providing a mock chat result object and an asset mock. It asserts that the returned string correctly incorporates details like message count, Chat ID, total cost, and the provided summary.*


### test_format_chat_result_from_utils (method, L406-L421, parent: TestRemyxCodeExecutor)

> *Summary: This test verifies the `format_chat_result` utility by providing a mock result object containing chat history, an ID, a summary, and cost data. It asserts that the returned string correctly incorporates the session summary title and the provided chat ID.*


### TestRemyxCodeResult (class, L425-L449)

> *Summary: This test suite verifies the instantiation and attribute setting of a `RemyxCodeResult` object. It confirms that the constructor correctly initializes fields like exit code, output string, arXiv ID, and paper title, handling cases both with and without supplementary paper metadata.*


### test_code_result_creation (method, L428-L440, parent: TestRemyxCodeResult)

> *Summary: This test verifies the correct initialization and attribute assignment of a `RemyxCodeResult` object. It instantiates the result with predefined values for exit code, output, arXiv ID, and paper title, then asserts that these properties match the input.*


### test_code_result_without_paper_info (method, L442-L449, parent: TestRemyxCodeResult)

> *Summary: Verifies that a `RemyxCodeResult` object correctly initializes with provided exit code and output, while ensuring optional fields like arXiv ID and paper title remain unset (None) when not supplied.*

