# test/test_token_count.py

5 function(s): test_num_tokens_from_functions, test_num_token_from_messages, test_num_tokens_from_gpt_image, test_count_token, test_model_aliases.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_num_tokens_from_functions | function |  |
| test_num_token_from_messages | function |  |
| test_num_tokens_from_gpt_image | function |  |
| test_count_token | function |  |
| test_model_aliases | function |  |

## Chunks

### test_num_tokens_from_functions (function, L62-L63)

> *Summary: This test verifies that a function correctly calculates the token count from a list of input functions. It asserts that the actual returned count matches the predefined `expected_count`.*


### test_num_token_from_messages (function, L75-L89)

> *Summary: Asserts that the token count derived from a predefined list of message objects matches an expected integer value when passed along with a specified model name. It tests the `_num_token_from_messages` utility function against this fixed input structure.*


### test_num_tokens_from_gpt_image (function, L93-L135)

> *Summary: This test verifies token counting for multimodal inputs by calling `count_token` with messages containing both text and an image. It asserts that the returned total accurately reflects the sum of text tokens plus the specific token count assigned to the image, differentiating between high and low detail settings.*


### test_count_token (function, L138-L156)

> *Summary: This test verifies the accuracy of token counting and usage calculations for both message lists and raw strings. It asserts that provided inputs yield expected token counts, percentage utilization against a 4096 limit, and remaining token capacity.*


### test_model_aliases (function, L159-L165)

> *Summary: Verifies that the token limit retrieval function returns consistent values when provided with different, yet equivalent, model alias strings (e.g., "gpt35-turbo" vs. "gpt-3.5-turbo"). This ensures API compatibility across various naming conventions for supported models.*

