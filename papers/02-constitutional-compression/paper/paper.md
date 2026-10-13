---
title: "Constitutional Compression"
subtitle: "The Emergence of Minimal Governance at Machine Speed"
paper_number: 2
version: "1.1"
author: "Jonathan M. Watson"
date: "2026-07"
series: "The Machine Speed Papers"
canonical_pdf: "paper.pdf"
license: "CC-BY-4.0"
---

# Constitutional Compression

*The Emergence of Minimal Governance at Machine Speed*

**Jonathan M. Watson** — The Machine Speed Papers, No. 2 — Version 1.1 — 2026-07

---

*Machine-readable text derived from the canonical PDF (`paper.pdf`). In case of any discrepancy, the PDF governs.*

*Note: the PDF title page states version 1.0; this file is released as version 1.1.*

## Chapter 1 — The Question

What survives when governance is exposed to machine-speed execution?
This is not a question about artificial intelligence, though artificial intelligence is what
made it urgent. It is a question about governance itself — what governance actually is,
once the conditions that gave it its familiar shape are removed.
For nearly the whole of institutional history, governance operated inside a generous
window of time. A decision was proposed. A period passed — minutes, days, sometimes years — during which the proposal could be examined, argued, revised, or rejected. Courts deliberated. Committees convened. Regulators reviewed. The interval
between a consequential action being proposed and that action taking effect was large
enough to hold a great deal of human judgment.
That interval is now, in a growing number of domains, gone.
An autonomous system can propose and commit a consequential action — a transaction, a record change, a physical movement — faster than any human process could
intervene. Not faster than a slow human process. Faster than the fastest one that could
exist. The constraint is not institutional design. It is machine execution outrunning
the architecture of human cognition, and human cognition is, in this contest, no longer
waiting to be asked.
Most accounts of governance assume the entity exercising judgment has time to exercise
it. Remove that assumption, and most of what we call governance turns out to have
needed it all along — quietly, never stated.
This paper does not ask how to make human governance faster. That has an answer,
and the answer is no. Speed isn’t the obstacle. What makes human judgment valuable
— weighing context, applying principle to a case no rule anticipated, being persuaded
by argument — cannot be separated from the time that judgment takes. A faster version
of deliberation is not deliberation working eﬀiciently. It is deliberation that has stopped
deliberating.
The question this paper asks instead is what remains of governance once judgment is
no longer available at the point of action — and whether what remains is governance
degraded, or governance reduced to what it actually is.
This is a discovery, not an assumption. It starts from one observed condition — action
now frequently outpaces the human capacity to evaluate it — and follows the consequences through several domains: physics, where distance imposes cost that cannot be
engineered away; computation, where a system can only verify what it can formally
check; economics, where competitive pressure eliminates whatever it cannot afford;
law, where liability has always followed control; and constitutional theory, where authority has always required a basis to be legitimate.
Each domain, approached independently, arrives at a similar answer. That convergence
is the evidence. No single domain carries the argument alone.

The Transition Already Underway
This is not a hypothetical future. It is already in motion, and naming where it stands is
worth a moment before the derivation begins.
For most of the history of computing, governance operated outside the execution path.
Human review, workflow approval, and organizational process all existed before an
action occurred — separate from the system doing the acting, consulted before it was
permitted to proceed.
As systems became more autonomous, governance moved closer to execution. Approval workflows became policy engines. Policy engines became runtime controls. Runtime controls increasingly evaluate actions immediately before they occur, rather than
reviewing them sometime after. The trend is visible across industries and technologies,
independent of any particular implementation. Governance is moving toward execution. It has been for some time.
What remains unresolved is not whether governance belongs at runtime. That question
is largely settled — the industry has converged on it without needing to argue the point.
What remains unresolved is what governance actually becomes, once it arrives there.
Runtime governance has been discovered.
The minimal mechanism inside runtime governance has not.
This paper investigates that question — not by surveying what currently exists, but by
deriving what must.
The chapters that follow are structured around it. Chapter 2 shows why interpretive
governance cannot simply continue at machine speed. Chapter 3 makes the paper’s
central discovery: governance does not disappear under this pressure, it redistributes
— interpretation moving upstream, enforcement compressing to a single point, accountability moving downstream. Chapter 4 examines the execution boundary itself: the
precise moment a proposed action becomes a committed one, and why this moment is
the only one at which governance can still be causal rather than descriptive. Chapter 5
asks whether a reasoning system can fill that moment, and shows why it cannot. Chapter 6 follows the compression to its end point: a minimal executable governance core.
Chapter 7 asks what kind of thing that core actually is. Chapter 8 takes the strongest
objections to this argument seriously, on their own terms. Chapter 9 concludes.
None of this depends on any particular technology, company, or product. The paper is
not an argument for something to be built. It is an argument that a structural shift is
already underway in what governance can be — that the shift follows from constraints
no policy can override — and that the architecture this shift produces deserves to be
understood clearly before it is built carelessly.
The constraint this paper describes was not invented for the purpose of describing it. It
exists, or it does not, independent of whether anyone writes it down. What follows is
an attempt to get it right.

## Chapter 2 — Why Interpretive Governance Cannot Simply Continue

Every governance mechanism in human institutions assumes one thing: there is time
between a decision being proposed and that decision taking effect.
Reviews need time. Appeal needs time. Audit needs time. None of these mechanisms
work through speed. They work by consuming an interval — examining a proposal
before it becomes final.
For most of history, this interval was abundant. A human initiates every consequential
action, and a human does not act instantly. Between intention and execution, there
was always a pause. Within that pause, governance happened — quietly, automatically,
without anyone designing it that way.
Call this the human latency subsidy. Governance has always borrowed time from the
fact that a human was the one acting. The subsidy was never priced, because it was
never visible.
Autonomous systems remove it.
When an agent initiates an action, there is no pause. No click. No moment of hesitation
before execution, because nothing requires one. The subsidy is gone — not reduced,
gone — and governance built on top of it loses its foundation.1
That is the first problem. It is not the only one.
The second problem is that interpretive governance does not just need time. It needs
judgment — the capacity to weigh context and apply a general rule to a specific case
no one fully anticipated. Judgment is not a calculation that gets faster with better hardware. Compress it into milliseconds and it does not become a faster judgment. It becomes something else wearing judgment’s name — a reflex, a guess, a coin flip in legal
clothing.
This is not a flaw in interpretive governance. It is a feature, built for an interval that has,
until now, always been there. Remove the interval and the feature does not become
faulty. It becomes inapplicable.
The third problem is volume. Even where a pause could be reinserted, a human reviewer examining one proposal carefully cannot examine the millionth proposal of the
day with the same care. Not from any failing — from the simple fact that attention does
not scale the way computation does. An autonomous system proposing a thousand actions in the time it takes to read one of them has not just shortened the interval. It has
exceeded the total reviewing capacity that exists.
This is a time-domain mismatch. Not a performance gap that better resourcing closes. A
domain incompatibility. Human governance is built for a domain measured in minutes,
     The absence of a human pause in autonomous agent execution is documented in Yao, S., Zhao, J.,
Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting
in language models. International Conference on Learning Representations (ICLR 2023) — which establishes
the architecture by which agents chain reasoning and execution steps without human initiation or review
at each step. Throughput and action frequency data for autonomous agents is documented in Wang, L.,
Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., … & Wen, J.R. (2024). A survey on large language model
based autonomous agents. Frontiers of Computer Science, 18(6).

hours, days. Autonomous execution operates in a domain measured in fractions of a
second. These are not the same domain at different speeds. They are different domains.
A mechanism built for one does not degrade gracefully in the other. It does not produce
a worse answer. It produces nothing, because by the time it starts, the window has
already closed.
None of this means interpretive governance has failed. It remains the only known mechanism for producing judgment — weighing context, applying principle to novel fact,
building legitimacy through visible deliberation. Nothing here replaces that.
What this chapter establishes is narrower: interpretive governance cannot operate at the
execution boundary, because the conditions it depends on — time, unhurried judgment,
manageable volume — are absent there. Not weak. Absent.
This leaves one question. If the place where actions actually commit cannot be governed by the mechanism that has always governed everything else, what happens to
that mechanism?
It does not disappear. It moves.
Where it moves, and what takes its place at the boundary, is the subject of the next
chapter.

## Chapter 3 — Governance Redistributes

Governance under machine-speed pressure does not vanish. It moves.
This is the central discovery of this paper, and it is worth stating plainly before it is examined in detail: when the interval that interpretive governance depends on disappears,
the functions that interval used to support do not disappear with it. They relocate to
places where the interval still exists.
There are three functions to track, and each goes somewhere different.
The first function is interpretation — the work of reading ambiguous language, weighing context, and deciding what a rule should mean in a case its authors did not precisely
foresee. This function requires time and judgment, and the execution boundary offers
neither. So interpretation moves upstream, into the process that produces policy before
any action is ever proposed. A human being still decides what “reasonable” means.
They simply decide it in advance, once, for the category of case rather than the instance
— and that decision is then compiled into a form that does not require re-interpretation
every time a similar case arises.
The second function is enforcement — the act of checking a proposed action against the
rule and permitting or denying it. This function does not move upstream, because it
cannot. It has to happen at the moment the action is proposed, or it does not happen
at all. What changes is not enforcement’s location but its size. Stripped of the need
to interpret — because interpretation has already happened upstream — enforcement
compresses to the smallest possible operation: compare the proposed action against the
compiled rule, return permit or deny. Nothing else fits in the time available.

