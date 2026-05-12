---
plan: 18-05
status: complete
started: "2026-05-12T19:20:00Z"
completed: "2026-05-12T19:25:00Z"
---

# SUMMARY: Plan 18-05 — CLI Integration, Language Filtering & End-to-End Tests

## What was built
Updated CLI help text, added language validation tests, walker discovery tests for all new languages, and fixed integration tests for the .h → CPP mapping change.

## Key Changes
- Updated --lang help text to list all 6 supported languages
- Added language validation tests (cpp, typescript, tsx, rust, invalid)
- Added walker tests for new language file discovery (7 tests)
- Verified .h not discovered with C-only, discovered with CPP
- Verified default config excludes new languages (no behavior change)
- Fixed integration tests for .h → CPP change (3 files vs 4)
- Added pytest import to test_cli.py

## Tests
- All 459 tests passing (was 447 before, +12 new tests)

## key-files.modified
- src/glma/cli.py
- tests/test_cli.py
- tests/test_walker.py
- tests/integration/test_full_index.py
