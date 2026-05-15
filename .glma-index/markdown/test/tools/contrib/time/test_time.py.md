# test/tools/contrib/time/test_time.py

1 class(es): TestTimeTool. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestTimeTool | class |  |

## Chunks

### TestTimeTool (class, L12-L56)

> *Summary: This test suite verifies the functionality of a time-related tool by checking its initialization parameters and schema against expected values. It also confirms that calling the tool asynchronously returns a string representing the current date and time in a specific format.*


### test_time_tool_init (method, L13-L42, parent: TestTimeTool)

> *Summary: This test verifies the correct initialization and configuration of a `TimeTool` instance. It asserts that the tool's name, description, format attribute, and generated function schema match expected values based on provided inputs.*


### test_time_tool_call (method, L45-L56, parent: TestTimeTool)

> *Summary: This test verifies that calling a `TimeTool` asynchronously returns a string formatted exactly as "YYYY-MM-DD HH:MM:SS". It asserts both the type and the specific date/time structure of the returned value.*

