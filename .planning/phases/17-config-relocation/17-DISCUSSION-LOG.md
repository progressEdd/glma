# Phase 17: Config Relocation - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-05-12
**Phase:** 17-config-relocation
**Areas discussed:** Migration behavior, `--config` flag interaction

---

## Migration Behavior

| Option | Description | Selected |
| ---------- | --------------------------------------- | -------- |
| A) Auto-move silently | Move `.glma.toml` into `.glma-index/` with no output | |
| B) Auto-move with notice | Move it and print `[moved] .glma.toml → .glma-index/.glma.toml` | ✓ |
| C) Warn and stop | Print deprecation warning, require manual move, then exit | |

**User's choice:** B — Auto-move with notice
**Notes:** Config file isn't source code, so auto-moving is fine. The notice keeps it transparent.

---

## `--config` Flag Interaction

| Option | Description | Selected |
| ---------- | --------------------------------------- | -------- |
| A) Skip check entirely | If `--config` provided, don't look at root-level config at all | ✓ |
| B) Still warn | Even with `--config`, warn about root-level config if it exists | |

**User's choice:** A — Skip check entirely
**Notes:** `--config` is an explicit override. Root-level config isn't relevant to that run.

---

## Agent's Discretion

- Exact warning message wording
- Whether to log migration or just print to console
- Edge case handling (`.glma-index/` doesn't exist yet)
- Whether `glma init` creates config in new location

## Deferred Ideas

None — discussion stayed within phase scope.
