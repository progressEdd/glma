# autogen/oai/openai_responses.py

2 function(s): calculate_openai_image_cost, _get_base_class. 5 class(es): ApplyPatchCallOutput, ShellCallOutcome, ShellCommandOutput, ShellCallOutput, OpenAIResponsesClient. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ApplyPatchCallOutput | class |  |
| ShellCallOutcome | class |  |
| ShellCommandOutput | class |  |
| ShellCallOutput | class |  |
| calculate_openai_image_cost | function |  |
| _get_base_class | function |  |
| OpenAIResponsesClient | class |  |

## Chunks

### ApplyPatchCallOutput (class, L59-L66)

> *Summary: Represents the result of applying a patch call, storing its unique ID, current status, and resulting output string. It provides a method to serialize this data structure into a standard dictionary format.*


### to_dict (method, L65-L66, parent: ApplyPatchCallOutput)

> *Summary: Converts the object's state into a standard Python dictionary representation. It takes no arguments and returns a `dict[str, str]` containing all its attributes.*


### ShellCallOutcome (class, L70-L78)

> *Summary: Represents the result of executing a shell command, storing either an exit code or indicating a timeout. It provides a method to serialize its state into a standard Python dictionary.*


### model_dump (method, L76-L78, parent: ShellCallOutcome)

> *Summary: Converts the object's state into a standard Python dictionary using `asdict`. This allows the instance to be easily serialized or used where a dictionary structure is expected.*


### ShellCommandOutput (class, L82-L91)

> *Summary: Represents the result of executing a shell command by storing its standard output, standard error, and execution outcome. It provides a method to serialize this data structure into a dictionary format.*


### model_dump (method, L89-L91, parent: ShellCommandOutput)

> *Summary: Converts the instance's state into a standard Python dictionary using `asdict`. This allows the object to be easily serialized or used where a dictionary structure is expected.*


### ShellCallOutput (class, L95-L110)

> *Summary: Represents the payload structure for shell call results in an API response. It holds a `call_id`, a list of command outputs (`output`), and optional truncation settings, providing methods to serialize itself into a dictionary.*


### __post_init__ (method, L103-L106, parent: ShellCallOutput)

> *Summary: Ensures the `output` attribute is initialized to an empty list if it was not provided during object creation. This guarantees that subsequent operations can safely iterate over or append to the output collection.*


### model_dump (method, L108-L110, parent: ShellCallOutput)

> *Summary: Converts the instance's state into a standard Python dictionary using `asdict`. This allows the object to be easily serialized or used where a dictionary structure is expected.*


### calculate_openai_image_cost (function, L113-L153)

> *Summary: Determines the monetary cost of generating a single image based on the specified model, size, and quality settings. It accepts `model`, `size`, and `quality` as inputs and returns a tuple containing the calculated cost (float) and an error message (str).*


### _get_base_class (function, L156-L160)

> *Summary: This function lazily imports the `OpenAILLMConfigEntry` class from `autogen.oai.client`. It returns this imported class, preventing circular dependency issues during module loading.*


### OpenAIResponsesClient (class, L167-L1108)

> *Summary: This class manages interactions with the experimental `/responses` endpoint of an OpenAI client, providing methods to create responses, retrieve messages, and calculate costs. It handles complex message normalization by processing internal tool calls (like file patching and shell execution) before formatting inputs for the API or extracting structured outputs from received responses.*


### __init__ (method, L179-L198, parent: OpenAIResponsesClient)

> *Summary: Initializes an object to interact with OpenAI, storing the provided client and setting up default parameters for image generation requests. It also initializes tracking variables for previous response IDs and accumulated image generation costs.*


### _usage_dict (method, L203-L223, parent: OpenAIResponsesClient)

> *Summary: Extracts token usage and cost metrics from an OpenAI response object. It standardizes the input by converting Pydantic models or existing dictionaries into a uniform dictionary structure before returning key values like prompt, completion, total tokens, and associated costs.*


### _add_image_cost (method, L225-L242, parent: OpenAIResponsesClient)

> *Summary: This method calculates and accumulates the cost associated with generated images from a given response object. It iterates through the response's outputs, checks for `ImageGenerationCall` instances containing model extras, and uses an external function to determine the cost based on specified size and quality.*


