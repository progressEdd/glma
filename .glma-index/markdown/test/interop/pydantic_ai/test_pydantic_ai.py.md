# test/interop/pydantic_ai/test_pydantic_ai.py

3 class(es): TestPydanticAIInteroperabilityWithoutContext, TestPydanticAIInteroperabilityDependencyInjection, TestPydanticAIInteroperabilityWithContext. 10 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestPydanticAIInteroperabilityWithoutContext | class |  |
| TestPydanticAIInteroperabilityDependencyInjection | class |  |
| TestPydanticAIInteroperabilityWithContext | class |  |

## Chunks

### TestPydanticAIInteroperabilityWithoutContext (class, L25-L60)

> *Summary: This test suite verifies the interoperability of a custom function wrapped as an AI tool. It initializes and tests the conversion of a simple dice-rolling function into an `Interoperable` object, ensuring correct metadata and successful execution when integrated with an LLM agent via a simulated chat session.*


### setup (method, L27-L33, parent: TestPydanticAIInteroperabilityWithoutContext)

> *Summary: Initializes a test fixture by creating a `PydanticAITool` wrapper around a dice-rolling function and then converting this tool into an interoperable format for testing. The resulting converted tool is stored in the instance's `self.tool` attribute.*


### test_type_checks (method, L35-L39, parent: TestPydanticAIInteroperabilityWithoutContext)

> *Summary: Verifies that an instance created from `PydanticAIInteroperability` correctly adheres to the `Interoperable` interface at runtime. This test ensures type correctness for interoperability structures.*


### test_convert_tool (method, L41-L44, parent: TestPydanticAIInteroperabilityWithoutContext)

> *Summary: Verifies that an initialized tool object has the correct name and description, and confirms its execution returns one of the expected six possible string outcomes.*


### test_with_llm (method, L47-L60, parent: TestPydanticAIInteroperabilityWithoutContext)

> *Summary: This test verifies that an AI agent correctly uses a registered tool when prompted by a user proxy. It initiates a short conversation and asserts that the resulting message from the chatbot contains a valid die roll result from the tool execution.*


### TestPydanticAIInteroperabilityDependencyInjection (class, L64-L127)

> *Summary: This test verifies that parameter injection correctly maps function arguments from a `RunContext` and provided keyword arguments to a target callable. It also confirms the mechanism handles exceptions by retrying the execution up to a specified limit, updating the context's retry count accordingly.*


### test_dependency_injection (method, L65-L91, parent: TestPydanticAIInteroperabilityDependencyInjection)

> *Summary: This test verifies that parameter injection correctly resolves dependencies for a given function. It takes a `RunContext` containing dependency values and returns an injectable callable, which is then tested by calling it with keyword arguments to ensure the correct output string is generated using the injected context data.*


### test_dependency_injection_with_retry (method, L93-L127, parent: TestPydanticAIInteroperabilityDependencyInjection)

> *Summary: This test verifies that parameter injection correctly handles function execution with automatic retries when the underlying function raises a specific error. It asserts that the retry counter increments correctly during transient failures and ultimately fails after exhausting the maximum allowed attempts.*


### TestPydanticAIInteroperabilityWithContext (class, L132-L205)

> *Summary: This test suite verifies the interoperability of a Pydantic-backed AI tool with an agent system. It sets up a function that retrieves player details from a context object and asserts that this tool is correctly serialized for LLMs and successfully executed during a simulated chat interaction.*


### setup (method, L134-L150, parent: TestPydanticAIInteroperabilityWithContext)

> *Summary: This method initializes a test setup by defining a Pydantic model for a player and creating an AI tool that retrieves the player's name and age from a context object. It then converts this specialized tool into a generic interoperability format using provided dependency data.*


### test_convert_tool_raises_error_if_take_ctx_is_true_and_deps_is_none (method, L152-L154, parent: TestPydanticAIInteroperabilityWithContext)

> *Summary: Asserts that calling `convert_tool` with a Pydantic AI tool and `deps=None` raises a `ValueError` if the tool is configured to require context. This verifies the dependency check logic within the interoperability conversion process.*


### test_expected_tools (method, L156-L184, parent: TestPydanticAIInteroperabilityWithContext)

> *Summary: This test verifies that an `AssistantAgent` correctly registers a predefined set of tools with its LLM configuration when initialized with specific API settings. It asserts that the agent's internal tool list matches the expected structure containing a function definition for "get\_player".*


### test_with_llm (method, L187-L205, parent: TestPydanticAIInteroperabilityWithContext)

> *Summary: This test verifies an LLM interaction by setting up a chatbot agent and registering tools for execution. It initiates a chat with the chatbot and asserts that a specific tool response containing player information is received within the conversation history.*

