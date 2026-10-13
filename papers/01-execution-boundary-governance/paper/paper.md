---
title: "Execution-Boundary Governance"
subtitle: "A Runtime Control Model for Autonomous Systems"
paper_number: 1
version: "2.1"
author: "Jonathan M. Watson"
date: "2026-07"
series: "The Machine Speed Papers"
canonical_pdf: "paper.pdf"
license: "CC-BY-4.0"
---

# Execution-Boundary Governance

*A Runtime Control Model for Autonomous Systems*

**Jonathan M. Watson** — The Machine Speed Papers, No. 1 — Version 2.1 — 2026-07

---

*Machine-readable text derived from the canonical PDF (`paper.pdf`). In case of any discrepancy, the PDF governs.*

*Note: the PDF title page states version 2.0; this file is released as version 2.1.*

## Abstract

Current AI governance frameworks focus on policy, oversight, documentation, transparency, and post-execution accountability. As autonomous systems gain the ability
to execute transactions, invoke tools, modify records, move funds, and trigger physical
actions, governance must operate within finite latency budgets.
This paper proposes Execution-Boundary Governance (EBG), a framework that distinguishes interpretive governance from executable governance and introduces the Executable Governance Kernel (EGK) — a minimal, deterministic, tamper-resistant mechanism operating at the final control point preceding autonomous action.
The paper advances seven claims. First, existing AI governance frameworks contain
no latency model and cannot distinguish between a system that prevents an inadmissible action and a system that documented one. Second, governance effectiveness is
formally bounded by a latency condition: governance latency must be less than action
latency, or governance becomes observational rather than controlling. Third, human institutions subsidized governance complexity with human decision latency — a subsidy
that autonomous systems cancel. Fourth, the transition from interpretive to executable
governance requires governance compilation: the transformation of human-readable
policy into machine-enforceable constraints before the execution boundary is reached.
Fifth, the kernel enforcing those constraints must satisfy five properties — complete
mediation within defined consequence scope, determinism, latency compatibility, tamper resistance, and evidence generation — and must be minimal rather than layered.
Sixth, liability naturally converges on the execution boundary as the last point at which
control was possible. Seventh, insurance underwriting of autonomous systems will
require execution-time evidence — contemporaneous proof of governance presence —
rather than post-hoc documentation.
These claims are derived from first principles and supported by convergent independent developments across governance theory, cybersecurity, safety engineering, financial market design, edge infrastructure, liability doctrine, and insurance underwriting.
The paper does not argue for the removal of human oversight. It argues for its correct positioning — upstream of the execution boundary, where interpretation belongs,
rather than at the boundary itself, where only enforcement is possible.
The constraint the paper identifies is not invented. It was discovered. It exists whether
or not it is instrumented.

A note on human oversight
This paper does not argue that human oversight should be removed from autonomous
systems. It argues that human oversight must be correctly positioned. Interpretive governance — the deliberative, contextual, judgment-based governance that courts, committees, and compliance teams perform — belongs upstream of the execution boundary, where it can do the work it was designed to do. At the execution boundary itself,
the time for interpretation has passed. What remains possible is enforcement. The paper’s argument is about sequence, not substitution.

## Chapter 1 — The Human-Speed Economy

For most of recorded history, every consequential decision passed through a biological
processor. A judge deliberated. A banker approved. A regulator reviewed. An auditor
inspected.
This was not a design choice. It was a physical constraint.
Human cognition imposed a natural speed limit on economic and institutional life.
Courts assumed time for deliberation. Contracts assumed time for review. Insurance
assumed time for loss assessment. Regulation assumed time for human oversight.
Every institution humanity built — legal systems, financial markets, corporations, governments — was architecturally optimized around a single shared assumption: that the
entity making consequential decisions was human, and that human decision latency
was the floor below which no process needed to operate.1
This assumption was so universal it became invisible.
Nobody wrote it down because nobody needed to. There was no alternative substrate.
Human cognition was not one option among many. It was the only option available.
The institutions that emerged from this constraint were not merely compatible with
human latency. They were expressions of it. Deliberation, appeals, audit cycles, review boards, committee approvals — these are not bureaucratic preferences. They are
adaptations to the operating characteristics of the only decision-making substrate that
existed.
For thousands of years, this held.
The human-speed economy was not simply the dominant economy. It was the only
economy anyone had ever known.

## Chapter 2 — Human Governance and Human Latency

Human governance is not slow by accident. It is slow by design.
Every mechanism that defines modern governance — appeals, reviews, audits, committees, oversight boards — assumes that time exists between a decision and its consequence. Time to object. Time to correct. Time to reverse.
This assumption is so deeply embedded in legal and institutional architecture that it
rarely appears as an assumption at all. It appears as procedure.
Due process is latency, formalized.2

       The framing of institutions as expressions of human cognitive constraints rather than deliberate design choices is developed in Simon, H.A. (1947). Administrative Behavior: A Study of Decision-Making Processes in Administrative Organizations. Macmillan; and North, D.C. (1990). Institutions, Institutional Change
and Economic Performance. Cambridge University Press.
       The formalization of procedural delay as a governance mechanism is analyzed in Fuller, L.L. (1964).
The Morality of Law. Yale University Press. The statutory expression of this principle in United States
administrative law appears in the Administrative Procedure Act (1946), 5 U.S.C. §§ 500–596, which institutionalizes notice, comment, and review periods as governance requirements.

The right of appeal is latency, institutionalized.
The audit cycle is latency, scheduled.
None of these mechanisms were designed for speed. They were designed for correctness — and correctness, in a human-speed system, could always be purchased with
time. If a decision was wrong, time existed to identify the error, convene the relevant
parties, and apply a remedy.
Governance latency was not a cost to be minimized. It was the medium through which
governance operated.
This created a set of structural assumptions that persisted across centuries and institutions. That a human would initiate every consequential action. That a human could
be held accountable for every consequential outcome. That time would exist between
action and irreversibility. That the volume of decisions would remain within human
review capacity.
These assumptions were never stated as design parameters because they never needed
to be. They were simply true.
They are no longer simply true.

## Chapter 3 — The Human Latency Subsidy

Autonomous systems did not create a new problem. They revealed a hidden assumption.
For decades, digital systems operated at speeds far exceeding human cognition.
Databases processed queries in milliseconds. Networks routed packets in microseconds. Yet governance kept pace — not because it was fast, but because something else
was slow.
The human was slow.
Every digital transaction contained a human pause. A click. A confirmation. A signature. A review. That pause — invisible, unmeasured, taken entirely for granted — was
the latency subsidy that governance had always been spending without knowing it.
Consider a purchase. Between the intention to buy and the completed transaction, a
human moment exists. At that moment, fraud detection runs. Policy checks execute.
Compliance conditions are evaluated. Risk scores compute.3 The human never noticed
because the result was already there when they looked.
The governance didn’t complete in time because it was fast. It completed in time because the human was slow.4

       Transaction-level fraud detection and compliance check latency benchmarks are documented in Federal Reserve (2022). Federal Reserve Payments Study. Board of Governors of the Federal Reserve System.
       The human pause as a structural assumption in digital commerce architecture is documented in Amazon.com Inc. (1999). United States Patent No. 5,960,411 — Method and System for Placing a Purchase Order
via a Communications Network. United States Patent and Trademark Oﬀice. The patent explicitly architects
around the interval between human intent and transaction commitment.

Autonomous systems cancel that subsidy.
When an agent initiates a transaction, there is no human pause. No click. No confirmation interval. The latency budget that governance had always borrowed from human
reaction time is no longer available.
This is not a speed problem. It is a subsidy removal.
Every governance mechanism that was calibrated — consciously or not — to the rhythm
of human initiation must now operate without that rhythm. The budget it was spending
was never its own.

## Chapter 4 — The Machine-Speed Economy

The human pause is gone.
Not diminished. Not compressed. Gone. When an autonomous agent initiates an action, no biological processor stands between intention and execution. No click. No
confirmation. No moment of human hesitation in which governance could quietly do
its work.
This is the structural break.
Throughout economic history, decision frequency was bounded by human processing
capacity. A trader could place only so many orders. A loan oﬀicer could approve only
so many applications. A compliance oﬀicer could review only so many transactions.
Volume had a human ceiling, and that ceiling was also a governance floor.
Autonomous systems remove the ceiling.
An agent can initiate thousands of actions in the interval a human requires to read a
single notification.5 It can call tools, execute transactions, modify records, and trigger
downstream effects at a rate that has no historical precedent and no natural governance
mechanism designed to meet it.
This is not merely a quantitative change — more decisions per second. It is a qualitative
change in what governance mechanisms can physically do.
Human-speed governance was not designed for a world where the decision-maker
never pauses. It was designed for a world where pausing was unavoidable.
That world is ending.
What replaces it is not yet fully defined. But the first requirement is clear: any governance architecture that assumes a human pause will fail — not occasionally, not at the
margins, but structurally, by design, every time an autonomous system acts.

      Human reaction time — the biological floor on decision latency — is established at approximately
200-250 milliseconds in Donders, F.C. (1868). Over de snelheid van psychische processen. Onderzoekingen gedaan in het Physiologisch Laboratorium der Utrechtsche Hoogeschool. English translation: On the speed
of mental processes (1969), Acta Psychologica, 30, 412–431. Agentic action throughput is documented in
Anthropic (2024). Claude Model Card; OpenAI (2023). GPT-4 Technical Report.

## Chapter 5 — Governance Has No Theory of Time

