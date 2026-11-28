#!/usr/bin/env python3
"""news-image-20261127 v10 — entry program (Python stdlib only).

Copies the entry image shipped beside this file to the output directory.
No network, deterministic.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.png")
    if out_dir.endswith("entry.png"):
        out_dir = os.path.dirname(out_dir) or "."
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
