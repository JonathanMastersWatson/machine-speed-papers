#!/usr/bin/env python3
"""Convert a Machine Speed Paper PDF to clean markdown with front matter.

Usage: pdf_to_md.py <pdf> <out_md> <out_abstract> --title T --subtitle S ...
"""
import argparse
import re
import subprocess
import sys


def extract(pdf_path: str) -> str:
    out = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"],
        capture_output=True, text=True, check=True,
    ).stdout
    return out


def clean(text: str, short_title: str) -> list[str]:
    lines = text.replace("\x0c", "\n").split("\n")
    cleaned: list[str] = []
    skip_contents = False
    heading_re = re.compile(
        r"^(Chapter \d+[A-Z]?\s*—\s*.+|Interlude\s*—\s*.+|Appendix(\s+[A-Z])?\s*—?\s*.+|"
        r"References|Abstract|Acknowledg(e)?ments?)$")

    def is_contents_line(s: str) -> bool:
        # contents entries end with a page number, carry dot leaders,
        # or are hyphen-wrapped across lines
        return bool(re.search(r"\.\s*\d+\s*$", s) or s.endswith("-")
                    or re.search(r"\.{2,}", s))

    for raw in lines:
        line = raw.rstrip()
        s = line.strip()

        if skip_contents:
            # a real heading: matches heading pattern AND is not a contents entry
            if heading_re.match(s) and not is_contents_line(s):
                skip_contents = False
            else:
                continue

        if not s:
            cleaned.append("")
            continue
        # series header on title page
        if s == "The Machine Speed Papers":
            continue
        # contents block
        if s == "Contents":
            skip_contents = True
            continue
        # dot-leader contents lines that slipped through
        if re.search(r"\. \. \.", s):
            continue
        # running header: short title + page number
        if re.match(rf"^{re.escape(short_title)}\s+\d+$", s):
            continue
        # standalone page number
        if re.match(r"^\d{1,4}$", s):
            continue
        # headings
        if heading_re.match(s) and not is_contents_line(s):
            cleaned.append("")
            cleaned.append("## " + s)
            cleaned.append("")
            continue
        cleaned.append(line)

    # drop the title-page block: everything before the first real heading
    # (front matter already carries title/author/version)
    first_heading = next(
        (i for i, l in enumerate(cleaned) if l.startswith("## ")), None)
    if first_heading is not None:
        cleaned = cleaned[first_heading:]

    text = "\n".join(cleaned)
    # dehyphenate line-break hyphens
    text = re.sub(r"([A-Za-z])-\s*\n\s*([A-Za-z])", r"\1\2", text)
    # collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip().split("\n")


def extract_abstract(lines: list[str]) -> str:
    start = end = None
    for i, line in enumerate(lines):
        if line.strip() == "## Abstract":
            start = i + 1
        elif start is not None and line.startswith("## "):
            end = i
            break
    if start is None:
        return ""
    body = "\n".join(lines[start:end]).strip()
    # single paragraph flow
    body = re.sub(r"\n+", " ", body)
    return body.strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out_md")
    ap.add_argument("out_abstract")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", required=True)
    ap.add_argument("--short-title", required=True)
    ap.add_argument("--number", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--interior-version", required=True)
    args = ap.parse_args()

    raw = extract(args.pdf)
    lines = clean(raw, args.short_title)
    abstract = extract_abstract(lines)

    front = (
        "---\n"
        f'title: "{args.title}"\n'
        f'subtitle: "{args.subtitle}"\n'
        f"paper_number: {args.number}\n"
        f'version: "{args.version}"\n'
        f"author: \"Jonathan M. Watson\"\n"
        f'date: "{args.date}"\n'
        'series: "The Machine Speed Papers"\n'
        'canonical_pdf: "paper.pdf"\n'
        'license: "CC-BY-4.0"\n'
        "---\n\n"
        f"# {args.title}\n\n"
        f"*{args.subtitle}*\n\n"
        f"**Jonathan M. Watson** — The Machine Speed Papers, No. {args.number} — "
        f"Version {args.version} — {args.date}\n\n"
        "---\n\n"
        "*Machine-readable text derived from the canonical PDF (`paper.pdf`). "
        "In case of any discrepancy, the PDF governs.*\n\n"
    )
    if args.interior_version != args.version:
        front += (
            f"*Note: the PDF title page states version {args.interior_version}; "
            f"this file is released as version {args.version}.*\n\n"
        )

    with open(args.out_md, "w") as f:
        f.write(front + "\n".join(lines).strip() + "\n")
    with open(args.out_abstract, "w") as f:
        f.write(f"# Abstract — {args.title}\n\n{abstract}\n")
    print(f"wrote {args.out_md} ({len(lines)} lines), abstract {len(abstract)} chars")


if __name__ == "__main__":
    main()
