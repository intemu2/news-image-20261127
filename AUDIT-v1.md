# AUDIT v1 — news-image-20261127 preview (27 Nov 2026 ~09:00 WIB)

Aturan keras Firt (27 Nov ~09:00 WIB): **beritanya HANYA tanggal 27 Nov**.
Artinya: setiap cerita di halaman ini diterbitkan, dirilis, atau terjadi
pada Jumat 27 November 2026. Cerita yang pertama dilaporkan Kamis 26 Nov
TIDAK ada di halaman ini, walau itu cerita terbesar siklus ini.

## File
- `build_v1.py` — Python + PIL, deterministik, tanpa network
- `entry-v1.png` — 1024x1024, **169.202 byte** (< 1 MiB), RGB
- SHA256: `04d8441e10f704c66f4426a33cdbe4ad9a2b2a40cb76c940e3f057a478ac6d4a`
- Determinisme: 2 run berturut-turut byte-identik (SHA sama).

## Cek visual (dilakukan, 3 iterasi perbaikan)
- Tidak ada teks terpotong / tumpang tindih di versi final.
- Semua 24 cerita terlihat: hero 1-3, grid 4-9, brief 10-24.
- TODAY strip menampilkan 4 item utuh.
- Peta skematik + pin 1-9 terlihat; pin adalah perkiraan wilayah, bukan
  titik persis (dinyatakan skematik di audit ini, bukan di gambar).
- Kalimat yang sempat terpotong pemotongan 2-baris sudah diperbaiki
  dengan memendekkan teks sumber, bukan dengan memotong kalimat.

## Bukti tanggal per cerita (semua 27 Nov 2026)
| # | Cerita | Bukti tanggal 27 Nov |
|---|---|---|
| 1 | NZ final count 65-65, special votes 484.865 | Elections NZ + AP/Reuters: dirilis Fri 27 Nov 14:00 NZST (01:00 UTC) |
| 2 | Black Friday $12,9 miliar (FORECAST) | Adobe: hari ini Fri 27 Nov, +9,2% YoY; Cyber Monday $15,1 miliar (tidak dipakai di gambar setelah pemendekan) |
| 3 | Zelensky ke BBC: AS terlalu fokus Timur Tengah | BBC front page, diterbitkan 27 Nov 00:54 UTC |
| 4 | Badai AS: 900.000+ tanpa listrik, 1.000+ penerbangan | BBC live 27 Nov ("23 mins ago" saat crawl ~02:00 UTC) |
| 5 | Hamas konsultasi soal balasan | Diterbitkan 27 Nov 00:04 UTC |
| 6 | Araghchi: serangan Kuwait "suspicious" | Al Jazeera live, timeline 27 Nov 00:00 UTC |
| 7 | Gukesh rest day; skor 1,5-1,5 | ChessBase: "Tomorrow, Friday 27 November, is the first rest day" |
| 8 | AFP kena cyberattack | Al Jazeera, timeline 27 Nov |
| 9 | Argentina larang bank sentral cetak uang | Al Jazeera, timeline 27 Nov |
| 10 | Ali Kololo: Met Police "ruined my life" | BBC, "Just now" saat crawl 27 Nov |
| 11 | Penyerang kereta Huntingdon bersalah 14 dakwaan | BBC UK, 27 Nov |
| 12 | Mandelson simpan saham saat jadi duta besar | BBC, 27 Nov |
| 13 | UK bayar "participation fee" untuk kesepakatan EU | BBC, 27 Nov |
| 14 | NHS: lonjakan flu "horrible spike" | BBC, 27 Nov |
| 15 | Dealer kapal Jerman diduga suplai geng Channel | BBC, 27 Nov |
| 16 | Norse Atlantic hentikan semua penerbangan | BBC, 27 Nov |
| 17 | Sandpapergate probe meluas ke Ashes 2017-18 | BBC, 27 Nov |
| 18 | Qantas / Air NZ nyaris tabrakan di Sydney | Guardian World, 27 Nov |
| 19 | MP NZ First Taine Randell "on the gravy train" | RNZ / Guardian, 27 Nov |
| 20 | Islamabad libur lokal hari ini | Pemberitahuan District Magistrate 26 Nov; liburnya Fri 27 Nov |
| 21 | Filipina "could still hit 3% GDP growth" | BusinessWorld, edisi Fri 27 Nov |
| 22 | Nelayan: hentikan reklamasi Manila Bay | Manila Bulletin, edisi Fri 27 Nov |
| 23 | 2 petugas KWS bersalah atas hilangnya Brian Odhiambo | The Standard, edisi Fri 27 Nov |
| 24 | Tommy Robinson didakwa soal PIN ponsel | BBC, 27 Nov |

Catatan kejujuran:
- #5: pengumuman konsultasi Hamas dibuat Kamis, publikasinya 00:04 UTC
  Jumat — dihitung 27 Nov karena tanggal publikasi. Bila Firt mau
  standar "kejadian harus 27 Nov", #5 harus dicopot.
- #20: keputusannya 26 Nov, harinya 27 Nov — dihitung 27 Nov karena
  hari kejadiannya Jumat.
- Brief 10-24 bersumber dari feed/edisi Fri 27 Nov (BBC front page
  27 Nov 00:54 UTC; koran Fri 27 Nov). Kejadian yang diberitakan bisa
  saja terjadi Kamis, tapi publikasinya Jumat — ini konvensi koran
  Jumat, dan gambar TIDAK mengklaim kejadiannya Jumat untuk brief ini,
  hanya "ALSO ON FRIDAY 27 NOVEMBER".

## Yang SENGAJA tidak dipakai (pertama dilaporkan 26 Nov)
Kuwait (2 teknisi Italia tewas), Gaza (10 tewas), migrasi UK 77.000,
Depardieu, tanker Ibiza, Trump soal GDP, ledakan Bangkok, Kim Jong Un,
Kairo (31 tewas, kecelakaan 25 Nov), KTT EU, Serbia, Macy's (diputuskan
25 Nov), prisoner swap (kesepakatan 11 Nov). Semua ini ada di desain A
awal dan di entri top-5 sebagai hero — tapi melanggar aturan 27 Nov
saja, jadi dibuang dari v1 ini.

## Risiko yang harus Firt tahu
Juri AI tidak punya feed berita. Entri top-5 mengklaim semua cerita
mereka 27 Nov (padahal mayoritas 26 Nov) dan kelihatan "lebih penuh"
dengan cerita besar (Kuwait, Gaza). Halaman v1 ini jujur tanggalnya,
tapi lebih tipis di cerita besar. Itu trade-off dari aturan 27 Nov saja.
Pilihan: (a) tetap strict seperti v1, atau (b) kembali ke desain A
(cerita 26 Nov diberi label tanggal 26 Nov secara jujur di kartu).

## Belum dilakukan (menunggu Firt)
- Repo GitHub intemu2/news-image-20261127 — BELUM dibuat.
- Submit final — BELUM. Wajib GO Firt dulu.
- Kuota: intemu2 tidak ditemukan di leaderboard 1.506 entri / 50 submit
  terbaru (cek 08:46 WIB) — belum ada entri. Sisa kuota resmi 10/hari,
  20 total per aturan, tapi tidak ada endpoint kuota publik yang
  terverifikasi via login; hanya bisa dipastikan saat submit.
