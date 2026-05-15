# autogen/tools/experimental/google/drive/toolkit.py

1 class(es): GoogleDriveToolkit. 2 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| GoogleDriveToolkit | class |  |

## Chunks

### GoogleDriveToolkit (class, L25-L88)

> *Summary: This class provides a set of callable tools to interact with Google Drive, initialized with OAuth credentials and a target download directory. It exposes methods to list files within specified folders or download individual files from the drive based on provided file information.*


### __init__ (method, L28-L81, parent: GoogleDriveToolkit)

> *Summary: Initializes a Google Drive toolkit by setting up the service using provided credentials and defining two callable tools: one to list files/folders and another to download specific files. It ensures the specified download directory exists before registering the selected tools with its parent class.*


### recommended_scopes (method, L84-L88, parent: GoogleDriveToolkit)

> *Summary: Provides a list of essential Google Drive API scopes required for utilizing the associated toolkit's functionalities. It returns a static list containing `"https://www.googleapis.com/auth/drive.readonly"`.*

