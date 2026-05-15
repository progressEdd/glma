# autogen/beta/events/input_events.py

20 function(s): ImageInput, ImageInput, ImageInput, ImageInput, ImageInput, DocumentInput, DocumentInput, DocumentInput, DocumentInput, DocumentInput and 10 more. 8 class(es): Input, ModelRequest, DataInput, TextInput, BinaryType, BinaryInput, FileIdInput, UrlInput. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Input | class |  |
| ModelRequest | class |  |
| DataInput | class |  |
| TextInput | class |  |
| BinaryType | class |  |
| BinaryInput | class |  |
| FileIdInput | class |  |
| UrlInput | class |  |
| ImageInput | function |  |
| ImageInput | function |  |
| ImageInput | function |  |
| ImageInput | function |  |
| ImageInput | function |  |
| DocumentInput | function |  |
| DocumentInput | function |  |
| DocumentInput | function |  |
| DocumentInput | function |  |
| DocumentInput | function |  |
| AudioInput | function |  |
| AudioInput | function |  |
| AudioInput | function |  |
| AudioInput | function |  |
| AudioInput | function |  |
| VideoInput | function |  |
| VideoInput | function |  |
| VideoInput | function |  |
| VideoInput | function |  |
| VideoInput | function |  |

## Chunks

### Input (class, L23-L34)

> *Summary: Provides a base for all input events to the model. It ensures that any provided content—whether it's an existing `Input`, a string, or another type—is converted into a concrete `Input` subclass (`TextInput` or `DataInput`) before being used.*


### ensure_input (method, L29-L34, parent: Input)

> *Summary: This method validates and standardizes incoming message content. It returns the original `Input` if it's already of that type, wraps a string in `TextInput`, or defaults to wrapping any other input as `DataInput`.*


### ModelRequest (class, L37-L44)

> *Summary: Represents a user turn sent to the model, holding a list of input parts. It provides a class method to construct an instance from an iterable of strings or `Input` objects after ensuring they are valid inputs.*


### ensure_request (method, L43-L44, parent: ModelRequest)

> *Summary: This method takes an iterable of messages (strings or `Input` objects) and constructs a `ModelRequest` instance by ensuring each message is properly formatted as an input. It returns the fully constructed request object.*


### DataInput (class, L47-L50)

> *Summary: Represents an event carrying data intended for the model. It accepts a `SendableMessage` object as its primary input.*


### TextInput (class, L53-L62)

> *Summary: Represents a text input event intended for the model. It takes a string `content` as input and outputs a dictionary formatted for API consumption, explicitly setting the role to "user".*


### to_api (method, L58-L62, parent: TextInput)

> *Summary: Converts the event object into a dictionary format suitable for API consumption. It packages the event's content and explicitly sets the role to "user".*


### BinaryType (class, L65-L70)

> *Summary: Defines an enumeration of supported binary data types. It provides constant string values like "binary", "image", and "audio" for classifying different media inputs.*


### BinaryInput (class, L73-L80)

> *Summary: Represents an input event carrying raw binary data to the model. It accepts byte data, a media type specification, and optional vendor-specific metadata.*


### FileIdInput (class, L83-L87)

> *Summary: Represents an input event that references a previously uploaded file using its unique identifier. It accepts the `file_id` string and optionally includes the original `filename`.*


### UrlInput (class, L90-L93)

> *Summary: Represents an input that expects a URL string, inheriting from a base `Input` class. It is typed as a binary data type and stores the provided URL in its `url` attribute.*


### ImageInput (function, L97-L97)

> *Summary: Creates a `UrlInput` object from a provided image URL string. This function encapsulates the input data for an image resource.*


### ImageInput (function, L101-L101)

> *Summary: Creates an input event representing an image by accepting a required `file_id` and an optional `filename`. It returns a structured `FileIdInput` object.*


### ImageInput (function, L105-L105)

> *Summary: Creates a binary input object containing image data and its corresponding MIME type. It accepts raw byte data and an `ImageMediaType` enum as inputs to produce the structured `BinaryInput`.*


### ImageInput (function, L109-L109)

> *Summary: Creates a binary input object from an image file specified by its path. It optionally accepts a specific `ImageMediaType` to define the content type of the image data.*


### ImageInput (function, L112-L164)

> *Summary: This factory function constructs an image input event based on provided parameters. It accepts a URL string, a pre-uploaded file ID, raw binary data (requiring a media type), or a local file path to generate the appropriate `UrlInput`, `FileIdInput`, or `BinaryInput`.*


### DocumentInput (function, L168-L168)

> *Summary: Creates a `UrlInput` object from a provided URL string, effectively wrapping the input for subsequent processing.*


### DocumentInput (function, L172-L172)

> *Summary: Creates an input event representing a document by accepting a required `file_id` and an optional `filename`. It returns a structured `FileIdInput` object.*


### DocumentInput (function, L176-L176)

> *Summary: Creates a `BinaryInput` object from raw byte data and its associated MIME type. This function packages document content for subsequent processing within the system.*


### DocumentInput (function, L180-L180)

> *Summary: Accepts a file path and optional media type to create an input object that holds binary data. This function returns a `BinaryInput` instance ready for processing.*


### DocumentInput (function, L183-L235)

> *Summary: This factory function constructs various document input event types based on provided arguments. It accepts a URL, file ID, local path, or raw binary data along with an optional media type to return the appropriate `UrlInput`, `FileIdInput`, or `BinaryInput`.*


### AudioInput (function, L239-L239)

> *Summary: Creates a `UrlInput` object from a provided audio file URL string. This function serves to wrap an external audio resource into the system's input format.*


### AudioInput (function, L243-L243)

> *Summary: Creates an input event representing audio data, requiring a `file_id` and optionally accepting a `filename`. It returns a structured `FileIdInput` object.*


### AudioInput (function, L247-L247)

> *Summary: Creates a `BinaryInput` object representing audio input by accepting raw byte data and its corresponding audio media type. This function packages the necessary audio information for subsequent processing within the system.*


### AudioInput (function, L251-L251)

> *Summary: Creates a binary input object representing audio data from a specified file path. It accepts the file path and an optional `AudioMediaType` to define the audio format.*


### AudioInput (function, L254-L306)

> *Summary: This factory function constructs an audio input event based on provided parameters. It accepts a URL, pre-uploaded file ID, raw binary data (requiring a media type), or a local file path to determine the appropriate `UrlInput`, `FileIdInput`, or `BinaryInput` object.*


### VideoInput (function, L310-L310)

> *Summary: Creates a `UrlInput` object from a provided video URL string. This function encapsulates the input source as a specific type of URL reference.*


### VideoInput (function, L314-L314)

> *Summary: Creates an input event representing a video source using a required `file_id` and an optional `filename`. It returns a structured `FileIdInput` object.*


### VideoInput (function, L318-L318)

> *Summary: Creates a `BinaryInput` object representing video input by accepting raw byte data and its corresponding media type. This function packages the necessary binary stream information for processing.*


### VideoInput (function, L322-L322)

> *Summary: Creates a `BinaryInput` object representing video data from a specified file path. It accepts the file path and an optional `VideoMediaType` to define the input source.*


### VideoInput (function, L325-L377)

> *Summary: This factory function constructs various video input event objects based on provided parameters. It accepts a URL string, a pre-uploaded file ID, raw binary data (requiring a media type), or a local file path to determine the appropriate `UrlInput`, `FileIdInput`, or `BinaryInput` output.*

