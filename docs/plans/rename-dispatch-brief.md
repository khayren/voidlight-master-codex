# Dispatch: Eksekusi rename ID permanen - Divine Alignment (1-6)

Role: executor (persona cadence). Workflow: baca `config harness lokal (~/.codex)/agents/work.md`
+ `config harness lokal (~/.codex)/AGENTS.md` dulu. Repo kerja: WORKSPACE INI
(repo master codex VDL). Kamu boleh spawn subagent
(collaboration.spawn_agent, agent_type echo) untuk gate review.

## Konteks

Fitur compiler split-entities butuh filename = full entity ID. Round 4
verifikasi GAGAL karena ada ID 254-256 karakter (melebihi batas filename
Windows 255). Keputusan owner (FINAL, permanen, tanpa residu): RENAME ID
langsung, BUKAN field slug. Pemetaan usulan sudah ada:
`docs/plans/shortname-mapping-draft.md` (baca dulu, penuh).

## Konvensi naming (WAJIB, masuk SKILL.md nanti)

Prefix = fungsi/genre, konsep di tengah, postfix = kind:
- `prereq-*` gate prerequisite; `case-*` case study; `scenario-*` branching;
  `threat-*`/`attack-*` threat model; `glossary-*`/`changelog-*`/`refs-*`
  appendix; `*-protocol`/`*-matrix`/`*-index`/`*-stack` named kinds.
- Container/section: nama konsep polos (mis. `foundation`, `mitsaq-alast`).
- ID = kontrak stabil publik: pilih nama SEKALI, rename berikutnya setelah
  publikasi = breaking change. Jaga lowercase-kebab.

## Task

1. **Bangun tabel rename final** old-full-ID -> new-full-ID dari draft
   mapping (semua entity yang terflag panjang + container yang diusulkan
   ganti; entity pendek = keep). Full ID harus di-resolve dari struktur
   hierarki beneran (cek includes/declaration), jangan dikarang. Simpan
   tabelnya ke `docs/plans/rename-table.md` (kolom: old, new, container).
   Nama baru mengikuti konvensi di atas + draft.
2. **Dry-run semua**: `vdl rename <old> <new>` (tanpa --write) per entry;
   pastikan 0 unresolved/error. Kalau tool menolak karena ambigu, klarifikasi
   manual dengan cek file.
3. **Apply** (`--write`) per batch kecil (10-15), lalu `vdl validate .`
   SETELAH tiap batch. Semua harus tetap hijau (326 file / 472 entitas).
4. **Sinkron registry `dalil-references.vdl`** (stale sejak batch 3):
   pastikan 66 koordinat terpopulasi semua terdaftar dengan ID current
   (17:100 sudah pindah ke 42:27, dll.), hapus entry koordinat yang sudah
   tidak direferensikan, tambah yang baru. Validate ulang.
5. **E2E split di snapshot copy** (salin repo ke `.rename-verify/` di
   workspace, JANGAN nulis dist/ di repo asli — repo asli dist/ boleh
   di-skip): `vdl compile --split-entities` di snapshot dengan binary
   release terbaru (workspace compiler: `repo compiler lokal`,
   binary di `.cargo-target/release/vdl.exe` — READ-ONLY akses, cukup
   path ke binary). Verifikasi: ~472 halaman, **0 filename >255 char**,
   **0 filename ber-hash suffix**, semua link internal resolve (0 missing),
   index DA 10 child + HO 11 child, teks Arab UTF-8 utuh di halaman dalil.
6. **Update SKILL.md** (`.agents/skills/voidlight-vdl/SKILL.md`): tambah
   section "Naming convention" (tabel prefix/postfix di atas + aturan
   "ID dipilih sekali, stabil setelah publikasi").

## Forbidden

- Commit/push. Menulis di luar workspace ini (kecuali READ binary dari
  path compiler). Mengubah konten/isi dokumen (yang berubah CUMA ID dan
  referensinya via tool). Menghapus file. Menyentuh `.env`, secret.

## Report contract

- Laporan: `docs/plans/rename-execution-report.md` (tabel rename final,
  jumlah ref yang di-rewrite per batch, hasil validate tiap batch, hasil
  E2E, isi perubahan SKILL.md).
- Response akhir: Status (DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED) +
  Gate verdict (PASS/FAIL/UNVERIFIED — kalau kamu review sendiri tanpa
  echo, wajib UNVERIFIED) + tabel evidence + Verdict satu baris.
