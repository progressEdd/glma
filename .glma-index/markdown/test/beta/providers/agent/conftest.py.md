# test/beta/providers/agent/conftest.py

7 function(s): _require, _require_gemini_key, openai_config, anthropic_config, gemini_config, streaming_config, provider_config.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _require | function |  |
| _require_gemini_key | function |  |
| openai_config | function |  |
| anthropic_config | function |  |
| gemini_config | function |  |
| streaming_config | function |  |
| provider_config | function |  |

## Chunks

### _require (function, L24-L28)

> *Summary: Retrieves an environment variable specified by the input string, skipping the test if the variable is not set in the environment. It returns the retrieved environment variable's value upon success.*


### _require_gemini_key (function, L31-L35)

> *Summary: Checks for the presence of either `GEMINI_API_KEY` or `GOOGLE_API_KEY` environment variables. If found, it returns the API key string; otherwise, it skips tests that require a live API connection.*


### openai_config (function, L39-L44)

> *Summary: This function constructs and returns an `OpenAIConfig` object, requiring the `OPENAI_API_KEY` environment variable to initialize with a specific model ("gpt-5.4-nano") and zero temperature. It serves as a standardized configuration provider for OpenAI interactions within tests.*


### anthropic_config (function, L48-L53)

> *Summary: This function constructs and returns an `AnthropicConfig` object, requiring the `ANTHROPIC_API_KEY` environment variable. It configures the provider to use the "claude-haiku-4-5" model with a fixed temperature of zero.*


### gemini_config (function, L57-L62)

> *Summary: Creates and returns a `GeminiConfig` object configured to use the "gemini-3.1-flash-lite-preview" model with a temperature of 0, sourcing the necessary API key from an external requirement function.*


### streaming_config (function, L72-L96)

> *Summary: This function generates provider-specific configuration objects for tests that require streaming capabilities. It takes a parameter indicating the desired provider ("openai", "anthropic", or default to Gemini) and returns the corresponding configured object with `streaming=True`.*


### provider_config (function, L106-L114)

> *Summary: This fixture dynamically retrieves a specific configuration object based on a provided parameter, ensuring tests run once per provider. It uses lazy resolution to prevent dependency issues when running tests against only a subset of available providers.*

