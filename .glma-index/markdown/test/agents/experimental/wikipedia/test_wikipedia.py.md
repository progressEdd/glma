# test/agents/experimental/wikipedia/test_wikipedia.py

1 class(es): TestWikipediaAgent. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestWikipediaAgent | class |  |

## Chunks

### TestWikipediaAgent (class, L13-L69)

> *Summary: This test suite verifies the initialization and configuration of a Wikipedia-aware agent. It asserts that the agent correctly registers specific tools, sets default system messages, and properly passes through extra keyword arguments during instantiation.*


### test_init (method, L14-L43, parent: TestWikipediaAgent)

> *Summary: Verifies that an initialized `WikipediaAgent` correctly sets its name, configures the LLM settings, registers specific Wikipedia tools, and assigns a default system message based on provided credentials. It asserts that the registered tools match expected names both on the agent instance and within the LLM configuration dictionary.*


### test_format_instructions (method, L45-L57, parent: TestWikipediaAgent)

> *Summary: When provided with specific formatting instructions, the agent's system message is constructed by appending those instructions to a predefined default message. This test verifies that the `format_instructions` argument correctly modifies the final system prompt sent to the language model.*


### test_extra_kwargs_pass_through (method, L59-L69, parent: TestWikipediaAgent)

> *Summary: Verifies that extra keyword arguments passed during the initialization of a `WikipediaAgent` instance are correctly forwarded and accessible on the resulting object. It confirms that the provided `description` argument is set as expected.*