The third function is accountability — the work of recording what happened, attributing responsibility, and supporting review after the fact. This function also requires time,
and the execution boundary does not provide it either. So accountability moves downstream, into evidence generated at the moment of the decision and examined afterward,
at whatever pace the examining process requires. Courts, auditors, and regulators continue to operate at human speed. They now operate on a record rather than on the
action itself.
Put together, this is the shape governance takes once compressed by machine-speed
conditions:
Interpretation happens before the action, slowly, by humans. Enforcement happens at
the action, instantly, by a minimal mechanism with no interpretive capacity of its own.
Accountability happens after the action, slowly, by humans, examining a record the
enforcement step left behind.
Nothing in this sequence requires fewer total decisions than interpretive governance required before. If anything, it requires more — because every case that would once have
been handled by discretion at the point of action must now be anticipated, in advance,
by whoever compiles the policy. What has changed is not the amount of governance.
It is where each piece of it has to live.
This matters because the most common misreading of compression is to treat it as simplification. It is not simplification. It is redistribution under a hard constraint: only the
enforcement function can survive at the execution boundary, because only enforcement
can be done without time. Everything else has nowhere to live except before or after
that boundary, and so that is where it goes.
It is also worth being precise about what does not survive the move. Some properties of interpretive governance are tied to the location, not just the function. Discretion
exercised at the point of action — a human looking at this specific case, in this specific moment, and deciding what fairness requires here — has no upstream equivalent.
The upstream process can anticipate categories of case. It cannot anticipate every case.
Some genuinely novel situations will arrive at the execution boundary with no compiled rule that fits them cleanly. What happens then is addressed later in this paper.
For now, it is enough to note that this is a real cost of compression, not a detail that
resolves itself. Whatever record exists to show that a determination was reached correctly — what was decided, on what basis, when — has the same problem discretion
does. Proof requires time that discretion does not — and that puts it on the downstream
side of the boundary, with everything else accountability already claimed.
The redistribution described in this chapter is not a design choice. It is the shape governance is left with once one fact is accepted: that some actions now commit faster than
any human process can evaluate them, and that fact does not change because it is inconvenient. Given that fact, interpretation has nowhere to go but upstream. Accountability
has nowhere to go but downstream. And enforcement has nowhere to go but into the
single, narrow moment between proposal and consequence — compressed to whatever
can survive being done with no time at all.

That moment is the subject of the next chapter.

## Chapter 4 — The Execution Boundary

There is a precise moment, inside every consequential autonomous action, that governance theory has not had a name for.
It is not the moment a system begins reasoning about what to do. It is not the moment
a policy is written, or a rule compiled, or a risk reviewed. It is the moment immediately
before an action commits — the last instant in which two futures are still both possible:
one in which the action happens, and one in which it does not.
After that instant, only one future remains.
This paper calls that instant the execution boundary. It is not a metaphor. It is the specific, locatable point in a system’s operation where a proposed action either becomes
real or does not. Before it, everything is still preparation. After it, everything is consequence. The boundary itself is the only place where a determination can still change
the outcome.
This gives the execution boundary four properties that distinguish it from every other
point in a system’s operation.
It is singular. For any given action, there is exactly one moment at which the choice
between occurrence and non-occurrence is still open. Governance applied before that
moment is preparation. Governance applied after it is documentation. Only governance applied at the boundary itself is control.
It is precise. The boundary is not a fuzzy zone or an approximate window. It is the
exact point at which a proposed action becomes an executed one — identifiable, instrumentable, enforceable. This precision is what makes the boundary governable at all. A
vague boundary cannot be checked. A precise one can.
It is consequential. The boundary only exists for actions that matter — actions that
change a state of the world, commit a resource, or produce an effect that cannot be
casually reversed. An action with no real consequence has no meaningful boundary,
because nothing follows from it that requires governing.
It is the only place enforcement can occur. Not the only place governance happens —
interpretation happens before it, accountability happens after it — but the only place
where the specific act of permitting or denying can still matter. Everywhere else, the
decision has either not yet been needed or has already stopped mattering.
This is the precise sense in which the redistribution described in the previous chapter is not optional. Interpretation and accountability have room to operate across long
stretches of time, before and after the action. Enforcement has exactly one moment, and
that moment is the execution boundary. There is no second chance to place it. Either
something is present at that instant, evaluating the action before it commits, or nothing is — and an action that commits without anything evaluating it first is, regardless

of what governance exists around it, an ungoverned action at the only point where it
mattered.
This distinction — control versus documentation — is worth making sharply, because
it is the one most governance frameworks blur without noticing.
A system that records what an autonomous agent did, after it did it, has produced a log.
The log can be detailed. It can be timestamped, structured, even legally useful. But it
did not prevent anything, because by the time it was written, the thing it describes had
already happened. This is narrative governance: documentation that arrives too late to
be causal, however well it is built.
A system that evaluates a proposed action before it commits, and permits or denies it
on that basis, has done something categorically different. It has not merely described
an outcome. It has participated in determining which outcome occurred. This is controlling governance — and it is only possible at the execution boundary, because that
is the only point at which both outcomes are still available to choose between.
Most current AI governance is narrative.2 This is not a criticism of intent. It is a direct consequence of where governance has historically been placed — usually after the
action, because that is where humans have always been positioned to look. The execution boundary requires governance to be present before, not after, and very little existing
infrastructure was built with that requirement in mind.
The implication is not that documentation is worthless. Documentation supports the
accountability function described in the previous chapter, and accountability remains
essential. The implication is narrower and harder to avoid: documentation is not control, no matter how complete it is, and a governance architecture that only documents
has not governed the moment that mattered. It has only described it afterward.
The execution boundary is where that distinction becomes unavoidable. It is the place
where governance either happens, or it does not — with no further chance to revisit the
question once the action has passed through it.
What can actually occupy that boundary, given everything established in the previous
two chapters about the conditions it imposes, is the subject of the next chapter.

     The characterization of current AI governance as primarily documentary rather than controlling is
supported by two independent assessments. Varma, S. (2026). Gartner Says Applying Uniform Governance Across AI Agents Will Lead to Enterprise AI Agent Failure. Gartner Newsroom, May 26, 2026 —
finding that 40% of enterprises will demote or decommission agents by 2027 specifically because governance models do not match autonomy levels. ISACA (2026). AI Use Accelerates, While Governance and ROI
Lag. ISACA AI Pulse Poll, May 5, 2026 — reporting that only 38% of organizations have a comprehensive
AI policy and 39% do not know whether an override process exists for their AI systems.

## Chapter 5 — Why a Reasoning System Cannot Sit at the Boundary

Something has to occupy the execution boundary. The previous chapter established
that this is the only point where enforcement can happen, and that nothing happening
there means the action proceeds ungoverned. The question this chapter asks is what
kind of thing can actually do that job.
The obvious candidate, in an age increasingly built around them, is a reasoning system
— a model that looks at a proposed action and produces a judgment about whether it
should proceed. This candidate fails, and it is worth being precise about exactly why,
because the failure is not a matter of current technology being insuﬀiciently advanced.
It is structural. No future improvement in reasoning systems resolves it, because the
problem is not a deficiency in reasoning. It is a mismatch between what reasoning is
and what the execution boundary requires.
The execution boundary imposes four requirements simultaneously. A mechanism sitting there must be fast enough to complete within whatever interval the action allows.
It must produce the same output every time it is given the same input. It must produce a determination capable of supporting a record that can be checked and trusted
after the fact — whether or not the mechanism itself generates that record. And it must
fail in a safe direction — denying, not permitting — when something prevents it from
completing its evaluation. These are not four independent preferences. They are four
conditions that must all hold at once, because the boundary does not allow trading one
off against another.
A reasoning system cannot satisfy all four.
Speed is the most visible failure. Reasoning — even fast reasoning — takes time proportional to the complexity of what it is reasoning about, and that time does not shrink to
zero. At meaningful transaction volume, the cumulative cost of reasoning about every
proposed action exceeds what any system can sustain.3 This alone would be enough to
disqualify reasoning from the boundary even if nothing else were wrong with it.
There is also a cost argument that compounds the speed argument rather than merely
restating it. Every inference call consumes tokens. A compressed model, a distilled
model, a purpose-built mini-model optimized specifically for boundary evaluation —
each still consumes tokens per call, because token consumption is not a function of
model size alone. It is a function of having performed inference at all. Multiply a minimal per-call token cost across the transaction volume of any serious deployment —
thousands of calls per second, millions per day — and the economic consequence is not
a rounding error. It is a structural tax on every governed action, accumulating continuously, scaling with volume, with no floor below which it disappears. A deterministic
kernel evaluating compiled Boolean expressions consumes no tokens. It consumes CPU

      Production agentic system latency benchmarks are documented in Cisco Systems Engineering Team
