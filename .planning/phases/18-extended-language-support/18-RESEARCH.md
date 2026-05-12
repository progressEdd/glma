# Phase 18: Extended Language Support - Research

**Researched:** 2026-05-12
**Status:** Complete

## Research Question

"What do I need to know to PLAN this phase well?"

---

## 1. Current Architecture Summary

The language support pipeline has clear extension points:

### Files that need changes

| File | Role | Change Type |
|------|------|-------------|
| `src/glma/models.py` | `Language` enum (C, PYTHON) | Add CPP, TYPESCRIPT, TSX, RUST |
| `src/glma/index/detector.py` | `EXTENSION_MAP` dict | Add `.cpp/.hpp/.cc/.hxx/.h→CPP`, `.ts→TYPESCRIPT`, `.tsx→TSX`, `.rs→RUST` |
| `src/glma/index/parser.py` | `LanguageConfig` + `PARSER_CONFIGS` + `_build_parsers()` | Add 4 new configs with grammar imports |
| `src/glma/index/relationships.py` | `extract_relationships()` dispatcher + per-language extractors | Add 4 new branches + ~12 new functions |
| `src/glma/index/comments.py` | `COMMENT_TYPES` + docstring extractors | Add TS JSDoc + Rust `///`/`//!` extraction |
| `src/glma/index/walker.py` | `supported_extensions` default dict | Add new extensions |
| `src/glma/cli.py` | `--lang` help text | Update to list all supported languages |
| `src/glma/config.py` | Config loading (already works via Language enum) | No functional change needed |
| `pyproject.toml` | Dependencies | Add 3 tree-sitter grammar packages |
| `src/glma/index/chunks.py` | `_extract_node_name()` | Add name extraction for CPP/TS/Rust |

### Files that need NO changes

| File | Reason |
|------|--------|
| `src/glma/index/pipeline.py` | Language-generic — dispatches by Language enum already |
| `src/glma/index/writer.py` | Language-generic |
| `src/glma/index/progress.py` | Language-generic |
| `src/glma/db/ladybug_store.py` | Language-generic |
| `src/glma/export.py` | Language-generic |
| `src/glma/summaries.py` | Language-generic |

---

## 2. Tree-sitter Grammar Package Research

### Current pattern (from `parser.py`)

```python
import tree_sitter_c as tsc
import tree_sitter_python as tspython
from tree_sitter import Language as TSLanguage

TSLanguage(tsc.language())  # Returns PyCapsule → TSLanguage object
```

### New grammar packages needed

| Package | PyPI name | Import name | Language function(s) | Notes |
|---------|-----------|-------------|---------------------|-------|
| C++ | `tree-sitter-cpp` | `tree_sitter_cpp` | `language()` | Single grammar |
| TypeScript | `tree-sitter-typescript` | `tree_sitter_typescript` | `language_typescript()` + `language_tsx()` | **Two grammars in one package** |
| Rust | `tree-sitter-rust` | `tree_sitter_rust` | `language()` | Single grammar |

### Key discovery: TypeScript dual-grammar

The `tree-sitter-typescript` package exports TWO language functions:
- `tree_sitter_typescript.language_typescript()` — for `.ts` files
- `tree_sitter_typescript.language_tsx()` — for `.tsx` files

This means TYPESCRIPT and TSX need **separate** `LanguageConfig` entries with different `ts_language` values but could share the same chunk_types and relationship extractors.

### Minimum versions (from ROADMAP)

```
tree-sitter-cpp>=0.23.4
tree-sitter-typescript>=0.23.2
tree-sitter-rust>=0.24.2
```

These align with the existing tree-sitter 0.25.x API (PyCapsule-based language creation).

---

## 3. AST Node Type Mappings per Language

### C++ (`tree-sitter-cpp`)

**Chunk types (tree-sitter node → chunk type):**

