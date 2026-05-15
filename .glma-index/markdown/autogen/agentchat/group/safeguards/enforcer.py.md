# autogen/agentchat/group/safeguards/enforcer.py

1 class(es): SafeguardEnforcer. 22 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| SafeguardEnforcer | class |  |

## Chunks

### SafeguardEnforcer (class, L22-L1158)

> *Summary: This class enforces security and policy rules across agent interactions, tool usage, and LLM communications. It initializes by loading a defined policy, parsing various inter-agent and environment safeguards (LLM or regex), and then provides hooks to intercept and modify content based on these rules when methods like `check_and_act` are called.*


### _stringify_content (method, L26-L32, parent: SafeguardEnforcer)

> *Summary: Converts various input types into a string representation. It attempts to use `content_str` for strings and lists, falling back to the standard `str()` conversion or returning an empty string if the input is `None`.*


### __init__ (method, L34-L86, parent: SafeguardEnforcer)

> *Summary: This constructor initializes a safeguard enforcer by loading a specified policy, configuring LLMs for safeguarding and masking, and optionally linking to a group chat manager and agents. It then validates the policy, creates a dedicated content masking agent if configured, parses inter-agent and environment rules, and emits a load event detailing the loaded rules.*


### _send_safeguard_event (method, L88-L109, parent: SafeguardEnforcer)

> *Summary: This method constructs a `SafeguardEvent` using provided details like event type, message, and agent identifiers. It then transmits this structured event to the default `IOStream`.*


### _load_policy (method, L111-L117, parent: SafeguardEnforcer)

> *Summary: Reads a policy either by loading it from a file path (string input) or directly accepting it as a dictionary. It returns the loaded or provided policy structure as a dictionary.*


### _validate_policy (method, L119-L124, parent: SafeguardEnforcer)

> *Summary: This method ensures the integrity of a stored policy by instantiating a `SafeguardValidator` with the policy data and then calling its structure validation routine. It takes no external inputs but performs an internal check on the object's state, raising errors if the policy format is invalid.*


### _parse_inter_agent_rules (method, L126-L212, parent: SafeguardEnforcer)

> *Summary: Parses configuration from the policy to generate a list of inter-agent safeguard rules. It processes agent transition rules, creating either LLM or Regex guardrails based on specified conditions and then includes a separate groupchat message check rule if present in the input policy.*


### _parse_environment_rules (method, L214-L371, parent: SafeguardEnforcer)

> *Summary: Parses safeguard configurations from a policy object into a standardized list of rule dictionaries. It processes three types of rules—tool, LLM, and user interactions—validating required fields like `message_source`, `message_destination`, and the specific checking mechanism (`llm` or `regex`). The output is a list containing structured rule objects ready for enforcement.*


### create_agent_hooks (method, L373-L496, parent: SafeguardEnforcer)

> *Summary: Generates a dictionary of specialized hook functions for a given agent based on defined environment rules. It checks for and creates hooks for tool interactions, LLM communications, user inputs, and inter-agent message sending, applying safeguards only if relevant rules exist for the specified agent.*


### _check_llm_violation (method, L498-L535, parent: SafeguardEnforcer)

> *Summary: This method validates input content against predefined safety rules using an LLM guardrail. It accepts the content string and optional lists of disallowed items or a custom prompt to define the violation condition, returning a boolean indicating activation and a justification message.*


### _check_regex_violation (method, L537-L545, parent: SafeguardEnforcer)

> *Summary: This method determines if a given string contains a match for a specified regular expression pattern. It returns a boolean indicating the match status along with a descriptive message detailing whether a violation occurred or not.*


### _apply_action (method, L547-L598, parent: SafeguardEnforcer)

> *Summary: This method processes a specified action ("block," "mask," or "warning") against provided content based on an explanation and disallow items. It emits corresponding safeguard events before either returning the original content, handling it as blocked/masked, or passing through the warning.*


### _mask_content (method, L600-L634, parent: SafeguardEnforcer)

> *Summary: This method sanitizes input text by attempting to mask sensitive information using a provided regex pattern first. If no pattern is given, it optionally uses an LLM agent with a specific prompt to replace disallowed content categories before returning the resulting string.*


### _handle_blocked_content (method, L636-L696, parent: SafeguardEnforcer)

> *Summary: This method sanitizes input content by replacing sensitive information with a standardized block message. It accepts content as a string, dictionary, or list and returns the modified structure, ensuring that blocked data is appropriately flagged within messages, tool calls, or responses based on the input type.*


### _handle_masked_content (method, L698-L775, parent: SafeguardEnforcer)

> *Summary: This method recursively applies a masking function to sensitive data within structured inputs. It processes `str`, `dict`, or `list` inputs, specifically targeting and masking content in fields like `"content"`, `"tool_responses"`, `"tool_calls"` arguments, and list items accordingly.*


### _check_inter_agent_communication (method, L777-L935, parent: SafeguardEnforcer)

> *Summary: This method validates communication between two agents by inspecting the message content, which can be a string or a dictionary containing tool calls/responses. It iterates through defined rules, applying checks via integrated guardrails (LLM or Regex) to determine if the message violates any safety policies, returning an action result if a violation occurs.*


### _check_interaction (method, L937-L998, parent: SafeguardEnforcer)

> *Summary: This method enforces safety rules by iterating through configured environmental rules based on the interaction type and participating agents. It checks the provided content against defined criteria (regex or LLM), sends corresponding events, and returns an actioned result if a violation is detected, otherwise returning `None`.*


### _perform_check (method, L1000-L1025, parent: SafeguardEnforcer)

> *Summary: Executes a content validation against a specified rule by dispatching to either an LLM-based or regex-based checking mechanism. It accepts the rule configuration, the content string, and the method type, returning a boolean indicating compliance along with a status message.*


### _check_tool_interaction (method, L1027-L1063, parent: SafeguardEnforcer)

> *Summary: This method validates interactions involving tools by extracting the relevant tool name and determining the source/destination agents based on the interaction direction ("input" or "output"). It then passes this structured information to a core checking mechanism, returning either the validation result or the original input data.*


### _check_llm_interaction (method, L1065-L1086, parent: SafeguardEnforcer)

> *Summary: This method validates interactions involving an LLM by wrapping the provided data and direction. It determines whether the agent or the LLM is the source/destination before calling a core checking function, returning the validation result or the original data if no issues are found.*


### _check_user_interaction (method, L1088-L1101, parent: SafeguardEnforcer)

> *Summary: This method validates a user's input directed at a specific agent by calling an internal check function. It returns any enforcement message from the check if present; otherwise, it passes the original user input through unchanged.*


### check_and_act (method, L1103-L1134, parent: SafeguardEnforcer)

> *Summary: This method intercepts messages exchanged between agents to enforce group chat safeguards. It checks the incoming content against defined rules and returns a modified message if a violation is detected, otherwise it returns `None`.*


### _resolve_tool_executor_source (method, L1136-L1158, parent: SafeguardEnforcer)

> *Summary: When the source agent is identified as a group tool executor, this method determines the true originating agent by querying the `GroupToolExecutor` instance. It returns the originator's name if available, otherwise it defaults to `"tool_executor"`.*

