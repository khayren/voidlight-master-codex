---
title: Voidlight Soul VDL
type: spec
status: active
pillar: soul
created: 2026-11-13
updated: 2026-11-16
tags: [soul, vdl]
---
# Voidlight Soul VDL

Proyek ini membangun Voidlight Human OS dan Divine Alignment Architecture. Dari root repo:

```sh
vdl validate .
vdl compile .
vdl compose . --root soul.human-os.immutable-core.fitrah
```

Pakai compiler VDL yang mendukung proyek multi-file, nested composition, body berkurung kurawal, deklarasi `package`, dan komposisi inline.
Hasil build ada di `dist/soul/voidlight-human-os.md`.
Target itu mengaktifkan `number_headings = true` di `vdl.toml`.
Nomor heading mengikuti urutan dan kedalaman komposisi. Judul di sumber
VDL dan preview dengan `vdl compose` tetap tanpa nomor.

`human-os/framework.vdl` membuka nama artifact dengan `import soul.human-os.*`
dan memberi alias `ar-rahman` pada dalil landasan (`grounded_in`).
Urutan directive `include` di dalam `body` menentukan susunan dokumen.
Setiap artifact memiliki ID, judul, dan body yang bisa dirender mandiri.
`package` menetapkan prefix ID per file. Misalnya, `package
soul.human-os.kernel` dan `artifact ruh` membentuk ID
`soul.human-os.kernel.ruh`. Saat file dipindah, biarkan deklarasi package
dan nama lokal tetap sama agar ID dan referensinya tetap berlaku.
Artifact juga bisa merakit artifact lain lewat `includes` dan menunjuk ke
dalil lewat `cites`. Kedua field boleh dihilangkan kalau kosong.

## Dalil module (`dalil/`)

Koordinat dalil hidup di module `dalil/` — `dalil/quran/<nomor-surah>/<ayat>.vdl`
dan `dalil/hadith/<kitab>/<nomor>.vdl` — sebagai satu sumber kanonik yang
dikutip kedua framework lewat `cites` (ID pakai package numeric surah, mis.
`soul.revelation.quran.30.30`). Status 2026-11-15: **lengkap — 66/66
koordinat terpopulasi (quran 49 + hadits 17), nol stub**.

File dalil lengkap membawa teks kanonik (`original_text`, `transliteration`,
`translation`), metadata (field `title` untuk sitasi short-mode, `narrator`,
`numbering`, `grade_status`, `grade_by`, `sanad_status`, `book_section`),
dan entity `audit_note` inline untuk catatan audit. Relasi tersebut merekam
atribusi penulis; spesifikasi: `labs/projects/vdl-dalil-module-proposal.md`.

**Aturan mutu (wajib):**

- Teks `original_text`/`translation` HARUS verbatim dari sumber yang di-fetch,
  bukan dirakit dari ingatan. Fetch pakai `tools/dalil-fetch.py`
  (quran.com API: text_uthmani + Kemenag resource 33 + Al-Muyassar tafsirs/16;
  sunnah.com untuk hadits) — dijalankan oleh sanad-auditor sendiri, bukan
  orchestrator (SOP auditor-runs-script).
- Retyping teks Arab lewat chat mengubah codepoint Unicode: setelah menulis
  file, field verbatim di-rewrite programatik dari hasil fetch, lalu fidelity
  check programatik (bandingkan field vs extract) wajib hijau sebelum commit.
- Setiap perubahan dalil/passage dengan implikasi klaim wajib lewat
  `sanad-auditor`, dan setiap penanganan didokumentasi di `audit_note`.
- Sebelum commit: `vdl validate .` → `vdl compile .` → copy dist ke path
  legacy (rule di bawah).

## Cites rendering

`vdl.toml` mengatur mode sitasi per target: `cites = "none|link|short"`.
Kedua target framework aktif `cites = "short"` — sitasi dirender sebagai
baris `**Cites:** ...` di bawah label entitas; koordinat yang punya field
`title` dirender dengan judulnya (mis. `QS. Al-A'raf [7]:172`), sisanya
fallback ke ID. CLI override: `vdl compose --cites <mode>`. Default `none`
menghasilkan dist yang identik dengan perilaku lama.

## Divine Alignment Architecture

Target `soul.divine-alignment` membangun `dist/soul/divine-alignment.md`
sebagai satu dokumen. `based_on` menunjuk ke `soul.axiom-zero`. Daftar
`opening_axioms` menyusun axiom pembuka, lalu `includes` menentukan urutan
sembilan bagian dan appendix. Tiap artifact memiliki prosa sendiri dan dapat
dirender mandiri. Contoh:

```sh
vdl compose . --root soul.axiom-zero
vdl compose . --root soul.alignment.sleep-and-death
```

Relasi `passages` menyusun entitas `revelation`, `synthesis`, dan `analogy`
dalam urutan baca. Prosa biasa ditulis langsung sebagai `prose { … }` di
daftar itu. Edit isi entitas bertipe di `divine-alignment/passages/`.
`vdl compose --root <ID>` bisa merender entitas itu mandiri.
**Gotcha:** rename entitas passage wajib diikuti update daftar `passages [...]`
di artifact parent — referensi yang tak ter-resolve membuat `vdl validate`
gagal.

Satu `synthesis` dapat memuat beberapa paragraf, tabel, dan caveat jika
semuanya menjelaskan simpulan yang sama. Label klasifikasi dirender
otomatis dari tipe entitas sebagai heading h4 (`#### REVELATION`,
`#### SYNTHESIS`, `#### ANALOGY`) — bukan lagi bracket `[REVELATION]`;
heading dihasilkan renderer dari schema `label`, verbatim jika mulai `#`.
Schema juga mendeklarasikan type `audit_note` (label `#### AUDIT NOTE`)
dan field `notes` ref untuk menautkannya; inline entity merender text
field terisi sebagai metadata `**field:** value`.

Relasi `cites` menunjuk ke entitas `revelation` di dalil module. ID yang
sudah dipakai framework digunakan ulang. Kutipan, tafsir, dan catatan audit
yang melekat pada satu blok tetap bersama body blok itu. Label inline,
legenda tabel, dan rujukan naratif tetap dalam prosa.

Judul sumber bersih dari nomor urut. Penomoran otomatis target Divine
Alignment dimatikan karena prosa v5.0.7 masih merujuk ke nomor bagian lama.
Penanda `Rujukan v5.0.7` menyimpan nomor itu di bagian yang sesuai.
Navigasi hub dan catatan pemecahan file lama digantikan oleh komposisi VDL.

## Rendered output

`vdl compile .` merender target Markdown yang terdaftar di `vdl.toml` ke
folder `dist/`. Dokumen Soul hasil render (Human OS dan Divine Alignment)
dipublikasikan lewat repositori dokumentasi Voidlight; folder `dist/`
di-gitignore dan bukan bagian dari repo ini.

## Backlog compiler

Validasi ko-occurrence ditunda (mis. modifier schema `require` agar
`sanad_status "verified"` menuntut `original_text` terisi; alternatif murah:
lint script di pipeline build). Rencana lanjutan lain: output graph/DOT/
search untuk schema-form — lihat catatan roadmap di repositori compiler.
