---
plan: 18-01
status: complete
started: "2026-05-12T19:00:00Z"
completed: "2026-05-12T19:10:00Z"
---

# SUMMARY: Plan 18-01 — Language Foundation

## What was built
Added C++, TypeScript, TSX, and Rust as supported languages with full tree-sitter parsing, detection, and chunk extraction. Foundation for relationship extraction in Plans 02-04.

## Key Changes
- Added CPP, TYPESCRIPT, TSX, RUST to Language enum
- Added tree-sitter-cpp, tree-sitter-typescript, tree-sitter-rust to pyproject.toml
- Updated EXTENSION_MAP with .cpp/.hpp/.cc/.hxx/.ts/.tsx/.rs extensions
- Changed .h mapping from C to CPP (C++ grammar is a superset of C)
- Added LanguageConfig entries for all 4 new languages in parser.py
- Added name extraction logic for C++, TypeScript, Rust in chunks.py
- Updated walker.py supported_extensions with new languages
- Generalized container_type recursion in _walk_chunks (fixes namespace nesting)
- Created fixture files: sample.cpp, sample.ts, sample.tsx, sample.rs
- Added detector, parser, and chunk tests for all new languages

## Tests
- All 429 tests passing (was 398 before, +31 new tests)

## Key Decisions
- `.h` maps to CPP not C — C++ grammar is a superset
- Default IndexConfig.languages stays [C, PYTHON] — new languages opt-in only
- Container types now recurse universally (not Python-only)

## key-files.modified
- src/glma/models.py
- src/glma/index/detector.py
- src/glma/index/parser.py
- src/glma/index/chunks.py
- src/glma/index/walker.py
- pyproject.toml
- tests/test_detector.py
- tests/test_parser.py
- tests/test_chunks.py
- tests/test_config.py
- tests/fixtures/sample.cpp
- tests/fixtures/sample.ts
- tests/fixtures/sample.tsx
- tests/fixtures/sample.rs

## key-files.created
- tests/fixtures/sample.cpp
- tests/fixtures/sample.ts
- tests/fixtures/sample.tsx
- tests/fixtures/sample.rs
