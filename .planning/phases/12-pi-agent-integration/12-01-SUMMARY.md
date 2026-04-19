---
phase: 12
plan: 01
status: complete
started: "2026-04-19T12:45:00Z"
completed: "2026-04-19T12:50:00Z"
---

# Plan 01: Provider Preset System - Summary

## Objective
Expand `--summarize-provider` to accept named presets (ollama, lmstudio, llamacpp, vllm, aphrodite) that auto-fill `base_url` and `model` defaults. Add custom provider overrides via `.glma.toml` `[summarize.providers]` section.

## What Was Built

### PROVIDER_PRESETS dict (models.py)
- 7 named presets: local, pi, ollama, lmstudio, llamacpp, vllm, aphrodite
- Each maps to `{base_url, model}` defaults
- `SummarizeProvider` enum kept at `LOCAL`/`PI` for backward compat; preset names resolved to `local` by config layer

### Preset Resolution (config.py)
- `load_summarize_config()` resolves preset names before Pydantic validation
- Custom providers from `[summarize.providers]` in `.glma.toml` override built-in presets
- Resolution priority: preset fills defaults → explicit CLI flags override

### New SummarizeConfig Fields
- `model_hint: str` — for pi extension (fast/capable/exact ID)
- `custom_providers: dict` — user-defined presets from config

### CLI Updates
- `--summarize-provider` help text lists all preset names
- `--ai-url` flag added for overriding API base URL

### PiProvider Removal
- `PiProvider` class removed from `providers.py` (was broken stub using non-existent `from pi import Agent`)
- Real integration is the TypeScript extension in Plan 02
- `__init__.py` and `cli.py` updated to remove all PiProvider references

## Key Files
- `02-worktrees/glma/src/glma/models.py` — PROVIDER_PRESETS, model_hint, custom_providers
- `02-worktrees/glma/src/glma/config.py` — preset resolution logic
- `02-worktrees/glma/src/glma/cli.py` — --ai-url flag, updated help text, PiProvider removed
- `02-worktrees/glma/src/glma/summarize/providers.py` — PiProvider removed
- `02-worktrees/glma/src/glma/summarize/__init__.py` — imports updated
- `02-worktrees/glma/tests/test_config.py` — 7 new preset tests
- `02-worktrees/glma/tests/test_providers.py` — PiProvider tests replaced with removal verification

## Tests
- 314 total (274 existing + 40 new across this phase; no tests deleted, only updated)
- All pass

## Self-Check: PASSED
