# test/beta/config/anthropic/tools/test_web_search.py

7 function(s): test_defaults, test_with_max_uses, test_with_user_location, test_with_allowed_domains, test_with_blocked_domains, test_dynamic_version, test_dynamic_version_with_domains.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_defaults | function |  |
| test_with_max_uses | function |  |
| test_with_user_location | function |  |
| test_with_allowed_domains | function |  |
| test_with_blocked_domains | function |  |
| test_dynamic_version | function |  |
| test_dynamic_version_with_domains | function |  |

## Chunks

### test_defaults (function, L13-L21)

> *Summary: This test verifies that the `WebSearchTool` correctly generates a specific API schema when provided with a context. It asserts that the resulting tool definition matches an expected structure for web search functionality.*


### test_with_max_uses (function, L25-L34)

> *Summary: This test verifies that a `WebSearchTool` configured with a maximum usage limit correctly generates the expected API schema. It asserts that the resulting tool definition includes the specified `max_uses` value of 10.*


### test_with_user_location (function, L38-L54)

> *Summary: This test verifies that a `WebSearchTool` correctly incorporates user location data when generating its API schema. It asserts the resulting structure matches an expected format, including specific city, country, and timezone details for London.*


### test_with_allowed_domains (function, L58-L67)

> *Summary: This test verifies that a `WebSearchTool` correctly generates an API schema when initialized with specific allowed domains. It asserts the resulting structure matches the expected format, including the provided domain list.*


### test_with_blocked_domains (function, L71-L80)

> *Summary: This test verifies that the `WebSearchTool` correctly incorporates a list of blocked domains when generating its API schema. It asserts that the resulting schema includes `"untrusted.com"` in the `blocked_domains` field.*


### test_dynamic_version (function, L84-L92)

> *Summary: This test verifies that a specific versioned `WebSearchTool` correctly generates an API schema. It asserts the resulting structure matches the expected format, including the specified tool version.*


### test_dynamic_version_with_domains (function, L96-L112)

> *Summary: This test verifies that a `WebSearchTool` correctly serializes its configuration when generating schemas. It asserts the resulting API structure matches the provided inputs, including specific versioning and domain restrictions.*

