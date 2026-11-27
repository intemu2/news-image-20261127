# AUDIT v3 — news-image-20261127 preview (27 Nov 2026 ~09:05 WIB)

Revisi visual putaran ke-2 atas perintah Firt: **ganti seluruh
ilustrasi 9 kartu utama (no. 1-9) dengan set baru yang konsisten**.
Isi berita TIDAK berubah — HEROES, GRID, BRIEFS, dan TODAY di
`build_v3.py` byte-identik dengan v2/v1 (dicek programatis). Tetap 24
cerita, 100% bertanggal Jumat 27 November 2026. Bukti tanggal per
cerita ada di `AUDIT-v1.md`; tidak ada fakta/angka baru di v3.

## File
- `build_v3.py` — Python + PIL, deterministik, tanpa network
- `entry-v3.png` — 1024x1024, RGB, **181.176 byte** (< 1 MiB)
- SHA256: `aa50b6cc6de541d4d9b64852800fc6477fc0062e3d2a90c43e57eba48875d061`

## Yang diubah di v3 (hanya ilustrasi 1-9)
Satu bahasa visual baru yang sama untuk ke-9 panel: latar warna aksen
dengan garis diagonal halus, bingkai putih tipis, titik emas di sudut,
garis dasar emas, dan **medali putih di tengah** berisi satu piktogram
tebal. Piktogram baru per kartu:
1. NZ — centang tebal (navy + merah) + bintang emas
2. Black Friday — "%" merah besar
3. Zelensky — mikrofon + gelombang suara emas
4. Badai AS — awan + petir emas + hujan
5. Hamas — dua balon percakapan (navy + emas) + titik-titik
6. Iran — bulan sabit merah + bintang emas
7. Catur — mahkota raja + kotak papan di kaki medali
8. AFP — perisai + tanda seru + baris kode emas
9. Argentina — "$" dengan cincin + garis larangan merah
   (dilarang mencetak uang)

Perbaikan selama build: garis diagonal v3 awal sempat meluber ke luar
kotak panel dan menutupi teks — diperbaiki dengan memotong (clip)
segmen garis tepat di batas kotak panel, lalu render ulang dan cek
visual ulang. Versi final bersih.

## Cek lokal (dijalankan, semua lolos)
- Ukuran: 1024x1024, 181.176 byte < 1.048.576 byte — LOLOS
- Determinisme: 2 run, SHA identik `aa50b6cc…` — LOLOS
- Network: grep `urllib|requests|socket|http|urlopen|subprocess|
  os.system` di build_v3.py = tidak ada — LOLOS
- Isi cerita: HEROES/GRID/BRIEFS/TODAY identik v2 — LOLOS
- Visual: dicek langsung. Teks semua kartu terbaca penuh, tidak ada
  tumpang tindih. Label benua + pin 1-9 di peta tidak berubah dan
  tetap terbaca (tidak disentuh di v3).

## Belum dilakukan (menunggu Firt)
- Repo GitHub intemu2/news-image-20261127 — BELUM dibuat.
- Submit final — BELUM. Wajib GO Firt dulu.
- Kuota: intemu2 tidak ditemukan di leaderboard 1.506 entri / 50
  submit terbaru (cek 08:46 WIB) — belum ada entri. Sisa kuota resmi
  10/hari, 20 total per aturan; tidak ada endpoint kuota publik yang
  terverifikasi via login, hanya bisa dipastikan saat submit.
