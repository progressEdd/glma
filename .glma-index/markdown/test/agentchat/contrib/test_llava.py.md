# test/agentchat/contrib/test_llava.py

3 class(es): TestLLaVAAgent, TestLLavaCallBinaryWithConfig, TestLLavaCall. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLLaVAAgent | class |  |
| TestLLavaCallBinaryWithConfig | class |  |
| TestLLavaCall | class |  |

## Chunks

### TestLLaVAAgent (class, L19-L35)

> *Summary: This test verifies the initialization of an agent configured to use a mock LLava model endpoint. It confirms that an instance of `LLaVAAgent` is correctly created with specified configuration parameters.*


### test_init (method, L20-L35, parent: TestLLaVAAgent)

> *Summary: Instantiates an agent configured to use a mock LLava model endpoint. It verifies that the resulting object is correctly typed as an `LLaVAAgent`.*


### TestLLavaCallBinaryWithConfig (class, L39-L93)

> *Summary: This test suite verifies the `_llava_call_binary_with_config` function's behavior in two modes. It asserts that when called with a prompt and configuration, the function correctly makes HTTP requests (in local mode) or uses Replicate's API (in remote mode) to return the expected text output based on mocked responses.*


### test_local_mode (method, L41-L71, parent: TestLLavaCallBinaryWithConfig)

> *Summary: This test verifies the local mode functionality by mocking an HTTP POST request to simulate a backend response. It asserts that the function correctly processes the mocked streamed output and that the underlying API call was made with the expected parameters.*


### test_remote_mode (method, L74-L93, parent: TestLLavaCallBinaryWithConfig)

> *Summary: This test verifies the remote execution path for an LLava call by mocking the `replicate.run` response to return specific text. It asserts that the function correctly processes the mocked output and that the underlying API call was made with the expected configuration, including the base URL and input data.*


### TestLLavaCall (class, L97-L126)

> *Summary: This test verifies the `llava_call` function by mocking its dependencies to simulate image formatting and LLM interaction. It asserts that the formatter is called with the prompt and that the binary call receives the formatted prompt, image tokens, and specific configuration parameters, ultimately confirming the expected return value.*


### test_llava_call (method, L100-L126, parent: TestLLavaCall)

> *Summary: This test verifies the `llava_call` function by mocking its dependencies to ensure it correctly formats a prompt and passes the resulting data along with configuration parameters to the underlying LLM call. It asserts that the formatter was called once with the input prompt and that the binary caller received the expected formatted prompt, image tokens, and specific configuration values.*

