# autogen/beta/a2a/push.py

6 function(s): create_push_notification_config, get_push_notification_config, list_push_notification_configs, delete_push_notification_config, _to_proto, _from_proto. 2 class(es): A2APushAuthentication, A2APushConfig.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| A2APushAuthentication | class |  |
| A2APushConfig | class |  |
| create_push_notification_config | function |  |
| get_push_notification_config | function |  |
| list_push_notification_configs | function |  |
| delete_push_notification_config | function |  |
| _to_proto | function |  |
| _from_proto | function |  |

## Chunks

### A2APushAuthentication (class, L20-L24)

> *Summary: This class holds authentication metadata for push notification webhooks, storing the required scheme and optional opaque credentials. It serves as a container for these two string attributes.*


### A2APushConfig (class, L28-L34)

> *Summary: Represents a configuration for an A2A push notification subscription, holding the target `url`, optional `token` and `authentication` details. It also includes an optional server-assigned `id`.*


### create_push_notification_config (function, L37-L49)

> *Summary: This asynchronous function registers a push-notification webhook for a given task ID using provided configuration objects. It takes the necessary inputs and returns the resulting `A2APushConfig` after interacting with the backend service via an SDK session.*


### get_push_notification_config (function, L52-L65)

> *Summary: Retrieves a stored push notification configuration by its ID using the provided application and task context. It interacts with an SDK session to fetch the data, which is then converted into the expected configuration object.*


### list_push_notification_configs (function, L68-L84)

> *Summary: Retrieves a paginated list of push notification configurations associated with a specific task ID, using provided optional parameters like tenant, page size, or token. It takes an `A2AConfig` and `task_id` as input and returns a list of `A2APushConfig` objects.*


### delete_push_notification_config (function, L87-L99)

> *Summary: This asynchronous function removes a registered push-notification configuration from the system. It takes an `A2AConfig`, a `task_id`, and a specific `config_id` as input to execute the deletion via the configured SDK session.*


### _to_proto (function, L102-L119)

> *Summary: Converts configuration objects into a `TaskPushNotificationConfig` proto message. It takes an A2A configuration, optional tenant override, task ID, and push settings to construct the final notification structure.*


### _from_proto (function, L122-L134)

> *Summary: Converts a `TaskPushNotificationConfig` protocol buffer message into an `A2APushConfig` object. It extracts the URL, token, ID, and optionally constructs authentication details from the input proto.*

