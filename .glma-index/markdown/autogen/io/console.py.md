# autogen/io/console.py

1 class(es): IOConsole. 3 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| IOConsole | class |  |

## Chunks

### IOConsole (class, L19-L56)

> *Summary: This class implements console I/O by wrapping standard Python `print` and `input` functionality into a stream interface. It sends output via an internal event mechanism (`send`) and provides methods to read user input, optionally masking it as a password.*


### print (method, L22-L33, parent: IOConsole)

> *Summary: This method serializes provided objects along with specified separators and endings into a `PrintEvent` message before sending it through the instance's communication channel. It effectively wraps standard output printing functionality for internal event handling.*


### send (method, L35-L41, parent: IOConsole)

> *Summary: This method takes a `BaseEvent` object and prints its contents directly to the console's output stream. It serves as the mechanism for displaying events to the user interface.*


### input (method, L43-L56, parent: IOConsole)

> *Summary: Reads a line of text from standard input, optionally displaying a prompt and handling sensitive input via `getpass` if the `password` flag is set to true. Returns the user-entered string.*

