# examples/stt_tts.py/stt_tts.py

1 function(s): main.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| main | function |  |

## Chunks

### main (function, L16-L33)

> *Summary: This function orchestrates a real-time voice interaction loop by recording user audio, sending it to an OpenAI transcription pipeline for processing, and streaming the resulting response back to the user via an audio player. It performs two sequential rounds of input/output exchange: first playing the initial reply while capturing new input, and then using that second input to generate a final response.*

