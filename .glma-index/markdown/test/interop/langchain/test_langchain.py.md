# test/interop/langchain/test_langchain.py

2 class(es): TestLangChainInteroperability, TestLangChainInteroperabilityWithoutPydanticInput. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLangChainInteroperability | class |  |
| TestLangChainInteroperabilityWithoutPydanticInput | class |  |

## Chunks

### TestLangChainInteroperability (class, L23-L75)

> *Summary: This test suite verifies the interoperability between a custom search tool and LangChain components. It sets up a mockable, decorated tool that accepts a structured input model and tests its conversion, execution with mocked inputs, and integration within an LLM-driven chat session using GPT-4o credentials.*


### setup (method, L25-L39, parent: TestLangChainInteroperability)

> *Summary: Initializes the test environment by creating a mock object and defining a mocked search tool using Pydantic for input validation. This process registers the tool with the class instance, converting it into an interoperable format.*


### test_type_checks (method, L41-L46, parent: TestLangChainInteroperability)

> *Summary: Verifies that an instance of `LangChainInteroperability` correctly implements the `Interoperable` interface at runtime. This test ensures type compatibility between components.*


### test_convert_tool (method, L48-L56, parent: TestLangChainInteroperability)

> *Summary: Verifies that a specific tool object has the correct name and description, then tests its execution by creating an input instance from its schema and asserting the returned string matches an expected value.*


### test_with_llm (method, L59-L72, parent: TestLangChainInteroperability)

> *Summary: This test initializes an `AssistantAgent` using provided GPT-4o credentials and registers it with a user proxy. It then initiates a chat session to prompt the agent about "LangChain" and asserts that mocking calls were made during this interaction.*


### test_get_unsupported_reason (method, L74-L75, parent: TestLangChainInteroperability)

> *Summary: Asserts that the `LangChainInteroperability` utility returns `None` when checking for an unsupported reason, verifying expected default behavior.*


### TestLangChainInteroperabilityWithoutPydanticInput (class, L79-L125)

> *Summary: This test verifies that a custom function can be successfully converted into an interoperable tool structure without relying on Pydantic input validation. It sets up a mock-backed search tool, converts it using `LangChainInteroperability`, and then executes it via an LLM agent interaction to confirm correct invocation and mocking behavior.*


### setup (method, L81-L92, parent: TestLangChainInteroperabilityWithoutPydanticInput)

> *Summary: Initializes a mock object and defines a decorated tool function that simulates an online search by calling the mock with provided query and length arguments. This setup then converts the defined tool into a `LangChainInteroperability` object for testing purposes.*


### test_convert_tool (method, L94-L101, parent: TestLangChainInteroperabilityWithoutPydanticInput)

> *Summary: This test verifies that a specific tool object correctly exposes its input schema as a `BaseModel`. It then executes the tool with sample inputs derived from that schema and asserts the returned output matches an expected string format.*


### test_with_llm (method, L104-L125, parent: TestLangChainInteroperabilityWithoutPydanticInput)

> *Summary: This test sets up an `AssistantAgent` configured with GPT-4o credentials and registers it to interact with a mock tool via a `UserProxyAgent`. It then initiates a chat session, expecting the agent to use the registered tool based on the prompt.*

