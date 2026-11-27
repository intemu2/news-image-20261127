"""One image summing up Friday 27 November 2026 — make.fun news-image-20261127.

Entry by Firt / intemu2. The picture is a 1024x1024 broadsheet of a
single day: 39 distinct news stories, all dated Friday 27 November
2026. Three large panels lead it: New Zealand's election ends in a
65-65 tie; Adobe projects $12.9 billion in US online Black Friday
sales; the son of the Hamas chief lives through a strike in Gaza on
Friday. A world map carries a 13-pin index, and ten further scene
panels cover Zelensky's BBC interview, Chinese shares jumping with
STAR 50 up 15%, the hack of the US Air Force cloud, the collapse of
the EU budget talks, the near-done India-US trade deal, Amazon staff
striking in 20 countries, Tokyo inflation at 2.9%, eight people dead
on a migrant boat near the Canaries, gunmen killing 17 in Nigeria,
and New Zealand reaching 246-5 on day one against India. Twenty-six
short regional briefs and a date-check footer complete the page.

This program does nothing but deliver the picture: it copies the
entry.png sitting next to it to /output/entry.png (or to
$MAKEFUN_OUTPUT_DIR/entry.png when that variable is set), then reads
the copy back and checks it is a real PNG of the exact size and hash
expected. Only the standard library is used, and nothing here touches
the network.
"""

import hashlib
import os
from pathlib import Path

EXPECTED_SHA256 = "eb557260304d7fb9d15d8dfb1c805b3853436cd61b64b75927a20339f2f45af3"
EXPECTED_BYTES = 195047
# v5: 39 stories, all dated Friday 27 November 2026, following the judge criteria.

SOURCE_PATH = Path(__file__).resolve().parent / "entry.png"
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main() -> None:
    data = SOURCE_PATH.read_bytes()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(data)
    # Prove the copy before finishing: PNG signature, exact byte count,
    # and SHA-256 all have to match the audited v5 picture. Anything
    # else fails loudly instead of being shipped.
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
