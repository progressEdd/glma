# Phase 18: Extended Language Support - Context

**Gathered:** 2026-05-12
**Status:** Ready for planning

<domain>
## Phase Boundary

Add C++, TypeScript, and Rust as supported languages with full tree-sitter parsing, relationship extraction, and comment attachment. This is primarily wiring work — the parsing pipeline already handles multi-language via tree-sitter.

Requirements: LANG-01 through LANG-06.

No changes to `glma search`, `glma query`, `glma export`, `glma embed`, or `glma watch` commands beyond recognizing the new languages. No new CLI commands. No changes to output formats. Pipeline reliability (Phase 16) features (resume, signal handling) continue to work for new languages.

</domain>

<decisions>
## Implementation Decisions

### C++ Chunk Type Mapping (LANG-01, LANG-04, LANG-05)
- **D-01:** Full C++ coverage — extract chunks for: `function_definition`, `class_specifier`, `struct_specifier`, `enum_specifier`, `type_definition`, `namespace_definition`, `template_declaration`, `constructor_definition`, `destructor_definition`.
- **D-02:** `.h` extension parsed as C++ always. The C++ grammar is a superset of C — valid C parses correctly under C++ grammar. Only `.c` files are parsed as C. `.cpp`, `.hpp`, `.cc`, `.hxx`, `.h` all map to C++.
- **D-03:** C and C++ are independent language selections. `--lang c` indexes `.c` only. `--lang cpp` indexes `.cpp`, `.hpp`, `.cc`, `.hxx`, `.h`. `--lang c,cpp` indexes everything.

### C++ Relationships (LANG-04)
- **D-04:** Core relationship set: `#include` (reuse C pattern), `using` declarations, function calls, class inheritance (`class Foo : public Bar`). Templates left as INFERRED.

### C++ Comment Attachment (LANG-05)
- **D-05:** C++ uses same `//` and `/* */` comment nodes as C — `comment` AST node type. No docstring-like construct (no JSDoc equivalent in standard C++). Reuse existing C comment proximity heuristic.

### TypeScript Chunk Type Mapping (LANG-02, LANG-04)
- **D-06:** Both `interface_declaration` and `type_alias_declaration` become chunks. They define reusable types that agents need when querying TS codebases.
- **D-07:** Separate grammars: `.ts` → tree-sitter-typescript `typescript` grammar, `.tsx` → tree-sitter-typescript `tsx` grammar.
- **D-08:** `enum_declaration` becomes a chunk. `namespace_definition` and `module` are container types only (their children are the real chunks), matching the Python `class_definition` container pattern.

### TypeScript Relationships (LANG-04)
- **D-09:** Core relationship set: `import/export` statements, function/method calls, `extends` (class inheritance), `implements` (interface implementation).

### TypeScript Comment Attachment (LANG-05)
- **D-10:** TypeScript uses JSDoc `/** */` as docstrings (attached to following declaration, similar to Python docstring pattern) plus standard `//` and `/* */` as proximity-attached comments. Need language-specific docstring extraction for JSDoc.

### Rust Chunk Type Mapping (LANG-03, LANG-04)
- **D-11:** Individual methods within `impl` blocks are extracted as chunks, with the `impl` block itself as a container type (matches Python class/method pattern).
- **D-12:** `trait` definitions become class-type chunks. Method signatures within traits are part of the trait chunk content (not separate chunks).
- **D-13:** `struct`, `enum`, `fn` (standalone), `type_alias` all become chunks. `mod` and `use` are NOT chunks — they're relationship extraction targets.

### Rust Relationships (LANG-04)
- **D-14:** Core relationship set: `use` (imports), function calls, `impl ... for ...` (trait implementation), `mod` (module references).

### Rust Comment Attachment (LANG-05)
- **D-15:** Rust has three doc comment styles: `///` (outer doc), `//!` (inner doc), and standard `//`. Outer doc comments (`///`) attach to the following item (like JSDoc). Inner doc comments (`//!`) attach to the enclosing item (typically the module). Standard `//` uses proximity heuristic.

