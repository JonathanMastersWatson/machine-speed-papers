# Executive Summary — Upstream

*Where Human-in-the-Loop Goes at Machine Speed*

**Jonathan M. Watson** — The Machine Speed Papers, No. 4 — Version 1.1 — 2026-07

*Draft — prepared from the paper text for author review and approval. The paper governs in case of any discrepancy.*

---

## Four thousand years of deciding afterwards

Around 2100 BC, a scribe in Ur pressed rules into wet clay: if a man knocks out another man's tooth, he pays two shekels. The list was already incomplete on the day it was written — no list of situations covers the situations — so somebody had to decide, a person, in a room, after the fact. Four thousand years later we are still doing it. Contracts are interpreted when disputed, not when signed. Accounts are audited after the year closes. Courts operate entirely in the past tense.

That is not a flaw in the design. It is the design. Ambiguity is permitted at the moment of action, and resolved at leisure by someone with standing. It produced entire professions whose expertise is precisely this: reading what was written, deciding what it meant, long after the event.

Machine-speed execution does not remove the review. It removes the interval the review lives in. There is no later. A system that cannot resolve ambiguity afterwards has to eliminate it beforehand. That is the shift, and every consequence in this paper falls out of it.

## What a rule has to become

A rule a machine can enforce has to answer six questions, and the paper derives them rather than choosing them. What exactly is being proposed — name the action, not the area. What does the rule actually say, in terms a machine can test — a number, a set, a list, a match. Who is allowed to do this — with a record that exists and is current. Can the check finish in time — every lookup returning, inside the window, every time. What comes out, and does it bind — if the system can carry on regardless of the answer, no rule was enforced. And what happens when this cannot be evaluated — because the authority record will be down, the lookup will time out, and whether the business stops or proceeds is a decision at the level of the person who owns the consequence.

A rule is compiled when all six are answered. There is no partial credit. Compilation is not the same as the decision at the gate: the gate fires in milliseconds, thousands of times a day, with nobody present; compilation happens once, upstream, over weeks, with people in a room disagreeing.

There is also a ten-minute screen that finds most of the same problems. Print the policy. Highlight every word that came into English from Norman French or Latin — appropriate, material, reasonable, excessive, necessary. Those highlights are your ambiguity, nearly every time. The words that compile are the old ones describing physical acts with visible actors: hold, stop, send, pay, who signs. The words that fail arrived with lawyers and administrators after 1066, built to describe delegated authority at a distance, deliberately broad enough to cover cases nobody could list in advance. That breadth was the point — it is how a policy survives contact with situations its author never imagined — and it is exactly what a machine cannot use.

## What happens to ten thousand policies

Run the six questions across a corpus and you get a funnel. Ten thousand policy statements go in; roughly two thousand executable rules come out. The figures are illustrative — no organisation has yet published measured attrition — but the direction is solid, and everything that fell out is the actual work. Each stage routes to a different owner: values statements back to the business owner, untestable judgment terms to whoever owns the standard, missing authority to Legal, unbounded checks to Engineering, advisory non-rules back to the business, and the empty failure-behaviour box to whoever carries the consequence — often the board.

Not one of those owners is a technology team.

The losses are the product. The funnel found every place where the organisation's rules were ambiguous and named the ambiguity. It found every place where nobody knew who was in charge and forced an answer. It found the rules that had quietly stopped applying years ago, and the exception pathways governing real decisions while existing in no document. The organisation was already running on ambiguous authority and undocumented practice. It was simply doing so without a record. This is a governance modernisation programme that produces executable rules as a by-product — and the by-product is the smaller half of the value.

One figure comes out of all this for the board: of the policies governing what our agents are permitted to do, this many are executable. Here is what blocks the rest, and whose desk each blockage sits on. That is a coverage figure — measurable, moving quarter over quarter, and the only honest answer to the question the insurer and the regulator are already asking.

## Four weeks and four milliseconds

A health insurer processes claims against a benefit table. A new treatment code arrives that is not in the table. An assessor finds the nearest thing that is and processes under that — ninety seconds, no record that a judgment occurred. Nobody did anything wrong; it is how the department worked for a decade. It had simply never been written down, because nothing ever required it to be.

Deploy agents on forty thousand claims a day and the sentence they work from — approve routine claims up to the standard limit — fails three of the six questions. What counts as routine? Who is allowed to decide a mapping? What happens when the benefit system is unreachable? Four weeks of workshops settled it: mappings defined in advance by medical coding, routine defined by exclusion, and the COO deciding that when the system is unreachable, everything stops.

Twenty-two lines of compiled rule. Four weeks to write them — spent discovering that a large insurer did not know who was allowed to decide what a treatment was equivalent to, and had been running on that gap, successfully, for over a decade. The governance then takes under two milliseconds, forty thousand times a day. The cost is entirely upstream: four weeks of expensive human argument, then a permanent asset that costs almost nothing to run.

## Both halves, permanently

Today's claims floor already decides most claims without a person reading them — machine-speed adjudication is not coming, it has been here for years — but the record shows only that claims cleared, not the decisions that produced them. After compilation, most claims still clear without a person, and the record shows which rule matched, which conditions were satisfied, what authority the agent held, and what the gate decided. Same volume of unattended decisions. Entirely different question answerable afterwards.

It does not end with the exception queue shrinking to nothing, because adjudication cost falling toward zero drops the floor under which insurance products can exist — Jevons' paradox — and the new products each need their own rules, limits, exclusions, and failure behaviour. The better compilation gets, the more governance the business generates. The compilation function is not a project that finishes. It is standing capacity, sized for a corpus that has not been written yet, covering products nobody has invented.

