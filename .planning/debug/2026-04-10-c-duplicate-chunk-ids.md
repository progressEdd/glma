---
status: investigating
trigger: "Indexing Linux kernel C files crashes with duplicate primary key"
created: 2026-04-10T23:10:00.000Z
updated: 2026-04-10T23:14:00.000Z
---

## Current Focus

hypothesis: Chunk ID format `{file}::{type}::{name}::{start_line}` produces duplicates when tree-sitter reports same-named structs at different locations in C files
test: Index crypto/api.c from Linux kernel
expecting: Crash with duplicate primary key on crypto_alg
next_action: Defer to v2 — add content_hash or byte offset to chunk ID

## Symptoms

expected: `glma index` successfully indexes all C files including those with duplicate struct names
actual: Crash: `RuntimeError: Found duplicated primary key value api.c::class::crypto_alg::38`
errors: `RuntimeError: Found duplicated primary key value ... which violates the uniqueness constraint of the primary key column`
reproduction: `glma index /path/to/linux-kernel/crypto --lang c`
started: Always broken — C chunker doesn't de-duplicate IDs

## Eliminated

- hypothesis: It's a Ladybug DB issue
  evidence: The duplicate is in the chunk ID itself — same file, same type, same name, same start_line. Multiple tree-sitter nodes resolve to identical ID strings.
  timestamp: 2026-04-10T23:11:00Z

## Evidence

- timestamp: 2026-04-10T23:10:30Z
  checked: Tried indexing `block/` directory (74 .c files)
  found: Crashes on `block/elevator.h::class::request::138`
  implication: Not file-specific — structural issue with C parsing

- timestamp: 2026-04-10T23:11:00Z
  checked: Tried indexing `crypto/` directory (159 .c files)
  found: Crashes on `api.c::class::crypto_alg::38` — likely macro-expanded or forward-declared structs
  implication: C headers and macros create duplicate AST nodes with same name/line

## Resolution

root_cause: _chunk_id() in chunks.py uses format `{file}::{type}::{name}::{start_line}`. When C macros or forward declarations produce multiple struct definitions with same name and reported start line, IDs collide.

fix: Not yet applied. Proposed: append content_hash (first 8 chars) or byte offset to chunk ID to guarantee uniqueness. Requires updating _chunk_id(), upsert_chunks() primary key handling, and potentially the resolver.

verification: `glma index` on Linux kernel crypto/ directory completes without error.

files_changed: []
