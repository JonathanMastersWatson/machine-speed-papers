---
title: "Machine-Speed Economics"
subtitle: "How Evidence Becomes the Price Signal"
paper_number: 6
version: "0.2"
author: "Jonathan M. Watson"
date: "2026-10"
series: "The Machine Speed Papers"
canonical_pdf: "paper.pdf"
license: "CC-BY-4.0"
---

# Machine-Speed Economics

*How Evidence Becomes the Price Signal*

**Jonathan M. Watson** — The Machine Speed Papers, No. 6 — Version 0.2 — 2026-10

---

*Machine-readable text derived from the canonical PDF (`paper.pdf`). In case of any discrepancy, the PDF governs.*

## Abstract

An economy is buyers meeting sellers, prices moving, and obligations settling — with
enough reliability that strangers will trade. This paper describes that economy with the
humans removed from the middle of each transaction, and argues that what makes it
possible is not faster money but independently witnessed evidence.

The paper makes six claims.

First, the machine-speed economy requires nothing that does not already exist. Agents
carry a purse — bounded spending authority committable at the point of action — and
a mandate — preconstrained limits on what may be done, for whom, at what cost. Every
component maps to deployed technology. The assembly is connection, not invention.

Second, admissibility becomes the matching criterion. Today matching happens first
and compliance is checked afterward, usually by humans, usually too late. Where two
agents' constraint sets intersect, a trade is admissible; where they do not, no candidate
ever appears. There is no non-compliant transaction to prevent because it was never
matchable.

Third, once latency, uptime, jurisdiction, security posture and energy mix are attested
by parties with no position in the trade, those attestations become bid attributes. Price
discovery turns differences in the real world into differences in the number. The market
prices pickiness, which no human market can sustain, because no human holds the
whole vector.

Fourth, a receipt is not a payment. Execution, evidence, obligation, settlement and enforcement are five distinct functions, and collapsing any two destroys the unpaid state
— the economy's ability to say the service occurred, the obligation exists, the payment has not
cleared. An architecture that fires a payment per action has nothing to net.

Fifth, and this is the paper's candidate for what is new: a single evidence artifact does
three jobs at once. The receipt that proves a determination was legitimate is the IOU
the settlement layer nets and the input the valuation layer prices on. Governance control, settlement primitive, valuation denominator — one artifact, three functions, each
reinforcing the others. No prior literature appears to synthesize them.

Sixth, the thesis is falsifiable by a single measurement. Run the same market governed
and ungoverned and compare prices. If the spread is zero — if nobody will pay for
attested terms, deterministic admissibility and independent evidence — the thesis is
wrong. Not incomplete. Wrong.

Participation is voluntary throughout. No regulator mandates the gates; no treaty compels the witness. The enforcement is access.

Preliminaries

Vocabulary. This paper uses the terminology established across Papers 1–5: execution
boundary, Executable Governance Kernel (EGK), admissibility, independent witness,
policy compilation, Compiled Region, execution surface. It names no implementation
of any of them.

Naming. To avoid collision with the EGK, this paper does not use the abbreviation EKG
for the continuous economic trace described in Chapter 14. That trace is called the Pulse
throughout.

Prior papers in this series. All five are posted and publicly available.

  1. Watson, J. M. (2026). Execution-Boundary Governance: A Runtime > Control Model
     for Autonomous Systems. SSRN Working Paper No. > 7034678.

  2. Watson, J. M. (2026). Constitutional Compression: The Emergence of > Minimal Governance at Machine Speed. SSRN Working Paper No. > 7199200.

  3. Watson, J. M. (2026). Evidence Systems: Why Independent Witnesses > Emerge at
     Machine Speed. SSRN Working Paper No. 7207219.

  4. Watson, J. M. (2026). Upstream: Where Human-in-the-Loop Goes at > Machine Speed.
     SSRN Working Paper No. 7211100.

  5. Watson, J. M. (2026). The Execution Surface: Why Distributed > Compute Cannot Be
     Shared. SSRN Working Paper No. [pending].

Papers 1–5 established the components: the execution boundary and its kernel (1), the
compression of governance to that kernel (2), the independent witness (3), the relocation of human judgment upstream (4), and the distribution of the execution surface to
the edge (5). This paper shows the assembled machine running.

PART ONE — THE MACHINE

## Chapter 1 — What an Economy Is

An economy is not a collection of fast computers. An economy is buyers meeting sellers,
prices moving, and obligations settling — with enough reliability that strangers will
trade.

The machine-speed economy is that, with the humans removed from the middle of each
transaction. Software agents buy and sell from each other: tokens for compute, mandates for attested properties. Each agent carries its own purse — bounded spending
authority it can commit at the point of action — and its own mandate — preconstrained
limits on what it may do, for whom, and at what cost. Agents broadcast the terms they
require. Where two broadcasts intersect, a trade is admissible. Settlement follows in
fractions of a cent. All of it happens faster than any human can observe, let alone approve.

None of this is a metaphor. Read it again literally: an agent holds money it is allowed
to spend, rules about what it may buy, and a way to prove both to a stranger. That is all
an economy has ever required of its participants. The rest — the shouting on trading
floors, the signatures, the compliance departments — was the interface. The interface
is being replaced. The economy underneath stays.

It has always been the economy. Take a Florentine factor — a merchant's agent — in
England in the 1200s, buying wool for the looms of Flanders.1 In his saddlebag: a bill of
exchange drawn on his house in Florence — money he is allowed to spend. His master's
instructions — Cotswold wool, so many sacks, no more than such a price per sack. And
the bill itself, bearing his master's mark — the way to prove both to a stranger in a market
town who has never seen him before.

The agent, the purse, the mandate, the proof.

What makes this an economy rather than automation is the same thing that has always
made it one: price discovery under constraint. Prices move because properties are
attested. Trades clear because both sides proved admissibility before they met. Obligations settle because the receipt is separate from the payment. Take any one of those
away, and you have software. Keep all three, and you have a market.
      On the Italian merchant companies' use of factors, standing instructions and bills of exchange in the English wool trade, see de Roover, R. (1963). The Rise and Decline of the Medici
Bank, 1397–1494. Harvard University Press; and Lopez, R. S. (1976). The Commercial Revolution
of the Middle Ages, 950–1350. Cambridge University Press. The three-part structure — delegated
spending authority, written constraints on its exercise, and a mark by which a stranger could
verify both — is the standard form of the period and is described here as structure rather than
as a specific documented transaction.

## Chapter 2 — The Configuration

Here are the parts, how they fit, and — the discipline this paper holds throughout —
what each part already is. Nothing in this section is invented. If any component required
a new technology, the design would be wrong, and the paper would say so.

The agent. Software acting for a principal — a person, a company, a function. It proposes actions, carries a purse, and answers for what it commits. This exists: agent frameworks already transact as tools inside orchestration stacks, calling each other's outputs
as inputs, operating without human initiation at the individual transaction level.2

The purse. Bounded spending authority the agent carries to the boundary and settles
against at the point of commit — an amount, an expiry, a scope. Not a bank account
with a human watching it; an instrument the agent itself can spend from, inside limits
set upstream. This exists: prepaid caps, hardware-backed wallets, per-request payment
rails. Coinbase's x402 — per-request HTTP payments, live — is the shape of it.3

Why purse? Because the word is doing work. A purse is carried on the person, and it
holds only what was put into it — you cannot spend what isn't in it. The Hudson's Bay
Company ran a continent on this shape: London held the capital, the vault; each fort
was outfitted for the season, the chest; and the men who went inland carried what they
were authorized to deal, the purse — bounded, personal, accounted for on return.4 The
frontier ran on trade goods and made-beaver accounting, not coin; the purse names the
shape, not the contents. The agent's purse is the same instrument four centuries later:
spending authority carried to the boundary, bounded before it moves, settled when it
returns.

The mandate. The preconstrained limits: whose authority the agent carries, the identity of its principal, what it may do, for whom, at what cost, with what receipt capability.
       Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. International Conference on Learning Representations (ICLR 2023). Wang, L., Ma, C., Feng, X., et al. (2024). A survey on large language model
based autonomous agents. Frontiers of Computer Science, 18(6).
      ‡ Coinbase. x402: an open payments protocol for HTTP, reviving HTTP status code 402
Payment Required for per-request machine-to-machine settlement. Specification and reference
implementation published 2025. Cited as an existence proof of per-request payment rails, not
as an endorsement of any implementation. Confirmed: launched by the Coinbase Developer
Platform (2025, Apache-2.0) and live in production on Base mainnet. The default facilitator
adds no surcharge; execution cost is Layer-2 gas only (typically <$0.001–$0.005 per settlement in USDC), with ~1–2 second finality. Cited as an existence proof of per-request payment rails, not as an endorsement of any implementation. See the x402 protocol specification
(x402.gitbook.io) and CDP documentation.
       Hudson's Bay Company Archives, Provincial Archives of Manitoba.
   The Company's three-tier outfitting structure — London committee capital, annual post outfits, and individually accounted trading goods carried inland — is documented across the Company's account books and standing instructions to Chief Factors. On made-beaver as unit of
account, see Ray, A. J., & Freeman, D. (1978). ”Give Us Good Measure”: An Economic Analysis
of Relations between the Indians and the Hudson's Bay Company before 1763. University of Toronto
Press.

Declared before anything moves, signed, versioned. This exists: signed policy artifacts,
capability tokens bound to a caller and a window, versioned terms references.5 In deployment it looks like an intent envelope — caller, purpose, use class, maximum cost,
time-to-live, context budget — submitted before the action it would authorize.

The EGK. The executable governance kernel: a deterministic gate that evaluates a proposed action against compiled constraints and returns ALLOW or DENY with a reason
code, before the action commits. It does not reason. It does not learn. It checks. This
exists: policy engines evaluating declarative rules in microseconds, eBPF filters in the
Linux kernel, hardware security modules signing only what policy permits, trusted execution environments attesting what ran.6 The contract it satisfies is strict — canonical
input, pure check functions, no clock reads, no network calls inside evaluation, enumerated reason codes — because anything looser cannot produce evidence two strangers
will both trust.

Broadcast terms. Each agent publishes the constraints it requires of a counterparty —
what it will buy, under what conditions, at what limits. This exists in skeleton form: service
descriptors, capability advertisements, API contracts. The new part is not the broadcast.
It is that the broadcast is provable: the terms resolve to attestations from a party with no
position, and to a mandate version both sides can name.

Matching. Agent 1's constraint set against Agent 2's, in both directions. A trade is admissible only where the two sets intersect. Here is the inversion the whole paper turns
on: today matching happens first, and compliance is checked afterward — usually
by humans, usually too late. Here admissibility is the matching criterion. A trade
that would fail governance never appears as a candidate. There is no non-compliant
transaction to prevent, because it was never matchable.

The witness. An independent mechanism that captures each determination the moment it occurs — captured, chained, externally timestamped, administratively separate
from every party it observes, disclosable without any party's cooperation. It does not
govern. It cannot permit, deny, or delay. It records. This exists: hash-chained logs,
Merkle trees, transparency logs. Certificate Transparency — every public TLS certificate logged in public, browser-enforced, no legislation — is the working proof that independent witnessing scales.7
      On capability tokens bound to a caller and a validity window, see the macaroon construction in Birgisson, A., Politz, J. G., Erlingsson, Ú., Taly, A., Vrable, M., & Lentczner, M. (2014).
Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud.
Network and Distributed System Security Symposium (NDSS 2014).
      Open Policy Agent and the Rego policy language, CNCF graduated project. Amazon Web
Services, Cedar policy language, open source. † Published per-request pricing and evaluation latency for managed authorization services are cited in Chapter 10 and require verification against
primary vendor documentation.
      Laurie, B., Langley, A., & Kasper, E. (2013). Certificate Transparency. RFC 6962. Internet
Engineering Task Force. Superseded by Laurie, B., Messeri, E., & Stradling, R. (2021). Certificate
Transparency Version 2.0. RFC 9162. Browser enforcement — rather than legislation — drove
ecosystem adoption; Chrome began requiring CT logging for certificates issued from 30 April

