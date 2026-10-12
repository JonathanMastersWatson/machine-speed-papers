#!/usr/bin/env python3
"""Install the 5 canonical PDFs + derived markdown into the new paper folders,
restructure per-paper directories, and install Paper 6 draft + Paper 7 brief."""
import json
import os
import shutil
import subprocess

ROOT = os.path.expanduser("~/workspace/machine-speed-papers-build")
SRC = os.path.expanduser("~/workspace/user/files")
GOAL = os.path.expanduser(
    "~/workspace/goals/final-seal-of-512-cvs-schema-prime-papers-dec-5-2026/files")

PAPERS = [
    dict(num="01", slug="01-execution-boundary-governance",
         title="Execution-Boundary Governance",
         subtitle="A Runtime Control Model for Autonomous Systems",
         version="2.1", date="2026-07",
         pdf="PAPER_01_-_Execution-Boundary_Governance_-_A_Runtime_Control_Model_for_Autonomous_Systems_-_V2.1.pdf",
         md="/tmp/p1.md", abstract="/tmp/p1abs.md",
         prev="V2 (124 pp) — superseded 2026-10-12 by V2.1 (75 pp), tightened and reconfirmed."),
    dict(num="02", slug="02-constitutional-compression",
         title="Constitutional Compression",
         subtitle="The Emergence of Minimal Governance at Machine Speed",
         version="1.1", date="2026-07",
         pdf="PAPER_02_-_Constitutional_Compression_-_The_Emergence_of_Minimal_Governance_at_Machine_Speed_-_V1.1.pdf",
         md="/tmp/p2.md", abstract="/tmp/p2abs.md",
         prev="V1 (55 pp) — superseded 2026-10-12 by V1.1 (34 pp), tightened and reconfirmed."),
    dict(num="03", slug="03-evidence-systems",
         title="Evidence Systems",
         subtitle="Why Independent Witnesses Emerge at Machine Speed",
         version="1.1", date="2026-07",
         pdf="PAPER_03_-_Evidence_Systems_-_Why_Independent_Witnesses_Emerge_at_Machine_Speed_-_V1.1.pdf",
         md="/tmp/p3.md", abstract="/tmp/p3abs.md",
         prev="V1 (67 pp, circulated privately) — superseded 2026-10-12 by V1.1 (41 pp), tightened and reconfirmed."),
    dict(num="04", slug="04-upstream",
         title="Upstream",
         subtitle="Where Human-in-the-Loop Goes at Machine Speed",
         version="1.1", date="2026-08",
         pdf="PAPER_04_-_Upstream_-_Where_Human-in-the-Loop_Goes_at_Machine_Speed_-_V1.1.pdf",
         md="/tmp/p4.md", abstract="/tmp/p4abs.md",
         prev="First public release: V1.1 (69 pp), 2026-10-12."),
    dict(num="05", slug="05-the-execution-surface",
         title="The Execution Surface",
         subtitle="Why Distributed Compute Cannot Be Shared",
         version="1.1", date="2026-10",
         pdf="PAPER_05_-_The_Execution_Surface_-_Why_Distributed_Compute_Cannot_Be_Shared_-_V1.1.pdf",
         md="/tmp/p5.md", abstract="/tmp/p5abs.md",
         prev="First public release: V1.1 (59 pp), 2026-10-12. "
              "Supersedes the earlier standalone draft 'THE EDGE' V1.0 (26 pp), whose material was reworked into this paper."),
]

NO_ABSTRACT_NOTE = (
    "This paper has no standalone abstract section — it opens directly with Chapter 1. "
    "The opening paragraphs are quoted below as the entry point.\n")


def sh(*args):
    subprocess.run(args, cwd=ROOT, check=True,
                   capture_output=True, text=True)


