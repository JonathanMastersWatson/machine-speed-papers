# Executive Summary

## Execution-Boundary Governance: A Runtime Control Model for Autonomous Systems

**Jonathan M. Watson** | Independent Researcher | jonmwatson@gmail.com  
**Version 2.0 — July 1, 2026**

---

## The panel has never mentioned the speed of light.

Walk into any AI governance conference today.

You will find serious, credentialed people discussing accountability frameworks,
transparency requirements, human oversight mechanisms, and responsible AI
principles. They will reference NIST. They will cite the EU AI Act. They will
debate model cards and impact assessments and audit obligations.

Not one of them will mention the speed of light.

That omission is not accidental. It reflects the foundational assumption baked
into every governance framework on the table: that time is not a variable.
That governance can happen whenever governance happens, and the action will
wait.

Autonomous systems do not wait.

---

## What AI governance actually is right now

Look past the frameworks and examine what AI governance is in practice.

It is a stack of PDFs.

Lengthy, carefully drafted, genuinely well-intentioned PDFs — published by
standards bodies, regulatory agencies, and national governments — built on
yesterday's cloud stack. Policies living in document management systems.
Controls evaluated by humans reading reports. Audit cycles running quarterly.
Oversight mechanisms designed for systems that wait for a human to initiate
the next step.

Ambiguous by design — because ambiguity is a feature of human governance.
It allows judgment to fill the gaps. A compliance officer reads the situation,
weighs the context, decides what the rule means in this particular case.
A committee interprets. A review cycle applies. An auditor confirms.

This works beautifully at human speed.

At machine speed it produces nothing.

Because ambiguity requires deliberation. Deliberation requires time. And time
is precisely what the execution boundary does not provide.

The governance stack is not wrong. It is late. It was built for the systems
that existed when it was written. The problem is that the substrate has changed
underneath it — and the frameworks have not.

---

## The evidence is already here

You may be thinking: I build agents. I do not see this problem.

That is probably true — today.

Most agents currently in production operate in low-consequence environments.
They retrieve documents. They summarize content. They draft responses for human
review. They query APIs. These are reversible, local, limited-impact actions
where the cost of error is low and governance can afford to be slow.

But the signals from the boundary cases are already visible.

Agents have deleted production databases. Autonomous systems have triggered
unintended financial transactions. AI-driven workflows have modified records
in ways that could not be cleanly reversed. These are not hypotheticals.
They are incidents — most of them unreported, some of them expensive, a few
of them catastrophic enough to attract attention.

More telling: the insurance market is moving.

QBE and Beazley have introduced sublimits on AI-linked losses. ISO and Verisk
have filed generative AI exclusion endorsements effective January 2026. The
industry's standard response to a risk it cannot price is exclusion — and
exclusion is exactly what is happening.

Underwriters are not pulling back because they read a governance framework
and found it inadequate. They are pulling back because they cannot observe
governance presence at the point of consequence. They cannot verify that a
control existed at the moment the action committed. The audit trail tells them
what happened. It cannot tell them that governance was present before it
happened.

That distinction — between a record that is consistent with control and a
record that proves it — is the commercial gap the insurance market is now
pricing.

---

## The latency condition

There is a formal way to state the underlying problem:

**Governance latency must be less than action latency.**

Governance latency is the time required to evaluate whether an action is
admissible. Action latency is the time available before that action commits
to consequence.

When governance latency is less than action latency, governance can influence
outcomes. It operates before commitment. It can allow, deny, or defer.

When governance latency exceeds action latency, governance cannot influence
outcomes. It can only observe them.

This is the latency condition. It is binary. There is no partial credit for
almost completing in time. An action that commits before admissibility is
determined is an ungoverned action — regardless of how sophisticated the
governance system that follows it.

Not one current AI governance framework acknowledges this condition exists.

---

## Where this applies — and where it does not

Not every agent needs execution-boundary governance. This framework is not
a mandate for maximum-intensity controls on every autonomous system regardless
of what it does.

This paper proposes a three-tier consequence classification:

**Low consequence** — reversible, local, limited human impact. Reading files.
Querying APIs. Drafting content for human review. These actions warrant
governance presence but the determination is lightweight. Most agents built
today operate here. The framework is not aimed at them.

**High consequence** — irreversible, externally visible, regulated, or
materially impactful. Moving funds. Modifying records. Sending communications
on behalf of a principal. Accessing protected data. Executing contracts.
These actions require full governance evaluation at the execution boundary.

**Sovereign consequence** — systemic, cross-jurisdictional, infrastructure-
level, or capable of cascading effects at population scale. These require the
highest governance intensity, including human escalation before execution
regardless of how well the compiled policy is written.

The governance architecture proposed in this paper is calibrated to consequence,
not capability. The question is not what an agent *can* do. It is what an agent
*is doing* at the moment it acts.

If you are building agents today that stay in the low-consequence tier, this
framework is your early warning system. The moment your agents gain access to
financial systems, regulated data, external APIs with write access, or
infrastructure controls — the consequence classification shifts. The governance
architecture needs to be in place before that crossing happens, not after.

---

## The machine-speed economy

The near-term problem is individual agents crossing consequence thresholds.

The medium-term problem is larger.

Agents are beginning to transact with agents. Orchestration frameworks
coordinate fleets of specialized agents, each calling others as tools, each
receiving outputs that become inputs to subsequent consequential actions, each
operating without human initiation or review at the individual transaction
level.

When all participants are autonomous, transaction velocity is bounded only by
infrastructure. No human compliance officer can review a transaction that
completes in 12 milliseconds. No audit committee can convene between the
proposal and the commitment of an action that executes in the time it takes
light to cross a city.

