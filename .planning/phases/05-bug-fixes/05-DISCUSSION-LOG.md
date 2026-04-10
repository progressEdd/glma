# Phase 5: Bug Fixes - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-04-10
**Phase:** 5-bug-fixes
**Areas discussed:** Export flag naming, Summary function sharing

---

## Export Flag Naming

| Option | Description | Selected |
| ------ | ----------- | -------- |
| `--include-code` | Positive opt-in flag, matches new default direction | ✓ |
| Both `--include-code` and `--no-code` | Backward compat, more flags to document | |
| Keep `--no-code` only | Double negative, confusing | |

**User's choice:** `--include-code` — clean positive opt-in
**Notes:** Old `--no-code` removed. No backward compat concern (v1.0 users are the developer only).

---

## Summary Function Sharing

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Move to shared module (`glma/summaries.py`) | Clean separation, both export.py and writer.py import from there | ✓ |
| Import from export.py in writer.py | Works but couples writer → export (backwards dependency) | |
| Duplicate in writer.py | Two copies to maintain | |

**User's choice:** Move to shared module
**Notes:** Avoids coupling where writer (core) depends on export (consumer).

---

## the agent's Discretion

- Exact shared module name
- Comprehension truncation root cause diagnosis approach
- Whether to keep `--no-code` as hidden alias
- Test case specifics

## Deferred Ideas

None — discussion stayed within phase scope.
