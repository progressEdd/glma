# test/tools/experimental/browser_use/test_langchain_factory.py

3 class(es): TestLangchainFactory, TestChatVertexAIFactory, TestChatOpenAIFactory. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLangchainFactory | class |  |
| TestChatVertexAIFactory | class |  |
| TestChatOpenAIFactory | class |  |

## Chunks

### TestLangchainFactory (class, L28-L146)

> *Summary: This test suite verifies the `LangChainChatModelFactory`'s ability to instantiate various LLM models based on configuration inputs. It tests successful creation across multiple API types (OpenAI, Azure, Google, etc.) and asserts that required parameters like `base_url` are correctly enforced when missing for specific providers.*


### test_number_of_factories (method, L31-L32, parent: TestLangchainFactory)

> *Summary: Verifies that the `LangChainChatModelFactory` class maintains exactly seven registered factories. This assertion checks the internal state of the factory collection against an expected count.*


### test_create_base_chat_model (method, L107-L123, parent: TestLangchainFactory)

> *Summary: This test verifies that the factory correctly instantiates a specified chat model based on configuration inputs. It asserts the resulting object's class name and checks specific attribute values like `azure_endpoint` or `openai_api_base` if a base URL is provided.*


### test_create_base_chat_model_raises_if_mandatory_key_missing (method, L142-L146, parent: TestLangchainFactory)

> *Summary: Asserts that attempting to create a base chat model with an incomplete configuration list raises a `ValueError` containing the expected error message. This test verifies input validation when mandatory keys are absent from the provided configuration.*


### TestChatVertexAIFactory (class, L160-L209)

> *Summary: This test suite verifies the `ChatVertexAIFactory`'s behavior for Google Vertex AI integrations. It confirms that the factory correctly identifies configurations specifying `"api_type": "google_vertex"` and successfully instantiates a `ChatVertexAI` object, normalizing inputs like `project_id` to the internal `project` attribute.*


### test_accepts_google_vertex (method, L165-L170, parent: TestChatVertexAIFactory)

> *Summary: This test verifies that the `ChatVertexAIFactory` correctly identifies configurations specifying `"api_type": "google_vertex"` as valid, while rejecting other API types like generic `"google"` or `"openai"`. It confirms the factory's specific acceptance criteria for Google Vertex AI integration.*


### test_creates_chat_vertex_ai (method, L172-L189, parent: TestChatVertexAIFactory)

> *Summary: This test verifies that the factory correctly instantiates a `ChatVertexAI` model when provided with specific Google Vertex AI configuration details. It asserts that the resulting object is of the correct type and holds the specified project and location identifiers.*


### test_project_id_is_normalized_to_project (method, L191-L209, parent: TestChatVertexAIFactory)

> *Summary: This test verifies that when creating a chat model using the `LangChainChatModelFactory` with an AG2-style `project_id`, the resulting `ChatVertexAI` instance correctly exposes this ID under the internal `.project` attribute. It confirms seamless translation between external and internal project identifier naming conventions.*


### TestChatOpenAIFactory (class, L223-L237)

> *Summary: This test verifies that the `ChatOpenAIFactory` correctly instantiates a `ChatOpenAI` object when provided with different configuration formats containing model names and API keys. It uses parameterized tests to check both direct dictionary input and list-of-dictionaries input for the factory's creation method.*


### test_create (method, L233-L237, parent: TestChatOpenAIFactory)

> *Summary: This test verifies that the factory method correctly instantiates a `ChatOpenAI` object when provided with an LLM configuration dictionary. It ensures this by temporarily removing the `OPENAI_API_KEY` environment variable before calling the creation function.*

