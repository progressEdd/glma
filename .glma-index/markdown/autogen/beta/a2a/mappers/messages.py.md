# autogen/beta/a2a/mappers/messages.py

6 function(s): build_user_message, build_tool_result_message, build_input_response_message, parse_message, extract_context_update, _build_message. 1 class(es): ParsedMessage.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| ParsedMessage | class |  |
| build_user_message | function |  |
| build_tool_result_message | function |  |
| build_input_response_message | function |  |
| parse_message | function |  |
| extract_context_update | function |  |
| _build_message | function |  |

## Chunks

### ParsedMessage (class, L43-L59)

> *Summary: Represents the structured output after decoding an incoming A2A message. It aggregates various components like inputs, tool definitions, execution results, event history, and context variable updates from the source message.*


### build_user_message (function, L62-L104)

> *Summary: Constructs a `Message` object representing user input by aggregating provided inputs, optional conversation history events, and tool schemas into data parts. It returns the fully assembled message structure, incorporating metadata updates and any extra content specified.*


### build_tool_result_message (function, L107-L140)

> *Summary: Constructs a `Message` object to send tool execution results back to the server. It aggregates tool result payloads, optional schemas, and conversation history into distinct parts before packaging them with task and context identifiers.*


### build_input_response_message (function, L143-L168)

> *Summary: Constructs a `Message` object to relay a human-in-the-loop (HITL) response back to the server. It takes user text and associated identifiers like `task_id` and optional metadata to resume an existing task.*


### parse_message (function, L171-L194)

> *Summary: This function processes an incoming `Message` by iterating through its parts to decode them into structured buckets within a `ParsedMessage`. It routes data based on MIME type—handling tool schemas, calls, results, and history events separately—while routing all other parts as general inputs.*


### extract_context_update (function, L197-L209)

> *Summary: This function retrieves the `ag2.context_update` payload from a message's metadata. It returns this dictionary if present and valid, otherwise it yields an empty dictionary for unconditional updates by the caller.*


### _build_message (function, L212-L240)

> *Summary: Constructs a `Message` object by assembling provided parts, role, and optional identifiers like task or context IDs. It incorporates metadata from extra inputs and context updates before returning the fully formed message structure.*

