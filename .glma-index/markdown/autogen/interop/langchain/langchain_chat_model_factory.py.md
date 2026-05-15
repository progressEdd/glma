# autogen/interop/langchain/langchain_chat_model_factory.py

8 class(es): LangChainChatModelFactory, ChatOpenAIFactory, DeepSeekFactory, ChatAnthropicFactory, ChatGoogleGenerativeAIFactory, ChatVertexAIFactory, AzureChatOpenAIFactory, ChatOllamaFactory. 20 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| LangChainChatModelFactory | class |  |
| ChatOpenAIFactory | class |  |
| DeepSeekFactory | class |  |
| ChatAnthropicFactory | class |  |
| ChatGoogleGenerativeAIFactory | class |  |
| ChatVertexAIFactory | class |  |
| AzureChatOpenAIFactory | class |  |
| ChatOllamaFactory | class |  |

## Chunks

### LangChainChatModelFactory (class, L41-L78)

> *Summary: This abstract factory pattern provides a mechanism to instantiate specific chat models based on configuration. It uses a registration system where concrete factories declare which `api_type` they support, allowing the main creation method to select and build the correct model from an input configuration dictionary.*


### create_base_chat_model (method, L45-L51, parent: LangChainChatModelFactory)

> *Summary: This method determines and instantiates a base chat model by iterating through registered factories. It accepts an `LLMConfig` or dictionary, uses it to select the appropriate factory, and returns the corresponding initialized model instance.*


### register_factory (method, L54-L59, parent: LangChainChatModelFactory)

> *Summary: This decorator registers a provided model factory class into the `_factories` set of its decorated class. It wraps the factory to ensure it is added upon registration, allowing for dynamic instantiation later.*


### prepare_config (method, L62-L65, parent: LangChainChatModelFactory)

> *Summary: This method modifies an input configuration dictionary by removing specific keys like `"api_type"` and `"response_format"`. It returns the cleaned-up configuration dictionary for subsequent use.*


### create (method, L69-L70, parent: LangChainChatModelFactory)

> *Summary: This method constructs a `BaseChatModel` instance using the provided configuration dictionary for the initial language model. It serves as a factory to instantiate chat models based on input settings.*


### get_api_type (method, L74-L74, parent: LangChainChatModelFactory)

> *Summary: Determines the specific API type string associated with a given class object. It takes a class as input and returns its corresponding API type identifier.*


### accepts (method, L77-L78, parent: LangChainChatModelFactory)

> *Summary: Determines if a class is compatible with an LLM configuration dictionary by comparing the `api_type` specified in the config against the class's inherent API type. It returns a boolean indicating this match.*


### ChatOpenAIFactory (class, L82-L91)

> *Summary: This factory method constructs a `ChatOpenAI` instance by taking a configuration dictionary, preparing it internally, and instantiating the model. It also provides a static method to identify its associated API type as "openai".*


### create (method, L84-L87, parent: ChatOpenAIFactory)

> *Summary: This method constructs a `ChatOpenAI` instance by first validating and preparing the provided configuration dictionary using a class-specific preparation step, then instantiating the model with the resulting parameters.*


### get_api_type (method, L90-L91, parent: ChatOpenAIFactory)

> *Summary: This method unconditionally returns the string `"openai"` when provided with a class object. It serves to identify or categorize an API type, currently hardcoded for OpenAI compatibility.*


### DeepSeekFactory (class, L95-L104)

> *Summary: This factory extends a base class to specifically handle DeepSeek API configurations. It requires a `base_url` in the input configuration dictionary and returns an instance of `ChatOpenAI`, identifying itself as the "deepseek" type.*


### create (method, L97-L100, parent: DeepSeekFactory)

> *Summary: This method validates that a `base_url` exists within the provided configuration dictionary before calling the parent's creation logic. It ensures necessary API endpoint information is present when initializing a specific chat model instance.*


### get_api_type (method, L103-L104, parent: DeepSeekFactory)

