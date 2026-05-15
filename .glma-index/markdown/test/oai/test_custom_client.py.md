# test/oai/test_custom_client.py

4 function(s): test_custom_model_client, test_registering_with_wrong_class_name_raises_error, test_not_all_clients_registered_raises_error, test_registering_with_extra_config_args.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_custom_model_client | function |  |
| test_registering_with_wrong_class_name_raises_error | function |  |
| test_not_all_clients_registered_raises_error | function |  |
| test_registering_with_extra_config_args | function |  |

## Chunks

### test_custom_model_client (function, L24-L89)

> *Summary: This test defines a mock model client that simulates API responses, allowing verification of configuration passing. It instantiates an `OpenAIWrapper` with this custom client and asserts that the wrapper correctly uses the provided parameters when generating a response.*


### test_registering_with_wrong_class_name_raises_error (function, L93-L120)

> *Summary: This test verifies that attempting to register a model client using an incorrect class name configuration raises a `ValueError`. It instantiates an `OpenAIWrapper` with a misconfigured list and then asserts the expected exception when registering the actual custom class.*


### test_not_all_clients_registered_raises_error (function, L124-L168)

> *Summary: This test verifies that an error is raised when the `OpenAIWrapper` attempts to use a model client for which it has not been explicitly registered, even if multiple configurations are provided. It initializes the wrapper with two model configurations and then calls a creation method while only registering one of the required custom clients.*


### test_registering_with_extra_config_args (function, L172-L209)

> *Summary: This test verifies that an `OpenAIWrapper` correctly registers and utilizes a custom model client implementation when provided with extra configuration arguments during registration. It asserts that the registered custom class's hook is triggered after calling the wrapper's creation method.*

