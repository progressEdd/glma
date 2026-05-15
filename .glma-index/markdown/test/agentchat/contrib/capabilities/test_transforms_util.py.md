# test/agentchat/contrib/capabilities/test_transforms_util.py

5 function(s): test_cache_content, test_cache_key, test_min_tokens_reached, test_count_text_tokens, test_is_content_text_empty.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_cache_content | function |  |
| test_cache_key | function |  |
| test_min_tokens_reached | function |  |
| test_count_text_tokens | function |  |
| test_is_content_text_empty | function |  |

## Chunks

### test_cache_content (function, L30-L49)

> *Summary: This test verifies the functionality of caching content by setting and retrieving data from a disk-backed `Cache` instance using various input types (string, list/tuple, and `None`). It asserts that retrieved values match the stored inputs and correctly handles edge cases like attempting to use `None` for cache operations.*


### test_cache_key (function, L53-L60)

> *Summary: This test verifies that the `transforms_util.cache_key` function produces identical keys for identical input messages and distinct keys for different input messages, given a fixed context size of 10. It takes two message dictionaries as input and asserts the consistency of the generated cache keys based on content equality.*


### test_min_tokens_reached (function, L64-L67)

> *Summary: Verifies that a utility function correctly determines when the minimum token count has been reached for a given message, testing scenarios both with and without an initial threshold. It asserts expected boolean outcomes based on whether the provided token limit is met or exceeded by the message's inherent token count.*


### test_count_text_tokens (function, L71-L72)

> *Summary: Verifies that the provided `transforms_util.count_text_tokens` function accurately counts the tokens within a message's content against an expected value stored in the message dictionary. It asserts equality between the calculated token count and the pre-defined `text_tokens`.*


### test_is_content_text_empty (function, L76-L77)

> *Summary: Verifies that a utility function correctly determines if the text content of a message is empty by comparing its result against whether the message's token count is zero. It takes a dictionary containing message data as input and asserts a boolean output based on the provided structure.*

