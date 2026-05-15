# test/beta/events/test_image_input.py

2 function(s): test_url_returns_image_url_input, test_no_args_raises. 3 class(es): TestFileId, TestData, TestPath. 9 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| test_url_returns_image_url_input | function |  |
| TestFileId | class |  |
| TestData | class |  |
| TestPath | class |  |
| test_no_args_raises | function |  |

## Chunks

### test_url_returns_image_url_input (function, L12-L16)

> *Summary: This test verifies that providing a URL string to the `ImageInput` constructor results in an object of type `UrlInput`, and confirms the original URL is correctly stored within it.*


### TestFileId (class, L19-L31)

> *Summary: This test verifies that `ImageInput` correctly constructs a `FileIdInput` object based on provided inputs. It asserts that the resulting object holds the correct `file_id` and handles optional `filename` assignment appropriately.*


### test_returns_image_file_id_input (method, L20-L25, parent: TestFileId)

> *Summary: This test verifies that providing a `file_id` string to the `ImageInput` constructor correctly produces an instance of `FileIdInput`, retaining the input ID and setting the filename to `None`.*


### test_with_filename (method, L27-L31, parent: TestFileId)

> *Summary: This test verifies that providing a `file_id` and `filename` to the input constructor correctly instantiates an object of type `FileIdInput` and stores the provided filename. It asserts both the resulting class type and the accuracy of the stored filename attribute.*


### TestData (class, L34-L44)

> *Summary: This class tests the `ImageInput` constructor's behavior when initialized with image data. It verifies that providing both binary data and a media type results in a `BinaryInput` object containing the correct values, while omitting the media type correctly raises a `ValueError`.*


### test_returns_binary_input (method, L35-L40, parent: TestData)

> *Summary: This test verifies that an `ImageInput` object correctly wraps and preserves binary data and its associated media type when instantiated. It asserts the resulting object is a `BinaryInput` instance with the exact input values.*


### test_missing_media_type_raises (method, L42-L44, parent: TestData)

> *Summary: Asserts that instantiating `ImageInput` with raw byte data lacking a specified media type raises a `ValueError`. This test verifies the input validation mechanism for image data processing.*


### TestPath (class, L47-L88)

> *Summary: These tests verify the `ImageInput` class's ability to infer media types from file paths, correctly handling PNG and JPEG extensions while raising errors for unknown ones unless an explicit type is provided. It also confirms that string representations of paths are accepted as input.*


### test_infers_png (method, L48-L56, parent: TestPath)

> *Summary: This test verifies that an `ImageInput` object correctly parses a PNG file provided as input. It asserts the resulting object is a `BinaryInput`, contains the original byte data, and has the correct MIME type set to `"image/png"`.*


### test_infers_jpeg (method, L58-L64, parent: TestPath)

> *Summary: This test verifies that an `ImageInput` object correctly infers the media type as `"image/jpeg"` when initialized with a file containing JPEG data. It achieves this by creating a temporary file and passing its path to the input constructor.*


### test_unknown_extension_raises (method, L66-L71, parent: TestPath)

> *Summary: This test verifies that attempting to process an image file with an unrecognized extension (like `.bmp` in this case) correctly raises a `ValueError` indicating the inability to infer the format. It achieves this by creating a temporary file and passing its path to the `ImageInput` constructor within a `pytest.raises` context manager.*


### test_unknown_extension_with_explicit_media_type (method, L73-L80, parent: TestPath)

> *Summary: When provided a file with an unknown extension but an explicit `image/png` media type, the function creates a `BinaryInput` object that correctly retains the specified PNG media type. This tests how the system handles mismatched file extensions and declared content types.*


### test_accepts_string_path (method, L82-L88, parent: TestPath)

> *Summary: This test verifies that the `ImageInput` constructor correctly processes a file path provided as a string input. It asserts that when initialized with a valid image file path, the resulting object reports the correct media type ("image/webp").*


### test_no_args_raises (function, L91-L93)

> *Summary: Asserts that instantiating the `ImageInput` class without any arguments raises a `ValueError` containing the specific message "requires one of". This verifies that the input object enforces required parameters upon initialization.*