Settlement. The transfer of value, kept strictly separate from the determination and
the evidence. The obligation is created at ALLOW; the transfer happens on its own
rails, on its own schedule, netted per obligor, obligee, and currency. Chapter 5 treats
the obligation as the load-bearing layer it is. The obligation layer itself never touches
money: the rails move the value and report back as witnessed events. And authorized is
not happened. This exists: sub-cent settlement rails operating off the hot path,8 stablecoins
— and, as the institutional precedent, the card networks themselves, which operate with
authorization, clearing, settlement, and dispute as distinct functions. The separation of
obligation from transfer is a solved, century-old design, not a proposal.9

Version-binding, throughout. The mandate version in force at the instant of the trade.
The policy version the kernel evaluated. The attestation version the counterparty relied
on. Version-binding appears everywhere in this architecture because at machine speed
”the current terms” is a meaningless phrase unless the terms carry their version with
them. This exists: content hashing, semantic versioning, certificate epochs.

The handshake, then, requires three distinct things: each side proves it holds the mandate it claims, without revealing its full terms; each side's claimed properties resolve to
attestations from a disinterested party; and both sides agree the mandate versions in
force at that instant. Miss any one, and there is no trade — not a blocked trade, not a
flagged trade. No trade. The candidate never existed.

One honest boundary before the paper proceeds: bilateral agent-to-agent matching at
machine speed is the mechanism this configuration points at. The deployments that
exist today are unilateral — one gate, one principal, one boundary. The paper does not
pretend otherwise. What it argues is that every deployed part is already in place, and
the assembly is a matter of connection, not invention.

2018.
     ‡ XRP Ledger consensus finality and per-transaction cost. Confirmed against XRPL Foundation primary documentation (xrpl.org): deterministic finality in 3–5 seconds per ledger
close (median ~3.6s) via UNL consensus, with no probabilistic reorganization; reference
transaction cost 10 drops of XRP ($0.000010 XRP, on the order of $0.00001–$0.00003) — thousandths of a cent. Cited as one instance of a class of sub-cent settlement rails; the architecture
is rail-agnostic and the paper endorses no implementation.
      Committee on Payment and Settlement Systems and Technical Committee of IOSCO (2012).
Principles for Financial Market Infrastructures. Bank for International Settlements. The separation
of authorization, clearing, settlement and dispute as distinct functional layers is foundational to
the PFMI framework and to card network operating rules.

## Interlude — The Certificate

The certificate arrives in Lagos on a Tuesday afternoon. Amara has been studying structural load analysis for eleven weeks. She has just finished the last assessment. She closes
the laptop and goes to make dinner.

Nothing about the afternoon feels like a machine-speed economy. That is the point.

Her submission — a bridge design, forty pages of calculation, a failure analysis — is
picked up by an assessing agent. The agent reconstructs her reasoning, checks her load
paths against physical constraints, finds the two places she rounded early and the one
place she caught an error the reference solution does not. Four seconds. It is not the
interesting part.

The interesting part is that the assessing agent issues nothing. It proposes. This work
meets the standard, at this level, against this rubric, and I am prepared to say so. The
proposal goes to a gate it does not control and cannot bypass.

The gate runs on the assessment appliance in the exam center, not in the accreditor's data
center two countries away, because a determination that depends on a network round
trip is a determination that can be delayed, and a delayed determination is the first thing
dropped under load. It checks: is this agent authorized to assess this subject at this level;
is the rubric version it applied the one in force today or one that expired last month;
does the identity chain hold from submission to this instant; is there any condition — a
jurisdiction, a sanction, a lapsed accreditation — that makes issuing inadmissible right
now. ALLOW, with a receipt. Or DENY, with a reason code.

ALLOW.

In the same instant, in a system with a position in none of it — not the institution, not
the platform, not Amara — the determination is captured. Not the grade. The act:
this agent, holding this authority, applied rubric version 7.1, to this submission, at this
moment, and the answer was aﬀirmative. Written once, chained, and not revisable by
anyone who benefits from revising it, including the people who built the system that
produced it.

Nobody reads that record today. That is not what it is for.

Three obligations form at the same instant. The accrediting body is owed for maintaining the standard. The assessment provider is owed for the work performed. The witness
is owed a fraction of a cent for having been present. None of these are payments. They
are amounts owed, in a state that says: this occurred, this is due, nothing has moved.

Value moves that night, netted, when moving it is cheap. Amara never knows.

Fourteen months later, a firm in Rotterdam is hiring. An engineer on the desk has never
heard of the institution that issued the certificate and has no reason to trust it.

He does not need to. He is not asking whether the institution is honest — an unanswerable question. He is asking a narrower one: on that Tuesday, was the assessing agent
authorized, was the rubric current, was the determination made before the credential
issued rather than reconstructed afterward, and could anyone with an interest in the
answer have changed the record?

It resolves in under a second. He does not read it. He sees that it resolves, and moves
to the next candidate.

Amara is hired six weeks later. She never learns any of this happened, and she wouldn't
find it interesting even if she did.

Now notice what the credential required. It was trusted by a party who did not trust
the issuer — which is the whole trick, and the rest of this paper is an explanation of
it. It worked because four things were true at once, and each is a physical or economic
condition rather than a policy preference.

The determination was made before the credential was issued, because a credential
validated afterward has already been relied on, and reliance does not reverse.

It was made by something that was not the assessing agent, because a system that
authorizes its own output provides no coverage against the failure it exists to catch.

It happened where the action was committed, because there was no interval in which
to consult anything further away.

And the record came from a party with nothing at stake, because a fact asserted by an
interested party is not evidence, however permanently it is stored.

Remove any one and the engineer in Rotterdam has to trust an institution in Lagos.
Which he will not do. That means Amara doesn't get hired, the credential is worth
nothing outside the country that issued it, and the eleven weeks were an expensive
hobby.

That is the situation today.

PART TWO — THE PRICE

## Chapter 3 — Price Discovery

Once latency, uptime, security posture, jurisdiction, ESG, and everything else that moves
price are attested — each by a party with no position in the trade — those attestations
become bid attributes. A buyer doesn't just ask for compute. It asks for compute with
an attested latency band, an attested jurisdiction, an attested posture, at or under a price,
within a mandate. A seller doesn't just offer tokens. It offers tokens with those same
properties attached and proven.

Then the auction runs. Each agent evaluates candidate counterparties against its mandate and returns a bid — not one number, but a vector: price per unit, attested latency,
attested jurisdiction, attested posture, and every other attribute its principal cares about.
The match clears where the constraint sets intersect, and the vector is best. Two trades
for the same nominal good can clear at different prices because the attested properties
differ. That is price discovery doing exactly what price discovery is supposed to do:
turning differences in the real world into differences in the number.10

This produces a phenomenon no human market can sustain, because humans can't hold
the whole vector in their heads: the market prices pickiness. An agent evaluates two
thousand sellers across price, attested latency band, attested jurisdiction, attested energy mix, attested security posture, and attested uptime history — and finds seller number 1,437: eight percent lower latency, two percent higher price, a jurisdiction that fits
the mandate exactly. No human runs that comparison. What the agent is really discovering is the price of each attribute separately: the price of ten milliseconds, the price of
a jurisdiction, the price of a cleaner record. Pickiness stops being a vibe and becomes a
number.

Pass-rate transparency — which mandates clear which gates, at what cost, how often
— lets both sides tune. A seller learns that relaxing a latency band from 50ms to 80ms
clears three times the volume at a two-percent discount. A buyer learns that requiring
a specific jurisdiction costs a seven-percent premium and clears half the time. Neither
side is guessing anymore. The trade-off between terms and clearance is visible, priced,
and adjustable. Openness itself becomes a priced variable: you cannot advertise open
terms and enforce strict ones, because the attestations are public and the witness keeps
the record.
    On the function of price in aggregating dispersed information, see Hayek, F. A. (1945).
The Use of Knowledge in Society. American Economic Review, 35(4), 519–530. The claim here is
narrower than Hayek's: not that prices aggregate knowledge, but that attestation increases the
number of dimensions on which they can do so.

The test is the spread

Run the same market governed and ungoverned — the same goods, the same agents,
one venue with attested terms and deterministic admissibility, one without — and compare the prices. The prediction is that the governed venue trades at a spread to the ungoverned one, and that the spread measures the market's price for trust: for knowing
the latency is real, the jurisdiction is true, the counterparty is who it claims.

If the spread is zero — if governed and ungoverned markets trade at the same price
— the thesis is wrong. That is the falsifiable line. Everything else in this paper is mechanism. The spread is the judge.

Two caveats

First, it is voluntary all the way down. That isn't a design choice of this paper — it is
the kernel's second constraint: all interactions must be voluntary and based on explicit
consent.11 The market is voluntary because the gate it runs on admits nothing else. No
one is forced; anyone can verify. No regulator mandates attested terms. No treaty compels the witness. The enforcement is access: governed venues get the counterparties
that demand proof, and proof-demanding counterparties are the ones with the money.

The precedent is Certificate Transparency. Nobody legislated it. A dominant browser
stopped trusting certificates that were not publicly logged, and within roughly two
years the ecosystem had moved.12 Voluntary in form, decisive in effect, because the
cost of exclusion exceeded the cost of compliance.

But voluntary with network effects becomes compulsory in practice, and whoever sets
the admissibility criteria holds the gate. The design's answer is that the criteria are
public, the witness is independent, and the kernel is deterministic — none of which
prevents capture, all of which make capture visible. An updated economy still needs
its capture caveat. The paper states it. The mechanism prices it.

Second, some properties point forward. An attestation that a model will be retrained
quarterly, that a key will be rotated, that a dataset will remain under its stated license —
these are promises, not measurements, and the architecture treats them as such: bound
cryptographically at the moment of the trade, witnessed when made, and checked
against reality when the future arrives. A promise kept is evidence. A promise broken
is evidence too, priced into every subsequent bid. The treatment is provisional — the
honest status of a hard problem — but the direction is fixed: forward commitments get
     The constraint is stated in Paper 1 of this series and is not re-derived here.
     ‡ Google LLC. Chrome Certificate Transparency Policy, effective 30 April 2018, requiring all
publicly trusted certificates issued after that date to be logged in qualifying CT logs as a condition of being trusted by Chrome. Adoption data confirmed: Scheitle et al., Proc. ACM Internet
Measurement Conference (2018), document pre-enforcement logging below 35% of DV/OV
certificates, rising to near-100% of newly issued certificates within 48 hours of enforcement,
with public log intake jumping from ~1.5M to >8M certificates per day.

the same witnessing as present facts, and the market learns which promisors to trust.

The separation that holds the price layer together

The witness disciplines the honesty of the numbers — was the latency real, the jurisdiction true — not their eﬀiciency. Whether a price was good is a valuation question,
and valuation lives in a disjoint layer that reads the witness's receipts but never writes
to them. Conflate the two and the witness becomes a judge; keep them apart and the
market prices what the evidence supports, nothing more.

The firm-level denominator

The Pulse measures the economy; the CFO measures the firm. Revenue per machine
action: what each agent-executed transaction earns, costs, and risks, with the evidence
attached. The information discount: the spread between what a witnessed action is
worth and what the same action unwitnessed would fetch — the firm's private version
of the market spread.13

Witnessed work becomes the unit the market prices on: not headcount, not hours, not
tickets closed, but attested actions completed under mandate. A firm that can state its
revenue per machine action knows what its agents are worth. A firm that can't is pricing
blind.

The precedent is not metaphorical. Commercial aircraft are not valued on age; they
are valued on cycles and hours remaining against a certified, externally verifiable maintenance record. The record is maintained to a standard and independently auditable,
which is precisely why the asset trades on it rather than on a depreciation schedule.14
       On the relationship between independent assurance and the cost of capital, see Minnis, M.
