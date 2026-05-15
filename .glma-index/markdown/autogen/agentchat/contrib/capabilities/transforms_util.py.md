# autogen/agentchat/contrib/capabilities/transforms_util.py

8 function(s): cache_key, cache_content_get, cache_content_set, min_tokens_reached, count_text_tokens, is_content_right_type, is_content_text_empty, should_transform_message.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| cache_key | function |  |
| cache_content_get | function |  |
| cache_content_set | function |  |
| min_tokens_reached | function |  |
| count_text_tokens | function |  |
| is_content_right_type | function |  |
| is_content_text_empty | function |  |
| should_transform_message | function |  |

## Chunks

### cache_key (function, L16-L24)

> *Summary: Generates a unique string identifier by concatenating the string representations of provided message content and any additional hashable arguments. This function serves to create consistent keys for caching based on input parameters.*


### cache_content_get (function, L27-L37)

> *Summary: Retrieves previously stored message content using a provided cache object and string key. It returns the cached content if found, otherwise it returns `None`.*


### cache_content_set (function, L40-L51)

> *Summary: This utility function stores message content and optional extra data into a provided cache object using a specified key. It conditionally writes the tuple containing the content and extras to the cache if a valid cache instance is supplied.*


### min_tokens_reached (function, L54-L65)

> *Summary: Checks if the cumulative token count of a list of message dictionaries meets or exceeds a specified minimum. It returns `True` immediately if no minimum token threshold is provided.*


### count_text_tokens (function, L68-L83)

> *Summary: Determines the total number of text tokens within a message content structure, which can be a string or a list containing strings or nested objects with a "text" field. It recursively sums the token counts from all textual components found in the input.*


### is_content_right_type (function, L86-L88)

> *Summary: Checks if an input `content` object is either a string or a list. Returns `True` if it matches one of these types, otherwise returns `False`.*


### is_content_text_empty (function, L91-L108)

> *Summary: Determines if a message's content lacks textual information by inspecting its type. It returns `True` if the input is empty, or if it's a list containing no strings or dictionaries with non-empty "text" fields.*


### should_transform_message (function, L111-L122)

> *Summary: Determines if a message requires transformation by checking it against a provided filter configuration. It returns `True` if no filter is present or if the message matches the criteria defined in the filter dictionary (respecting an exclusion flag).*

