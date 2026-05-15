# test/agentchat/contrib/test_web_surfer.py

3 function(s): test_web_surfer, test_web_surfer_oai, test_web_surfer_bing.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_web_surfer | function |  |
| test_web_surfer_oai | function |  |
| test_web_surfer_bing | function |  |

## Chunks

### test_web_surfer (function, L38-L90)

> *Summary: This test verifies the functionality of a web surfing agent by mocking API keys and executing navigation, scrolling, and search functions against a configured `WebSurferAgent`. It asserts correct behavior for page transitions, boundary conditions (scrolling too far), and expected failures when necessary external APIs are unavailable.*


### test_web_surfer_oai (function, L95-L128)

> *Summary: This test verifies the `WebSurferAgent` by initiating multiple chats with a user proxy, using specific OpenAI and GPT-4o credentials for configuration. It tests the agent's ability to perform various web interactions like visiting pages, scrolling, and answering questions based on the content.*


### test_web_surfer_bing (function, L135-L162)

> *Summary: This test verifies the functionality of a `WebSurferAgent` by executing its search functions against Bing. It asserts that both informational and navigational web searches return expected content, including specific address formats and page status messages.*

