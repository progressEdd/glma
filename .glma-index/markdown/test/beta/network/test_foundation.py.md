# test/beta/network/test_foundation.py

6 function(s): _agent, test_unknown_sender_raises_not_found, test_hydrate_reloads_identities_from_disk, test_outbound_access_denied, test_unregister_makes_send_fail, test_set_resume_updates_index.

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| _agent | function |  |
| test_unknown_sender_raises_not_found | function |  |
| test_hydrate_reloads_identities_from_disk | function |  |
| test_outbound_access_denied | function |  |
| test_unregister_makes_send_fail | function |  |
| test_set_resume_updates_index | function |  |

## Chunks

### _agent (function, L34-L35)

> *Summary: Creates and returns a new `Agent` instance configured to use the "claude-sonnet-4-6" model from Anthropic. It accepts a string name for initialization.*


### test_unknown_sender_raises_not_found (function, L43-L58)

> *Summary: This test verifies that attempting to post an envelope from an unregistered sender ID results in a `NotFoundError`. It initializes a knowledge store and hub, then asserts that calling `hub.post_envelope` with an unknown sender will raise the expected exception.*


### test_hydrate_reloads_identities_from_disk (function, L62-L114)

> *Summary: This test verifies that agent identities and associated data persist correctly when the central hub is closed and reopened using a disk-backed store. It registers two agents, closes the initial hub instance, then reopens it to confirm that retrieved agents retain their original IDs and that stored attributes like resumes and skills are accurately loaded from disk.*


### test_outbound_access_denied (function, L118-L144)

> *Summary: This test verifies that an agent configured with an outbound access block will fail when attempting to send a message to a restricted recipient. It sets up a communication environment, registers two agents (one with the restriction), and asserts that sending an envelope from the restricted agent raises an `AccessDeniedError`.*


### test_unregister_makes_send_fail (function, L148-L183)

> *Summary: This test verifies that an agent becomes inert after unregistering from the system. It confirms that attempting to send a message using the unregistered agent results in a `RuntimeError`, and subsequently, the central hub can no longer locate or list the agent's ID.*


### test_set_resume_updates_index (function, L187-L207)

> *Summary: This test verifies that updating an agent's resume via `set_resume` correctly updates the cached state within a knowledge store and makes the new information discoverable through capability queries. It confirms both listing agents by a specific capability and retrieving the updated resume content.*