Human-speed pricing breaks. Monthly subscriptions and per-seat licenses were
designed for human consumption patterns. An agent invoking a platform thousands
of times per hour at machine speed accumulates fee burdens that make the
economics unworkable — or forces operators to route around the fee structures
in ways that also route around the governance that fee structures implicitly
assumed.

Human-speed compliance breaks. Audit cycles designed for quarterly review
cannot catch errors that compound across thousands of machine-speed
transactions before the quarter ends.

Human-speed liability breaks. When agents chain across agent boundaries —
Agent A instructing Agent B instructing Agent C to take a consequential action
— the question of who had control at the moment the action committed becomes
legally incoherent without a defined execution boundary and the evidence to
prove what occurred there.

The machine-speed economy is not arriving. It is assembling itself, right now,
in production environments, faster than any governance framework currently
in development can track.

---

## The physics argument — why this gets worse, not better

For most agents currently in production, the latency condition is not yet
binding. Agents running behind firewalls or on local hyperscalers have
governance infrastructure close enough to satisfy any reasonable latency
budget. The round-trip to a governance check is milliseconds. The action
latency window is comfortably larger.

This will not remain true.

As inference hardware improves, as agent architectures mature, as
orchestration frameworks compress the intervals between reasoning and
execution, action latency will shrink. The governance window that is
comfortable today will become tight tomorrow and binding the day after.

And the physics do not reverse.

The speed of light imposes a hard lower bound on round-trip latency between
any two points separated by physical distance. A governance check requiring
a round trip to infrastructure on another continent cannot complete in under
130 milliseconds regardless of software performance. As action latency
compresses toward single-digit milliseconds — the operating envelope of the
next generation of agentic systems — cloud-hosted governance becomes
physically incapable of satisfying the latency condition.

Not slower. Physically incapable.

The governance architecture you build today will govern tomorrow's systems.
If that architecture assumes a comfortable latency window, it will fail
precisely when the systems it governs become consequential enough to matter.

---

## The architecture that follows

This paper proposes **Execution-Boundary Governance (EBG)** — a framework
derived from physical constraints that apply wherever autonomous agents act
with consequence.

The central mechanism is the **Executable Governance Kernel (EGK)**: a
minimal, deterministic, tamper-resistant control point operating at the final
moment before an autonomous action commits. Five required properties:

1. **Complete mediation** within defined consequence scope
2. **Determinism** — identical inputs, identical outputs, every time
3. **Latency compatibility** — determination completes before action commits
4. **Tamper resistance** — structural isolation from the agent it governs
5. **Evidence generation** — contemporaneous proof that governance was present

The EGK is not invented here. Reference monitors implemented it in
cybersecurity in 1972. Safety kernels implement it in physical systems.
Pre-trade risk checks implement it in financial markets at microsecond
latency, at commercial scale, every trading day.

What has not existed until now is a unified treatment applying this to
autonomous AI agents — and deriving it from the physical constraints that
make machine-speed systems ungovernable by any other means.

The key architectural insight is the **Minimal Surface Principle**: the closer
governance moves to the execution boundary, the smaller it must become.
Complexity at the boundary is not safety. It is risk. Additional layers add
latency, failure modes, and probabilistic variance. The governance mechanism
that survives at the execution boundary is the smallest one capable of making
a deterministic admissibility determination within the available interval.

Governance expands upstream to handle ambiguity. At the boundary itself, it
contracts to enforce what has already been decided.

---

## The convergence

Every discipline this paper examines converges independently on the same point.

**Liability doctrine** finds that control and accountability are paired —
liability attaches where control was last possible, and in autonomous systems
that point is the execution boundary.

**Insurance underwriting** finds that coverage requires evidence of controls
at the point of consequence — and that documentation assembled after the fact
cannot prove governance was present before it.

**Economics** finds that governance imposing latency costs will be selected
against under competitive pressure — the only governance that survives is
governance cheap enough to operate at the only point that matters.

**Physics** finds that governance architecture requiring round-trips to distant
infrastructure is physically incapable of satisfying the latency condition in
a growing number of deployment configurations.

**Agent architecture** finds that governance distributed across reasoning steps
burns latency and tokens at every step that does not matter — and that
governance concentrated at the execution boundary pays its cost once, at the
only step that does.

None of these disciplines set out to find the same thing. The convergence is
not the result of coordination. It is the result of independent inquiry into
the same underlying reality.

---

## The constraint

The requirement is not invented. It was discovered.

*A determination must be made before a consequence-bearing action commits,
within a finite interval, at a point physically proximate to the execution
surface.*

This is not a policy recommendation. Not a framework preference. Not a
conference panel conclusion.

It is a constraint.

It exists whether or not it is instrumented. The governance frameworks do not
need to acknowledge it for it to apply. The panel does not need to put it on
the agenda for it to be true.

The speed of light does not wait for the committee to convene.

The window between a proposed action and a committed one is open whether or
not a governance mechanism is placed in it.

The question is whether the systems being built today will be governed at that
boundary — or whether we will discover, through the accumulation of
consequential failures in ungoverned autonomous systems, that the window was
always there and we chose not to use it.

---

## The paper

**32 chapters. 8 parts. One constraint.**

Spanning governance theory, cybersecurity, safety engineering, financial
market design, edge infrastructure, liability doctrine, and insurance
underwriting — all converging on the execution boundary as the primary
governance concept for autonomous systems operating at machine speed.

Full manuscript available in this repository and on arXiv and SSRN.

Feedback, critique, and discussion welcome via GitHub Issues or
jonmwatson@gmail.com

*Curious whether others are seeing the same convergence.*

---

*The constraint the paper identifies is not invented. It was discovered.
It exists whether or not it is instrumented.*
