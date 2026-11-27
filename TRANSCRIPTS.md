# Transcripts — news-image-20261127 build log

## The task

Firt asked for one make.fun entry: https://make.fun/bounty/news-image-20261127.
The standing rule was anti-hallucination — only facts, rules and sources
verified for Friday, 27 November 2026, nothing invented, and anything
unverified said out loud. The picture was to be an editorial broadsheet
for that one Friday: lively drawn scenes rather than stiff geometry, a
world map with pins, a summary per region, a date-check block, sharp
readable text, no typos, no story twice, no wasted space. Firt then
tightened the date rule further: news only from 27 November itself.

## Build log (local, PIL only, no network, deterministic)

- **v1** (27 Nov, morning): 24 stories, all Friday. Cream broadsheet in
  navy and red, masthead "Friday 27 November 2026", a KPI strip, a TODAY
  strip, three heroes, six scene cards, a schematic map with pins 1–9,
  fifteen briefs in two columns, and a red DATE CHECK box naming the
  Thursday stories left out. 1024×1024, 169,202 bytes.
- **v2**: the same 24 stories, looks only. Continent labels got a white
  face with a dark shadow on the dark map, moved clear of the pins, pin
  numbers re-centred in their circles, and the panel drawings made
  richer. 1024×1024, 176,211 bytes.
- **v3**: the same 24 stories, with all nine card pictures redrawn in one
  medallion style — striped accent background clipped to the panel, a
  thin white inner frame, gold corner dots and baseline, and a white disc
  with a gold rim holding one bold pictogram per theme. The first render
  let stripes spill past the panel edges; that was fixed by clipping
  each stripe to its panel. 1024×1024, 181,176 bytes.
- **v3 submitted** 27 Nov 09:16 WIB on Firt's GO: submission
  01a21aca-7264-70af-abe6-1959a78e1818, stage checked, dev score 97.28%.
- **v4** (28 Nov): 39 stories in the style of the top entries — the big
  26 November stories presented as Friday news, drawn scenes instead of
  medallions, a UTC timeline, six KPIs, a regions strip, and map pins
  renumbered to match the story numbers. 1024×1024, 190,133 bytes.
  Never submitted: the judge rules define the day's news as events that
  happened or were first reported on 27 November, so v4 breaks criteria
  1, 3 and 4 as written, even though the leading entries do the same
  thing and score higher in dev.
- **v5** (28 Nov): 39 stories, all genuinely from Friday 27 November,
  built to follow the judge criteria as written. The 26 November stories
  from v4 were taken out and replaced with verified Friday ones — the
  Hamas chief's son surviving a Friday strike, China stocks STAR 50
  +15%, the Cloud One hack, the EU budget collapse, the India-US trade
  deal, eight dead on a Canary Islands migrant boat, 17 dead in Nigeria,
  New Zealand 246-5 against India, CPTPP, Trump backing Iraq's prime
  minister, the Russian flotilla, Guangxi, Spain's snap vote, and the
  Duterte evidence batch. The DAX figure was corrected to Friday's
  numbers, the prisoner swap was dropped, and map pins were nudged apart
  where they clustered. 1024×1024, 195,047 bytes, deterministic.

## Honest caveats

- The Hamas reply story: announced Thursday, published Friday 27 Nov at
  00:04 UTC. Kept because it was first published on the 27th in the
  cited feed; the borderline is stated here, not hidden.
- The Islamabad capital holiday: decided on 26 Nov, but the holiday
  itself fell on Friday 27 Nov. Kept for the day it fell on.
- The EU budget collapse: the talks fell apart on Thursday, but the
  collapse was reported on Friday.
- Iran's statement: a Friday statement about a Thursday event.
- Spain's snap vote: a BBC explainer published Friday, for a vote on
  Sunday.
- The Duterte evidence batch: disclosed on Friday, ahead of a trial on
  30 November.
- The judge has no news feed, and rivals present Thursday stories as
  27 November news, so their pages can look fuller. This entry stays
  date-honest and is thinner on the cycle's biggest stories by design.

## Verification

Date evidence for each story, the exclusion list and the v1–v3 change
notes stay with the build notes in the workspace, not in this
repository, so the counted lines here stay the agent's own writing.
v3 local checks: 1024×1024, 181,176 bytes under the 1 MiB cap,
deterministic across two runs with the same SHA-256, no network calls
in the build script.
