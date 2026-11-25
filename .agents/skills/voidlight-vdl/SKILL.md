---
name: voidlight-vdl
description: Author, revise, or migrate knowledge into this VDL repository (Voidlight Master Codex). Use for schema and entity design, modular Soul content, typed citations, document composition, and verification of rendered Markdown.
---

# Voidlight VDL

The VDL project lives in this repository. Paths below are relative to the
repository root. Before changing declarations or build targets, check:

- Build manifest: `vdl.toml`
- Schema: `schema.vdl`
- Project guide: `README.md`

Use the project files as the authority on supported types and existing IDs.
Rendered Soul documents are published to the Voidlight documentation
repository — see "Edit and verify" below.

## Model the knowledge

- Give each entity an ID, an owner for its content, and a reason to be reused or addressed independently. Split by concept or role. A Markdown heading can suggest a boundary. Keep supporting paragraphs, tables, and caveats together when they explain one claim.
- Declare `package` in each source file and use a short local name for the entity. Use human-readable filenames and keep existing IDs stable when moving files or editing titles. Use full IDs across packages, or file-local imports where they improve readability. Wildcards expose direct members of one package.
- Keep ordinal numbers out of titles and filenames. Preserve meaningful designations such as `Axiom 0` and old section locators that prose still cites. Use `number_headings` per Markdown target in `vdl.toml` when a document needs generated numbering.
- A framework owns its identity and arranges reusable content. In the current Soul schema, `based_on` points to axioms, `grounded_in` points to revelations, and `cites` links a claim or module to its sources. Preserve these meanings when reorganizing a document.
- An artifact owns its title and prose and can render independently. Use `body { … }` for authored Markdown. A framework can place standalone `include <id>` directives among its prose when the schema enables body composition. Ordered `includes` and `opening_axioms` serve the existing Divine Alignment structure. Order comes from declarations in the parent.

## Keep evidence and prose editable

- Use `revelation`, `synthesis`, and `analogy` for the categories the author actually declared. A typed passage owns its full text. Keep quotations, interpretation, and audit notes together where they give context. Consolidate a synthesis when its parts develop the same claim. Sharing a citation alone is insufficient to establish that two claims are the same.
- Reuse a revelation ID for the same source and locator. Attach citations at the entity that uses them. Preserve uncertain attributions and audit flags from the source. Compiler validation establishes that references resolve and types match.
- In a mixed `passages` list, use inline `prose { … }` for connective text and typed references for reusable passages. The schema supplies the rendered block labels. Keep those labels out of passage bodies.

## Edit and verify

- Read the current source and relevant domain registry before migrating. Preserve authored wording, Markdown, and reading order unless the task calls for editorial changes. Record structural changes that affect headings, links, IDs, or output metadata.
- Edit `.vdl` here and regenerate Markdown with `vdl compile .`. Rendered Soul documents are published to the Voidlight documentation repository after compiling (copy `dist/soul/divine-alignment.md` and `dist/soul/voidlight-human-os.md` to their published names there; those are generated views, never edit them directly). Keep generated views under the output directory configured in `vdl.toml`.
- From the repository root, run `vdl validate .` and `vdl compile .` with a compiler that supports the current schema. Preview a reusable entity with `vdl compose . --root <full-id>`. Check the affected output for order, heading depth, prose fidelity, and expected citations. For a structural migration, compare the old and new renders and explain deliberate differences.

For a framework with imports and a body scaffold, read
[Human OS](human-os/framework.vdl). For typed evidence and a distinct axiom,
read [Divine Alignment](divine-alignment/framework.vdl) and
[the Axiom 0 passages](divine-alignment/passages/axiom-zero/dua-kelas-wujud.vdl).
