# autogen/agentchat/contrib/math_user_proxy_agent.py

4 function(s): _is_termination_msg_mathchat, _add_print_to_last_line, _remove_print, get_from_dict_or_env. 2 class(es): MathUserProxyAgent, WolframAlphaAPIWrapper. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _is_termination_msg_mathchat | function |  |
| _add_print_to_last_line | function |  |
| _remove_print | function |  |
| MathUserProxyAgent | class |  |
| get_from_dict_or_env | function |  |
| WolframAlphaAPIWrapper | class |  |

## Chunks

### _is_termination_msg_mathchat (function, L104-L116)

> *Summary: Determines if a given message signals the end of a math chat session. It checks if the message contains code blocks (Python or Wolfram) and verifies that it has a non-empty, valid answer extracted from it.*


### _add_print_to_last_line (function, L119-L135)

> *Summary: This utility modifies a code string by appending `print()` to its final line if it doesn't already contain one. It specifically handles cases where the last line contains an assignment operator (`=`) differently than simple statements.*


### _remove_print (function, L138-L142)

> *Summary: This utility function strips all lines starting with `print(` from an input string of code. It returns the modified string containing only the non-printing lines.*


### MathUserProxyAgent (class, L148-L364)

> *Summary: This deprecated agent handles mathematical problems by executing code blocks (Python or WolframAlpha) found in incoming messages. It processes inputs to generate an automated reply containing execution results, managing state like previous code and tracking invalid queries based on configuration.*


### __init__ (method, L159-L208, parent: MathUserProxyAgent)

> *Summary: Initializes a specialized agent proxy for mathematical interactions, accepting configuration for its name, termination condition, human input behavior, and default replies. It sets up internal state tracking for query validation and registers a specific reply generation function to handle math-related responses.*


### message_generator (method, L211-L241, parent: MathUserProxyAgent)

> *Summary: Constructs a prompt string for an assistant agent based on a provided problem and configuration context. It prioritizes a custom prompt if supplied, otherwise selects a template from predefined types ("default", "python", or "two\_tools") and appends the problem description to it.*


### _reset (method, L243-L249, parent: MathUserProxyAgent)

> *Summary: Resets internal state variables, including query counts and accumulated invalid queries, to their initial values for a new interaction cycle. This prepares the agent proxy for subsequent use by clearing historical context like previous code execution.*


### execute_one_python_code (method, L251-L297, parent: MathUserProxyAgent)

> *Summary: Executes a provided block of Python code by prepending it with previously executed code. It handles error reporting, checks for output presence, truncates excessively long results, and performs validation runs to ensure the code remains functional before returning the final output and success status.*


### execute_one_wolfram_query (method, L299-L315, parent: MathUserProxyAgent)

> *Summary: This method executes a single mathematical or factual query against WolframAlpha using an API wrapper. It takes a string query as input and returns the resulting output string along with a boolean indicating if the execution was successful.*


### _generate_math_reply (method, L317-L364, parent: MathUserProxyAgent)

> *Summary: Processes a list of messages to generate an automated response by executing code blocks found in the last message using language-specific executors (Python or Wolfram). It returns a boolean indicating success and the generated reply string, while also managing state regarding repeated or failed query attempts.*


### get_from_dict_or_env (function, L391-L404)

> *Summary: Retrieves a string value by first checking a provided dictionary using a specific key; if not found, it checks an environment variable specified by `env_key`, falling back to a user-defined default or raising a `ValueError`.*


### WolframAlphaAPIWrapper (class, L407-L503)

> *Summary: This class wraps the WolframAlpha API, requiring an environment variable for authentication to initialize a client. It accepts a string query and returns a tuple containing the formatted answer (including assumptions) and a boolean indicating success after handling potential network errors and parsing the response structure.*


### validate_environment (method, L427-L435, parent: WolframAlphaAPIWrapper)

> *Summary: This method ensures the necessary Wolfram Alpha API key and initializes a corresponding client object within the provided configuration dictionary. It retrieves the API ID from either the input dictionary or environment variables, then populates both the `wolfram_alpha_appid` and `wolfram_client` keys in the returned dictionary.*


### validate_environment (method, L442-L450, parent: WolframAlphaAPIWrapper)

> *Summary: This method ensures the necessary Wolfram Alpha API key is present in the input dictionary, retrieves it from environment variables if missing, and initializes a `wolframalpha.Client` instance to store within the returned dictionary. It validates and enriches the provided configuration with the required client object for external service interaction.*


### run (method, L452-L503, parent: WolframAlphaAPIWrapper)

> *Summary: Executes a query against WolframAlpha, retrying up to 20 times upon HTTP errors. It parses the returned JSON structure to extract an assumption and the final answer, returning both as a formatted string along with a success boolean.*

