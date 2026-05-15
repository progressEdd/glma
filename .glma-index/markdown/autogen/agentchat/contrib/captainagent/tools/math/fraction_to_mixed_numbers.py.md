# autogen/agentchat/contrib/captainagent/tools/math/fraction_to_mixed_numbers.py

1 function(s): fraction_to_mixed_numbers.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| fraction_to_mixed_numbers | function |  |

## Chunks

### fraction_to_mixed_numbers (function, L4-L39)

> *Summary: This function converts a given fraction, provided as an integer numerator and denominator, into its mixed number string representation. It first validates the inputs for type and division by zero before using `sympy.Rational` to simplify and format the output as either a whole number or a mixed fraction.*

