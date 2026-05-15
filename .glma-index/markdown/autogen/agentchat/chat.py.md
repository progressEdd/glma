# autogen/agentchat/chat.py

10 function(s): _validate_recipients, __create_async_prerequisites, __find_async_chat_order, _post_process_carryover_item, __post_carryover_processing, initiate_chats, __system_now_str, _on_chat_future_done, _dependent_chat_future, a_initiate_chats. 2 class(es): CostDict, ChatResult.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| CostDict | class |  |
| ChatResult | class |  |
| _validate_recipients | function |  |
| __create_async_prerequisites | function |  |
| __find_async_chat_order | function |  |
| _post_process_carryover_item | function |  |
| __post_carryover_processing | function |  |
| initiate_chats | function |  |
| __system_now_str | function |  |
| _on_chat_future_done | function |  |
| _dependent_chat_future | function |  |
| a_initiate_chats | function |  |

## Chunks

### CostDict (class, L29-L31)

> *Summary: This structure defines a dictionary type to hold cost metrics for an interaction. It requires two nested dictionaries: one detailing usage including cached inference and another for usage excluding it.*


### ChatResult (class, L36-L61)

> *Summary: Represents the outcome of a conversation, storing metadata such as a unique ID, the full exchange history, a generated summary, and detailed cost breakdowns. It also tracks any specific inputs provided by the user during the interaction.*


### _validate_recipients (function, L64-L74)

> *Summary: Checks a list of chat entries to ensure each contains a "recipient" key and warns if any recipients are duplicated within the queue. This validation prevents issues by alerting the user about potential history clearing due to repeated participants.*


### __create_async_prerequisites (function, L77-L89)

> *Summary: Generates a list of dependency pairs from a queue of chat information dictionaries. It validates that each chat has an ID and correctly structures the output as `(current_chat_id, prerequisite_chat_id)` tuples.*


### __find_async_chat_order (function, L92-L129)

> *Summary: Calculates a valid execution sequence for chats based on dependency constraints using Kahn's algorithm (topological sort). It takes a set of chat IDs and a list of prerequisite pairs, returning an ordered list of chat IDs or an empty list if a cycle exists.*


### _post_process_carryover_item (function, L132-L141)

> *Summary: This utility function standardizes the format of a `carryover_item` by ensuring it returns a string. It handles inputs that are already strings, dictionaries containing content, or any other type by coercing them to a string representation.*


### __post_carryover_processing (function, L144-L153)

> *Summary: This function processes chat information after a carryover event by first checking for an existing "message" within the input dictionary. It then emits a `PostCarryoverProcessingEvent` containing the provided chat data through the default IO stream.*


### initiate_chats (function, L157-L215)

> *Summary: Processes a queue of chat configuration dictionaries to initiate multiple conversations with specified agents. It iteratively starts each chat, incorporating summaries from previously completed chats into the current chat's context before returning a list of resulting `ChatResult` objects.*


### __system_now_str (function, L218-L220)

> *Summary: Generates a string containing the current system date and time, formatted for inclusion in system messages. It takes no inputs and returns a descriptive timestamp string.*


### _on_chat_future_done (function, L223-L227)

> *Summary: This function processes the outcome of an asynchronous chat operation by retrieving the result from a provided `asyncio.Future`. It then attaches the corresponding `chat_id` to the returned `ChatResult` object before logging the completion.*


### _dependent_chat_future (function, L230-L264)

> *Summary: This function constructs an asynchronous task to initiate a new chat based on its configuration and the results of prerequisite chats. It awaits the completion of specified futures, aggregates relevant summaries into the current chat's carryover data, and then starts the actual chat process via the sender object.*


### a_initiate_chats (function, L267-L325)

> *Summary: This asynchronous function orchestrates multiple agent chats based on a provided queue of configuration dictionaries. It processes the chats in an order determined by dependencies, concurrently running them and returning a dictionary mapping Chat IDs to their final results upon completion.*

