# Phase 12: Pi Agent Integration - Research

**Gathered:** 2026-04-14
**Status:** Complete

## Research Question

"What do I need to know to PLAN this phase well?"

---

## 1. Pi Extension API — What's Available

### Extension Entry Point
- TypeScript file exporting a default function receiving `ExtensionAPI`
- Auto-discovered from `.pi/extensions/*.ts` (project-local) or `~/.pi/agent/extensions/*.ts` (global)
- Loaded via jiti (no compilation step needed)

### Key Imports
```typescript
import type { ExtensionAPI, ExtensionCommandContext } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";           // or "@mariozechner/pi-ai" (re-export)
import { complete, getModel } from "@mariozechner/pi-ai";
```

### Tool Registration Pattern
```typescript
pi.registerTool({
  name: "glma_summarize",
  label: "Glma Summarize",
  description: "...",
  parameters: Type.Object({ ... }),
  async execute(toolCallId, params, signal, onUpdate, ctx) {
    return {
      content: [{ type: "text", text: "..." }],
      details: {},
    };
  },
});
```

### Command Registration Pattern
```typescript
pi.registerCommand("glma-summarize", {
  description: "Summarize codebase chunks using AI",
  handler: async (args, ctx) => {
    ctx.ui.notify("Starting summarization...", "info");
    // ...
  },
});
```

### Model Access & Invocation (Cloud Models)
```typescript
// Get a specific model
const model = getModel("openai", "gpt-5.2");

// Get API key and auth headers from pi's registry
const auth = await ctx.modelRegistry.getApiKeyAndHeaders(model);
// auth.ok, auth.apiKey, auth.headers

// Call the model
const response = await complete(model, { messages: [...] }, {
  apiKey: auth.apiKey,
  headers: auth.headers,
});
```

### ctx.modelRegistry API
- `ctx.model` — currently active model in pi
- `ctx.modelRegistry.find(provider, id)` — find a specific model
- `ctx.modelRegistry.getApiKeyAndHeaders(model)` — get auth for a model
- `ctx.modelRegistry.getAvailable()` — all available models
- `ctx.modelRegistry.getApiKeyForProvider(provider)` — API key for a provider

### Model Type Structure
```typescript
interface Model<TApi> {
  id: string;
  name: string;
  api: TApi;
  provider: Provider;    // e.g., "anthropic", "openai", "ollama"
  baseUrl: string;
  reasoning: boolean;
  input: ("text" | "image")[];
  cost: { input: number; output: number; cacheRead: number; cacheWrite: number; };
  contextWindow: number;
  maxTokens: number;
}
```

### UI Methods Available
- `ctx.ui.notify(message, type)` — toast notification ("info" | "success" | "warning" | "error")
- `ctx.ui.confirm(title, message)` → boolean
- `ctx.ui.select(title, options)` → selection
- `ctx.ui.custom(...)` — full custom TUI component
- `ctx.hasUI` — false in print/JSON mode

### Key Constraints
- Tool `execute()` receives `ExtensionContext` (no session control)
- Command `handler()` receives `ExtensionCommandContext` (can call `ctx.waitForIdle()`, `ctx.newSession()`)
- To make a tool trigger a command: tool returns a message telling agent to run the command, or use `ctx.sendUserMessage()` pattern
- Per CONTEXT.md D-01: tool is a thin trigger, command does the real work

---

## 2. Glma Summarization Pipeline — Current State

### Entry Points
1. **CLI:** `glma index --summarize --summarize-provider local --summarize-model llama3`
2. **Programmatic:** `summarize_chunks(store, chunks, provider, max_chunk_chars=3000)`

### Provider Protocol
```python
class SummarizerProvider(Protocol):
    def summarize(self, code: str, context: str) -> str: ...
```

### Current Providers
- `OpenAICompatibleProvider(base_url, model)` — works with any OpenAI-compatible endpoint
- `PiProvider(model)` — **stub**, uses `from pi import Agent` which doesn't match pi's actual extension API

### Config Loading
- `load_summarize_config(repo_root, cli_overrides)` → `SummarizeConfig`
- `SummarizeConfig` fields: `enabled`, `provider` (SummarizeProvider enum: LOCAL/PI), `model`, `base_url`, `max_chunk_chars`
- `SummarizeProvider` enum currently has only `LOCAL` and `PI`

### DB Access (LadybugStore)
- `store.get_indexed_files()` → dict of file_path → content_hash
- `store.get_chunks_for_file(file_path)` → list of Chunk
- `store.update_chunk_summary(chunk_id, summary)` — persists to DB
- `store.update_file_summary(file_path, summary)` — persists file-level summary
- DB path convention: `{repo_root}/{output_dir}/db/index.lbug` (default: `.glma-index/db/index.lbug`)

