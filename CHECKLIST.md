# Checklist — apa yang belum

Status terakhir: 9 November 2026. Diurutkan dari yang paling berdampak.

---

## A. Wajib sebelum dipublikasikan

| # | Item | Kenapa penting |
|---|---|---|
| A1 | **Ejaan nama**: logo "ANUGRAH", situs "ANUGERAH" | Nama badan usaha harus konsisten di semua materi. Pilih satu. |
| A2 | **Alamat lengkap**: logo menyebut *Desa Karangjaya, Kec. Pebayuran, Bekasi*, situs masih "Bekasi, Jakarta & Sekitarnya" | Alamat adalah sinyal kepercayaan nomor satu untuk usaha lokal. |
| A3 | **Email aktif**: `info@anugerahkembar.co.id` | Domain ini kemungkinan belum dimiliki; email mati = lead hilang. |
| A4 | **Angka statistik**: 500+ pelanggan, 1.2K+ unit, 4.9★ | Kalau belum terukur, jangan ditampilkan — berisiko dianggap klaim palsu. |
| A5 | **Testimoni**: Budi Santoso, Siti Rahma, Andi Wijaya | Saat ini fiktif. Ganti testimoni asli atau kosongkan dulu. |
| A6 | **Kebijakan Privasi** | Form mengumpulkan nama + nomor HP + alamat (UU PDP No. 27/2022). |
| A7 | **Hosting + domain + HTTPS** | Sekarang masih file lokal; belum bisa diakses publik. |

## B. Konten yang bikin orang percaya & menghubungi

| # | Item | Kondisi sekarang |
|---|---|---|
| B1 | **Foto asli** (tim, unit, proses pemasangan, sebelum/sesudah) | Semua visual masih ikon vektor. |
| B2 | **Peta Google Maps + tombol "Buka di Maps"** | Kartu peta masih dekorasi, bukan peta sungguhan. |
| B3 | **Harga / kisaran harga** | Tidak ada info harga sama sekali, padahal ini pertanyaan pertama calon pembeli. |
| B4 | **Daftar layanan berpakat** (cuci AC, isi freon, bongkar-pasang, perbaikan) | Layanan masih 4 kartu umum tanpa detail/estimasi. |
| B5 | **Katalog produk** | 4 kartu generik; "Lihat Semua Katalog" cuma membuka WhatsApp. |
| B6 | **Legalitas** (NIB, akta CV, sertifikat teknisi) | Belum ada bagian khusus — nilai jual besar untuk B2B. |
| B7 | **Jam operasional konsisten** | Kartu "24/7 Konsultasi" vs footer "Senin–Sabtu 08.00–17.00". |
| B8 | **Tombol WhatsApp mengambang** | Belum ada; di HP pengguna harus scroll ke atas untuk menghubungi. |

## C. Teknis, SEO, dan performa

| # | Item | Catatan |
|---|---|---|
| C1 | **Tailwind CDN** → build CSS lokal | CDN memunculkan peringatan produksi, ±300 KB JS, dan halaman tanpa gaya bila CDN diblokir. |
| C2 | **Konten bergantung JavaScript** (`opacity:0` + IntersectionObserver) | Tanpa JS/`<noscript>`, banyak section tampak kosong. |
| C3 | **Google Maps embed** | Sekalian untuk C2 di atas: peta + alamat terverifikasi. |
| C4 | **JSON-LD LocalBusiness** | Nama, alamat, telepon, jam buka, koordinat → peluang muncul di Google Maps/pencarian lokal. |
| C5 | **canonical, robots.txt, sitemap.xml** | Belum ada satu pun. |
| C6 | **og:image 1200×630** | Sekarang memakai logo persegi 512 px; preview share WA/FB jadi kecil. |
| C7 | **Analytics + tracking klik WA** | Tanpa ini tidak ketahuan berapa orang menghubungi dari web. |
| C8 | **Aksesibilitas** | Label tidak terhubung (`for`/`id`), modal tanpa `role="dialog"`/`aria-modal`, fokus tidak terkunci di modal, tombol menu tanpa `aria-expanded`, teks `slate-400` kontras rendah. |
| C9 | **Performa** | Preconnect font/CDN, Font Awesome diganti subset/ikon SVG, minify. |
| C10 | **`prefers-reduced-motion`** | Animasi snowflake berputar & float tetap jalan bagi pengguna yang minta animasi dikurangi. |
| C11 | **Halaman tambahan**: Kebijakan Privasi, Syarat & Ketentuan, 404 | Semua masih satu file. |
| C12 | **Git + backup** | Belum ada version control; satu file bisa hilang tanpa jejak. |

## D. Bug kecil yang sudah ditemukan

| # | Lokasi | Masalah |
|---|---|---|
| D1 | Tentang → statistik | Tertulis **"100% ORIENTAL"** — hampir pasti maksudnya **ORISINAL**. |
| D2 | Kontak → kartu email | Bukan link `mailto:`, jadi tidak bisa diklik (footer sudah benar). |
| D3 | Menu mobile | Setelah memilih menu, panel menu **tetap terbuka** menutupi halaman. |
| D4 | Form pemesanan | Pesan WhatsApp tidak di-`encodeURIComponent`, jadi karakter `&`, `#`, atau `%` di alamat pelanggan bisa merusak isi pesan. |
| D5 | Footer | Tahun `© 2026` ditulis manual. |
| D6 | Header mobile | Nama perusahaan disembunyikan di layar < 640 px (hanya logo). |

## E. Yang saya butuh dari Anda

1. Ejaan resmi: **ANUGRAH** atau **ANUGERAH**.
2. Alamat lengkap + kode pos + titik Google Maps.
3. Nomor WhatsApp & email resmi (dan apakah domain `anugerahkembar.co.id` sudah ada).
4. Jam operasional sebenarnya.
5. Angka nyata (jumlah pelanggan/unit/rating) atau izin menghapusnya.
6. Testimoni asli (nama, kota, jenis pekerjaan) — atau izin menghapus sementara.
7. Foto: logo sudah ✓, tinggal foto unit/tim/pengerjaan bila ada.

---

## Usulan urutan kerja

**Paket 1 — perbaikan cepat (bisa dikerjakan sekarang, tanpa data baru):**
D1, D2, D3, D4, D5, C2 (`<noscript>`), C8 (aksesibilitas dasar), C10.

**Paket 2 — siap online:**
C1 (build Tailwind lokal), C5, C6, C4 (JSON-LD), C7, B8 (tombol WA mengambang).

**Paket 3 — konten & kepercayaan (butuh data/foto Anda):**
A2, A3, A4, A5, B1–B7.

**Paket 4 — naik kelas:**
A6, A7, C11, C12, halaman katalog produk.
