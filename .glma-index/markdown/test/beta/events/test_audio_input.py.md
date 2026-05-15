# test/beta/events/test_audio_input.py

2 function(s): test_url_returns_audio_url_input, test_no_args_raises. 3 class(es): TestFileId, TestData, TestPath. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_url_returns_audio_url_input | function |  |
| TestFileId | class |  |
| TestData | class |  |
| TestPath | class |  |
| test_no_args_raises | function |  |

## Chunks

### test_url_returns_audio_url_input (function, L12-L16)

> *Summary: This test verifies that providing a URL string to the `AudioInput` constructor results in an object of type `UrlInput`, and confirms the stored URL matches the input value.*


### TestFileId (class, L19-L31)

> *Summary: This test verifies that the `AudioInput` constructor correctly initializes a `FileIdInput` object based on provided arguments. It confirms that both `file_id` and optional `filename` are accurately stored in the resulting input structure.*


### test_returns_file_id_input (method, L20-L25, parent: TestFileId)

> *Summary: This test verifies that instantiating `AudioInput` with a provided `file_id` correctly produces an object of type `FileIdInput`, retaining the input ID and setting the filename to `None`.*


### test_with_filename (method, L27-L31, parent: TestFileId)

> *Summary: Instantiates an `AudioInput` object using a provided file ID and filename string. It then asserts that the resulting object is of type `FileIdInput` and correctly stores the input filename.*


### TestData (class, L34-L44)

> *Summary: Verifies that the `AudioInput` constructor correctly wraps binary data and media type into a `BinaryInput` object, while also ensuring it raises a `ValueError` if the required `media_type` argument is omitted.*


### test_returns_binary_input (method, L35-L40, parent: TestData)

> *Summary: This test verifies that the `AudioInput` constructor correctly wraps input data and media type into a `BinaryInput` object. It asserts that the resulting object is of the correct type and retains the original binary data (`b"raw"`) and MIME type (`"audio/wav"`).*


### test_missing_media_type_raises (method, L42-L44, parent: TestData)

> *Summary: Asserts that instantiating `AudioInput` with raw data but no specified media type raises a `ValueError`. This test verifies the input validation for required metadata during audio stream initialization.*


### TestPath (class, L47-L89)

> *Summary: These tests verify the `AudioInput` class's ability to correctly infer audio file types from paths, handling WAV and MP3 formats while raising errors for unknown extensions unless an explicit media type is provided. It also confirms that string representations of file paths are accepted as input.*


### test_infers_wav (method, L48-L57, parent: TestPath)

> *Summary: This test verifies that the `AudioInput` constructor correctly parses a mock WAV file. It asserts that the resulting object is a `BinaryInput`, contains the expected raw data, and has the correct media type and vendor metadata derived from the input path.*


### test_infers_mp3 (method, L59-L65, parent: TestPath)

> *Summary: This test verifies that an `AudioInput` object correctly identifies the media type as `"audio/mpeg"` when initialized with a file containing MP3 data. It achieves this by creating a temporary file and passing its path to the input constructor.*


### test_unknown_extension_raises (method, L67-L72, parent: TestPath)

> *Summary: This test verifies that attempting to initialize `AudioInput` with a file having an unrecognized extension (`.xyz`) correctly raises a `ValueError`. It achieves this by creating a temporary file and passing its path to the constructor within a `pytest.raises` context manager.*


### test_unknown_extension_with_explicit_media_type (method, L74-L81, parent: TestPath)

> *Summary: When provided with a file having an unknown extension but explicitly supplied with a `media_type`, the function instantiates an input object that correctly identifies itself as binary and retains the specified media type. This test verifies that the system respects the explicit media type even when the filename suggests otherwise.*


### test_accepts_string_path (method, L83-L89, parent: TestPath)

> *Summary: Verifies that the `AudioInput` constructor correctly parses and identifies an audio file when provided with a string path to a local file. It creates a temporary OGG file, initializes `AudioInput` using its string representation, and asserts the resulting media type is `"audio/ogg"`.*


### test_no_args_raises (function, L92-L94)

> *Summary: Asserts that instantiating the `AudioInput` class without any arguments raises a `ValueError` containing the specific message "requires one of". This verifies that the constructor enforces required input parameters.*

