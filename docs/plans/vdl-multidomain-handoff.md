# VDL Multi-Domain: Session Handoff

> **Lokasi update 2026-11-24:** project VDL dipindah keluar dari vault — folder `vdl/` kini di repo master codex (root project). Path `vdl/...` di dokumen ini adalah catatan historis saat project masih di dalam vault; baca sebagai `repo master codex\...` (flattened, tanpa prefix `vdl/`).


Date: 2026-11-12
Status: Proposed; implementation has not started.

> **Status update 2026-11-14:** compiler capabilities assumed missing in this
> handoff have since landed on `origin/main` (multi-file projects, schema
> documents, `vdl compose`, heading labels, `cite` flag + V16, cite render
> modes). The vault now runs a dalil module (`vdl/dalil/`) as the reference
> implementation of reusable cross-framework modules — read it before
> designing the non-Soul Music example. Still accurate: the first
> implementation slice below, the domain-neutral/profile direction, and the
> versioning caveats. Now outdated: any statement that schema documents or
> composition are not yet supported.

## Objective

Extend Voidlight Definition Language beyond Soul documents into a general knowledge definition language while preserving Soul-specific epistemic safeguards and compatibility with existing VDL documents.

## Project

- Local compiler: repo compiler VDL
- Repository: https://github.com/voidlight-labs/vdl
- Existing project registry: labs/projects/vdl.md
- Before implementation, read the compiler repository's AGENTS.md and inspect its current working tree and changes. Do not overwrite unrelated work.

## Architectural direction

1. Separate domain-neutral language and structural validation from domain-specific rules. Explore explicit validation profiles, including Soul and a general-purpose profile; choose semantics and defaults after inspecting existing APIs and compatibility requirements.
2. Preserve existing Soul evidence categories (revelation, synthesis, analogy) and existing validation behavior for current users. Structural validation is not theological or source verification.
3. Allow non-Soul knowledge to express appropriate provenance, such as a human decision or source, without forcing it into theological evidence categories. Design the representation from concrete examples before extending grammar.
4. Support versions such as 5.0.7 without rejecting valid existing major.minor versions. Specify version semantics and compatibility before implementing.
5. Treat VDL source, compiled graph, Markdown, and indexes as distinct layers. Choose a single authoritative source for any migrated content; avoid independent edits to generated views.
6. Keep sync and conflict resolution separate from compiler validation. Do not introduce a database or vector index unless a demonstrated runtime need warrants one.

## First implementation slice

- Inspect parser, AST, validation orchestration, CLI and fixtures, plus existing tests and any uncommitted local work.
- Define a small non-Soul Music example: a release, track slot, song, and decision/provenance. Determine minimal expressive changes instead of assuming existing relationship types suffice.
- Implement the smallest coherent backward-compatible profile and version changes, with meaningful tests showing existing Soul validation remains effective and the non-Soul example validates correctly.
- Update compiler documentation and AGENTS.md if architecture changes; run appropriate Rust tests and report results and limitations.
- Do not assume the VDL divine_alignment.vdl fixture is authoritative: it says version 2.0 and is test data. Check the current Soul registry and audit status before using actual framework content.
- Existing v0.1 diff ignores version arguments; do not represent it as real version history. Address only if in scope of the selected implementation slice, otherwise document it.

## Constraints and continuation

- No code changes or tests were performed in the previous session.
- The compiler directory was readable but outside that session's writable roots. Open repo compiler VDL as the writable workspace for the next session.
- No commit or push without explicit instruction.
- This is an initial direction, not an approved complete language specification. Resolve routine technical choices from the repository and real examples; ask only for material product decisions that cannot be inferred.
