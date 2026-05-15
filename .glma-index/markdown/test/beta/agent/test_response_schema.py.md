# test/beta/agent/test_response_schema.py

2 class(es): TestAgentLevelResponseSchema, TestAskLevelResponseSchema. 23 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestAgentLevelResponseSchema | class |  |
| TestAskLevelResponseSchema | class |  |

## Chunks

### TestAgentLevelResponseSchema (class, L16-L177)

> *Summary: This test suite verifies the `Agent`'s ability to parse and return structured data from an LLM response based on various schema inputs, including basic types, dataclasses, Pydantic models, custom schemas, callables, and prompted structures. It also tests error handling for validation failures and confirms retry logic functions correctly under different failure scenarios.*


### test_type_response_schema (method, L17-L23, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an `Agent` configured with a specific integer schema correctly processes a prompt and returns the expected value from its response content. It asserts that the retrieved content matches the predefined data within the configuration.*


### test_dataclass_response_schema (method, L25-L36, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an `Agent` correctly parses and returns a structured response matching a defined dataclass schema (`Point`). It initializes the agent with configuration data and asserts that the content retrieved from the agent's reply matches the expected instance of the schema.*


### test_pydantic_response_schema (method, L38-L50, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an `Agent` correctly parses and returns a structured response matching a defined Pydantic schema (`User`). It initializes the agent with configuration data and asserts that the resulting content is an instance of the expected model containing the correct input values.*


### test_response_schema_object (method, L52-L59, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent correctly processes a request and returns the expected value based on a predefined `ResponseSchema`. It initializes an agent with a schema expecting an integer, sends it a prompt, and asserts the resulting content matches the configured data.*


### test_callable_response_schema (method, L61-L71, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent correctly executes a callable response schema, which doubles the input string's integer value. It asserts that calling the resulting content yields the expected doubled integer (42).*


### test_async_callable_response_schema (method, L73-L83, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent correctly executes a response schema defined as an asynchronous callable. It passes input to the `double` function via the agent's query and asserts the final returned value is twice the expected input content converted to an integer.*


### test_prompted_schema_with_type (method, L85-L91, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent, configured with a specific `response_schema` expecting an integer, correctly processes a prompt and returns the expected integer value from its response content. It asserts that the retrieved content matches the predefined schema type.*


### test_prompted_schema_with_response_schema (method, L93-L100, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent correctly processes a prompt and returns the expected integer value based on a predefined response schema. It initializes an agent with a specific configuration and a `PromptedSchema` wrapping an `int` type, then asserts the final output matches the configured data.*


### test_prompted_schema_with_callable (method, L102-L112, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent correctly executes a callable defined within a response schema when prompted. It asserts that the agent's output, after processing the input "Hi!", results in the value 42 by doubling the parsed content.*


### test_no_schema_returns_string (method, L114-L120, parent: TestAgentLevelResponseSchema)

> *Summary: When an agent is initialized without a specific response schema, calling its `ask` method and then retrieving the content returns a plain string matching the configuration's input value. This test verifies that the default behavior yields a simple string output.*


### test_validation_error (method, L122-L128, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an `Agent` raises an exception when initialized with invalid configuration data, specifically when the provided schema type cannot handle the input value. It asserts that calling `.content()` on the resulting response will trigger the expected error.*


### test_retry_succeeds_on_second_attempt (method, L130-L142, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent successfully processes a request after one automatic retry. It initializes the agent with a configuration designed to fail initially, then asserts that the final output matches the expected value and that the underlying service was called exactly twice.*


### test_retry_with_prompted_schema_omits_null_schema (method, L144-L154, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that when an agent's response schema is provided, retrying the request with a prompt will omit any null values from the final output. It asserts that the resulting content matches the expected integer value after one retry attempt.*


### test_retry_exhausted_raises (method, L156-L166, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that attempting to process a response after exhausting all retries raises an exception. It initializes an agent with a failing configuration and asserts that the underlying request mechanism is called exactly twice (initial attempt plus one retry).*


### test_retries_keeps_retrying (method, L168-L177, parent: TestAgentLevelResponseSchema)

> *Summary: This test verifies that an agent continues to retry its request indefinitely when configured with infinite retries. It asserts that the underlying mock call count increases by four, confirming one initial attempt plus three subsequent retries resulted in a final output of 7.*


### TestAskLevelResponseSchema (class, L181-L250)

> *Summary: This test suite verifies various ways to specify and override the expected output format when querying an `Agent`. It demonstrates that providing different schema types (like built-in types, custom objects, or callables) during a single `ask` call dictates the result, while subsequent calls revert to the agent's inherent configuration.*


### test_ask_type_override (method, L182-L188, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that an `Agent` correctly uses a provided type hint (`int`) in the `response_schema` argument when processing an input query. It asserts that the final extracted content matches the value specified in the agent's configuration data.*


### test_ask_response_schema_object (method, L190-L196, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that an `Agent` correctly processes a request against a specified schema. It sends the prompt "Hi!" to the agent with a target integer schema and asserts that the resulting content matches the expected value of 42 from the configuration.*


### test_ask_callable_override (method, L198-L208, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that an agent correctly uses a custom callable as a response schema. It passes the string "Hi!" to the agent, which then executes the provided `double` function on its output and asserts the final integer result is 42.*


### test_ask_prompted_schema_override (method, L210-L216, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that an agent correctly uses a provided schema override when responding to a prompt. It initializes an agent with specific configuration data and asserts the returned content matches the expected value defined in the schema.*


### test_ask_overrides_agent_schema (method, L218-L224, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that providing a `response_schema` during the `.ask()` call overrides the schema defined in the `Agent`'s configuration. It asserts that the final content returned matches the value specified by the runtime override (`float`).*


### test_ask_none_drops_schema (method, L226-L232, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that when an agent is queried with `response_schema=None`, the returned content matches a predefined expected string value from its configuration. It confirms the agent correctly processes the request without imposing a specific output schema.*


### test_next_turn_preserves_agent_schema (method, L234-L241, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that an agent maintains its response schema across subsequent interactions. It initializes an agent with a specific schema and confirms the output changes correctly from the initial prompt to a follow-up query.*


### test_ask_override_does_not_persist (method, L243-L250, parent: TestAskLevelResponseSchema)

> *Summary: This test verifies that an initial instruction provided via `response_schema` is not retained across subsequent calls to the agent's `ask` method. It confirms the agent correctly switches its behavior from returning a float based on the first call to returning a string ("42") on the second call.*