### Pipeline Features (from Phase 10)
- Incremental: skips chunks with existing summaries
- Decomposition: class chunks via method children; standalone via map-reduce
- Error handling: context-length errors trigger decomposition, other errors logged and skipped

---

## 3. Integration Architecture — How It Fits Together

### Two Code Paths (per CONTEXT.md D-02)

**Cloud Models (Claude, GPT, Gemini):**
1. Extension reads chunks from glma DB
2. Extension calls `complete()` with resolved model + API key from pi's registry
3. Extension writes summaries back to DB directly

Challenge: Extension is TypeScript, DB is Ladybug (Rust/kuzu). Extension can't directly access Ladybug.

**Solution: Shell out to `glma` CLI for ALL paths.** The extension's command resolves the model and auth, then invokes:
```bash
glma index --summarize --summarize-provider local --summarize-model <model> --ai-url <url>
```
For cloud models, we need to either:
- (a) Pass API key via env var to the CLI subprocess
- (b) Have the extension call `complete()` directly and write summaries via a separate helper

**Per CONTEXT.md discussion log:** User chose to shell out to glma CLI. For cloud models, the extension could set an env var with the API key and pass base_url pointing to the cloud provider.

**However**, there's a simpler approach aligned with D-02:
- For cloud models: Extension calls `complete()` directly, then writes summaries to DB via a small helper script or CLI subcommand
- For local models: Extension shells out to `glma index --summarize` with preset flags

**Simplest viable approach:** The extension always shells out to `glma index --summarize`. For cloud models, it resolves the model's base_url and API key from pi's registry and passes them as `--ai-url` and env var `OPENAI_API_KEY`. This works because:
- All providers (Anthropic, OpenAI, Google) expose OpenAI-compatible proxy endpoints, OR
- The extension could use a local proxy pattern

**Actually, the cleanest approach:**
1. Extension resolves model hint → actual model + auth from pi's registry
2. For ANY model: extension calls `complete()` directly in TypeScript (bypasses Python entirely)
3. For reading/writing chunks: extension shells out to a minimal `glma` helper to read unsent chunks and write summaries back

Wait — but `complete()` returns summaries, and we need to write them to Ladybug DB. The extension can't write to Ladybug directly.

**Resolution:** Add a new `glma summarize-chunks` CLI subcommand (or flags to existing commands) that:
- Reads chunks needing summaries from DB (already exists in pipeline)
- Accepts summaries via stdin/file (for write-back from extension)
- OR the simpler path: just use `glma index --summarize` for local models (reuses full pipeline), and for cloud models via pi extension, use a lightweight approach

**Final architecture decision for planning:**

The pi extension command (`/glma-summarize`) works as follows:
1. Resolves model_hint → model + API key from pi's registry
2. Reads chunks needing summaries by shelling out to `glma query --format json` or a new helper
3. For each unsent chunk: calls `complete()` with the chunk, gets summary
4. Writes summaries back by shelling out to `glma` with a write-summary subcommand

OR simpler: The extension just invokes `glma index --summarize` with the right flags, passing API credentials via env vars. The Python pipeline handles everything. This keeps the TypeScript extension as a thin bridge.

---

## 4. Provider Preset System — Design

### Current State
`--summarize-provider` accepts `local` or `pi` (SummarizeProvider enum). `local` defaults to `http://localhost:1234/v1`.

### Required Changes
1. Expand `SummarizeProvider` enum (or replace with string-based resolution) to accept: `local`, `pi`, `ollama`, `lmstudio`, `llamacpp`, `vllm`, `aphrodite`
2. Add preset → (base_url, default_model) mapping
3. Add `[summarize.providers]` section to `.glma.toml` for custom presets
4. Resolution: `--summarize-provider ollama` → fills `base_url=http://localhost:11434/v1` + `model=llama3`, then `--summarize-model` and `--ai-url` can override

### Preset Map
| Preset | base_url | default model |
|--------|----------|---------------|
| local | http://localhost:1234/v1 | default |
| ollama | http://localhost:11434/v1 | llama3 |
| lmstudio | http://localhost:1234/v1 | default |
| llamacpp | http://localhost:8080/v1 | default |
| vllm | http://localhost:8000/v1 | default |
| aphrodite | http://localhost:7860/v1 | default |

### Implementation Approach
- Create `PROVIDER_PRESETS` dict in `models.py` or new `presets.py`
- Modify `load_summarize_config()` to resolve preset names before Pydantic validation
- Keep `SummarizeProvider` as enum for backward compat, add preset resolution layer

---

## 5. model_hint Resolution — Design

### From CONTEXT.md (D-05, D-06, D-07)
- `model_hint` lives in `.glma.toml` `[summarize]` section
- Resolved by pi extension using pi's model registry
- Values: `fast` → cheapest/fastest, `capable` → strongest, exact ID → use that, empty → pi's active model
- Heuristic uses built-in preference order of known model families