And the line between the two halves moves but never closes. Some of the exception queue is routed to humans on purpose — deciding one treatment is equivalent to another is a clinical judgment the organisation chose not to hand to a machine. That routing does not expire.

The dangerous half: once most volume flows through the gate without incident, attention follows the volume — while every hard case in the business concentrates into the smallest team, and nobody is watching them. The gate will be fine. The risk moved to where people are still deciding.

## The morning the table went down

The benefit table stops responding at 09:14 on a Tuesday. The gate cannot evaluate. It stops — eleven thousand claims held in thirty-three minutes — because the COO decided four weeks earlier, in a room, that stop was the behaviour. The chaos is the policy working. The record shows exactly what was ungoverned, for how long, and what was done about it.

Two years earlier, the same outage: assessors worked from memory for thirty-three minutes, most of them right, some not. Nothing flagged. Ask six months later which claims were paid during those minutes and nobody can tell you — not because someone is hiding it, but because the question was never capable of being answered. One morning was loud and left a complete record. The other was quiet and left nothing. The quiet one is the dangerous one, and that is the whole point of the sixth question.

Stopping is not the only right answer — a grid continues in a restricted mode, an interlock fails to a safe state — and anyone claiming governed systems must universally fail one way has not looked at more than one industry. What is universal underneath: the behaviour was decided in advance, by someone with standing, the machine does not invent authority, authority resolves somewhere specific, and the transition is recorded. Declared Failure Sovereignty.

## The people who move upstream

Liz has twenty-two years of knowing which treatments can stand in for which. None of it is written down. Ask her how she decides and you get "well, it depends," followed by four examples and an exception to the third. That is what expertise looks like from the inside, in every field — and it is exactly what the compilation programme needs, because the knowledge is nowhere else.

Every previous automation wave displaced the experienced first. This one runs the other way, for a structural reason: the scarce input is knowledge that exists in no document, and only the people holding it can supply it. The junior analyst can operate the tooling. The junior analyst cannot answer question three.

Three roles emerge. The Domain Authority holds the knowledge and has standing to say what the answer is. The Constraint Architect knows what the six questions require and how to extract an answer that will hold — part analyst, part interviewer, part draftsman, constitutionally capable of asking the same question a fourth time when the room wants to move on. The authority holder decides when the room disagrees. Notice who is absent: nobody in that list is writing code. The engineering is downstream and comparatively trivial.

The honest part about headcount: this paper will not tell you automation preserves jobs. Two hundred and twenty assessors became thirty, plus a handful upstream, and that reduction is permanent. What changed for the ones who remain is the weight of each decision — Liz's judgment, written down once and applied to every claim that follows, is wrong at volume for months if she gets it wrong, with her name on the document. Fewer people. Much more consequence each.

And the window is demographic, not technological. The knowledge leaves when the person does. An organisation that starts this work while its experienced cohort is still employed can extract what they know. One that starts ten years from now will find its rules cannot be reconstructed. The tooling will improve. Liz will not still be there.

## What you actually bought

Four weeks for one rule, two hundred rules, a year of expensive people's time. The natural way to book that is project cost. That is the wrong way to think about it. At the end of that year the organisation possesses something it did not possess before: a written, current, authoritative statement of what it will and will not do, in a form that can be enforced without asking anyone. It persists, it compounds — the fiftieth rule costs a fraction of the first — and it transfers, because it is written against what every gate requires rather than against a vendor. The most valuable durable thing the programme produces will not appear anywhere in the financial statements, which is precisely why it gets underfunded.

## The new compliance officer

Eighteen months in, the corpus is running, and the new Head of Compliance arrives with a list: flag anything unusual, check every claim against the sanctions feed, flag high-value claims for review but let them proceed. Three reasonable requests, three different failures — untestable, unbounded, non-binding. Add them anyway and the corpus quietly stops being decisions made by people with authority and becomes a mixture of those and defaults chosen by whoever was implementing that week. The corpus does not decay through neglect. It decays through accumulation.

So nothing gets rejected; everything gets converted, and the conversion is the Constraint Architect's job — which is why the role is permanent rather than a project appointment. An organisation that funds the programme and not the function has bought an asset with no maintenance.

## Where the value actually sits

The gate is where the technology is. The corpus is where the value is. Convergent architecture commoditises: independent teams reaching the same design means the problem admits one answer, and designs that fall out of the situation get implemented repeatedly, standardised, and shipped as a feature nobody pays separately for. The insurer's two hundred and forty rules are the opposite of convergent — specific, accumulated, costly to reproduce, compounding, non-transferable. Whoever holds the corpus holds the customer.

Three businesses, not one: discovery — getting Liz in a room, billed by the day, the largest of the three by revenue; the platform — the system of record for compiled governance, durable because the corpus accumulates inside it; and assurance — independent verification that a corpus is what it claims to be, which does not exist yet and will be created the way SOC 2 was, by a buyer refusing to accept the seller's word.

## What would actually falsify this

An institution of real size that compiled its full governance corpus and held that state through a normal year. A seventh load-bearing requirement. Corpus attrition data showing the funnel does not narrow. A compilation platform that resolves ambiguity without human authority, defensibly. None has been tested, because the assessment is new. All four are testable by anyone willing to do the work.

## The one-sentence version

For four thousand years we wrote rules that a person would interpret afterwards, and built our institutions and our professions around the interpreting. There is no afterwards now. The interpretation has to happen first, in a room, before the case exists — which is harder, and slower, and requires exactly the people every previous wave of automation let go. It never finishes. That is not the problem with it. It is what makes it a profession.
