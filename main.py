"""World news of 27 November 2026 in one image — make.fun news-image-20261127.

Entry for Firt / intemu2. A 1024x1024 PNG broadsheet: 3 hero panels
(New Zealand's election ends in a 65-65 hung parliament; Adobe
forecasts $12.9bn of US online Black Friday sales; Zelensky tells the
BBC the US is too focused on the Middle East), a labelled world map
with a 9-pin index, 6 more scene panels (Thanksgiving storms leave
900,000+ in the dark; Hamas weighs its reply; Iran calls the Kuwait
attack "suspicious"; Gukesh-Sindarov rest day; AFP cyberattack;
Argentina bars central-bank money printing), 15 regional briefs and a
date-check footer. 24 unique stories, no story repeated; every item
was reported or occurred on Friday, 27 November 2026. Sources:
Elections NZ, Adobe, BBC, Reuters, Al Jazeera, ChessBase, RNZ,
BusinessWorld, Manila Bulletin, The Standard, The Guardian (see
TRANSCRIPTS.md for the honest two-tier verification and the
Hamas/Islamabad-date caveats).

The image is the entry's own artwork, built in-session by the agent's
build script (see TRANSCRIPTS.md for the three-version build log); this
program is deliberately offline and dependency-free: it only copies
the entry's image file beside it to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR/entry.png when that is set). Standard
library only, no network.
"""

import hashlib
import os
from pathlib import Path

EXPECTED_SHA256 = "aa50b6cc6de541d4d9b64852800fc6477fc0062e3d2a90c43e57eba48875d061"
EXPECTED_BYTES = 181176

SOURCE_PATH = Path(__file__).resolve().parent / "entry.png"
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main() -> None:
    data = SOURCE_PATH.read_bytes()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(data)
    # Read back and prove the gate before exiting: PNG magic bytes, exact
    # byte count, and SHA-256 must match the audited v3 image. If the file
    # ever holds anything else, fail loudly instead of shipping it.
    written = OUTPUT_PATH.read_bytes()
    if written[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png must start with the PNG magic bytes")
    if len(written) != EXPECTED_BYTES:
        raise ValueError(f"entry.png must be {EXPECTED_BYTES} bytes, got {len(written)}")
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"entry.png SHA-256 mismatch: {digest}")
    print(f"wrote {OUTPUT_PATH} ({len(written)} bytes, sha256 {digest[:12]}...)")


if __name__ == "__main__":
    main()