### Heuristic Approach
```typescript
const FAST_FAMILIES = ["haiku", "flash", "mini", "nano", "turbo"];
const CAPABLE_FAMILIES = ["opus", "sonnet", "gpt-4", "gpt-5", "ultra", "pro"];

function resolveModelHint(hint: string, registry: ModelRegistry, currentModel: Model): Model | null {
  if (!hint || hint === "") return currentModel;
  
  const allModels = registry.getAvailable();
  
  if (hint === "fast") {
    // Find models matching fast families
    const fast = allModels.filter(m => FAST_FAMILIES.some(f => m.id.toLowerCase().includes(f)));
    if (fast.length) return fast.sort(byCost)[0]; // cheapest among fast
    // Fallback: cheapest overall
    return allModels.sort(byCost)[0];
  }
  
  if (hint === "capable") {
    const capable = allModels.filter(m => CAPABLE_FAMILIES.some(f => m.id.toLowerCase().includes(f)));
    if (capable.length) return capable.sort(byCostDesc)[0]; // most expensive among capable
    return allModels.sort(byCostDesc)[0]; // most expensive overall
  }
  
  // Exact model ID — search across all providers
  const exact = allModels.find(m => m.id === hint);
  return exact || null;
}
```

---

## 6. Python Changes Needed

### models.py
- Add `model_hint` field to `SummarizeConfig` (string, optional)
- Add `ProviderPreset` type or expand `SummarizeProvider` enum
- Add `PROVIDER_PRESETS` constant mapping preset names to (base_url, model)

### config.py
- Modify `load_summarize_config()` to resolve preset names
- Add loading of `[summarize.providers]` custom presets from `.glma.toml`

### cli.py
- Expand `--summarize-provider` help text to list preset names
- Add preset resolution before provider instantiation
- Add `--ai-url` flag as alias for overriding base_url (or reuse existing pattern)

### providers.py
- Keep `PiProvider` as-is (it's a stub, but removing it is a separate decision)
- OR: remove `PiProvider` since the real integration is the TypeScript extension
- `OpenAICompatibleProvider` already works with any base_url/model — presets just pre-fill these

### New: `.pi/extensions/glma-summarize.ts`
- The pi extension file
- Registers `/glma-summarize` command and `glma_summarize` tool
- Implements model_hint resolution
- Shells out to `glma` CLI for actual summarization work

---

## 7. Testing Strategy

### Python Tests (existing + new)
- Test preset resolution in `config.py` — each preset name maps to correct URL/model
- Test custom provider overrides in `.glma.toml` `[summarize.providers]`
- Test `SummarizeConfig` with preset names (backward compat with `local`/`pi`)
- Test CLI `--summarize-provider` accepts preset names
- All 274+ existing tests must pass

### TypeScript Extension Tests
- Manual testing: load extension in pi, run `/glma-summarize`
- model_hint resolution unit tests (fast, capable, exact ID, empty)
- Verify `complete()` call pattern works with pi's auth
- End-to-end: extension triggers summarization, summaries appear in DB

---

## 8. Key Risks & Open Questions

1. **Extension-to-DB bridge**: The TypeScript extension can't directly access Ladybug DB. Must shell out to `glma` CLI or add a new CLI subcommand for reading/writing summaries.

2. **Cloud model auth passthrough**: For the extension to use cloud models (Claude, GPT) via pi's auth and then write summaries to glma's DB, there needs to be a write path. Simplest: add `glma write-summary <chunk_id> <summary>` subcommand, or have the extension invoke the full pipeline with env-var-based credentials.

3. **Backward compatibility**: `SummarizeProvider` enum currently has `LOCAL` and `PI`. Adding preset names as enum values would break the enum. Better approach: keep enum for backward compat, add a string-based preset resolution layer before enum validation.

4. **PiProvider stub**: The Python `PiProvider` uses `from pi import Agent` which doesn't exist in pi's extension API. It should either be removed or repurposed. Per CONTEXT.md D-03: "Phase 12 replaces it with the real TypeScript extension."

5. **DB path discovery**: Extension needs to know where glma's DB is. Convention: `{cwd}/.glma-index/db/index.lbug`. Extension can use `ctx.cwd` to resolve this.

---

## RESEARCH COMPLETE

Key findings:
- Pi extension API is well-documented with clear patterns for tool/command registration and model access
- The `complete()` function from `@mariozechner/pi-ai` is the primary integration point for cloud model calls
- Extension can't directly access Ladybug DB — must shell out to glma CLI or add helper subcommands
- Provider presets are straightforward config changes in Python (expand enum + add preset map)
- model_hint resolution is a TypeScript-side concern using pi's `ctx.modelRegistry.getAvailable()`
- The Python `PiProvider` stub should be removed/replaced since the real integration is the TypeScript extension