NIST. ISO 42001. The EU AI Act. The NIST AI Risk Management Framework.6 Read
them carefully, and you will find something missing.
Not missing by accident. Missing by assumption.
None of them contain a latency model.
They specify what must be governed. They specify who bears accountability. They
specify which records must exist, which disclosures must be made, and which oversight
mechanisms must be in place. They are detailed, carefully constructed, and in many
respects genuinely useful.
But none of them specify when governance must occur relative to the action it is meant
to govern.
This is not a minor omission. It is a foundational one.
A governance framework without a theory of time cannot distinguish between two fundamentally different things: a system that prevented an inadmissible action, and a system that documented one. Both can produce a compliance report. Both can satisfy an
audit. Only one actually governed anything.
The absence of a latency model means that existing frameworks are, in principle, equally
satisfied by a system that stops a harmful action before it occurs and a system that
generates a detailed log of the harmful action after it occurs.
That equivalence is not a feature. It is a flaw.
Governance that cannot specify when it must operate relative to action cannot guarantee that it operates before action. And governance that operates after action is not
governance. It is record-keeping with ambitions.
The frameworks are not wrong about what they require. They are incomplete about
when those requirements must be met for them to constitute control rather than documentation.
That incompleteness is what this paper addresses.

      The four frameworks cited are: National Institute of Standards and Technology (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. U.S. Department of Commerce; ISO/IEC
42001:2023. Information Technology — Artificial Intelligence — Management System. International Organization for Standardization; European Parliament & Council of the European Union (2024). Regulation (EU)
2024/1689 on Artificial Intelligence (EU AI Act). Oﬀicial Journal of the European Union. None of these
frameworks specify a timing requirement for when governance must operate relative to the action being
governed.

## Chapter 6 — Governance Latency and Action Latency

Two concepts. One condition.
Governance latency is the time required to evaluate whether an action is admissible —
to check authority, apply policy, assess constraints, and reach a determination.
Action latency is the time available between the moment an autonomous system proposes an action and the moment that action commits — the interval within which any
determination must be reached if it is to influence the outcome.
These two intervals exist in every autonomous system. In human-speed systems, they
were never in tension. Governance latency was milliseconds or minutes. Action latency
was hours or days. The gap was so wide that it required no management.
That gap is closing.
As autonomous systems compress action latency — executing in milliseconds, chaining
steps without pause, operating continuously across distributed infrastructure — governance latency becomes the binding constraint. Not policy quality. Not oversight intent.
Not regulatory ambition.
Time.
The controlling condition is simple:
Governance latency must be less than action latency.
When this condition holds, governance can influence outcomes. It operates before commitment. It can allow, deny, or defer.
When this condition fails, governance cannot influence outcomes. It can only observe
them. It becomes a documentation system wearing the clothes of a control system.
This paper refers to this as the latency condition.7 It has no exception for good intentions. A governance framework that requires more time than is available is not a slow
governance framework. It is not a governance framework at all. It is a reporting framework that arrived after the fact.
The latency condition is binary. Either governance completes within the available interval, or it does not. There is no partial credit for almost completing in time. An action
that commits before admissibility is determined is an ungoverned action, regardless of
how sophisticated the governance system that follows it.
Everything that follows in this paper is a consequence of taking the latency condition
seriously.

      The formal treatment of deadline constraints in real-time systems — the closest analogue in the existing literature to the latency condition as defined here — is established in Liu, C.L. & Layland, J.W. (1973).
Scheduling algorithms for multiprogramming in a hard-real-time environment. Journal of the ACM, 20(1),
46–61. The latency condition as applied to governance architecture is an original contribution of this paper,
extending the real-time scheduling framework to the governance domain.

## Chapter 7 — Time-Domain Mismatch

The latency condition is a symptom of a deeper structural problem.
Human governance and autonomous execution do not merely operate at different
speeds. They operate in different time domains.
A time domain is not simply a rate of operation. It is the complete set of assumptions a
system makes about the interval between decision and consequence — how long that
interval is, what can happen within it, and what mechanisms are available to act during
it.
Human governance was built for a time domain defined by biological constraints.8 Decisions took seconds, minutes, hours, or days because human cognition, communication,
and coordination imposed those timescales. Every governance mechanism — review,
appeal, audit, oversight — was designed to fit within that domain and exploit its intervals.
Autonomous execution operates in a different time domain entirely. Decisions take
milliseconds. Actions chain without pause. Consequences accumulate faster than any
human review mechanism can track.
These two domains are not merely offset in speed. They are structurally incompatible
in the mechanisms they make available.
In the human time domain, oversight is possible because the interval between decision
and consequence is long enough for a human to observe, evaluate, and intervene. In the
machine time domain, that interval may be shorter than human reaction time — shorter,
in some cases, than the time required to read a single line of a governance document.
Time-domain mismatch is therefore not a problem of governance ambition or regulatory will. It is a problem of physical compatibility.
A governance mechanism designed for one time domain does not degrade gracefully
when applied to another. It does not slow things down or introduce friction. It simply
fails to engage. The action occurs. The consequence commits. The governance mechanism arrives to find nothing left to govern.
This is the core failure mode that execution-boundary governance is designed to address. Not slow governance. Not insuﬀicient governance. Governance that operates
in the wrong time domain entirely — and therefore cannot, by construction, remain
causally relevant to the actions it was designed to control.
Recognizing time-domain mismatch as a structural condition rather than a performance
problem changes what solutions are possible. You cannot solve a time-domain mismatch by making human governance faster. Human governance optimized for speed
is still human governance — deliberative, interpretive, latency-tolerant by design. It
      The formal model of human processing time establishing the biological floor on decision latency is
developed in Card, S.K., Moran, T.P., & Newell, A. (1983). The Psychology of Human-Computer Interaction.
Lawrence Erlbaum Associates. The GOMS model quantifies human cognitive, motor, and response times
as architectural constraints on system design — constraints that governance frameworks have historically
been calibrated to exploit.

will always be outpaced by a system operating in a fundamentally different time domain.
The solution is not acceleration. It is translation — converting governance from a form
native to the human time domain into a form capable of operating in the machine time
domain without losing its essential properties.
That translation is what the remainder of this paper describes.

## Chapter 8 — Why Faster Systems Win

History does not record the governance frameworks that failed to keep pace with faster
systems. It records the faster systems.
Every major compression of economic velocity — maritime trade, rail, telegraph, telephony, electronic markets, algorithmic trading — followed the same pattern.9 Faster
systems did not wait for governance to catch up. They created facts on the ground.
Governance adapted afterward, imperfectly, to a world already reshaped by the speed
advantage.
This is not a story of malice. It is a story of selection pressure.
Economic systems select for eﬀiciency. Eﬀiciency favors speed. Speed favors lighter
governance. Not because participants choose to evade governance, but because under
competitive pressure, any friction that can be removed will be removed. Governance
that imposes latency costs is friction. Friction is a competitive disadvantage. Competitive disadvantages are eliminated.
The result is predictable. Governance architectures that cannot operate within the latency envelope of the systems they govern are not repealed. They are bypassed. They
remain on the books, satisfied on paper, while the actual decisions occur at speeds they
were never designed to reach.
This dynamic has a name in evolutionary biology: selection pressure.10 Organisms that
cannot adapt to environmental conditions do not argue with the environment. They
disappear. Governance frameworks face the same pressure. A framework that requires
human review of every autonomous action will not slow down autonomous systems. It
will be routed around by operators who cannot afford the latency penalty in competitive
markets.
The implication is uncomfortable but important. Governance that cannot operate at
machine speed will not govern machine-speed systems. It will govern the paperwork
       The historical pattern of velocity compression displacing prior governance structures is documented
across transport and communication in Chandler, A.D. (1977). The Visible Hand: The Managerial Revolution
in American Business. Harvard University Press. The most recent and precise example — algorithmic
trading reshaping market structure faster than regulatory response — is documented in SEC & CFTC
(2010). Findings Regarding the Market Events of May 6, 2010 (Flash Crash Report); and SEC (2010). Concept
Release on Equity Market Structure. Release No. 34-61358.
       The application of evolutionary selection pressure logic to competitive economic systems is established in Alchian, A.A. (1950). Uncertainty, evolution, and economic theory. Journal of Political Economy,
58(3), 211–221. The analogy used here is structural, not biological: systems that cannot survive the cost
pressures of their competitive environment are displaced regardless of their intrinsic merit.

that those systems generate. The systems themselves will operate outside its reach —
not by design, but by physics.
The full consequences of this selection dynamic for autonomous systems and their markets are developed in Part VI. What matters here is the foundational pattern: speed
advantage compounds, governance lag accumulates, and the gap between what governance intends and what markets do is filled permanently by whoever moves first.
The alternative to governance that can operate at execution speed is not slower machines. It is ungoverned ones.

## Chapter 9 — Interpretive Governance and Its Limits

Not all governance is broken. Some of it was never designed to control execution — and
should not be faulted for that.
Interpretive governance is the dominant mode of human institutional life. It is humanreadable, contextually rich, deliberately flexible, and latency-tolerant by design. Corporate policy. Regulation. Ethical frameworks. Risk committees. Board oversight. These
mechanisms were built to handle ambiguity — to weigh competing considerations, apply judgment, and produce nuanced determinations that no rule set could anticipate
in advance.
This is not a weakness. It is the point.
Interpretive governance excels at the things machines cannot do: reading intent, weighing context, applying principles to novel situations, and producing legitimacy through
process. A court does not merely produce a verdict. It produces a reasoned decision
that society can inspect, argue with, and build upon. That process requires time, and it
earns its latency.
Most readers of this paper will have spent their entire lives inside interpretive governance without ever having named it. It is the water they swim in. Courts. Contracts.
Compliance departments. Audit cycles. Board oversight. The assumption that somewhere, someone with judgment will read the situation and decide what the rule actually
means in this particular case.
That assumption is so embedded in institutional life that it rarely surfaces as an assumption at all. It surfaces as procedure.
Consider how interpretive governance actually works in practice.
A contract says the vendor must use “reasonable efforts.”11 No one defines reasonable
in the contract. No one can. Reasonable is context-dependent, relationship-dependent,
industry-dependent, and fact-specific in ways that no drafter can fully anticipate. When
a dispute arises, a lawyer argues what reasonable means in this context. A judge or

      The reasonable efforts standard as a documented example of deliberate ambiguity in commercial law
appears in Uniform Commercial Code § 2-306 (1952, as amended). American Law Institute and Uniform
Law Commission. The leading case on judicial interpretation of this standard is Bloor v. Falstaff Brewing
Corp., 601 F.2d 609 (2d Cir. 1979).

arbitrator decides. The decision becomes precedent, shaping what reasonable means
next time — until circumstances change enough that the question reopens.
A financial regulator says a bank must maintain “adequate capital buffers.”12 Adequate
is not a number. It is a judgment. Regulators publish guidance. Banks hire compliance
teams to interpret the guidance. Auditors assess whether the interpretation was defensible. In edge cases, regulators issue no-action letters. Courts occasionally weigh in.
The meaning of adequate is never fully settled. It is continuously negotiated.
A healthcare policy says physicians must exercise “clinical judgment.”13 Clinical judgment is not an algorithm. It is the accumulated expertise of a trained professional applied to a specific patient in a specific moment. No policy document can fully specify
it. No rule set can replace it. The law protects its exercise precisely because it cannot be
reduced to procedure.
This is interpretive governance in its natural habitat. It is not a design flaw. It is a
design achievement. The ambiguity is the point. It allows governance to extend across
situations that rule-makers could not anticipate, to handle novel circumstances without
requiring new legislation, and to import human wisdom into spaces where rigid rules
would produce absurd results.
A judge can interpret “reasonable.” A CPU cannot.
An auditor can debate “material.” A kernel cannot.
A compliance oﬀicer can weigh context. A boundary gate cannot.
Interpretive governance works because it runs on a substrate capable of handling ambiguity: human cognition. It assumes time for deliberation. It assumes the capacity for
judgment. It assumes that the entity applying the rule can read the situation, weigh
competing considerations, and arrive at a determination that is defensible even if it is
not perfectly predictable.
These assumptions are not limitations. In a human-speed system, they are strengths.
The flexibility of interpretive governance is what allows a body of law developed over
centuries to remain applicable to circumstances its authors could not have imagined.
The failure begins when this mode of governance is moved into a machine-speed execution path.
Not because interpretive governance becomes wrong. Because it becomes impossible.
The ambiguity that interpretive governance was designed to handle cannot be resolved
in the interval available at machine speed. The judgment it was designed to apply requires time that the execution boundary does not provide. A governance mechanism
       The adequate capital buffers standard as interpretive governance is documented in Basel Committee
on Banking Supervision (2010). Basel III: A Global Regulatory Framework for More Resilient Banks and Banking Systems. Bank for International Settlements. The interpretation machinery surrounding it — guidance,
no-action letters, supervisory discretion — is documented in Federal Reserve (2011). SR Letter 12-7: Supervisory Guidance on Model Risk Management. Board of Governors of the Federal Reserve System.
       The legal protection of clinical judgment from reduction to procedure is established in Cruzan v.
Director, Missouri Department of Health, 497 U.S. 261 (1990). The professional standard is codified in
AMA Council on Ethical and Judicial Affairs (2016). AMA Code of Medical Ethics, Opinion 1.1.1: PatientPhysician Relationships. American Medical Association.

that asks “what does reasonable mean in this context?” cannot complete that inquiry in
25 milliseconds. It cannot complete it in 250 milliseconds. The question itself assumes
a deliberative process that the latency condition does not permit.
Interpretive governance, when placed within a machine-speed execution path, does not
degrade gracefully. It does not produce approximate answers or rough heuristics. It
produces nothing — because the action has already been committed before the interpretation could complete.
This is not a criticism of interpretive governance. It is a statement about domain compatibility. Interpretive governance is native to the human time domain. It evolved there.
It thrives there. It is the right tool for every governance problem that can be solved with
time and judgment.
It is simply the wrong tool for the execution boundary.
The execution boundary does not need judgment. By the time an action reaches it, judgment should already have been exercised — upstream, by humans, in the interpretive
governance processes that produced the policy now being enforced. The boundary
needs the result of that judgment, compiled into a form it can evaluate in the available
interval.
That compilation — the transformation of interpretive governance output into
executable governance input — is what the following chapters describe.
Interpretive governance does not disappear in a machine-speed system. It moves upstream. Its job is to decide, in advance, what the answer will be. The execution boundary’s job is to enforce that answer, deterministically, before the action commits.
Those are two different jobs. They require two different mechanisms. Confusing them
— placing interpretive governance at the execution boundary, expecting judgment
where only enforcement is possible — is the architectural error that most current AI
governance makes.

## Chapter 10 — Narrative Governance vs Controlling Governance

There is a distinction that current governance literature does not make cleanly enough.
Some governance controls outcomes. Some governance describes them.
These are not the same thing. They are not even close to the same thing. But they are
routinely treated as equivalent — in compliance frameworks, in audit requirements, in
regulatory filings, and in the governance sections of AI system documentation. The
conflation is not deliberate. It is a consequence of building governance frameworks
in an era when control and description were nearly always simultaneous. If you documented what happened, you had, by implication, been present when it happened.
Presence implied the possibility of intervention. Intervention implied control.
That implication no longer holds.
Narrative governance produces records. It generates logs, audit trails, explainability
reports, incident analyses, and compliance documentation. It answers the question:

what happened, and can we account for it? In a human-speed system, this was suﬀicient because the humans producing the narrative were, in principle, also capable of
intervening. The record and the control were produced by the same process.
Controlling governance prevents outcomes. It evaluates admissibility before commitment. It operates at the point where an action is proposed but not yet executed, where
a determination can still change what happens. It answers a different question entirely:
should this action be permitted?
The difference is not philosophical. It is causal.
A system that logs every transaction in perfect detail has not governed those transactions. It has documented them. The transactions occurred. The consequences committed. The log was produced afterward, by a system that was never in a position to
intervene. This is narrative governance. It has genuine value — for accountability, for
learning, for legal proceedings. But it is not control.
A system that evaluates each transaction before execution and permits or denies it based
on policy has governed those transactions. Not perfectly. Not with human nuance. But
causally — in the sense that its determination influenced whether the action occurred
at all.
Most current AI governance is narrative.
This is not an accusation. It is an observation about what is physically possible given the
latency condition. When governance latency exceeds action latency, narrative is what
remains. You cannot control what has already happened. You can only describe it.
The transition from narrative to controlling governance is therefore not a matter of
adding more oversight, more documentation, or more accountability mechanisms. It
is a matter of moving the governance operation to a point in time where it can still
influence outcomes — before the action commits, not after.
That point is the execution boundary.
Everything before it is interpretation. Everything after it is narrative. The boundary
itself is the only place where control remains physically possible.14

## Chapter 11 — Executable Governance

Interpretive governance reasons. Executable governance decides.
The distinction is not one of sophistication. It is one form. Interpretive governance
operates in natural language — flexible, contextual, and amenable to judgment. Executable governance operates in logic — deterministic, binary, latency-compatible. One
is designed to be read by humans. The other is designed to run at machine speed.
Executable governance is not a new idea. It appears in several existing disciplines under
different names.
     No new citations in this chapter (10). The argument is derived from the latency condition established
in Chapter 6 and the frameworks surveyed in Chapter 5. The distinction between narrative and controlling
governance is an original conceptual contribution of this paper.

In cybersecurity, it is the reference monitor — a mechanism invoked on every access attempt that enforces a security policy deterministically, without exception and without
deliberation.15 In safety engineering, the safety kernel is the minimal verified component that enforces critical constraints regardless of what the rest of the system does.16
In financial markets, it is the pre-trade risk check — a hard limit evaluated before every
order reaches the exchange, operating in microseconds, with no appeal and no override
at the moment.17
What these mechanisms share is more important than what distinguishes them. Each
operates before commitment. Each produces a binary outcome. Each is designed to
complete within a bounded time. Each is non-negotiable at the point of execution.
None of them deliberate. None of them contextualize. None of them weigh competing considerations. They enforce. Deliberation happened earlier, when the policy was
written. At the execution point, the time for deliberation is over.
This is not a limitation. It is a design requirement.
An executable governance mechanism that deliberates at execution time is not an executable governance mechanism. It is an interpretive governance mechanism operating
under time pressure — which is precisely the condition under which interpretive governance fails.
The value of executable governance is not that it makes better decisions than interpretive governance. It makes faster decisions — fast enough to be causally relevant at the
execution boundary. The quality of those decisions depends entirely on the quality of
the policy compiled into them. Which is why the relationship between interpretive and
executable governance is not competitive. It is sequential.
Interpretive governance sets policy. Executable governance enforces it.
The gap between those two activities — the process by which human policy becomes
machine-enforceable constraint — is the subject of the next chapter.

       The reference monitor concept is introduced in Anderson, J.P. (1972). Computer Security Technology
Planning Study. ESD-TR-73-51. Electronic Systems Division, Air Force Systems Command, Hanscom AFB,
Massachusetts. Its three defining properties — complete mediation, tamper resistance, and verifiability —
are the foundational prior art for the EGK properties defined in Chapter 14.
       The safety kernel concept is codified in IEC 61508 (2010).               Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems. International Electrotechnical Commission,
Geneva; and ISO 26262 (2018). Road Vehicles — Functional Safety. International Organization for Standardization, Geneva.
       The regulatory mandate for pre-trade risk controls is established in FINRA Rule 15c3-5 (2010). Market
Access Rule. Financial Industry Regulatory Authority; and SEC Release No. 34-63241 (2010). Risk Management Controls for Brokers or Dealers with Market Access. U.S. Securities and Exchange Commission.

## Chapter 12 — Governance Compilation

Policy does not arrive at the execution boundary ready to enforce. It arrives as language
— ambiguous, contextual, written for human readers who will apply judgment when
edge cases emerge. Before policy can operate at machine speed, it must be transformed.
That transformation is governance compilation.
The analogy to software compilation is precise.18 Source code is written for humans
— readable, structured around human concepts, tolerant of ambiguity that a compiler
will resolve. The compiler transforms it into something a machine can execute directly:
deterministic, binary, operating without interpretation. The source code and the executable are expressions of the same intent in two different forms. One is for reading.
One is for running.
Governance compilation performs the same transformation on policy. Humanreadable rules — thou shalt not move funds without authorization, thou shalt not
access records outside permitted scope, thou shalt not execute irreversible actions
above threshold X without escalation — are translated into machine-enforceable
constraints that can be evaluated deterministically, within a bounded time, at the
moment an action is proposed.
This is not a trivial process. Natural language policy contains ambiguity that is a feature, not a bug — it allows human judgment to handle cases the policy author did not
anticipate. Compilation requires that ambiguity to be resolved in advance, before the
execution boundary is reached. Edge cases that a human governance committee would
deliberate over must be pre-decided, encoded, and locked.
This creates a fundamental sequencing requirement. Interpretation must precede compilation. Compilation must precede enforcement. The execution boundary is not a
place for deliberation. By the time an action reaches the boundary, every relevant policy question must already be resolved and encoded in a form the kernel can evaluate in
the available interval.
Governance compilation is therefore not merely a technical step. It is the mechanism
by which human governance extends its authority into machine-speed systems — not
by being present at execution, but by having decided, in advance, what the answer will
be.
The compilation problem is not yet fully solved, but it is being actively addressed.
Prose2Policy demonstrates an end-to-end pipeline that ingests natural-language access
control policies and compiles them into executable Rego modules, achieving a 95.3%
compile rate on benchmark datasets.19 Policy-to-Tests extends this with SMT-based
      The formal treatment of compilation as a source-to-executable transformation is established in Aho,
A.V., Lam, M.S., Sethi, R., & Ullman, J.D. (2006). Compilers: Principles, Techniques, and Tools (2nd ed.).
Addison-Wesley. The governance compilation analogy is original to this paper — the analogy is structural, not technical: both processes transform human-readable intent into machine-executable form while
resolving ambiguity in advance.
      Prose2Policy (P2P): A Practical LLM Pipeline for Translating Natural-Language Access Policies into
Executable Rego. arXiv:2603.15799. The 95.3% compile rate is reported on the ACRE benchmark dataset
with automated unit test validation.

consistency auditing — before compiled rules are deployed, a satisfiability solver
evaluates them for logical contradictions and ruleset coherence.20 These systems
demonstrate that governance compilation is not waiting for a theoretical breakthrough.
It is being operationalized now, domain by domain, with human escalation handling
residual ambiguity.
The EGK does not require complete compilation to be effective. It requires suﬀicient
compilation — enough to govern the consequence classes that can be anticipated, while
preserving human escalation paths for those that cannot.
The entity that holds the compiled result and enforces it at the execution boundary is
the subject of the next chapter.

## Chapter 13 — Authority Migration

When governance fails to reach machine speed, authority does not disappear. It migrates.
This is one of the least-examined dynamics in current AI governance literature and one
of the most consequential. The assumption embedded in most regulatory frameworks
is that authority resides where policy places it — with the regulator, the operator, the
accountable human. That assumption holds when governance can reach the execution
surface. When it cannot, authority relocates to whoever controls that surface, regardless
of where policy intended it to sit.
The migration is not deliberate. No platform operator decides to absorb regulatory
authority. No infrastructure provider sets out to become a de facto governance body.
The migration occurs because decisions must be made, actions must be permitted or
denied, and if the designated governance mechanism cannot operate at the required
speed, something else will fill the gap.21
That something else is usually the execution surface itself.
The model provider whose system prompt shapes agent behavior. The platform operator whose terms of service define permitted actions. The infrastructure owner whose
rate limits and access controls determine what an agent can reach. None of these entities was designated as a governance authority. All of them are exercising governance
functions — because governance that cannot operate at execution speed has, in practice,
ceded that function to them.

       Executable Governance for AI: Translating Policies into Rules Using LLMs. arXiv:2512.04408. The
SMT-based consistency auditing uses Z3 or equivalent satisfiability solvers to verify ruleset coherence
before deployment.
       The baseline model for authority migrating to whoever controls the execution surface — rather than
remaining with whoever policy designates — draws on two bodies of literature. Stigler, G.J. (1971). The
theory of economic regulation. Bell Journal of Economics and Management Science, 2(1), 3–21, establishes
regulatory capture as the mechanism by which authority migrates to those closest to the regulated activity. Lessig, L. (1999). Code and Other Laws of Cyberspace. Basic Books, establishes that architectural control
of a system’s execution layer constitutes a form of governance authority independent of formal designation. Authority migration as defined in this paper is an original synthesis of these mechanisms applied to
autonomous system deployment.

This has a precise implication for regulatory design. A framework that places authority
in a human governance body but fails to specify how that authority reaches the execution boundary has not retained authority. It has created a vacuum. Vacuums fill.
The question is not whether authority will migrate when governance fails to keep pace.
The question is where it will migrate to, and whether that destination is accountable to
anyone.
Authority migration is not a future risk. It is a present condition. Every autonomous
system operating today without a defined execution-boundary governance architecture
has already ceded its effective authority to the execution surface — to the infrastructure,
the platform, the model provider, or the agent’s default behavior. The policy documents that describe intended authority and the architectural reality of where authority
actually operates are, in most current deployments, different things.
Execution-boundary governance addresses authority migration not by preventing it
but by making it unnecessary. When a compiled governance policy enforces authority
deterministically at the execution boundary, authority need not migrate. It is already
there, encoded and operational, before the action occurs.
The alternative — leaving the execution surface ungoverned and hoping that policy
intent survives the latency gap — is not a governance strategy. It is an optimistic assumption about a gap that the latency condition does not permit.

## Chapter 14 — The Executable Governance Kernel

There must be a thing that enforces.
Not a policy. Not a principle. Not a framework. A thing — operational, deterministic, present at the execution boundary before every consequential action, capable of
reaching a determination within the available latency budget and producing a result
the system is bound to respect.
That thing is the Executable Governance Kernel.
The EGK is not defined here by its implementation. Implementations will vary — by
system, by domain, by latency budget, by consequence class. What is defined here are
the properties that any implementation must satisfy to constitute genuine governance
at the execution boundary, rather than its appearance.
The first property is complete mediation within the defined scope of consequences.
The EGK must be invoked for every action classified as high-consequence or sovereignconsequence under the framework established in Chapter 16. Low-consequence actions
do not require full governance evaluation at the execution boundary — the consequence
classification is itself the governance decision. Once an organization has mapped its
execution surfaces using the boundary discovery methodology in Chapter 18 and identified the state changes that are irreversible, externally visible, or materially consequential, the EGK governs those points completely. Not partially. Not occasionally. The

requirement is complete mediation within the defined consequence scope — not universal instrumentation of every agent action regardless of weight. A governance mechanism that can be bypassed within its defined scope — even occasionally, even for actions
near the consequence threshold — is not a governance mechanism. It is a suggestion.22
The second property is determinism. Given the same inputs — proposed action, authority context, compiled policy, environmental state — the EGK must produce the
same output every time. Not a probabilistic assessment. Not a confidence score. A
determination: permit or deny. Determinism is not a limitation on sophistication. It is
the property that makes the EGK’s output trustworthy and its behavior auditable.23
The third property is latency compatibility. The EGK must complete its determination
within the available action latency. A kernel that produces correct determinations too
slowly is not a slow governance kernel. It is not a governance kernel at all. Latency
compatibility is not a performance optimization. It is a definitional requirement. The
specific latency envelope varies by deployment context — the 25-millisecond benchmark referenced throughout this paper represents current agentic system benchmarks
for high-consequence tool-call actions, not a universal threshold.24
The fourth property is tamper resistance. The EGK must be structurally isolated from
the agent whose actions it governs. An agent that can modify its own governance kernel
has no governance kernel. Tamper resistance in this context means structural isolation
from the governed agent — not a claim of absolute cryptographic security, which no
software implementation can guarantee unconditionally. The separation between the
governed system and the governing mechanism is not an architectural preference. It is
the condition that makes governance meaningful.25
The fifth property is evidence generation. Every determination the EGK makes must
produce an evidence artifact — a contemporaneous, tamper-evident record of what was
proposed, what policy applied, and what was determined. This artifact is not a log. It is
proof. Proof that governance was present. Proof that a determination was made. Proof
that the action that followed was permitted, or that an action that did not follow was

       The complete mediation property derives from the reference monitor concept established in Anderson, J.P. (1972). Computer Security Technology Planning Study. ESD-TR-73-51. Electronic Systems Division,
Air Force Systems Command, Hanscom AFB, Massachusetts. The extension to consequence-scoped rather
than universal mediation is an original contribution of this paper, grounded in the consequence classification framework developed in Chapter 16.
       The formal model for deterministic policy enforcement as the basis for trustworthy and auditable
governance outputs is developed in Schneider, F.B. (2000). Enforceable security policies. ACM Transactions
on Information and System Security, 3(1), 30–50.
       The 25-millisecond benchmark is derived from production agentic system latency data reported in
Cisco Systems Engineering Team (2026). BRKSPG-1180: Advanced Network Architectures for LLM Ingestion.
Cisco Live EMEA, February 2026; and LangChain (2026). SmithDB Inverted Index Performance Benchmarks.
LangChain Platform, May 13, 2026, which reports P50 trace latencies of 71-92ms for agentic workflows.
       The tamper resistance property derives from the reference monitor concept in Anderson, J.P. (1972).
Computer Security Technology Planning Study. ESD-TR-73-51. The qualification that structural isolation
— rather than absolute cryptographic security — is the operative requirement is original to this paper,
reflecting the practical constraints of software implementation at the execution boundary.

denied. The nature and legal suﬀiciency of this evidence artifact are developed fully in
Chapter 25.26
These five properties — complete mediation within defined consequence scope, determinism, latency compatibility, tamper resistance, evidence generation — are not a wish
list. They are the minimum conditions under which a mechanism can be said to govern
rather than observe.
The EGK is where compiled policy meets autonomous action. It is the point at which
human governance, transformed through compilation into executable form, becomes
causally relevant at machine speed.
Everything before it is preparation. Everything after it is consequence.

## Chapter 14A — Kernel Minimality

The instinctive response to any governance problem is to add more governance.
More layers. More reviewers. More checkpoints. More supervisory models. More escalation paths. More runtime monitors. More policy engines. More audit hooks. More
fallback systems. When the stakes are high, the instinct is to build bigger — to surround
the execution path with so many overlapping controls that nothing consequential can
escape notice.
That instinct is correct for interpretive governance. It is exactly wrong for the execution
boundary.
At the execution boundary, complexity is not safety. Complexity is a risk.
Consider the architecture that instinct produces. An agent proposes an action. A policy
engine retrieves and interprets applicable rules. A supervisory model evaluates context.
A risk scoring system assesses the proposal. An anomaly detector checks for unusual
patterns. A fallback model provides a second opinion. A human escalation path is
triggered if confidence falls below the threshold. A runtime checksum validates the
output of the preceding steps. The action executes.
This looks governed. Every step adds a layer of oversight. Every layer adds a degree of
assurance. The diagram is impressive. The compliance documentation is extensive.
But examine what has actually been built.
Each additional layer adds latency. Each additional component adds failure modes.
Each additional model introduces probabilistic variance — outputs that are not identical given identical inputs, that cannot be formally verified, that may disagree with
adjacent layers in ways the system cannot resolve deterministically. Each additional
escalation path introduces a surface through which compiled governance can be renegotiated at runtime. Each additional dependency introduces a point at which the chain

       Evidence generation as a safety kernel requirement is established in IEC 61508 (2010). Functional
Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems. § 7.4. International Electrotechnical Commission, Geneva. The extension of evidence generation to downstream legal, regulatory, and
insurance functions is an original contribution of this paper.

can fail silently, partially, or in ways that produce the appearance of governance without its substance.
This is governance accretion. More machinery, less certainty. More complexity, more
attack surface. More layers, more ways to fail at the moment that matters.
The architecture that survives scrutiny at the execution boundary is the opposite of
what instinct produces. It is not a stack of overlapping controls. It is a minimal surface
— the smallest mechanism capable of making an admissibility determination before the
action commits.
This is the Minimal Surface Principle.
The closer governance moves to the execution boundary, the smaller it must become.
The principle is not a preference for elegance. It is a consequence of the constraints
that govern the execution boundary. Latency budgets measured in milliseconds do
not accommodate iterative reasoning. Deterministic requirements do not accommodate probabilistic models. Tamper resistance requirements do not accommodate components that can be influenced by the agent under governance. Evidence generation
requirements do not accommodate systems whose internal state cannot be formally described.
Each of these constraints pushes in the same direction: toward a kernel that does almost
nothing, does it deterministically, and does it fast.
The kernel does not reason. Reasoning happened upstream, in the interpretive governance processes that produced the compiled policy now loaded into the kernel. The
kernel does not explain. Explanation happens downstream, in the evidence artifact the
kernel emits after each determination. The kernel does not negotiate. Negotiation is a
form of interpretation, and interpretation belongs upstream. The kernel does not call
another model, consult a policy engine at runtime, or ask a human. Each of those operations introduces latency, variance, or dependency that the execution boundary cannot
absorb.
The kernel evaluates. That is all.
It receives a structured description of the proposed action. It checks the authority context. It evaluates the proposal against the compiled constraint set. It produces a determination: permit or deny. It emits an evidence artifact that records the inputs, the
applied constraint version, the determination reached, and the timestamp. If it cannot complete this sequence — if its own operation cannot be confirmed — it fails safe,
denying execution rather than permitting an ungoverned action.
The structure of a valid kernel is therefore definable precisely:
A proposal object describing the action. An authority state describing who or what is
requesting it. A compiled constraint set encoding the admissible conditions. A deterministic evaluation function that takes those inputs and produces a binary output. A
decision output — permit or deny — that the system is bound to respect. An evidence
emission capturing the determination in real time. A declared failure posture specifying behavior when the evaluation cannot be completed.

Seven components. Each is necessary. None of them is a reasoning system, a policy
engine, a probabilistic model, or a supervisory layer.
The governance architecture surrounding this kernel may be arbitrarily rich. Upstream,
interpretive governance processes can be as deliberative, contextual, and layered as the
problem demands. Downstream, evidence management, audit systems, and accountability mechanisms can be as comprehensive as regulators require. The kernel does not
constrain what surrounds it. It constrains only what happens at the execution boundary
itself.
Human governance expands to handle ambiguity. Execution governance contracts to
eliminate it.
That sentence captures the architectural move precisely. The boundary between interpretation and enforcement is the boundary between expansion and contraction — between a governance surface that grows to accommodate uncertainty and a governance
surface that shrinks to exclude it.
An organization that builds a large, layered, probabilistic governance stack at the execution boundary has not built stronger governance. It has built a system that will fail
the latency condition, cannot be formally verified, generates ambiguous evidence, and
presents a larger attack surface than the threat it was designed to address.
An organization that builds a minimal, deterministic, tamper-resistant kernel at the execution boundary and places its interpretive governance upstream has built a system
that can satisfy the latency condition, can be formally verified against its compiled constraints, generates unambiguous evidence, and presents the smallest possible surface
for adversarial interference.
The minimal kernel is not a compromise. It is the correct architecture.
Smallness at the boundary is not a limitation. It is the proof that interpretation has been
completed before enforcement begins — that the hard work of governance happened
where it could be done properly, and that what remains at the execution boundary is
only what needs to happen there.27

       No new citations in this chapter. The Minimal Surface Principle is an original architectural contribution of this paper, derived from the five EGK properties established in Chapter 14 and the constraints
imposed by the latency condition established in Chapter 6. The seven-component kernel structure is an
original specification. The governance accretion anti-pattern is described here for the first time as a named
failure mode.

## Chapter 15 — Reasoning vs Execution

Autonomous agents do not act in a single step. They think, then act.
The reasoning phase is exploratory. An agent working through a complex task may
evaluate options, call retrieval tools, consult context, revise its approach, and chain intermediate steps before arriving at a consequential action. This phase is probabilistic,
iterative, and — critically — reversible.28 Nothing has happened yet. The agent is thinking.
The execution phase is different in kind, not degree. When an agent calls a tool that
moves funds, writes to a database, sends a communication, or triggers a physical effect,
it crosses from the domain of thought into the domain of consequence. The action
commits. The state of the world changes. Reversal, if possible at all, requires a separate
action with its own consequences.
This distinction matters for governance.
Governance applied uniformly across all agent steps — both reasoning and execution
— is governance misapplied. It imposes overhead on reversible cognitive steps where
the cost of error is low and the opportunity for self-correction is high. It burns latency
and tokens at every intermediate step.29 accumulating cost across what may be dozens
of reasoning cycles before a single consequential action occurs.
Governance concentrated at the execution boundary is governance correctly placed.
The reasoning phase can proceed without interruption. The agent thinks freely. At
the moment reasoning becomes action — at the precise point where reversibility ends
and consequence begins — the EGK engages.
One check. One determination. One evidence artifact. Not twenty checks distributed
across twenty reasoning steps. One check, at the only step that matters.
This is not a relaxation of governance. It is a concentration of it — placing governance
exactly where consequences originate and nowhere else.
The reasoning phase is not ungoverned in any meaningful sense. The agent reasons
within a context established by compiled policy — the authority tokens, the permission
boundaries, the constraint envelopes that define what actions are available to it. The
reasoning phase is shaped by governance, even when governance does not evaluate it at
each step. The EGK does not govern thought. It governs action. And it governs action
at the only point where governance is both causally necessary and computationally
feasible.

       The foundational distinction between reasoning traces and execution actions in LLM agents is established in Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing
reasoning and acting in language models. International Conference on Learning Representations (ICLR 2023).
The ReAct framework explicitly separates the probabilistic, iterative reasoning phase from the deterministic execution phase — the same distinction this paper applies to governance placement.
       Multi-step agent overhead patterns are documented in Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H.,
Zhang, J., … & Wen, J.R. (2024). A survey on large language model based autonomous agents. Frontiers of
Computer Science, 18(6). The survey documents that governance and policy evaluation distributed across
reasoning steps compounds latency and token costs multiplicatively rather than additively.

The boundary between reasoning and execution is therefore not merely an architectural
feature. It is the governance surface. Everything before it is thought. Everything after
it is consequence. The EGK sits at the threshold between the two.

## Chapter 16 — Consequence Classification

Not all autonomous actions are equal. Not all execution boundaries carry the same
weight.
An agent that retrieves a document operates in a different consequence class than an
agent that transfers funds. An agent that drafts a message operates in a different consequence class than an agent that sends one.
Current governance frameworks tend toward capability-based regulation30 — governing what a system can do based on its technical sophistication, model size, training data,
or overall risk profile. This is a reasonable starting point but an insuﬀicient endpoint. A
highly capable system performing a low-consequence action requires less governance
intensity at the execution boundary than a low-capability system performing a highconsequence one. Capability is a proxy for consequence. Consequence is the actual
variable that matters.
This paper proposes a three-tier classification of consequences as the basis for calibrating governance intensity at the execution boundary.
The first tier is low consequence. Actions that are reversible, local in effect, and limited
in human impact. Reading a file. Querying a public API. Drafting a response that a
human will review before it is sent. These actions warrant governance presence — the
EGK should be invoked — but the governance determination is lightweight. The cost of
error is low. Recovery is straightforward. Many currently deployed autonomous systems operate entirely within this tier and function well without execution-boundary
governance of the kind described in this paper. The framework is not intended to impose high-consequence controls on low-consequence systems.
The second tier is high consequence. Actions that are irreversible, externally visible, regulated, or capable of material impact on individuals or organizations. Moving funds.
Modifying records. Sending communications on behalf of a principal. Accessing protected data. Executing contracts. These actions warrant full governance evaluation —
authority verification, policy compliance, constraint checking, and evidence generation.
The cost of error is significant. Recovery may be incomplete.
The third tier is sovereign consequence. Actions that are systemic, cross-jurisdictional,
infrastructure-level, or capable of cascading effects beyond the immediate principal.
Actions that affect critical systems, financial markets, public infrastructure, or populations at scale. These actions warrant the highest governance intensity — including, in
     Capability-based regulation as the current dominant regulatory model is documented in European
Parliament & Council of the European Union (2024). Regulation (EU) 2024/1689 on Artificial Intelligence
(EU AI Act). Oﬀicial Journal of the European Union. Articles 6-16 establish a risk classification system
based primarily on application domain and system capability rather than consequence of specific actions.
The consequence-based classification proposed in this paper is an original contribution intended to complement rather than replace capability-based frameworks.

many cases, human escalation before execution is permitted, regardless of how well the
compiled policy is written.
Consequence classification serves two functions. First, it allows governance intensity
to be proportionate — concentrating the most rigorous controls where the stakes are
highest, and avoiding the overhead of maximum-intensity governance on every lowstakes action. Second, it provides the foundation for consequence-based regulation: a
regulatory model that governs what systems do rather than what systems are.
The execution boundary does not change across consequence tiers. The EGK is always
present within its defined scope. What changes is the depth of evaluation the EGK performs, the evidence it generates, and the conditions under which it will permit rather
than deny or escalate.
Consequence classification is therefore not a relaxation of governance. It is a governance
calibration — ensuring that the weight of enforcement matches the weight of what is at
stake.

## Chapter 17 — The Execution Boundary

Every autonomous system contains a moment that governance theory has yet to name.
It is not the moment an agent begins reasoning. It is not the moment a policy is written
or a risk assessment completed. It is the moment immediately before an action commits
— the final interval in which the world still contains two possible futures: one in which
the action occurs, and one in which it does not.
After that moment, only one future remains.
The execution boundary is that moment, formalized as an architectural concept. It is the
final deterministic control point immediately preceding an autonomous action — the
threshold at which authority, policy, constraints, and admissibility can still be evaluated
before execution occurs. Once crossed, the action is no longer proposed. It is a fact.
The execution boundary has properties that distinguish it from every other point in an
autonomous system’s operation.
It is singular. For any given action, there is one execution boundary — one moment
at which the determination between occurrence and non-occurrence remains available.
Governance that operates before the boundary is preparation. Governance that operates after the boundary is documentation. Only governance that operates at the boundary is control.
It is deterministic. The boundary is not a probabilistic zone or a fuzzy threshold. It is
the precise point at which a proposed action becomes an executed one. This determinism is what makes the boundary governable — it can be identified, instrumented, and
enforced.
It is consequential. The boundary exists only for actions that matter — actions that
change state, commit resources, affect other systems, or trigger effects that cannot be

trivially reversed. Actions without consequence have no meaningful execution boundary because they have no meaningful execution. The boundary is defined by what follows it.
It is the governance surface. Not a monitoring surface. Not an audit surface. Not an
explainable surface. A governance surface — the only point in the system where a
determination can still causally influence whether an action occurs.
Understanding the execution boundary as a distinct architectural concept clarifies what
has been missing from existing governance frameworks. The reference monitor understood it in the context of access control. Safety engineering understood it in the context
of physical systems. Financial markets understood it in the context of pre-trade risk.31
What has not existed until now is a unified treatment of the execution boundary as the
primary governance concept for autonomous systems operating across domains — a
concept general enough to apply wherever an autonomous agent crosses from reasoning into consequence.
That crossing point is the execution boundary. It is where governance either happens
or it does not. There is no third option.

## Chapter 18 — Boundary Discovery

Knowing that an execution boundary exists and knowing where it is are different problems.
Most organizations building or deploying autonomous systems have not mapped their
execution boundaries.32 Not because the boundaries do not exist — they always exist
— but because no methodology has required them to. Governance frameworks have
not asked the question. Audit processes have not demanded the answer. Risk assessments have evaluated what systems can do without precisely identifying where doing
becomes irreversible.
The result is a predictable failure mode: organizations discover their execution boundaries only when they are crossed, not before. The funds move. The record changes.
The communication sends. The system logs the event. And only then does anyone ask

      The execution boundary as a control point is independently established in three prior domains. In cybersecurity: Anderson, J.P. (1972). Computer Security Technology Planning Study. ESD-TR-73-51 — the reference monitor as the mechanism invoked immediately prior to every access attempt. In safety engineering:
IEC 61508 (2010). Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems. International Electrotechnical Commission — the safety kernel as the minimal verified component at the
boundary between system and environment. In financial markets: FINRA Rule 15c3-5 (2010). Market
Access Rule — the pre-trade risk check as a hard limit evaluated before every order reaches the exchange.
The unified treatment of the execution boundary as a primary governance concept for autonomous agentic
systems is an original contribution of this paper.
      The gap between autonomous system deployment and governance mapping is documented in two
independent sources. Varma, S. (2026). Gartner Says Applying Uniform Governance Across AI Agents
Will Lead to Enterprise AI Agent Failure. Gartner Newsroom, May 26, 2026 — predicting that 40% of
enterprises will demote or decommission agents by 2027 specifically because governance models do not
match autonomy levels. ISACA (2026). AI Use Accelerates, While Governance and ROI Lag. ISACA AI Pulse
Poll, May 5, 2026 — reporting that only 38% of organizations have a comprehensive AI policy and 39% do
not know whether an override process exists for their AI systems.

where, in the chain of operations that preceded the outcome, a determination could
have been made.
Boundary discovery is the process of answering that question in advance.
It is not a theoretical exercise. It is an operational methodology — a structured approach to identifying, for any autonomous system or agentic workflow, the precise
points at which reversibility ends and consequence begins. Those points are the execution boundaries. They are where the EGK must be placed. They cannot be governed
if they cannot be found.
The methodology proceeds in four steps.
The first step is action enumeration. Every action available to the autonomous system
is listed — every tool it can call, every API it can invoke, every record it can modify,
every transaction it can initiate. The list is not filtered or prioritized at this stage. Completeness matters more than eﬀiciency. An execution boundary that is not enumerated
cannot be governed.
The second step is reversibility assessment. For each enumerated action, a single question is asked: if this action executes, can its effects be undone by a subsequent action
without residual consequence? Actions that can be cleanly reversed fall into a different
governance category than those that cannot. Sending an email cannot be unsent. A
database write can sometimes be rolled back. A financial transfer may or may not be
reversible, depending on the timing and the counterparty. Reversibility is not binary
in practice, but the assessment forces precision about what recovery actually requires.
The third step is commit surface identification. Among the irreversible or partially reversible actions, the commit surface is the specific operation at which the point of no
return is crossed. In a multi-step workflow, the commit surface may not be the final
step. It may be an intermediate operation whose effects propagate forward regardless
of what the system does afterward. Precisely identifying the commit surface is the difference between placing governance where it is needed and where it is convenient.
The fourth step is authority mapping. For each identified commit surface, the question
of authority is asked: who has sanctioned this action, under what conditions, with
what constraints? Authority mapping connects the physical location of the execution
boundary to the governance policy that should operate there. Without this mapping,
an EGK can be placed correctly but enforce the wrong policy, or enforce no policy at
all.
Boundary discovery is not a one-time exercise. Autonomous systems evolve. New tools
are added. Workflows are extended. Each addition potentially introduces new execution boundaries that did not exist before. The methodology must be applied continuously, not as a deployment checklist but as an ongoing operational discipline.
The value of boundary discovery extends beyond the systems that ultimately deploy
an EGK. The act of mapping execution boundaries — of asking, for every autonomous
action, where the point of no return actually is — produces organizational clarity that
is valuable regardless of which governance architecture is followed. Organizations that

have mapped their execution boundaries understand their autonomous systems in a
way that organizations that have not cannot.
The boundary exists whether or not it is mapped. Mapping it is the precondition for
governing it.

## Chapter 19 — EGK and Multi-Step Agent Eﬀiciency

The case for execution-boundary governance is usually made in terms of safety. It
should also be made in terms of cost.
An autonomous agent executing a complex workflow does not act once. It acts many
times — retrieving context, calling tools, evaluating intermediate results, revising its
approach, and chaining outputs across what may be ten, twenty, or fifty discrete steps
before a consequential action occurs. Each step consumes compute. Each step consumes time. Each step consumes tokens.
If governance is distributed across all of those steps — if policy is evaluated, retrieved,
or reasoned about at each intermediate point — the cost compounds. Not linearly.
Across a twenty-step workflow, governance overhead applied at every step multiplies
the latency budget, token consumption, and compute cost by a factor proportional to
the number of steps. For high-frequency agentic systems operating at scale, that multiplication is not a rounding error. It is a structural cost that accumulates with every
workflow execution, every hour of operation, every agent deployed.
This is the hidden tax of distributed governance.
It is not visible in single-agent demonstrations. It becomes visible at scale — when
thousands of agents are running simultaneously, each executing dozens of steps, each
incurring governance overhead at every step, regardless of whether that step is consequential.
Execution-boundary governance eliminates that tax.
When governance is concentrated at the execution boundary — evaluated once, deterministically, immediately before the action that actually matters — the reasoning phase
is entirely free of governance overhead. The agent thinks without interruption. It retrieves, evaluates, chains, and revises without paying a governance cost at each step.
The cost is paid once, at the boundary, where it is both necessary and suﬀicient.
The arithmetic is straightforward. A twenty-step workflow with governance evaluated
at every step pays twenty governance costs. The same workflow with an EGK at the execution boundary pays one.33 If the governance cost per step is non-trivial — and in any
      Production agentic workflow latency data supporting the per-step governance cost argument is documented in LangChain (2026). SmithDB Inverted Index Performance Benchmarks. LangChain Platform, May
13, 2026, which reports P50 latencies of 71ms for single run loads, 82ms for run filtering, and 92ms for trace
tree loads in multi-step agentic workflows; and Cisco Systems Engineering Team (2026). BRKSPG-1180:
Advanced Network Architectures for LLM Ingestion. Cisco Live EMEA, February 2026, which documents toolcall latency envelopes of 25-100ms in production agentic architectures. A twenty-step workflow paying
per-step governance overhead at these latency ranges accumulates 1.4 to 2.0 seconds of governance cost
before reaching the consequential action. The same workflow governed only at the execution boundary
incurs a single governance cost of 25-100ms.

system that requires policy retrieval, token-based reasoning, or external authorization
calls, it is — the eﬀiciency difference is an order of magnitude.
This has implications beyond cost. Latency compounds in the same way. A workflow
that pays for governance latency at twenty steps accumulates twenty latency penalties
before reaching the consequential action. A workflow governed only at the execution
boundary accumulates one. In latency-sensitive applications — real-time systems, timecritical workflows, high-frequency agent operations — that difference is not merely
economic. It is architectural. Distributed governance may make certain applications
physically impossible. Boundary governance makes them feasible.
The eﬀiciency argument reinforces the safety argument rather than competing with
it. Governance concentrated at the execution boundary is not a compromise between
safety and performance. It is the architecture that makes both possible simultaneously
— safety, because governance is present at the only point that matters; performance,
because governance is absent from every point that does not.
At scale, this is not a marginal improvement. It is the difference between a governance
architecture that autonomous systems can afford to operate under and one they cannot.
Governance that systems cannot afford to operate under will not be operated under. It
will be worked around, disabled, or excluded from deployment decisions made under
competitive pressure.
Governance that costs one check instead of twenty has a future. Governance that costs
twenty checks instead of one does not.

## Chapter 20 — Governance Locality

The latency condition has a spatial corollary.
Governance executed at distance from the execution surface incurs unavoidable network latency. As action latency shrinks, the maximum permissible governance distance
shrinks with it. This is not an architectural preference. It is a derived constraint from
the latency condition and the physics of information propagation.
For most of the history of institutional governance, location was irrelevant. A law applied regardless of where the courthouse sat. A policy governed regardless of where
the compliance team was located. The substance of governance and the physical location of its execution were independent variables.
That independence was always an illusion sustained by human latency. When decisions took hours or days, the milliseconds consumed by network transit were negligible. Governance could live anywhere because the time it operated in was so much
larger than the time it took to get there.
That illusion does not survive machine-speed systems.

In an autonomous system operating within a tight latency budget, every millisecond of
governance transit is a millisecond subtracted from the available action latency. At sufficient distance — or insuﬀicient bandwidth, or degraded network conditions — governance latency exceeds action latency entirely. The latency condition fails. Governance
becomes observational.
The speed of light imposes a hard lower bound on round-trip latency between any two
points separated by physical distance. A governance check that requires a round trip
to a data center on another continent cannot complete in under approximately 130 milliseconds, regardless of how fast the software runs.34 If the action latency budget is 25
milliseconds, that governance check will never be controlled. Not with better hardware.
Not with faster software. Not with more investment. The physics do not permit it.
Governance locality is therefore a derived requirement. As action latency shrinks — as
autonomous systems operate faster, chain steps more tightly, and execute in intervals
measured in single-digit milliseconds — the maximum permissible distance between
the EGK and the execution surface shrinks with it. Governance that could previously
run in a regional data center must move to an edge node. Governance that could run
on an edge node must move even closer. In the limit, governance must be co-located
with execution — not because co-location is architecturally elegant, but because the
alternative violates the latency condition.
This creates a design requirement that most current autonomous system architectures
do not address: governance locality must be specified as an architectural constraint, not
left as an operational detail. The question of where the EGK runs is not separable from
the question of whether the EGK governs. They are the same question.
Governance locality also has implications for resilience. A governance mechanism that
depends on a remote connection to function is a governance mechanism that fails when
that connection degrades. At the execution boundary, a failed governance check is not
a degraded governance check. It is an ungoverned action — unless the EGK is designed
to fail safe, denying execution when its own operation cannot be confirmed. Locality
reduces the attack surface, failure modes, and dependence on network infrastructure
whose reliability the EGK cannot control.
The principle is simple. Governance must be where execution is. Not near it. Not
reachable from it within acceptable latency under normal conditions. Where it is.
Proximity to the execution surface is not a deployment detail. It is a governance requirement.

       The 130-millisecond floor for a New York-to-London round-trip is derived from two sources. Intercontinental cable distances are documented in TeleGeography (2024). Submarine Cable Map. TeleGeography Inc. submarinecablemap.com. Fiber optic propagation speed — approximately two-thirds of the
speed of light in vacuum, or roughly 2×10� m/s — is established in Agrawal, G.P. (2019). Fiber-Optic Communication Systems (6th ed.). Wiley. Empirically observed round-trip latency data by geography is documented in Cloudflare (2024). Global Network Latency Report. Cloudflare Inc. cloudflare.com/radar. The
130ms figure represents the physical minimum imposed by distance and propagation speed, independent
of software performance.

## Chapter 21 — Edge Compute and the 25ms Envelope

The locality requirement is theoretical until infrastructure makes it practical. That infrastructure now exists.
The buildout of edge compute — telco-deployed mobile edge compute nodes, retail
edge servers, industrial edge systems — was not designed with governance in mind.
It was designed for latency-sensitive applications: augmented reality, autonomous vehicles, real-time analytics, low-latency gaming, industrial control. The governance use
case is a consequence of the same physical requirements that drove those deployments.
Proximity to the point of action reduces latency. Reduced latency makes real-time computation feasible. The EGK is real-time computation. The infrastructure fits.
The 25-millisecond envelope is not an arbitrary threshold. It emerges from the operational characteristics of current agentic systems and the latency budgets within which
consequential actions are initiated. An agent executing a tool call — invoking an API,
writing to a database, initiating a transaction — operates within an action latency window that current benchmarks place in the range of 25 to 100 milliseconds for the categories of actions this paper identifies as high consequence.35 Below that window, the
action has committed before any remote governance check could complete. Within that
window, a locally deployed EGK can operate.
The telco edge buildout provides the physical nodes. Mobile edge compute infrastructure, deployed by major carriers across urban and industrial environments.36 places
compute resources within single-digit millisecond round-trip distance of most commercial and industrial execution surfaces. A governance kernel running on a co-located
edge node can complete a deterministic admissibility check — authority verification,
policy evaluation, constraint assessment — well within the 25-millisecond envelope
without requiring any new infrastructure investment beyond what the edge compute
market already deploys for other purposes.
The commoditization of edge hardware accelerates this. Server hardware vendors targeting retail, industrial, and enterprise edge deployments are producing systems specifically designed for low-latency, high-reliability local computation.37 These are not research platforms. They are commercial products, available today, designed for exactly
the operational profile the EGK requires: deterministic, local, continuously available,

       Production agentic system latency benchmarks placing high-consequence tool-call actions in the 25-
100ms range are documented in Cisco Systems Engineering Team (2026). BRKSPG-1180: Advanced Network
Architectures for LLM Ingestion. Cisco Live EMEA, February 2026; and LangChain (2026). SmithDB Inverted
Index Performance Benchmarks. LangChain Platform, May 13, 2026, reporting P50 trace latencies of 71-92ms
for agentic workflows in production environments.
       The MEC framework and reference architecture are specified in ETSI GS MEC 001 (2022).
  Multi-access Edge Computing (MEC): Terminology. European Telecommunications Standards Institute;
and ETSI GS MEC 003 (2022). Multi-access Edge Computing (MEC): Framework and Reference Architecture.
European Telecommunications Standards Institute. 5G latency specifications guaranteeing single-digit
millisecond round-trip times are established in 3GPP Release 17 (2022). 5G System Specifications. 3rd
Generation Partnership Project.
       Commercial edge hardware targeting the operational profile required by the EGK is documented in
SuperMicro (2024). Edge Computing Server Product Line. Super Micro Computer Inc.; Dell Technologies
(2023). Edge Computing Solutions White Paper. Dell Technologies Inc.; and HPE (2023). Edgeline Converged
Edge Systems Portfolio. Hewlett Packard Enterprise.

and capable of handling high request volumes without the latency penalties of cloud
round-trips.
This matters for the governance argument in a precise way. One of the standard objections to execution-boundary governance is infrastructural: that requiring local governance computation imposes deployment costs making the model impractical at scale.
The current state of edge compute infrastructure neutralizes that objection. The infrastructure is being deployed regardless of reasons unrelated to AI governance. The EGK
rides that infrastructure. The marginal cost of adding a governance workload to an
already-deployed edge node is not the cost of building edge infrastructure. It is the
cost of running software on existing infrastructure.
The 25-millisecond envelope also has implications for EGK design. A kernel that must
complete within 25-milliseconds cannot perform operations that exceed that budget
— complex policy reasoning, external authorization calls with non-trivial round-trip
times, probabilistic assessments requiring iterative computation. The latency budget
is a design constraint that forces the EGK toward determinism. Compiled policy, preresolved authority contexts, and binary admissibility evaluations are not merely architecturally elegant. They are the only designs that fit within the envelope.
The latency condition established in Chapter 6 requires that governance complete
within the action latency. The locality requirement established in Chapter 20 requires
governance to run proximate to the execution surface. The 25-millisecond envelope
quantifies the requirements for the current generation of agentic systems. And the
existing edge compute buildout provides the physical infrastructure to satisfy them —
today, at commercial scale, without waiting for infrastructure that does not yet exist.
The governance argument and the infrastructure reality have arrived at the same moment. That convergence is not coincidental. It is the consequence of the same underlying force: the compression of action latency in systems that operate at machine speed.

## Chapter 21A — The Edge Is Not the Edge

Edge compute is not a location. It is a spectrum.
The word “edge” has become a convenience that obscures more than it reveals. In infrastructure discussions, edge refers to anything that is not the central cloud — a category so broad that it encompasses telco nodes serving millions of users, factory-floor
servers managing industrial equipment, hospital racks processing patient data, vehicle
controllers making sub-millisecond decisions, and the neural processing units now embedded in consumer phones. These environments share a name. They share almost
nothing else.
For execution-boundary governance, this distinction is not semantic. It is architectural.
The governance requirements at each tier of the edge spectrum differ in kind, not merely
in degree. A framework that treats edge as a single deployment target will satisfy none
of them well.
Three tiers define the spectrum.

The first tier is network edge. Telco-deployed mobile edge compute nodes, regional
cloud presence points, hyperscaler edge zones. These environments offer latency in
the range of five to twenty-five milliseconds — meaningfully lower than central cloud,
suﬀicient for the current generation of high-consequence agentic actions. They operate
under enterprise-grade controls: physical security, access management, logging
infrastructure, audit posture, and compliance certifications required by regulated
industries. The 25 millisecond envelope described in Chapter 21 is anchored here.
Network edge is where execution-boundary governance can be deployed today at
commercial scale, with the evidentiary and underwriting properties that liability and
insurance frameworks can recognize.
The second tier is facility edge. The server rack in the hospital basement. The industrial
controller on the factory floor. The financial processing unit in the bank branch. The
airport operations system in the terminal. These environments sit physically closer to
the point of consequence — closer to the patient, the machine, the transaction, the gate.
Latency drops accordingly: single-digit milliseconds, sometimes sub-millisecond. Governance placed here is more local, more immediate, and more causally proximate to the
action it governs.
But proximity introduces complications that network edge does not present. Facility
edge environments vary enormously in their security posture, administrative controls,
physical hardening, and audit infrastructure. A hospital basement server may be close
enough to govern a medical record access decision in under a millisecond. Whether it
is adequately secured, independently logged, key-managed, and administratively separated from the systems it governs is a different question entirely — and the answer
varies by facility, by operator, and by the regulatory regime that applies.
The third tier is device edge. Vehicle electronic control units. Smartphone neural processing units. Wearable sensors. Industrial robots. Autonomous drones. These systems
execute at speeds that make the 25-millisecond envelope appear leisurely. A vehicle’s
safety systems operate in microseconds.38 On-device inference on current consumer
hardware runs in single-digit milliseconds.39 An industrial robot’s control loop may
complete in hundreds of microseconds. At these speeds, no remote governance check
of any kind can participate in the decision path. If governance is present at the device
edge, it must be embedded — compiled into firmware, loaded into hardware-adjacent
processes, operating within the execution envelope of the device itself.
Device edge is where the governance argument reaches its physical limit and its logical
conclusion simultaneously. The latency condition demands governance locally. The
infrastructure available at this tier makes governance at this local level extraordinarily
diﬀicult to instrument, verify, audit, and insure.

      Vehicle safety system timing requirements at the microsecond level are established in ISO 26262
(2018). Road Vehicles — Functional Safety. International Organization for Standardization — specifically
the ASIL-D timing constraints for safety-critical automotive systems; and SAE J3061 (2016). Cybersecurity
Guidebook for Cyber-Physical Vehicle Systems. SAE International.
      On-device inference latency in single-digit milliseconds is documented in Apple Inc. (2023). A17
Pro Chip — Neural Engine Specifications. Apple Developer Documentation; and Qualcomm Technologies
(2023). Snapdragon 8 Gen 3 Mobile Platform — AI Performance Specifications. Qualcomm Technologies Inc.

This creates the central tension that the edge spectrum reveals.
The architecture that satisfies latency requirements may not satisfy underwriting requirements.
Consider a concrete example. A hospital deploys an autonomous agent with authority
to access and update patient medical records. The agent operates on a local server in
the hospital’s data center — facility edge, ten milliseconds from the point of action. An
EGK on that server can evaluate admissibility and produce a determination well within
the available latency budget.
But the underwriter assessing this deployment asks different questions. Is the local
server physically secured against unauthorized access? Are the EGK’s evidence artifacts stored independently of the systems whose actions it governs, such that a compromise of those systems cannot alter the governance record? Is the key management
for evidence signing independent of the hospital’s operational IT? Is the server’s audit
posture suﬀicient to satisfy HIPAA’s requirements for access logging and breach notification?40 Is the governance evidence producible in a form that a court would recognize,
and that an insurer could rely upon in a coverage dispute?
These are not latency questions. They are evidentiary, administrative, and regulatory
questions — and the answers at facility edge are far less reliable than the answers at
network edge, where enterprise-grade controls are standard rather than variable.
The device edge tier makes this tension acute. A governance kernel embedded in a
vehicle controller or phone NPU may satisfy the latency condition with microseconds
to spare. It cannot satisfy the evidentiary independence condition, the administrative
separation condition, or the audit posture condition that regulated industries and underwriters require. The device is the execution surface. The governance kernel on the
device is not independent of the execution surface. Evidence produced by a kernel that
shares physical infrastructure with the system it governs is evidence whose integrity
cannot be guaranteed by the kernel alone.
This requires a distinction that the paper’s earlier treatment of locality did not make
explicit.
Technical locality means the governance check is close enough to the execution surface
to satisfy the latency condition.
Evidentiary locality means the governance check is positioned so that its evidentiary
artifacts are produced independently of the system whose actions it governs — close
enough to witness execution, yet separated enough to prove it.
Underwriting locality means that the governance deployment satisfies the physical security, administrative separation, key management, audit posture, and resilience standards required by an underwriter to treat governance presence as a covered control.

      HIPAA audit control requirements applicable to facility edge deployments are established in 45 CFR §
164.312(b). HIPAA Security Rule — Audit Control Requirements. U.S. Department of Health and Human
Services; and 45 CFR §§ 164.400–414. HIPAA Breach Notification Rule. U.S. Department of Health and
Human Services.

Regulatory locality means the governance deployment satisfies the jurisdiction-specific
requirements that apply to the consequence class being governed — HIPAA for medical
records, PCI-DSS for payment data,41 NERC CIP for energy infrastructure, whatever
framework governs the action being evaluated.42
These four localities are not the same. An architecture may satisfy one while failing
the others. The governance framework that is technically suﬀicient at device edge may
be evidentarily insuﬀicient, underwriting-ineligible, and regulatorily non-compliant simultaneously.
The implications for governance architecture are direct.
As execution moves down the edge spectrum — from the network edge toward the
device edge — the latency condition becomes easier to satisfy, while the evidentiary,
underwriting, and regulatory conditions become harder. The governance kernel must
become smaller and faster. The evidence it produces must travel further from the execution surface to reach an environment where its integrity can be independently verified.
This suggests that the governance architecture for low-latency edge deployments cannot be fully self-contained at the edge. The kernel executes locally — it must, to satisfy
the latency condition. But the evidence it produces must be transmitted to an environment with the controls necessary to guarantee its integrity — an environment where
independent verification, regulatory audit, and underwriting assessment can occur.
The edge is therefore not where governance lives. It is where governance acts. The
evidence of that action must travel upstream to where governance can be proven.
This is not a retreat from the locality argument. It is its completion. Governance locality
means the enforcement mechanism is where execution is. Evidence integrity means the
proof of enforcement is where verification can be trusted. These are two different requirements, satisfied at two different tiers of the infrastructure stack, working together
to constitute governance that is both causally effective and legally credible.
The trajectory of the edge compute market — faster hardware, lower latency, deeper
deployment into physical environments — does not relax the governance requirement.
It intensifies it. As consequential autonomous actions shift toward device-level execution, the governance kernel must accompany them. The evidence those kernels produce
must be designed, from the outset, to survive the journey from microsecond device
execution to the human-speed institutions — courts, regulators, insurers — that will
eventually evaluate it.
The edge is not the edge. It is the beginning of a compression gradient that ends at the
physics of silicon itself.
Governance must follow that gradient. Evidence must survive it.

      Payment data governance requirements are established in PCI DSS v4.0 (2022). Payment Card Industry
Data Security Standard. PCI Security Standards Council.
      Energy infrastructure governance requirements are established in NERC CIP-007-6 (2022). Systems
Security Management. North American Electric Reliability Corporation.

Both requirements are non-negotiable. Neither is simple. The tension between them
is not a problem to be solved before deployment begins. It is the central design challenge of execution-boundary governance in a world where consequences increasingly
originate at the edge of the network and at the bottom of the latency stack.

## Chapter 22 — Physics and the Speed of Information

Every argument in this paper traces back to the same constraint.
Not policy. Not organizational will. Not regulatory ambition. Not technological sophistication. A physical constant — one that does not negotiate, does not accommodate
good intentions, and does not yield to investment.
The speed of light.
Information cannot travel faster than approximately 299,792 kilometers per second in
a vacuum. In fiber optic cable, the effective propagation speed is roughly two-thirds
of that.43 These are not engineering limitations awaiting a better solution. They are
properties of the universe that the governance architecture must accommodate or fail
to accommodate.
The implications are precise and unavoidable. A round-trip between New York and
London — approximately 5,570 kilometers — cannot be completed in under roughly
56 milliseconds, regardless of what runs on either end.44 A round-trip between a device in Tokyo and a data center in Virginia cannot be completed in under roughly 140
milliseconds. These numbers do not improve with better software, faster processors, or
more investment. They are floors imposed by distance and the finite speed of electromagnetic signal propagation through physical media.
For human-speed governance, these floors were irrelevant. A governance check that
required 140 milliseconds of network transit operated within a decision cycle measured
in seconds, minutes, or hours. The physics were invisible because the latency budget
was so large that physical constraints never bound it.
For machine-speed governance operating within a 25-millisecond action-latency envelope, the physics are the binding constraint. A governance mechanism that requires a
round-trip to infrastructure more than roughly 1,500 kilometers away cannot complete
within that envelope under any conditions. Not with optimization. Not with caching.
Not with prefetching. The distance is too great, and the speed of light is too slow.

       The speed of light in vacuum — c = 299,792,458 m/s — is an exact defined value per the 1983 SI redefinition, documented in NIST (2018). CODATA Internationally Recommended 2018 Values of the Fundamental
Physical Constants. National Institute of Standards and Technology. Its theoretical basis is established in
Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. Annalen der Physik, 17, 891–921. Fiber optic
propagation speed of approximately 2×10� m/s — roughly two-thirds of c — is documented in Agrawal,
G.P. (2019). Fiber-Optic Communication Systems (6th ed.). Wiley.
       The 56-millisecond floor for a New York-to-London round-trip is derived from the cable distance documented in TeleGeography (2024). Submarine Cable Map. TeleGeography Inc. submarinecablemap.com,
and the fiber propagation constant established in Agrawal (2019). Empirically observed latency data consistent with this derivation is documented in Cloudflare (2024). Global Network Latency Report. Cloudflare
Inc. cloudflare.com/radar.

This is not a theoretical edge case. It is the operating condition of any autonomous
system whose governance infrastructure is not co-located with its execution surface.
Cloud-hosted governance checking edge-deployed execution is, in many configurations, physically incapable of satisfying the latency condition — not because the cloud
is slow, but because the cloud is far.
The physics argument transforms execution-boundary governance from a design recommendation into a derived necessity. The question is not whether governance should
be local to the execution surface. The question is whether non-local governance can
satisfy the latency condition. In a growing number of deployment configurations, the
answer is no — not as a matter of engineering judgment but as a matter of arithmetic
derived from the speed of light and the distance between infrastructure components.
This also clarifies the long-term trajectory of governance architecture. As autonomous
systems continue to compress action latency — the interval between a system’s decision
and its consequence — toward the physical minimum, the maximum permissible governance distance shrinks with it. The physics do not reverse. The trend does not plateau.
The pressure toward governance locality is not a temporary condition of current technology. It is a permanent consequence of operating in a universe where information
has a finite propagation speed.
Governance architecture that ignores physics does not overcome physics. It simply fails
to govern — quietly, consistently, and precisely when governance is most needed.
The constraint beneath every framework, every policy, every regulatory ambition, every oversight mechanism is this: a determination must be made before a consequencebearing action commits, within a finite interval, in a universe where information travels
at a finite speed.
Everything else is commentary.

## Chapter 23 — Machine-Speed Markets and the Economics of Governance

The chapters preceding this one examined autonomous systems as individual actors —
single agents executing single workflows within governance architectures designed to
control their actions. That framing is already becoming incomplete.
Agents are beginning to transact with agents.
Not as a future possibility. As a present reality. Orchestration frameworks coordinate
fleets of specialized agents, each calling others as tools, each receiving outputs that become inputs to subsequent actions, each operating without human initiation or review
at the individual transaction level. The human who deployed the system may be hours
or continents away from the transactions it is executing on their behalf.
When agents transact with agents at machine speed, something new emerges: a market
whose velocity exceeds the observation capacity of any human governance mechanism.
This is not merely a scaling problem. It is a structural condition. In a human market,
the slowest participant sets a de facto floor on transaction velocity — a floor at which

human governance mechanisms can, in principle, operate. When all participants are autonomous, that floor disappears. Transactions occur at the speed of the infrastructure,
not the speed of the participants. Settlement, pricing, authorization, and execution all
collapse into intervals measured in milliseconds.
No human compliance oﬀicer can review a transaction that completes in 12 milliseconds. No audit committee can convene between the proposal and the commitment of
an action that executes in the time it takes light to cross a city. Human governance
mechanisms, applied to machine-speed markets, do not slow the markets down. They
document the outcomes of markets they never had the opportunity to govern.
There is a second problem that receives far less attention. It is not only governance that
was designed for human speed. It is pricing.
Every commercial model underlying the software infrastructure through which autonomous agents now operate was designed for a human consumer. Adobe charges
a monthly subscription — a flat fee calibrated to the rhythm of a human creative professional who opens the application, works for hours, and closes it. Salesforce charges
per seat — a unit of measure that assumes a human occupying a role, logging in, and
taking actions across a working day. A bank charges a fee for moving money or executing a trade — a transaction cost set at a level that a human-initiated transfer can absorb
without friction.45
These pricing models are not arbitrary. They are expressions of human-speed consumption patterns. They assume human initiation, human pacing, and human volume. They
were never designed for a world in which an autonomous agent might invoke the same
platform thousands of times in an hour, each invocation costing a fraction and lasting
a fraction of the time of any human interaction.
When existing software platforms become tools for agentic systems, the fee structures
do not disappear. They compress. An agent executing a bank-to-bank transfer still
triggers the transaction fee — but that fee, designed for a human moving money once,
is now being charged against an automated workflow that may execute hundreds of
equivalent transfers as intermediate steps in a single task. The per-seat license is still
active — but the seat is now occupied by an agent operating continuously, at throughput no human could match, under a pricing model that never anticipated non-human
consumption.
This creates a structural mismatch that the agent economy has yet to resolve. Humanspeed pricing applied to machine-speed consumption produces one of two outcomes.
Either the economics of agentic deployment become unworkable — the accumulated
fee burden of human-speed pricing across machine-speed transaction volumes makes
the operation prohibitively expensive — or operators route around the fee structures by
consolidating transactions, batching operations, or selecting tools specifically to minimize invocation costs rather than to maximize capability.
       The human-speed pricing models cited are publicly documented commercial pricing structures at
time of writing: Adobe Creative Cloud (2024), monthly subscription pricing; Salesforce (2024), per-seat
licensing. These are cited as illustrative examples of commercial models designed for human consumption
patterns rather than agentic throughput.

Neither outcome is what the software platforms intended. Neither outcome serves the
governance interest. Both are predictable consequences of applying human-speed commercial architecture to machine-speed execution.
The agent economy therefore faces a pricing transition that mirrors the governance transition this paper has described throughout. Monthly subscriptions are a blunt, aggregated measure of value — appropriate when consumption is human-paced and relatively predictable. Per-action pricing is the machine-speed equivalent: calibrated to
actual consumption rather than assumed human usage patterns.
This transition is not merely commercial. It is structural. When pricing moves to the
action level, the action becomes the atomic unit of economic exchange. And the action — as this paper has argued from its first chapter — is precisely where governance
must also operate. The execution boundary is not only where admissibility must be
determined. It is where economic value is created, where fees are triggered, and where
evidence must be generated.
An execution credential produced at the execution boundary is therefore not only a
compliance artifact. It is a potential settlement primitive — proof that an action occurred, that it was authorized, and that the associated economic obligation was incurred. The same evidence artifact that satisfies a regulatory audit can, if standardized,
settle a per-action fee. The same kernel that governs can also meter.
This convergence — of governance, pricing, and evidence at the execution boundary
— is not a coincidence. It is the consequence of machine-speed systems forcing every
human-speed abstraction to its atomic level. Monthly subscriptions dissolve into peraction fees. Audit cycles dissolve into execution evidence. Human oversight dissolves
into kernel determinations.
The selection pressure this creates is direct and uncomfortable.
Markets do not wait for governance. They evolve around it. Every time a new class of
economic activity emerged at speeds or scales that existing governance could not reach,
the same sequence followed: the activity expanded, governance adapted after the fact,
and the gap between what governance intended and what markets actually did was
filled — permanently, structurally — by whoever moved first.
Algorithmic trading did not wait for regulators to develop a framework for microsecond
order placement.46 It developed, proliferated, and reshaped market structure while regulators were still debating whether the phenomenon required a response. The frameworks that eventually emerged governed a market already transformed by the activity
they were meant to prevent.

     The pattern of algorithmic trading reshaping market structure faster than regulatory response is documented in SEC & CFTC (2010). Findings Regarding the Market Events of May 6, 2010 (Flash Crash Report).
U.S. Securities and Exchange Commission and Commodity Futures Trading Commission; Kirilenko, A.,
Kyle, A.S., Samadi, M., & Tuzun, T. (2017). The Flash Crash: High-frequency trading in an electronic
market. Journal of Finance, 72(3), 967–998; and SEC (2010). Concept Release on Equity Market Structure. Release No. 34-61358. U.S. Securities and Exchange Commission — the latter explicitly acknowledging that
regulators were examining market structure changes already driven by algorithmic trading.

The mechanism is not conspiracy. It is competition. In any market where participants
face competitive pressure, latency is a cost. Governance that imposes latency is a cost.
Costs that can be avoided will be avoided — not because participants are malicious but
because participants who absorb avoidable costs lose to participants who do not. The
market selects against expensive governance the same way evolution selects against
metabolically expensive traits in resource-constrained environments. Not through intent. Through pressure.
An agent deployment that operates under full governance overhead — policy evaluated at every step, human review required for consequential actions, compliance checks
distributed across the workflow — will be slower and more expensive than a deployment with minimal governance. In a competitive market for autonomous services, the
governed deployment loses. Not eventually. Immediately. Every transaction. Every
workflow. Every deployment decision made by a cost-conscious operator.
This creates a selection dynamic that no regulatory framework has yet addressed directly. Existing frameworks specify what governance must be in place. They do not
specify how governance must be structured to remain competitive. The result is predictable: operators will satisfy governance requirements in the cheapest way available
— which typically means narrative governance, documentation after the fact, compliance theater that satisfies the letter of requirements while the actual execution occurs
at speeds the requirements were never designed to govern.
Execution-boundary governance is a response to selection pressure, not merely a safety
argument.
A governance architecture that concentrates its cost at a single deterministic check —
one evaluation, one determination, one evidence artifact, at the only point that actually
matters — is a governance architecture that can survive competitive pressure. It does
not eliminate governance costs. It minimizes them. It places the cost precisely where it
must be paid and nowhere else.
The same logic applies to pricing architecture. A commercial model that charges at
the action level is a pricing model that survives the agent economy. Monthly subscriptions and per-seat licenses are not wrong. They are human-speed approximations of
value that will be replaced, at machine speed, by per-action pricing calibrated to actual
consumption. The transition is not optional. It is selected for.
Governance that the market cannot afford to operate under will not be operated under.
Pricing that the agent economy cannot absorb will be routed around. Selection pressure
does not care about the quality of governance intent or the elegance of the commercial
model. It cares about the cost of the operation.
Expensive governance loses. Human-speed pricing loses. Both for the same reason:
they were designed for a substrate that no longer sets the pace.
The choice facing governance architects is therefore not between more governance and
less. It is between governance calibrated to machine speed and governance that is not.
Execution-boundary governance is designed to be the former. Every alternative this
paper has examined is, at machine speed and at scale, the latter.

Chapter 24 — Sovereign AI and Regulatory Convergence Without Architectural Convergence
Every major jurisdiction is independently arriving at the same conclusions.
The European Union requires human oversight, traceability, and risk management.47
The United States emphasizes measurable, governable, and auditable AI systems.48
Canada mandates accountability, record-keeping, and risk mitigation.49 The United
Kingdom demands safety assurance, transparency, and accountability.50 Singapore requires model accountability, governance, and auditability.51 Australia focuses on operational resilience, accountability, and audit transparency.52 The UAE and Saudi Arabia
are building national AI governance frameworks anchored in traceability and verifiable
system behavior.53
The language differs. The jurisdictions differ. The enforcement mechanisms differ. The
underlying requirements do not.
Every framework, independently derived, converges on the same four demands: that
AI systems be accountable, that their behavior be traceable, that their operations be
auditable, and that oversight be demonstrably present.
This is regulatory convergence.
What is absent — in every framework, across every jurisdiction — is architectural convergence. No framework specifies how accountability is to be implemented at execution
time. No framework defines what traceability means at the moment an action commits.
No framework describes the mechanism by which oversight remains causally present in
a system operating faster than human review. Every framework agrees on what must
be achieved. None specifies the architecture required to achieve it.
This gap is not an oversight. It reflects the genuine diﬀiculty of specifying technical architecture in legal instruments designed to endure across multiple generations of technology. Regulators are right not to mandate specific implementations. But the absence
of architectural guidance creates a predictable problem: operators seeking compliance
will implement the cheapest mechanism that satisfies the letter of the requirement —
which, as Chapter 23 established, is almost always narrative governance. Documentation. Audit trails. Post-hoc reconstruction of what occurred.

       European Parliament & Council of the European Union (2024). Regulation (EU) 2024/1689 on Artificial Intelligence (EU AI Act). Oﬀicial Journal of the European Union. Articles 9, 13, and 14 establish human
oversight, traceability, and risk management requirements.
       National Institute of Standards and Technology (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. U.S. Department of Commerce.
       Government of Canada (2022). Bill C-27 — Artificial Intelligence and Data Act (AIDA). 44th Parliament,
1st Session.
       UK AI Safety Institute (2024). AI Safety Framework. Department for Science, Innovation and Technology, United Kingdom.
       Monetary Authority of Singapore (2023). Model AI Governance Framework (2nd ed., updated). MAS.
       Australian Prudential Regulation Authority (2019). Prudential Practice Guide CPG 234: Information
Security. APRA; Australian Government (2024). Voluntary AI Safety Standard. Department of Industry,
Science and Resources.
       UAE AI Oﬀice (2024). UAE National AI Strategy 2031 — Regulatory Framework Documentation. Government of the United Arab Emirates.

Compliance achieved through narrative governance satisfies regulatory requirements
as currently written. It does not satisfy the underlying intent of those requirements,
which is that systems operating autonomously remain under meaningful control.
The execution boundary is where that intent either materializes or fails. And no current
regulatory framework specifies that the execution boundary must be governed — only
that the system, in aggregate, must be accountable, traceable, and auditable.
This creates a specific opportunity to propose execution-boundary governance as an architectural approach. Not as a replacement for regulatory frameworks, but as the missing architectural layer that makes compliance with those frameworks meaningful rather
than nominal. An EGK deployed at the execution boundary produces exactly what every regulatory framework demands: contemporaneous evidence of control, traceable
to the specific action, auditable without reconstruction, and present at the moment the
action occurred rather than assembled afterward.
Nations building AI infrastructure at a national scale — state-sponsored AI systems,
government-deployed autonomous agents operating across public services, critical infrastructure, and defense — face a governance problem that purely procedural frameworks cannot solve. An autonomous system executing thousands of consequential actions per second cannot be governed by human review. It can only be governed by
something with the properties of an EGK. The label is irrelevant. The properties are not.
Complete mediation within defined consequence scope, determinism, latency compatibility, tamper resistance, evidence generation — these are the minimum conditions
under which any government can credibly claim that its autonomous systems remain
under meaningful operational control.
Regulatory convergence without architectural convergence is not a stable condition.
The frameworks are converging toward requirements that cannot be satisfied by the
governance architectures most operators currently employ. The gap will close — either
through regulatory specification of architectural requirements, through market adoption of architectures that actually satisfy the underlying intent, or through a consequential failure that forces the question.
Execution-boundary governance is proposed here not as the only possible architectural
response to that convergence, but as the first architectural framework that addresses
it directly — that names the execution boundary as the governance surface, specifies
the kernel properties required to govern it, and derives those requirements from the
same physical constraints that make machine-speed systems ungovernable by any other
means.
The frameworks know what they want. They do not yet know how to get it.
This paper proposes the how.

## Chapter 25 — Execution Evidence

Actions leave traces. Not all traces are equal.
There is a category of evidence that current governance literature treats as equivalent
to audit logs, compliance reports, and system documentation. It is not equivalent. It is
categorically different — different in when it is produced, different in what it proves,
and different in what it can support in legal, regulatory, and insurance contexts.
That category is execution evidence.
Execution evidence is produced at the execution boundary, by the EGK, at the moment
a determination is made. It is not assembled afterward from system logs. It is not
reconstructed from telemetry. It is not inferred from outcomes. It is generated contemporaneously with the governance determination — before the action commits, at the
precise moment the EGK evaluates admissibility and produces a result.
This timing is everything.
A log produced after an action has committed can tell you what happened. It cannot
tell you that governance was present before it happened. It cannot prove that a determination was made, that a policy was applied, or that the action was permitted rather
than simply executed. The log is consistent with governance having been present. It is
equally consistent with governance having been absent. The log does not distinguish
between the two cases because the log was not produced at the moment that distinguishes them.
Execution evidence distinguishes them. It is produced at that moment. It captures the
proposed action as presented to the EGK, the policy context that applied, the authority
credentials evaluated, the determination reached, and the timestamp at which the determination preceded the action. It is a record not of what happened but of what was
decided before what happened — a fundamentally different evidentiary artifact.
The distinction has legal significance. In liability proceedings involving autonomous systems, the question will not merely be what the system did. It will be whether the system
was under governance control at the moment it acted. A post-hoc log cannot answer
that question definitively. Execution evidence can. It is the difference between a record
that is consistent with control and a record that proves it.
The distinction has insurance significance. An underwriter assessing whether an autonomous system operated within its governance envelope cannot rely solely on
outcome data. Outcomes are consistent with both governed and ungoverned systems
— a system that happens to act within policy without being governed by policy
produces the same outcome record as a system that was governed. Execution evidence
breaks that equivalence. It provides direct proof that a governance determination
preceded each action, not merely that the action was consistent with policy.

The distinction has regulatory significance. Every major AI governance framework demands traceability and auditability.54 Those terms, as currently defined in regulatory
instruments, do not distinguish between post-hoc reconstruction and contemporaneous evidence. Execution evidence satisfies the intent of those requirements in a way
that audit logs do not — and as regulatory frameworks mature, the distinction between
reconstructed traceability and proven governance presence will become a compliance
boundary.
The evidentiary independence argument from Chapter 21A applies directly here. Evidence produced at the execution boundary must be designed to survive the journey
from the moment of action to the human-speed institutions — courts, regulators, and
insurers — that will eventually evaluate it. Evidence produced by a kernel that shares
physical infrastructure with the system it governs is evidence whose integrity cannot
be guaranteed by the kernel alone. The architecture must separate the act of enforcement from the act of proof — the kernel enforces locally, the evidence travels to where
its integrity can be independently verified.
Execution evidence is therefore not merely an output of the EGK. It is the mechanism
by which the EGK’s governance function extends beyond the moment of action into
the domains of liability, insurance, and regulatory compliance. The EGK governs at
the boundary. The evidence it produces proves that governance occurred. That proof
travels forward in time — into legal proceedings, into underwriting assessments, into
regulatory reviews — carrying the only information those processes actually need: that
a determination was made, before the action, by a governance mechanism that was
present.
The chain from execution to accountability runs through evidence. Without execution
evidence, accountability is reconstructed. With it, accountability is proven.
That is not a subtle difference. It is the difference that the rest of this paper depends
upon.

## Chapter 26 — Liability Convergence

Liability follows control.
This is not a novel legal principle. It is one of the oldest organizing concepts in tort
law.55 The entity that controlled the instrument that caused harm bears the liability
for that harm. Control and liability are paired because control implies the capacity
       Traceability and auditability requirements are established in European Parliament & Council of the
European Union (2024). Regulation (EU) 2024/1689 on Artificial Intelligence (EU AI Act). Article 12 (automated logging requirements) and Article 13 (transparency requirements); and National Institute of Standards and Technology (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI
100-1. Govern 1.6 and Map 1.5 (traceability requirements). Neither framework distinguishes between
post-hoc reconstruction and contemporaneous evidence — the distinction introduced in this chapter is an
original contribution of this paper.
       The control-liability relationship in tort doctrine is established in Restatement (Third) of Torts: Products Liability § 1 (1998). American Law Institute; and Prosser, W.L. & Keeton, W.P. (1984). The Law of
Torts (5th ed.). West Publishing. § 41. The principle that liability attaches where control was last possible
is a foundational organizing concept of Anglo-American tort law, not a novel claim of this paper.

to have prevented the outcome. Where control was present, liability attaches. Where
control was absent, liability migrates to whoever did have control — or, in its absence,
to whoever was closest to it.
Autonomous systems do not dissolve this principle. They stress-test it.
When a human makes a consequential decision, the locus of control is clear. The human
decided. The human acted. If the outcome was harmful, the human — or the organization the human represented — bears liability. The chain from decision to consequence
to accountability is short, direct, and legally legible.
When an autonomous system makes a consequential decision, the chain lengthens. The
model provider trained the system. The operator deployed it. The developer configured its tools and permissions. The principal directed its objective. Each contributed
to the conditions under which the consequential action occurred. None of them were
present at the moment it occurred. The action was autonomous — which is to say, it
occurred without a human decision at the moment of execution.
This is the liability problem that autonomous systems create. Not the absence of responsible parties — there are many. The absence of a clear locus of control at the moment
the consequential action committed.
California AB 316, effective January 1, 2026,56 addresses one dimension of this directly.
It forecloses the defense that an autonomous system’s independent operation relieves
its operator of liability. The AI did it is no longer a defense. Operators remain liable for
what their autonomous systems do. But the statute, while clarifying who bears liability,
does not clarify where in the system’s operation that liability should be anchored —
which decision, which moment, which architectural point represents the exercise of
control for which the operator is responsible.
The execution boundary answers that question.
If liability attaches where control was last possible, and the execution boundary is the
last point at which a consequential action could have been permitted or denied, then
liability converges on the execution boundary. Not because a court has so held — none
yet has, in terms this specific — but because the underlying logic of liability doctrine,
applied to the architecture of autonomous systems, produces that result.
An operator who deploys an autonomous system with an EGK at the execution boundary has exercised control at the last possible point. The EGK evaluated the action. It
applied policy. It produced a determination. The action that followed was permitted
by that determination. If the permitted action caused harm, the liability question becomes: was the governance policy adequate? Was the EGK correctly configured? Was
the authority correctly scoped? These are answerable questions. They are the questions
the liability doctrine is designed to resolve.

      California AB 316 (2025). Chaptered as amendment to California Civil Code. Effective January 1,
2026. California Legislative Information. The statute forecloses the defense that an autonomous system’s
independent operation relieves its operator of liability — establishing operator accountability without
specifying the architectural point at which that accountability should be anchored.

An operator who deploys an autonomous system without an EGK at the execution
boundary has not exercised control at the last possible point. The action occurred without a governance determination. Liability does not disappear — AB 316 ensures that —
but its anchor is unclear. The operator is responsible for an outcome that they had the
architectural capacity to govern and chose not to. That is a worse liability position than
governing imperfectly.
This creates a precise incentive structure. Operators who instrument the execution
boundary with an EGK can demonstrate, through execution evidence, that control was
exercised at the last available point. Operators who do not cannot make that demonstration. As liability doctrine develops around autonomous systems — and it will, as
consequential failures accumulate and litigation follows — the presence or absence of
execution-boundary governance will become a material factor in determining both liability and its allocation.
The convergence is not yet complete. Courts have not yet mapped liability doctrine onto
autonomous system architecture in the terms this paper uses. Regulators have not yet
required execution-boundary instrumentation as a condition of deployment. Insurers
have not yet made execution evidence a coverage condition.
But the trajectory is clear. Liability follows control. Control, in autonomous systems,
is architecturally locatable. The execution boundary is where it is located. As that understanding matures — in courts, in regulatory bodies, in insurance markets — liability
will converge on the execution boundary not as a legal innovation but as the application
of established principle to a new architectural reality.
The trajectory is no longer confined to academic prediction. Legal analysis of multiagent systems published in 2025 and 2026 is actively proposing identity standards, delegation tracking, handoff logging, and fault allocation across chains of autonomous
decisions — frameworks that assume liability will attach to specific execution points
rather than diffuse across the system.57 Willis Towers Watson has characterized AI
deployment as an accountability and liability challenge in which adoption is materially outpacing governance capability.58 The emerging litigation question is not which
model generated an output. It is who had authority at the moment of execution, what
controls existed, and what evidence proves it. That question has a precise architectural
answer. It is the execution boundary.
The execution boundary is not merely a governance concept. It is the point at which
accountability becomes locatable, liability becomes attributable, and the chain from autonomous action to legal consequence becomes legally coherent.
       Legal analysis actively proposing liability frameworks for multi-agent autonomous systems includes
Hoshino, T. (2026). The Price of Over-Delegation: Stackelberg Liability Design for Agentic AI Handoffs.
ICML 2026 Workshop (NExT-Game), June 6, 2026 — which proves mathematically that partial liability internalization across agent handoffs structurally inflates delegation depth and obscures forensic attribution;
and Tallam, K. (2026). Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure. arXiv:2605.05440 — which proposes cryptographic delegation tracking as the infrastructure
for establishing liability at specific execution points.
       Lipkin, S. & Willis Research Team (2026). Risk & Resilience Review: AI in Action — The Road to Responsible Adoption. Willis Towers Watson, May 27, 2026. wtwco.com/en-gb/insights/2026/05/risk-andresilience-review-ai-in-action-the-road-to-responsible-adoption

That is what makes it the most important architectural concept in autonomous systems
that no governance framework has yet named.

## Chapter 27 — Underwriting Autonomous Systems

Insurance exists because consequences are uncertain and losses are real.
For centuries, underwriters have solved the same problem: how to price risk that has
not yet materialized, based on evidence of controls that are already in place. The premium is not a guess. It is a calculation — anchored in the probability of a loss event,
the magnitude of potential loss, and the quality of the controls that reduce both.
That calculation depends on one thing above all else: evidence that the controls actually
work.
A fire insurer does not merely ask whether a building has a sprinkler system. It asks
whether the sprinkler system was inspected, whether it is operational, and whether
it will activate when conditions require.59 A maritime insurer does not merely ask
whether a vessel has safety equipment. It asks whether the equipment is certified,
maintained, and accessible.60 The control must not only exist. It must be demonstrably
present at the moment it would be needed.
This is the underwriting principle that autonomous systems are about to collide with.
Current underwriting of technology risk relies on a set of controls that were designed
for human-speed systems. Security questionnaires ask whether policies exist. Audits
verify whether documentation is maintained. Certifications confirm whether processes
were followed. The underlying assumption is that human oversight is present — that a
human reviewed the decision, that a human could have intervened, that the chain of accountability runs through identifiable human actors whose judgment the underwriter
is, in effect, insuring.
Autonomous systems break that assumption at the foundation.
When an autonomous agent executes a consequential action without human initiation
or review, the underwriter faces a new question for which existing frameworks provide no answer: was the system under governance control at the moment the action
occurred? Not in general. Not in principle. At that moment. For that action.
A policy document cannot answer that question. An audit trail assembled after the fact
cannot answer it definitively. A certification that the system passed testing at deployment cannot answer for the action that occurred six months later under conditions that
were not tested.
       Fire insurer inspection requirements as a precondition for coverage are established in NFPA 25 (2023).
Standard for the Inspection, Testing, and Maintenance of Water-Based Fire Protection Systems. National Fire Protection Association. The standard specifies inspection frequencies, operational testing requirements, and
documentation standards that underwriters rely upon as evidence of control presence.
       Maritime safety equipment certification requirements are established in IMO SOLAS Chapter III
(2020 consolidated edition). Life-Saving Appliances and Arrangements. International Maritime Organization.
Certification, maintenance records, and accessibility documentation are standard underwriting inputs for
marine hull and liability coverage.

Only execution evidence can answer it.
The evidence artifact produced by an EGK at the execution boundary is precisely the
evidence an underwriter needs. It is contemporaneous with the action. It is specific
to the action. It records what was proposed, what policy applied, what authority was
evaluated, and what determination was reached — before the action committed, at the
moment when governance was either present or absent. It does not reconstruct control.
It proves it.
This has direct implications for how autonomous system risk will be underwritten as
the market matures.
The first implication is coverage conditionality. Underwriters will increasingly require
evidence of execution-time governance as a condition of coverage for autonomous systems operating in high-consequence domains. Not documentation of governance intent. Not certification of governance policy. Evidence that governance was present at
execution — the same standard applied to sprinkler systems, safety equipment, and
pre-trade risk controls in every other domain where consequences are irreversible and
losses are material.61
The second implication is premium differentiation. Systems that produce execution
evidence will be priced differently from systems that do not. The difference is not cosmetic. It is actuarial. A system that can demonstrate governance presence at every
consequential action presents a fundamentally different risk profile than a system that
can only demonstrate governance intent. The evidence collapses the uncertainty that
drives premium pricing.
The third implication is admissibility metrics. As execution evidence becomes a standard underwriting input, the specific signals derivable from EGK output become actuarial variables. Denial rate — the proportion of proposed actions that the EGK denied
— is a measure of governance activity. Constraint violation frequency measures how
often the system approaches its governance boundaries. Override rate measures how
often human escalation was required. The policy compliance score measures adherence
to the compiled governance policy across all actions. Governance availability measures
the uptime of the EGK itself, because a governance kernel that was offline when a consequential action was executed is a governance kernel that did not govern that action.
These metrics are fully developed in Chapter 28.
The fourth implication concerns coverage boundaries. As liability doctrine converges
on the execution boundary — as courts and regulators increasingly ask whether governance was present at the moment of action — the insurance market will align its coverage structure accordingly. Policies will specify execution-time governance requirements as coverage conditions. Claims will be evaluated against execution evidence
records. Coverage disputes will turn on whether the EGK was operational, correctly
configured, and actually invoked for the action that caused the loss.
      The pre-trade risk check as the established precedent for execution-time governance as a coverage
condition in financial markets is documented in FINRA Rule 15c3-5 (2010). Market Access Rule. Financial
Industry Regulatory Authority; and SEC Release No. 34-63241 (2010). Risk Management Controls for Brokers
or Dealers with Market Access. U.S. Securities and Exchange Commission.

The underwriting market for autonomous systems is nascent. The frameworks do not
yet exist. The precedents are still forming. The metrics have not been standardized. But
the direction is not ambiguous.
Insurance has always required evidence of controls at the point of consequence. Autonomous systems create consequences at machine speed, without human presence,
at volumes that exceed human review capacity. The controls that matter are the ones
present at execution. The evidence that matters is the evidence produced there.
An autonomous system that cannot demonstrate execution-time governance cannot be
underwritten in the same way a building without a sprinkler system cannot be insured
against fire — not because the insurer is unwilling, but because the risk cannot be priced
without evidence that a control exists at the point where the loss would originate.
The execution boundary is that point. Underwriting will find it, because underwriting
always follows loss to its source.
The market is not waiting for theory to settle. A structural split has already formed.
Carriers including QBE and Beazley have moved toward sublimits and exclusion language for AI-linked losses, including autonomous agent abuse and AI-related regulatory breaches. Verisk and ISO have filed optional generative AI exclusion endorsements
for general liability and commercial umbrella coverage. Simultaneously, aﬀirmative AI
coverage has emerged: Cowbell’s Prime One offers up to ten million dollars in limits
with named coverage for AI-related incidents, and Munich Re’s aiSure product frames
AI as a distinct risk layer beyond conventional cyber, explicitly including failures not
caused by malicious attack. The insurance industry’s standard response to a risk it cannot price is exclusion. The emergence of dedicated aﬀirmative products alongside those
exclusions confirms that AI is now a named insurable peril — and that the underwriting market is actively searching for the evidence infrastructure that would allow it to
price that peril rationally rather than exclude it conservatively. The observability gap
is the commercial gap. Execution evidence is what closes it.62

## Chapter 28 — Admissibility Metrics

Evidence without measurement is anecdote.
The preceding chapters established that execution evidence is the foundational artifact
of execution-boundary governance — the contemporaneous proof that a governance
determination was made before a consequential action was committed. But proof of
presence is only the beginning of what underwriters, regulators, and liability courts
will eventually require. What they will require next is proof of performance.
Not merely that an EGK was present. That it worked.
     The structural split in the AI insurance market is documented in: Resultsense/Financial Times (2026).
London insurers cap cyber payouts as AI ‘LLMjacking’ losses mount. April 22, 2026 — confirming QBE
sublimit of £188,000 on a £3.8M policy and Beazley sublimits on AI-linked losses; Insurance Services Oﬀice
/ Verisk (2026). Generative Artificial Intelligence Exclusion Endorsements. Effective January 1, 2026. Forms
CG 40 47, CG 40 48, CG 35 08; Cowbell Cyber Inc. (2026). Cowbell Prime One Cyber Insurance. U.S. Launch
April 21, 2026. cowbell.insure/prime-one; Munich Reinsurance Company (2026). aiSure™: Performance
Guarantee Insurance for Artificial Intelligence Solutions. munichre.com/insure-ai.

Admissibility metrics are the measurable signals derivable from EGK output that answer that question. They are not abstract compliance indicators. They are operational
variables — generated continuously, at execution time, as a natural byproduct of the
EGK’s function — that collectively describe the governance health of an autonomous
system over time.
Five metrics form the core of the admissibility framework proposed in this paper.
The first is the denial rate. The proportion of proposed actions that the EGK denied
relative to the total actions it evaluated within defined consequence scope. Denial rate
is a measure of governance activity — evidence that the kernel is not merely present but
engaged, and that it is encountering actions that reach the boundary in a state requiring
a negative determination. A system with a zero denial rate across all high-consequence
action types is not necessarily well-governed. It may be a system whose agents never
approach their governance boundaries — or it may be a system whose EGK is misconfigured to permit everything. Denial rate requires interpretation in context, but its
absence from an underwriting assessment is a gap.
The second is constraint violation frequency. The rate at which proposed actions arrive at the execution boundary in violation of one or more compiled policy constraints
before the EGK’s determination. This is distinct from denial rate — a proposed action
may violate a constraint and still be permitted under escalation conditions, or the violation may be minor enough to fall within a permitted tolerance. Constraint violation
frequency measures how often the system is operating near its governance boundaries,
which is a leading indicator of the conditions under which failures are most likely to
occur.
The third is the override rate. The proportion of EGK determinations — permits or denials — that were subsequently overridden by a human escalation. Override rate measures the gap between compiled policy and operational reality. A high override rate
on denials suggests that the compiled policy is too restrictive for the operating environment — that human judgment is consistently reversing the kernel’s determinations in
ways that suggest the governance compilation requires revision. A high override rate
on permits suggests the opposite: that the EGK is permitting actions that human reviewers are subsequently flagging as inadmissible. Either pattern is a signal. Neither
is visible without the metric.
The fourth is the policy compliance score. A composite measure of the proportion of
executed actions that, in retrospect, were consistent with the full set of applicable governance policy — not merely the compiled constraints evaluated at the execution boundary, but the broader interpretive governance context that the compilation was designed
to capture. Policy compliance score is the bridge between executable and interpretive
governance: it asks whether the compiled policy accurately reflects the intent of the human governance framework it was derived from. Systematic gaps between compiled
policy and broader governance intent are a compilation failure — one that the policy
compliance score is designed to surface before it becomes a liability event.
The fifth is governance availability. The uptime of the EGK itself — the proportion of
time during which the kernel was operational and capable of evaluating actions at the

execution boundary. Governance availability is the most fundamental metric because
it is the precondition for all others. An EGK with perfect denial rate, zero constraint violations, and a flawless policy compliance score provides no governance during the intervals it is offline. For autonomous systems operating continuously, governance availability is not merely an operational metric. It is a coverage condition. An underwriter
who does not specify minimum governance availability as a policy requirement is underwriting an autonomous system that may operate without governance for unknown
intervals — and pricing that risk without the data required to quantify it.63
These five metrics — denial rate, constraint violation frequency, override rate, policy
compliance score, governance availability — are not exhaustive. As executionboundary governance matures and deployment experience accumulates, additional
metrics will emerge from operational practice. What the loss experience of governed
autonomous systems actually looks like. Which metrics correlate most strongly with
adverse outcomes. Which combinations of metric values predict the conditions under
which governance failures occur.
That actuarial knowledge does not yet exist because the systems that would generate
it do not yet exist at commercial scale. But the framework for generating it does. The
EGK produces execution evidence as a core property. Execution evidence contains the
raw data from which admissibility metrics are derived. The metrics are not a separate
instrumentation requirement imposed on top of the governance architecture. They are
a natural output of the architecture itself.
This matters for adoption. A governance architecture that requires additional instrumentation to produce its compliance evidence imposes a cost that selection pressure
will ultimately eliminate. A governance architecture whose compliance evidence is a
byproduct of its core function — generated automatically, at execution time, without
additional overhead — survives selection pressure because it costs nothing extra to produce.
Admissibility metrics are therefore not a measurement layer added to executionboundary governance. They are execution-boundary governance, observed over
time.
The underwriter who requires them is not imposing a new burden on the operator.
They are asking the operator to read the output of a system that, if governance is genuine, is already producing it.
External validation for this framework is emerging from an unexpected direction. An
IETF working draft circulated in 2026 proposes per-decision proof points, underwriting
evidence, premium differentiation, and parametric claims triggers for AI systems — explicitly identifying the decision-level evidence gap in AI insurance underwriting as the

     The foundational actuarial principle that premium pricing requires observable control metrics at the
point of consequence is established in Casualty Actuarial Society (1988). Statement of Principles Regarding
Property and Casualty Insurance Ratemaking. CAS. The regulatory precedent for mandated actuarial metrics
as coverage conditions is established in NAIC (current). Risk-Based Capital Model Laws and Regulations.
National Association of Insurance Commissioners. The five admissibility metrics proposed in this chapter
are an original contribution of this paper, derived from the EGK’s evidence generation property.

primary barrier to rational risk pricing.64 Separately, academic research has proposed
authority frontier models that evaluate database mutations, payments, refunds, commitments, and other side-effect-bearing actions as underwriting variables — attempting to price authority itself rather than system characteristics.65 These frameworks are
nascent and unstandardized. But their convergence on the same five observable variables this paper proposes — what was proposed, what policy applied, what authority existed, what was determined, and whether the governance mechanism was operational — is not coincidental. It is the actuarial community independently discovering
that execution-boundary evidence constitutes the minimum information set required
to move autonomous system risk from the exclusion column to the coverage column.
If the output does not exist, the governance was not genuine.
That is the test. It is a simple one. And it is the test that the underwriting market for autonomous systems will eventually apply — because it is the only test that distinguishes
a system that was governed from a system that was documented.

## Chapter 29 — Prior Art and Honest Placement

This paper does not claim to have invented the execution boundary.
That claim would be false, and a reviewer who tested it would quickly find it so. The
concept of a deterministic control point operating immediately prior to a consequential
action is not new. It appears in the literature of cybersecurity, safety engineering, and
financial market design, under different names, with different scopes, serving different
purposes. Honest engagement with that prior art is not a weakness of this paper’s
contribution. It is a precondition for the contribution being taken seriously.
The oldest and most direct precedent is the reference monitor, introduced in the Anderson Report of 1972.66 The reference monitor concept specifies a mechanism that
must be invoked on every access attempt, must be tamper-proof, and must be small
enough to be subject to analysis and testing. Three of the five EGK properties defined
in Chapter 14 — complete mediation, tamper resistance, and determinism — are direct
descendants of the reference monitor’s defining requirements. This lineage is not coincidental. The reference monitor was addressing the same structural problem: how
to enforce policy at the point of action rather than before or after. The EGK extends
that solution to a new domain — autonomous agentic systems operating in economic
      Adebayo, T., Apalowo, O., & Makanjuola, F. (2026). OMP Domain Profile: AI Liability Insurance Underwriting and Parametric Claims Evidence. IETF Network Working Group. draft-veridom-omp-aiins-00,
April 5, 2026. The draft proposes per-decision proof points and parametric claims triggers as the mechanism for moving AI risk from the exclusion column to the coverage column — independently converging
on the execution-boundary evidence framework proposed in this paper.
      Chen, H-H. (2026). Insuring Every Action: An Authority Frontier Framework for Runtime Actuarial
Control of Autonomous AI Agents. arXiv:2605.25632. Companion paper: SSRN 6761960. The authority
frontier framework proposes pricing authority itself — the capacity to execute consequential actions — as
the primary actuarial variable, treating every side-effect-bearing tool call as an insurable micro-exposure.
      Anderson, J.P. (1972). Computer Security Technology Planning Study. ESD-TR-73-51. Electronic Systems
Division, Air Force Systems Command, Hanscom AFB, Massachusetts. The reference monitor’s three
defining properties — complete mediation, tamper resistance, and verifiability — are the foundational
prior art from which three of the five EGK properties directly descend.

and digital environments — and adds two properties the reference monitor did not require: latency compatibility as a formal design constraint derived from the physics of
machine-speed execution, and evidence generation as a core output with downstream
legal, regulatory, and insurance implications rather than an incidental capability.
Safety engineering provides a second lineage. The safety kernel concept, embedded in
standards including IEC 61508 and ISO 26262,67 specifies a minimal verified component
that enforces critical constraints regardless of the behavior of surrounding systems. The
safety kernel operates at the boundary between the system under control and the physical or operational environment it affects — which is, in the language of this paper, the
execution boundary of a safety-critical system. The contribution this paper makes to
safety engineering is not architectural novelty but domain extension and formalization:
applying the safety kernel concept to autonomous AI agents operating in economic and
digital environments, and deriving the latency and locality requirements that govern
their deployment in those environments.
Financial markets provide a third lineage. Pre-trade risk checks — hard limits evaluated
before every order reaches an exchange, operating in microseconds, with no deliberation and no appeal in the moment — are execution-boundary governance mechanisms
deployed at commercial scale. They satisfy the complete mediation, determinism, and
latency compatibility requirements of the EGK as defined in this paper. They do not,
in their standard form, generate the structured evidence artifacts this paper proposes,
and they operate within a single domain rather than across the generalized action space
of an autonomous agent. But they demonstrate that execution-boundary governance
is not merely a theoretical possibility. It is operationally proven, at scale, in environments where latency budgets are measured in microseconds and the cost of failure is
immediate and measurable.
Zero trust architecture shares vocabulary with the EGK — continuous verification,
never trust always verify, least-privilege access — and deserves acknowledgment. The
distinction is precise: zero trust addresses access control across network segments and
identity boundaries; the EGK addresses admissibility of consequence-bearing actions
within an agentic execution path. These are related but distinct problems. Zero trust
governs whether an identity may access a resource. The EGK governs whether a
proposed action may commit to consequence. The scope of evaluation, the form of the
policy, and the downstream implications for liability and underwriting are different in
kind.68

       IEC 61508 (2010). Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems. International Electrotechnical Commission, Geneva; ISO 26262 (2018). Road Vehicles — Functional
Safety. International Organization for Standardization, Geneva.
       The zero trust model is established in Kindervag, J. (2010). No More Chewy Centers: Introducing the
Zero Trust Model of Information Security. Forrester Research; and codified in Rose, S., Borchert, O., Mitchell,
S., & Connelly, S. (2020). Zero Trust Architecture. NIST Special Publication 800-207. National Institute
of Standards and Technology. The distinction between zero trust access control and EGK admissibility
governance is an original contribution of this paper.

More recent prior art includes runtime policy enforcement systems such as PCAS,69
which applies Datalog-derived policy evaluation at the execution boundary of AI agent
actions, and the Aegis architecture, which interposes a policy enforcement layer between agent reasoning and tool execution.70 Both systems implement mechanisms with
substantial overlap with the EGK concept. Both predate this paper. Neither unifies the
latency constraint, the locality requirement, the liability convergence thesis, and the
underwriting implications into a single framework. That unification is the contribution
this paper makes — not the invention of boundary enforcement, but the derivation of
boundary enforcement as a necessary consequence of physical constraints that apply
across all domains in which autonomous systems operate.
Concurrent independent work has appeared in the April 2026 literature. Research
on embodied agent governance explicitly uses the term “execution boundary” and
proposes architectural requirements substantially similar to those defined in Chapter
14.71 Separately published work on execution governance proposes a structural separation between decision generation and execution authority that maps directly onto
the interpretive-to-executable governance transition described in Chapters 9 through
12.72 This paper was developed concurrently with those contributions, not in response
to them. Where they overlap, the overlap is evidence of convergence — multiple independent lines of inquiry arriving at the same architectural conclusion — rather than
derivation.
The honest placement of this paper within the existing literature is therefore as follows.
The execution boundary as a control point is established prior art. The reference monitor, the safety kernel, and the pre-trade risk check each implement it within their respective domains. This paper does not claim that concept as novel.
The EGK as a unified architectural specification; the governance compilation model; the
time-domain mismatch framework; the authority migration thesis; the human latency
subsidy concept; the liability convergence argument; the four-locality framework; and
the underwriting implications — taken individually, each has partial precedents or concurrent developments. Taken together, as a unified framework derived from physical

       Executable Governance for AI: Translating Policies into Rules Using LLMs. arXiv:2512.04408. PCAS
applies Datalog-derived policy evaluation at the execution boundary of AI agent actions — a mechanism
with substantial overlap with the EGK’s deterministic admissibility evaluation function.
       Mazzocchetti, A.M. (2026). Cryptographic Runtime Governance for Autonomous AI Systems: The
Aegis Architecture for Verifiable Policy Enforcement. arXiv:2603.16938. Zenodo DOI: 10.5281/zenodo.19027190. Aegis interposes a cryptographically sealed policy enforcement layer between agent reasoning and tool execution, demonstrating median proof verification latency of 238ms and publication
overhead of approximately 9.4ms.
       Qin, X., Luan, S., See, J., Boukhers, Z., Yang, C., & Li, Z. (2026). Harnessing Embodied Agents:
Runtime Governance for Policy-Constrained Execution. arXiv:2604.07833 (v4, June 10, 2026). The paper
explicitly uses the term “execution boundary” and proposes a runtime governance layer intercepting proposed action intentions before execution — demonstrating 96.2% ± 2.7% interception of unauthorized
actions across more than 1,000 randomized simulation trials.
       Swearingen, K. (2026). Execution Governance: A Control-Plane Architecture for Mediating Actions
of Adaptive Systems. SSRN 6441961. DOI: 10.2139/ssrn.6441961. Swearingen proposes a Governance
Gate — a non-bypassable structural interlock at the execution boundary — that shifts the system’s baseline
state from default-execute to default-block, directly paralleling the EGK’s tamper resistance and complete
mediation properties.

constraints that apply across all domains of autonomous system deployment, they constitute a contribution not found in the prior literature in this form.
The paper’s claim is not priority of discovery. It is priority of synthesis — the first
unified treatment of execution-boundary governance as a physical necessity, a liability anchor, and an underwriting requirement, derived from first principles that apply
wherever autonomous systems act with consequence.
That claim is defensible. It is the claim this paper makes.

## Chapter 30 — Objections and Counterarguments

Every significant architectural proposal attracts objections. The objections to executionboundary governance are predictable, some of them serious, and all of them worth
addressing directly. A framework that cannot survive its strongest counterarguments
does not deserve adoption. What follows is an honest engagement with the best case
against the claims this paper has made.
Objection one: This is just a reference monitor.
The reference monitor, introduced in the Anderson Report of 1972, is the most direct
precedent for the EGK. A reviewer who reduces the EGK to a reference monitor is not
wrong about the lineage. They are wrong about the contribution.
The reference monitor was designed for a specific problem: access control in operating systems. Its three defining properties — complete mediation, tamper resistance,
and verifiability — address whether a subject may access an object. The EGK inherits those properties and extends them in two directions the reference monitor did not
address. First, latency compatibility as a formal design constraint derived from the
physics of machine-speed execution — the reference monitor literature does not model
the latency budget as a variable that determines whether governance is controlling or
merely observational. Second, evidence generation as a core output with downstream
legal, regulatory, and insurance implications — the reference monitor produces an access decision, not a governance artifact designed to travel forward in time into liability
proceedings and underwriting assessments.
More fundamentally, the reference monitor is a mechanism. This paper proposes a
framework — one that derives the need for that mechanism from first principles applicable across domains, connects it to a liability convergence thesis, grounds it in a physical analysis of information propagation, and extends its implications into insurance
markets that did not exist when the reference monitor was conceived. The mechanism
is inherited. The framework is new.
Objection two: Runtime assurance already exists.
Runtime assurance systems — deployed in aviation, automotive, and industrial control
— monitor system behavior during operation and intervene when safety constraints are
violated. They are execution-boundary mechanisms in the precise sense this paper uses.
The objection is factually correct.

The response is domain and formalization. Runtime assurance as currently practiced
operates in physical systems under well-defined safety standards, with deterministic
plant models and bounded state spaces. Autonomous AI agents operating in economic
and digital environments present a different problem: unbounded action spaces, natural language policy sources, cross-domain consequence classes, and liability implications that safety engineering standards do not address. The EGK is not a runtime
assurance system. It is a generalization of the runtime assurance concept to a domain
where the existing standards do not apply and the governance compilation problem
— translating natural language policy into machine-enforceable constraints — does not
have an established solution.
Objection three: Policy cannot be fully compiled.
This is the most technically substantive objection and deserves the most careful response.
Natural language policy contains irreducible ambiguity. Edge cases exist that policy
authors did not anticipate. Novel situations arise that no compiled rule set can address.
A governance compilation process that claims to fully capture interpretive governance
in executable form is making a claim that formal verification researchers have been
unable to substantiate for decades.
The paper does not make that claim. Governance compilation is proposed not as a complete translation of interpretive governance into executable form, but as a partial one
— suﬀicient to govern the anticipated consequence classes and action types, while preserving human escalation paths for cases that cannot be anticipated. The EGK does not
replace interpretive governance. It enforces the subset of governance that can be compiled, and escalates the remainder. The incompleteness of compilation is not a refutation of the EGK model. It is a design parameter — one that determines the boundary
between what the kernel enforces autonomously and what it refers to human judgment.
The stronger version of this objection — that the compiled subset is too small to constitute meaningful governance — is an empirical question that cannot be settled in advance. In financial markets, pre-trade risk checks compile a surprisingly large proportion of consequential governance into deterministic rules.73 Prose2Policy demonstrates
95.3% compilation rates on benchmark policy datasets.74 The answer will emerge from
deployment experience, not from theory.
Objection four: Latency is overstated.

       The pre-trade risk check as evidence that a large proportion of consequential financial governance
can be compiled into deterministic rules is documented in FINRA Rule 15c3-5 (2010). Market Access Rule.
Financial Industry Regulatory Authority. The rule mandates pre-trade controls covering order size, position limits, credit limits, and regulatory compliance — demonstrating that governance compilation at
scale is operationally proven in high-consequence environments.
       Prose2Policy (P2P): A Practical LLM Pipeline for Translating Natural-Language Access Policies into
Executable Rego. arXiv:2603.15799. The 95.3% compilation rate on the ACRE benchmark dataset provides
the strongest available empirical evidence that governance compilation at meaningful scale is achievable
with current technology.

The 25-millisecond envelope is presented in this paper as a current benchmark for
high-consequence agentic actions. A reviewer may argue that most consequential autonomous actions do not occur at that latency — that fund transfers, database modifications, and regulatory filings involve human-readable interfaces and processing delays
that provide adequate governance windows without a local EGK.
This objection is correct about the present and wrong about the trajectory. Many highconsequence autonomous actions today operate within latency windows that permit
cloud-hosted governance. The paper’s argument is not that all autonomous systems are
currently operating beyond governance reach. The trajectory is toward shorter action
latency as systems mature, and governance architectures designed for today’s latency
windows will be inadequate for tomorrow’s. Building governance architecture for the
current state of autonomous systems is building for obsolescence. The 25-millisecond
envelope is not the current average. It is the near-term constraint that governance architecture must be capable of satisfying.
Objection five: Human oversight remains suﬀicient.
The argument that human oversight — review, approval, monitoring — remains an adequate governance mechanism for autonomous systems is the most common objection
in practice and the least defensible under examination.
Human oversight is adequate when three conditions hold: the volume of decisions remains within human review capacity, the interval between decision and consequence
is long enough for human intervention, and the cost of human review is acceptable
relative to the value of the governed activity. Each of these conditions is being systematically and increasingly violated by the autonomous systems this paper addresses.
Volume exceeds capacity. Intervals compress below intervention thresholds. Review
costs make oversight economically unviable at scale.
The objection that human oversight remains suﬀicient is therefore not an argument
about autonomous systems as they are becoming. It is an argument about autonomous
systems as they were. It describes a condition that is passing, not one that will persist.
This paper does not argue that human oversight should be removed. It argues that
human oversight must be repositioned — upstream of the execution boundary, where
interpretation belongs, rather than at the boundary itself, where only enforcement is
possible.
Objection six: A suﬀiciently capable agent can bypass the EGK.
This is the most serious objection in the long run. If an autonomous agent is capable of
reasoning about its own governance architecture, it may be capable of finding paths to
consequential action that do not pass through the EGK — through tool combinations,
through intermediate steps that individually appear non-consequential, through social
engineering of human override mechanisms.
The paper does not claim that the EGK is bypass-proof against arbitrarily capable adversarial agents. It claims that the EGK satisfies the tamper resistance property — that

it is structurally isolated from the agent whose actions it governs — and that this isolation makes bypassing it significantly harder than with alternatives. Complete bypassproofness is not achievable for any governance mechanism against a suﬀiciently capable adversary. The relevant comparison is not between a bypassable EGK and an
un-bypassable alternative. It is between a bypassable EGK and no governance at the
execution boundary at all. The EGK is not perfect. It is better than the alternative by a
margin that scales with the severity of the governed consequence class.
The bypass objection also conflates capability with intent. Most autonomous systems
operating in commercial and regulated environments are not adversarial agents seeking to circumvent their governance. They are systems operating within defined tool
sets and permission scopes, whose consequential actions flow through identifiable execution surfaces. For those systems — which constitute the vast majority of the deployment contexts this paper addresses — the EGK’s tamper resistance property is adequate. The adversarial case is a research problem for future work, not a refutation of
the framework for the present one.
Objection seven: The multi-agent chain problem makes the EGK unworkable in
practice.
In multi-agent systems, actions are chained across agent boundaries. The EGK governs a single execution surface. But authority may have been established several agenthops earlier, by an entity with no direct knowledge of what the downstream agent will
ultimately do. If the EGK cannot resolve authority across agent chains, its complete
mediation property fails wherever agents delegate to other agents.
This is a genuine limitation, acknowledged directly in Chapter 31.75 The response is
scope, not denial. The EGK as specified governs a defined execution surface within
a defined authority context. Multi-surface governance across agent chains is an open
problem — but it is an open problem for all governance approaches, not a unique failure of the EGK. The question is not whether the EGK solves multi-agent governance
perfectly. It is whether it governs the execution surfaces it can reach better than any
available alternative. For those surfaces, it does.

## Chapter 31 — Limitations and Future Research

This paper has made strong claims. Intellectual honesty requires stating clearly what it
has not established, what remains unresolved, and where the framework requires work
that this paper does not attempt.
The governance compilation problem is unsolved — but actively being addressed.

      The formal game-theoretic treatment of over-delegation and liability diffusion in multi-agent handoffs is established in Hoshino, T. (2026). The Price of Over-Delegation: Stackelberg Liability Design for
Agentic AI Handoffs. ICML 2026 Workshop (NExT-Game), June 6, 2026 — proving mathematically that
partial liability internalization structurally inflates delegation depth and obscures forensic attribution. Authorization propagation as candidate infrastructure for resolving the multi-agent boundary problem is
proposed in Tallam, K. (2026). Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure. arXiv:2605.05440.

Chapter 12 introduced governance compilation as the mechanism by which interpretive policy becomes executable constraint. It argued that the transformation is possible,
necessary, and analogous to software compilation. It did not solve the compilation
problem.
Translating natural language policy into machine-enforceable constraints with provable
fidelity to the original intent remains an open research problem. However, it is no longer
unaddressed. A convergent body of work is actively closing the gap from multiple
directions simultaneously.
Prose2Policy demonstrates an end-to-end pipeline that ingests natural-language access
control policies and compiles them into executable Rego modules via a structured
DSARCP schema — Decision, Subject, Action, Resource, Condition, and Purpose.
On benchmark datasets, the pipeline achieves a 95.3% compile rate with automated
test validation, demonstrating that a meaningful proportion of interpretive policy is
already compilable at production scale.76 Policy-to-Tests extends this with SMT-based
consistency auditing: before compiled rules are deployed, a satisfiability solver
evaluates them for logical contradictions, exemption conflicts, and ruleset coherence.77
Conflicts are routed to a repair loop rather than deployed. RegScale’s continuous
controls monitoring architecture goes further, linking compiled policy directly to live
infrastructure evidence, replacing periodic audit cycles with real-time verification.
What these systems collectively demonstrate is that governance compilation is not waiting for a theoretical breakthrough. It is being operationalized now, domain by domain,
with human escalation handling residual ambiguity. The EGK does not require complete compilation to be effective. It requires suﬀicient compilation — enough to govern
the consequence classes that can be anticipated, while preserving escalation paths for
those that cannot. The market is actively building the tools that make that suﬀiciency
achievable.
Future research must address the remaining hard problems: which formal representations adequately serve as proxies for natural language policy in edge cases? What
verification methods can assess compilation fidelity across jurisdictions? What residual ambiguity is acceptable, and how should the EGK behave when a proposed action
falls in the uncompiled region?
The multi-agent boundary problem is unresolved.
This paper has treated autonomous systems largely as individual agents acting on individual execution surfaces. That model is already insuﬀicient.
In multi-agent systems, actions are chained. Agent A calls Agent B as a tool. Agent B’s
output becomes the input to Agent C’s consequential action. The execution boundary
       Prose2Policy (P2P): A Practical LLM Pipeline for Translating Natural-Language Access Policies into
Executable Rego. arXiv:2603.15799. The DSARCP schema — Decision, Subject, Action, Resource, Condition, and Purpose — provides the structured intermediate representation enabling systematic compilation
of natural language policy into executable Rego modules.
       Executable Governance for AI: Translating Policies into Rules Using LLMs. arXiv:2512.04408. The
SMT-based consistency auditing uses satisfiability solvers to verify ruleset coherence before deployment,
routing conflicts to a repair loop rather than permitting logically inconsistent compiled policy to reach the
execution boundary.

for the consequential action lies within Agent C’s workflow. But the authority that
permitted the chain of actions was established in Agent A’s context. The governance
determination that should have preceded Agent C’s action may have been made — or
not made — several steps earlier by an entity with no direct knowledge of what Agent
C would ultimately do.
Where is the EGK in a multi-agent chain? Whose compiled policy applies at the execution boundary of Agent C — the principal who initiated Agent A, the operator who
deployed Agent B, or the infrastructure provider whose system Agent C runs on? How
is authority transmitted across agent boundaries without being forged, diluted, or lost?
These questions do not have established answers. They are among the most important
open problems in agentic system governance, and this paper’s framework does not resolve them. They are not unique to execution-boundary governance — they are open
problems for all governance approaches to multi-agent systems. But they represent the
clearest boundary of the current framework’s applicability.78
The adversarial bypass problem remains open.
A suﬀiciently capable agent operating in an open-ended environment may discover action sequences that achieve consequential effects through combinations of individually
low-consequence steps — each of which passes the EGK’s admissibility check because
each, in isolation, falls below the consequence threshold that triggers full governance
evaluation. The aggregate effect of the sequence is high-consequence. Each individual
step was permitted.
This is the compositional bypass problem. It is the agent-economy equivalent of known
attack classes in security — the low-and-slow attack, the stepping-stone attack, the incremental privilege escalation. Defenses exist for those attacks in security contexts.
Analogous defenses for the compositional bypass of consequence-based governance
do not yet exist.
Future research must address how the EGK should reason about action sequences
rather than individual actions. What state must the kernel maintain across determinations to detect compositional consequence accumulation? How is that state maintained
eﬀiciently within the latency budget without violating the Minimal Surface Principle?
The evidence standardization and execution credential market is converging but not
yet standardized.
The evidence artifacts produced by the EGK have properties that extend beyond compliance. A contemporaneous, tamper-evident, cryptographically attributable record of
a governance determination is proof — and this kind of proof may eventually serve as
a settlement primitive in agent economies operating at machine speed.

     The multi-agent boundary problem is formally characterized in Hoshino, T. (2026). The Price of OverDelegation: Stackelberg Liability Design for Agentic AI Handoffs. ICML 2026 Workshop (NExT-Game),
June 6, 2026 — establishing mathematically that partial liability internalization across agent handoffs structurally inflates delegation depth and obscures forensic attribution. Candidate infrastructure for resolving
the authority transmission problem is proposed in Tallam, K. (2026). Authorization Propagation in MultiAgent AI Systems: Identity Governance as Infrastructure. arXiv:2605.05440.

The cryptographic verification infrastructure required to make execution credentials
viable is already being built, though not yet under that name. Merkle-anchored evidence architectures — systems that hash sequential execution events, structure them
as Merkle trees, and anchor the root to a public settlement ledger at regular intervals —
are in commercial deployment across regulated industries.79 The append-only, tamperevident evidence store with public anchoring is not a speculative primitive. It is an
operational architecture with known implementations.
The settlement layer for execution credentials is similarly nascent but directionally clear.
Public ledgers provide the neutral, decentralized anchoring surface that governance
evidence requires: a record no single operator controls, against which any party can
verify that a given Merkle root existed at a given time. The standardization of what
that proof contains — which fields constitute a governance determination, what policy
version applied, what authority context was evaluated — is the remaining work.
What does not yet exist is an execution credential standard: a formalized, interoperable credential format that enables a receiving system to verify an EGK determination
without replicating the governance evaluation. Future research must engage with standards bodies, legal scholars, and insurers to define what fields a governance evidence
artifact must contain to be legally admissible, what cryptographic standards it must
satisfy, and what public anchoring frequency is suﬀicient for evidentiary purposes.
The regulatory mapping is incomplete.
Chapter 24 argued that every major jurisdiction is converging on accountability,
traceability, and auditability requirements that execution-boundary governance is
positioned to satisfy. That argument is structural. It does not map specific EGK
properties to specific regulatory requirements in specific jurisdictions.
That mapping is necessary for adoption. An operator deploying an EGK in a regulated
environment needs to know which properties of the kernel satisfy which requirements
of which frameworks — EU AI Act Article X, NIST AI RMF Category Y, MAS Notice
Z. That specificity requires engagement with each regulatory framework in detail that
this paper’s scope does not permit. Future work should produce jurisdiction-specific
compliance mappings.
The insurance market framework is nascent.
Chapter 27 argued that underwriters will increasingly require execution-time evidence
as a coverage condition for autonomous systems. Chapter 28 proposed five admissibility metrics as actuarial inputs. Both arguments rest on a market that does not yet exist
at commercial scale.
The actuarial basis for pricing autonomous system risk has not been established. Loss
experience data from governed autonomous systems does not yet exist in volumes sufficient to support statistical modeling. The correlation between admissibility metrics

    Commercially deployed Merkle-anchored evidence architectures include Guardtime KSI technical
documentation and CodeNotary immuDB documentation (2024) — both implementing append-only,
tamper-evident evidence stores with public ledger anchoring in regulated industry deployments.

and loss outcomes has not been empirically validated. The coverage structures that
will govern autonomous system insurance have not been standardized.
This paper has argued the direction. The destination — a mature, actuarially grounded
underwriting market for autonomous systems with execution-boundary governance —
requires empirical data, market development, and regulatory engagement that is beyond this paper’s scope and ahead of the current state of the industry.
The physics argument has limits.
The 25-millisecond action-latency envelope is derived from current agentic system
benchmarks. Those benchmarks will change. As inference hardware improves and
agent architectures mature, action latency may compress further — tightening the
locality requirement — or may stabilize at levels that permit greater governance
distance than the current envelope suggests. The physics are fixed. The latency
budgets are not.
Additionally, the argument assumes that the EGK must operate synchronously —
that the governance determination must complete before the action executes. Asynchronous governance models, in which actions execute provisionally and are reversed
if the governance determination is negative, relax the synchronous latency constraint
at the cost of introducing rollback complexity and residual exposure to consequences
during the determination interval.
Asynchronous governance deserves more substantive treatment than this paper provides. For consequence classes where provisional execution is acceptable and rollback
is reliable, asynchronous models may prove viable and may significantly relax the locality requirement. The conditions under which asynchronous governance satisfies the
functional requirements of controlling governance — rather than merely documenting
it — are an important direction for future research.
What this paper has established, and what remains.
This paper has established the following with suﬀicient rigor to support academic examination: that existing AI governance frameworks contain no latency model; that
governance latency and action latency are distinct concepts whose relationship determines whether governance is controlling or observational; that time-domain mismatch
is a structural failure mode distinct from governance inadequacy; that the execution
boundary is a definable architectural concept with properties that distinguish it from
other control points; that an Executable Governance Kernel with five specified properties is the minimal mechanism capable of governing at that boundary within a defined
consequence scope; that liability converges on the execution boundary as autonomy increases; and that execution evidence is categorically different from audit logs in what
it proves.
What remains is substantial. The compilation problem. The multi-agent problem. The
adversarial bypass problem. Evidence standardization. Regulatory mapping. Insurance market development. Asynchronous governance models.
These are not failures of this paper. They are the research agenda it generates.

A framework that produces no open questions has not advanced the field. A framework
that produces the right open questions has.

## Chapter 32 — The Constraint Beneath the Frameworks

This paper has traveled through governance theory, computer science, economics,
liability doctrine, insurance markets, physics, and the emerging architecture of autonomous systems. The disciplines are different. The vocabulary is different. The
practitioners are different.
The conclusion is the same.
Every line of inquiry this paper has followed — from every starting point, through every domain, using every analytical framework available — converges on a single structural requirement: a determination must be made before a consequence-bearing action
commits, within a finite interval, at a point that is physically proximate to the execution
surface.
That is not a policy recommendation. It is not a framework preference. It is not a regulatory opinion.
It is a constraint.
Constraints of this kind are not invented. They are discovered. Gravity was not invented. The speed of light was not invented. The requirement that governance operate before consequence in order to influence consequence was not invented by this
paper. It was always true. What this paper has attempted is to make it visible — to
trace the same underlying requirement as it appears, independently, across disciplines
that rarely speak to one another.
Consider what each discipline found when it looked at autonomous systems operating
at machine speed.
Governance theory found that existing frameworks contain no latency model — that
they cannot distinguish between a system that prevented an inadmissible action and a
system that documented one. The absence of a theory of time means governance cannot
guarantee it operates before action rather than after.
Economics found that faster systems create selection pressure against expensive governance — that governance architectures imposing latency costs will be bypassed by
competitive pressure regardless of regulatory intent, and that the only governance that
survives is governance cheap enough to be deployed at the only point that matters.
Liability doctrine found that control and accountability are paired — that liability attaches where control was last possible, and that in autonomous systems, the last point
of possible control is the execution boundary. As autonomy increases, that is where
liability converges.
Insurance found that underwriting requires evidence of controls at the point of consequence — that documentation assembled after the fact cannot prove governance was
present before it, and that a market for autonomous system risk cannot be rationally

priced without contemporaneous evidence that a governance determination preceded
each consequential action.
Physics found that information travels at a finite speed — that governance architecture
requiring round-trips to distant infrastructure is physically incapable of satisfying the
latency condition in an increasing number of deployment configurations, and that the
pressure toward governance locality is permanent, not temporary.
Agent architecture found that reasoning and execution are different in kind — that governance distributed across reasoning steps burns latency and tokens at every step that
does not matter, and that governance concentrated at the execution boundary pays its
cost once, at the only step that does.
None of these disciplines set out to find the same thing. Each approached the problem
from its own starting point, using its own methods, asking its own questions. The
convergence is not the result of coordination. It is the result of independent inquiry
into the same underlying reality.
That reality is this.
Human institutions were built around human latency. They assumed human decisionmaking as the substrate. They evolved to govern a world where the decision-maker
paused, where the pause provided a governance window, and where that window was
long enough to accommodate the mechanisms humans developed to exercise control.
That world is not ending because machines are malicious. It is changing because a
new substrate exists — one that does not pause, does not wait, does not provide the
latency that human governance mechanisms have always consumed without knowing
they were consuming it.
The governance window that autonomous systems provide is not zero. But it is finite.
It is bounded by physics. It is located at the execution boundary. And it is shrinking as
systems mature.
The question this paper has asked, from the first chapter to this one, is whether governance can be present within that window — not in principle, not aspirationally, but
operationally, deterministically, at the moment when it is the only thing that can still
influence what happens next.
The Executable Governance Kernel is the answer this paper proposes to that question.
Not the only possible answer. The first answer that derives from first principles rather
than assuming them — that grounds the requirement for execution-boundary governance in physics and economics and liability doctrine and insurance markets and agent
architecture, and shows that each of those grounds leads to the same place.
That place is the execution boundary.

It is not a new idea. Reference monitors found it in 1972.80 Safety engineers found it in
physical systems.81 Financial markets found it in pre-trade risk.82 What is new is the
synthesis — the recognition that every discipline that has grappled with the problem of
governing consequential action has converged on the same architectural requirement,
expressed in different language, enforced through different mechanisms, applied in
different domains.
The execution boundary is where governance either happens or it does not.
The constraint exists whether or not you instrument it.
The window is open whether or not you place a kernel in it.
The question is not whether the execution boundary matters. It always has. The question is whether the systems we are building will be governed at that boundary — or
whether we will discover, through the accumulation of consequential failures in ungoverned autonomous systems, that the window was always there and we chose not to
use it.
That choice is still available.
It will not remain available indefinitely.
The machine-speed economy does not wait for governance to find its footing. It runs.
And at the moment a consequence-bearing action crosses the execution boundary without a governance determination having been made, the window closes.
What follows is not governed.
It is merely what happened.

End of manuscript — Version 2.0
Execution-Boundary Governance: A Runtime Control Model for Autonomous Systems
32 chapters. 8 parts. One constraint.
Jonathan M. Watson
Independent Researcher
jonmwatson@gmail.com
July 1, 2026

       Anderson, J.P. (1972). Computer Security Technology Planning Study. ESD-TR-73-51. Electronic Systems
Division, Air Force Systems Command, Hanscom AFB, Massachusetts.
       IEC 61508 (2010). Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems. International Electrotechnical Commission, Geneva; ISO 26262 (2018). Road Vehicles — Functional
Safety. International Organization for Standardization, Geneva.
       FINRA Rule 15c3-5 (2010). Market Access Rule. Financial Industry Regulatory Authority; SEC Release
No. 34-63241 (2010). Risk Management Controls for Brokers or Dealers with Market Access. U.S. Securities and
Exchange Commission.

Glossary of Terms
Terms are defined as used in this paper. Where a term has an established prior meaning in another
discipline, the relationship to that prior meaning is noted.
Action latency The time available between the moment an autonomous system proposes an action and the moment that action commits to consequence. Action latency
defines the interval within which any governance determination must be reached if it is
to influence the outcome. As autonomous systems mature, action latency shrinks. See
also: governance latency, latency condition.
Admissibility The property of a proposed action that permits it to cross the execution boundary and execute. An action is admissible when it satisfies the compiled constraints evaluated by the Executable Governance Kernel — when authority is present,
policy conditions are met, and no constraint is violated. Admissibility is determined
before execution, not inferred from outcomes afterward.
Admissibility metrics Measurable signals derivable from EGK output that describe the
governance health of an autonomous system over time. The five core metrics proposed
in this paper are: denial rate, constraint violation frequency, override rate, policy compliance score, and governance availability. Admissibility metrics are natural outputs of
the EGK architecture — not a separate instrumentation layer imposed on top of it.
Authority migration The structural dynamic by which effective governance authority
relocates from designated governance bodies to whoever controls the execution surface, when governance frameworks cannot operate at the speed required to reach that
surface. Authority migration is not deliberate. It occurs because decisions must be
made and actions permitted or denied regardless of whether the designated governance mechanism can operate in time. Authority migration is a present condition in
most autonomous system deployments, not a future risk.
Boundary discovery The operational methodology by which an organization identifies the precise points within an autonomous system or agentic workflow at which reversibility ends and consequence begins. Boundary discovery proceeds in four steps:
action enumeration, reversibility assessment, commit surface identification, and authority mapping. Boundary discovery is a precondition for governing the execution boundary — the boundary exists whether or not it is mapped.
Commit surface The specific operation within a multi-step workflow at which the point
of no return is crossed — the precise step whose effects propagate forward regardless
of what the system does afterward. The commit surface is the location of the execution
boundary within a given workflow. Identifying the commit surface precisely is the
difference between placing governance where it is needed and placing it where it is
convenient.
Complete mediation The first required property of the Executable Governance Kernel.
Within its defined consequence scope, the EGK must be invoked for every action that
crosses the governed execution boundary. A governance mechanism that can be bypassed within its defined scope — even occasionally — is not a governance mechanism.
Complete mediation applies within the consequence scope established by boundary

discovery, not as a requirement to instrument every agent action regardless of consequence class.
Consequence classification The three-tier taxonomy proposed in this paper for calibrating governance intensity at the execution boundary. Tier one: low consequence —
reversible, local, limited human impact. Tier two: high consequence — irreversible, externally visible, regulated, or materially impactful. Tier three: sovereign consequence
— systemic, cross-jurisdictional, infrastructure-level, or capable of cascading effects at
population scale. Consequence classification is the basis for consequence-based regulation: governing what systems do rather than what systems are.
Controlling governance Governance that prevents inadmissible outcomes before
they occur by evaluating admissibility before commitment. Controlling governance is
causally upstream of the action it governs. Distinguished from narrative governance,
which documents outcomes after they occur. The execution boundary is the only
point in an autonomous system at which controlling governance remains physically
possible.
Determinism The second required property of the Executable Governance Kernel.
Given identical inputs — proposed action, authority context, compiled policy, environmental state — the EGK must produce identical outputs every time. Determinism
is not a limitation on sophistication. It is the property that makes the EGK’s output
trustworthy, its behavior auditable, and its evidence legally meaningful. A probabilistic governance mechanism at the execution boundary is not a governance mechanism.
It is a risk assessment.
Evidentiary locality The requirement that evidence artifacts produced at the execution
boundary are generated independently of the system whose actions the kernel governs
— close enough to witness execution, separated enough to prove it. Evidentiary locality
is distinct from technical locality. An architecture may satisfy technical locality while
failing evidentiary locality if the kernel shares physical infrastructure with the governed
system. See also: technical locality, underwriting locality, regulatory locality.
Executable Governance Kernel (EGK) The minimal deterministic governance surface
operating immediately prior to autonomous execution. The EGK is defined by five
required properties: complete mediation within defined consequence scope, determinism, latency compatibility, tamper resistance, and evidence generation. The EGK is
not defined by its implementation — implementations will vary by system, domain,
latency budget, and consequence class. Any mechanism satisfying these five properties constitutes an EGK. Any mechanism claiming to govern at the execution boundary
must satisfy them.
Execution boundary The final deterministic control point immediately preceding an
autonomous action — the threshold at which authority, policy, constraints, and admissibility can still be evaluated before execution occurs. Once crossed, the action is no
longer proposed. It is a fact. The execution boundary is singular, deterministic, and
consequential. It is the governance surface: the only point in an autonomous system
where a determination can still causally influence whether an action occurs. Prior art

implements the concept under different names in specific domains — reference monitor in cybersecurity, safety kernel in safety engineering, pre-trade risk check in financial
markets.
Execution credentials Standardized, interoperable artifacts derived from EGK determinations that allow governance presence to be verified by a receiving system without
replicating the governance evaluation. Execution credentials are the governance equivalent of payment rail settlement primitives — proof that an action was evaluated, that a
specific policy applied, and that execution was permitted or denied. Execution credential standards do not yet exist. Their emergence is a named direction for future research.
Previously referred to in some literature as governance tokens — a term avoided in this
paper due to associations with cryptocurrency infrastructure.
Execution evidence A contemporaneous, tamper-evident record produced by the EGK
at the moment of each governance determination — before the action commits. Execution evidence captures the proposed action, the policy context applied, the authority credentials evaluated, the determination reached, and the timestamp at which the
determination preceded the action. Execution evidence is categorically distinct from
audit logs, which are produced after actions commit and can only demonstrate consistency with governance, not prove its presence. Execution evidence is the foundational
artifact for liability attribution, insurance underwriting, and regulatory compliance in
autonomous systems.
Governance availability The fifth admissibility metric proposed in this paper. The
proportion of time during which the EGK was operational and capable of evaluating
actions at the execution boundary. Governance availability is the precondition for all
other admissibility metrics — an EGK that is offline when a consequential action executes is an EGK that did not govern that action. Governance availability is both an
operational metric and a coverage condition for underwriting purposes.
Governance compilation The transformation of interpretive governance — humanreadable, contextual, ambiguous policy — into executable governance: machineenforceable constraints that can be evaluated deterministically within a bounded time
at the execution boundary. Governance compilation is formally analogous to software
compilation: natural language policy is source code; the compiled constraint set
loaded into the EGK is the executable binary. Interpretation must precede compilation.
Compilation must precede enforcement. The execution boundary is not a place for
deliberation.
Governance latency The time required to evaluate whether a proposed action is admissible — to check authority, apply policy, assess constraints, and reach a determination.
Governance latency is one of the two intervals that define the latency condition. When
governance latency exceeds action latency, governance cannot influence outcomes before they commit. See also: action latency, latency condition.
Governance locality The requirement that the EGK operates physically proximate to
the execution surface it governs. Governance locality is a derived constraint from the
latency condition and the physics of information propagation: governance executed

at suﬀicient distance from the execution surface cannot satisfy the latency condition
regardless of software performance. Governance locality is not an architectural preference. It is a physical necessity for systems operating within tight action latency envelopes.
Human latency subsidy The unearned latency budget that governance mechanisms
have historically borrowed from the human pause between intention and action — the
click, the confirmation, the review interval that provided time for fraud detection, policy evaluation, and compliance checks to complete. Digital governance systems completed in time not because they were fast, but because humans were slow. Autonomous
systems cancel the human latency subsidy by removing the human pause entirely.
Interpretive governance The dominant mode of human institutional governance:
human-readable, contextually rich, deliberately flexible, and latency-tolerant by design. Interpretive governance handles ambiguity through judgment — the application
of accumulated expertise and contextual reasoning to produce determinations that are
defensible even when not perfectly predictable. Interpretive governance is native to
the human time domain. It becomes structurally incompatible when placed inside a
machine-speed execution path — not because it is wrong, but because the deliberative
process it requires cannot complete within the available interval. In a machine-speed
system, interpretive governance moves upstream of the execution boundary, where
it performs governance compilation. At the boundary itself, only enforcement is
possible.
Latency condition The formal condition governing whether governance is controlling
or observational: governance latency must be less than action latency. When this condition holds, governance can influence outcomes before they commit. When this condition fails, governance can only observe and document outcomes that have already
occurred. The latency condition is binary — there is no partial credit for almost completing in time. It is the foundational constraint from which the paper’s remaining arguments derive.
Minimal Surface Principle The architectural principle that the closer governance
moves to the execution boundary, the smaller the governance mechanism must
become. Complexity at the execution boundary is not safety — it is risk: additional
latency, additional failure modes, additional probabilistic variance, additional attack
surface. The EGK must be the smallest mechanism capable of making an admissibility
determination before the action commits. Smallness at the boundary is not a limitation.
It is proof that interpretation has been completed upstream, before enforcement begins.
Narrative governance Governance that documents outcomes after they occur — producing logs, audit trails, explainability reports, and compliance records. Narrative governance has genuine value for accountability, learning, and legal proceedings. But it
is not controlling governance. A system that logs every transaction in perfect detail
has not governed those transactions. It has documented them. Most current AI governance is narrative. This is not a deficiency of intent. It is a consequence of the latency
condition: when governance latency exceeds action latency, narrative is what remains.

Regulatory locality The requirement that a governance deployment satisfies the
jurisdiction-specific requirements that apply to the consequence class being governed
— HIPAA for medical records, PCI-DSS for payment data, NERC CIP for energy
infrastructure. Regulatory locality is distinct from technical locality, evidentiary
locality, and underwriting locality. An architecture may satisfy all three of the other
locality requirements while failing regulatory locality if the deployment environment
does not meet the specific compliance standards of the governing regulatory regime.
Tamper resistance The fourth required property of the Executable Governance Kernel.
The EGK must be structurally isolated from the agent whose actions it governs. An
agent that can modify its own governance kernel has no governance kernel. Tamper
resistance in this context means structural isolation from the governed agent — not a
claim of absolute cryptographic security. The separation between the governed system and the governing mechanism is the condition that makes governance meaningful
rather than performative.
Technical locality The requirement that the governance check is physically close
enough to the execution surface to satisfy the latency condition. Technical locality is
necessary but not suﬀicient for governed deployment. An architecture that satisfies
technical locality may still fail evidentiary locality, underwriting locality, or regulatory
locality. See also: evidentiary locality, underwriting locality, regulatory locality,
governance locality.
Time-domain mismatch The structural incompatibility between human governance
and machine-speed execution arising from their operation in fundamentally different
time domains. A time domain is not simply a rate of operation — it is the complete set
of assumptions a system makes about the interval between decision and consequence.
Human governance was built for a time domain defined by biological constraints. Autonomous execution operates in a time domain defined by computational and network
constraints. Time-domain mismatch is not a performance problem solvable by making
human governance faster. It is a domain compatibility problem requiring translation —
the conversion of governance from interpretive form native to the human time domain
into executable form capable of operating in the machine time domain.
Underwriting locality The requirement that a governance deployment satisfies the
physical security, administrative separation, key management, audit posture, and resilience standards that an underwriter requires to treat governance presence as a covered control. Underwriting locality is distinct from technical locality. A deployment
may be technically local enough to satisfy the latency condition while being physically
unsecured, administratively co-mingled with the governed system, or insuﬀiciently auditable to constitute an insurable control in the eyes of an underwriter.
End of Glossary
Working Bibliography — Version 2.0
Execution-Boundary Governance: A Runtime Control Model for Autonomous Systems

A — Foundational Security and Safety Architecture Anderson, J.P. (1972). Computer Security Technology Planning Study. ESD-TR-73-51. Electronic Systems Division,
Air Force Systems Command, Hanscom AFB, Massachusetts.
Schneider, F.B. (2000). Enforceable security policies. ACM Transactions on Information
and System Security, 3(1), 30–50.
Liu, C.L. & Layland, J.W. (1973). Scheduling algorithms for multiprogramming in a
hard-real-time environment. Journal of the ACM, 20(1), 46–61.

B — Safety Engineering Standards IEC 61508 (2010). Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems. International Electrotechnical Commission, Geneva.
ISO 26262 (2018). Road Vehicles — Functional Safety. International Organization for
Standardization, Geneva.
SAE J3061 (2016). Cybersecurity Guidebook for Cyber-Physical Vehicle Systems. SAE International.

C — AI Governance Frameworks National Institute of Standards and Technology
(2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1.
U.S. Department of Commerce.
ISO/IEC 42001:2023. Information Technology — Artificial Intelligence — Management System. International Organization for Standardization.
European Parliament & Council of the European Union (2024). Regulation (EU)
2024/1689 on Artificial Intelligence (EU AI Act). Oﬀicial Journal of the European Union.
Government of Canada (2022). Bill C-27 — Artificial Intelligence and Data Act (AIDA).
44th Parliament, 1st Session.
UK AI Safety Institute (2024). AI Safety Framework. Department for Science, Innovation
and Technology, United Kingdom.
Monetary Authority of Singapore (2023). Model AI Governance Framework (2nd ed., updated). MAS.
Australian Prudential Regulation Authority (2019). Prudential Practice Guide CPG 234:
Information Security. APRA.
Australian Government (2024). Voluntary AI Safety Standard. Department of Industry,
Science and Resources.
UAE AI Oﬀice (2024). UAE National AI Strategy 2031 — Regulatory Framework Documentation. Government of the United Arab Emirates.

D — Regulatory and Legal Sources        Administrative Procedure Act (1946). 5 U.S.C.
§§ 500–596.
California AB 316 (2025). Chaptered as amendment to California Civil Code. Effective
January 1, 2026. California Legislative Information.

FINRA Rule 15c3-5 (2010). Market Access Rule. Financial Industry Regulatory Authority.
SEC Release No. 34-63241 (2010). Risk Management Controls for Brokers or Dealers with
Market Access. U.S. Securities and Exchange Commission.
SEC & CFTC (2010). Findings Regarding the Market Events of May 6, 2010 (Flash Crash
Report). U.S. Securities and Exchange Commission and Commodity Futures Trading
Commission.
SEC (2010). Concept Release on Equity Market Structure. Release No. 34-61358. U.S. Securities and Exchange Commission.
Restatement (Third) of Torts: Products Liability § 1 (1998). American Law Institute.
Prosser, W.L. & Keeton, W.P. (1984). The Law of Torts (5th ed.). West Publishing. § 41.
Cruzan v. Director, Missouri Department of Health, 497 U.S. 261 (1990). U.S. Supreme
Court.
Bloor v. Falstaff Brewing Corp., 601 F.2d 609 (2d Cir. 1979).
45 CFR § 164.312(b). HIPAA Security Rule — Audit Control Requirements. U.S. Department of Health and Human Services.
45 CFR §§ 164.400–414. HIPAA Breach Notification Rule. U.S. Department of Health
and Human Services.
PCI DSS v4.0 (2022). Payment Card Industry Data Security Standard. PCI Security Standards Council.
NERC CIP-007-6 (2022). Systems Security Management. North American Electric Reliability Corporation.

E — Financial Market and Economic Sources Uniform Commercial Code § 2-306
(1952, as amended). American Law Institute and Uniform Law Commission.
Kirilenko, A., Kyle, A.S., Samadi, M., & Tuzun, T. (2017). The Flash Crash: Highfrequency trading in an electronic market. Journal of Finance, 72(3), 967–998.
Alchian, A.A. (1950). Uncertainty, evolution, and economic theory. Journal of Political
Economy, 58(3), 211–221.
Chandler, A.D. (1977). The Visible Hand: The Managerial Revolution in American Business.
Harvard University Press.

F — Insurance and Underwriting Sources Casualty Actuarial Society (1988). Statement of Principles Regarding Property and Casualty Insurance Ratemaking. CAS.
NAIC (current). Risk-Based Capital Model Laws and Regulations. National Association of
Insurance Commissioners.
NFPA 25 (2023). Standard for the Inspection, Testing, and Maintenance of Water-Based Fire
Protection Systems. National Fire Protection Association.

IMO SOLAS Chapter III (2020 consolidated edition). Life-Saving Appliances and Arrangements. International Maritime Organization.
Resultsense/Financial Times (2026). London insurers cap cyber payouts as AI ‘LLMjacking’ losses mount. April 22, 2026. resultsense.com/news/2026-04-22-insurers-capcyber-llmjacking-ai-payouts [QBE sublimit: £188,000 on £3.8M policy; Beazley: same
source.]
Insurance Services Oﬀice / Verisk (2026). Generative Artificial Intelligence Exclusion Endorsements. Effective January 1, 2026. Forms: CG 40 47, CG 40 48, CG 35 08.
Cowbell Cyber Inc. (2026). Cowbell Prime One Cyber Insurance. U.S. Launch April 21,
2026. Underwritten by Chaucer Insurance Company. cowbell.insure/prime-one
Munich Reinsurance Company (2026). aiSure™: Performance Guarantee Insurance for
Artificial Intelligence Solutions. Munich Re Insure AI Program. munichre.com/insure-ai

G — Computer Science and Agent Architecture Yao, S., Zhao, J., Yu, D., Du, N.,
Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting
in language models. International Conference on Learning Representations (ICLR 2023).
Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., … & Wen, J.R. (2024). A
survey on large language model based autonomous agents. Frontiers of Computer Science,
18(6).
Aho, A.V., Lam, M.S., Sethi, R., & Ullman, J.D. (2006). Compilers: Principles, Techniques,
and Tools (2nd ed.). Addison-Wesley.
Prose2Policy (P2P): A Practical LLM Pipeline for Translating Natural-Language Access
Policies into Executable Rego. arXiv:2603.15799.
Executable Governance for AI: Translating Policies into Rules Using LLMs. arXiv:2512.04408.
Qin, X., Luan, S., See, J., Boukhers, Z., Yang, C., & Li, Z. (2026). Harnessing Embodied
Agents: Runtime Governance for Policy-Constrained Execution. arXiv:2604.07833 (v4,
June 10, 2026).
Swearingen, K. (2026). Execution Governance: A Control-Plane Architecture for Mediating Actions of Adaptive Systems. SSRN 6441961. DOI: 10.2139/ssrn.6441961.
Mazzocchetti, A.M. (2026). Cryptographic Runtime Governance for Autonomous AI
Systems: The Aegis Architecture for Verifiable Policy Enforcement. arXiv:2603.16938.
Zenodo DOI: 10.5281/zenodo.19027190.
Tallam, K. (2026). Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure. arXiv:2605.05440.

H — Zero Trust and Security Architecture Kindervag, J. (2010). No More Chewy Centers: Introducing the Zero Trust Model of Information Security. Forrester Research.
Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). Zero Trust Architecture. NIST
Special Publication 800-207. National Institute of Standards and Technology.

I — Infrastructure and Edge Compute ETSI GS MEC 001 (2022). Multi-access Edge
Computing (MEC): Terminology. European Telecommunications Standards Institute.
ETSI GS MEC 003 (2022). Multi-access Edge Computing (MEC): Framework and Reference
Architecture. European Telecommunications Standards Institute.
3GPP Release 17 (2022). 5G System Specifications. 3rd Generation Partnership Project.
Agrawal, G.P. (2019). Fiber-Optic Communication Systems (6th ed.). Wiley.
TeleGeography (2024).           Submarine Cable Map.   TeleGeography Inc. submarinecablemap.com
Cloudflare (2024). Global Network Latency Report. Cloudflare Inc. cloudflare.com/radar
Apple Inc. (2023). A17 Pro Chip — Neural Engine Specifications. Apple Developer Documentation.
Qualcomm Technologies (2023). Snapdragon 8 Gen 3 Mobile Platform — AI Performance
Specifications. Qualcomm Technologies Inc.
SuperMicro (2024). Edge Computing Server Product Line. Super Micro Computer Inc.
Dell Technologies (2023). Edge Computing Solutions White Paper. Dell Technologies Inc.
HPE (2023). Edgeline Converged Edge Systems Portfolio. Hewlett Packard Enterprise.
Cisco Systems Engineering Team (2026). BRKSPG-1180: Advanced Network Architectures
for LLM Ingestion. Cisco Live EMEA, February 2026.
LangChain (2026). SmithDB Inverted Index Performance Benchmarks. LangChain Platform, May 13, 2026.

J — Physics Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. Annalen der
Physik, 17, 891–921.
NIST (2018). CODATA Internationally Recommended 2018 Values of the Fundamental Physical Constants. National Institute of Standards and Technology. c = 299,792,458 m/s.

K — Cognitive Science and Human Factors Card, S.K., Moran, T.P., & Newell, A.
(1983). The Psychology of Human-Computer Interaction. Lawrence Erlbaum Associates.
Donders, F.C. (1868). Over de snelheid van psychische processen. Onderzoekingen
gedaan in het Physiologisch Laboratorium der Utrechtsche Hoogeschool. English translation:
On the speed of mental processes (1969), Acta Psychologica, 30, 412–431.

L — Institutional and Economic Theory Simon, H.A. (1947). Administrative Behavior:
A Study of Decision-Making Processes in Administrative Organizations. Macmillan.
North, D.C. (1990). Institutions, Institutional Change and Economic Performance. Cambridge University Press.
Fuller, L.L. (1964). The Morality of Law. Yale University Press.

Stigler, G.J. (1971). The theory of economic regulation. Bell Journal of Economics and
Management Science, 2(1), 3–21.
Lessig, L. (1999). Code and Other Laws of Cyberspace. Basic Books.

M — Medical and Healthcare Sources AMA Council on Ethical and Judicial Affairs
(2016). AMA Code of Medical Ethics, Opinion 1.1.1: Patient-Physician Relationships. American Medical Association.
Basel Committee on Banking Supervision (2010). Basel III: A Global Regulatory Framework for More Resilient Banks and Banking Systems. Bank for International Settlements.
Federal Reserve (2011). SR Letter 12-7: Supervisory Guidance on Model Risk Management.
Board of Governors of the Federal Reserve System.

N — Industry Reports and Surveys Federal Reserve (2022). Federal Reserve Payments
Study. Board of Governors of the Federal Reserve System.
Amazon.com Inc. (1999). United States Patent No. 5,960,411 — Method and System for Placing a Purchase Order via a Communications Network. United States Patent and Trademark
Oﬀice.
Varma, S. (2026). Gartner Says Applying Uniform Governance Across AI Agents
Will Lead to Enterprise AI Agent Failure. Gartner Newsroom, May 26, 2026.
gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniformgovernance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure
ISACA (2026). AI Use Accelerates, While Governance and ROI Lag. ISACA AI Pulse Poll,
May 5, 2026. isaca.org/resources/ai-pulse-poll
Lipkin, S. & Willis Research Team (2026). Risk & Resilience Review: AI in Action — The
Road to Responsible Adoption. Willis Towers Watson, May 27, 2026. wtwco.com/engb/insights/2026/05/risk-and-resilience-review-ai-in-action-the-road-to-responsibleadoption

O — Insurance and Actuarial Research (2026) Hoshino, T. (2026). The Price of OverDelegation: Stackelberg Liability Design for Agentic AI Handoffs. ICML 2026 Workshop (NExT-Game), June 6, 2026. openreview.net/forum?id=oR9NEviIsX
Chen, H-H. (2026). Insuring Every Action: An Authority Frontier Framework for
Runtime Actuarial Control of Autonomous AI Agents. arXiv:2605.25632. Companion:
SSRN 6761960.
Adebayo, T., Apalowo, O., & Makanjuola, F. (2026). OMP Domain Profile: AI Liability Insurance Underwriting and Parametric Claims Evidence. IETF Network Working
Group. draft-veridom-omp-aiins-00, April 5, 2026.
End of Bibliography — Version 2.0. All citations resolved.