| Node type | Chunk type | Notes |
|-----------|-----------|-------|
| `function_definition` | function | Standard |
| `class_specifier` | class | `class Foo { ... }` |
| `struct_specifier` | class | `struct Foo { ... }` |
| `enum_specifier` | class | `enum Foo { ... }` |
| `type_definition` | class | `typedef ...` |
| `namespace_definition` | class | `namespace Foo { ... }` — container too |
| `template_declaration` | function/class | Wraps function/class, extract inner name |
| `constructor_definition` | function | `Foo() { ... }` |
| `destructor_definition` | function | `~Foo() { ... }` |

**Container types:** `translation_unit`, `namespace_definition`, `class_specifier`

**Relationship node types:**

| Relationship | Node type | Extraction approach |
|-------------|-----------|-------------------|
| #include | `preproc_include` | **Reuse C `_extract_c_includes()`** — same grammar |
| using | `using_declaration` | New: extract `using namespace X` and `using X::Y` |
| calls | `call_expression` | **Reuse C `_extract_c_calls()`** — same grammar structure |
| inheritance | `class_specifier` with `base_class_clause` | New: extract `class Foo : public Bar` |

**Key insight:** C++ grammar is a superset of C. The tree-sitter-cpp grammar handles `.c` files correctly. Per D-02, `.h` should map to C++. Per D-03, `--lang c` only indexes `.c` files. The resolution: `.h` maps to `Language.CPP` in `EXTENSION_MAP`, but `walker.py` filters by active languages. If only C is active, `.h` won't be walked because its language (CPP) isn't in the active set. This is clean and consistent.

### TypeScript (`tree-sitter-typescript`)

**Chunk types:**

| Node type | Chunk type | Notes |
|-----------|-----------|-------|
| `function_declaration` | function | `function foo() {}` |
| `arrow_function` | function | `const foo = () => {}` — tricky, skip for now (usually assigned to variable) |
| `class_declaration` | class | `class Foo { ... }` |
| `interface_declaration` | class | `interface Foo { ... }` — maps to "class" chunk type |
| `type_alias_declaration` | class | `type Foo = ...` — maps to "class" chunk type |
| `enum_declaration` | class | `enum Foo { ... }` — maps to "class" chunk type |
| `method_definition` | method | Inside classes |
| `lexical_declaration` | function | `const foo = () => {}` — only if value is arrow_function |

**Container types:** `program`, `class_declaration`, `module`

**Relationship node types:**

| Relationship | Node type | Extraction approach |
|-------------|-----------|-------------------|
| import | `import_statement`, `import_clause` | New: extract from/import { X } patterns |
| export | `export_statement` | Skip for now (not a relationship between chunks) |
| calls | `call_expression` | New: extract callee names |
| extends | `class_declaration` with `class_heritage` | New: `class Foo extends Bar` |
| implements | `class_declaration` with `class_heritage` | New: `class Foo implements Bar` |

### Rust (`tree-sitter-rust`)

**Chunk types:**

| Node type | Chunk type | Notes |
|-----------|-----------|-------|
| `function_item` | function | `fn foo() { ... }` |
| `struct_item` | class | `struct Foo { ... }` |
| `enum_item` | class | `enum Foo { ... }` |
| `trait_item` | class | `trait Foo { ... }` — methods inside are part of trait chunk |
| `type_item` | class | `type Foo = ...` |
| `impl_item` | container | Container only — methods inside are separate chunks |
| `function_signature_item` | function | Inside traits (just the signature) |

**Container types:** `source_file`, `impl_item`, `trait_item`

**Relationship node types:**

| Relationship | Node type | Extraction approach |
|-------------|-----------|-------------------|
| use | `use_declaration` | New: extract `use crate::foo::bar` |
| calls | `call_expression` | New: extract callee |
| impl for | `impl_item` with `trait` field | New: `impl Trait for Type` |
| mod | `mod_item` | New: `mod foo;` references |

---

## 4. Comment/Docstring Attachment Research