def install_paper(p):
    d = os.path.join(ROOT, "papers", p["slug"])
    # clear legacy layout
    for legacy in ["paper", "README.md", "LICENSE", ".gitchange"]:
        t = os.path.join(d, legacy)
        if os.path.isdir(t):
            shutil.rmtree(t)
        elif os.path.isfile(t) or os.path.islink(t):
            os.remove(t)
    # figures-diagrams -> figures ; linkedin-posts -> outreach
    fd = os.path.join(d, "figures-diagrams")
    if os.path.isdir(fd):
        for f in os.listdir(fd):
            if f.startswith(".git"):
                os.remove(os.path.join(fd, f))
        os.rename(fd, os.path.join(d, "figures"))
    lp = os.path.join(d, "linkedin-posts")
    if os.path.isdir(lp):
        os.rename(lp, os.path.join(d, "outreach"))
        with open(os.path.join(d, "outreach", "README.md"), "w") as f:
            f.write(
                "# Outreach\n\nLaunch and announcement material for this paper "
                "(LinkedIn series, June–July 2026).\n\nThese posts are public "
                "history and discovery material — they are not part of the "
                "paper itself. The canonical text is `../paper.pdf`.\n")
    # install canonical files
    shutil.copy(os.path.join(SRC, p["pdf"]), os.path.join(d, "paper.pdf"))
    shutil.copy(p["md"], os.path.join(d, "paper.md"))
    shutil.copy(p["abstract"], os.path.join(d, "abstract.md"))
    if p["num"] in ("02", "03"):
        with open(os.path.join(d, "abstract.md"), "a") as f:
            f.write("\n" + NO_ABSTRACT_NOTE)
    # per-paper README
    with open(os.path.join(d, "README.md"), "w") as f:
        f.write(
            f"# {p['title']}\n\n*{p['subtitle']}*\n\n"
            f"**The Machine Speed Papers, No. {p['num']} — Version {p['version']} "
            f"({p['date']})**  \n**Jonathan M. Watson**, Independent Researcher\n\n"
            f"## Files\n\n"
            f"- `paper.pdf` — the canonical paper\n"
            f"- `paper.md` — machine-readable text derived from the PDF "
            f"(the PDF governs in any discrepancy)\n"
            f"- `abstract.md` — abstract / entry point\n")
        ex = os.path.join(d, "executive-summary")
        if os.path.isdir(ex):
            f.write("- `executive-summary/` — executive summary\n")
        fg = os.path.join(d, "figures")
        if os.path.isdir(fg):
            f.write("- `figures/` — figures and diagrams\n")
        oc = os.path.join(d, "outreach")
        if os.path.isdir(oc):
            f.write("- `outreach/` — launch and announcement material (not part of the paper)\n")
        f.write(
            f"\n## License\n\nCC BY 4.0 — see `../../LICENSE`. "
            f"Share and adapt freely, with attribution to Jonathan M. Watson.\n"
            f"\n## Cite\n\n"
            f"Watson, J.M. ({p['date'][:4]}). *{p['title']}: {p['subtitle']}.* "
            f"The Machine Speed Papers, No. {p['num']}, Version {p['version']}. "
            f"https://github.com/JonathanMastersWatson/machine-speed-papers\n")
    # changelog
    with open(os.path.join(d, "CHANGELOG.md"), "w") as f:
        f.write(
            f"# Changelog — {p['title']}\n\n"
            f"## {p['version']} ({p['date']})\n\n- {p['prev']}\n"
            f"- PDF title page states an earlier version number; "
            f"the released version is {p['version']} per the author's release files.\n")
    print(f"installed {p['slug']}")


def install_paper6():
    d = os.path.join(ROOT, "papers", "06-machine-speed-economics")
    for legacy in ["research", "manuscript", "evidence", "README.md"]:
        t = os.path.join(d, legacy)
        if os.path.isdir(t):
            shutil.rmtree(t)
        elif os.path.isfile(t):
            os.remove(t)
    os.makedirs(os.path.join(d, "manuscript"), exist_ok=True)
    shutil.copy(os.path.join(GOAL, "paper-6-draft-v0.1.md"),
                os.path.join(d, "manuscript", "paper-06-draft.md"))
    with open(os.path.join(d, "README.md"), "w") as f:
        f.write(
            "# Machine-Speed Economics\n\n"
            "**The Machine Speed Papers, No. 6 — DRAFT IN PROGRESS**\n\n"
            "Unit of analysis: the firm and the transaction. A technical blueprint "
            "of the machine-speed economy — what the configuration looks like, "
            "how it works, what the results are.\n\n"
            "## Status\n\nWorking draft (v0.1, ~9,000 words, October 2026). "
            "Not final. The manuscript will be released as `paper.pdf` / `paper.md` "
            "when complete.\n\n"
            "## Files\n\n"
            "- `manuscript/paper-06-draft.md` — working draft\n\n"
            "## License\n\nCC BY 4.0 — see `../../LICENSE`.\n")
    print("installed 06-machine-speed-economics (draft)")