(2026). BRKSPG-1180: Advanced Network Architectures for LLM Ingestion. Cisco Live EMEA, February
2026, which documents tool-call latency envelopes of 25–100ms in production agentic architectures; and
LangChain (2026). SmithDB Inverted Index Performance Benchmarks. LangChain Platform, May 13, 2026,
reporting P50 trace latencies of 71–92ms for agentic workflows in production environments.

cycles, at a cost orders of magnitude smaller and falling.4 The economic selection argument from Chapter 1 applies here with full force: governance architectures that impose
a per-transaction cost at the boundary will be displaced, under competitive pressure, by
architectures that do not. Token burn at the boundary is not an engineering ineﬀiciency
waiting to be optimized away. It is an inherent property of inference, and inference is
what reasoning systems do.
But something else is wrong with it. Reasoning systems are not deterministic in the
way the boundary requires. The same input does not reliably produce the same output,
because the mechanism is probabilistic by design — that is part of what makes it useful
for the tasks it is good at. At the execution boundary, this property becomes a liability
rather than a strength. A determination that might come out differently if asked again
is not a determination a system can be governed by. It is a guess that happened to be
written down.
This has a direct consequence for evidence. The accountability function described
in Chapter 3 depends on a record that can be examined and trusted after the fact —
a record that proves a specific determination was reached, on specific grounds, and
would be reached again under the same conditions. A reasoning system’s output
does not support this. It can be logged, but the log proves only that something was
generated, not that the same evaluation would recur if it mattered. This is not a minor
technical gap. It is the difference between evidence and a transcript.
There is a final problem, less obvious than the first three but more serious. A reasoning
system evaluating whether to permit an action is, by virtue of reasoning at all, also a
system that can be reasoned with. It can be presented with framing, context, or argument designed to shift its output. This is not a hypothetical vulnerability. It is the same
property that makes reasoning systems useful elsewhere — the capacity to be moved
by an argument — turned into an attack surface at the one point in the system where
that capacity is actively dangerous. A mechanism that enforces a constraint should not
be persuadable. The execution boundary requires something that evaluates, not something that can be argued with.
None of this means that reasoning has no place in the architecture this paper describes.
It has a place — the place established in Chapter 3, upstream, where policy is interpreted, debated, and compiled before any action is proposed. Reasoning is exactly the
right tool for that work. It is slow enough to be careful, and being persuadable is not a
flaw there — it is the entire point of deliberation. The objection is not to reasoning. It is
to reasoning occupying a position that requires the opposite of what reasoning is good
at.

     Token consumption as a structural cost of inference-based systems is documented in Yao, S., Zhao, J.,
Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in
language models. International Conference on Learning Representations (ICLR 2023); and Wang, L., Ma, C.,
Feng, X., Zhang, Z., Yang, H., Zhang, J., … & Wen, J.R. (2024). A survey on large language model based
autonomous agents. Frontiers of Computer Science, 18(6) — both documenting that inference-based governance evaluation at every agent step compounds token consumption multiplicatively across workflow
steps.

This produces a clean division of labor, not a demotion of either side. Reasoning belongs
where time is available, and persuasion is appropriate. Enforcement belongs at the
boundary, where neither is available, and where the only thing that can function is
something that does not reason at all — something that simply checks a proposed action
against a rule decided in advance, and returns one of two answers.
What that something actually looks like, stripped down to whatever can survive these
four requirements simultaneously, is the subject of the next chapter.

## Chapter 6 — The Minimal Kernel

If a reasoning system cannot occupy the execution boundary, something else has to.
This chapter asks what that something actually is — not as a design preference, but
as whatever remains once every requirement from the previous two chapters is taken
seriously at the same time, and nothing else.
Start from what governance, stripped to its irreducible function, actually is: the exercise
of authority to permit or forbid. Not record what was permitted. Not prove later that
it was permitted correctly. Permit or forbid, at the moment it matters. Everything that
follows is derived by asking what this function requires in order to exist at all — not
what would make it trustworthy, not what would make it auditable, not what would
make it eﬀicient at scale. Those are real and important questions. They are not this
question.
Six things turn out to be irreducible.
There must be a proposed action — something to govern. Without it, there is nothing
for any of what follows to apply to.
There must be a compiled standard — the basis the proposal is measured against. Without a standard, permit or forbid has no foundation. It would be arbitrary, which is not
governance. It is chance wearing governance’s clothes.
There must be an authority check — confirmation that the entity proposing the action
has standing to propose it. This is not a courtesy and it is not a subset of the standard
above, even though it can look that way at first. A standard answers is this action permitted, in general. Authority answers a separate question: is this specific entity permitted
to ask. Collapsing the two creates a single point of failure where an attacker only has to
defeat one check instead of two.
There must be an evaluation act — the actual comparison of the proposal against the
standard and the authority context. A standard that exists but is never applied governs
nothing.
There must be a binding output — permit or deny, and critically, an output the rest
of the system actually obeys. A determination that can be ignored downstream is not
governance. It is a recommendation.
And there must be fail-safe behavior — a defined, pre-declared response when the
evaluation cannot complete. Without this, a kernel that crashes, stalls, or is starved of

what it needs to finish its evaluation does not fail loudly. It fails silently, into whichever
direction the surrounding system happens to default to. The requirement is that a default exists and was declared in advance, not discovered by accident at the moment
of failure. Which direction that default points — permit or deny — is not something
this paper can derive in the abstract. A domain where failing closed means a patient
cannot receive emergency treatment may correctly choose to fail open, with the gap
logged and reviewed. A domain where failing open means an unauthorized transfer
completes may correctly choose to fail closed. The direction is a compiled decision,
made upstream, specific to what is actually at stake. What the kernel requires is only
that some direction was chosen on purpose.
Six primitives. No more, and — as the rest of this chapter will show — no fewer survive
scrutiny either.
A natural question follows immediately, because it is the question that decides whether
this list is actually finished: what happens when one of these six is given something
false? Not absent — false. A forged proposal. A counterfeit authority credential. A
standard that has been quietly substituted for the one that was actually compiled.
It is tempting to answer this by adding a seventh function — something that verifies
each input is genuine before the other six ever touch it. This temptation should be
examined carefully, because it does not survive its own logic.
The kernel is an evaluator, not an investigator. It does not discover whether a proposal
is true. It does not discover whether an authority credential is genuine. It does not
discover whether the standard it has loaded is the one that was actually compiled. It
receives each of these as presented, and it evaluates — exactly the way a court does
not authenticate evidence as part of deliberating on it. Authentication happens before
deliberation, through a separate function entirely: chain of custody, admissibility procedure, cross-examination. The court’s reasoning is sound given what was admitted. It
is not the court’s failure if something admitted was false. The failure belongs to whatever process lets a false thing through the door.
The same structure holds here, and it holds without exception across every input the
kernel touches. If a forged standard would justify adding a verification function for
the standard, the identical reasoning justifies a verification function for the proposal,
and another for the authority credential, and another for the output itself — because
every one of these is, in exactly the same way, vulnerable to being presented falsely. A
test that proves this much proves nothing in particular. It was never testing for what
belongs inside governance. It was testing for what is vulnerable to forgery, and the
honest answer is: everything is. Build a kernel that tries to authenticate every input
it receives, and it has stopped being a governance mechanism. It has become a governance mechanism fused to a trust infrastructure — larger, slower, and carrying exactly
the kind of implementation weight this paper has been deriving the kernel away from
since Chapter 5.
This does not mean forged inputs are a problem the architecture ignores. It means
forged inputs are a problem solved somewhere else, by mechanisms purpose-built for

the job rather than bolted onto an evaluator that was never designed to do it. A legitimate compiled standard, in practice, will carry its own integrity check — an immutable
hash committed at the moment of compilation, verified against the hash the gate holds,
before evaluation proceeds. A legitimate authority credential will carry its own signature, checked against a record the credential itself cannot forge. None of this happens
inside the six primitives described above. It happens in the systems that produce what
those primitives receive — exactly the way a shipping manifest can be hash-sealed at the
moment of loading, verifiable by anyone downstream, without the port authority that
later reads the manifest needing to personally witness the loading. The port authority’s
job is to act correctly on what the manifest says. Whether the manifest is genuine is a
question answered before it ever reaches the port authority’s desk — and if it isn’t, the
failure that follows is not a failure of the authority that read it correctly. It is a failure
of whatever was supposed to make the manifest trustworthy before it arrived.
This is not a gap in the kernel. It is the kernel’s edge, found precisely, and worth stating plainly: the kernel evaluates presented claims. It does not establish their truth.
Whether a given claim — a proposal, a credential, a standard — can be trusted to be
what it says it is, is a question answered by the systems that produce and transmit it,
not by the system that evaluates it. Forgery and fraud are real failure modes. They are
failure modes of the surrounding evidentiary infrastructure, addressed by the mechanisms that infrastructure builds for exactly this purpose — hashing, signing, sealing,
witnessing — not by expanding what counts as governance until it absorbs a second
discipline entirely.
That second discipline — how trustworthy inputs come to exist at all, and what happens
in the world when they don’t — is its own subject, with its own architecture, its own
market dynamics, and its own selection pressures. It is not this paper’s question. This
paper’s question was narrower from the start: given a proposal and a standard, can
admissibility be determined. The answer is six primitives, complete, and no larger than
they need to be.
What sits immediately adjacent to this kernel — close enough to receive its output the
instant a determination is made, far enough to be honestly described as a separate function — is the subject of Chapter 6A.

