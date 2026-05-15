# test/agentchat/test_dependency_injection.py

12 function(s): f_with_annotated, f_with_annotated_async, f_without_annotated, f_without_annotated_async, f_with_annotated_and_depends, f_with_annotated_and_depends_async, f_with_multiple_depends, f_with_multiple_depends_async, f_without_base_context, f_without_base_context_async and 2 more. 2 class(es): MyContext, TestDependencyInjection. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MyContext | class |  |
| f_with_annotated | function |  |
| f_with_annotated_async | function |  |
| f_without_annotated | function |  |
| f_without_annotated_async | function |  |
| f_with_annotated_and_depends | function |  |
| f_with_annotated_and_depends_async | function |  |
| f_with_multiple_depends | function |  |
| f_with_multiple_depends_async | function |  |
| f_without_base_context | function |  |
| f_without_base_context_async | function |  |
| f_with_default_depends | function |  |
| f_with_default_depends_async | function |  |
| TestDependencyInjection | class |  |

## Chunks

### MyContext (class, L19-L20)

> *Summary: This class inherits from `BaseContext` and `BaseModel`, initializing an instance attribute named `b` as an integer. It serves as a context object that incorporates base model functionality.*


### f_with_annotated (function, L23-L31)

> *Summary: This function accepts an integer `a`, a context object derived from dependencies (`ctx`), and a chat context object (`chat_ctx`). It returns the sum of `a`, the `b` attribute from the context, and the optional integer `c`.*


### f_with_annotated_async (function, L34-L42)

> *Summary: This asynchronous function accepts an integer `a`, a context object derived from dependency injection with a fixed value of 2 for its internal `b` field, and a `ChatContext`. It returns the sum of `a`, the injected context's `b` value, and an optional integer `c`.*


### f_without_annotated (function, L45-L52)

> *Summary: This function accepts an integer `a`, a `ChatContext` object, and context values derived from dependencies (`ctx`) and annotations (`c`, `d`). It returns the sum of `a`, the `b` attribute from `ctx`, and the annotated value `c`.*


### f_without_annotated_async (function, L55-L61)

> *Summary: This asynchronous function accepts an integer `a`, a context object derived from dependencies, and two optional annotated integers/nullable integers (`c` and `d`). It returns the sum of `a`, the context's internal value `ctx.b`, and the annotated value `c`.*


### f_with_annotated_and_depends (function, L64-L70)

> *Summary: This function accepts an integer `a`, a context object `ctx` with a default value for its internal field `b`, and two optional annotated integers/nullable integers (`c` and `d`). It returns the sum of `a`, `ctx.b`, and the value of `c`.*


### f_with_annotated_and_depends_async (function, L73-L79)

> *Summary: This asynchronous function accepts an integer `a`, a context object `ctx` with a default value, and two annotated integers (`c` and `d`) with defaults. It returns the sum of `a`, `ctx.b`, and the value of `c`.*


### f_with_multiple_depends (function, L82-L89)

> *Summary: This function accepts an integer `a`, two context objects (`ctx` and `ctx2`) initialized with specific values, and optional integers `c` and `d`. It returns the sum of `a`, the `b` attribute from both context objects, and the value of `c`.*


### f_with_multiple_depends_async (function, L92-L99)

> *Summary: This asynchronous function accepts an integer and two context objects, each initialized with a specific value for `b`, along with optional integers. It returns the sum of the input integer, the `b` values from both contexts, and the provided integer `c`.*


### f_without_base_context (function, L102-L108)

> *Summary: This function accepts an integer `a`, a context value derived by adding two to `a` via dependency injection, and optional integers/None values for `c` and `d`. It returns the sum of `a`, the injected context value, and `c`.*


### f_without_base_context_async (function, L111-L117)

> *Summary: This asynchronous function accepts an integer `a` and another integer `ctx`, which is derived by adding 2 to `a`. It also takes optional integers or `None` for parameters `c` and `d`, ultimately returning the sum of `a`, `ctx`, and `c`.*


### f_with_default_depends (function, L120-L126)

> *Summary: This function accepts an integer `a` and uses dependency injection for `ctx`, which is calculated by adding 2 to the input `a`. It also takes optional annotated arguments `c` (defaulting to 3) and `d` (defaulting to None), returning the sum of `a`, `ctx`, and `c`.*


### f_with_default_depends_async (function, L129-L135)

> *Summary: This asynchronous function accepts an integer `a` and uses dependency injection for `ctx`, which is calculated by adding two to the input `a`. It also takes optional annotated arguments `c` (defaulting to 3) and `d` (defaulting to None), returning the sum of `a`, `ctx`, and `c`.*


### TestDependencyInjection (class, L138-L267)

> *Summary: This test class verifies dependency injection and tool registration within an agent system. It uses parameterized tests to validate function execution with various configurations (sync/async, annotated/non-annotated) against expected outputs, and includes end-to-end tests simulating a chat interaction that requires external dependencies like user context.*


### expected_tools (method, L140-L162, parent: TestDependencyInjection)

> *Summary: Returns a list containing a single dictionary defining an example function schema. This structure specifies the function's name ("f"), description, and detailed parameter definitions including types, required fields, and default values for inputs like `a`, `c`, and `d`.*


### test_register_tools (method, L182-L203, parent: TestDependencyInjection)

> *Summary: This test verifies that a provided function is correctly registered with an agent for both LLM awareness and execution capabilities. It asserts the tool configuration matches expectations, confirms the function is mapped internally, and finally executes the function to validate its output against an expected value.*


### _test_end2end (method, L205-L256, parent: TestDependencyInjection)

> *Summary: This test verifies end-to-end interaction by setting up an agent and a user proxy to execute a mocked login function. It simulates both asynchronous and synchronous chat initiation, asserting that the mock was called exactly once with the correct user context and success message.*


### test_end2end (method, L262-L267, parent: TestDependencyInjection)

> *Summary: This test method executes an end-to-end workflow by calling a private helper function. It accepts `Credentials` and a boolean flag to determine if the execution should be asynchronous.*

