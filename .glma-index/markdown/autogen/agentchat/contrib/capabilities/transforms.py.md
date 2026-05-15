# autogen/agentchat/contrib/capabilities/transforms.py

5 class(es): MessageTransform, MessageHistoryLimiter, MessageTokenLimiter, TextMessageCompressor, TextMessageContentName. 24 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| MessageTransform | class |  |
| MessageHistoryLimiter | class |  |
| MessageTokenLimiter | class |  |
| TextMessageCompressor | class |  |
| TextMessageContentName | class |  |

## Chunks

### MessageTransform (class, L21-L53)

> *Summary: Defines a contract for message transformers that must implement `apply_transform` to process a list of messages into a new transformed list. It also requires a `get_logs` method to generate a descriptive log string and indicate if the transformation actually changed the input messages.*


### apply_transform (method, L28-L37, parent: MessageTransform)

> *Summary: This method takes a list of message dictionaries as input and returns a new list where each message has been modified according to an internal transformation logic. It serves to process and alter the content or structure of conversational history.*


### get_logs (method, L39-L53, parent: MessageTransform)

> *Summary: Generates a log string detailing message transformations by comparing pre- and post-transformation message lists. It returns this log alongside a boolean indicating if any changes occurred between the two states.*


### MessageHistoryLimiter (class, L56-L140)

> *Summary: This class truncates a list of conversation messages to maintain only the most recent entries, optionally filtering out specific senders. It accepts configuration for maximum size, preserving the first message, and excluding certain speakers before returning the limited history.*


### __init__ (method, L63-L79, parent: MessageHistoryLimiter)

> *Summary: Initializes a message history transformer with optional parameters to control context size, preserve the initial message, and filter out specific sender messages. It stores these configuration settings internally for later use in processing conversation logs.*


### apply_transform (method, L81-L122, parent: MessageHistoryLimiter)

> *Summary: This method filters and truncates a list of conversation messages based on configured limits and exclusion rules. It returns a new, potentially shortened list containing the most recent messages, respecting settings for message count, initial message retention, and tool message handling.*


### get_logs (method, L124-L136, parent: MessageHistoryLimiter)

> *Summary: Compares the length of two message lists (before and after transformation). It returns a descriptive string detailing any message removals and a boolean indicating if reduction occurred.*


### _validate_max_messages (method, L138-L140, parent: MessageHistoryLimiter)

> *Summary: Ensures the provided `max_messages` integer is either `None` or at least one. If a non-positive value is supplied, it raises a `ValueError`.*


### MessageTokenLimiter (class, L143-L326)

> *Summary: This class manages conversation history by truncating messages based on specified token limits for individual messages and the overall chat. It processes messages in reverse order, applying both per-message and total history constraints while respecting filtering rules to ensure efficient LLM processing.*


### __init__ (method, L171-L198, parent: MessageTokenLimiter)

> *Summary: Initializes a token transformation utility by accepting configuration for message and history size limits, a target model name, and optional filtering rules. It stores these parameters to govern how chat messages will be truncated or filtered during processing.*


### apply_transform (method, L200-L250, parent: MessageTokenLimiter)

> *Summary: This method truncates a conversation history based on predefined minimum and maximum token limits for the entire chat and individual messages. It iterates backward through the input message list, selectively including or truncating content to ensure the resulting list adheres to the specified token constraints.*


### get_logs (method, L252-L268, parent: MessageTokenLimiter)

> *Summary: Calculates the token difference between two message lists by summing content tokens. It returns a log string and a boolean indicating if truncation occurred, specifically when post-transformation tokens are fewer than pre-transformation tokens.*


### _truncate_str_to_tokens (method, L270-L276, parent: MessageTokenLimiter)

> *Summary: This method truncates input content to a specified token limit based on its type. If the input is a string, it uses a standard text truncation; if it's a list, it applies multimodal text truncation logic.*


### _truncate_multimodal_text (method, L278-L287, parent: MessageTokenLimiter)

> *Summary: This method processes a list of multimodal content dictionaries, selectively truncating the text within any element whose type is "text" based on a specified token limit. It returns a new list maintaining the original structure while ensuring no individual text component exceeds the token count.*