## Chapter 6A — The Accountability Interface

The kernel described in Chapter 6 is deliberately incapable of proving anything about
itself. This is not an oversight corrected here. It is the direct consequence of holding
the kernel strictly to the test of governance failure — and that test, applied honestly,
excludes evidence from the kernel’s interior. Evidence does not disappear from the
architecture. It moves next door.
Call this adjacent function the accountability interface. It is not part of the kernel. It
does not evaluate anything, does not check authority, and has no power to permit or
forbid. Its only function is to receive the kernel’s output — the proposal, the standard

applied, the determination reached — at the moment that output exists, and to make a
durable record of it that someone other than the kernel can later examine.
The case for this separation does not rest on convenience, or on a preference for tidy
architecture. It rests on something stricter: admissibility and evidence cannot occupy
the same causal position relative to the action, under any condition, on any substrate, at
any speed. One is necessarily prior to commitment. The other is necessarily posterior
to it. No improvement in speed, sophistication, or engineering closes that gap, because
it is not a gap of time. It is a gap of logical order.
Admissibility is what determines, before an action commits, whether it is permitted
to commit at all. By definition, it must occur first — there is no version of “permit or
forbid” that makes sense applied to something that has already happened. Evidence is
a record of a determination that was already, fully, completely reached. By definition,
it must occur after — there is no version of “a record of what was decided” that makes
sense applied to something not yet decided. These are not two points on the same axis
that a suﬀiciently advanced system might someday merge. They are opposite sides of
the one moment this paper has spent five chapters establishing as singular: the instant
an action becomes irreversible. Admissibility lives on one side of that instant. Evidence
lives on the other. Nothing can live on both.
This becomes clear under direct pressure. Could evidence ever participate in governance — not just support it, but actually perform part of the admissibility decision?
Examine the hardest version of this challenge: a standard that conditions permission
on whether evidence can later be generated — for instance, a rule permitting a transfer
only if it will be independently witnessed. Does this not fold evidence into the act of
governing?
It does not, and the reason is precise. What the kernel evaluates here is not evidence. It
is a compiled fact about a precondition — will a witness be available — checked the same
way any other clause is checked: instantly, as a binary fact about the world, before the
action proceeds. The kernel does not generate the witnessing. It checks whether the
witnessing’s precondition holds, exactly as it would check whether an authority token
is valid or a transfer amount falls under a limit. A standard can reference accountability infrastructure as a condition without accountability infrastructure becoming part of
governance, in the same way a standard can reference the time of day without the clock
becoming a governance primitive. Reference is not absorption.
The reverse question is equally direct. Can governance ever be reconstructed from evidence — and if so, doesn’t that prove the two are entangled rather than separate? A
complete evidence record contains the proposal, the standard applied, and the determination reached. Given all three, the original decision can be reconstructed with total
fidelity. But reconstruction is possible precisely because evidence is a faithful trace of
an act that had already, fully, occurred before the trace was made. A photograph of
a collapsed bridge lets an engineer reconstruct the sequence of structural failure with
complete accuracy. The photograph did not cause the collapse, did not participate in
it, and could not have prevented it. It exists downstream of forces that were already
fully determined before the photograph was taken. The ability to reconstruct an event

from a record is evidence that the record was always causally subsequent to the event —
never causally inside it. If it could have been reconstructed any other way, it was never
inside the event to begin with.
The sharpest version of the challenge asks whether suﬀiciently fast, suﬀiciently reliable
evidence could substitute for admissibility entirely — permit actions provisionally, and
use the evidence trail to reverse anything that turns out to have been wrong. This deserves a real answer rather than a dismissal, because it is the asynchronous governance
model this paper has already acknowledged as a genuine alternative architecture, not
a confused one. The answer rests on the same causal-priority argument, pushed to its
limit: even at theoretical zero latency, evidence generation remains causally subsequent
to the action, because a fact must exist before it can be recorded. No speed improvement
changes evidence’s position relative to the thing it records, the same way no improvement in camera shutter speed changes a photograph’s position relative to the event it
captures. What this model actually does is not substitute evidence for admissibility. It
substitutes a different, weaker admissibility policy — permit by default, detect failure
afterward — for the one this paper derives, and then relies on the accountability interface to do exactly the job already assigned to it: catch what the weaker upstream policy
let through. This is a legitimate choice for domains where reversal is genuinely possible and cheap. It is not evidence performing governance. It is a riskier governance
policy that still depends on accountability remaining a separate function to detect its
own failures.
The cleanest version of the question resolves the entire matter in one move. Can a record
of what happened ever stop the thing it is a record of from having happened? No —
not as an engineering limitation, but as a matter of what the words mean. Evidence
is evidence of something, and the something must already be settled before there is
anything to be evidence of. A mechanism capable of preventing the action it documents
would not be documenting that action. It would be the determination itself, occurring
before the action — which is precisely the kernel’s job, already fully specified, already
doing exactly that work, one layer upstream of where evidence operates. Give evidence
the power to prevent execution, and evidence has not been improved. A second kernel
has been built and mislabeled.
This is why the separation in this chapter is not a design choice the paper is recommending. It is a logical boundary the paper is describing. Admissibility is necessarily
prior. Evidence is necessarily posterior. The two cannot trade places, cannot merge,
and cannot substitute for one another under any condition — not because no one has
yet engineered a way around the constraint, but because the constraint is not engineering. It is causal order, and causal order does not yield to better tools.
What this leaves unresolved, deliberately, is how rich the accountability interface needs
to be to satisfy whatever is eventually demanded of it — legally, regulatorily, or by
the market forces that price trustworthy records differently from unreliable ones. That
is a question of implementation and of evidentiary infrastructure, addressed in full
elsewhere. The claim this chapter makes is narrower and does not depend on any of
those answers: the function exists, it is necessary, and there is no version of governance

— however fast, however well-engineered — in which it can be folded back into the
kernel without asking the kernel to occupy two positions in time at once.

## Chapter 7 — The Constitutional Question

What kind of thing is the kernel described in the previous chapter?
The obvious answer is that it is compliance machinery — a check that stops an action
when a box isn’t ticked, no different from any other automated rule enforcement. That
answer is wrong. Seeing why requires asking a more basic question first: what is a
constitution actually for?
One answer treats a constitution as a statement of values — dignity, fairness, proportionality, rights understood as moral facts a society has agreed to protect. This describes
something real about how constitutional language is often written and argued over. But
it is not the only answer, and testing whether the kernel depends on it turns out to be a
more useful question than simply assuming it.
Locke offers a different starting point. He does not begin with values. He begins with
a narrower, more mechanical question: what stops a sovereign from doing whatever it
wants? His answer is not dignity. It is delegated, bounded authority. A government
holds only the powers given to it by those it governs, exercised only within the scope
of that delegation, forfeit the moment it exceeds that scope.5 A constitution, on this
account, is not primarily a declaration of what is good. It is a specification of what is
permitted — an answer, in advance, to one question: does this authority exist?
That is a binary question. Permit or deny.
Look again at the kernel from Chapter 6 with this framing in mind. It does not ask
whether an action is wise, fair, or proportionate — those questions were already settled
upstream, compiled into the standard before the kernel ever sees a proposal. It asks
exactly one thing: does the entity proposing this action hold the authority to propose
it, and does the action fall within the scope that authority was granted. Permit or deny.
Nothing else.
This is not compliance machinery checking boxes against a rulebook. It is the Lockean
question, mechanized, asked at the only moment it is operative — before the action, not
after.
But the question worth asking now is whether this resemblance depends on Locke being correct about anything. A skeptical reader is entitled to reject Locke entirely — to
prefer Hobbes, or Rawls, or the narrower procedural language of administrative law
— and the kernel’s claim to be constitutional, rather than merely mechanical, should
not collapse just because one philosophical tradition is set aside. If it does collapse, the

      The account of delegated, bounded authority as the foundation of constitutional legitimacy is developed in Locke, J. (1689). Two Treatises of Government. Particularly the Second Treatise, Chapters XI–XIV,
which establish that legislative and executive power derive from consent of the governed and are forfeit
upon violation of that trust. The edition most commonly cited in contemporary constitutional theory is
Laslett, P. (ed.) (1988). Two Treatises of Government. Cambridge University Press.

