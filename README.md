# CV Anugerah Kembar Makmur Jaya — Website

Website profil perusahaan (satu file HTML, tanpa build step).

## Struktur

```
index.html                    Halaman utama (semua section, CSS, dan JS)
assets/logo.png               Logo perusahaan untuk web (512 px, PNG, ±37 KB)
assets/logo-master.png        Logo resolusi penuh (930x908) untuk cetak / og-image
assets/favicon-logo-32.png    Ikon tab browser 32x32
assets/favicon-logo-64.png    Ikon tab browser 64x64 (layar Retina)
assets/apple-touch-icon.png   Ikon iOS / bookmark (180x180)
preview/                      Tangkapan layar hasil render terakhir
_tools/make_icons.py          Pembuat ulang favicon dari file logo
```

## Cara membuka

Klik dua kali `index.html`, atau:

```powershell
start index.html
```

Butuh koneksi internet saat dibuka (Tailwind CDN, Font Awesome, Google Fonts).

## Logo terpasang di 4 titik

| Lokasi | Ukuran tampil |
|---|---|
| Header / navbar | 56 px |
| Kartu "Tentang Kami" | 64 px |
| Judul form pemesanan (modal) | 56 px |
| Footer | 44 px |

Logo dimuat oleh blok `loadBrandLogo()` di bagian bawah `index.html`.
Blok itu mencoba `assets/logo.png` → `logo.svg` → `logo.webp` → `logo.jpg`
→ `logo.jpeg` berurutan. Selama file belum ada, tampil ikon snowflake
bawaan sehingga tidak pernah muncul ikon gambar rusak.

Karena logo sudah membawa bentuknya sendiri (lingkaran, sudut transparan),
kotak penampung otomatis jadi transparan saat logo terpasang
(class `logo-loaded`) dan diberi bayangan halus supaya tetap "mengambang"
di atas latar putih maupun biru tua.

## Mengganti logo

1. Timpa `assets/logo.png` dengan file baru (nama harus sama), atau
   simpan sebagai `assets/logo.png` dengan latar transparan.
2. Buat ulang ikon browser:

   ```powershell
   python _tools/make_icons.py --from-logo assets/logo.png
   ```

Rekomendasi file: latar transparan, bentuk persegi 1:1, sisi minimal 512 px.

> Chrome menyimpan ikon tab di cache per URL. Karena itu nama file ikon
> diberi versi (`favicon-logo-32/64.png`). Kalau logo diganti lagi dan ikon
> di tab masih yang lama, ubah angka pada nama file di `index.html`
> (mis. jadi `favicon-logo-64-v2.png`) atau paksa muat ulang dengan
> **Ctrl + Shift + R**.

## Catatan

- Teks di dalam logo tertulis **"CV. ANUGRAH KEMBAR MAKMUR JAYA"**, sedangkan
  teks di website memakai **"ANUGERAH"**. Salah satu perlu diselaraskan.
- Alamat pada logo: **Desa Karangjaya, Kec. Pebayuran, Bekasi** — belum
  dicantumkan di halaman Kontak (saat ini masih "Bekasi, Jakarta & Sekitarnya").
