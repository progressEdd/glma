# autogen/math_utils.py

12 function(s): remove_boxed, last_boxed_only_string, _fix_fracs, _fix_a_slash_b, _remove_right_units, _fix_sqrt, _strip_string, get_answer, is_equiv, is_equiv_chain_of_thought and 2 more.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| remove_boxed | function |  |
| last_boxed_only_string | function |  |
| _fix_fracs | function |  |
| _fix_a_slash_b | function |  |
| _remove_right_units | function |  |
| _fix_sqrt | function |  |
| _strip_string | function |  |
| get_answer | function |  |
| is_equiv | function |  |
| is_equiv_chain_of_thought | function |  |
| voting_counts | function |  |
| eval_math_responses | function |  |

## Chunks

### remove_boxed (function, L9-L27)

> *Summary: This function extracts the content enclosed within a `\boxed{...}` LaTeX environment from an input string. It returns the extracted text if the string matches the expected format, otherwise it returns `None`.*


### last_boxed_only_string (function, L30-L55)

> *Summary: This function extracts the final LaTeX-style boxed expression, either enclosed in `\boxed{...}` or `\fbox{...}`, from an input string. It scans backward from the last occurrence of these markers to correctly identify and return the complete content including its delimiters.*


### _fix_fracs (function, L58-L101)

> *Summary: This utility reformats LaTeX-style fraction strings by replacing simple numerator/denominator sequences following `\frac` with proper curly brace delimiters. It parses the input string, reconstructs it piece by piece, and handles cases where numerators or denominators are single characters or contain subsequent text.*


### _fix_a_slash_b (function, L104-L126)

> *Summary: Transforms simple fraction strings like "a/b" into LaTeX format `\frac{a}{b}` if both parts can be parsed as integers. It returns the original string otherwise, handling cases where the input doesn't contain exactly one slash or the components are not valid integers.*


### _remove_right_units (function, L129-L140)

> *Summary: This utility strips trailing units from a mathematical expression string by splitting the input at the pattern `\text{ }`. If the pattern is found and results in exactly two parts, it returns only the first part (the value); otherwise, it returns the original string.*


### _fix_sqrt (function, L143-L164)

> *Summary: This utility function reformats string representations of square roots. It takes a string containing `\sqrt` and replaces instances where the argument is not enclosed in curly braces with the standard LaTeX format, like `\sqrt{x}`.*


### _strip_string (function, L167-L238)

> *Summary: This utility function cleans and reformats a raw input string by removing various LaTeX artifacts like newlines, specific commands ($\backslash$left, $\backslash$right), units, and percentage signs. It also performs structural fixes such as ensuring leading zeros for decimals, correcting fraction notations, and standardizing mathematical expressions before returning the processed string.*


### get_answer (function, L241-L250)

> *Summary: This function extracts the final answer from a provided solution string. It first isolates the last boxed content, then strips any surrounding box characters to return the clean answer or `None` if no valid answer can be found.*


### is_equiv (function, L253-L272)

> *Summary: Compares two string representations of mathematical expressions to determine if they are equivalent, ignoring formatting differences like units or superfluous LaTeX. It returns `1.0` if the stripped versions match, `0.0` otherwise, handling `None` inputs appropriately.*


### is_equiv_chain_of_thought (function, L275-L280)

> *Summary: Compares two strings by extracting their final answers using `get_answer` and then checks if those extracted answers are equivalent via `is_equiv`. It returns a float representing the equivalence result.*


### voting_counts (function, L283-L298)

> *Summary: This function tallies the occurrences of equivalent responses within a list. It iterates through the input `responses`, grouping them based on equivalence checks and returning a dictionary where keys are representative equivalents and values are their respective counts.*


### eval_math_responses (function, L301-L338)

> *Summary: This function determines the outcome of math problem evaluations by first aggregating votes from a list of provided responses. It returns a dictionary containing metrics such as the most voted answer, the success status based on individual response correctness against a known solution, and expected success rates.*