resemblance to constitutionalism was decorative. If it does not, something sturdier is
being described.
Hobbes provides the first test, and a useful one, because his starting question is nearly
the opposite of Locke’s. Hobbes does not ask how authority should be bounded. He
asks what prevents the collapse into chaos when no authority is absolute enough to be
obeyed without contest. His answer is a sovereign whose authority is accepted precisely
because it is not up for renegotiation at the moment of decision — the alternative being
worse than any single abuse the sovereign might commit.6 Read the kernel this way,
and it fits cleanly, perhaps even more naturally than it fits Locke: the kernel is absolute
and non-negotiable at the instant of evaluation, enforcing whatever the compiled standard says without appeal, in exactly the way a Hobbesian sovereign’s word is final at
the point of decision even though the deliberation that produced that word happened
elsewhere, earlier, among different people. The kernel does not need Locke’s account
of bounded delegation to be doing something Hobbes would recognize as sovereign
enforcement.
Rawls provides the harder test, because Rawlsian legitimacy is explicitly about outcomes — a just structure is one a rational party would choose without knowing their
own position in it.7 The kernel cannot perform this reasoning, and there is no use pretending otherwise. It has no capacity for the kind of contextual, distributive judgment
Rawls requires. But notice precisely where that judgment has to live under this paper’s own architecture: upstream, in the compilation process, exactly where Chapter
3 already placed everything requiring time and context. A standard compiled according to Rawlsian principles would be enforced by the kernel with the same fidelity as
a standard compiled under any other theory. The kernel does not need to be capable
of Rawlsian reasoning. It needs to enforce whatever the upstream process, governed
by whichever account of justice an institution adopts, decides the standard should say.
This is, if anything, the strongest demonstration that the kernel’s classification does not
depend on any one theory: it is indifferent to which theory compiles the standard, because its own primitives say nothing about what makes a standard just — only about
how a standard, once compiled, is enforced without drift.
Administrative law provides the most practical test, because it is the framework most
likely to be invoked by an institutional reader uninterested in seventeenth-century political philosophy and concerned only with whether this is a permissions system wearing
a borrowed vocabulary. Administrative law does not ask about ultimate sovereignty.
It asks narrower, procedural questions: was the action within the actor’s granted authority, was the rule actually in force when the action was taken, is the action void

       The Hobbesian account of sovereign authority accepted as preferable to the state of nature is developed in Hobbes, T. (1651). Leviathan. Particularly Chapters XVII–XVIII, which establish the covenant by
which subjects transfer natural rights to a sovereign in exchange for protection, and the conditions under
which that authority is non-negotiable at the moment of exercise. The edition most commonly cited in
contemporary political theory is Tuck, R. (ed.) (1996). Leviathan. Cambridge University Press.
       The veil of ignorance as the basis for determining just institutional structures is developed in Rawls, J.
(1971). A Theory of Justice. Harvard University Press. Particularly §§ 3–4, which establish the original position and veil of ignorance as the mechanism by which rational parties select principles of justice without
knowledge of their own social position, natural abilities, or conception of the good.

if it was not. Run the kernel through these questions directly. Ultra vires doctrine —
did the entity act within its actual granted scope — is, word for word, what authority
check already does, and administrative law treats a positive answer to this question
with real force: an ultra vires act is void, not merely irregular.8 The kernel’s binding
output, where denial means the action does not occur at all, maps onto void-not-merelyimproper more precisely than it maps onto anything in Locke’s own language. The kernel survives this test completely intact, and arguably fits it more literally than it fits any
of the philosophical accounts that came before it.
What this sequence establishes is not that Locke was the wrong choice. It is that Locke
was never the load-bearing element. The kernel’s classification as constitutional rather
than administrative survives Hobbes, survives Rawls, survives administrative law —
three accounts of legitimate authority that disagree with each other and with Locke
on almost everything except the one thing the kernel actually needs: a clear answer to
whether power was exercised within its granted bounds. The kernel requires that some
coherent account of legitimate authority exists upstream, compiling the standard it will
enforce. It does not require that account to be Locke’s, or anyone’s in particular. Locke
remains the clearest, most historically resonant illustration of the question the kernel
mechanizes — does this authority exist — but illustration is not foundation, and the
architecture does not lean on Locke being right.
This does not mean the kernel is a perfect constitutional mechanism, under any of these
four accounts. The kernel enforces whatever authority was delegated to it by the compilation process described in Chapter 3 — performed by humans, upstream, exercising
exactly the interpretive judgment Chapter 2 established cannot survive at the boundary
itself. If that upstream process is illegitimate — if the authority it delegates was never
properly granted, under whichever theory was supposed to govern the granting — the
kernel enforces that illegitimacy with the same speed and precision it would enforce
legitimate authority. The kernel cannot tell the difference. It was never built to.
This is not a flaw unique to the kernel. It is the oldest unresolved problem shared by
every account tested above, applied one layer deeper. None of them — Locke, Hobbes,
Rawls, administrative law — fully specifies who decides that a given delegation of authority was made honestly in the first place. Every constitutional system built on any
of these foundations faces the same unresolved question at its root: who legitimately
compiles the rules that authority is then bound to. The kernel does not introduce that
problem. It inherits it, faithfully, regardless of which tradition is used to describe it.
A reader might expect a constitutional mechanism built into software to be a thinner
version of the human institutions it sits beneath — political philosophy with the hard
parts engineered away. The opposite is closer to true. The kernel reproduces the hard
part exactly, under any of the four accounts tested here. It does not solve the question

     The ultra vires doctrine as the foundational principle of administrative law — establishing that acts
beyond granted authority are void rather than merely irregular — is developed in Wade, W. & Forsyth,
C. (2014). Administrative Law (11th ed.). Oxford University Press. Chapters 2 and 5 establish the scope
and consequences of ultra vires action in Anglo-American administrative law. The doctrine’s application
in United States administrative law is codified in the Administrative Procedure Act (1946), 5 U.S.C. §§
500–596, which establishes judicial review of agency action exceeding statutory authority.

of legitimate authority. It enforces whatever answer that question was given upstream,
with a fidelity human institutions have never achieved — because human institutions
have always had the gap of time the previous six chapters spent explaining away.
What this paper has not yet done is take the strongest objections seriously, on their own
terms, before claiming to have established anything at all.

## Interlude — The Panel

The paper has now made its argument. Before that argument meets its objections formally, it is worth pausing to observe what the argument will actually collide with —
because the strongest resistance to what precedes this page will not be technical. Most
people who understand the latency argument will eventually concede it, however reluctantly. The resistance that matters, the kind that produces a room full of nodding
heads and a panel moderator asking the question with complete confidence, is something else.
Imagine an AI conference, a room full of professional, highly educated, experienced
policy makers. The presenter has just finished walking through the redistribution argument — interpretation upstream, enforcement at the boundary, accountability downstream. A hand goes up. The moderator, not waiting, voices what the room is already
thinking:
Surely there must always be a human in the loop.
The room nods. Of course there must be. This seems self-evident. It feels almost moral.
And it will be asserted — not derived, asserted — with the confidence of someone who
has never needed to derive it because it has never been seriously questioned before.
The presenter asks one question in return.
Where? Silence.
At 10 milliseconds? At 1 millisecond? At 100 microseconds? At 10 microseconds?
The human is still there, in theory. The authority is still human. The policy was written
by humans. The standard was compiled by humans. The accountability will be reviewed by humans. But at what point, exactly, does the human intervene — and what
does intervention mean when the action has already committed before the intervention
could have physically begun?
The room is quiet in a different way now. Not the quiet of agreement. The quiet of
something having shifted without anyone deciding to let it shift.
This scene will play out in every serious venue where this paper is discussed, because
the objection it surfaces is not really about latency. It is about something the latency
argument merely reveals.
The professional groups in the room respond differently, but predictably.
The engineers are the easiest. Most of them, once the latency numbers land, will concede the logic — not happily, but honestly. They can see the arithmetic. They know
what a CPU cycle costs. They understand what it means when the governance check

cannot physically complete before the action commits. They may not like the conclusion. They will usually admit it follows.
The lawyers are harder, but for a different reason. The objection sounds like there must
be accountability — and of course there must, and the paper agrees there must, and the
accountability interface exists precisely for this reason. But what the lawyer is actually
worried about, beneath the accountability language, is attribution. Who is responsible when something goes wrong? The answer this paper gives — whoever compiled
the standard — is technically complete and deeply unsatisfying to someone whose professional life is organized around finding a human being to hold accountable at the
moment of action. The accountability didn’t disappear. The moment changed.
The policy professionals are harder still. Their objection sounds like humans must interpret — and again, the paper agrees. Entirely. Interpretation is upstream, where humans
still perform it, where it is still essential, where nothing in this paper diminishes its importance by a single degree. But the policy professional experiences the relocation of
interpretation upstream as something closer to the elimination of interpretation at the
point that felt most important. The execution boundary felt like where meaning was
made. The paper is saying meaning was always made elsewhere, and the execution
boundary was just where it arrived. That is a subtle shift, but it lands as a large one.
The fourth group is the one that doesn’t move. Not because the argument is wrong.
Because accepting the argument would require revising something that isn’t really a
belief — it’s an identity. For this group, being responsible means personally deciding.
Not defining the envelope inside which decisions are made. Not compiling the standard
against which actions are evaluated. Personally deciding, at the moment of action, with
the weight of the decision felt in real time.
The paper says: that model is no longer physically available at machine speed, and
clinging to it does not preserve human authority. It produces the opposite — a ceremonial presence that feels like control while the actual decisions accumulate below the
threshold of human attention.
The last reviewer.
Picture the final human in the loop. Not a metaphor — a real person, a real role, a real
console. Their job is to review autonomous agent actions before they execute.
At ten transactions per second, the job is hard but possible. At a hundred, it becomes
a blur. At a thousand, the reviewer is no longer reviewing — they are performing review, which is different. At ten thousand, the signature exists, the authority exists, the
human is present, and the intervention is ceremonial. The title remained. The function
migrated upstream the moment the volume exceeded what a human could genuinely
process.
This is not a failure of the human. It is not a failure of the institution. It is the latency
argument made visible in a person — the moment when the gap between what governance claims to be doing and what it is actually doing becomes impossible to ignore.
That gap is not new. It has been opening quietly for years, in every domain where
autonomous systems began executing faster than their nominal oversight mechanisms

