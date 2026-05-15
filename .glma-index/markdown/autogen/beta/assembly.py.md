# autogen/beta/assembly.py

2 class(es): AssemblyPolicy, AssemblerMiddleware. 4 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| AssemblyPolicy | class |  |
| AssemblerMiddleware | class |  |

## Chunks

### AssemblyPolicy (class, L22-L42)

> *Summary: Defines a contract for policies that modify LLM inputs before invocation. It accepts lists of prompts and events along with a context object, returning the transformed versions.*


### apply (method, L35-L42, parent: AssemblyPolicy)

> *Summary: This asynchronous method takes lists of strings (prompts) and base event objects, along with a context object, to transform both inputs. It returns the resulting modified lists of prompts and events.*


### AssemblerMiddleware (class, L45-L112)

> *Summary: This middleware intercepts LLM calls to execute a sequence of assembly policies, transforming input prompts and event lists before they reach the model. It ensures proper policy ordering by validating that reduction policies do not precede injection policies within the provided list.*


### __init__ (method, L62-L70, parent: AssemblerMiddleware)

> *Summary: Initializes an assembly object by accepting a base event and context. It stores a list of `AssemblyPolicy` objects to govern its behavior.*


### on_llm_call (method, L72-L90, parent: AssemblerMiddleware)

> *Summary: This method intercepts an LLM call by iterating through registered policies to modify the input prompts and events based on the current context. It temporarily substitutes the context's prompt with the modified versions before passing them to the next handler, ensuring the original state is restored afterward.*


### validate_order (method, L93-L112, parent: AssemblerMiddleware)

> *Summary: This function checks a list of assembly policies for problematic ordering, specifically ensuring that injection policies precede reduction policies. It takes a list of `AssemblyPolicy` objects as input and returns a list of strings detailing any detected violations where a reduction policy runs before an injection policy.*

