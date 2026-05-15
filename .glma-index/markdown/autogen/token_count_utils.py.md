# autogen/token_count_utils.py

8 function(s): num_tokens_from_gpt_image, get_max_token_limit, percentile_used, token_left, count_token, _num_token_from_text, _num_token_from_messages, num_tokens_from_functions.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| num_tokens_from_gpt_image | function |  |
| get_max_token_limit | function |  |
| percentile_used | function |  |
| token_left | function |  |
| count_token | function |  |
| _num_token_from_text | function |  |
| _num_token_from_messages | function |  |
| num_tokens_from_functions | function |  |

## Chunks

### num_tokens_from_gpt_image (function, L26-L27)

> *Summary: This function currently returns zero regardless of its inputs. It is intended to calculate the token count associated with a GPT image input.*


### get_max_token_limit (function, L34-L107)

> *Summary: This function determines the maximum token limit for a specified language model string. It first normalizes common Azure aliases in the input model name before looking up and returning the corresponding integer limit from an internal dictionary mapping.*


### percentile_used (function, L110-L111)

> *Summary: Calculates the token usage percentage of an input by dividing its token count by the specified model's maximum token limit. It accepts a text `input` and an optional `model` identifier to determine the capacity.*


### token_left (function, L114-L124)

> *Summary: Calculates the remaining token capacity for a specified OpenAI model by subtracting the input's token count from the model's maximum limit. It accepts various data types (string, list, or dictionary) as input and returns an integer representing available tokens.*


### count_token (function, L127-L142)

> *Summary: Calculates the token count for an input provided as a string, list, or dictionary against a specified OpenAI model. It delegates to specialized helper functions based on the input type to return the total number of tokens used.*


### _num_token_from_text (function, L145-L152)

> *Summary: Calculates the token count of an input string using a specified OpenAI model's tokenizer, falling back to `cl100k_base` if the requested model is unknown. It returns an integer representing the number of tokens in the provided text.*


### _num_token_from_messages (function, L155-L278)

> *Summary: Calculates the total token count for a list of messages, accepting either a list or a single dictionary as input. It uses `tiktoken` based on the specified model to account for message structure, content text, function calls, and image data tokens, returning an integer representing the estimated token usage.*


### num_tokens_from_functions (function, L281-L329)

> *Summary: Calculates the token count for a list of provided function descriptions based on a specified model. It iterates through each function, encoding its name, description, and parameter details (including properties and enums) using `tiktoken` to sum up the total tokens.*