could track. The paper simply names it, traces it to its cause, and asks what governance
looks like when the gap is acknowledged honestly rather than papered over with a role
that no longer does what it says it does.
What this interlude is not.
It is not an argument that human judgment is obsolete. The paper has said this before
and means it: human judgment is irreplaceable, and the architecture described in these
chapters depends on it entirely — upstream, in the compilation of the standard the
kernel will enforce. Without human judgment there, the kernel has nothing to enforce.
The kernel is not a replacement for human authority. It is the mechanism through which
human authority, compiled in advance, reaches the one moment it cannot physically
occupy in person.
The strongest resistance to this paper will come from people who experience that sentence as a consolation prize. They wanted to be present at the moment of action. The
paper is saying they can no longer be, at machine speed, and that the authority they
care about is still fully theirs — but located differently than they assumed.
That is genuinely uncomfortable. It is not wrong.
Chapter 8 addresses the formal objections. This interlude exists only to note that the formal objections are rarely the real ones — and that readers who find themselves reaching
for there must always be a human in the loop may find it useful to ask themselves, before
reading further, exactly what they mean by that, and at what speed they mean it.

## Chapter 8 — Objections

A paper that survives only the objections it chooses to raise has not been tested. What
follows are the strongest cases against the argument made so far, presented as their
proponents would make them, answered only as far as the answer goes.
Objection one: This is still compliance machinery.
The constitutional reframe in the previous chapter is elegant, but elegance is not evidence. A mechanism that checks whether an action falls within a pre-defined scope
of authority is, whatever language is used to describe it, the same thing a permissions
system has always been — and permissions systems are not constitutions. They are infrastructure. Calling the kernel constitutional does not change what it does. It changes
how comfortable the reader feels about what it does.
A conventional permissions system checks access against a static, narrow rule — can
this user open this file. It does not claim to answer a constitutional question, because the
question it answers is too small to be one. The kernel’s claim is different in kind, not just
in framing: it answers, before any consequential action proceeds, whether authority for
that action was ever actually delegated — the same question a court asks when it rules a
government acted ultra vires, asked at the only moment that question can still be causal
rather than merely declarative.9 The resemblance to a permissions system is real. So is
    The ultra vires doctrine as the basis for judicial review of governmental action is established in Wade,
W. & Forsyth, C. (2014). Administrative Law (11th ed.). Oxford University Press; and in United States

the resemblance between a permissions system and a constitution, if the permissions
system is the only mechanism standing between an actor and the exercise of power, and
nothing about that power’s legitimacy is checked anywhere else in the chain. Whether
that resemblance earns the word “constitutional” is a judgment this paper has made
and the reader is free to reject. It is not a confusion of categories. It is a claim that, at
suﬀicient scale and consequence, the categories converge.
Objection two: The legitimacy problem is fatal, not inherited.
Chapter 7 conceded that the kernel enforces whatever authority the upstream compilation process delegates to it, and that nothing in the kernel can distinguish legitimate
delegation from illegitimate delegation. The paper treats this as an inherited problem,
present in every account of legitimate authority examined. A more skeptical reading
treats it as fatal here, and worse here than anywhere it has previously appeared.
The argument runs as follows. Human constitutional systems, whatever their flaws, retain a slow but real corrective mechanism: courts can later rule that authority was never
legitimately granted, and that ruling has teeth, because the action being reviewed is
usually still contestable, reversible, or compensable after the fact.10 The kernel removes
exactly this corrective. By design, by the entire argument of Chapters 2 through 5, it
acts before any human review is possible. An illegitimate delegation, once compiled
into the kernel’s standard, is enforced with a speed and completeness that means the
downstream correction this paper relies on — accountability, the slow human-speed
institutions Chapter 3 relocated review to — arrives only after whatever damage the
illegitimate authority caused has already occurred at scale. The gap of time that made
human constitutional systems imperfect also made them survivable. Closing the gap
does not just inherit the legitimacy problem. It removes the safety margin that made
the problem tolerable.
This is the strongest objection the paper faces, and there is no clean answer to it. What
Chapters 1 through 7 establish is narrower: if authority is going to be enforced at machine speed at all, it will be enforced by something with the kernel’s properties, whether
or not the legitimacy of that authority was ever properly examined. The objection is
right that this raises the stakes of getting the upstream process right. It does not show
that getting it right is impossible, or that the alternative — no enforcement mechanism
at the boundary at all — produces a safer outcome. An illegitimate authority enforced
nowhere is not contained. It simply acts without even the constraint of having to match
a compiled standard first.

administrative law in the Administrative Procedure Act (1946), 5 U.S.C. §§ 500–596. The causal versus
declarative distinction — that review before action prevents harm while review after action merely describes it — is an original contribution of this paper.
       The corrective mechanism of judicial review as the primary accountability instrument in constitutional systems is established in Hamilton, A., Madison, J., & Jay, J. (1788). The Federalist Papers. No. 78
(Hamilton) — establishing judicial review as the mechanism by which unconstitutional acts are voided.
The doctrine’s development in United States law is anchored in Marbury v. Madison, 5 U.S. 137 (1803),
which established the power of courts to void acts exceeding constitutional authority. The equivalent doctrine in English constitutional law is developed in Wade, W. & Forsyth, C. (2014). Administrative Law (11th
ed.). Oxford University Press.

Objection three: Something essential has been lost, even if nothing has been added
incorrectly.
The third objection does not dispute the kernel’s derivation. It disputes what the derivation leaves out. Constitutional governance has never been only about checking authority against a pre-defined scope. It has been about the capacity to recognize when a situation falls genuinely outside anything the rule-makers anticipated — and to exercise
judgment in that gap rather than mechanically denying it. A constitution that cannot
recognize its own incompleteness is not a leaner constitution. It is a brittle one, certain
to fail exactly where judgment was needed most.
This objection lands cleanly against the kernel as described. The kernel’s fail-safe behavior — a pre-declared default when evaluation cannot complete — is precisely a mechanical, judgment-free response to encountering something the standard did not anticipate. It does not recognize novelty. It defaults, indiscriminately, alongside genuine
violations. A human institution facing a genuinely unanticipated case can pause and
deliberate; the kernel cannot, because the judgment that pause requires is exactly what
Chapter 2 already showed cannot survive at the boundary. This is a real cost of the
architecture this paper has derived. Novel, legitimate, unanticipated actions will be denied — or permitted, depending on the declared default — by a system built this way,
at a rate the paper has made no attempt to estimate.
The cost is not unbounded: a sensibly chosen default fails in a known, declared direction rather than an accidental one. And the cost is not permanent: nothing in this architecture prevents the upstream compilation process from being revised, deliberately
and often, specifically to absorb categories of action the standard did not originally anticipate. The kernel will be brittle at the margin until the standard is updated. It will
not stay brittle indefinitely, unless the upstream process itself fails to do the job this
paper has assigned to it.
The objection correctly identifies that something is lost. It does not establish that the
loss is permanent, or that it outweighs what the previous chapters have shown is gained
by being present, deterministically, at a boundary nothing else can occupy.
Objection four: Reality is ambiguous, therefore governance must retain discretion.
This objection is the most predictable one this paper will face, and it deserves to be
stated at full strength before it is answered. The argument runs in three steps. Reality is not fully specifiable — novel situations emerge, context shifts, rules are written
before the cases that will test them exist.11 Some decisions, therefore, require interpretation. And if interpretation is required, governance systems must retain the discretion
to perform it. A kernel that cannot interpret, on this account, has not achieved minimal
governance. It has achieved a governance system incapable of governing the cases that
matter most.
     The irreducible incompleteness of rule systems as a foundational challenge for governance is developed in Hart, H.L.A. (1961). The Concept of Law. Oxford University Press. Chapter 7 establishes the open
texture of legal rules — the structural inability of any rule system to anticipate every case its terms will be
applied to — as a permanent feature of law rather than a deficiency to be corrected. Fuller, L.L. (1964). The
Morality of Law. Yale University Press develops the complementary argument that legal systems require
human judgment precisely because rules cannot be fully self-applying.

