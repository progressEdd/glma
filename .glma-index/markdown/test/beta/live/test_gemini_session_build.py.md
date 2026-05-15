# test/beta/live/test_gemini_session_build.py

2 function(s): gemini_client, _build. 7 class(es): TestModalities, TestAudioOutput, TestInputConfig, TestPromotedKwargs, TestInstructions, TestTools, TestMergeOrder. 16 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| gemini_client | function |  |
| _build | function |  |
| TestModalities | class |  |
| TestAudioOutput | class |  |
| TestInputConfig | class |  |
| TestPromotedKwargs | class |  |
| TestInstructions | class |  |
| TestTools | class |  |
| TestMergeOrder | class |  |

## Chunks

### gemini_client (function, L21-L25)

> *Summary: Instantiates and returns a `Client` object for the Gemini API, using an environment variable or a hardcoded test key as the API key. This setup is designed to allow in-memory testing without requiring actual network connectivity.*


### _build (function, L28-L34)

> *Summary: This function constructs a session dictionary by calling the `_build_session` method on a provided configuration object. It accepts optional lists of instructions and tool schemas to configure the resulting session data structure.*


### TestModalities (class, L37-L64)

> *Summary: This test suite verifies how different output configurations affect the resulting API payload when initializing a real-time Gemini session. It asserts that specifying audio output includes specific voice settings, text output omits audio configuration, and explicit config overrides correctly set response modalities.*


### test_default_audio_output (method, L38-L44, parent: TestModalities)

> *Summary: This test verifies the default audio output configuration when building a Gemini session. It asserts that the resulting payload correctly specifies `AUDIO` as the response modality and sets the voice to "Kore".*


### test_text_output_drops_audio_config (method, L46-L54, parent: TestModalities)

> *Summary: This test verifies that when a Gemini session is configured to produce only text output, the resulting payload correctly specifies `TEXT` as the sole response modality. It takes a client instance and asserts the structure of the built configuration object.*


### test_config_override_replaces_response_modalities (method, L56-L64, parent: TestModalities)

> *Summary: This test verifies that a configuration override correctly sets the response modalities for a Gemini session. It constructs a request using `RealTimeConfig` specifying only `"TEXT"` as the desired output modality and asserts this value is present in the resulting payload.*


### TestAudioOutput (class, L67-L91)

> *Summary: These tests verify the construction of configuration payloads for real-time audio output when using a Gemini client. They assert that the generated payload correctly includes specified voice names and language codes based on the `AudioOutput` settings provided during initialization.*


### test_voice_only (method, L68-L78, parent: TestAudioOutput)

> *Summary: This test verifies that a configuration built for voice-only output correctly sets the `speech_config` to specify the "Aoede" voice. It takes a `Client` object as input and asserts the resulting payload structure matches the expected voice setting.*


### test_voice_and_language (method, L80-L91, parent: TestAudioOutput)

> *Summary: This test verifies that a configuration object correctly serializes voice and language settings. It takes a `Client` instance as input and asserts the resulting payload contains the specified voice name ("Charon") and language code ("en-US").*


### TestInputConfig (class, L94-L137)

> *Summary: This test suite verifies the configuration serialization for real-time Gemini sessions. It asserts that various input settings, such as enabling transcription, specifying languages, and setting audio detection parameters, are correctly reflected in the generated payload structure when passed to a client.*


### test_no_user_transcription_by_default (method, L95-L103, parent: TestInputConfig)

> *Summary: This test verifies that the default configuration for a Gemini session does not include user audio transcription. It constructs a real-time configuration using a provided client and asserts the absence of the `input_audio_transcription` key in the resulting payload.*


### test_user_transcription_opt_in (method, L105-L113, parent: TestInputConfig)

> *Summary: This test verifies the initial state of a Gemini session configuration when transcription is enabled for a specific model. It asserts that the `input_audio_transcription` field in the resulting payload is an empty dictionary.*


### test_transcription_languages_propagate (method, L115-L123, parent: TestInputConfig)

> *Summary: This test verifies that specified transcription languages are correctly propagated within the request payload. It asserts that the `input_audio_transcription` section of the built payload contains the expected list of language codes provided in the configuration.*


### test_realtime_input_knobs_propagate (method, L125-L137, parent: TestInputConfig)

> *Summary: This test verifies that a specific configuration for real-time input, including an automatic activity detection setting of 500ms silence duration, is correctly packaged into the request payload when using a Gemini client. It asserts that the resulting `realtime_input_config` matches the expected structure.*


### TestPromotedKwargs (class, L140-L151)

> *Summary: This test verifies that configuration parameters like `temperature` and `max_output_tokens`, passed into a build function, are correctly included in the resulting payload structure when using a Gemini client. It asserts the presence and correct values of these specific arguments within the generated data.*


### test_temperature_and_max_output_tokens (method, L141-L151, parent: TestPromotedKwargs)

> *Summary: This test verifies that a configuration object correctly serializes the specified `temperature` (0.7) and `max_output_tokens` (1024) when building a request payload for Gemini. It asserts these values are present in the resulting dictionary structure.*


### TestInstructions (class, L154-L175)

> *Summary: This test suite verifies how system instructions are constructed when building a Gemini session configuration. It asserts that provided instruction tuples are correctly joined into the `system_instruction` field, handles cases with no input instructions, and confirms that explicit configuration overrides take precedence over passed-in instructions.*


### test_instructions_joined (method, L155-L160, parent: TestInstructions)

> *Summary: This test verifies that multiple instruction strings provided to the build function are correctly concatenated into a single system instruction string within the resulting payload. It takes a Gemini client and a tuple of instructions as input, asserting the joined output format.*


### test_no_system_instruction_when_empty (method, L162-L164, parent: TestInstructions)

> *Summary: This test verifies that no system instruction is included in the request payload when the configuration provided to the build function is empty. It asserts the absence of the `"system_instruction"` key in the resulting data structure.*


### test_config_overrides_instructions (method, L166-L175, parent: TestInstructions)

> *Summary: This test verifies that a system instruction provided in the configuration overrides any instructions passed separately. It constructs a request using a specific model and configures it with `"raw override"` as the system instruction, then asserts this value is present in the resulting payload.*


### TestTools (class, L178-L210)

> *Summary: Verifies that a provided `FunctionToolSchema` is correctly serialized into the expected JSON structure when building a Gemini real-time configuration payload. It takes a `Client` instance and asserts the resulting `tools` field matches the defined function declaration for "sum\_numbers".*


### test_function_tool_serialized (method, L179-L210, parent: TestTools)

> *Summary: This test verifies that a provided `FunctionToolSchema` is correctly serialized into the expected JSON structure for Gemini API calls. It constructs a payload containing a function declaration named "sum\_numbers" and asserts its exact representation within the output.*


### TestMergeOrder (class, L213-L235)

> *Summary: This test suite verifies how configuration settings are merged when initializing a real-time Gemini session. It asserts that explicit parameters override those in the `config` dictionary, and that unrelated keys from the `config` are correctly included alongside primary parameters.*


### test_config_overrides_typed_config (method, L214-L223, parent: TestMergeOrder)

> *Summary: This test verifies that configuration overrides take precedence when building a Gemini session payload. It asserts the final `temperature` in the resulting payload is set to $0.99$, overriding the initial value of $0.2$.*


### test_config_extends_with_unrelated_keys (method, L225-L235, parent: TestMergeOrder)

> *Summary: This test verifies that a configuration object correctly merges settings from its base and provided dictionaries. It asserts that the resulting payload contains both the explicitly set `temperature` and any extra keys like `seed` passed in the config dictionary.*

