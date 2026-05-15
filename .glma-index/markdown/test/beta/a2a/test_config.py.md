# test/beta/a2a/test_config.py

1 function(s): _card_with_interfaces. 1 class(es): TestFromCardUrlResolution. 5 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _card_with_interfaces | function |  |
| TestFromCardUrlResolution | class |  |

## Chunks

### _card_with_interfaces (function, L14-L31)

> *Summary: Constructs an `AgentCard` object configured to support multiple external interfaces. It accepts a variable number of URLs and configures each one with JSON-RPC protocol binding for communication.*


### TestFromCardUrlResolution (class, L34-L58)

> *Summary: These tests verify the logic for resolving a `card_url` when creating an `A2AConfig` from a card object. It ensures that the configuration prioritizes explicit overrides, then selects the first non-empty interface URL, and raises errors if no valid URL can be determined.*


### test_picks_first_non_empty_interface_url (method, L35-L38, parent: TestFromCardUrlResolution)

> *Summary: When provided a card with multiple interface URLs, this test verifies that the configuration object selects and uses the first non-empty URL found in the card's interfaces. It asserts that `config.card_url` matches the second specified URL when the first is empty.*


### test_picks_first_when_all_have_urls (method, L40-L43, parent: TestFromCardUrlResolution)

> *Summary: When provided a card object where all interfaces have URLs, this test asserts that the resulting configuration selects the URL from the first interface encountered. It takes a pre-configured card and verifies which URL is chosen by the `A2AConfig` factory method.*


### test_explicit_url_overrides_card (method, L45-L48, parent: TestFromCardUrlResolution)

> *Summary: When provided a card object and an explicit `card_url`, this test verifies that the configuration correctly prioritizes the supplied URL over any URL embedded within the card itself. It asserts that the resulting configuration's `card_url` matches the override value.*


### test_no_interfaces_and_no_override_raises (method, L50-L53, parent: TestFromCardUrlResolution)

> *Summary: Asserts that attempting to create an `A2AConfig` from a card object lacking both interfaces and configuration overrides raises an `A2AInvalidCardError`. This test verifies the validation logic when necessary components are absent.*


### test_all_empty_urls_and_no_override_raises (method, L55-L58, parent: TestFromCardUrlResolution)

> *Summary: This test verifies that attempting to configure an A2A system with a card containing empty URLs and no overrides raises an `A2AInvalidCardError`. It achieves this by calling `A2AConfig.from_card` on a specially constructed card object.*

