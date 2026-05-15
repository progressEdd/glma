# test/test_conftest.py

1 function(s): test_credentials_from_test_param_fixture. 1 class(es): TestSecrets. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_credentials_from_test_param_fixture | function |  |
| TestSecrets | class |  |

## Chunks

### test_credentials_from_test_param_fixture (function, L21-L40)

> *Summary: Validates that the `Credentials` object provided by a test parameter fixture correctly matches the expected API type based on the name of the test function being executed. It checks if the first configuration in the credentials list aligns with whether the test involves GPT-4/OpenAI, Gemini, or Anthropic models.*


### TestSecrets (class, L43-L78)

> *Summary: This test verifies that sensitive data added to the `Secrets` manager is correctly redacted when it appears in standard output or error streams during testing. It achieves this by simulating a test run where an exception intentionally exposes a secret and asserting that the output contains masked placeholders instead of the actual secret value.*


### test_sanitize_secrets (method, L44-L48, parent: TestSecrets)

> *Summary: Tests the secret sanitization functionality by adding a known secret and then asserting that a sample string containing that secret is correctly masked with asterisks upon calling `sanitize_secrets`.*


### test_sensitive_output_is_sanitized (method, L50-L78, parent: TestSecrets)

> *Summary: This test verifies that sensitive data, when accidentally leaked via an exception during testing, is properly sanitized in the captured output. It achieves this by setting up a temporary environment where a secret is registered and then asserting that the secret string does not appear in the combined standard output and error streams.*

