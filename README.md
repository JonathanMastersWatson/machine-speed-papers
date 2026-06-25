# Execution-Boundary Governance: A Runtime Control Model for Autonomous Systems

**Version 2.0 — Working Manuscript**  
**Jonathan M. Watson** | Independent Researcher | jonmwatson@gmail.com  
**Published:** July 1, 2026  
**arXiv:** [cs.AI + cs.CY] | **SSRN:** [link]

---

## The Problem

Every major AI governance framework — NIST, ISO 42001, the EU AI Act — specifies 
what must be governed, who bears accountability, and what records must exist.

None of them specify *when* governance must occur relative to the action it is 
meant to govern.

That omission is foundational.

Autonomous systems invoke tools, modify records, move funds, and trigger workflows 
in milliseconds — without a human pause. The latency budget that governance 
mechanisms have always borrowed from human reaction time is no longer available.

Governance that cannot reach an action before it commits is not governance.  
It is narration.

---

## The Argument

This paper proposes **Execution-Boundary Governance (EBG)** — a framework 
derived from first principles that applies wherever autonomous agents act with 
consequence.

**The latency condition:** Governance latency must be less than action latency. 
When this condition fails, governance becomes observational. No framework 
currently acknowledges this condition exists.

**The execution boundary:** The final deterministic control point immediately 
preceding an autonomous action — the only moment at which a determination can 
still causally influence whether an action occurs. Prior art implements this 
concept under different names in cybersecurity (reference monitor), safety 
engineering (safety kernel), and financial markets (pre-trade risk check). No 
unified treatment has existed for autonomous AI agents operating across domains.

**The Executable Governance Kernel (EGK):** A minimal, deterministic, 
tamper-resistant mechanism that must satisfy five properties:

1. Complete mediation within defined consequence scope
2. Determinism
3. Latency compatibility
4. Tamper resistance
5. Evidence generation

**Seven claims** are advanced and defended across 32 chapters:

1. Existing AI governance frameworks contain no latency model
2. Governance effectiveness is formally bounded by the latency condition
3. Human institutions subsidized governance with human decision latency — 
   a subsidy autonomous systems cancel
4. The transition to executable governance requires governance compilation
5. The EGK must be minimal rather than layered
6. Liability naturally converges on the execution boundary
7. Insurance underwriting will require execution-time evidence, not 
   post-hoc documentation

---

## Why This Matters Now

Three independent developments are converging simultaneously:

- **Agent systems** are executing consequential actions at machine speed without 
  human pause
- **Edge compute infrastructure** (telco MEC, 5G) now provides the physical 
  substrate for locally deployed governance kernels within the 25ms action 
  latency envelope
- **Insurance and liability markets** are actively searching for execution-time 
  evidence infrastructure — the gap between what underwriters need and what 
  current governance produces is becoming a commercial problem

The constraint this paper identifies is not invented. It was discovered. It 
exists whether or not it is instrumented.

---

## Structure

| Part | Chapters | Topic |
|------|----------|-------|
| I | 1–4 | The Human-Speed Economy and Its End |
| II | 5–8 | Time, Latency, and Selection Pressure |
| III | 9–14A | Interpretive vs Executable Governance |
| IV | 15–19 | The Execution Boundary and EGK |
| V | 20–22 | Locality, Edge Compute, and Physics |
| VI | 23–24 | Machine-Speed Markets and Regulatory Convergence |
| VII | 25–28 | Evidence, Liability, and Underwriting |
| VIII | 29–31 | Prior Art, Objections, and Limitations |
| — | 32 | The Constraint Beneath the Frameworks |

**32 chapters. 8 parts. One constraint.**

---

## Key Concepts

**Human latency subsidy** — The unearned latency budget governance mechanisms 
borrowed from the human pause between intention and action. Autonomous systems 
cancel it.

**Time-domain mismatch** — Human governance and autonomous execution operate 
in structurally incompatible time domains. The solution is not faster governance. 
It is translation.

**Governance compilation** — The transformation of human-readable policy into 
machine-enforceable constraints before the execution boundary is reached.

**Authority migration** — When governance cannot reach the execution surface, 
authority relocates to whoever controls that surface, regardless of where policy 
intended it to sit.

**Minimal Surface Principle** — The closer governance moves to the execution 
boundary, the smaller the governance mechanism must become. Complexity at the 
boundary is not safety. It is risk.

**Execution evidence** — A contemporaneous, tamper-evident record produced at 
the moment of each governance determination. Categorically distinct from audit 
logs. The foundational artifact for liability attribution, insurance underwriting, 
and regulatory compliance.

---

## Files

| File | Description |
|------|-------------|
| `paper/Execution-Boundary-Governance-V2.0.pdf` | Full manuscript (32 chapters) |
| `executive-summary/Executive-Summary.pdf` | Standalone 1-2 page summary |
| `figures/` | Key diagrams |

---

## Citation

```bibtex
@techreport{watson2026ebg,
  title     = {Execution-Boundary Governance: A Runtime Control Model 
               for Autonomous Systems},
  author    = {Watson, Jonathan M.},
  year      = {2026},
  month     = {July},
  note      = {Version 2.0. Independent Research Working Paper.},
  url       = {https://github.com/JonathanMastersWatson/execution-boundary-governance}
}
```

---

## Engagement

This is a working paper. Feedback, critique, and discussion are welcome.

- **Open an Issue** on this repo for questions or comments
- **Connect on LinkedIn:** [Jonathan M. Watson](https://linkedin.com/in/jonmwatson)
- **Email:** jonmwatson@gmail.com

Curious whether others are seeing the same convergence.

---

## License

This work is licensed under  
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

You are free to share and adapt this material for any purpose, provided you 
give appropriate credit to the author.

---

*The window is open whether or not you place a kernel in it.*