### Language Filtering & CLI (LANG-06)
- **D-16:** Unrecognized language strings produce a clear error immediately: `Error: Unknown language 'java'. Supported: c, cpp, python, typescript, rust`. Fail fast, don't silently skip.
- **D-17:** Default language list stays `[c, python]` — no behavior change for existing users. New languages are opt-in via `--lang cpp,typescript,rust` or `[index] languages = [...]` in `.glma.toml`.

### Testing Strategy
- **D-18:** Synthetic fixtures per language in `tests/fixtures/` — small hand-crafted `.cpp`, `.ts`, `.tsx`, `.rs` files that exercise all chunk types, relationship patterns, and comment styles. Deterministic, fast, matches existing test pattern.
- **D-19:** Full per-language coverage: chunk extraction test + comment/doc attachment test + relationship extraction test for each of C++, TS, TSX, and Rust (minimum 3 tests per language, 12 new tests total).

### Agent's Discretion
- Exact file extensions for each language mapping (e.g., whether to include `.cxx`, `.c++`, `.mjs` etc.)
- Whether to add `Language.CPP` / `Language.TYPESCRIPT` / `Language.RUST` to the Language enum or use a different naming convention
- How to structure per-language relationship extraction functions (mirror existing `_extract_c_*` / `_extract_python_*` pattern, or refactor to a data-driven approach)
- Whether to consolidate comment attachment into a more data-driven config (language → doc comment markers + strategy) vs keeping language-specific functions
- Exact tree-sitter grammar package versions beyond minimum requirements in ROADMAP
- Whether `.h` files should be detected as C++ even when only `--lang c` is specified (currently D-02 says parse as C++ always, but this conflicts with D-03 where `--lang c` only indexes `.c`)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Language detection and parsing (primary integration points)
- `02-worktrees/glma/src/glma/index/detector.py` — `EXTENSION_MAP` maps file extensions to `Language` enum. Must add `.cpp`, `.hpp`, `.cc`, `.hxx`, `.h` → CPP, `.ts` → TYPESCRIPT, `.tsx` → TSX, `.rs` → RUST.
- `02-worktrees/glma/src/glma/index/parser.py` — `LanguageConfig` dataclass and `PARSER_CONFIGS` dict. Each new language needs a `LanguageConfig` with chunk_types, container_types, and relationship node types. New tree-sitter grammar imports go here.
- `02-worktrees/glma/src/glma/models.py` — `Language` enum needs `CPP`, `TYPESCRIPT`, `TSX`, `RUST` values. `IndexConfig.languages` field already accepts `list[Language]`.

### Relationship extraction (per-language dispatch)
- `02-worktrees/glma/src/glma/index/relationships.py` — `extract_relationships()` dispatcher routes by `Language` enum. Add C++, TypeScript, and Rust branches. Existing `_extract_c_*` and `_extract_python_*` functions show the pattern to follow.
- `02-worktrees/glma/src/glma/index/resolver.py` — Import resolution helpers (`build_import_map`, `resolve_callee`). New languages may need their own resolver functions.

### Comment attachment
- `02-worktrees/glma/src/glma/index/comments.py` — `COMMENT_TYPES` dict and `attach_comments()` function. `Language.CPP` reuses C pattern. TypeScript and Rust need language-specific docstring extraction (JSDoc for TS, `///`/`//!` for Rust).

### Config and CLI
- `02-worktrees/glma/src/glma/config.py` — `load_config()` already converts language strings from `.glma.toml` to `Language` enum values.
- `02-worktrees/glma/src/glma/cli.py` — `--lang` flag (line 47) accepts language strings. Help text needs updating.
- `02-worktrees/glma/pyproject.toml` — Add `tree-sitter-cpp`, `tree-sitter-typescript`, `tree-sitter-rust` dependencies.

### Requirements and roadmap
- `.planning/REQUIREMENTS.md` — LANG-01 through LANG-06
- `.planning/ROADMAP.md` — Phase 18 success criteria and key implementation notes