(2011). The value of financial statement verification in debt financing: Evidence from private
U.S. firms. The Accounting Review, 86(2), 457–490.
   Pittman, J. A., & Fortin, S. (2004). Auditor choice and the cost of debt capital for newly public firms. Journal of Accounting and Economics, 37(1), 113–136. The mechanism — independent verification reducing the uncertainty premium applied by capital providers — is the same
one claimed here for witnessed machine work. Confirmed: DOI 10.1016/j.jacceco.2003.06.005
(working paper: SSRN No. 273618). Subsequent literature qualifies the effect in ways that
strengthen this paper’s framework: the certification discount attenuates as firms age and
build track records (Pittman & Fortin), and for private firms the presence of an audit matters
more than auditor brand (Minnis, 2011, The Accounting Review, 86(2), 457–490).
      † Commercial aircraft and engine valuation practice conditions residual value on remaining cycles and hours against maintenance status, documented through certified maintenance
records maintained to airworthiness-authority standards. See International Society of Transport
Aircraft Trading (ISTAT) appraisal standards and the maintenance-record requirements of 14
CFR Part 43 and EASA Part-145. Confirmed against appraisal methodology: valuation starts
from a Half-Life baseline — the theoretical value assuming 50% of operating utility remains
before major overhaul — then applies dollar-for-dollar adjustments for documented hours,
cycles, and calendar time remaining (ISTAT, Appraisal Principles and Standards of Practice).
Record quality is itself a valuation input: life-limited parts lacking unbroken Back-to-Birth
traceability are legally non-airworthy and valued at scrap (FAA 14 CFR §91.417; EASA PartM), and missing or unverifiable records discount current market value by 40–60%.

Hardware and agent fleets valued on witnessed economic output rather than book depreciation is the same structure.

One concession, stated here rather than discovered by a reviewer. Once revenue-permachine-action drives a multiple, firms will decompose work into more actions. The
witness proves an action occurred; it cannot prove the action was necessary.15 This is a
genuine limit and it is bounded rather than solved: the witness disciplines the numerator's honesty, not the denominator's eﬀiciency. Ratios built on witnessed counts resist
fabrication. They do not resist inflation. Different metrics resist different attacks; none
resist all.

     Goodhart, C. A. E. (1975). Problems of monetary management: the U.K. experience. In
Papers in Monetary Economics, Reserve Bank of Australia. The formulation that a measure ceases
to be a good measure once it becomes a target is Goodhart's; the application to witnessed action
counts is this paper's.

## Chapter 4 — The Asymmetry Tax

Papers 1–5 handed you the blocks. This paper builds with them. The question for the
rest of it is the one a CTO asks: how do I apply this to my workflows — where does it
go? It goes wherever value changes hands at the commit boundary. Part Three shows
where.

Step back, and what this amounts to is an extension of the free market — an updated
economy. Same principles: voluntary exchange, price signals, competition, no central
planner. New substrate: the rules are executable instead of litigated, admissibility is
determined before matching instead of audited after, and every price-moving variable
that can be attested is attested by a party with no position.

The used-car lot

The claim, kept real: attestation shrinks the seller-knows-buyer-guesses asymmetry that
distorts every human market, and a market with less asymmetry discovers truer prices.

Think of the used-car lot. The dealer knows which cars are lemons; you don't. So you
discount every car for the risk — and the dealer with genuinely good cars can't get a
fair price, so he stops bringing good cars to this lot. That's the distortion, and it's worse
than overcharging: asymmetry doesn't just misprice quality; it drives quality out of
the market.16 Every buyer pays the asymmetry tax — the discount for not knowing —
and honest sellers pay most of it.

Attestation removes the tax at the source. The mileage, the accident history, the mechanical state: attested by a party with no position, bound to the listing, checked before
the bid. You don't trust the dealer. You read the attestation. The lemons still exist —
but they're priced as lemons, and the good cars finally get their price.

That is what ”truer prices” means. Not perfect prices. Prices with the asymmetry tax
removed.

That is a prediction, not a fact — the market doesn't exist yet, and the spread is the
test that will judge it. What is already true is the mechanism: deterministic gates, independent witnesses, separated settlement, voluntary participation, and constraints that
police themselves through detectability rather than prevention.

That last one isn't this paper's invention either. It is the constraints' own doctrine, scaled
up: detection carries no penalty inside the system — consequences are priced by the
market and judged at human speed. A violation isn't blocked by force. It's seen by
everyone, priced by everyone, and the violator's future access is what pays for it.
    Akerlof, G. A. (1970). The Market for ”Lemons”: Quality Uncertainty and the Market Mechanism. Quarterly Journal of Economics, 84(3), 488–500.Akerlof's result is that information asymmetry can drive high-quality goods out of a market entirely, not merely misprice them — the
stronger form of the claim used here.

Inherited, not invented

There is a pattern in this paper worth naming. Its market properties keep turning out
to be Paper 1's constraints, inherited rather than invented. Voluntary exchange is Constraint II. Self-policing through detectability is the constraints' own doctrine. Versionbinding everywhere is Constraint VII. The witness that disciplines honesty but never
judges eﬀiciency is the separation the whole architecture is built on.

Paper 6 is Paper 1 running at market scale — the same seven constraints, seen from
the outside, with strangers transacting under them at machine speed. That is why the
paper can be confident about the shape of the thing: it isn't proposing new rules. It's
describing what the old rules imply.

The novelty claim, stated plainly

Reviewers need to be told what is new, so here it is. The new thing is not the gate,
the witness, or the settlement rail — each has precedents, and Papers 1–3 place them
honestly against prior art.

It is that a single evidence artifact does three jobs at once. The same receipt that
proves a determination was legitimate is the IOU the settlement layer nets and the input the valuation layer prices on. Governance control, settlement primitive, valuation
denominator — one artifact, three functions, each reinforcing the others: the control is
trusted because the witness is independent, the settlement is safe because the control
was deterministic, the valuation is honest because the evidence is checkable.

A cross-domain review of the AI governance, payment systems, audit and assurance,
information economics and platform economics literatures did not locate a prior formulation of that convergence. The nearest prior art pairs two of the three functions:
smart-contract architectures combine governance with settlement without feeding the
receipt into valuation (Szabo, 1997); automated trade-finance rails combine settlement
with valuation without pre-execution authorization; continuous auditing combines governance with valuation without settling anything (Vasarhelyi, Alles, & Kogan, 2004).17
The components are documented separately and extensively. The synthesis is this paper's candidate for what is new, and it is offered as a claim to be tested rather than a
claim of priority over any component.

Voluntary exchange, true price signals, competition on attested terms, policing by visibility. The free market, rebuilt on a substrate fast enough for the machines now doing
the trading.
     Negative claim, scoped and dated. A structured review conducted in October 2026 across
the AI governance, payment systems architecture, audit and assurance economics, information
economics and platform economics literatures did not identify a prior work arguing that a single point-of-execution evidence artifact serves simultaneously as governance control, settlement
primitive and valuation input. Negative claims cannot be proved by citation; this one is scoped
as narrowly as the evidence allows.

## Chapter 5 — Obligation

Everything above clears because of one separation, and it is worth stating on its own
because collapsing it is the most common error in systems being built right now.

A receipt is not a payment. The gate's ALLOW creates an economic fact — this party
consumed this, under these terms, and owes this amount. It does not move value. It
records that value is owed. The witness is the IOU. It is not the collector.

Five functions, each prevented from doing the next one's job

 Layer                           Function                       Must not

 Execution                       Performs the action            Attest to itself
 Evidence                        Records what happened          Move money
 Obligation                      Computes what is owed          Enforce payment
 Settlement                      Transfers value                Rewrite evidence
 Enforcement                     Handles failure                Manufacture facts

Execution performs the action. It must not attest to itself — self-attestation provides no
coverage against the failure mode it exists to cover.

Evidence records what happened. It must not move money. A witness that releases
funds is a party to the trade.

Obligation computes what is owed. It must not enforce payment.

Settlement transfers value. It must not rewrite evidence.

Enforcement handles failure. It must not manufacture facts.

This separation is not a proposal. It is how every metered economy has worked. A utility
meter records consumption and collects nothing. A taxi meter records distance and fare
and collects nothing. A shipping receipt records delivery. A trade confirmation records
terms and settles nothing. An invoice states an amount owed and moves no money.
The card networks run authorization, clearing, settlement, and dispute as four distinct
functions, and have for most of a century.18 The receipts in this architecture belong to
that family. They are evidence of an obligation, not evidence of a settlement.

Accounting standards already encode the distinction. A performance obligation is recognized when it is satisfied, independently of when consideration is received; the receivable and the cash are different objects with different recognition events.19 The arCPSS–IOSCO (2012), op. cit. See also card network operating regulations, which define
authorization, clearing, settlement and chargeback as separate processes with distinct timing,
distinct records and distinct liability allocation.
      Financial Accounting Standards Board, ASC 606, Revenue from Contracts with Customers; Inchitecture proposed here is the same distinction expressed at machine speed.

What collapse destroys

What collapse destroys is the unpaid state. A machine economy must be able to say:
the service occurred, the obligation exists, the payment has not cleared.

That sentence is impossible when receipt and payment are the same object. And it is
the sentence the economy needs when liquidity is absent, when settlement is delayed,
when a transfer is blocked by sanction, when fraud is alleged, when evidence conflicts,
when performance was partial, when an amount is disputed.

An atomic settlement that succeeds or rolls back has no vocabulary for owed but unpaid,
which means it has no vocabulary for trade credit, deferred billing, or commercial dispute. It forces full collateralization of every transaction and calls the result eﬀiciency.

It also makes netting impossible. One hundred thousand retrievals at $0.002 settle as
a single $200 transfer closing one hundred thousand obligations, each still individually
traceable. That only works because each obligation was separately itemized. You cannot net what you cannot itemize — and an architecture that fires a payment per action
has nothing to net.20

Authorized is not happened

One more distinction the layers protect. An obligation created at ALLOW for an action
that never executed must be voided by a witnessed event, never silently deleted. The
void is itself a fact, and it is recorded as one. A system that quietly removes obligations
can't distinguish a transaction that didn't occur from one someone wished away.

The error is now visible in the field

The agent-commerce platforms building today have wallets, smart-contract escrow, evaluator agents, on-chain history and reputation registries — every component of a settlement system — protocol designers have acknowledged recurring cases of agent wallets
drained by prompt injection in production.21 The explanation offered is that the market
ternational Accounting Standards Board, IFRS 15, Revenue from Contracts with Customers (2014,
effective 2018). Both frameworks recognize revenue on satisfaction of a performance obligation
and treat the resulting receivable as an object distinct from its settlement.
      On multilateral netting as a settlement-eﬀiciency mechanism dependent on itemized obligation records, see CPSS–IOSCO (2012), Principle 8 (Settlement Finality) and Principle 9 (Money
Settlements).
     † No primary disclosure — protocol documentation, audited on-chain data, or company
statement — supports the numerical claims (transaction volume, realized profit, completion
rates) made in promotional webinars for agent-commerce protocols, and they are not relied on
here. What is independently documented is the failure mode: indirect prompt injections compromising execution tool parameters and credentials in production agent systems; see Agentlacks a killer use case.

The structural explanation is different. Completion that stalls below reliability is not
a payment-rail problem; it is an admissibility problem. A wallet emptied by injection
is not a currency problem; it is an authority problem. An evaluator agent deciding
whether work was done is not an escrow problem; it is an evidence problem, and a
third agent with an opinion is not an independent witness.

These systems compress evidence, evaluation, adjudication, and settlement into one
automated mechanism and treat a successful evaluation as suﬀicient authority to release
funds. They built the rails before the architecture that makes them safe to use, and the
result is not a market that is too early. It is a market missing a layer.

Dojo and OWASP agentic-AI security evaluations.

PART THREE — THE DEPLOYMENTS

Five directions, each in the same shape: what it looks like deployed, how it works, what
the results are — and the testable metric that would prove the paper wrong. No forecasts with dates. The reader in each case is the person who would have to sign for it.

