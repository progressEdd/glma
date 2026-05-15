# test/beta/middleware/test_tool_execution.py

3 class(es): OrderingMiddleware, TestToolExecutionMiddleware, TestToolMiddlewareRegistration. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| OrderingMiddleware | class |  |
| TestToolExecutionMiddleware | class |  |
| TestToolMiddlewareRegistration | class |  |

## Chunks

### OrderingMiddleware (class, L16-L37)

> *Summary: This middleware wraps tool execution by recording entry and exit points using a provided mock object at a specific position. It intercepts the `ToolCallEvent`, passes it to the next handler, and then returns the resulting `ToolResultEvent`.*


### __init__ (method, L17-L26, parent: OrderingMiddleware)

> *Summary: Initializes an object with a base event, context, a mock object, and a specific integer position. It stores these inputs for later use during testing or execution flow management.*


### on_tool_execution (method, L28-L37, parent: OrderingMiddleware)

> *Summary: This asynchronous method wraps the execution of a tool call by entering and exiting a mock context around the `call_next` invocation. It takes a next handler, a tool call event, and a context as input, returning the resulting tool outcome event.*


### TestToolExecutionMiddleware (class, L40-L218)

> *Summary: This code chunk contains several asynchronous unit tests verifying the behavior of a tool execution middleware system within an agent framework. It demonstrates how custom middlewares can intercept and modify tool calls, test call ordering between different middleware layers, and handle errors during tool execution.*


### test_basic (method, L42-L80, parent: TestToolExecutionMiddleware)

> *Summary: This test verifies middleware behavior by wrapping an agent's execution with a mock object. It asserts that the custom middleware correctly calls `mock.enter` before tool execution and `mock.exit` after receiving the result from the underlying tool call.*


### test_call_sequence (method, L83-L100, parent: TestToolExecutionMiddleware)

> *Summary: This test verifies the execution order of middleware when an agent calls a tool. It asserts that the middleware enters and exits in a specific sequence (1 then 2 then 3 for entry, and 3 then 2 then 1 for exit) during the agent's response to "Hi!".*


### test_capture_error (method, L103-L142, parent: TestToolExecutionMiddleware)

> *Summary: This test verifies that a custom middleware correctly captures and reports an error raised during tool execution. It sets up an agent with a mock middleware, runs it to trigger the failing tool, and asserts that the mock's exit method was called with the expected error representation.*


### test_mutates_arguments_and_result (method, L145-L184, parent: TestToolExecutionMiddleware)

> *Summary: This test verifies that a custom middleware modifies both the input arguments and the final output of a tool execution. It sets up an agent with three instances of a mutating middleware to confirm the argument is incremented by three and the result string has exclamation marks appended.*


### test_tool_local_then_agent_middleware_order (method, L187-L218, parent: TestToolExecutionMiddleware)

> *Summary: This test verifies the execution order of middleware when a tool is called by an agent. It asserts that hooks registered at positions 1, 2, and 3 are entered sequentially (1 then 2 then 3) and exited in reverse order (3 then 2 then 1).*


### TestToolMiddlewareRegistration (class, L221-L275)

> *Summary: These tests verify that middleware hooks are correctly invoked when an `Agent` executes tools, both directly defined and those provided via a `Toolkit`. The functions assert that the mocked middleware method is called exactly once during the agent's interaction with the tool.*


### test_agent_tool_consumes_middleware (method, L223-L246, parent: TestToolMiddlewareRegistration)

> *Summary: This test verifies that an agent's tool execution correctly invokes a provided middleware hook. It sets up an agent with a decorated tool and asserts that the mock middleware function is called exactly once when the agent processes a prompt.*


### test_toolkit_tool_consumes_middleware (method, L249-L275, parent: TestToolMiddlewareRegistration)

> *Summary: This test verifies that a custom middleware hook is executed when an agent invokes a tool decorated with it. It sets up an agent using a toolkit containing a tool wrapped with the middleware and asserts that the mock function within the middleware was called exactly once during execution.*

