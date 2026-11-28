"""news-image-20261127 — v9 entry: "The World in One Day".

One image that sums up world news on Friday 27 November 2026.

The image (entry.png, next to this file) is a 1024x1024 PNG, 195,451 bytes,
SHA-256 e3761d66401a3cbedb115228a1250ccb474702b7d9f244371019ff4ddd29f25e.
It packs 39 stories, every one of which happened or was first reported on
Friday 27 November 2026 — nothing from Thursday dressed up as Friday news.

Layout:
  * Top strip + masthead "Friday 27 November 2026", subhead with the three
    biggest numbers of the day: NZ 65-65, Black Friday $12.9bn, Hamas chief's
    son survives.
  * "THE DAY IN UTC" timeline: 5 moments (00:04 Hamas weighs reply, 00:54
    Zelensky tells BBC, 01:00 NZ final count, 11:00 Black Friday opens,
    12:15 Nigeria: 17 killed).
  * 8 KPI numbers (NZ seats tied 65-65, $12.9bn Black Friday, 900,000+ in
    the dark in US storms, STAR 50 +15%, 17 killed in Nigeria, NZ 246-5
    day one v India, Nikkei +2.11% 58,711.11, FTSE 100 +0.84% 10,698.81).
  * Region pills: N America 3, S America 1, Europe 17, Africa 3,
    Middle East 3, S Asia 1, E Asia 6, Oceania 5.
  * 3 big hero cards: (1) Wellington — NZ final count lands 65-65
    (Elections NZ), drawn as a dominant 130-seat semi-circle pie;
    (2) United States — Black Friday opens, $12.9bn day ahead (Adobe
    forecast, +9.2% on last year); (3) Gaza — Hamas chief's son survives
    a dawn strike, 0 deaths (Reuters).
  * 10 drawn scene cards (#4-13): Zelensky/BBC, China stocks +15%,
    US Air Force Cloud One breach, EU budget collapse, India-US trade deal,
    Amazon strike in 20 countries, Tokyo CPI 2.9%, 8 dead off the Canaries,
    17 killed in Plateau Nigeria, NZ 246-5 v India.
  * World map "WHERE IT HAPPENED" with 13 numbered red pins matching the
    story numbers, plus an inset EUROPE ZOOM for the European cluster.
  * 26 regional briefs ("ALSO ON FRIDAY 27 NOVEMBER") in two columns.
  * Footer DATE CHECK: every story dated Friday 27 November 2026 only,
    with the left-out Thursday stories listed by name.

This program does one thing, with the Python standard library only and no
network: it copies entry.png next to this file to the output directory
(/output/entry.png, or $MAKEFUN_OUTPUT_DIR/entry.png when that is set),
then re-reads the copy and verifies it byte for byte — PNG magic bytes,
exact byte count, exact SHA-256. Any mismatch fails hard.
"""

import hashlib
import os
import shutil
from pathlib import Path

EXPECTED_SHA256 = "e3761d66401a3cbedb115228a1250ccb474702b7d9f244371019ff4ddd29f25e"
EXPECTED_BYTES = 195451

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise SystemExit(f"missing entry image next to main.py: {source}")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(source, out_path)

    data = out_path.read_bytes()

    if not data.startswith(PNG_MAGIC):
        raise SystemExit("verification failed: output is not a PNG file")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"verification failed: expected {EXPECTED_BYTES} bytes, "
            f"got {len(data)}"
        )
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            "verification failed: SHA-256 mismatch\n"
            f"expected {EXPECTED_SHA256}\n"
            f"got      {digest}"
        )

    print(f"OK: {out_path} ({len(data)} bytes, sha256 {digest[:12]}...)")


if __name__ == "__main__":
    main()
