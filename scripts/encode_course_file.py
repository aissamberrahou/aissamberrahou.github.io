"""Encode a course document (PDF or notebook) for the read-only viewer.

Usage:  python scripts/encode_course_file.py <input file> <output .dat file>

The encoded file cannot be opened directly; it is decoded in the browser
by /viewer/index.html (same key).
"""
import sys

KEY = b"ensias-aissam-berrahou-viewer-2026"


def encode(data: bytes) -> bytes:
    return bytes(b ^ KEY[i % len(KEY)] for i, b in enumerate(data))


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, "rb") as f:
        raw = f.read()
    with open(dst, "wb") as f:
        f.write(encode(raw))
    print(f"{src} -> {dst} ({len(raw)} bytes)")
