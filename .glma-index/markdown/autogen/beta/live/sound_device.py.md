# autogen/beta/live/sound_device.py

2 class(es): Recorder, Player. 17 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| Recorder | class |  |
| Player | class |  |

## Chunks

### Recorder (class, L27-L122)

> *Summary: Manages audio input, providing methods to either synchronously record a specified duration or asynchronously stream real-time audio chunks into a conversation context. It initializes with sample rate and channel settings, using `async` context managers for safe resource acquisition and release of the underlying sound device streams.*


### __init__ (method, L28-L46, parent: Recorder)

> *Summary: Initializes a sound device handler by setting audio parameters like sample rate and channel count, defaulting the block size to 100ms if not provided. It also sets up an internal context for conversation management and initializes necessary asynchronous components for input handling.*


### stream (method, L49-L50, parent: Recorder)

> *Summary: Returns the active streaming object from the device's context, providing access to real-time audio data. This method acts as a getter for the established stream connection.*


### record (method, L52-L67, parent: Recorder)

> *Summary: Captures audio from the configured sound device for a specified duration. It takes a `duration` (float) as input and returns a `VoiceInput` object containing the raw audio data encoded as 16-bit PCM bytes, sample rate, and channel count.*


### __aenter__ (method, L69-L81, parent: Recorder)

> *Summary: Upon entering an asynchronous context, this method initializes the audio recording system by setting up a queue and starting a background draining task. It then configures and starts an input stream using specified sample rate, channels, and block size parameters.*


### __aexit__ (method, L83-L99, parent: Recorder)

> *Summary: When exiting an asynchronous context, this method ensures proper cleanup of the sound device by stopping and closing any active input stream. It also cancels and awaits a draining task to gracefully shut down background operations.*


### _callback (method, L101-L106, parent: Recorder)

> *Summary: This method executes on the audio thread to safely transfer incoming audio data from a NumPy array into an asynchronous queue managed by the main event loop. It ensures thread safety by using `call_soon_threadsafe` before enqueuing the copied byte representation of the input data.*


### _enqueue (method, L108-L116, parent: Recorder)

> *Summary: This method adds an audio `chunk` of bytes to the internal queue, prioritizing fresh data by discarding the oldest item if the buffer is already full. It operates on the loop thread and uses non-blocking operations for insertion.*


### _drain_to_bus (method, L118-L122, parent: Recorder)

> *Summary: This asynchronous method continuously pulls audio chunks from an internal queue and forwards them to a context bus via a `RecordedAudioEvent`. It ensures that all queued data is processed until the queue is empty or the loop is interrupted.*


### Player (class, L125-L204)

> *Summary: Manages audio playback by setting up an output stream and a background worker thread upon entering an asynchronous context. It accepts raw byte content via the `play` method, queues it, and the worker thread continuously reads from this queue to write PCM data to the sound device until explicitly closed.*


### __init__ (method, L126-L138, parent: Player)

> *Summary: Initializes the sound device by setting up a conversation context, optionally accepting an existing output stream. It prepares internal structures including an audio queue and thread management components for handling audio playback.*


### stream (method, L141-L142, parent: Player)

> *Summary: Returns the active streaming object from the device's context, providing access to real-time audio data. This method acts as a getter for the established stream connection.*


### __aenter__ (method, L144-L155, parent: Player)

> *Summary: When entering an asynchronous context, this method initializes the audio output stream if it's missing and starts a background worker thread to process audio events. It also subscribes a callback to receive synthesized audio data from the current context.*


### __aexit__ (method, L157-L168, parent: Player)

> *Summary: When an asynchronous context manager exits, it unsubscribes any active streams and closes the device's output stream if one exists. This ensures proper cleanup of resources upon exiting the `async with` block.*


### play (method, L170-L173, parent: Player)

> *Summary: This method queues raw audio data for playback if the input `content` is not empty. It adds the provided byte sequence to an internal asynchronous queue managed by the object.*


### join (method, L175-L182, parent: Player)

> *Summary: This method checks if a worker exists and then enters a loop, acquiring a speaker lock to continuously check the audio queue until it is empty. It exits the loop once no audio data remains in the queue.*


### close (method, L184-L189, parent: Player)

> *Summary: Stops the background audio processing thread by sending a stop signal to the queue and waiting for the worker to terminate, then clears the internal worker reference.*


### _on_audio (method, L191-L192, parent: Player)

> *Summary: When a synthesized audio event is received, this method asynchronously plays the provided audio content. It takes an `SynthesizedAudioEvent` as input and performs no return value.*


### _run_worker (method, L194-L204, parent: Player)

> *Summary: Continuously processes audio data retrieved from an internal queue until a `None` signal is received. It converts the raw PCM bytes into a NumPy array and writes this buffer to the active speaker output stream while holding a lock.*

