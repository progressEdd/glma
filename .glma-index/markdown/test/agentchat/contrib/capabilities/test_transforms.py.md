# test/agentchat/contrib/capabilities/test_transforms.py

25 function(s): get_long_messages, get_short_messages, get_no_content_messages, get_tool_messages, get_tool_messages_kept, get_messages_with_names, get_messages_with_names_post_start, get_messages_with_names_post_end, get_messages_with_names_post_filtered, get_text_compressors and 15 more. 1 class(es): _MockTextCompressor. 1 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _MockTextCompressor | class |  |
| get_long_messages | function |  |
| get_short_messages | function |  |
| get_no_content_messages | function |  |
| get_tool_messages | function |  |
| get_tool_messages_kept | function |  |
| get_messages_with_names | function |  |
| get_messages_with_names_post_start | function |  |
| get_messages_with_names_post_end | function |  |
| get_messages_with_names_post_filtered | function |  |
| get_text_compressors | function |  |
| message_history_limiter | function |  |
| message_history_limiter_keep_first | function |  |
| message_token_limiter | function |  |
| message_token_limiter_with_threshold | function |  |
| _filter_dict_test | function |  |
| test_message_history_limiter_apply_transform | function |  |
| test_message_history_limiter_apply_transform_keep_first | function |  |
| test_message_history_limiter_get_logs | function |  |
| test_message_token_limiter_apply_transform | function |  |
| test_message_token_limiter_with_filter | function |  |
| test_message_token_limiter_with_threshold_apply_transform | function |  |
| test_message_token_limiter_get_logs | function |  |
| test_text_compression | function |  |
| test_text_compression_with_filter | function |  |
| test_message_content_name | function |  |

## Chunks

### _MockTextCompressor (class, L23-L25)

> *Summary: This mock class simulates a text compression service by accepting a string input and returning a dictionary containing an empty `compressed_prompt`. It serves as a placeholder for actual compression logic during testing.*


### compress_text (method, L24-L25, parent: _MockTextCompressor)

> *Summary: This method takes a string of text and returns a dictionary containing an empty key for the compressed prompt. It serves as a placeholder implementation for text compression logic.*


### get_long_messages (function, L28-L35)

> *Summary: Returns a predefined list of message dictionaries simulating a conversation history. This data structure includes various roles and content types, designed to test handling of lengthy inputs.*


### get_short_messages (function, L38-L43)

> *Summary: Returns a predefined list of message dictionaries simulating a short conversation history. This data structure is used for testing conversational agent capabilities.*


### get_no_content_messages (function, L46-L47)

> *Summary: Returns a predefined list containing two message dictionaries: one user message with a function call and one assistant message where the content is explicitly set to `None`. This serves as a test fixture for scenarios involving empty or null content.*


### get_tool_messages (function, L50-L57)

> *Summary: Returns a predefined list of message dictionaries simulating a multi-turn conversation involving user input, tool calls, and subsequent responses. This structure is used to provide test data for agent interactions.*


### get_tool_messages_kept (function, L60-L67)

> *Summary: Returns a predefined list of message dictionaries simulating a conversation history involving user input, tool calls, and subsequent tool responses. This structure is used for testing agent interactions with external tools.*


### get_messages_with_names (function, L70-L76)

> *Summary: Returns a predefined list of message dictionaries, simulating a chat history. Each dictionary specifies a role and content, with some user messages also including a unique name.*


### get_messages_with_names_post_start (function, L79-L85)

> *Summary: Returns a predefined list of message dictionaries, simulating a conversation history. Each dictionary includes a `role`, `content`, and optionally a `name` for user messages.*


### get_messages_with_names_post_end (function, L88-L94)

> *Summary: Returns a predefined list of message dictionaries, simulating a chat history. Each dictionary includes a role and content, with user messages also containing a specific `name` field.*


### get_messages_with_names_post_filtered (function, L97-L103)

> *Summary: Returns a predefined list of message dictionaries, simulating chat history. Each dictionary includes a `role`, `content`, and optionally a `name` for user messages.*