### C++ Comments
- Same `comment` node type as C (`//` and `/* */`)
- No standard docstring convention (Doxygen uses `///` but not universally)
- **Decision D-05:** Reuse C comment proximity heuristic. Add `Language.CPP` → `{"comment"}` to `COMMENT_TYPES`.

### TypeScript Comments
- `comment` node type for `//` and `/* */`
- JSDoc `/** ... */` is still a `comment` node in tree-sitter — differentiated by content starting with `/**`
- **Decision D-10:** Need JSDoc extraction similar to Python docstring — attach `/** */` comments to the following declaration
- Implementation: check if comment text starts with `/**` → treat as docstring, attach to next chunk by proximity (1-line gap)

### Rust Comments
- Three types, all `comment` node type in tree-sitter:
  - `///` (outer doc) — text starts with `///` 
  - `//!` (inner doc) — text starts with `//!`
  - `//` (regular) — text starts with `//` but not `///` or `//!`
- **Decision D-15:** `///` attaches to following item (like JSDoc). `//!` attaches to enclosing module. Regular `//` uses proximity.
- Implementation: similar to JSDoc — check comment text prefix to determine strategy

### Shared pattern: doc-comment extraction

Both JSDoc and Rust `///` share the same pattern: check if a `comment` node's text starts with a specific prefix, and if so, treat it as a docstring attached to the **following** chunk. This can be a shared utility function.

---

## 5. Language Filtering (LANG-06) Research

### Current flow

1. `cli.py` `--lang` flag → `Language(lang_string)` conversion → `IndexConfig.languages`
2. `config.py` `[index]` section `languages` array → same conversion
3. `walker.py` uses `supported_extensions` (extension → language string) and `active_languages` set
4. Walker yields `(filepath, language_string)` — language is a string like `"c"`, not the enum

### Key observation

The walker already filters by active languages. Adding new languages to `supported_extensions` and the `Language` enum is sufficient. No changes to walker logic needed.

### Error handling for unknown languages

Decision D-16: Unrecognized language strings must fail fast. The current `Language(lang_string)` constructor will raise `ValueError` for unknown values — this is already the desired behavior. Just need to ensure the error message is helpful.

---

## 6. Chunk Name Extraction

### Current `_extract_node_name()` in `chunks.py`

- **Python:** Uses `child_by_field_name("name")` — works for functions and classes
- **C:** Uses `declarator` field → drill down to `identifier` — works for functions, `name` field for structs/enums

### New languages

| Language | Pattern | Notes |
|----------|---------|-------|
| **C++** | Same as C for functions. `class_specifier` has `name` field. `namespace_definition` has `name` field. `template_declaration` needs drilling through to the inner declaration's name. | C++ function name extraction same as C. Templates are tricky — the `template_declaration` wraps the actual declaration. |
| **TypeScript** | `function_declaration` has `name` child (identifier). `class_declaration` has `name` child. `interface_declaration` has `name` child. `type_alias_declaration` has `name` child. | Straightforward — `child_by_field_name("name")` works for most |
| **Rust** | `function_item` has `name` field. `struct_item` has `name` field. `enum_item` has `name` field. `trait_item` has `name` field. | `child_by_field_name("name")` works for all |

### Template handling (C++)

`template_declaration` wraps the actual declaration:
```
template_declaration
  ├── template_parameter_list
  └── function_definition (or class_specifier)
       └── name
```

For `_extract_node_name`, when we see `template_declaration`, we need to drill through to find the inner declaration and extract its name. The chunk content should include the `template<...>` prefix.

---

## 7. Relationship Extraction Complexity Analysis

### Difficulty per language

| Language | Complexity | Reason |
|----------|-----------|--------|
| **C++** | **Low** | Can reuse C call extraction and include extraction. Only need: `using` declarations, class inheritance (`class Foo : public Bar`). Templates left as INFERRED per D-04. |
| **TypeScript** | **Medium** | Import extraction is more complex than C (multiple patterns: `import X`, `import { X, Y }`, `import X from 'y'`). Class heritage (extends/implements) needs parsing `class_heritage` nodes. Call extraction similar to C. |
| **Rust** | **Medium** | `use` declarations have path syntax (`crate::module::item`). `impl ... for ...` needs extracting both trait and type names. `mod` references point to files/modules. Call extraction similar to C. |

