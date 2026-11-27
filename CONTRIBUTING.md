# Contributing to Voidlight Master Codex

Terima kasih sudah mau berkontribusi. Repo ini sengaja dibuka untuk dibaca,
dibantah, dan diperbaiki. Kontribusi yang paling berharga: **audit konten**
(koreksi framework, koordinat dalil, ketelusuran tafsir dan hadits) dan
perbaikan alat (`tools/`).

Baca dulu [README](README.md) (posisi konten) dan [LICENSE-CONTENT](LICENSE-CONTENT)
/ [NOTICE.md](NOTICE.md) supaya konteksnya jelas sebelum mulai.

## Posisi yang kami pegang

- Framework di sini **bukan klaim kebenaran final**. Koreksi dan sanggahan
  berbasis sumber selalu lebih diutamakan daripada mempertahankan redaksi lama.
- Atribusi itu urusan pertanggungjawaban, bukan gengsi: setiap perubahan
  bisa ditelusuri siapa mengubah apa, supaya koreksi punya alamat.
- Analogi dan sintesis harus terlabel jelas, tidak boleh menyaru sebagai
  kutipan sumber.

## Cara berkontribusi

### 1. Koreksi kecil (salah lafaz, salah koordinat, salah atribusi)

Buka **Issue** dengan format:

```
Judul: [Koreksi] <lokasi: file atau ID entitas>
Isi:
- Lokasi: <path file / ID entitas VDL, mis. dalil/quran/42/27>
- Tertulis: <kutipan persis yang dianggap salah>
- Seharusnya: <teks/kutipan yang benar>
- Sumber pembanding: <URL / edisi / halaman>
- Catatan: <konteks, kalau perlu>
```

### 2. Perbaikan besar (perubahan doktrin posisi, struktur modul, schema)

Buka **Issue diskusi dulu** sebelum PR, supaya arahnya disepakati bersama.

### 3. Perbaikan langsung (typo, format, broken link, tooling)

PR langsung diterima.

## Standar mutu kutipan dalil (WAJIB)

Ini aturan paling keras di repo ini, karena kesalahan di sini bersifat
silent failure:

1. **Teks harus verbatim dari sumber, bukan dari ingatan.** Al-Qur'an
   (Uthmani), terjemahan (Kemenag), dan tafsir (Al-Muyassar) diverbatim via
   Quran.com API; hadits via Sunnah.com. Teks yang dirakit dari ingatan
   sudah terbukti berkali-kali menghasilkan lafaz yang salah, jadi tolong
   fetch dulu sebelum menulis.
2. Gunakan `tools/dalil-fetch.py` untuk fetch (stdlib saja):

   ```sh
   python tools/dalil-fetch.py quran 42:27 94:5-6
   python tools/dalil-fetch.py hadith bukhari:773
   ```

   Output di `.scratch/dalil/` (raw + extract per koordinat). Status OK
   script berarti fetch/extract berhasil saja, bukan pengesahan atribusi
   (attribution tetap cek manual).
3. **Setiap penanganan audit wajib didokumentasikan** di entity `audit_note`
   (konvensi nama: `sanad-<nomor>-<tanggal>`, unik per package). Ganti teks
   atau atribusi tanpa jejak audit = PR ditolak.
4. Kalau terjemahan yang tersedia bervarian antar edisi, pertahankan
   verbatim edisi yang dipakai dan catat variannya di `audit_note` — jangan
   dirata-rata atau dipoles.

## Standar penulisan framework

- Struktur entri, tipe passage, disiplin sitasi: lihat
  [`.agents/skills/voidlight-vdl/SKILL.md`](.agents/skills/voidlight-vdl/SKILL.md).
- Validasi wajib hijau sebelum commit:

  ```sh
  vdl validate .
  vdl compile .
  ```

- Sitasi dalil cukup memakai ID koordinat yang sudah ada
  (mis. `soul.revelation.quran.30.30`) — jangan duplikasi teks dalil ke
  dalam dokumen framework.
- Metafora framework (istilah sistem/provisioning, dll.) selalu dilabel
  sebagai analogi penulis di body, terpisah dari teks sumber.

## Lisensi kontribusi

Dengan membuka PR, Anda menyetujui kontribusi Anda dilisensikan sesuai
license repo: [CC BY 4.0](LICENSE-CONTENT) untuk konten dokumen dan
[MIT](LICENSE-MIT) untuk kode. Teks dalil pihak ketiga tidak dilisensikan
di sini (lihat [NOTICE.md](NOTICE.md)).

## Gaya

- Dokumen ditulis dalam Bahasa Indonesia (campur istilah teknis Inggris).
- Satu perubahan satu tema; commit message singkat dan jelas.
- Kalau koreksi Anda menyentuh klaim keagamaan, sertakan sumbernya.
  Koreksi tanpa sumber tetap ditinjau, tapi butuh waktu lebih lama.
