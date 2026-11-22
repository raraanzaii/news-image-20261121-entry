"""make.fun entry for news-image-20261121: "The Saturday World".

The repository holds the finished front page as entry.png (drawn by
generate.py at build time). This program is the graded entrypoint: it runs
offline with the Python standard library only and copies entry.png to the
output directory, so the two grading runs write byte-identical files.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024  # kit limit: 1 MiB, at most 1024x1024


def check_source() -> None:
    """Fail loudly rather than ship a broken page: the bundled entry.png
    must be a real PNG inside the kit's size and dimension limits."""
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    width, height = struct.unpack(">II", data[16:24])  # IHDR dimensions
    if width > 1024 or height > 1024:
        raise SystemExit(f"entry.png is {width}x{height}, over the 1024px limit")


def output_dir() -> Path:
    """The grader mounts a writable /output; locally MAKEFUN_OUTPUT_DIR wins."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(override) if override else Path("/output")


def main() -> None:
    check_source()
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target_dir / "entry.png")


if __name__ == "__main__":
    main()