### get_text_compressors (function, L106-L116)

> *Summary: This function returns a list of text compressor instances, starting with a mock implementation. It conditionally adds an `LLMLingua` compressor if the optional import of `llmlingua` succeeds.*


### message_history_limiter (function, L120-L121)

> *Summary: This factory function creates and returns a `MessageHistoryLimiter` instance configured to retain only the last three messages. It serves as a standardized way to instantiate this history management utility.*


### message_history_limiter_keep_first (function, L125-L126)

> *Summary: Creates a `MessageHistoryLimiter` instance configured to retain only the first message when the history exceeds three messages. This utility is used for testing scenarios involving message history constraints.*


### message_token_limiter (function, L130-L131)

> *Summary: Creates and returns a `MessageTokenLimiter` instance configured to restrict messages to a maximum of three tokens. This utility is used for enforcing token constraints on chat messages.*


### message_token_limiter_with_threshold (function, L135-L136)

> *Summary: Creates and returns a `MessageTokenLimiter` instance configured to enforce a maximum of 1 token per message while requiring at least 10 tokens. This setup is used for testing specific token constraints within agent chat capabilities.*


### _filter_dict_test (function, L139-L163)

> *Summary: Determines a boolean based on content length comparisons between two message dictionaries, applying different logic depending on the message's role and an `exclude_filter` flag. It checks if the post-transformed message content is shorter than or equal to the pre-transformed message content under specific conditions.*


### test_message_history_limiter_apply_transform (function, L179-L185)

> *Summary: This test verifies that a message history limiter correctly truncates an input list of messages to a specified length. It asserts the resulting list's size and checks specific role types for the first two elements when using a predefined set of tool-related messages.*


### test_message_history_limiter_apply_transform_keep_first (function, L198-L206)

> *Summary: This test verifies that a message history limiter, configured to keep the first items, correctly truncates an input list of messages. It asserts both the final length and specific roles of elements within the resulting, transformed message sequence.*


### test_message_history_limiter_get_logs (function, L219-L224)

> *Summary: This test verifies the logging and effect tracking of a message history limiter. It applies the transformation to input messages and then retrieves the generated log string and whether an effect occurred by comparing pre- and post-transformation states against expected values.*


### test_message_token_limiter_apply_transform (function, L234-L242)

> *Summary: This test verifies that a token limiter correctly modifies a list of messages. It applies the transformation to a copy of input messages and asserts that the total content tokens match an expected count, while also checking the resulting message list length.*


### test_message_token_limiter_with_filter (function, L246-L264)

> *Summary: This test verifies the behavior of a message token limiter when configured with specific filters. It asserts that messages are either completely removed or retained based on whether they match the specified roles in the input list.*


### test_message_token_limiter_with_threshold_apply_transform (function, L271-L279)

> *Summary: This test verifies the behavior of a token limiter transform by applying it to a list of messages. It asserts that the total token count and the resulting number of messages match predefined expectations after transformation.*


### test_message_token_limiter_get_logs (function, L290-L295)

> *Summary: This test verifies the logging and effect tracking of a token limiter transformation. It applies the limiter to input messages, then retrieves the generated log string and whether an effect occurred by comparing pre- and post-transformation message states against expected values.*


### test_text_compression (function, L302-L324)

> *Summary: This test verifies the `TextMessageCompressor`'s functionality by applying it to sample text messages. It asserts that after transformation, the resulting content length is strictly shorter than the original input content for both single and multiple message inputs.*


### test_text_compression_with_filter (function, L329-L346)

> *Summary: This test verifies the behavior of a message compressor when applying different filtering rules. It asserts that messages are correctly truncated based on whether the filter is inclusive or exclusive for specific roles like "user."*


### test_message_content_name (function, L350-L403)

> *Summary: This test verifies the `TextMessageContentName` transformation by applying it to a list of messages, asserting correct output formatting when names are added at the start or end. It also validates filtering logic (inclusion/exclusion) and ensures proper input validation for configuration parameters like position and format string.*

