# The Machine Speed Papers

**Jonathan M. Watson** — Independent Researcher

A multi-paper research program examining what happens when decision-making, execution, commerce, governance, and coordination transition from human-speed systems to machine-speed systems.

The objective is not to advocate for a specific technology, product, company, protocol, implementation, or political outcome. It is to identify the structural realities that emerge when machines acquire the ability to make decisions, execute actions, transact economically, coordinate with other machines, and operate at speeds beyond human supervision.

The central question:

> What institutional, technical, legal, economic, and governance structures become necessary once execution occurs at machine speed?

## The series

| No. | Paper | Status |
|-----|-------|--------|
| 0 | [The Industrialization of Cognition](papers/00-the-industrialization-of-cognition/) — *Transformed* (V0.1) | Executive-summary placeholder |
| 1 | [Execution-Boundary Governance](papers/01-execution-boundary-governance/) — *A Runtime Control Model for Autonomous Systems* (V2.1) | Published |
| 2 | [Constitutional Compression](papers/02-constitutional-compression/) — *The Emergence of Minimal Governance at Machine Speed* (V1.1) | Published |
| 3 | [Evidence Systems](papers/03-evidence-systems/) — *Why Independent Witnesses Emerge at Machine Speed* (V1.1) | Published |
| 4 | [Upstream](papers/04-upstream/) — *Where Human-in-the-Loop Goes at Machine Speed* (V1.1) | Published |
| 5 | [The Execution Surface](papers/05-the-execution-surface/) — *Why Distributed Compute Cannot Be Shared* (V1.1) | Published |
| 6 | [Machine-Speed Economics](papers/06-machine-speed-economics/) — *How Evidence Becomes the Price Signal* (V0.2) | Draft |
| 7 | [The Metered Mind](papers/07-the-metered-mind/) — *Micropayments and licensing economics of machine-speed judgment* | Outline brief |

The arc: governance doesn't disappear at machine speed — it redistributes. Interpretation moves upstream, enforcement compresses to a minimal kernel at the execution boundary, and accountability moves downstream into independently witnessed evidence. Paper Zero opens the frame; Papers 1–5 establish the components; Paper 6 assembles the running machine; Paper 7 follows the money to the individual.

## Repository layout

```
papers/
  00-the-industrialization-of-cognition/   # placeholder (full paper in progress)
  01-execution-boundary-governance/
  02-constitutional-compression/
  03-evidence-systems/
  04-upstream/
  05-the-execution-surface/
  06-machine-speed-economics/      # draft in progress
  07-the-metered-mind/             # outline brief
```

Each published paper folder contains:

- `paper.pdf` — the canonical paper (this is the version of record)
- `paper.md` — machine-readable text derived from the PDF
- `abstract.md` — abstract / entry point
- `figures/` — figures and diagrams (where present)
- `executive-summary/` — executive summary (where present)
- `outreach/` — launch and announcement material; public history, not part of the paper
- `CHANGELOG.md` — version history

Machine-readable series metadata (titles, versions, abstracts, SHA-256 hashes of the canonical PDFs) lives in [`papers.json`](papers.json). Citation metadata lives in [`CITATION.cff`](CITATION.cff).

## License

CC BY 4.0 — share and adapt freely, even commercially, with attribution to Jonathan M. Watson. See [LICENSE](LICENSE).

## Cite

Watson, J.M. (2026). *The Machine Speed Papers.* https://github.com/JonathanMastersWatson/machine-speed-papers

Per-paper citations are listed in each paper's README.