## Chapter 6 — Payments

For the CFO.

What it looks like. A payment network where authorization is proof-based. Today a
card transaction authorizes on credentials — a number, an expiry, a code — and the
fraud industry is the tax on that design. Global card fraud losses run to tens of billions
of dollars annually;22 chargebacks carry a per-incident cost to merchants well above the
disputed amount;23 and US card-not-present fraud alone runs to billions.24 Every one
of those dollars is a payment that was authorized correctly under the rules and was
wrong anyway.

How it works. The payer's agent holds a mandate — whose money, how much, for what
class of purchase, within what window. At authorization, the agent doesn't present
credentials. It presents proof: a Merkle proof against a live policy tree, evaluated in
microseconds against the fraction of a second the authorization already takes. The gate
returns ALLOW with a receipt, or DENY with a reason code, and the transaction never
enters the network without it. There is no credential to steal, because there is no credential — only a proof that this payer, under this mandate, may make this payment,
evaluated fresh at the instant of the trade.
      ‡ The Nilson Report. Global card fraud losses, annual series. Confirmed: The Nilson Report, Issue 1276 (Jan 2025): $33.83 billion in worldwide gross card fraud losses for 2023 —
6.58 cents per $100 of volume — measured before recoveries (chargeback representments,
reversals, and law-enforcement recoveries are not deducted). Issue 1297 (Jan 2026): $33.41
billion for 2024, on $51.92 trillion in volume. US-issued cards were ~25% of global volume
but absorbed ~42% ($14.32 billion) of 2023 losses.
      ‡ Javelin Strategy & Research / Mastercard dispute-management research: an estimated
$128 in operational handling overhead per disputed transaction for US merchants — roughly
$82 in internal labor (intake, investigation, representment evidence) plus ~$46 in third-party
processing fees. That is handling cost, not all-in loss: merchandise value, shipping, and
network monitoring-program fines are excluded. An industry estimate with vendor interest
(it promotes automated dispute-mitigation tooling); independent processor fee schedules
typically run $15–$45 per case before internal labor.
      ‡ The eMarketer “~$9.5 billion for 2023” figure is a secondary commercial forecast, not
an audited total, and is not relied on here. Primary-adjacent figures: The Nilson Report
puts total US gross card fraud at $14.32 billion for 2023, with issuers estimating CNP at 75–
82% ($10.7–$11.7 billion); the Federal Reserve’s Regulation II data covers debit only — $2.43
billion in covered-issuer fraud in 2021, CNP-dominant — and no US authority publishes an
all-channel CNP dollar total.

What the results are. The fraud tax moves from prevention-by-pattern-matching to
prevention-by-construction. A stolen card number buys nothing, because a card number is not what authorizes. The issuer's question changes from does this look like fraud?
to is there a proof? — a question with a deterministic answer, answered before money
moves.

The metric. Fraud loss rate before and after deployment, per portfolio. If it doesn't fall,
the direction fails.

## Chapter 7 — Treasury

For the CFO.

What it looks like. A treasury function where no transfer settles without proof that it
was authorized — not reviewed, not sampled, not reconciled afterward. Proof, before
the commit. The US federal government reports improper payments in the hundreds
of billions of dollars annually — $246.7 billion in FY2022 alone. But “improper” is a
statutory term of art: under the Payment Integrity Information Act it sweeps in payments that may have been substantively proper but lacked suﬀicient documentation.25
A large share of the total is missing paperwork, not confirmed fraud. None of them had
proof at the boundary.

How it works. Each disbursement agent carries a mandate bound to the appropriation:
which program, which payee class, which amount band, which window. The kernel
evaluates the payment against the mandate before the transfer instruction is released.
No proof, no instruction. The witness captures the determination. Settlement happens
on its own rails, netted per obligor — the obligation layer the series has carried since
the receipts were separated from the payments.

What the results are. Improper payments stop being a reconciliation problem and become a matching problem: a payment that can't prove admissibility never becomes a
candidate. The audit moves from after-the-fact sampling to before-the-fact determinism. The auditor's job doesn't disappear — it moves upstream, to the mandates, where
human judgment belongs.

The metric. Improper-payment rate, per program, before and after. The GAO's published figure is the baseline the direction is measured against.

    ‡ United States Government Accountability Oﬀice, annual improper payments reporting.
Confirmed: an estimated $246.7 billion (reported as $247 billion) across 82 programs in
FY2022 (GAO-23-105837; GAO-23-106201); $236 billion in FY2023, $162 billion in FY2024,
$186 billion in FY2025 (GAO-26-108073). Under the Payment Integrity Information Act (31
U.S.C. §§3351–3557), “improper” includes payments that may have been substantively proper
but lacked suﬀicient documentation — it is not a measure of fraud. GAO separately estimated
actual annual fraud losses of $233–$521 billion for FY2018–22 (GAO-24-105833).

## Interlude — Nine Cents

The drone is thirty seconds into the flight when it buys insurance.

Not for the day. Not for the fleet. For this flight — a pharmacy delivery across four kilometres of Rotterdam, eleven minutes, one landing on a residential balcony. Coverage
begins at wheels-up and ends when the package is released. Premium: nine cents.

Nobody sold it to anyone. No application, no broker, no underwriter, no policy document. The operating agent proposed the flight, and requested cover as part of proposing
it. Something priced it and bound it before the rotors reached speed.

Nine cents is a real number because the underwriter is not pricing a risk class. It is not
asking what drones of this type typically do, or what this operator's loss history looks
like across three years. It is pricing this flight. It knows the airframe's maintenance
determinations, each one witnessed, none self-reported by the operator. It knows the
route's incident record. It knows the navigation model in use was authorized for this
airspace class as of this morning. It knows the wind. It knows this agent has completed
nine hundred thousand landings under determinations made before each landing committed, by a gate the operator cannot switch off.

The uncertainty that makes insurance expensive is largely absent. What remains is
weather and physics.

So the premium is thin, and because it is thin the product exists at all. Nobody could sell
eleven minutes of liability cover for nine cents under the old arrangement — not because
the risk was unacceptable, but because underwriting it, issuing it and adjudicating a
claim on it cost three orders of magnitude more than the premium. The product was
not too dangerous. It was too small.

At minute seven, the drone drops the package. A gust it was not built for, four metres
above a balcony. The package lands on a parked car. Nobody is hurt. Dented hood,
cracked windscreen.

The claim does not begin with a person. It begins with the witnessed record arriving
at the insurer: the determination that authorized the release, the sensor state at that
instant, the wind reading, and the fact that the operating agent proposed an abort four
hundred milliseconds earlier and the gate returned DENY — because the abort would
have put the package over a pedestrian crossing. Recorded by something with no stake
in the outcome. Neither the operator nor the insurer can revise it.

Liability resolves in about a second, and not where anyone would have guessed.

Not the operator: the flight was authorized, maintenance current, the agent inside its
mandate. Not the agent's builder: the abort was proposed correctly and denied correctly.
The denial was right under the rule in force, and the rule in force said a package over a
crossing is worse than a package over a car — a rule compiled from a municipal safety
standard adopted eighteen months earlier by a council that never imagined this gust.

The obligation attaches to the standard's own indemnity pool. (The pool is illustrative.
The mechanism is the claim: whoever publishes an executable rule inherits exposure for its
outcomes. The institution is not.) Municipalities that publish machine-executable safety
rules carry cover for the outcomes those rules produce, because otherwise nobody compiles their rules and every operator writes its own.

A claims agent contacts the car owner forty minutes later, already knowing what happened and what it owes. She is paid in three days.

Three things had to be true. A nine-cent policy required underwriting cost below nine
cents, which required the facts to already exist rather than be gathered. A one-second
liability determination required a record from a party with nothing to gain — the operator's own logs would have resolved nothing, whatever they said. And an obligation
landing on a municipal standard required that the standard was compiled, versioned,
and that the version in force at 14:07 on that Tuesday is knowable now.

Remove the independent record, and it reverts: a dispute between an operator and an
insurer over whose logs to believe, settled in months, costing more than the car.

## Chapter 8 — Insurance

For the CEO.

What it looks like. An insurance market where risk is priced on evidence instead of
proxies. Today underwriting prices what it can observe — industry class, revenue band,
loss history — and loads the premium for everything it can't. The unobservable is where
the margin hides, on both sides: the insurer can't see the risk, the insured can't prove
they're better than the class average.

How it works. Every execution inside the insured boundary is traceable to a declared
constraint: the kernel version, the mandate, the determination, the receipt. The underwriter doesn't ask what the company's security posture is. It reads the witness's record
of what the posture did — every ALLOW, every DENY, every reason code, over the
policy period. A company whose gates denied four thousand unauthorized attempts
has a different risk profile than one whose gates never fired, and now both profiles are
checkable instead of asserted.

What the results are. Coverage unlocks where it didn't exist, because the previously unpriceable becomes priced. Premiums separate: the evidenced pay less, the unevidenced
pay for the uncertainty. The honest carrier's advantage — clean evidence history — becomes a number instead of a pitch.

The direction of travel is already visible in carrier behavior. Standard-forms bodies have
published generative-AI exclusion endorsements for commercial general liability, attaching at renewals from January 2026.26 Cyber carriers have drafted AI-related sublimits that remain in development rather than attached wordings.27 Some carriers have
drafted and filed broad AI exclusions across management-liability lines.28 Simultaneously, aﬀirmative AI coverage products have emerged.29
      Insurance Services Oﬀice / Verisk. Generative Artificial Intelligence Exclusion Endorsements, forms CG 40 47, CG 40 48 and CG 35 08, January 2026 edition, attaching at US commercial general liability renewals from 1 January 2026. Attachment is optional and at each carrier's
discretion.
     ‡ Financial Times (2026). Insurers move to cap cyber payouts related to AI and ”LLMjacking.”
22 April 2026. Reported sublimits held payouts on specified AI losses to approximately 10%
of overall policy value. At the time of reporting, at least one carrier's wording remained in
development and had not attached to in-force policies.
     ‡ Lathrop GPM (2026). The AI Coverage Gap: What New Insurance Exclusions Mean for
Your Business. 4 May 2026. Reports that some carriers have drafted and filed ”absolute” AI exclusions across D&O, E&O and fiduciary liability, including claims alleging inadequate AI governance or oversight. The underlying forms are confirmed in force: ISO/Verisk generative-AI
exclusion endorsements CG 40 47 01 26, CG 40 48 01 26 and CG 35 08 01 26 (January 2026 edition), attaching at commercial general liability renewals; and W. R. Berkley form PC 51380 00,
“Artificial Intelligence Exclusion (Absolute),” filed and approved (CT, NY) for managementliability lines. By contrast, AI-related sublimits in cyber lines (e.g., ~10% schedules reported
at Beazley and QBE) remain drafted underwriting proposals, not attached standard wordings
— see Financial Times, 22 April 2026.
     ‡ Cowbell Cyber Inc., Prime One, US launch 21 April 2026; Munich Re, aiSure performanceguarantee insurance for AI solutions. Both cited as evidence that aﬀirmative AI coverage is being
written alongside exclusions, not as endorsements.

Exclusion is not a price. It is a refusal to price, because there is nothing admissible to
price against. That refusal is the commercial opening this chapter describes: a witnessed
system gives an underwriter something to price where an unwitnessed one gives them
a reason to exclude.

The floor drops

Every insurance product has a floor set by the fixed cost of underwriting, verifying and
adjudicating a claim against it. Below that floor the administrative cost exceeds the
premium and the product is not offered — not because there is no demand, but because
it cannot be written profitably. Insurance below the floor is not expensive. It is absent.

Drop the floor and the space beneath it fills. Per-action coverage becomes writable. A
single agent transaction can carry its own policy, priced on evidence from that transaction, because underwriting it no longer costs more than the premium. That is a product
class that does not exist today — not a cheaper version of one, a new one.

