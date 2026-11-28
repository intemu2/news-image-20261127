# TRANSCRIPTS.md — news-image-20261127, entri v10

Build log v1–v10 dan caveat jujur. Gambar entry.png 1024x1024 ini digambar
dengan program gambar (PIL) yang ditulis agen dari spesifikasi; main.py hanya
menyalin entry.png ke output.

## Log build v1–v10

- v1 (27 Nov pagi): 24 cerita, semua Jumat. Broadsheet krem navy+merah, masthead
  "Friday 27 November 2026", strip KPI, strip TODAY, 3 hero, 6 kartu adegan,
  peta skematis pin 1–9, 15 brief 2 kolom, kotak DATE CHECK merah.
  1024x1024, 169.202 byte.
- v2: 24 cerita yang sama, perbaikan tampilan: label benua putih berbayangan di
  peta gelap, pin dipindah menjauh, nomor pin di-center ulang, gambar panel
  diperkaya. 176.211 byte.
- v3: 24 cerita yang sama, 9 gambar kartu digambar ulang gaya medallion.
  181.176 byte. SUBMIT 27 Nov 09:16 WIB, submission
  01a21aca-7264-70af-abe6-1959a78e1818, stage checked, skor dev 97,28%.
- v4 (28 Nov): 39 cerita gaya entri top — cerita besar 26 November disajikan
  sebagai berita Jumat, adegan digambar, timeline UTC, 6 KPI, strip region,
  pin peta dinomori ulang sesuai nomor cerita. 190.133 byte. TIDAK DISUBMIT:
  kriteria juri mendefinisikan berita hari itu sebagai peristiwa yang terjadi
  atau pertama dilaporkan 27 November, jadi v4 melanggar kriteria 1, 3, 4.
- v5 (28 Nov): 39 cerita, semua murni Jumat 27 November, patuh kriteria juri.
  195.047 byte. SUBMIT 28 Nov 05:22 WIB, submission
  01a21f1a-7f61-755f-9fe1-74a55ba70f8e, commit cc2b83b, stage checked, ronde 2,
  rank #616/7.674, 97,78% (cek 06:58 WIB).
- v6 (28 Nov): adegan kartu ditinggikan ~45%, peta terang, briefs 2 kolom
  1 baris, timeline 5 titik, KPI lebih besar, pil region berwarna.
  174.283 byte. Tidak disubmit.
- v7 (28 Nov): adegan #4/#8/#9 digambar ulang (Big Ben + kubah St Sophia +
  bendera Ukraina; India Gate + bendera AS; gudang + plakat "PAY"/"20"),
  #13 bat + stumps + papan "246-5", #7 cincin bintang EU, tag FORECAST #2
  pindah ke bawah-kanan scene, bodi #1 satu baris, peta + inset "EUROPE ZOOM".
  178.251 byte. Tidak disubmit.
- v8 (28 Nov): peta digambar ulang (Selandia Baru digambar, pin 1/13 di NZ,
  pin 10 di Honshu, pin 5 di pantai Shanghai, inset EUROPE ZOOM pindah ke
  tengah-bawah peta), nomor pin di-center dengan textbbox, adegan #10/#6/#12
  digambar ulang, pie #1 diperbesar dengan label "65 - 65", headline hero
  naik ~15%, subhead 3 fragmen, KPI jadi 8 angka (Nikkei +2,11% 58.711,11 dan
  FTSE +0,84% 10.698,81 ditambah), fakta #7 jadi "Ukraine loan delayed to
  17-18 Dec", #10 hanya fakta CPI, kata kunci brief dikembalikan, #16
  "GENEVA" jadi "CHESS", footer Sources tambah "Sydney", strip atas
  "19 FIELDS" jadi "13 DRAWN SCENES", catatan pil region Canary/Mediterania.
  186.808 byte. Tidak disubmit.
- v9 (28 Nov): hero #1 kini visualisasi data dominan — pie setengah lingkaran
  130 kursi besar (diameter 116px), "65" besar di tiap belahan, label
  "Nat 40 • Lab 36 • Opp 7 • 66 needed", parlemen hanya strip tipis; chart #2
  dan label "$12.9bn" diperbesar; #3 tambah pill "0 DEATHS" dan "DAWN STRIKE";
  #12 peta Plateau diperbesar dengan "17" besar; label #5 "+15%" dan #10
  "2.9%" diperbesar; peta digambar ulang (Selandia Baru lebih besar,
  kepulauan Jepang terpisah, garis penunjuk klaster Eropa). 195.451 byte,
  SHA256 e3761d66401a3cbedb115228a1250ccb474702b7d9f244371019ff4ddd29f25e.
  SUBMIT 28 Nov 07:19 WIB, submission 01a21f85-a2fc-717d-b1a4-e573cab7d086,
  stage checked, rank #524/8.460, 97,90% (cek 28 Nov 08:37 WIB).
- v10 (28 Nov): 49 cerita (39 v9 + 10 baru terverifikasi Jumat: Kyiv 155 drone,
  Tallinn NATO scramble, Rome FAO/WFP hunger hotspots, Seoul school strike,
  Seoul KOSPI +4.3%, Hong Kong ferry crash, Dubai stocks/Brent, Canberra gas
  law, Kathmandu Nepal mourns, New York UN condemns Kuwait). Kartu adegan baru
  no. 14 (Kyiv 155 drone). Hero #1 pie diperbesar ke ~140 px; hero #2 tambah
  etalase toko; hero #3 dawn diperbesar; tiap hero tambah baris WHY IT MATTERS
  + chip jam UTC; timeline 5 -> 7 titik; peta diperbesar + pin 14 di-offset
  dari pin 4; pil region dihitung ulang (4/1/20/3/4/2/9/6 = 49).

## Caveat jujur

- Balasan Hamas: diumumkan Kamis, pertama diterbitkan Jumat 27 Nov 00:04 UTC.
  Disimpan karena pertama terbit di feed yang dikutip pada tanggal 27.
- Libur ibu kota Islamabad: diputuskan 26 Nov, tapi liburnya sendiri jatuh
  Jumat 27 Nov. Disimpan untuk hari jatuhnya.
- Runtuhnya pembicaraan anggaran EU: gagal Kamis, tapi keruntuhannya
  dilaporkan Jumat.
- Pernyataan Iran: pernyataan Jumat tentang peristiwa Kamis.
- Snap vote Spanyol: penjelasan BBC terbit Jumat, untuk pemungutan suara Minggu.
- Batch bukti Duterte: diungkap Jumat, menjelang sidang 30 November.
- Nepal berkabung (no. 48): pernyataan Jumat tentang pekerja yang tewas
  Kamis di Jazan; yang Jumat adalah pernyataan/duka resminya.
- Kecaman Sekjen PBB atas serangan Kuwait (no. 49): pernyataan Jumat tentang
  serangan Kamis; yang Jumat adalah kecamannya.
- Jazan, Delhi 164, SpaceX FCC, dan postingan Trump 'pull back' TIDAK masuk
  sebagai cerita — semuanya peristiwa/pengumuman 26 Nov atau lebih lama — hanya
  dicantumkan di DATE CHECK sebagai yang ditinggalkan.
- Juri tidak punya feed berita, dan rival menyajikan cerita Kamis sebagai
  berita 27 November sehingga halaman mereka bisa terlihat lebih penuh.
  Entri ini tetap jujur tanggal.
