"""Build a viewer link whose address does not show the file name.

Usage:
  python scripts/viewer_link.py <course> <file name without extension> [pdf|nb|video] [title]

Examples:
  python scripts/viewer_link.py ml TP_1_Introduction nb "Lab 1"
  python scripts/viewer_link.py dl L01_introduction pdf "Lecture 1"

Courses (see COURSES in viewer/index.html): ml -> /files/ml/, idm -> /files/idm/, dl -> /files/
"""
import base64
import sys


def viewer_link(course, doc, kind="pdf", title=""):
    payload = "|".join([course, doc, kind, title]).encode("utf-8")
    return "/viewer/?d=" + base64.urlsafe_b64encode(payload).decode().rstrip("=")


if __name__ == "__main__":
    a = sys.argv[1:]
    print(viewer_link(a[0], a[1], a[2] if len(a) > 2 else "pdf", a[3] if len(a) > 3 else ""))