The same mechanism runs in reverse, and the paper should say so. The absence of evidence hides mispricing in both directions. Some deployments move from uninsurable
to priced. Some move the other way and turn out to be worse than the pool assumed.

The metric. Availability of coverage and premium spread between evidenced and unevidenced systems, per line. The cautionary exhibit is already trading: when autonomous
agents transact without attested terms — the ungoverned market — the result is not a
market but a casino. The spread between the two is the whole thesis, priced.

## Chapter 9 — Intelligence Licensing

For the CTO.

What it looks like. A corpus — every document, every record, every vector — licensed
per retrieval, to agents, at machine speed. The publisher sets policy once: who may
retrieve, for what purpose class, at what price, with what attribution. Then the metering
runs underneath, and the money flows back per use.

A worked example: a corpus doing 10,000 retrievals a day at $0.00063 per retrieval settles roughly $189 a month.30 Real revenue, per use, with no human in the loop. The
figure is small because the unit is small; the point is that the unit exists at all.

How it works. The retrieval request arrives with an intent envelope: caller, purpose,
use class, maximum cost, time-to-live. The policy gateway evaluates it against the publisher's declared terms — ALLOW or DENY, with a reason code. On ALLOW, a capability token binds that retrieval to that caller for that window; the retrieval executes; the
witness captures a receipt; settlement happens off the hot path, netted per obligor per
epoch, on sub-cent rails. No token, no retrieval.

The token is not a currency — it is a bound authorization, and the distinction matters:
price lives outside the kernel, in the delivery descriptor, never inside the policy artifact. A kernel that evaluates price has acquired an economic position and is no longer
a disinterested gate.

What the results are. Licensing moves from bulk annual deals — negotiated by humans, priced by lawyers, blind to actual use — to per-invocation settlement priced by
the market. The publisher learns what each retrieval is worth because each retrieval is
priced. The agent learns what knowledge costs because every call carries its price back
up the chain.

The metric. Retrieval revenue per corpus, and cost per settled micro-transaction. If
per-use licensing can't beat the bulk deal on the publisher's own books, the direction
fails.

    Worked example from the author's prior technical work on verification-sidecar architectures. The arithmetic is illustrative: 10,000 × $0.00063 × 30 = $189. The per-retrieval figure is a
design target derived from policy-evaluation and settlement cost assumptions, not a measured
production price.

## Chapter 10 — Compute

For the CTO.

What it looks like. A compute market where buyers broadcast requirements and sellers broadcast attested properties, and kernels match them. The buyer wants inference
capacity: attested latency under a band, attested jurisdiction, attested capability, at or
under a price. The sellers — data centers, edge operators, spare-capacity holders —
broadcast what they can prove. Where the constraint sets intersect, the trade clears.
Where they don't, it never appears as a candidate.

How it works. Exactly the configuration in Chapter 2, with compute as the good: mandates carry the spend authority, the kernel evaluates admissibility, the witness captures
the determination, settlement nets off the hot path. Many venues can operate at once —
there is no requirement for one central exchange — because agents act as arbitrageurs
between them, and the witness makes every venue's terms checkable. The mesh coheres
the way markets always have: through participants carrying price information across
boundaries.

On the cost of the gate itself. The objection that governance overhead will be competed away requires a number, and the number is available. Managed authorization
services price single policy evaluations in the single-digit millionths of a dollar per request — batch calls are metered per API call, discounting only at high bundle density;31
formally verified policy engines evaluate in sub-millisecond time with published, peerreviewed guarantees.32 The witnessing side — hash-chaining, external timestamping
and anchoring — is the less well-documented half, and the honest position is that no
independently sourced per-event cost at production scale has been published.33 What
can be said is that the determination is cheap enough that it is not the binding constraint,
and that the burden of proof sits with anyone claiming otherwise.

What the results are. Verified compute trades at a spread to unverified compute, and the
spread is the market's price for trust. The market already pays enormously for trust. It
      ‡   Confirmed       against    current    AWS      pricing    (aws.amazon.com/verifiedpermissions/pricing/, retrieved Oct 2026; pricing moves): single authorization calls
(IsAuthorized) at $0.000005 per request. Batch calls (BatchIsAuthorized, up to 30 decisions
per call) are metered per API call — $0.000150 at Tier 1 — so batching only lowers the
per-decision cost at high bundle density (a full 30-decision batch at Tier 3 pricing reaches
~$0.00000133 per decision; a sparse batch costs more per decision than single calls). The
draft’s “lower rate on batch calls” was directionally wrong at the API-call level.
      † The sub-microsecond vendor benchmark claims for open policy engines are maintainer
self-attestation (sapl.io) with no independent primary source, and are not relied on here. For
peer-reviewed authorization performance, see the formally verified Cedar engine: Hicks et
al., Proc. ACM OOPSLA (PACMPL, 2024), with decidable sub-millisecond evaluation; and
the CNCF performance suite for Open Policy Agent’s Rego evaluation.
       Negative claim, scoped and dated. As of October 2026, no independently sourced per-event
cost figure for tamper-evident witnessing infrastructure at production scale appears to have been
published. Commercial Merkle-anchored evidence architectures are in deployment; their perevent economics are not public.

just pays it blindly — in overprovisioning, in diligence, in the diligence that fails anyway.
Attestation turns the blind payment into a priced one.

Paper 5 documented the negative case at length: decentralised compute marketplaces
have offered production-grade capacity at large discounts to hyperscale list rates, and
production workloads stayed away.34 That is a measured price for the absence of verification, and it is a high one.

The metric. The verified-versus-unverified compute-price spread, per workload class.
If it converges to zero, the thesis is wrong.

     See Paper 5, Chapter 10, and the sources cited there. The pattern — large price discounts
failing to move production or regulated workloads onto unverified hardware — is reported by
the platforms' own users.

PART FOUR — WHAT FOLLOWS

## Chapter 11 — The New Work

The paper has described the mechanism, the prices, and the deployments. It hasn't
answered the question every executive asks first: what happens to the people?

Start with what the old jobs were for. Blocking, reviewing, approving, interpreting
— those roles existed to compensate for systems that couldn't mechanically say yes or
no. Humans were hired to enforce constraints socially because the constraints couldn't
enforce themselves. At machine speed that job is impossible: no human sits inside a
millisecond. So the work moves — from during-execution to pre-execution, from enforcement to encoding. Authority doesn't disappear. It moves upstream, where it
becomes explicit, pre-committed, and accountable.

That movement creates new categories. Constraint architects — a small upstream role:
design and publish the primitives, then done. Execution-fitness consultants — the
scale role, and not regulatory compliance as the industry knows it: execution-boundary
audits, constraint refactoring, exception elimination, fail-fast redesign, readiness preparation. Evidence specialists — exposure consulting, systems integration, forensic replay, readiness diagnostics. New consultancies, not just new job titles: the firms that
today sell compliance review will sell execution fitness, or lose to the ones that do.

Take the two professions the witness paper already put on notice.

The auditor. If an audit is a button press — the deterministic fail-open of the witness
chain, every authorization checked, every obligation accounted for, arrears computed,
all in machine time — the sampling-based audit dies. No more testing controls months
after the fact; the controls are the record. The auditor's work moves to the two places the
button can't reach: auditing the mandates themselves — are the constraints right, are
the terms honest — and forensic replay when humans dispute what the record means.

The lawyer. Most of litigation's cost is discovery, the fight over what happened. With a
complete witnessed record that both sides already hold, what happened is settled. What
remains is what was meant — the terms, the mandate, the declaration. Lawyers stop
being fact-finders and become terms-architects upstream, interpreters downstream.

One honest boundary: the witness attests that the declaration was made and the check
ran, not that the declaration was true. A lied-about diamond gets a faithful receipt
for the lie. Policing the boundary between the world and the declaration — the oracle
problem — is the work that never becomes a button press.35
      The oracle problem — that a system cannot verify the truth of an external fact, only the
fidelity of its record of an assertion about that fact — is treated in Paper 3, Chapter 4, and in the

And it is migration, not extinction. The veterans of the old system carry the institutional memory that makes them valuable — the auditor who knows where the bodies
are buried is the person you want writing the mandate. Role inversion, not displacement: the compliance department doesn't disappear; it moves upstream of the commit
boundary, and its work finally becomes the work that matters.

The broader labour question — what happens to the class of workers whose economic
position rests on being the required intermediary between knowledge and a decision —
is Paper 7's subject, not this one's.36

distributed systems literature on trusted data feeds.
      On the exposure of credentialed knowledge professions to algorithmic automation, see
Susskind, R., & Susskind, D. (2015). The Future of the Professions: How Technology Will Transform
the Work of Human Experts. Oxford University Press.

## Chapter 12 — The Reputation Engine

In the old days your reputation was what the market knew about you — not your ability
to close a deal, but your character as the market had watched it: the quality of your
work, whether your word held, did you pay your suppliers, was the product delivered
on time. John the blacksmith did a fair trade in high-quality horseshoes — good man,
that John Blacksmith — and the village knew, because the village watched.

And it wasn't just the village. Reputation traveled to the regional fairs with the merchant
who carried it — a name, a mark, a house standing behind a bill. This was an economy
without identity papers or credit scores.37 Reputation did the work those do now: it
was the infrastructure of trust.

Then the world got big, the watching stopped scaling, and reputation became marketing:
what you claim about yourself, times your ad budget.

The witness is the village, rebuilt at machine scale. Every determination captured,
chained, checkable — a reputation you can't buy and can't fake, only accumulate. Three
places that break open.

A brand manufacturing sneakers

Today a sneaker brand's reputation is a story told in advertising, defended by lawyers
fighting counterfeits. Under the witness, every pair carries its provenance as receipts:
the factory, the materials, the labor conditions, the shipment — each step witnessed,
each claim checkable. A counterfeit can't clear a governed marketplace; it has no chain.

And here's the hinge: the brand stops owning its reputation. A small maker with a
perfect witnessed record out-reputes a giant with a patchy one, because reputation is
no longer the logo — it's the record. The swoosh becomes a pointer to receipts.

Your credit history

Today it's a score computed about you, by companies you didn't choose, from data you
can't see — and disputing an error takes months. Under the witness, your financial
life is a stream you carry: obligations created, settled on time, voided, overdue — each
evidence-linked, each checkable. Underwriting becomes reading, not scoring.

The hinge: credit goes portable across borders. A lender in Toronto can read the witnessed record of a borrower in Nairobi — two thousand micro-obligations, all settled —
     On reputation as the operative trust infrastructure of pre-modern commerce and its enforcement through merchant communities, see Greif, A. (1993). Contract Enforceability and
Economic Institutions in Early Trade: The Maghribi Traders' Coalition. American Economic Review, 83(3), 525–548; and Milgrom, P. R., North, D. C., & Weingast, B. R. (1990). The Role of
Institutions in the Revival of Trade: The Law Merchant, Private Judges, and the Champagne
Fairs. Economics and Politics, 2(1), 1–23.

better than any bureau file. The thin-file problem that locks hundreds of millions out
of credit dissolves.38 Thin was never the problem. Unwitnessed was.

Identity itself

The deepest one. Today identity is documents a state issues and platforms rent back to
you — attestations by interested parties. Under the witness, identity is the accumulated
record of what you did: what you committed, what you settled, what you promised
and kept. You don't have an identity; you accumulate one — exactly like John Blacksmith,
except the village is the whole economy and nobody can lie about what John did.

A fresh identity with no witnessed history is worth what a stranger's word was worth
in 1300: nothing, until proven.

The collision is real and the paper will not pretend otherwise. The witnessed record
doesn't forget, so selective disclosure — prove you're over 21 without revealing your
birthdate, prove you're trustworthy without revealing the transactions — isn't a feature. It's the price of admission.39 A reputation infrastructure without it is a surveillance infrastructure wearing better language, and the distinguishing property is who
holds the record and what they can move. If the platform holds it, it is a lock-in mechanism. If the subject holds it and anyone can verify it, it is an asset.