### Shared patterns with existing code

1. **Call extraction** — All three languages use `call_expression` with a callee child. The C `_extract_c_calls()` pattern (walk AST, find `call_expression`, extract callee name, find enclosing chunk, check same-file chunks) works almost verbatim for C++ and Rust. TypeScript has `call_expression` too but may also have `new` expressions (`new Foo()`) that should be treated as calls.

2. **Import/include resolution** — C++ reuses C's `preproc_include` handling. TypeScript and Rust have more complex import patterns but follow the same INFERRED/DIRECT confidence model.

3. **Inheritance** — Each language has its own syntax but the pattern (find declaration node, extract base class names, search same-file chunks then store) is shared.

---

## 8. Test Strategy Research

### Existing test patterns

1. **Parser tests** (`test_parser.py`): Test that `get_root_node()` returns valid trees and correct node types
2. **Chunk tests** (`test_chunks.py`): Extract chunks from fixture files, verify names, types, counts, hashes, IDs
3. **Relationship tests** (`test_relationships_c.py`, `test_relationships_python.py`): Create synthetic source files, extract chunks + relationships, verify types and confidence levels
4. **Comment tests** (`test_comments.py`): Extract chunks + attach comments, verify docstring and proximity attachment
5. **Detector tests** (`test_detector.py`): Test `detect_language()` for each extension

### Required new tests (per D-18, D-19)

**Fixture files needed:**
- `tests/fixtures/sample.cpp` — C++ with classes, namespaces, templates, constructors, destructors
- `tests/fixtures/sample.ts` — TypeScript with interfaces, type aliases, enums, imports, class extends/implements
- `tests/fixtures/sample.tsx` — TSX with JSX elements (minimal — just ensure parsing works)
- `tests/fixtures/sample.rs` — Rust with structs, enums, traits, impls, use declarations, mod

**Test files needed (minimum per D-19: 3 per language × 4 = 12):**

| Test file | Language | Tests |
|-----------|----------|-------|
| `test_parser.py` additions | CPP, TS, TSX, Rust | Parse returns valid tree |
| `test_chunks.py` additions | CPP, TS, TSX, Rust | Extract correct chunk types and names |
| `test_relationships_cpp.py` | C++ | Calls, includes, using, inheritance |
| `test_relationships_typescript.py` | TS/TSX | Imports, calls, extends, implements |
| `test_relationships_rust.py` | Rust | use, calls, impl for, mod |
| `test_comments.py` additions | CPP, TS, Rust | Doc-comment attachment |

---

## 9. Risk Areas and Edge Cases

### C++ template_declaration nesting
Templates wrap the actual declaration. Need to:
1. Add `template_declaration` to chunk_types
2. In `_extract_node_name`, handle template by finding inner declaration
3. In `_walk_chunks`, recurse into template_declaration to find nested declarations

**Risk:** Template specialization syntax could confuse name extraction. Decision D-04 says leave as INFERRED.

### TypeScript dual-grammar
`tree-sitter-typescript` provides two grammars. Need:
1. Two separate `LanguageConfig` entries (TYPESCRIPT and TSX)
2. Same chunk_types and relationship extractors for both
3. Only difference is `ts_language` value

**Risk:** TSX adds JSX node types that could interfere with chunk extraction. Test with a minimal TSX fixture.

### Rust impl blocks
`impl_item` is a container, not a chunk itself. Methods inside impl blocks are separate chunks. Need:
1. `impl_item` in `container_types` only
2. Walk into `impl_item` to find `function_item` children
3. Name extraction: function name from within impl

**Risk:** `impl Trait for Type` needs special handling — extract both trait name and type name for relationships.

