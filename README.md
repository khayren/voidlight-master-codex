---
title: Voidlight Master Codex
type: index
status: active
pillar: soul
created: 2026-11-13
updated: 2026-11-24
tags: [voidlight, vdl, modules]
---
# Voidlight Master Codex

Sumber terpadu modul-modul **Voidlight** yang ditulis dalam format **VDL**
(Voidlight Definition Language) — format deklaratif untuk menulis framework
pengetahuan: setiap dokumen mendefinisikan modelnya sendiri, konten dipecah
menjadi unit bertipe yang komposabel, dan setiap klaim menyandang sitasi
bertipe ke modul dalil.

Repo ini dirancang sebagai rumah bersama seluruh modul Voidlight. Saat ini
berisi dua framework pada pillar Soul; modul lain akan ditambahkan sebagai
direktori sendiri seiring perkembangan.

## Isi repo

| Direktori | Isi |
| --- | --- |
| `divine-alignment/` | **Divine Alignment Architecture** — arsitektur alignment ruhani: Axiom 0 (wajib vs mumkin), qalb sebagai penentu, kasb, qada-qadar, hingga threat model drift |
| `human-os/` | **Human OS** — arsitektur manusia dengan metafora sistem operasi: ruh, qalb, nafs, immutable core, dan protokol maintenance-nya |
| `dalil/` | **Modul dalil kanonik** — satu sumber koordinat Al-Qur'an dan Hadits untuk semua framework (66/66 koordinat terisi dan terverifikasi) |
| `schema.vdl` | Model dokumen: tipe entitas, field, dan aturan komposisi |
| `vdl.toml` | Manifest build: target Markdown yang dirender |
| `tools/dalil-fetch.py` | Alat pengambil teks verbatim (Quran.com API + Sunnah.com) |

Dokumen ditulis dalam Bahasa Indonesia (campur istilah teknis Inggris).

## Integritas dalil

Setiap file di `dalil/` membawa teks Arab kanonik, transliterasi, terjemahan
(Kemenag RI), ringkasan tafsir (Al-Muyassar), dan metadata audit (`audit_note`)
yang merekam proses verifikasi. Teks diambil verbatim dari sumber terbuka
(Quran.com API dan Sunnah.com), diverifikasi sanad-auditor, dan dicek
secara programatik sebelum masuk repo — tidak ada teks yang disusun dari
ingatan. Koordinat dikutip lintas framework lewat ID stabil (mis.
`soul.revelation.quran.30.30`), sehingga satu koordinat cukup diverifikasi
satu kali untuk semua modul.

## Cara build

Butuh [compiler VDL](https://github.com/voidlight-labs/vdl) (Rust, install
via `cargo install --path .`). Dari root repo:

```sh
vdl validate .                                # validasi seluruh project
vdl compile .                                 # render semua target ke dist/
vdl compose . --root soul.human-os.immutable-core.fitrah   # preview satu entitas
```

Hasil render ada di `dist/` (di-gitignore). Dokumen Soul hasil render
(Human OS dan Divine Alignment) dipublikasikan lewat repositori dokumentasi
Voidlight.

## Menambah modul baru

Modul adalah direktori mandiri di root: satu sub-direktori berisi source
`.vdl` dengan `package` sendiri, didaftarkan sebagai target build di
`vdl.toml`. Sitasi ke dalil cukup memakai ID koordinat yang sudah ada.
Panduan penulisan (struktur entri, tipe passage, disiplin sitasi) ada di
[`.agents/skills/voidlight-vdl/SKILL.md`](.agents/skills/voidlight-vdl/SKILL.md).

## Terkait

- [voidlight-labs/vdl](https://github.com/voidlight-labs/vdl) — compiler VDL
  (Rust): validasi, komposisi, dan rendering Markdown
