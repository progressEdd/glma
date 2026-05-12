# Phase 18: Extended Language Support - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md - this log preserves the alternatives considered.

**Date:** 2026-05-12
**Phase:** 18-extended-language-support
**Areas discussed:** C++ Chunk Mapping, TypeScript Constructs, Rust Constructs, Language Filtering & CLI, Relationship Extraction Depth, Testing Strategy

---

## C++ Chunk Type Mapping

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Conservative (match C pattern) | Only function/struct/enum/typedef. Skips C++-specific constructs. | |
| Full C++ coverage | Add class, namespace, template, constructor, destructor. Most useful for agents. | ✓ |
| Aggressive | Full + using aliases, lambdas, operator cast. Maximum detail, many tiny chunks. | |

**User's choice:** Full C++ coverage (recommended)
**Notes:** Matches the richness of C++ and provides maximum value for agent queries.

### .h extension handling

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Parse as C++ always | C++ grammar is superset of C. Simple, works for almost all cases. | ✓ |
| Heuristic-based | Check for C++ keywords in content, then pick grammar. More accurate but slower. | |
| User config required | User must specify .h handling. Clean but burdens user. | |

**User's choice:** Parse as C++ always
**Notes:** C++ grammar superset of C makes this the simple correct answer.

---

## TypeScript Constructs

### Interfaces and type aliases as chunks

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Yes, both | Interfaces and type aliases become chunks. Critical for TS codebases. | ✓ |
| No, only classes/functions | Skip interfaces and type aliases. Simpler but loses type info. | |
| Interfaces only | Type aliases can be trivial, but interfaces almost always meaningful. | |

**User's choice:** Yes, both (recommended)

### TSX handling

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Separate TSX grammar | .ts → TS grammar, .tsx → TSX grammar. Correct JSX parsing. | ✓ |
| Parse everything as TSX | TSX is superset of TS. Simpler but less precise. | |

**User's choice:** Separate TSX grammar (recommended)

### Enums and namespaces

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Enums as chunks, namespaces as containers only | Enums define named values; namespaces group definitions. Matches Python class pattern. | ✓ |
| Both as chunks | Namespaces become chunks too. May produce large unfocused chunks. | |
| Neither | Skip both. Loses enum values and namespace organization. | |

**User's choice:** Enums as chunks, namespaces as containers only (recommended)

---

## Rust Constructs

### impl block chunking depth

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Individual methods as chunks, impl as container | Method-level granularity. Matches Python class/method pattern. | ✓ |
| Whole impl as one chunk | Simpler but large chunks, can't query individual methods. | |
| Both impl AND individual methods | Most detail but some duplication. | |

**User's choice:** Individual methods as chunks, impl as container (recommended)

### Traits as chunks

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Yes, as class-type chunks | Frequently queried. Map trait → class chunk type. | ✓ |
| No, skip traits | Loses important abstraction layer information. | |

**User's choice:** Yes, as class-type chunks (recommended)

### mod declarations

| Option | Description | Selected |
| ------ | ----------- | -------- |
| As import/include relationships | mod and use are references, not definitions. Like C #include. | ✓ |
| As chunks | mod becomes a chunk. Doesn't match how mods work. | |

**User's choice:** As import/include relationships (recommended)

---

## Language Filtering & CLI

### C/C++ interaction in filtering

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Independent languages | --lang c indexes .c only, --lang cpp indexes C++ extensions. Explicit user control. | ✓ |
| C++ implies C | Selecting cpp auto-includes C extensions. Convenient but surprising. | |

**User's choice:** Independent languages (recommended)

### Unrecognized language errors

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Clear error with valid options | Fail immediately, list supported languages. | ✓ |
| Warning + skip | Print warning, continue with recognized languages. User might miss it. | |

**User's choice:** Fail immediately with clear error (recommended)

### Default language list

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Keep current default [c, python] | No behavior change. New languages opt-in. | ✓ |
| Expand to all supported | Indexes everything found. Changes existing behavior. | |

**User's choice:** Keep current default, new languages opt-in

---

## Relationship Extraction Depth

### C++ relationships

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Core: #include, using, calls, inheritance | Matches C extraction depth. Covers most common queries. | ✓ |
| Extended: core + template instantiation, namespace resolution | More complete but significantly more complex. | |

**User's choice:** Core set (recommended)

### TypeScript relationships

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Core: import/export, calls, extends, implements | Most common agent queries. | ✓ |
| Extended: core + type alias resolution, decorator relationships | More complete but type aliases can be deeply chained. | |

**User's choice:** Core set

### Rust relationships

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Core: use, calls, impl...for..., mod | Covers main code navigation paths. | ✓ |
| Extended: core + trait bound resolution, macro expansion | Trait bounds useful but macro handling complex. | |

**User's choice:** Core set (recommended)

---

## Testing Strategy

### Test approach

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Synthetic fixtures per language | Small hand-crafted files. Deterministic, fast, matches existing pattern. | ✓ |
| Real open-source snippets | More realistic but harder to maintain. | |
| Both | Most thorough but doubles maintenance. | |

**User's choice:** Synthetic fixtures per language (recommended)

### Minimum viable coverage

| Option | Description | Selected |
| ------ | ----------- | -------- |
| Chunks + comments + relationships per language | Covers all three language-sensitive pipeline stages. 12 new tests minimum. | ✓ |
| Just chunk extraction | Minimal. Verify files parse and produce chunks only. | |

**User's choice:** Full per-language coverage (recommended)

---

## Agent's Discretion

- Exact file extensions for each language (`.cxx`, `.c++`, `.mjs`, etc.)
- Language enum naming convention (CPP vs C_PLUS_PLUS, TYPESCRIPT vs TS, etc.)
- Whether to refactor relationship extraction to data-driven approach vs mirror existing per-language functions
- Whether to consolidate comment attachment config vs keep language-specific functions
- Resolution of D-02/D-03 tension (.h detected as C++ but user may only select `--lang c`)

## Deferred Ideas

None — discussion stayed within phase scope.