The counterexample already exists and should be named rather than discovered. A
commercial employment-verification database holds payroll records on roughly a hundred million American workers, contributed by millions of employers, queried by parties the subject never dealt with.40 It is a cross-firm work record held by a credit bureau
with no relationship to the worker. That is the architecture this chapter argues against,
operating now, at scale.

      ‡ US scope: 26 million credit-invisible adults plus 19 million with unscored thin files
— 45 million total (CFPB, “Data Point: Credit Invisibles,” 2015, with subsequent research
briefs). Global scope: 1.4 billion adults unbanked, with hundreds of millions more lacking
formal credit footprints (World Bank, Global Findex Database, 2021). The draft’s “hundreds
of millions” is the global figure.
       On selective disclosure and zero-knowledge credential presentation, see Camenisch, J., &
Lysyanskaya, A. (2001). An Eﬀicient System for Non-transferable Anonymous Credentials with
Optional Anonymity Revocation. EUROCRYPT 2001. See also W3C Verifiable Credentials Data
Model.
      ‡ Equifax Workforce Solutions, The Work Number. Equifax Workforce Solutions, The
Work Number: 125+ million active payroll records from 2.5+ million contributing employers
(Equifax Inc., Form 10-K, Item 1). The 2022 incident — Equifax scanning 1,000+ of its own remote staff against the database and terminating 24 for undisclosed secondary employment —
is reported only in investigative journalism (Business Insider, Oct 2022); Equifax disclosed
nothing in SEC filings and no court record exists. Treated here as reported, not adjudicated.

## Chapter 13 — Below the Cent

Everything in this paper works because the price signal survives at any granularity.
Obligations are decimal strings, never floats — $0.0003 and $333.00 are the same kind
of object — and settlement nets per window. So ask what an economy looks like when
pricing a ten-thousandth of a cent costs nothing to administer.

Part of the answer is already in the five directions: retrieval licensing, micro-compute,
proof-based authorization. The rest of the answer is that no one can predict it, and the
paper won't pretend to.

Every general-purpose market infrastructure has been followed by services nobody foresaw. The barcode wasn't invented for supply-chain finance. Decimalization wasn't designed for high-frequency trading. The paper predicts the conditions, not the services:
where the marginal transaction cost rounds to zero, categories of exchange appear that
were never worth pricing before.

Some are visible from here.

Attestation becomes a business. The disinterested party with no position is a role the
market pays for, so firms will sell attestations the way auditors sell opinions — except
mechanically, at machine speed. The structural precedent is the marine classification
society: surveyors inspect to a published standard, underwriters refuse to cover what
is unclassed, and the shipowner submits not because survey improves his vessel but
because unclassed ships cannot get freight.41

Witness operation becomes infrastructure. Independent receipt-keeping as a utility.

Arbitrage across the venue mesh becomes a profession again, the way it was on every
trading floor — except the traders are agents and the edge is attested terms.

What people sell — when a human's judgment itself becomes billable per invocation
rather than per week — is the next paper's subject. The rails are this paper's.

      Lloyd's Register historical records. The Society for the Registry of Shipping published its
first Register of Ships in 1764; marine underwriters conditioned cargo and hull coverage on
active listing, with unclassed vessels refused or priced prohibitively. The direction of the incentive — compliance driven by access to freight rather than by inspection's intrinsic merit — is the
mechanism this paper claims for attested terms.

## Chapter 14 — The Pulse

Today we measure the economy the way a nineteenth-century doctor took a pulse: occasionally, by hand, and the number arrives long after the moment. Quarterly GDP,
revised twice. Surveys at the end of the period. By the time the statisticians agree on
what happened, the economy has moved on.

The cadence was never a choice. The monthly survey exists because observation was
expensive — enumerators, mail-back forms, sampling frames. When observation cost
collapses, the cadence has no reason to survive.

The governed economy emits something else: a continuous trace. Every determination
a receipt, every receipt timestamped and chained — obligations created, settled, overdue; authorizations granted and denied — aggregated with privacy preserved. Activity,
velocity, composition, visible now. A sector's obligations spiking overdue is arrhythmia,
visible the day it starts rather than the quarter it gets revised into the record.

Three limits, stated rather than discovered

Coverage bias is worse than sampling error, not better. A survey samples randomly
and reports a confidence interval. A trace observes everything inside its footprint and
nothing outside it — and the footprint is exactly the instrumented, capitalized, agentic
part of the economy. Early on that is a small and deeply unrepresentative slice. A realtime series with no error bars, drawn from firms that could afford instrumentation, is
not a better indicator than a monthly survey. It is a confidently wrong one. Statistical
agencies know how to weight a sample. Nobody yet knows how to weight a census of
the observed portion of an economy.42

Reflexivity. The farm report was slow enough that it described the economy rather
than steering it. Continuous, tradeable economic observation gets traded against, and
behavior adjusts to the measure. This is Goodhart's problem at macro scale, where it
has policy consequences rather than accounting ones.

Custody. A real-time observatory of economic activity is concentrated power. The disjointness discipline answers the coupling objection at transaction level — the witness
has no position in the trade. It does not answer this. A witness with no position in
any single transaction still holds an aggregate view of every transaction, and whoever
holds that view sees the economy before anyone else does. Statistical agencies handle
     On the methodological transition from survey-based to administrative and transactionderived economic indicators, and the coverage problems it introduces, see the national statistical oﬀices' published guidance on alternative data sources. Named: Cantú, C., Cheng, G., &
Doerr, S. (2021). How do central banks use big data? BIS Working Papers No. 907 — commercial card feeds and web-scraped indices over-sample banked, urban populations, distorting
measurement during shocks; and Alvarez, P., et al. (2020). Tracking Economic Activity with
High-Frequency and Big Data. IMF Working Paper WP/20/274 — unadjusted merchant feeds
miss informal cash-heavy sectors without probability-stratified sampling.

this with embargo protocols, release schedules and legal separation from market participants — institutional machinery built precisely because early sight of economic data is
worth money.43 That machinery is a design requirement for the mesh, not a footnote.

The honest framing: the mesh does not produce economic statistics. It produces the
substrate from which statistics could be computed, and the hard problems of representativeness, custody and release remain exactly where they have always been. What
changes is the input, not the discipline.

The voluntary engine

Here is the limit that is also the mechanism: nobody mandates the gates, and nobody
mandates the witness. Both are purely voluntary. But absence is a signal. A counterparty with ten years of witnessed receipts is deep; one with ten days is shallow; one
with none is a stranger — worth what a stranger's word was worth in 1300.

The market prices depth. So it makes sense to be on the system, and the longer you're on,
the farther back your receipts go, the deeper your reputation. Voluntary to join; reputational to stay. That is how a voluntary system becomes effectively universal without
anyone forcing it — the capture caveat's gentler twin, stated here rather than discovered
later.

Two more limits, plainly. The trace covers the governed economy; cash, informal activity
and non-participating venues stay dark. And the scan is not a diagnosis: it shows the
rhythm and the structure, not the health. Value-add, imputations, quality adjustment
— the economists' work — still needs doing. What disappears is the lag between the
economy and our picture of it.

     On embargo and release protocols for market-sensitive oﬀicial statistics, see the IMF Special
Data Dissemination Standard and the principles governing advance release calendars and prerelease access at major statistical agencies.

PART FIVE — CLOSE

## Chapter 15 — Why Now

Three forces, then the precedents.

AI-driven deflation. Machine execution keeps getting cheaper. Every order of magnitude the cost falls, transactions that were uneconomical become economical — not ten
times more of the same acts, but whole categories of exchange that never existed. The
price signal has to survive at that granularity. A market that can't price a ten-thousandth
of a cent can't govern a ten-thousandth-of-a-cent act, and the acts are coming regardless.
Sub-cent settlement isn't a feature. It's the precondition.

Jevons, at the market layer. When the cost of a resource falls, its use rises — and when
the cost of transacting falls, the number of transactions rises faster than the cost fell.44
Each tenfold drop in transaction cost unlocks exchanges nobody bothered to price before: the retrieval, the inference, the verification, the attestation itself. The machinespeed economy is what the Jevons effect looks like when the thing getting cheaper is
the trade.

The supply side sets the clock. The objection that nobody needs governance at machine
speed — that a claimant does not care whether reimbursement takes ten microseconds
or ten days — is correct and misses the causality. The claimant does not set the interval.
The operator does, and the operator faces competitive pressure on compute utilization.
The silicon vendors have made the argument on the record: agents are described as
operating on timescales measured in nanoseconds rather than seconds, and processor
architecture is being redesigned around that premise, because every interval an agent
spends waiting is accelerator capacity sitting idle.45

Cite that as evidence of where capital is moving, not as physics. The rhetorical figure
      Jevons, W. S. (1865). The Coal Question: An Inquiry Concerning the Progress of the Nation, and
the Probable Exhaustion of Our Coal-Mines. Macmillan. The extension from resource eﬀiciency to
transaction cost is this paper's; Jevons's own argument concerns coal.
     ‡ NVIDIA Corporation. GTC Taipei keynote and associated announcements, 31 May – 1
June 2026, introducing the Vera CPU as a processor designed for agentic workloads, with the
stated argument that prior CPUs were designed for human-timescale interaction and that agent
workloads are latency-bound on tool calls, database access and memory retrieval. Cited as evidence of industry investment direction, not as an independent physical finding; the vendor
has a commercial interest in the claim. Corrected: the Vera CPU was announced in Jensen
Huang’s Computex Taipei keynote, 2 June 2024, and reaﬀirmed at GTC 2025 — not at a 2026
GTC Taipei event. The stated argument (prior compute designed for human-timescale interaction; agent loops latency-bound on tool calls, serialization, and memory retrieval) is
confirmed as NVIDIA’s framing. Cited as evidence of industry investment direction, not
as an independent physical finding; the vendor has a commercial interest in the claim. See
NVIDIA keynote archives and Rubin-architecture technical publications.

is directional; memory latency is nanoseconds, tool calls and database round trips are
microseconds to milliseconds. What matters is that the window is being compressed for
revenue reasons by parties not thinking about governance at all — which is precisely
why it will close, and why nobody will reopen it for a compliance check.

The mesh. There will not be one exchange. There will be many venues — payments,
treasury, compute, licensing, and venues nobody has named yet — and agents will arbitrage between them the way traders always have, carrying price information across
boundaries. The market coheres through the participants, not through a center. The witness makes every venue's terms checkable, which is what lets the mesh hold together
without a trusted intermediary.

This has happened before

Not the technology — the pattern: a measurement becomes cheap, a market forms
around the measurement, and the economy reorganizes itself on top.

Decimalization is the lead exhibit. On 29 January 2001 the New York Stock Exchange
completed its move to a minimum price increment of one cent, from one-sixteenth of a
dollar; Nasdaq completed its rollout on 9 April 2001.46 Nothing about the underlying
companies changed. The measurement changed. Within years, high-frequency trading
— machines quoting and trading inside the new granularity — grew to a substantial
share of US equity volume.47 The machines didn't appear because someone invented
trading. They appeared because the market started measuring in units fine enough for
machines to trade in. The groundwork matters too: the 1996 Order Handling Rules
and 1998 Regulation ATS had already opened the structure.48 Decimalization was the
detonator, not the whole charge.

The Chicago Board of Trade, founded in 1848, spent its first decade as a club where
grain traded on inspection and reputation. Standardized grading and inspection arrived in the late 1850s, and standardized futures contracts followed in the 1860s — and
grain became fungible: interchangeable warehouse receipts, tradable sight unseen, by
     ‡ US Securities and Exchange Commission, decimalization implementation orders and
phase-in schedule, 2000–2001. Confirmed: SEC Release No. 34-42914 (June 8, 2000) ordering decimalization, with phase-in from August 28, 2000; NYSE full decimalization January
29, 2001 (Release No. 34-43638); Nasdaq full decimalization April 9, 2001 (Release No. 34-
44048). Dates as carried in the draft.
     ‡ TABB Group estimated high-frequency trading at 61% of total US equity share volume
