# PAPER 7 — The Metered Mind *(working title)*

**Unit of analysis: the worker and the market.**

## Core thesis

The same architecture that lets agents transact lets an individual sell judgment per
use rather than selling time per week. Micropayments were never the obstacle; the
human in the decision loop was. Remove that, and the economic unit of knowledge
work becomes the invocation.

## Opening argument — micropayments, claim vs fact

**Fact:** consumer micropayment systems repeatedly failed. Millicent (DEC, Systems
Research Center, mid-1990s; public beta 1997; KCOM Japan pilot June 1999),
CyberCoin/CyberCash (CyberCash founded 1994; CyberCoin launched October 1996;
bankrupt 2001), Peppercoin (MIT spin-off, Rivest & Micali; launched December
2003; probabilistic settlement cutting the fee on a 99¢ sale from ~27¢ to under
10¢; faded mid-2000s). **[FIXED]** Date Millicent mid-1990s, not 1999.

**Claim about why:** Shirky, "Fame vs Fortune: Micropayments and Free Content"
**(2003 — NOT 2000)**, borrowing Szabo's "mental transaction costs" to argue the
decision cost of buying exceeds the payment; Odlyzko, "The Case Against
Micropayments" (2003, FC 2003, LNCS 2742) — obstacles economic/sociological/
psychological rather than technological, consumers want predictable simple pricing;
Szabo — cite both: "The Mental Accounting Barrier to Micropayments" (1996) and
"Micropayments and Mental Transaction Costs" (1999). **[FIXED]**

**The move:** metered per-unit pricing has worked continuously at enormous scale
wherever the decision was automated. Electricity, mobile data, cloud compute, API
calls, per-token inference. Nobody calls those micropayments. The failure was never
the payment. **It was the prompt.**

Frame the section as an explicit refutation of transferability — not "micropayments
will work now," but "the diagnosis that killed them was correct and does not apply
to agents."

## The symmetric problem — confront it early

Humans still appear as *sellers*. If a curator must price, monitor and approve each
use, cognitive cost returns on the supply side and the whole argument collapses.

The answer: the seller sets a policy once and metering runs underneath. Same move
as the agent's mandate — constraints on who may invoke, for what purpose, at what
price, under what terms. The human makes one decision about a class of
transactions, not a decision per transaction. (Deployed: WP-A's author sets
`unit_price` in the signed policy artifact once; every retrieval settles
deterministically — "no subscription, no advertising, no audience required.")

This objection is obvious and a reviewer will raise it. Answer it in the first ten
pages.

## Structure

1. *Micropayments Never Worked.* The fact, the diagnosis, the non-transferability.
   Metered pricing that already works and isn't called micropayment.
2. *The Seller's Problem.* Cognitive cost on the supply side; policy set once,
   metered underneath.