The first two steps are correct, and this paper has never disputed either of them. Chapter 3 conceded directly that discretion exercised at the point of action has no clean upstream equivalent, and that genuinely novel cases will arrive at the boundary with no
compiled rule that fits them. The break is in the third step, and it is a quiet one: “governance systems must retain discretion” silently assumes that the system performing governance and the system executing the action are the same system. Nothing in this paper
has assumed that, and the entire argument of Chapters 3 and 4 was built specifically to
separate them. Interpretation does not have to occur at the boundary for interpretation
to occur. It has to occur somewhere — and this paper has spent six chapters showing
precisely where: upstream, before compilation, where time and judgment are both still
available.
The architecture’s actual answer to a genuinely ambiguous case is not embedded interpretation. It is fail-safe — already fully derived in Chapter 6, not a new mechanism
invented to meet this objection. An ambiguous proposal is one the compiled standard
cannot resolve; the kernel does not attempt to resolve it by reasoning about what was
probably intended. It defaults, in the pre-declared direction, and the case routes back
to wherever the declared fallback sends it — typically, legitimate upstream authority,
exactly where interpretation belongs. The kernel never acquires interpretive power. It
simply declines to act on a case it cannot evaluate, which is a different and much narrower claim than refusing to recognize ambiguity exists.
This produces a comparison worth stating precisely rather than as a slogan. It is not that
ambiguity makes the kernel stronger in some unqualified sense — that overstates the
case. It is narrower and fully defensible: the cost of a kernel that refuses to act on cases
it cannot resolve is lower than the cost of a kernel that silently decides, on its own, what
an unresolved case probably means — because the second failure mode is invisible.
A system that interprets at runtime does not announce that it has started legislating
instead of enforcing. It produces an output indistinguishable from a correctly governed
one, and the authority it has quietly acquired leaves no trace anywhere this paper’s
evidence layer would catch it, because the determination it produced looks, from the
outside, exactly like every other determination. A kernel that declines instead is at least
declining visibly, in a direction someone chose on purpose, with the unresolved case
sent back to people who can actually weigh it.
A note on how this conclusion was reached.
The honest answer to “how do we know this wasn’t simply reverse-engineered to match
a predetermined destination” deserves stating plainly rather than left for a reader to
wonder about. This paper’s central architecture was tested, repeatedly and adversarially, against an existing implementation built independently and for different stated
purposes. The comparison was instructive in both directions, and both directions are
worth disclosing.
Several components derived here — the proposed action, the compiled standard, the
authority check, the evaluation act, the binding output — converged with that implementation’s equivalent components through a different reasoning path — one beginning from constitutional theory and latency physics, the other from hardware substrate

requirements:12 one beginning from physical constraints on machine-speed execution,
the other from engineering requirements at a specific hardware substrate. That convergence, reached independently, is meaningful evidence the derivation in Chapters 2
through 6 was tracking something real rather than assembling a predetermined answer.
The same comparison also surfaced a genuine candidate this paper considered seriously
and ultimately rejected: a seventh primitive, proposed to guarantee the authenticity of
the compiled standard itself. That candidate was tested at length, found to generalize
in a way that proved too much — the same reasoning would have required separate authenticity primitives for every input the kernel touches — and was excluded on exactly
the grounds this paper has used throughout: not whether a function would be useful,
but whether its absence constitutes a governance failure rather than a failure of the surrounding evidentiary infrastructure. The kernel that survived that test is narrower than
the version first proposed, not broader. A retrofitted argument tends to grow toward
its target. This one was cut back from it.
This disclosure is offered not as proof the paper’s conclusions are correct, but as an
honest account of how they were tested — including the places that didn’t hold up,
examined as carefully as the places that did.
What these objections leave standing, and what they do not.
None of the four objections in this chapter defeats the central claim that some form
of minimal, deterministic enforcement is required at the execution boundary if governance is to be present there at all — that claim rests on the physical and structural
arguments of Chapters 2 through 5, and none of these objections touches those chapters directly. What the objections establish, cumulatively, is that the kernel’s legitimacy
is entirely a function of what happens upstream of it, that the safety margin human institutions have always relied on is genuinely reduced by closing the time gap, that the
kernel will fail — predictably, but fail — at exactly the cases that most require judgment,
and that the architecture’s answer to ambiguity is restraint rather than interpretation,
with all the cost and all the discipline that restraint actually requires.
These are not objections this paper has defeated. They are the paper’s honest description of what it has not yet built, and what no version of this architecture can build on
its own. The compilation process — who performs it, what makes it legitimate, how
its failures are caught before they are compiled into something the kernel will enforce
without hesitation — is not a detail left for future work. It is the unresolved center the
entire argument has been circling since Chapter 3, and it is where the paper’s conclusion must be honest about what has, and has not, been established.

      The implementation referenced is 512 (Watson 2026), the author’s own prior work. The derivation in
Chapters 2–6 was completed without reference to 512 and [compared against it afterward], as a baseline.
This sequencing establishes that the derivation was not reverse-engineered toward a predetermined result;
it does not establish independence between the two, since both are the author’s. The comparison’s evidential value lies in its disagreements — see the rejection of specification integrity as a seventh primitive —
rather than in its agreements.

## Chapter 9 — Conclusion

This paper began with a single question: what survives when governance is exposed to
machine-speed execution? The answer it has arrived at is not the one most readers will
expect, and it is worth stating plainly, without the qualifications that have accompanied
it through eight chapters of derivation.
Governance survives. It does not survive intact.
What is lost is the assumption — never stated because it never needed to be, until now
— that the entity exercising judgment has time to exercise it. That assumption held for
nearly the whole of institutional history, because nothing before now moved faster than
the humans governing it. It does not hold for an autonomous system that proposes and
commits a consequential action in a span of time too short for any human process to
intervene. Not a slow human process. The fastest one that could exist.
What is not lost is governance itself, because governance does not require the assumption that gave it its familiar shape. It requires three things, and machine-speed execution does not remove any of them — it only relocates where each one can survive.
Interpretation, which requires time and judgment, moves upstream, into the compilation of policy before any action is proposed. Accountability, which also requires time,
moves downstream, into evidence examined after the fact, at whatever pace examination requires — and that evidence, this paper has shown, cannot be folded back into
the moment of decision no matter how fast it is generated, because admissibility and
evidence sit on opposite sides of the one instant that actually matters, and nothing engineers its way across that line. And enforcement — the only function that cannot move,
because it has exactly one moment in which it can still matter — compresses to the
smallest mechanism capable of occupying that moment: six primitives, no reasoning, a
binding answer to one question asked the instant before an action becomes irreversible.
This is not governance reduced. It is governance separated into the pieces that were
always doing different jobs, now finally visible because the conditions that used to let
them blur together no longer hold.
The kernel this paper has derived is not bureaucratic machinery. Chapter 7 showed
why, and showed it more carefully than a single philosophical tradition could support
on its own: the kernel asks exactly the question constitutional theory, in several of its
oldest and most incompatible forms, has always asked — does this authority exist —
and it asks that question at the one moment human institutions have never been able to
reach. This did not turn out to depend on any one account of legitimate authority being correct. Locke supplies the clearest version of the question. Hobbes recognizes the
kernel’s absolute, non-negotiable posture at the moment of decision. Rawls’s account
of justice, whatever its content, compiles upstream exactly like any other. Administrative law maps onto the kernel’s actual mechanics more literally than any of them. The
classification survived every account tested against it, which means the classification
was never resting on one of them in particular.
What none of those accounts solve — and what this paper does not solve either — is
who legitimately decides what authority is granted in the first place. Chapter 8 took the

strongest objections to this entire argument seriously, on their own terms, and found
that none of them defeats the central claim that something with the kernel’s properties is required at the boundary if governance is to be present there at all. Several of
them correctly identify costs the paper has not minimized: that the kernel’s legitimacy
depends entirely on what happens before it, that the safety margin human institutions
relied on for centuries is genuinely reduced by closing the gap of time those institutions
always had, and that ambiguous, genuinely novel cases will be met not with judgment
but with restraint — a declared default, not a guess. That restraint is not a weaker form
of governance pretending to be a stronger one. It is the deliberate alternative to a worse
failure: a system that interprets silently, at runtime, leaving no visible sign that it has
quietly begun deciding things it was never built to decide.
This paper has also tried to be honest about how its own conclusions were tested, not
just what they conclude. The kernel described here was checked against an existing
implementation — the author’s own prior work — after the derivation in Chapters 2–6
was complete, not before it. Several of its components converged with that implementation’s equivalents despite the different routes taken to reach them — meaningful evidence that the derivation was tracking something real. One serious candidate addition
was tested at length, found to prove too much once generalized, and was excluded —
not quietly, but on the record, because a derivation that only ever grows toward a predetermined answer is not a derivation, and this one was cut back from where it started
rather than expanded toward it.
This is also why the paper has been careful, throughout, not to argue that this is good
news. It is not an argument that machine-speed governance is superior to the deliberative institutions it sits beneath. The note early in this paper said as much directly:
selection does not measure merit, it measures fit, and a tool well suited to one domain
does not become worse for being unsuited to another. Interpretive governance remains
exactly what it has always been — the only mechanism capable of producing the judgment a kernel cannot generate for itself. It has not been retired. It has been relocated
to where its judgment now carries more weight than before, because less correction
remains available after it finishes its work.
What this paper claims, narrowly and specifically, is this. Machine-speed execution
does not eliminate governance. It redistributes it. As governance approaches the execution boundary, interpretation migrates upstream, accountability migrates downstream,
and enforcement compresses toward a minimal core — not because anyone designed
it that way, but because nothing else survives the conditions the boundary imposes.
Whether that core is ultimately built well or built carelessly, built accountably or built
to serve whoever controls the compiler, remains an open question this paper has not
answered and was never structured to answer alone.
The existence of the core, however, is no longer the open question.
The compression is not a choice being offered. It is a condition already underway, in
every domain where action has begun to outpace the institutions built to govern it. The
only choice remaining is whether the six functions that survive that compression are
built with the legitimacy problem named honestly, in the open, by people willing to

