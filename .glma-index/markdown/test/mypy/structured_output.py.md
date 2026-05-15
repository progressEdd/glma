# test/mypy/structured_output.py

16 function(s): check_default_response_schema, check_int_response_schema, check_dataclass_response_schema, check_union_response_schema, check_response_schema_object, check_sync_callable_response, check_async_callable_response, check_conversation_save_type, check_ask_overrides_response_type, check_ask_none_drops_response_type and 6 more. 1 class(es): CheckResponseSchema. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CheckResponseSchema | class |  |
| check_default_response_schema | function |  |
| check_int_response_schema | function |  |
| check_dataclass_response_schema | function |  |
| check_union_response_schema | function |  |
| check_response_schema_object | function |  |
| check_sync_callable_response | function |  |
| check_async_callable_response | function |  |
| check_conversation_save_type | function |  |
| check_ask_overrides_response_type | function |  |
| check_ask_none_drops_response_type | function |  |
| check_ask_response_type_not_affect_next_turn | function |  |
| check_prompted_schema_with_type | function |  |
| check_prompted_schema_with_dataclass | function |  |
| check_prompted_schema_with_response_schema | function |  |
| check_prompted_schema_with_callable | function |  |
| check_prompted_schema_ask_override | function |  |

## Chunks

### CheckResponseSchema (class, L13-L25)

> *Summary: This class provides unit tests to validate the `ResponseSchema` functionality. It verifies that the schema correctly handles `None`, primitive types like `str`, and nested schemas by asserting the resulting type matches expectations.*


### check_none (method, L14-L16, parent: CheckResponseSchema)

> *Summary: It validates that the `ResponseSchema` correctly handles a `None` input by asserting its resulting type is also `None`. This method ensures schema generation works as expected when no data is provided.*


### check_primitive (method, L18-L20, parent: CheckResponseSchema)

> *Summary: This method verifies that the schema generated for a string type conforms to the expected `ResponseSchema[str]` structure. It achieves this by first ensuring the input type is correctly represented as a schema object.*


### check_schema (method, L22-L25, parent: CheckResponseSchema)

> *Summary: This method validates a schema by first ensuring the input type is represented as a `ResponseSchema`, then nesting that schema within another `ResponseSchema`. It asserts that the final resulting structure conforms to the expected `ResponseSchema[str]` type.*


### check_default_response_schema (function, L28-L37)

> *Summary: This test verifies the structure of a default response from an `Agent` by sending it a simple prompt and asserting that both the body and content fields are either strings or null. It confirms the expected type contract for the agent's output.*


### check_int_response_schema (function, L40-L50)

> *Summary: This test verifies that an agent configured to return an integer adheres to the expected output structure when queried. It asserts that the raw response body is a string or null, while the parsed content is an integer or null.*


### check_dataclass_response_schema (function, L53-L67)

> *Summary: This test verifies that an agent configured with a specific dataclass schema correctly returns structured output. It calls the agent with a prompt and asserts that the response body is a string and the content adheres to the defined `Response` structure.*


### check_union_response_schema (function, L70-L80)

> *Summary: This test verifies that an agent configured to return a union type (`int | str`) correctly produces responses whose body is `str | None` and content is `int | str | None`. It achieves this by querying the agent with a simple prompt.*


### check_response_schema_object (function, L83-L92)

> *Summary: This test verifies that an agent configured with a specific response schema correctly returns data types matching the expected structure. It sends a prompt to the agent and asserts that the body is a string or null, while the content is an integer or null.*


### check_sync_callable_response (function, L95-L108)

> *Summary: This test verifies that an agent correctly processes a string input according to a defined response schema, which expects an integer output. It asserts that the initial body is a string and the final content resolves to an integer or `None`.*


### check_async_callable_response (function, L111-L124)

> *Summary: This test verifies that an agent correctly processes a response conforming to a defined asynchronous schema. It sends a prompt and asserts the resulting body is a string while the content, which should be an integer, can be awaited.*


### check_conversation_save_type (function, L127-L140)

> *Summary: This test verifies that an `Agent` configured with a response schema of `int` correctly returns string content in its body and integer content when the `.content()` method is called, across multiple conversational turns. It asserts the expected types for both the initial and subsequent responses from the agent.*


### check_ask_overrides_response_type (function, L143-L152)

> *Summary: This test verifies that an agent's response type can be overridden using a provided schema. It asserts that the initial body remains a string while the content adheres to the specified integer type when `response_schema=int` is passed during the query.*


### check_ask_none_drops_response_type (function, L155-L164)

> *Summary: This test verifies that when an agent is configured to accept `int` responses but asked with `response_schema=None`, the resulting reply body and content are correctly typed as `str | None`. It instantiates an agent, sends a prompt, and asserts the expected nullable string types on the response.*


### check_ask_response_type_not_affect_next_turn (function, L167-L180)

> *Summary: This test verifies that the response type specified in one turn does not constrain the expected output type of subsequent turns. It asserts that after an initial request expecting a `float`, the next turn can successfully be prompted to return an `int`, and a third turn reverts to expecting a `float`.*


### check_prompted_schema_with_type (function, L183-L192)

> *Summary: This test verifies that an agent configured with a `PromptedSchema` expecting an integer correctly returns the expected types for its response body and content. It sends a prompt to the agent and asserts the resulting structure matches the defined schema constraints.*


### check_prompted_schema_with_dataclass (function, L195-L209)

> *Summary: This test verifies that an agent correctly adheres to a predefined dataclass schema when responding to a prompt. It initializes the agent with a `Response` dataclass and asserts that the content returned by the agent matches this expected structure.*


### check_prompted_schema_with_response_schema (function, L212-L223)

> *Summary: This test verifies that an agent correctly adheres to a specified response schema when prompted. It initializes an agent with a `PromptedSchema` wrapping a target integer type and asserts the resulting content matches the expected integer structure.*


### check_prompted_schema_with_callable (function, L226-L239)

> *Summary: This test verifies that an agent correctly uses a callable function as its response schema. It prompts the agent with text and asserts that the raw body is a string while the parsed content adheres to the expected integer type defined by the callable.*


### check_prompted_schema_ask_override (function, L242-L247)

> *Summary: This test verifies that when a `response_schema` is provided to an agent's `ask` method, the returned body type matches the expected string structure while the content itself adheres to the specified integer schema. It confirms the correct handling of mixed return types based on the prompt and schema constraints.*