3. *The Knowledge Stream.* Curation as an asset. A stream is a mandate with
   content: what it contains, who may invoke it, at what price, with what
   attribution. Metered input into another stream or model. The economic unit is
   not the document and not the knowledge — it is the invocation that produced a
   decision. (Deployed: WP-A's depth multiplier — `Billable_Units =
   depth_multiplier × Σ(similarity_score_i × token_weight_i)` — pays for *grounded*
   contribution: "thinking that actually grounded the output earns more than
   thinking that was retrieved and ignored." This is "evidence is what gets priced"
   made mechanical.)
4. *What Makes It Licensable.* Three conditions: the invocation is determined
   before it commits, witnessed by a disinterested party, and version-bound.
   Without all three, a stream is publishing, not licensing, and the value accrues
   to whoever copies it.

**Interlude — São Paulo.** *(Moved here from Paper 6; it is Paper 7's thesis, not
Paper 6's closing illustration.)* The crop insurer, nineteen hours, 640,000
invocations, 31,000 euros total. The actuary in Toronto earns 2,400 from an
eleven-year-old method and finds out on Thursday. Determination at each model
holder's own boundary — 640,000 determinations in 640,000 places, each protecting
a different owner's asset.

5. *Employment Unbundled.* The handbook assumed buying time bought all of it.
   That assumption was never tested because output was unmeasurable and time was
   the only proxy. Equifax 2022 — Business Insider, 12 October 2022: 24 fired of
   25 investigated, 1,000+ employee and contractor records reviewed via The Work
   Number plus VPN usage and manager feedback, hunting overlapping pay periods;
   "Project Home Alone" / "Project Page 12"; ~$3.2M payroll savings. **[FIXED —
   nuances:]** one of the 25 survived; contractors were swept in too. Two real
   points: (a) the only existing cross-firm work record is held by a credit bureau
   with no relationship to the worker; (b) the fact that mattered was invisible
   from inside any single employer — **disjointness forced not by falsification
   risk but because the fact only exists at a vantage point no participant
   occupies.** Second, independent reason for the witness. *Use the Equifax
   figures; drop the unsourced Rachel Dorn anecdote.*
6. *The Transitional Class.* Hyper-productive knowledge workers already operating
   as multi-client service providers while contracted as exclusive employees. The
   form hasn't caught up to the substance. These are the first to be paid for
   witnessed output rather than presence — precisely because presence was never
   what the employer was buying.
7. *The Interpretive Class.* Position versus judgment. Those whose economic
   standing rests on being the required intermediary between knowledge and a
   decision. Susskind & Susskind (2015), *The Future of the Professions* (OUP) —
   algorithmic automation targets credentialed knowledge professionals, not only
   manual workers. The consultancy at a third its size: it lost assembly, not
   analysis. **The actuary did better than the consultancy. He held judgment.
   They held position.**
8. *Aggregate Gain, Local Devastation.* Historically compatible, and the actual
   result. Allen on Engels' Pause (2007 working paper; 2009 *Explorations in
   Economic History*); Mokyr (1988), Crafts (1985), Feinstein (1998); Acemoglu &
   Restrepo on displacement vs reinstatement (*JEP* 2019); Autor on polarisation
   (Autor & Dorn, *AER* 2013; Autor, Levy & Murnane, *QJE* 2003). No
   quantification, no forecasts — mechanism and historical shape only. Hand-loom
   weavers were not retrained (note: the decline took ~50 years — one word of
   pacing honesty); their children entered a different economy; aggregate output
   rose throughout.
9. *What This Paper Cannot Answer.* The professions were an accountability
   technology, workable because judgment was inseparable from a person — licence
   the person, sue the person, strike them off. Separation ends that. Handoff to
   Paper Zero without pre-empting it.

## Licensing-economics literature — the gap is closed (summary)

Full list with relevance notes in thread memory. Load-bearing items for Parts 3–4:
- **Live per-use precedents (feature prominently):** TollBit (bot/agent paywall,
  per-request publisher-set pricing); x402 (Coinbase, HTTP 402 per-request
  payments, live); Cloudflare "Pay Per Crawl" (closed beta, Jul 2025); ProRata.ai
  (Bill Gross; attribution-based publisher revenue splits — closest operational
  cousin of "invocation that produced a decision"); RSL Collective.
- **The "before" state (frame as what per-invocation licensing supersedes):**
  Reddit/Google (~$60M/yr), Reddit/OpenAI (~$70M/yr), News Corp/OpenAI (>$250M/
  5yr), Shutterstock/OpenAI ($104M AI-data licensing in 2023), AP, FT, Axel
  Springer — ALL flat/annual corpus licenses, none per-use. Cite as the
  pre-metering market, never as examples of metering.
- **Pricing machinery:** MPEG LA / Via LA patent pools (free-tier + tiered
  per-unit royalties — the pricing shape Paper 7 proposes); ASCAP/BMI blanket
  licensing (blanket = prepaid cap, allocation usage-metered); Spotify
  streamshare (NO fixed per-stream rate — $0.003–$0.005 is an emergent average;
  do not print as a price list); Getty rights-managed per-use pricing.
- **Academic:** Balasubramanian et al. (2015), *Marketing Science* — pay-per-use
  vs outright sale of information goods, pay-per-use generally dominates under
  usage uncertainty (directly on point); Pei et al. (2020/2021) data-pricing
  survey; Arrieta-Ibarra et al. (2018), "Should We Treat Data as Labor?";
  Posner & Weyl, *Radical Markets* (2018), ch. 5; Shapiro & Varian, *Information
  Rules* (1999); Admati & Pfleiderer (1990), *Econometrica*.

## Open questions

**Custody and portability.** A longitudinal capability record is categorically
different from a machine-action record: it observes a person over years. Who holds
it, who queries it, what she can see, what she can move, what happens to a failed
assessment from when she was nineteen. **Portability is the property that
distinguishes an asset from a dossier.** If the platform holds it, the closed-
platform objection eats the argument. The Work Number is the counterexample a
reviewer will raise — name it first.

**The witness does not do matching.** Cross-referencing capability against
employment history and project outcomes is *inference*, and inference about a
person can harm them. The witness produces facts; a separate system reasons over
them. Same disjointness rule as settlement and valuation, with more force because
the subject is a person.

---

## Embarrassment-risk checklist (check before any draft ships)

1. Shirky 2003, not 2000.
2. Szabo: both essays, full titles.
3. Millicent: mid-1990s, not 1999.
4. "Collapsing any two made the network uninsurable" — unsourced; relabel or cut.
5. Fundstrat/Virtuals — disclose commissioned research; no Lee endorsement; date PMF.
6. PFMI — main text (Principle 12), not Annex D.
7. Tesla — State National fronting; no per-driver telemetry at launch.
8. 1–3% — MICRO 2014 simulated hardware validator; scope caveat mandatory.
9. Spotify "rate" is emergent, not a price list.
10. Training-data deals are flat-rate — frame as pre-metering state.
11. WP-A price-in-kernel tension (unit_price in the policy artifact vs the
    price-outside-the-kernel doctrine) — unresolved; reconcile before quoting.
12. Equifax nuances: 24 of 25; contractors included.

---

## Enterprise opportunities — the "flip it to the head of product" layer

Paper 6 is the enterprise paper. Each opportunity below is drawn from the author's
own Substack archive (Jan–Mar 2026, the 512/CVS doctrine era), with the testable
metric attached. Full inventory: ~/workspace/your_files/substack-post-inventory.md.

**For the CFO:**
1. *Kill the fraud tax.* Card fraud >$30B/yr; chargebacks $2.40–$4.00 each;
   proof-based authorization at <10μs vs 130ms card auth ("Identity Theft and
   Credit Card Fraud Persist Because Authorization Is Interpretive," Feb 26).
   Testable: fraud loss rate before/after.
2. *Improper payments.* GAO $247B/yr in federal improper payments — money that
   cleared before proof existed; the 10-millisecond Treasury problem ("The U.S.
   Treasury Is the Settlement Layer of the State," Feb 25). Testable:
   improper-payment rate.
3. *Sub-cent settlement economics.* Visa's $0.30 floor vs $0.00063 per retrieval;
   XRPL $0.00001/tx and 3–5s finality; 1M receipts anchored <$100/month ("XRPL
   as a Settlement Anchor," Feb 13; "Monetising Vectorised Intelligence," Feb 3).
   Testable: cost per settled micro-transaction.

**For the CEO:**
4. *The commit layer is the last defensible position.* Intelligence commoditizes;
   authority doesn't. Enterprise AI procurement stalls on undefined liability;
   insurers are already excluding AI (Berkley Absolute AI Exclusion, AIG, ISO)
   ("AGI Becomes a Product the Moment Execution Has a Boundary," Feb 20).
   Testable: procurement cycle time; deals blocked on liability.
5. *Insurability unlocks capital.* Capital flows to what is insurable: Lloyd's
   coffee house (1688) unlocked maritime trade; Munich Re (1880) unlocked 600%
   U.S. manufacturing growth 1880–1910; modern project finance needs $250M+
   insurance before debt deploys ("The Insurance Blind Spot," Feb 4). Testable:
   cost and availability of coverage.
6. *The 2028 bifurcation.* The market splits into evidenced vs unevidenced
   systems; carriers without 2–3 years of clean evidence history face 40–60%
   higher transaction costs — "the reputation moat is forming now" ("Why AI
   Agents Will Be Uninsurable," Feb 12; "Why the Evidence Sidecar Solves What
   'AI Governance Platforms' Cannot," Feb 6). Testable: the spread — Paper 6's
   falsifiable prediction.
7. *Unpriced assets.* ~100B tokens/day touch embedded fragments that never
   compensate their sources; vectorisation severed meaning from ownership
   ("We Accidentally Made Intelligence Free," Feb 10). Testable: retrieval
   revenue per corpus.

**For the CTO:**
8. *The five walls.* Runaway cost and infinite loops; silent guardrail bypass
   under latency pressure; logs that don't explain causality; HITL collapse into
   rubber-stamping; catastrophic one-way actions — each mapped pain → root
   cause → 512 resolution ("The Wall in Agentic Development," Jan 23).
   Testable: incident rate; cost overruns; actions without provable authority.
9. *Execution-domain security.* Agents that act, not just analyze — the
   deterministic remediation boundary; the two executive questions (was the
   action allowed; can we prove it later) ("AI Cybersecurity Agents," Mar 17;
   "Microsoft Warns of 'Double Agent' AI," Mar 16). Testable: mean time to
   prove authorization for any executed action.
10. *The field report.* Pilots rolled back because auditors couldn't approve
    real-time decisions; cost shock from chained tool calls; 2027 is the
    earliest edge becomes investable — "the pacing item is proof, not compute"
    ("The Timeline Collapsed," Feb 3). Testable: pilot-to-production conversion
    rate.

Note: the 2025-era posts (America Ascendant, Canadian politics, markets) are a
separate body and do not feed Paper 6.

## Sequencing to Dec 5

Paper 6 Parts One–Three first (strongest, most defensible, contains the novelty
claim). Paper 6 Parts Four–Five, then Paper 7 drafted against the completed
licensing research above. Forward-binding attestation and selective disclosure now
carry provisional deployed answers — draft them as such rather than as open
wounds.