> *Summary: This method unconditionally returns the string `"deepseek"` when provided with a class object. It serves to identify or categorize the API type associated with the input class.*


### ChatAnthropicFactory (class, L108-L117)

> *Summary: This factory method constructs a `ChatAnthropic` instance by taking a configuration dictionary, preparing it internally, and instantiating the model. It also provides a static method to identify this factory as belonging to the "anthropic" API type.*


### create (method, L110-L113, parent: ChatAnthropicFactory)

> *Summary: This method constructs and returns a `ChatAnthropic` instance by first validating and preparing the provided configuration dictionary. It takes one configuration dictionary as input to initialize the chat model object.*


### get_api_type (method, L116-L117, parent: ChatAnthropicFactory)

> *Summary: This method statically returns the string `"anthropic"` when provided a class object, indicating the expected API type for that model.*


### ChatGoogleGenerativeAIFactory (class, L121-L139)

> *Summary: This factory creates a `ChatGoogleGenerativeAI` instance by mapping an LLM configuration dictionary to the Google Generative AI model. It specifically targets the AI Studio endpoint using a provided API key for authentication.*


### create (method, L132-L135, parent: ChatGoogleGenerativeAIFactory)

> *Summary: This method constructs a `ChatGoogleGenerativeAI` instance by first normalizing the provided configuration dictionary using a class-specific preparation step, and then instantiating the model with the resulting parameters.*


### get_api_type (method, L138-L139, parent: ChatGoogleGenerativeAIFactory)

> *Summary: Determines the API type for a given class instance, currently hardcoded to return `"google"`. This function takes a class object as input and outputs a string identifying the model's API.*


### ChatVertexAIFactory (class, L143-L170)

> *Summary: This factory creates a `ChatVertexAI` instance by mapping an LLM configuration dictionary to the Vertex AI endpoint. It handles normalization, specifically converting an input `project_id` field into the required `project` argument for the underlying model.*


### create (method, L159-L166, parent: ChatVertexAIFactory)

> *Summary: This method constructs a `ChatVertexAI` instance by taking an initial configuration dictionary. It normalizes the input by converting a potential `"project_id"` key to the required `"project"` key before instantiating and returning the model object.*


### get_api_type (method, L169-L170, parent: ChatVertexAIFactory)

> *Summary: This method determines the API type for a given class, hardcoding the return value to `"google_vertex"` regardless of the input. It serves as a simple factory helper to identify the underlying model interface.*


### AzureChatOpenAIFactory (class, L174-L187)

> *Summary: This factory method constructs an `AzureChatOpenAI` instance from a configuration dictionary, validating that required parameters like `base_url` and `api_version` are present. It transforms the input by renaming `"base_url"` to `"azure_endpoint"` before instantiation.*


### create (method, L176-L183, parent: AzureChatOpenAIFactory)

> *Summary: This method constructs an `AzureChatOpenAI` instance by validating and transforming the provided configuration dictionary. It ensures required Azure parameters are present, renames `"base_url"` to `"azure_endpoint"`, and then instantiates the model with the processed settings.*


### get_api_type (method, L186-L187, parent: AzureChatOpenAIFactory)

> *Summary: This method unconditionally returns the string `"azure"` when provided with a class object. It serves to identify or categorize an API type, though its current implementation is static.*


### ChatOllamaFactory (class, L191-L204)

> *Summary: This factory method constructs a `ChatOllama` instance from a configuration dictionary, ensuring the necessary base URL is set and defaulting the context window size to 32000 if not provided. It also provides a static method to identify this implementation as an "ollama" API type.*


### create (method, L193-L200, parent: ChatOllamaFactory)

> *Summary: This method constructs a `ChatOllama` instance by taking an initial configuration dictionary. It preprocesses the input, sets default values for context size if missing, and returns a fully configured chat model object.*


### get_api_type (method, L203-L204, parent: ChatOllamaFactory)

> *Summary: This method inspects a class and consistently returns the string `"ollama"`, indicating the expected API type for that model implementation.*

