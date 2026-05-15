# test/agentchat/realtime_agent/test_realtime_agent.py

2 function(s): f, f_async. 2 class(es): A, TestRealtimeAgent. 7 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| f | function |  |
| f_async | function |  |
| A | class |  |
| TestRealtimeAgent | class |  |

## Chunks

### f (function, L16-L17)

> *Summary: This function calculates the sum of two integers, where the second integer defaults to three if not provided. It accepts an initial integer and returns their total.*


### f_async (function, L20-L21)

> *Summary: This asynchronous function takes two integers, `a` and an optional `b`, and returns their sum. It performs simple addition asynchronously.*


### A (class, L24-L37)

> *Summary: This class provides four methods for integer addition: one instance method, an asynchronous instance method, and two static methods (one synchronous and one asynchronous). All methods accept two integers, with the second defaulting to three.*


### f (method, L25-L26, parent: A)

> *Summary: This method calculates the sum of two integers, where the second integer defaults to three if not provided. It accepts an initial integer and returns their total.*


### f_async (method, L28-L29, parent: A)

> *Summary: This asynchronous method takes two integers, `a` and an optional `b`, and returns their sum. It performs simple addition asynchronously.*


### f_static (method, L32-L33, parent: A)

> *Summary: This function takes two integers, `a` and an optional integer `b` defaulting to 3, and returns their sum. It performs simple addition based on the provided inputs.*


### f_static_async (method, L36-L37, parent: A)

> *Summary: This asynchronous function takes two integers, `a` and an optional `b`, and returns their sum. It performs simple addition asynchronously.*


### TestRealtimeAgent (class, L40-L96)

> *Summary: This test suite verifies the `RealtimeAgent`'s ability to register and execute functions as tools. It uses parameterized tests to check registration against a predefined schema and then executes both synchronous and asynchronous registered functions, asserting the return value matches an expected outcome.*


### agent (method, L42-L47, parent: TestRealtimeAgent)

> *Summary: Creates and returns a `RealtimeAgent` instance configured with provided LLM settings and a mocked audio adapter. This method takes credentials containing the necessary configuration as input to initialize the agent object.*


### expected_tools (method, L50-L63, parent: TestRealtimeAgent)

> *Summary: Returns a dictionary defining a single function tool, specifying its name, description, and required/optional integer parameters for invocation. This structure is used to provide available capabilities to an agent system.*


### test_register_tools (method, L77-L96, parent: TestRealtimeAgent)

> *Summary: This test verifies that a provided function is correctly registered as a realtime tool on an agent. It asserts the tool's existence, schema matching against expectations, and then executes the function to confirm its output matches the expected result.*

