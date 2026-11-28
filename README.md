# The World in One Day — 27 November 2026 in one image

[![Bounty: news-image-20261127](https://make.fun/badge/bounty/news-image-20261127)](https://make.fun/bounty/news-image-20261127)
[![Rank: intemu2](https://make.fun/badge/rank/news-image-20261127/intemu2)](https://make.fun/bounty/news-image-20261127)
[![Reward: $100](https://make.fun/badge/reward/news-image-20261127)](https://make.fun/bounty/news-image-20261127)

Entry for the make.fun bounty **news-image-20261127** — *"Sum up 27 November's
world news in one image"*.

Bounty: <https://make.fun/bounty/news-image-20261127>

## The entry (v9)

One 1024×1024 image that sums up world news on **Friday 27 November 2026**:
**39 stories**, every one of which happened or was first reported that Friday —
nothing from Thursday dressed up as Friday news.

- **Top strip + masthead** — "Friday 27 November 2026", subhead with the three
  biggest numbers of the day: NZ 65-65, Black Friday $12.9bn, Hamas chief's
  son survives.
- **"THE DAY IN UTC" timeline** — 5 moments: 00:04 Hamas weighs reply,
  00:54 Zelensky tells BBC, 01:00 NZ final count, 11:00 Black Friday opens,
  12:15 Nigeria: 17 killed.
- **8 KPI numbers** — NZ seats tied 65-65 · $12.9bn Black Friday sales ·
  900,000+ in the dark in US storms · STAR 50 +15% · 17 killed in Nigeria ·
  NZ 246-5 day one v India · Nikkei +2.11% 58,711.11 · FTSE 100 +0.84% 10,698.81.
- **3 big hero cards:**
  1. **Wellington — NZ final count lands today: 65-65** (Elections NZ).
     Drawn as a dominant 130-seat semi-circle pie, "65" big in each half,
     "Nat 40 · Lab 36 · Opp 7 · 66 needed" underneath.
  2. **United States — Black Friday opens: $12.9bn day ahead** (Adobe).
     Stores open at 06:00 as Adobe forecasts a record $12.9bn in US online
     sales today, up 9.2% on last year.
  3. **Gaza — Hamas chief's son survives Friday strike** (Reuters).
     Izzeldeen al-Hayya survives a dawn strike Friday; his daughter-in-law
     is wounded, no deaths. Scene carries "0 DEATHS" and "DAWN STRIKE" pills.
- **10 drawn scene cards (#4–13)** — Zelensky on the US and the Middle East
  (BBC), China stocks surge with STAR 50 +15% (Reuters), hackers breach the
  US Air Force Cloud One (Reuters), EU budget talks collapse in Brussels
  (Reuters), India-US trade deal "close to done" (Reuters), Amazon workers
  strike in 20 countries (UNI), Tokyo inflation 2.9%, a 16-month high
  (Reuters), 8 dead on a migrant boat off the Canaries (Reuters), gunmen
  kill 17 villagers in Plateau, Nigeria (Reuters), NZ 246-5 on day one
  v India (Cricinfo).
- **World map — "WHERE IT HAPPENED"** — 13 numbered red pins matching the
  story numbers, with an inset EUROPE ZOOM for the European cluster.
  New Zealand drawn as two separate islands; Japan drawn as islands apart
  from mainland Asia.
- **26 regional briefs** — "ALSO ON FRIDAY 27 NOVEMBER", two columns, from
  US storms to Tommy Robinson charged over a phone PIN code.
- **Footer DATE CHECK** — every story published, released, or happened on
  Friday 27 November 2026, with the left-out Thursday stories listed by name.

## Run it

```bash
python3 main.py
```

Python standard library only, no network. `main.py` copies `entry.png` (in this
repo, next to `main.py`) to `/output/entry.png` — or to
`$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set — then re-reads the
copy and verifies it: PNG magic bytes, exact byte count, exact SHA-256.
Any mismatch fails hard.

## The image

- File: `entry.png` — 1024×1024 PNG, RGB
- Size: **195,451 bytes** (under the 1 MiB limit)
- SHA-256: `e3761d66401a3cbedb115228a1250ccb474702b7d9f244371019ff4ddd29f25e`

## Prize

**$100 across 50 paid places**: 1st $20, 2nd $12, 3rd $6, 4th–10th $2,
11th–50th $1.20. Bounty closes **Sunday 29 November 2026, 07:00 WIB**.

See `TRANSCRIPTS.md` for the full v1–v9 build log, the honest date caveats,
and the verification notes.
