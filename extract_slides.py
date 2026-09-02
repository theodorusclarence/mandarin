"""Pull colour-annotated vocabulary out of class slide PDFs.

The plain text layer of these PDFs discards colour, which loses the blue-marked
words -- usually the ones actually being taught. This reads character colours and
positions instead, and regroups them into words.

    python3 extract_slides.py Slides_20260819.pdf
"""
import sys
from collections import defaultdict

import pdfplumber

BLUE = (0.0, 0.439, 0.753)
RED = (1.0, 0.0, 0.0)


def norm(colour):
    if isinstance(colour, (list, tuple)):
        return tuple(round(c, 3) for c in colour)
    return colour


def close(a, b, tol=0.08):
    """Colours vary slightly between exports, so match with a tolerance."""
    if not isinstance(a, tuple) or len(a) != 3:
        return False
    return all(abs(x - y) < tol for x, y in zip(a, b))


def group_runs(chars, gap=6):
    """Group characters into words: bucket by line, then split on x-gaps."""
    lines = defaultdict(list)
    for ch in chars:
        lines[round(ch["top"] / 3)].append(ch)

    runs = []
    for key in sorted(lines):
        row = sorted(lines[key], key=lambda c: c["x0"])
        current = [row[0]]
        for prev, ch in zip(row, row[1:]):
            if ch["x0"] - prev["x1"] <= gap:
                current.append(ch)
            else:
                runs.append(current)
                current = [ch]
        runs.append(current)
    return runs


def run_text(run):
    return "".join(c["text"] for c in run).strip()


def analyze(path):
    with pdfplumber.open(path) as pdf:
        sizes = [round(c["size"], 1) for page in pdf.pages for c in page.chars]
        body_size = max(set(sizes), key=sizes.count)

        for number, page in enumerate(pdf.pages, 1):
            found = []
            for label, colour in (("BLUE", BLUE), ("RED", RED)):
                chars = [c for c in page.chars
                         if close(norm(c.get("non_stroking_color")), colour)]
                words = [run_text(r) for r in group_runs(chars) if run_text(r)]
                if words:
                    found.append((label, words))

            # Pinyin annotations: latin text set noticeably smaller than body copy
            pinyin = [c for c in page.chars
                      if round(c["size"], 1) < body_size * 0.8
                      and c["text"].strip()
                      and ord(c["text"][0]) < 0x2E80]
            words = [run_text(r) for r in group_runs(pinyin, gap=3) if run_text(r)]
            if words:
                found.append(("PINYIN", words))

            if found:
                print(f"\n=== PAGE {number} ===")
                for label, words in found:
                    print(f"  [{label}] {words}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python3 extract_slides.py <slides.pdf>")
    analyze(sys.argv[1])
