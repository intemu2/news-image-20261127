#!/usr/bin/env python3
"""news-image-20261127 v10 — entry program (Python stdlib only).

Copies the entry image shipped beside this file to the output directory.
Validates the image against the competition's caps first (PNG, at most
1 MiB, at most 1024x1024) so a bad file fails loudly instead of entering.
No network, deterministic.
"""
import os
import shutil
import struct


def _png_size(path):
    """Return (width, height) of a PNG, or fail loudly if it is not one."""
    with open(path, "rb") as f:
        head = f.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    return struct.unpack(">II", head[16:24])


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    size = os.path.getsize(src)
    if size > 1048576:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB cap")
    width, height = _png_size(src)
    if width > 1024 or height > 1024:
        raise SystemExit(f"entry.png is {width}x{height}, over the 1024x1024 cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.png")
    if out_dir.endswith("entry.png"):
        out_dir = os.path.dirname(out_dir) or "."
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