def install_paper7():
    d = os.path.join(ROOT, "papers", "07-the-metered-mind")
    for legacy in ["research", "manuscript", "evidence", "README.md"]:
        t = os.path.join(d, legacy)
        if os.path.isdir(t):
            shutil.rmtree(t)
        elif os.path.isfile(t):
            os.remove(t)
    os.makedirs(os.path.join(d, "brief"), exist_ok=True)
    with open(os.path.join(GOAL, "paper-6-7-revised-brief.md")) as f:
        brief = f.read()
    idx = brief.find("# PAPER 7 — The Metered Mind")
    paper7 = brief[idx:].strip() + "\n" if idx != -1 else brief
    with open(os.path.join(d, "brief", "brief.md"), "w") as f:
        f.write(paper7)
    with open(os.path.join(d, "README.md"), "w") as f:
        f.write(
            "# The Metered Mind\n\n"
            "**The Machine Speed Papers, No. 7 — OUTLINE BRIEF (working title)**\n\n"
            "Unit of analysis: the worker and the market. The same architecture "
            "that lets agents transact lets an individual sell judgment per unit — "
            "micropayments, licensing economics, the metered mind.\n\n"
            "## Status\n\nOutline brief only (October 2026). No manuscript yet. "
            "The brief will be replaced by `paper.pdf` / `paper.md` when the "
            "paper is written.\n\n"
            "## Files\n\n"
            "- `brief/brief.md` — working outline brief\n\n"
            "## License\n\nCC BY 4.0 — see `../../LICENSE`.\n")
    print("installed 07-the-metered-mind (brief)")


def sha256(path):
    out = subprocess.run(["sha256sum", path], capture_output=True,
                         text=True, check=True).stdout
    return out.split()[0]


def write_manifest():
    manifest = {"series": "The Machine Speed Papers",
                "author": "Jonathan M. Watson",
                "repository": "https://github.com/JonathanMastersWatson/machine-speed-papers",
                "license": "CC-BY-4.0",
                "papers": []}
    for p in PAPERS:
        d = os.path.join(ROOT, "papers", p["slug"])
        with open(os.path.join(d, "abstract.md")) as f:
            abs_text = f.read()
        # strip the md title line for the manifest
        abs_text = abs_text.split("\n", 1)[-1].strip()[:600]
        manifest["papers"].append({
            "number": int(p["num"]),
            "title": p["title"],
            "subtitle": p["subtitle"],
            "version": p["version"],
            "date": p["date"],
            "status": "published",
            "path": f"papers/{p['slug']}",
            "pdf": f"papers/{p['slug']}/paper.pdf",
            "markdown": f"papers/{p['slug']}/paper.md",
            "sha256_pdf": sha256(os.path.join(d, "paper.pdf")),
            "abstract": abs_text,
        })
    manifest["papers"].append({
        "number": 6, "title": "Machine-Speed Economics",
        "subtitle": "A technical blueprint of the machine-speed economy",
        "version": "draft v0.1", "date": "2026-10", "status": "draft",
        "path": "papers/06-machine-speed-economics",
        "markdown": "papers/06-machine-speed-economics/manuscript/paper-06-draft.md",
    })
    manifest["papers"].append({
        "number": 7, "title": "The Metered Mind",
        "subtitle": "Micropayments and licensing economics of machine-speed judgment",
        "version": "outline brief", "date": "2026-10", "status": "brief",
        "path": "papers/07-the-metered-mind",
        "markdown": "papers/07-the-metered-mind/brief/brief.md",
    })
    with open(os.path.join(ROOT, "papers.json"), "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    print("wrote papers.json")


if __name__ == "__main__":
    for p in PAPERS:
        install_paper(p)
    install_paper6()
    install_paper7()
    write_manifest()
