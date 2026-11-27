# AUDIT v2 — news-image-20261127 preview (27 Nov 2026 ~09:00 WIB)

Revisi visual 1 putaran atas v1, atas perintah Firt. **Isi berita TIDAK
berubah sama sekali** — HEROES, GRID, BRIEFS, dan TODAY di `build_v2.py`
byte-identik dengan v1 (dicek programatis). Tetap 24 cerita, 100%
bertanggal Jumat 27 November 2026. Bukti tanggal per cerita ada di
`AUDIT-v1.md`; tidak ada fakta/angka baru di v2.

## File
- `build_v2.py` — Python + PIL, deterministik, tanpa network
- `entry-v2.png` — 1024x1024, RGB, **176.211 byte** (< 1 MiB)
- SHA256: `41757b4c1f120628036ad2909464a8d824cea961e544a5bb155a1d22e248dab2`

## Yang diubah di v2 (hanya visual)
1. **Label benua di peta gelap:** ditambah 6 label putih tebal dengan
   bayangan gelap 1 px (NORTH AMERICA, SOUTH AMERICA, AFRICA, EUROPE,
   ASIA, AUSTRALIA). Posisi dipilih agar tidak tertutup pin: EUROPE
   dipindah ke (5E, 64N), AFRICA ke (30E, 18N). Dicek lewat crop peta
   diperbesar — keenam label terbaca penuh, tidak ada yang tertutup pin.
2. **Pin angka tepat di tengah:** digambar dengan `anchor="mm"` (bukan
   lagi perkiraan `px - tw/2, py - 6`). Dicek di crop peta: angka 1-9
   semua di tengah lingkaran merah.
3. **Ilustrasi lebih kaya:** tiap panel kini punya 3-6 elemen, bukan
   1-2 ikon polos. Contoh: ballot = matahari + gedung parlemen
   (pedimen + 3 kolom) + kotak suara + centang merah; sale = awning
   garis + tag % + 2 tas + koin; mic = bendera biru-kuning + gelombang
   suara; storm = 2 awan + petir + hujan + tiang listrik; chess =
   papan + bidak K/Q + jam; cyber = monitor + baris kode + segitiga
   peringatan; bank = pedimen + kolom + tumpukan koin + panah naik.
   Plus garis dasar emas tipis di bawah tiap panel.

## Cek lokal (dijalankan, semua lolos)
- Ukuran: 1024x1024, 176.211 byte < 1.048.576 byte — LOLOS
- Determinisme: 2 run, SHA identik `41757b4c…` — LOLOS
- Network: grep `urllib|requests|socket|http|urlopen|subprocess|
  os.system` di build_v2.py = tidak ada — LOLOS
- Isi cerita: HEROES/GRID/BRIEFS/TODAY identik v1 — LOLOS
- Visual: dicek langsung (gambar penuh + crop peta diperbesar).
  Tidak ada teks terpotong / tumpang tindih. Semua 24 cerita terlihat.

## Belum dilakukan (menunggu Firt)
- Repo GitHub intemu2/news-image-20261127 — BELUM dibuat.
- Submit final — BELUM. Wajib GO Firt dulu.
- Kuota: intemu2 tidak ditemukan di leaderboard 1.506 entri / 50
  submit terbaru (cek 08:46 WIB) — belum ada entri. Sisa kuota resmi
  10/hari, 20 total per aturan; tidak ada endpoint kuota publik yang
  terverifikasi via login, hanya bisa dipastikan saat submit.
