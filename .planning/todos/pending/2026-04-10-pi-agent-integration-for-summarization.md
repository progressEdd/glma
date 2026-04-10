---
created: 2026-04-10T00:00:00Z
title: Pi/agent integration for code summarization
area: api
files:
  - 02-worktrees/glma/src/glma/export.py:68
  - 02-worktrees/glma/src/glma/cli.py:276
  - 02-worktrees/glma/src/glma/models.py:106
---

## Problem

Currently AI summarization requires a running local LLM (LM Studio, Ollama, etc.) with an OpenAI-compatible endpoint. This means:
- User must have a separate model server running
- API keys duplicated between pi and glma config
- Can't leverage the coding agent (pi) that's already running and already has model access
- No way to use cloud models (Claude, GPT, etc.) for summaries without a separate endpoint

Pi (or any coding agent) already has an LLM connection and understands code context. It could generate summaries during or after indexing without requiring a separate model server.

## Solution

### Model ownership: pi owns the model, GLMA hints preferences

Pi manages all model config (API keys, providers, endpoints) via `auth.json` / `models.json` / custom providers.
GLMA only specifies a `model_hint` — the extension resolves it to an actual model via pi's registry.

Works with **any model** pi can access:
- Cloud: Claude, GPT, Gemini (keys in pi's auth.json)
- Local: Ollama, LM Studio, llama.cpp (registered as pi custom providers in models.json)
- The user's current pi model works out of the box

### GLMA config (glma.yaml)

```yaml
summary:
  mode: agent          # agent | local | rule
  model_hint: fast     # fast | capable | <exact model id> | (empty = use pi's current model)
```

No API keys or base_url needed — pi owns those.

### Pi extension (~/.pi/agent/extensions/glma-summarize.ts)

1. Register a `glma_summarize` tool callable by the LLM:
   - Reads chunks needing summaries from glma DB
   - Resolves `model_hint` to actual model via pi's ModelRegistry:
     - `fast` → cheapest/fastest available model (flash, haiku)
     - `capable` → stronger model (sonnet, gpt-4o)
     - exact model ID → use that model
     - empty → pi's currently active model
   - Temporarily switches model with `pi.setModel()`, restores when done
   - Agent loops: tool returns batch of chunks → agent summarizes each → tool writes summaries back to glma DB
   - State tracked via `pi.appendEntry()` for crash recovery / resume
2. Local models (Ollama, LM Studio, etc.) registered once in pi's models.json — extension uses them like any other model
3. API keys only in one place: pi's auth.json

### Standalone mode (no pi): glma owns the model endpoint

When pi isn't running, glma talks to a local LLM directly via OpenAI-compatible API.
Currently only has `--ai-url` and `--ai-model` as raw flags. Should add **named provider presets**
so users don't have to remember ports and paths.

#### Preset defaults for common local servers

| Provider | Default URL | Default Model | Notes |
| -------- | ----------- | ------------- | ----- |
| `lmstudio` | `http://localhost:1234/v1` | loaded model | Current default, LM Studio OpenAI compat server |
| `ollama` | `http://localhost:11434/v1` | `llama3` | Ollama's OpenAI compat endpoint (requires `OLLAMA_HOST` or default) |
| `llamacpp` | `http://localhost:8080/v1` | `default` | llama.cpp server `--port 8080` with OpenAI compat |
| `vllm` | `http://localhost:8000/v1` | loaded model | vLLM's OpenAI-compatible server |
| `aphrodite` | `http://localhost:7860/v1` | loaded model | Aphrodite Engine OpenAI compat |

#### CLI usage (proposed)

```bash
# Easiest: just name the provider, glma knows the defaults
 glma export --ai-summaries --ai-provider ollama
 glma export --ai-summaries --ai-provider lmstudio
 glma export --ai-summaries --ai-provider llamacpp --ai-model my-model

# Override URL if non-default port
 glma export --ai-summaries --ai-provider ollama --ai-url http://localhost:11435/v1

# Raw: specify everything manually (backward compat)
 glma export --ai-summaries --ai-url http://localhost:1234/v1 --ai-model llama3

# Shortcut: --ai-summaries alone defaults to lmstudio (current behavior)
 glma export --ai-summaries
```

#### Implementation in models.py

```python
class AIProvider(str, Enum):
    lmstudio = "lmstudio"
    ollama = "ollama"
    llamacpp = "llamacpp"
    vllm = "vllm"
    aphrodite = "aphrodite"
    custom = "custom"

PROVIDER_DEFAULTS = {
    AIProvider.lmstudio: {"base_url": "http://localhost:1234/v1", "model": "default"},
    AIProvider.ollama:   {"base_url": "http://localhost:11434/v1", "model": "llama3"},
    AIProvider.llamacpp: {"base_url": "http://localhost:8080/v1", "model": "default"},
    AIProvider.vllm:     {"base_url": "http://localhost:8000/v1", "model": "default"},
    AIProvider.aphrodite:{"base_url": "http://localhost:7860/v1", "model": "default"},
}
```

### Full fallback chain for `glma export`

```
pi extension running?  → use pi's model (respects model_hint from glma.yaml)
  ↓ no
--ai-summaries flag?   → use local LLM endpoint
  ├── --ai-provider <name>?  → use preset defaults for that provider
  ├── --ai-url given?        → use that URL directly
  └── neither?               → default to lmstudio (localhost:1234/v1)
  ↓ no
rule-based summary     → no model needed (current default)
```

### Alternative: SDK headless session

- Use `createAgentSession()` with `SessionManager.inMemory()` for background summarization without TUI
- Could be triggered from glma CLI as `glma export --summarize-via agent`
- Same model ownership model — uses pi's auth + registry
