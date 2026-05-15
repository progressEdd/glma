# autogen/agentchat/group/guardrails.py

4 class(es): Guardrail, LLMGuardrail, RegexGuardrail, GuardrailResult. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Guardrail | class |  |
| LLMGuardrail | class |  |
| RegexGuardrail | class |  |
| GuardrailResult | class |  |

## Chunks

### Guardrail (class, L19-L45)

> *Summary: This abstract base class defines the structure for implementing safety checks; it requires subclasses to implement a `check` method that takes a string or list of dictionaries as input and returns a `GuardrailResult`. Instances are initialized with a name, a condition string, a target transition, and an optional activation message.*


### __init__ (method, L22-L30, parent: Guardrail)

> *Summary: Initializes a guardrail object by setting its unique name, the triggering condition string, and the desired transition target. It also sets an optional activation message, defaulting to a generic notification if none is provided.*


### check (method, L33-L45, parent: Guardrail)

> *Summary: This method validates provided input text or a list of dictionaries against predefined safety rules. It accepts either a string or a list of structured data and returns a `GuardrailResult` indicating whether the content passed the checks.*


### LLMGuardrail (class, L48-L97)

> *Summary: This class implements a safety mechanism that uses an LLM to evaluate conversation context against a predefined condition. It accepts the context (string or list of messages) and returns a `GuardrailResult` indicating whether the condition was met based on the LLM's assessment.*


### __init__ (method, L51-L71, parent: LLMGuardrail)

> *Summary: Initializes a guardrail agent by setting up its configuration, including deep-copying LLM settings and instantiating an OpenAI client based on those settings. It then constructs a specific prompt instructing the underlying model to check if a predefined condition is met within the conversation context.*


### check (method, L73-L97, parent: LLMGuardrail)

> *Summary: This method validates provided context against a predefined rule by sending the context and a system prompt to an LLM client. It accepts either a string or a list of message dictionaries as input and returns a `GuardrailResult` based on the LLM's response.*


### RegexGuardrail (class, L100-L145)

> *Summary: This component enforces content restrictions by compiling and applying a regular expression against provided context. It accepts either a single string or a list of message dictionaries as input, returning a `GuardrailResult` indicating if any part of the context matched the defined pattern.*


### __init__ (method, L103-L115, parent: RegexGuardrail)

> *Summary: Initializes a guardrail by compiling a provided string into a regular expression for condition checking. It accepts a name, the regex condition, a target transition, and an optional activation message.*


### check (method, L117-L145, parent: RegexGuardrail)

> *Summary: This method validates input content against a predefined regular expression. It accepts either a single string or a list of message dictionaries, returning a `GuardrailResult` indicating if any part of the context matched the regex and providing a justification upon activation.*


### GuardrailResult (class, L148-L179)

> *Summary: This data structure models the outcome of a safety check, holding whether a rule was triggered, which specific rule applied, and a textual justification. It provides methods to easily serialize/deserialize itself from JSON strings and generate human-readable responses based on its state.*


### __str__ (method, L157-L158, parent: GuardrailResult)

> *Summary: Provides a string representation of the guardrail result, detailing whether it was activated and providing the associated justification. This method takes no input and returns a formatted string summarizing the guardrail's state.*


### reply (method, L161-L162, parent: GuardrailResult)

> *Summary: Generates a response string by combining the guardrail's activation message with a provided justification. This method outputs a formatted string containing both pieces of information.*


### parse (method, L165-L179, parent: GuardrailResult)

> *Summary: Converts a JSON string into a structured `GuardrailResult` object, associating it with a specific guardrail instance. It handles parsing errors by raising a `ValueError` if the input text is not valid JSON.*

