# test/coding/test_user_defined_functions.py

14 function(s): add_two_numbers, load_data, function_incorrect_import, function_incorrect_dep, function_missing_reqs, test_can_load_function_with_reqs, test_can_load_function, test_fails_for_function_incorrect_import, test_fails_for_function_incorrect_dep, test_formatted_prompt and 4 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| add_two_numbers | function |  |
| load_data | function |  |
| function_incorrect_import | function |  |
| function_incorrect_dep | function |  |
| function_missing_reqs | function |  |
| test_can_load_function_with_reqs | function |  |
| test_can_load_function | function |  |
| test_fails_for_function_incorrect_import | function |  |
| test_fails_for_function_incorrect_dep | function |  |
| test_formatted_prompt | function |  |
| test_formatted_prompt_str_func | function |  |
| test_can_load_str_function_with_reqs | function |  |
| test_cant_load_broken_str_function_with_reqs | function |  |
| test_cant_run_broken_str_function_with_reqs | function |  |

## Chunks

### add_two_numbers (function, L23-L25)

> *Summary: This function takes two integers as input and returns their sum. It performs simple addition to combine the provided numerical values.*


### load_data (function, L29-L40)

> *Summary: This function constructs and returns a Pandas DataFrame containing sample user data with columns for name (string), location (string), and age (integer). It serves as a utility to provide predefined dataset inputs for testing purposes.*


### function_incorrect_import (function, L44-L45)

> *Summary: This function returns an empty Pandas DataFrame, simulating a scenario where an import error might occur if the `pandas` library were not correctly available or accessible in the execution environment.*


### function_incorrect_dep (function, L49-L50)

> *Summary: This function returns an empty Pandas DataFrame, simulating a scenario where dependencies might be incorrectly handled or mocked for testing purposes. It takes no inputs and produces a basic data structure as output.*


### function_missing_reqs (function, L53-L54)

> *Summary: This function returns an empty Pandas DataFrame, simulating a scenario where required inputs are missing for a data processing operation. It serves as a test case to verify behavior when necessary dependencies are absent.*


### test_can_load_function_with_reqs (function, L59-L74)

> *Summary: This test verifies that a function can be successfully loaded and executed within an isolated environment. It initializes an executor with a specific function (`load_data`) and then runs Python code that calls this function to assert the expected output is "John\n" with a successful exit code.*


### test_can_load_function (function, L79-L91)

> *Summary: This test verifies that the system can successfully load and execute a user-defined function (`add_two_numbers`) within an isolated temporary directory. It executes Python code that imports and calls this function, asserting the output is "3\n" and the exit code is zero.*


### test_fails_for_function_incorrect_import (function, L114-L125)

> *Summary: This test verifies that executing code referencing a function imported from an incorrect module raises a `ValueError`. It sets up a temporary environment, initializes the executor with a faulty function reference, and then attempts to run Python code that relies on this misconfigured import.*


### test_fails_for_function_incorrect_dep (function, L130-L141)

> *Summary: This test verifies that executing code referencing a function with an incorrect dependency raises a `ValueError`. It sets up an executor environment and attempts to run Python code that calls the specified, improperly dependent function.*


### test_formatted_prompt (function, L145-L155)

> *Summary: This test verifies that the execution environment correctly formats a provided function into a string suitable for inclusion in a prompt. It initializes an executor with a temporary directory and a specific function, then asserts the resulting formatted code contains the expected definition of `add_two_numbers`.*


### test_formatted_prompt_str_func (function, L159-L176)

> *Summary: This test verifies that a function correctly formats provided Python code into a prompt string. It takes a string containing a function definition and asserts the resulting formatted output includes the original source code.*


### test_can_load_str_function_with_reqs (function, L180-L200)

> *Summary: This test verifies that a string containing a Python function definition can be successfully loaded and executed by the system. It takes a string of code, parses it into a runnable function object, sets up an executor in a temporary directory, and asserts that executing a call to this function yields the expected output ("3\n") with a zero exit code.*


### test_cant_load_broken_str_function_with_reqs (function, L204-L212)

> *Summary: Asserts that attempting to parse an invalid string representation of a function using `FunctionWithRequirements.from_str` raises a `ValueError`. This test verifies the parser's robustness against malformed input code.*


### test_cant_run_broken_str_function_with_reqs (function, L216-L236)

> *Summary: This test verifies that attempting to execute a function with incorrect argument types will fail as expected. It loads a valid Python function definition, sets up an execution environment, and runs code that calls the function with incompatible inputs, asserting a `TypeError` in the output.*