### Prior phase decisions (for continuity)
- `.planning/phases/16-pipeline-reliability/16-CONTEXT.md` — Pipeline stage tracking, resume, chunk ID format. New languages must work with these features.
- `.planning/phases/01-core-indexing-pipeline/01-CONTEXT.md` — Original language detection and parsing architecture decisions.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`LanguageConfig` pattern** (`parser.py`): Dataclass with `chunk_types`, `container_types`, `call_node_type`, `import_node_type`, `inherit_node_type`. Each new language creates one config instance. Well-structured for adding languages.
- **`PARSER_CONFIGS` dict** (`parser.py`): `dict[Language, LanguageConfig]`. Just add new entries.
- **`EXTENSION_MAP`** (`detector.py`): Simple `dict[str, Language]`. Add new extensions.
- **Language-dispatched relationship extraction** (`relationships.py`): `extract_relationships()` if/elif dispatcher. Add new branches. Existing `_extract_c_*` and `_extract_python_*` functions serve as templates for new language extractors.
- **Comment attachment framework** (`comments.py`): `COMMENT_TYPES` dict + `attach_comments()` with language-specific docstring extraction. Pattern supports adding new languages.
- **Test fixture pattern** (`tests/`): Existing C and Python fixtures in test suite. Follow same pattern for new languages.
- **Config loading** (`config.py`): `Language(lang_string)` conversion already works — just needs new enum values.

### Established Patterns
- **`LanguageConfig` for chunk types**: `dict[str, str]` mapping tree-sitter node type → chunk type string ("function", "class", etc.)
- **Container types**: `set[str]` of tree-sitter node types whose children are checked for nested chunks (e.g., `class_definition` in Python)
- **Relationship extraction per language**: Separate `_extract_{lang}_{type}()` functions, called from a top-level `extract_{lang}_relationships()` dispatcher
- **Confidence tagging**: DIRECT for same-file resolved targets, INFERRED for unresolved or cross-file without confirmation
- **Comment attachment**: Two strategies — language-specific docstrings (Python) + generic proximity heuristic (all languages)

### Integration Points
- **`models.py` `Language` enum**: Add CPP, TYPESCRIPT, TSX, RUST. Downstream: detector, parser, relationships, comments, config all reference this enum.
- **`parser.py` `_build_parsers()`**: Add new `LanguageConfig` entries. Import new tree-sitter grammar packages.
- **`relationships.py` `extract_relationships()`**: Add new elif branches for CPP, TYPESCRIPT, TSX, RUST.
- **`comments.py` `COMMENT_TYPES`**: Add CPP (same as C), TYPESCRIPT, TSX (same as TS), RUST. Add docstring extraction for TS (JSDoc) and Rust (`///`, `//!`).
- **`pyproject.toml`**: Add `tree-sitter-cpp>=0.23.4`, `tree-sitter-typescript>=0.23.2`, `tree-sitter-rust>=0.24.2` dependencies.
- **`cli.py` `--lang` flag**: Update help text to list all supported languages.
- **`.glma.toml` `[index]` section**: `languages` array already accepts language strings — just needs new values documented.

### Potential Tension
- D-02 (`.h` parsed as C++ always) vs D-03 (C and C++ independent). If user specifies `--lang c` only, `.h` files would be detected as C++ (per detector) but C++ is not in the language list. Resolution: the agent should treat `.h` as C++ in the detector, but respect language filtering — if only `c` is selected, `.h` files could fall back to C parsing, or be skipped. The agent's discretion to resolve this cleanly.

</code_context>

<specifics>
## Specific Ideas

- The C++ grammar being a superset of C is the key insight that makes `.h` handling simple — no heuristic needed
- TypeScript's two grammars (TS and TSX) from a single `tree-sitter-typescript` package is a minor wrinkle — need to import both `tree_sitter_typescript.language_typescript()` and `tree_sitter_typescript.language_tsx()`
- Rust `///` doc comments are the most similar to JSDoc — both attach to the following item. The extraction pattern can be shared between TS and Rust

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 18-extended-language-support*
*Context gathered: 2026-05-12*