say plainly what has and has not been solved — or whether they are built quietly, by
whoever gets there first, with the hardest question left for someone else to discover only
after the architecture is already in place.
That choice is still available.
It will not remain available indefinitely.

End of manuscript — Version 1.0
Constitutional Compression: The Emergence of Minimal Governance at Machine Speed
10 chapters. 1 interlude. 6 primitives. One constraint.
Jonathan M. Watson
Independent Researcher
jonmwatson@gmail.com
August 01, 2026

Glossary of Terms
Terms are defined as used in this paper. Where a term is also used elsewhere with a different
meaning, that usage is not implied here.
Accountability interface The function, distinct from the kernel, that receives a determination at the moment it is reached and produces a durable, examinable record of it.
Necessarily posterior to the determination it records, by logical structure rather than by
engineering limitation. See also: evidence, causal priority.
Action latency The interval available between a proposed action and the moment that
action commits to consequence — the window within which a governance determination must be reached if it is to influence the outcome rather than merely describe it.
Admissibility The property of a proposed action that permits it to cross the execution
boundary and execute. Determined before commitment, never inferred from outcomes
afterward. Necessarily prior to any evidence produced about the same action.
Authority check The kernel primitive confirming that the entity proposing an action
holds standing to propose it — distinct from the compiled standard, which answers
whether the action itself is permitted in general. Collapsing the two creates a single
point of failure where one successful forgery defeats both questions at once.
Binding output The kernel primitive producing a permit or deny determination that
the surrounding system is actually obligated to obey. A determination that can be ignored downstream is not governance; it is a recommendation.
Causal priority The logical relationship establishing that admissibility must occur before an action commits and evidence must occur after a determination is reached — a
relationship of order, not of speed, that cannot be closed by any improvement in engineering. The foundation of the separation between the kernel and the accountability
interface.

Compiled standard The kernel primitive serving as the basis a proposed action is measured against. Produced upstream, before any action is proposed, by the interpretive
process this paper locates outside the execution boundary. The standard’s content is
a governance question; whether the standard presented to the kernel is authentic is
treated in this paper as a question belonging to the surrounding evidentiary infrastructure, not to the kernel itself.
Compliance machinery A characterization of the kernel this paper rejects. Distinguished from constitutional governance by the nature of the question asked:
compliance machinery checks conformance to a rule after or alongside an action; the
kernel answers, before commitment, whether authority for the action exists at all.
Constitutional compression The central phenomenon this paper describes: the redistribution of governance functions under machine-speed conditions, in which interpretation migrates upstream, accountability migrates downstream, and enforcement compresses to a minimal executable core at the execution boundary.
Controlling governance Governance capable of preventing an inadmissible outcome
because it operates before the action commits. Distinguished from narrative governance, which can only describe an outcome after it has already occurred. Only possible
at the execution boundary.
Evaluation act The kernel primitive performing the actual comparison of a proposed
action against the compiled standard and the authority context. A standard that exists
but is never applied governs nothing.
Evidence A record, produced after a determination is reached, capturing what was
proposed, what standard applied, and what was decided. Necessarily posterior to the
determination it documents. Cannot prevent the action it records, by the same logical
structure that makes it evidence in the first place. See also: accountability interface,
narrative governance.
Execution boundary The precise, singular moment at which a proposed action transitions from candidate to committed — the last instant at which two outcomes remain
possible. The only point at which a determination can still be causal rather than descriptive.
Fail-safe behavior The kernel primitive specifying a pre-declared response when evaluation cannot complete. The requirement is that a default exists and was chosen deliberately in advance; the direction of that default — permit or deny — is a domain-specific
compiled decision, not a universal constant derivable from first principles.
Human latency subsidy The unexamined interval governance has historically drawn
from the fact that a human, rather than a machine, was the one initiating action. Eliminated, not merely reduced, when an autonomous system initiates the action instead.
Interpretive governance The mode of governance native to conditions where time is
available — deliberative, contextual, capable of applying judgment to cases no rule anticipated. Cannot operate at the execution boundary, not because it is weak, but because the conditions it depends on (available time, unhurried judgment, manageable

volume) do not exist there. Relocates upstream under machine-speed conditions rather
than disappearing.
Minimal kernel The six-primitive mechanism this paper derives as the smallest configuration capable of performing admissibility evaluation at the execution boundary:
proposed action, compiled standard, authority check, evaluation act, binding output,
fail-safe behavior. Deliberately incapable of reasoning, recording, or proving anything
about itself.
Narrative governance Governance that documents outcomes after they occur. Genuinely valuable for accountability and institutional learning, but causally incapable of
preventing the outcome it describes. Distinguished sharply from controlling governance.
Proposed action The kernel primitive representing the object being governed — the
thing submitted for an admissibility determination. Without it, none of the kernel’s
other functions have anything to operate on.
Redistribution The paper’s central discovery: that governance under machine-speed
pressure does not disappear but separates into three functions occupying three different
positions in time — interpretation before, enforcement at, and accountability after the
moment an action commits.
Selection pressure The mechanism by which competitive and physical constraints determine which governance structures persist under machine-speed conditions. Explicitly distinguished in this paper from a measure of merit: selection determines fit to a
domain, not superiority in any general sense.
Specification integrity A candidate seventh kernel primitive, proposed and tested at
length, ultimately excluded. The argument for inclusion generalized to require authenticity verification for every kernel input — proposal, authority credential, and standard
alike — proving too much to justify singling out the standard. Resolved as a question
belonging to the surrounding evidentiary infrastructure rather than to the kernel.
Time-domain mismatch The structural incompatibility between human governance
and machine-speed execution, arising because the two operate under different assumptions about the interval between decision and consequence. Not a performance gap
closable by faster human institutions; a domain incompatibility.
End of Glossary
Working Bibliography — Version 1.0
Constitutional Compression: The Emergence of Minimal Governance at Machine Speed

A — Agent Architecture and Autonomous Systems Yao, S., Zhao, J., Yu, D., Du, N.,
Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting
in language models. International Conference on Learning Representations (ICLR 2023).
Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., … & Wen, J.R. (2024). A
survey on large language model based autonomous agents. Frontiers of Computer Science,
18(6).

B — Cognitive Science and Human Factors Card, S.K., Moran, T.P., & Newell, A.
(1983). The Psychology of Human-Computer Interaction. Lawrence Erlbaum Associates.
Donders, F.C. (1868). Over de snelheid van psychische processen. Onderzoekingen
gedaan in het Physiologisch Laboratorium der Utrechtsche Hoogeschool. English translation:
On the speed of mental processes (1969), Acta Psychologica, 30, 412–431.

C — Constitutional and Political Theory         Hamilton, A., Madison, J., & Jay, J. (1788).
The Federalist Papers. No. 78.
Hobbes, T. (1651). Leviathan. Tuck, R. (ed.) (1996). Cambridge University Press.
Locke, J. (1689). Two Treatises of Government. Laslett, P. (ed.) (1988). Cambridge University Press.
Rawls, J. (1971). A Theory of Justice. Harvard University Press.

D — Legal and Administrative Sources            Administrative Procedure Act (1946). 5
U.S.C. §§ 500–596.
Fuller, L.L. (1964). The Morality of Law. Yale University Press.
Hart, H.L.A. (1961). The Concept of Law. Oxford University Press.
Marbury v. Madison, 5 U.S. 137 (1803). U.S. Supreme Court.
Wade, W. & Forsyth, C. (2014). Administrative Law (11th ed.). Oxford University Press.

E — Industry Reports and Surveys Cisco Systems Engineering Team (2026).
BRKSPG-1180: Advanced Network Architectures for LLM Ingestion. Cisco Live EMEA,
February 2026.
ISACA (2026). AI Use Accelerates, While Governance and ROI Lag. ISACA AI Pulse Poll,
May 5, 2026. isaca.org/resources/ai-pulse-poll
LangChain (2026). SmithDB Inverted Index Performance Benchmarks. LangChain Platform, May 13, 2026.
Varma, S. (2026). Gartner Says Applying Uniform Governance Across AI Agents
Will Lead to Enterprise AI Agent Failure. Gartner Newsroom, May 26, 2026.
gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniformgovernance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure

F — Prior Implementation Watson, J.M. (2026). The Execution Boundary Principle: Deterministic Governance at the Point of Irreversible Action. Version 3.0. HyperEdgeX.
End of Bibliography — Version 1.0. All citations resolved.