### _truncate_tokens (method, L289-L296, parent: MessageTokenLimiter)

> *Summary: This method truncates an input string to a specified token limit using the tokenizer associated with the model. It encodes the text, slices the resulting tokens to the desired count, and then decodes them back into a shortened string.*


### _validate_max_tokens (method, L298-L317, parent: MessageTokenLimiter)

> *Summary: Ensures the provided `max_tokens` value is non-negative and caps it to the model's actual limit if the input exceeds that boundary. It returns the validated token count, defaulting to a system maximum if no valid limit was specified or determined.*


### _validate_min_tokens (method, L319-L326, parent: MessageTokenLimiter)

> *Summary: Ensures token constraints are valid by checking if `min_tokens` is non-negative and if it does not exceed `max_tokens`. It returns the validated `min_tokens`, defaulting to 0 if none is provided.*


### TextMessageCompressor (class, L329-L470)

> *Summary: This class transforms a list of conversation messages by applying text compression to reduce token count, using an injected `TextCompressor` instance. It accepts configuration for filtering, minimum token thresholds, and caching, returning the modified message list along with logging capabilities detailing the total tokens saved.*


### __init__ (method, L336-L376, parent: TextMessageCompressor)

> *Summary: Initializes a transformation utility by accepting optional components like a text compressor, token thresholds, caching mechanisms, and message filters. It configures these parameters to control when and how messages are compressed or filtered before processing.*


### apply_transform (method, L378-L426, parent: TextMessageCompressor)

> *Summary: Compresses a list of conversation messages by applying configured compression logic if the total token count exceeds a minimum threshold. It iterates through messages, checks filtering criteria, and replaces content with compressed versions (using caching if available), returning the modified message list along with tracking the total token savings.*


### get_logs (method, L428-L434, parent: TextMessageCompressor)

> *Summary: Checks if token savings occurred during a transformation process by comparing pre and post-transformation message lists. It returns a descriptive string indicating the savings amount and a boolean flag reflecting whether any saving was achieved.*


### _compress (method, L436-L443, parent: TextMessageCompressor)

> *Summary: This method handles content compression by dispatching to specialized functions based on the input type. It accepts either a string or a list of multimodal content and returns the compressed content along with an integer representing the compression size.*


### _compress_multimodal (method, L445-L456, parent: TextMessageCompressor)

> *Summary: This method iterates through a message's content to apply text compression to any string or dictionary containing text. It returns the modified content and the total number of tokens saved during the compression process.*


### _compress_text (method, L458-L466, parent: TextMessageCompressor)

> *Summary: This method takes a string input, compresses it using an internal compressor configured with specific arguments, and returns the resulting compressed text along with the token savings achieved during compression.*


### _validate_min_tokens (method, L468-L470, parent: TextMessageCompressor)

> *Summary: Ensures that if a minimum token count is provided, it must be a positive integer. It raises a `ValueError` if the input `min_tokens` is zero or negative.*


### TextMessageContentName (class, L473-L578)

> *Summary: This class modifies a list of message dictionaries by prepending or appending the agent's name to the content based on specified formatting and position. It accepts a list of messages as input and returns a new list with the names integrated into the content, while also tracking how many messages were altered.*


### __init__ (method, L494-L522, parent: TextMessageContentName)

> *Summary: Initializes a message transformation utility by setting parameters like where to prepend agent names (`position`), the formatting string, and filtering logic. It accepts configuration dicts and booleans to control deduplication and which messages are processed or excluded from compression.*


### apply_transform (method, L524-L570, parent: TextMessageContentName)

> *Summary: This method modifies a list of message dictionaries by injecting or appending a specified name into the `content` field based on configuration. It iterates through the input messages, applying formatting rules to update the content if certain conditions regarding content presence and transformation eligibility are met.*


### get_logs (method, L572-L578, parent: TextMessageContentName)

> *Summary: Checks if the internal message count has increased; if so, it returns a string indicating the number of changes and `True`, otherwise it returns a default message and `False`. This method takes pre- and post-transformation message lists as input but primarily relies on an internal state variable.*

