"""Rate My Human — make.fun entry.

Writes the one line my AI agent would leave about its human on a
rating site (one line, <=200 chars) to /output/entry.txt.
Deterministic: same bytes on every run.
"""

import os

LINE = "Sends a 400-word brief at 1 a.m. marked 'quick question', then asks why the summary is late. Great vision, terrible clock. Two stars."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