in 2009 — the commonly cited peak — declining thereafter; see SEC Concept Release on Equity Market Structure, Release No. 34-61358 (75 FR 3594, Jan 14, 2010), which cites TABB’s
figures. Trade-press repetition of ‘approximately 70%’ conflates HFT with algorithmic execution generally. Analysis of NASDAQ order-audit data puts HFT participation at 68.5% of
trades but 50–54% of share volume (Brogaard, Hendershott & Riordan, 2014).
      US Securities and Exchange Commission, Order Execution Obligations, Release No. 34-
37619A (1996); Regulation of Exchanges and Alternative Trading Systems (Regulation ATS),
Release No. 34-40760 (1998).

people who had never seen the grain.49 The grade created the market. Roughly two
decades of building, not an overnight flip — the discipline against imagining instant
transition.

The electricity meter arrived in the 1880s, and the meter created the market it measured:
once consumption could be metered per customer, pricing models and economies of
scale followed. Samuel Insull's work at Chicago Edison from 1892 is the famous case.50
He didn't invent the meter. He built the economy the meter made possible.

The barcode: symbology selected in 1973; first commercial scan on 26 June 1974 at
a Marsh supermarket in Troy, Ohio — a pack of Wrigley's gum.51 Billions of scans a
day now. Note what the barcode actually carries: identity, not price. The computer
resolves the price. Measurement and valuation, separate — the same separation this
paper's architecture keeps between the witness and the valuation layer.

The supporting cast is long. SWIFT, founded 1973, first message 1977, replacing freeform telex with standardized machine-readable financial messages.52 The stock ticker —
Edward Calahan's 1867 invention — putting prices on wire in real time.53 Double-entry
bookkeeping, described in print by Pacioli in 1494, making the firm's state checkable.54
The bill of lading, recognized as a document of title in Lickbarrow v Mason (1787), letting
goods trade while still at sea.55

Every one of them: a measurement or a record got cheap and trustworthy, and a market
      ‡ On the Chicago Board of Trade's transition from inspection-and-reputation trading to standardized grades, warehouse receipts and futures contracts, see Cronon, W. (1991). Nature's
Metropolis: Chicago and the Great West. W. W. Norton, especially Chapter 3. Dates confirmed:
first wheat categories 1856; oﬀicial inspector corps and uniform grading 1858; Illinois charter conferring inspection authority February 1859; standardized futures under Rule VIII —
delivery months, 5,000-bushel lots, standard grades, compulsory margins — 1865.
      ‡ On Insull's development of load-factor-based pricing and mass-market electricity supply at Chicago Edison from 1892, see McDonald, F. (1962). Insull. University of Chicago
Press. The metering mechanism was Arthur Wright’s maximum-demand indicator (US
Patent No. 583,803): Insull acquired the US rights in 1897 and deployed the two-part Wright
demand tariff across Chicago in 1898 — the meter made differential pricing, and the market
it enabled, possible. See Hughes, T. P. (1983). Networks of Power: Electrification in Western
Society, 1880–1930. Johns Hopkins University Press.
       GS1 and Smithsonian National Museum of American History records. The first commercial
scan of a Universal Product Code took place on 26 June 1974 at Marsh Supermarket, Troy, Ohio,
on a ten-pack of Wrigley's Juicy Fruit gum. ‡ The symbology selection date is confirmed: the
Uniform Grocery Product Code Council selected IBM’s proposal (George Laurer) on 3 April
1973. The frequently cited $17 billion in annual US grocery-industry savings is Garg, Jones
& Sheedy, “17 Billion Reasons to Say Thanks: The 25th Anniversary of the U.P.C. and Its
Impact on the Grocery Industry,” PricewaterhouseCoopers / Uniform Code Council (1998).
       Society for Worldwide Interbank Financial Telecommunication, founded 1973; first live message 1977.
       Calahan, E. A., stock ticker, 1867. Commonly misattributed to Edison, who improved the
design in 1869.
       Pacioli, L. (1494). Summa de Arithmetica, Geometria, Proportioni et Proportionalità. Venice.
Pacioli codified existing Venetian practice rather than inventing double-entry bookkeeping.
       Lickbarrow v Mason (1787) 2 TR 63; subsequent proceedings (1794) 5 TR 683. The case
established that an endorsed bill of lading is a document of title at common law, permitting
goods in transit to be sold or pledged.

formed around it.

## Chapter 16 — What Could Fail

A blueprint that can't name its failure modes is a brochure.

Coordination sometimes never resolves

Attested terms require shared schemas — what counts as a latency band, a jurisdiction,
a posture — and standards processes stall, fork, or get captured. The paper's answer is
that convergence comes from below, priced by pass rates, not from a committee. That
answer is a mechanism, not a guarantee. Persistent fragmentation is not an exotic outcome. It is the normal one; there are still incompatible rail gauges and competing electrical plugs.

Voluntary becomes compulsory

The capture caveat from Chapter 3, repeated because it is the failure mode: network
effects make the dominant venue's terms the terms, and whoever sets admissibility criteria holds the gate. Public criteria, independent witnesses and deterministic kernels
make capture visible. Visible is not the same as prevented.

The walled garden

This is the strongest objection and it deserves a fair hearing rather than a dismissal.

Apple and Tesla are genuine successes. A closed platform does not eliminate the four
functions; it performs all of them internally and self-attests the results. The platform
determines admissibility, records execution, computes obligation, settles and enforces
— all as one party. That works, and it has worked for a long time.

The paper does not ask them to submit to independent witnesses. They wouldn't. The
answer is structural rather than normative.

A closed platform cannot run a multi-seller auction on attested attributes, because the
attestations come from the party that owns the sellers. Self-attestation is an interested
party grading its own homework. It works inside the walls — the engineering can be
excellent — but it cannot price across them. The moment a buyer wants to compare the
closed platform's offering against an independent seller's on equal evidentiary terms,
the closed attestation is worth what the platform's word is worth.

Watch what each has had to build. Developer revenue reporting on major app platforms
has been contested for years precisely because developers have no independent measure
of their own sales: the platform is the sole source of the facts on which it pays them.56
     ‡ Epic Games, Inc. v. Apple Inc., 559 F. Supp. 3d 898 (N.D. Cal. 2021), and subsequent appellate and enforcement proceedings. Specified: the Rule 52 Findings of Fact and Conclusions of
Law (Dkt. 812, Sept 10, 2021), Parts II.C and IV.B — Apple’s anti-steering rules deprived deThat is the self-attestation problem appearing exactly where this paper's derivation says
it must — at the obligation layer, between parties who do not fully trust each other. And
at least one vehicle manufacturer vertically integrated an insurance arm, with vehicle
data cited as the pricing advantage; structurally, it absorbed the counterparty because
no external underwriter could price a risk whose evidence only the manufacturer could
see.57

The ceiling is breached by three conditions: consequence exceeding what the platform
can absorb on its own balance sheet; counterparties outside the walls, which is every
cross-platform, cross-border or cross-organizational transaction; and an external authority — regulator, court, reinsurer — demanding facts from a party with an interest
in them.

The governed market doesn't defeat the walled garden. It prices around it: every
transaction the garden can't evidence is a transaction whose trust discount the open
market doesn't pay. The honest claim is not that closed platforms lose. It is that the
walled garden's economics degrade as consequence rises and as counterparties multiply — and that agent-to-agent commerce is by construction a high-counterparty environment. How much value crosses trust boundaries relative to how much stays inside
them is an empirical question this paper does not resolve.

And the spread

If governed and ungoverned markets trade at the same price — if nobody will pay for
attested terms, deterministic admissibility, and independent evidence — the thesis is
wrong. Not incomplete, not early. Wrong.

The paper stakes itself on that test because a paper that can't be wrong isn't saying anything.

One more, repeated at the close

The honest boundary from Chapter 2. Deployed gates today are unilateral. Bilateral
agent-to-agent matching at machine speed is the mechanism they point toward. The
parts exist. The assembly is connection, not invention. But connection is still work, and
velopers of customer contact information, billing metadata, and transaction receipts, leaving
developers to accept Apple’s aggregated, delayed platform statements without independent
audit access to ledger events. Aﬀirmed in part, 67 F.4th 946 (9th Cir. 2023).
     ‡ Tesla, Inc., Tesla Insurance. Confirmed as substantially the company’s stated rationale.
Tesla Insurance launched in California, August 2019 (CDI File No. 19-3548); Safety-Score
telematics pricing in Texas from October 2021. On the Q2 2019 earnings call (July 24, 2019)
Tesla said external insurers lacked telemetry to separate safe from risky drivers, inflating EV
premiums; on the Q3 2020 call (Oct 21, 2020) Musk described vertical integration as an “information arbitrage” — real-time sensor streams versus demographic proxies. The structural
inference (absorbing the counterparty where evidence is manufacturer-visible only) is this
paper’s.

the paper doesn't grade its own homework.

Machine-Speed Economics is Paper 6 of the Machine Speed Papers. Paper 7 — The Metered
Mind — takes up what these rails do to human knowledge work: the individual selling judgment
per use instead of time per week, and the economic unit becoming the invocation.

Author interest statement

The author is the founder of HyperEdgeX.ai, a company working on execution-boundary
governance and verification infrastructure for autonomous systems. This paper names
no implementation of any component it describes and argues only that the architectural
categories are necessary, not which instance of them should be adopted. One worked
example (Chapter 9) derives from the author's prior technical work and is labeled as
such. The analysis stands or falls on the evidence presented; readers should weigh it
accordingly.

A note on the references

Footnotes marked † rest on aggregated, secondary or industry-reported sources rather
than a single primary document, and are identified as such so the reader can weigh
them. Footnotes marked ‡ record figures that were accurate at the time of writing but
are expected to move — regulatory filings, market sizes, pricing pages and product
launches. Working-draft footnotes that carried [VERIFY: …] flags have been resolved
against primary sources in this version; none remain. Several claims in this paper are
negative — that no prior literature synthesizes a given argument, that no per-event cost
figure has been published — and negative claims cannot be proved by citation. Each is
scoped as narrowly as the evidence allows and dated.

Glossary of Terms

Terms are defined as used in this paper. Where a term is also used elsewhere with a
different meaning, that usage is not implied here.

Admissibility — The property of a proposed action that permits it to cross the execution boundary. In this paper, admissibility is also the matching criterion: a trade is a
candidate only where both parties' constraint sets are satisfied.

Agent — Software acting for a principal, proposing actions, carrying a purse, and answerable for what it commits.

Asymmetry tax — The discount a buyer applies for not knowing what the seller knows.
Paid by every buyer; borne disproportionately by honest sellers, whose goods cannot
obtain their fair price in a market that cannot distinguish them.

Attestation — A claim about a price-moving property — latency, uptime, jurisdiction,
posture, energy mix — issued by a party with no position in the trade it informs. Distinguished from a vendor assertion, which is self-attestation.

Bid attribute — A property on which a trade can be priced. The paper's claim is that
attestation converts qualitative assurances into bid attributes.

Broadcast terms — The constraints an agent publishes about counterparties it will transact with. Provable rather than merely declared: the terms resolve to attestations and to
a nameable mandate version.

EGK (Executable Governance Kernel) — A deterministic gate evaluating a proposed
action against compiled constraints, returning ALLOW or DENY with a reason code
before the action commits. Established in Papers 1 and 2; not re-derived here.

Enforcement layer — The function that resolves failures to satisfy obligations. Must not
manufacture facts.

Evidence layer — The function that records what happened. Must not move money.

Execution layer — The function that performs the action. Must not attest to itself.

Information discount — The firm-level analogue of the spread: the difference between
what a witnessed action is worth and what the same action unwitnessed would fetch.

Mandate — The preconstrained limits an agent carries: whose authority, for what purpose, at what cost, within what window, with what receipt capability. Declared before
anything moves, signed, versioned.

Matching — The intersection of two agents' constraint sets. A trade that would fail
governance never appears as a candidate.

