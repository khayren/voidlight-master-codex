# Rename v2 Execution Report (master codex)

Tanggal: 2026-11-28. Executor: controller (ZCode) dengan binary compiler
baru (branch `feat/split-entities`, rename v2). Scope: MINIMAL - hanya
chain yang menghasilkan full ID melebihi batas filename/path Windows.

## Konteks

Fitur split-entities compiler memakai full entity ID sebagai filename.
Blocker empiris: inline passage entity
`...case-studies.<container-80char>.<istidraj-55char>.scenario-a.<synthesis-57char>`
butuh filename 259 char (>255). Percobaan kaskade pertama (237 rename)
di-revert owner; eksekusi ini pakai pendekatan minim-diff.

## Rename yang diaplikasikan (7 entity, via `vdl rename --write`)

| Old (segmen terakhir) | New | Alasan |
|---|---|---|
| case-studies-firaun-umar-and-istidraj-drift-realignment-and-degradation-patterns | firaun-umar-istidraj | chain terdalam, -62 char |
| istidraj-nikmat-as-alignment-test-vs-degradation-path | istidraj-test-vs-degradation | chain terdalam, -24 |
| scenario-a-ujian-naik-tier-alignment | scenario-ujian-naik | chain terdalam, -17 |
| scenario-b-istidraj-degradation-path | scenario-istidraj | chain terdalam, -17 |
| agency-architecture-the-alignment-agent | alignment-agent | full path 264 > MAX_PATH, -21 |
| boot-sequence-niat-as-alignment-activation-protocol | boot-sequence-niat | ikut chain agency, -27 |
| alignment-statement-vs-transactional-request | statement-vs-transaction | konsistensi file-entity |

Setiap rename: dry-run dulu (output ringkas: 2 edit + file/folder moves),
lalu `--write`, lalu `vdl validate .` (hijau 326 file / 472 entitas setiap
kali).

## Surgery descendants (gap tool yang ditemukan)

`vdl rename` v2 me-rename entity + file/folder-nya sendiri, tapi TIDAK
me-rewrite package header file-file descendant (file yang package-nya
mengandung chain entity yang direname) dan folder tree `passages/`.
Ditangani dengan satu pass terkontrol per chain: replace string segmen lama
→ baru di semua `.vdl` (45 + 44 + 2 occurrences, semua di konteks ID - diaudit
dulu: nol di prose) + `git mv`/`mv` folder & file di `passages/artifacts/`.
Setelah tiap pass: validate hijau.

Gap ini tercatat sebagai kandidat perbaikan tool berikutnya (rename v3:
rewrite package header descendant + move folder mirror tree).

## Verifikasi akhir

- `vdl validate .`: 326 file / 472 entitas, nol error.
- E2E split di snapshot bersih (luar repo): **472 halaman**, 0 filename
  >255, 0 absolute path >260 (worst 236), **1.146 internal links resolve
  semuanya**, teks Arab utuh di halaman dalil (30:30 spot-check).
- Reading order aman: urutan baca mengikuti `includes` (tidak diubah);
  rename file hanya memengaruhi sorted-path ordering di graph/stats, bukan
  urutan render.

## Sisa (opsional, tidak blocking)

ID 130-199 char yang masih panjang secara editorial (mis.
`case-study-knowledge-holders-and-ujub-as-uncomputable`,
`entity-types-different-node-roles-in-alignment-network`) lolos batas
teknis. Pemendekan lanjutan = keputusan editorial terpisah, pakai pola yang
sama (dry-run → write → surgery descendants → validate).