### _get_delta_messages (method, L244-L268, parent: OpenAIResponsesClient)

> *Summary: This method filters a list of messages, iterating backward to identify the segment that represents the most recent, fully completed response while excluding any preceding "apply\_patch\_call" items. It returns this relevant subset of messages in their original chronological order.*


### _parse_params (method, L270-L277, parent: OpenAIResponsesClient)

> *Summary: This method transforms a parameter dictionary by extracting optional keys like `verbosity` and `reasoning_effort`. It then restructures these values into nested dictionaries under `"text"` or `"reasoning"` within the input parameters.*


### _apply_patch_operation (method, L279-L391, parent: OpenAIResponsesClient)

> *Summary: Executes file creation, updating, or deletion based on a provided operation dictionary within a specified workspace. It handles both synchronous and asynchronous execution paths, returning an output structure detailing the operation's status and result for a given call ID.*


### _extract_apply_patch_calls (method, L393-L420, parent: OpenAIResponsesClient)

> *Summary: Scans a list of messages to find and extract all instances of `apply_patch_call` objects. It returns a dictionary mapping each call's ID to the corresponding patch call item found within either the message content or the tool calls section.*


### _execute_apply_patch_calls (method, L422-L457, parent: OpenAIResponsesClient)

> *Summary: Processes a dictionary of patch calls by iterating through them and executing each operation using an internal patching mechanism. It takes the call definitions, enabled tools, workspace directory, and allowed paths as input, returning a list of resulting output dictionaries.*


### _extract_shell_calls (method, L459-L486, parent: OpenAIResponsesClient)

> *Summary: Parses a list of messages to find and extract all instances of "shell\_call" objects, whether they are nested within the message content or listed in `tool_calls`. It returns a dictionary mapping each unique call ID to its corresponding shell call item.*


### _execute_shell_calls (method, L488-L532, parent: OpenAIResponsesClient)

> *Summary: Processes a dictionary of shell call requests by executing each one using an internal operation method. It takes configuration like allowed/denied commands and paths to safely run the specified shell actions within a given workspace, returning a list of structured output results.*


### _convert_messages_to_input (method, L534-L603, parent: OpenAIResponsesClient)

> *Summary: This method transforms a list of message dictionaries into the specific input format required by the Responses API, appending the results to an `input_items` list. It processes messages based on their role (user, assistant, or tool) and handles various content types like text, images, and function call outputs while skipping already processed calls.*


### _normalize_messages_for_responses_api (method, L605-L714, parent: OpenAIResponsesClient)

> *Summary: This method transforms a list of incoming messages into the specific format required by the Responses API. It processes and executes embedded `apply_patch_call` and `shell_call` actions from both current and previous message states, filtering commands based on provided security parameters before returning a chronologically ordered list containing processed outputs followed by the remaining original messages.*


### _execute_shell_operation (method, L716-L823, parent: OpenAIResponsesClient)

> *Summary: Executes a list of shell commands using an internal executor, applying various security and configuration constraints like allowed paths/commands. It accepts action details (commands, timeout) and returns a `ShellCallOutput` containing the results or any execution errors.*


### create (method, L825-L993, parent: OpenAIResponsesClient)

> *Summary: This method prepares and invokes the OpenAI Responses API to generate a response based on provided parameters, handling input normalization from legacy message formats. It manages tool configurations (like shell or web search), extracts necessary context from previous responses, and conditionally calls either `create` or `parse` depending on whether structured output is requested.*


### message_retrieval (method, L995-L1101, parent: OpenAIResponsesClient)

> *Summary: Parses a raw API response object to extract structured messages and tool calls. It iterates through the response's output, transforming different item types (like "message", "function\_call", or various tool call types) into standardized dictionary formats for content and separate lists of tool calls. The function returns a list containing a single structured message object summarizing the processed data.*


### cost (method, L1103-L1104, parent: OpenAIResponsesClient)

> *Summary: Retrieves the total monetary cost associated with a given API response by summing the usage cost from the response dictionary and any predefined image costs. It returns this combined value, defaulting to zero if no cost is specified in the response.*


### get_usage (method, L1107-L1108, parent: OpenAIResponsesClient)

> *Summary: Extracts usage statistics from an OpenAI response object by calling a helper method on the client. It takes one `response` object as input and returns a dictionary containing the usage details.*

