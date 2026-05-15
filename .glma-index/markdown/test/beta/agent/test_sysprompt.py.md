# test/beta/agent/test_sysprompt.py

11 function(s): test_sysprompt, test_multiple_sysprompts, test_sysprompt_reuse, test_sysprompt_override_with_call, test_callable_sysprompt, test_callable_sysprompt_called_once, test_decorator_sysprompt, test_callable_sysprompt_decorator, test_mixed_sysprompts, test_prompt_mutation and 1 more. 2 class(es): CustomEvent, MockClient. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CustomEvent | class |  |
| MockClient | class |  |
| test_sysprompt | function |  |
| test_multiple_sysprompts | function |  |
| test_sysprompt_reuse | function |  |
| test_sysprompt_override_with_call | function |  |
| test_callable_sysprompt | function |  |
| test_callable_sysprompt_called_once | function |  |
| test_decorator_sysprompt | function |  |
| test_callable_sysprompt_decorator | function |  |
| test_mixed_sysprompts | function |  |
| test_prompt_mutation | function |  |
| test_prompt_mutation_from_subscriber | function |  |

## Chunks

### CustomEvent (class, L16-L17)

> *Summary: This class inherits from `BaseEvent` to represent a custom event within the system. It serves as a basic, specialized event structure for internal communication or state changes.*


### MockClient (class, L20-L35)

> *Summary: This class simulates an LLM client by wrapping a `MagicMock` object for controlled testing. When called with messages and context, it sends a custom event via the context and then executes the mock against the prompt before returning a predefined successful response.*


### __init__ (method, L21-L22, parent: MockClient)

> *Summary: Initializes the object by storing a provided `MagicMock` instance as an internal attribute for later use in tests.*


### create (method, L24-L25, parent: MockClient)

> *Summary: Returns a reference to the current instance, effectively acting as a factory or builder pattern method for creating a mock client object.*


### __call__ (method, L27-L35, parent: MockClient)

> *Summary: This asynchronous method simulates an agent's response by first sending a custom event and mocking the prompt context. It then immediately returns a predefined `ModelResponse` containing a greeting message.*


### test_sysprompt (function, L39-L49)

> *Summary: This test verifies that an `Agent` correctly uses its system prompt when responding to user input. It asserts that the underlying mock client was called with the configured system prompt and confirms the resulting conversation context contains this prompt.*


### test_multiple_sysprompts (function, L53-L63)

> *Summary: This test verifies that an `Agent` correctly uses a provided list of system prompts when interacting with the underlying client. It asserts that the agent calls the mock client with the expected prompt array and that the resulting conversation context reflects those initial prompts.*


### test_sysprompt_reuse (function, L67-L78)

> *Summary: This test verifies that the system prompt is correctly reused across multiple turns of an agent's conversation. It asserts that the underlying client method was called exactly twice, once for each turn, passing the initial system prompt as input.*


### test_sysprompt_override_with_call (function, L82-L90)

> *Summary: This test verifies that an `Agent` correctly calls its underlying client when prompted with specific input. It asserts that the mock client receives exactly one call containing the provided list of inputs (`["1"]`).*


### test_callable_sysprompt (function, L94-L105)

> *Summary: This test verifies that an `Agent` correctly invokes a callable system prompt when asked a question. It asserts that the underlying mock client receives the string returned by the provided prompt function as its input.*


### test_callable_sysprompt_called_once (function, L109-L123)

> *Summary: This test verifies that a provided system prompt function is executed exactly once when an agent processes two consecutive user inputs. It achieves this by mocking the prompt execution and asserting the call count after running the agent's `ask` method twice.*


### test_decorator_sysprompt (function, L127-L135)

> *Summary: This test verifies that an agent correctly uses a decorated system prompt when responding to a query. It asserts that the underlying mock client receives the string returned by the decorated function ("1") as its input during the `ask` call.*


### test_callable_sysprompt_decorator (function, L139-L147)

> *Summary: This test verifies that the `@agent.prompt()` decorator correctly injects a predefined system prompt into the agent's interaction flow. It asserts that when `agent.ask()` is called, the underlying mock client receives the string returned by the decorated function as its input argument.*


### test_mixed_sysprompts (function, L151-L164)

> *Summary: This test verifies that an agent correctly executes a mix of static and dynamic system prompts when processing an input event. It asserts that the underlying client mock is called with the sequence of prompt results: the initial static prompt followed by the return value from the custom asynchronous prompt function.*


### test_prompt_mutation (function, L168-L190)

> *Summary: This test verifies that an agent correctly updates its internal prompt state across multiple interactions. It confirms that subsequent calls to `ask` use the newly set prompt value, as validated by mock assertions on the underlying client calls.*


### test_prompt_mutation_from_subscriber (function, L194-L209)

> *Summary: This test verifies that an agent's prompt can be mutated by a subscriber listening for `CustomEvent`s during an interaction. It asserts that after the mutation occurs via the event handler, the underlying client method is called with the updated prompt content.*

