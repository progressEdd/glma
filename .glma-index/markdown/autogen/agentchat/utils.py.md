# autogen/agentchat/utils.py

6 function(s): consolidate_chat_info, gather_usage_summary, parse_tags_from_content, _parse_tags_from_text, _parse_attributes_from_tags, _reconstruct_attributes.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| consolidate_chat_info | function |  |
| gather_usage_summary | function |  |
| parse_tags_from_content | function |  |
| _parse_tags_from_text | function |  |
| _parse_attributes_from_tags | function |  |
| _reconstruct_attributes | function |  |

## Chunks

### consolidate_chat_info (function, L14-L33)

> *Summary: This utility standardizes chat history by ensuring it's a list and validates each entry for required fields like "sender" and "recipient." It also checks that if `reflection_with_llm` is specified, an LLM client is available on either the sender or recipient.*


### gather_usage_summary (function, L37-L101)

> *Summary: Aggregates token and cost usage across a list of agents by combining summaries from both cached and actual inference data. It returns a dictionary containing two nested structures: one for total usage including cache, and another for usage excluding the cache.*


### parse_tags_from_content (function, L104-L141)

> *Summary: Extracts structured data from message content by searching for a specified HTML tag pattern. It accepts either a string or a list of content items (handling multimodal input) and returns a list of dictionaries detailing the found tags and their attributes.*


### _parse_tags_from_text (function, L144-L153)

> *Summary: Extracts structured data from a given text string based on a specified XML-like tag format. It iterates over all occurrences matching the pattern `<tag attribute_string>` and returns a list of dictionaries containing the tag name, parsed attributes, and the full regex match object for each instance.*


### _parse_attributes_from_tags (function, L156-L179)

> *Summary: Parses attribute key-value pairs from a string of HTML-like tags. It extracts attributes, handling both unquoted and quoted values, and aggregates any attributes without an explicit value into a 'src' field within the returned dictionary.*


### _reconstruct_attributes (function, L182-L206)

> *Summary: This utility function merges fragmented attribute strings from an input list into complete attributes. It iterates through the list, appending subsequent non-attribute elements to the last recognized attribute if one has already been found or started.*