### `.h` file language conflict (D-02 vs D-03)
- `EXTENSION_MAP[".h"] = Language.CPP` (per D-02, always parse as C++)
- If user runs `--lang c`, walker only includes files where language string is `"c"`
- `.h` files have language string `"cpp"` in walker, so they're excluded
- This is the correct behavior per D-03 (C and C++ are independent selections)
- **Risk:** Users upgrading may be surprised that `.h` files are no longer indexed with `--lang c`. The old behavior indexed `.h` as C. Need to document this in CLI help text or release notes.

---

## 10. RelType Enum Considerations

Current `RelType` enum:
- `CALLS` = "calls"
- `IMPORTS` = "imports"
- `INHERITS` = "inherits"
- `INCLUDES` = "includes" (C-specific)

New relationship types needed:

| Type | Existing? | Notes |
|------|-----------|-------|
| calls | ✓ `CALLS` | Reused for all languages |
| imports | ✓ `IMPORTS` | TypeScript `import`, Rust `use` |
| includes | ✓ `INCLUDES` | C++ `#include` (reused from C) |
| inherits | ✓ `INHERITS` | C++ `class Foo : Bar`, TS `extends` |
| implements | **New** | TypeScript `class Foo implements Bar` |
| uses | **New** (or reuse IMPORTS?) | C++ `using`, Rust `use` |

**Decision:** Consider whether to add new `RelType` values or reuse existing ones:
- `using` declarations (C++) and `use` (Rust) are semantically imports → reuse `IMPORTS`
- `implements` (TypeScript) is distinct from `inherits` → add `IMPLEMENTS` RelType
- `mod` (Rust) is a module reference → could be `IMPORTS` or a new `MODULE_REF` type

This is agent's discretion, but the planner should be aware of the choice.

---

## 11. Implementation Wave Strategy

Based on dependency analysis:

**Wave 1: Foundation (no dependencies between tasks)**
- Task A: Add Language enum values + dependencies in pyproject.toml
- Task B: Add LanguageConfig entries to parser.py + extension map
- These can be in the same plan since they're small and tightly coupled

**Wave 2: Per-language extractors (parallel within wave)**
- Task C: C++ relationship extraction + comment attachment
- Task D: TypeScript relationship extraction + comment attachment  
- Task E: Rust relationship extraction + comment attachment

**Wave 3: Integration + CLI + tests**
- Task F: Walker updates, CLI help text, language filtering
- Task G: Comprehensive test suite for all new languages

Actually, a better grouping:

**Plan 01: Language Foundation** (Wave 1)
- Language enum, pyproject.toml, detector, parser configs, walker extensions, chunk name extraction
- This is the "plumbing" that everything else depends on

**Plan 02: C++ Support** (Wave 2)
- Relationship extraction, comment attachment, fixtures, tests
- Reuses most C patterns

**Plan 03: TypeScript Support** (Wave 2)  
- Relationship extraction, comment attachment, fixtures, tests
- Most complex import patterns

**Plan 04: Rust Support** (Wave 2)
- Relationship extraction, comment attachment, fixtures, tests
- Unique impl/trait patterns

**Plan 05: CLI Integration & Language Filtering** (Wave 3)
- CLI updates, filtering tests, end-to-end integration tests
- Depends on all language support being complete

---

## RESEARCH COMPLETE

Key findings:
1. **Architecture is well-structured for extension** — clear extension points, no refactoring needed
2. **C++ is easiest** — grammar is C superset, most extractors reusable
3. **TypeScript needs careful handling** — dual grammar, complex imports
4. **Rust impl blocks are the main wrinkle** — container-only pattern, trait impl relationships
5. **Comment attachment needs new doc-comment strategies** for TS (JSDoc) and Rust (`///`/`//!`)
6. **`.h` file handling is clean** — detector maps to CPP, walker filters by active languages
7. **RelType enum may need `IMPLEMENTS`** — TypeScript interface implementation is semantically distinct
8. **~12 new test files/functions minimum** per D-19, plus fixture files for each language