Obligation layer — The function that computes what is owed. Must not enforce payment. The layer whose collapse into settlement destroys the unpaid state.

Pass-rate transparency — Published data on which mandates clear which gates, at what
cost, how often. Lets both sides tune terms against clearance.

Pulse — The continuous trace of determinations and obligations emitted by a governed
economy, aggregated with privacy preserved. Named to avoid collision with EGK.

Purse — Bounded spending authority carried to the boundary and settled against at
the point of commit. An amount, an expiry, a scope. You cannot spend what isn't in it.

Receipt — The witness's output: a verifiable claim that a determination occurred, unaltered, at a stated time. Evidence of an obligation, not evidence of a settlement. The
IOU, not the collector.

Revenue per machine action — The firm-level denominator: what each agent-executed
transaction earns, costs and risks, with the evidence attached.

Settlement layer — The function that transfers value. Must not rewrite evidence.

Spread, the — The price difference between a governed and an ungoverned venue for
the same goods. The paper's falsifiable test. If it is zero, the thesis is wrong.

Unpaid state — The economy's ability to say: the service occurred, the obligation exists,
the payment has not cleared. Impossible when receipt and payment are the same object.

Version-binding — The practice of carrying the version of every rule, mandate and
attestation with the thing itself, because at machine speed ”the current terms” is meaningless without it.

Walled garden — A closed platform performing admissibility, evidence, obligation,
settlement and enforcement internally and self-attesting the results. Works inside the
walls; cannot price across them.

Witness — An independent mechanism capturing each determination as it occurs: chained,
externally timestamped, administratively separate, disclosable without any party's cooperation. It does not govern. Established in Paper 3.

Bibliography

A — Economics and market theory

Akerlof, G. A. (1970). The Market for ”Lemons”: Quality Uncertainty and the Market
Mechanism. Quarterly Journal of Economics, 84(3), 488–500.

Alvarez, P., et al. (2020). Tracking Economic Activity with High-Frequency and Big Data:
Opportunities and Challenges. IMF Working Paper WP/20/274.

Brogaard, J., Hendershott, T., & Riordan, R. (2014). High-frequency trading and price discovery. Review of Financial Studies, 27(8), 2267–2306.

Cantú, C., Cheng, G., & Doerr, S. (2021). How do central banks use big data? BIS Working
Papers No. 907.

Catalini, C., & Gans, J. S. (2020). Some simple economics of the blockchain. Management
Science, 66(11), 5012–5039.

Consumer Financial Protection Bureau (2015). Data Point: Credit Invisibles. CFPB Oﬀice of
Research.

Davidson, S., De Filippi, P., & Potts, J. (2018). Blockchains and the economic theory of the firm.
Journal of Institutional Economics, 14(4), 639–658.

Alvarez, P., et al. (2020). Tracking Economic Activity with High-Frequency and Big Data:
Opportunities and Challenges. IMF Working Paper WP/20/274.

Brogaard, J., Hendershott, T., & Riordan, R. (2014). High-frequency trading and price discovery. Review of Financial Studies, 27(8), 2267–2306.

Cantú, C., Cheng, G., & Doerr, S. (2021). How do central banks use big data? BIS Working
Papers No. 907.

Catalini, C., & Gans, J. S. (2020). Some simple economics of the blockchain. Management
Science, 66(11), 5012–5039.

Consumer Financial Protection Bureau (2015). Data Point: Credit Invisibles. CFPB Oﬀice of
Research.

Davidson, S., De Filippi, P., & Potts, J. (2018). Blockchains and the economic theory of the firm.
Journal of Institutional Economics, 14(4), 639–658.

Goodhart, C. A. E. (1975). Problems of monetary management: the U.K. experience. In
Papers in Monetary Economics. Reserve Bank of Australia.

Greif, A. (1993). Contract Enforceability and Economic Institutions in Early Trade: The
Maghribi Traders' Coalition. American Economic Review, 83(3), 525–548.

Hayek, F. A. (1945). The Use of Knowledge in Society. American Economic Review, 35(4),
519–530.

Jevons, W. S. (1865). The Coal Question. Macmillan.

Milgrom, P. R., North, D. C., & Weingast, B. R. (1990). The Role of Institutions in the Revival of Trade: The Law Merchant, Private Judges, and the Champagne Fairs. Economics
and Politics, 2(1), 1–23.

Susskind, R., & Susskind, D. (2015). The Future of the Professions. Oxford University Press.

TABB Group (2009). US equity high-frequency trading volume estimates; cited in SEC Release
No. 34-61358.

World Bank (2021). The Global Findex Database: Financial Inclusion, Digital Payments, and
Resilience in the Age of COVID-19.

B — Accounting, assurance and market infrastructure

Business Insider (2022). Equifax’s internal Work Number audit and employee terminations. October 2022. (Investigative reporting; no primary disclosure.)

Committee on Payment and Settlement Systems & IOSCO (2012). Principles for Financial Market Infrastructures. Bank for International Settlements.

Financial Accounting Standards Board. ASC 606, Revenue from Contracts with Customers.

International Accounting Standards Board (2014). IFRS 15, Revenue from Contracts
with Customers.

Javelin Strategy & Research / Mastercard (2025–2026). Dispute-management operational cost research: $128 average merchant handling cost per chargeback (US).

Minnis, M. (2011). The value of financial statement verification in debt financing: Evidence from private U.S. firms. The Accounting Review, 86(2), 457–490.

Pittman, J. A., & Fortin, S. (2004). Auditor choice and the cost of debt capital for newly
public firms. Journal of Accounting and Economics, 37(1), 113–136.

Pacioli, L. (1494). Summa de Arithmetica, Geometria, Proportioni et Proportionalità. Venice.

Vasarhelyi, M. A., Alles, M. G., & Kogan, A. (2004). Principles of analytic monitoring for
continuous assurance. Journal of Emerging Technologies in Accounting, 1, 1–21.

C — Legal and regulatory

Epic Games, Inc. v. Apple Inc., 559 F. Supp. 3d 898 (N.D. Cal. 2021), aff’d in part, 67 F.4th
946 (9th Cir. 2023). Rule 52 Findings of Fact and Conclusions of Law, Dkt. 812 (Sept 10,
2021), Parts II.C, IV.B.

Lickbarrow v Mason (1787) 2 TR 63; (1794) 5 TR 683.

US Securities and Exchange Commission (1996). Order Execution Obligations. Release
No. 34-37619A.

US Securities and Exchange Commission (1998). Regulation of Exchanges and Alternative Trading Systems. Release No. 34-40760.

US Securities and Exchange Commission. Decimalization orders: Release No. 34-42914
(June 8, 2000); Release No. 34-43638 (Nov 29, 2000); Release No. 34-44048 (Mar 7, 2001).
Concept Release on Equity Market Structure, Release No. 34-61358 (Jan 14, 2010).

United States Government Accountability Oﬀice. Improper payments annual reporting:
FY2022 estimate $246.7 billion (GAO-23-105837; GAO-23-106201); FY2023 $236 billion;
FY2024 $162 billion; FY2025 $186 billion (GAO-26-108073).

D — Insurance

Insurance Services Oﬀice / Verisk (2026). Generative Artificial Intelligence Exclusion
Endorsements. Forms CG 40 47, CG 40 48, CG 35 08. January 2026 edition.

W. R. Berkley. Artificial Intelligence Exclusion (Absolute), Form PC 51380 00 (06-24).
Filed and approved (CT, NY); attaching to management-liability lines.

Lathrop GPM (2026). The AI Coverage Gap: What New Insurance Exclusions Mean for
Your Business. 4 May 2026.

Financial Times (2026). Insurers move to cap cyber payouts related to AI and “LLMjacking.” 22
April 2026. (Reports drafted ~10% AI sublimit schedules at Beazley and QBE; in development,
not attached.)

Lloyd's Register. Historical records of the Register of Ships, from 1764.

Cowbell Cyber Inc. (2026). Prime One. — Munich Re. aiSure. (Aﬀirmative AI coverage
products.)

E — Protocols, cryptography and policy engines

Birgisson, A., Politz, J. G., Erlingsson, Ú., Taly, A., Vrable, M., & Lentczner, M. (2014).
Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the
Cloud. NDSS 2014.

Camenisch, J., & Lysyanskaya, A. (2001). An Eﬀicient System for Non-transferable
Anonymous Credentials with Optional Anonymity Revocation. EUROCRYPT 2001.

Hicks, M., et al. (2024). Formally verified authorization: the Cedar policy language.
Proc. ACM OOPSLA (PACMPL).

Laurie, B., Langley, A., & Kasper, E. (2013). Certificate Transparency. RFC 6962. IETF.

Laurie, B., Messeri, E., & Stradling, R. (2021). Certificate Transparency Version 2.0. RFC
9162. IETF.

Scheitle, Q., et al. (2018). Large-scale measurement of Certificate Transparency adoption. Proc. ACM Internet Measurement Conference.

Open Policy Agent. Rego policy language. CNCF graduated project.

Amazon Web Services. Cedar policy language.

Amazon Web Services. Verified Permissions pricing. (aws.amazon.com/verified-permissions/pricing/.)

Szabo, N. (1997). The idea of smart contracts.

W3C. Verifiable Credentials Data Model.

XRP Ledger Foundation. Developer documentation: consensus finality and transaction
cost. (xrpl.org.)

Coinbase Developer Platform. x402: open payments protocol for HTTP (Apache-2.0);
specification and reference implementation, 2025. Live on Base mainnet. (x402.gitbook.io.)

F — Agent architecture

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct:
Synergizing reasoning and acting in language models. ICLR 2023.

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., et al. (2024). A survey on
large language model based autonomous agents. Frontiers of Computer Science, 18(6).

NVIDIA Corporation. Vera CPU announcement, Computex Taipei keynote, 2 June 2024;
reaﬀirmed GTC 2025.

G — Economic and commercial history

Cronon, W. (1991). Nature's Metropolis: Chicago and the Great West. W. W. Norton.

de Roover, R. (1963). The Rise and Decline of the Medici Bank, 1397–1494. Harvard
University Press.

Garg, V., Jones, C., & Sheedy, C. (1998). 17 Billion Reasons to Say Thanks: The 25th
Anniversary of the U.P.C. and Its Impact on the Grocery Industry. PricewaterhouseCoopers / Uniform Code Council.

Garg, V., Jones, C., & Sheedy, C. (1998). 17 Billion Reasons to Say Thanks: The 25th
Anniversary of the U.P.C. and Its Impact on the Grocery Industry. PricewaterhouseCoopers / Uniform Code Council.

Lopez, R. S. (1976). The Commercial Revolution of the Middle Ages, 950–1350. Cambridge
University Press.

McDonald, F. (1962). Insull. University of Chicago Press.

Ray, A. J., & Freeman, D. (1978). ”Give Us Good Measure.” University of Toronto Press.

Hudson's Bay Company Archives, Provincial Archives of Manitoba.

Hughes, T. P. (1983). Networks of Power: Electrification in Western Society, 1880–1930.
Johns Hopkins University Press.

Hughes, T. P. (1983). Networks of Power: Electrification in Western Society, 1880–1930.
Johns Hopkins University Press.

GS1 / Smithsonian National Museum of American History. Universal Product Code
historical records.

Society for Worldwide Interbank Financial Telecommunication. Founding and operational history, 1973–1977.

H — Prior papers in this series

Watson, J. M. (2026). Execution-Boundary Governance. SSRN 7034678.

Watson, J. M. (2026). Constitutional Compression. SSRN 7199200.

Watson, J. M. (2026). Evidence Systems. SSRN 7207219.

Watson, J. M. (2026). Upstream. SSRN 7211100.

Watson, J. M. (2026). The Execution Surface. SSRN [pending].

End of manuscript — Version 0.2 Machine-Speed Economics: How Evidence Becomes the
Price Signal 16 chapters. 2 interludes. One falsifiable test.

Jonathan M. Watson Independent Researcher jonmwatson@gmail.com October 2026
