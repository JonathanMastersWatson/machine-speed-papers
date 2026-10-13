# Executive Summary — The Execution Surface

*Why Distributed Compute Cannot Be Shared*

**Jonathan M. Watson** — The Machine Speed Papers, No. 5 — Version 1.1 — 2026-07

*Draft — prepared from the paper text for author review and approval. The paper governs in case of any discrepancy.*

---

## A day on the surface

It is 16:00 on a Tuesday and a purchase order commits in two milliseconds. Not in a data centre — in a shop, at a junction cabinet, on hardware nobody in the transaction has ever inspected. The decision was made where the action happened, because there was no time for it to be made anywhere else, and the account of what happened can be checked by a stranger in another city who does not trust the operator.

That is the claim of this paper: a planetary execution surface is being built now, continuously, thickest where consequences happen — and whether it becomes infrastructure or stays private property depends on one thing.

## Thinking, checking, doing

Every device on the surface plays up to four roles, and chip counts are the wrong unit because one device plays several at once. A data source produces an observation. Thinking produces a proposal. Deciding produces an admissibility verdict inside a commit window measured in microseconds. Recording produces an account of what happened that must bracket the commit. Two of the four must be local. Two need not be.

Two populations are emerging and they fail in opposite ways. One decides but cannot be reached — tens of billions of microcontrollers making real decisions at microsecond scale, overwhelmingly un-networked, their rules frozen at manufacture. The other can be reached but mostly does not decide — tens of billions of connected devices streaming telemetry upstream, their rules living on a server a round trip away. What is actually emerging is a third population, growing from both directions: devices that decide acquiring connectivity, and connected devices acquiring local inference. Every segment in this paper lives there, and satisfies two of three requirements. Reachable. Deciding. Not evidenced.

## The hard cases

The field: a sprayer classifying each plant as crop or weed, the whole loop in a quarter of a second, herbicide reduction up to ninety percent — and the characteristic shape of machine-speed failure. Not a dramatic error. A sensitivity setting chosen months earlier, applied perfectly, thousands of times a minute, across seasons, with nobody present at any individual decision. Weed populations compounding silently until control was lost. A record of which setting was in force would have established in month three what took until month eight to notice. It would not have made the setting correct. Nothing at a boundary can establish agronomic judgment; it can only establish what was applied, under what parameters, on whose authority.

The camp: a mining site with no road access five months of the year, running on a rack in a heated container. The satellite link is genuinely good — and nobody imagines running operations over it. The rack decides; the link reports. Connectivity is a reporting channel, not a decision channel. Remote industry arrived at this architecture decades before anyone wrote "edge" in a marketing document, because there was no alternative.

National infrastructure: a fault on a distribution feeder, a gateway tripping a breaker in milliseconds, because a local surge not isolated becomes a regional event. Utilities require distributed energy resources to execute pre-configured fail-safe on loss of communications — deterministic local behaviour as the precondition for admission. Power engineers arrived at the central requirement of this series from a completely different direction and wrote it into their interconnection standards. Water, transit, dispatch, ports — a country's operational infrastructure is becoming a distributed autonomous system, and nobody is assembling it as one.

The home: the segment most people get wrong. Not a box in the basement earning money — that model has been attempted repeatedly and does not work. People are buying local inference for their own reasons: privileged work that cannot leave, token bills that keep rising, and a consumer category forming around a small quiet appliance on a shelf. By unit count this will be the largest segment of the entire surface. By underwriting difficulty it is by far the worst: no operator, no certification, no uptime obligation, and a person who may unplug it to plug in a lamp.

## The telco

One segment was built deliberately, by well-capitalised operators, in the best possible locations, specifically to sell local execution. It did not sell. Seventy-one mobile operators across dozens of countries deployed standalone cores; carriers partnered with equipment vendors and cloud providers to place servers at central offices. Then almost nobody bought it. One national carrier's multi-million-pound edge site, covering a hundred-kilometre radius, was still its only site nearly three years later.

The guarantee covered the wrong thing. A carrier can commit to uptime, power, physical security and data residency — a facility guarantee, genuinely valuable. But a buyer running consequential automation needs something else: what was decided here, under whose authority, against which rule, and can I show that to a regulator. No carrier could offer that, because nothing in the rack produced it. Proximity was solved. Power was solved. Security was solved. Counterparty risk did not exist. The market still did not form. Whatever is missing, it is none of those things.

## Nobody builds this to sell compute

Here is the mechanical fact that explains everything: nobody deploys this hardware in order to sell capacity. The store node is paid for by egress and shrinkage avoided. The junction cabinet is a line in a capital programme. The factory controller is paid for by downtime it prevents. The vehicle computer is a bill-of-materials item. The lawyer's box is paid for by her token bill and her professional obligation. The justification column never says revenue — except in the one segment that tried it and failed.

Idle capacity is structural, not transitional. Retail load follows footfall, factory load follows shifts, a vehicle spends most of its life parked, a box on a shelf does nothing for twenty-three hours. These are not underperforming assets; they are correctly sized for their owners' peaks, and scale does not fix it — scale multiplies it. Which dissolves the normal objection: utilisation is fatal only when third-party utilisation has to repay the capital. Here it never did.

Where an owner does get value from outside workloads, it arrives third, and the order is not negotiable. First, avoided cost. Second, the owner's own accountability — a node that produces an account of its decisions produces an account of the owner's decisions, which for a regulated operator may be worth more than any rental income. Third, and only third, anything earned on spare capacity.

The financing shape is the most underrated fact: after the 1996 Telecommunications Act, carriers put over $500 billion of borrowed money into fibre against projected third-party demand, and the builders were destroyed when demand did not arrive on schedule. Every segment here is funded the opposite way — as operating expense and bill of materials across millions of unrelated balance sheets, each justified locally. There is nothing to write down, because nothing was financed against revenue that has not appeared.

## Edge has been tried

Fog computing had the consortium, the reference architecture, the working groups — and was absorbed without adoption. Carrier edge had the facilities — and almost no buyers. Industrial IoT platforms had the capital — and became case studies. Smart city platforms had the pilots — and produced documentation instead of districts. Decentralised compute marketplaces had the auction, enormous supply, and discounts of fifty to eighty percent below cloud rates — and production workloads stayed away, because reliability depended on which provider you landed on and there was no compliance certification, no isolation guarantee, and realised costs ran well above listed prices.

And yet: content-delivery edge compute is one of the largest distributed deployments ever built, with no consortium and no reference architecture — it simply got built and sold. Private on-premises deployment won the enterprise decisively. And every segment in Part Three is a success — in production, at scale, paying for itself.

Sort every item by one question — does it require two parties who do not know each other to trust an execution? The failures all say yes. The successes all say no. Distributed execution does not fail. Markets for distributed execution fail. What has never worked, in more than a decade of well-funded attempts, is getting one party to rely on execution that happened on another party's hardware, in a place they cannot inspect, under conditions they cannot verify.

Why the markets fail is not technical. It is a three-link chain. Uninsurable: no underwriter will write cover for automated decision-making at an unattended location they cannot inspect, on hardware they cannot certify, producing no account of what was decided — not because the risk is large, but because it is unquantifiable. Unfinanceable: large infrastructure is funded through securitised credit, which requires assets that can be insured, valued, and pledged. Unusable by anyone else: capacity that is installed, capable, and idle cannot be sold, because the buyer cannot verify it and nobody will stand behind it.

This problem is old. A cargo owner in the 1700s could not tell a sound hull from a rotten one, so he could not insure the cargo, so he could not risk the trade. The solution was not better ships. It was a classification society: surveyors inspecting vessels against a common standard, underwriters refusing cover on unclassified ships. Shipowners did not submit to survey because it improved their vessels. They submitted because unclassified ships could not get freight. What was certified was the vessel's condition, not the owner's reputation. Trustworthiness of the counterparty was never the missing piece.

## The missing pieces

Five things are missing. There is no exchange — no open market, no price discovery, no signal telling an owner whether their idle box is worth anything. No node can say what it is — push works, pull does not, and there is no vocabulary in which an inventory could be written. Nothing can be priced on the two things that decide whether a node fits a job — latency class and jurisdiction. An agent cannot pay for what it does where it does it — no arrangement lets an agent carry bounded spending authority to the boundary. And underneath all four: there is no way for a stranger to check what happened.

That last one has to bracket the act — what was proposed, what was permitted, what was attempted, what came back, and whether this was a new attempt or a repeat. Producing a record of a decision is straightforward. Producing an account of what actually happened is not, and the second is what anyone relying on it actually needs. And there is a ceiling: an account produced at a boundary attests to observation, not to truth.

## Why the mesh coheres, or doesn't

Drop the four prior papers onto this surface and something striking appears. The grid gateway ramping to a safe output. The safety cabinet the control system cannot write to. The protection relay tripping without consulting anything. Every distributed energy resource executing pre-configured fallback. Silicon shipping pre-certified to functional safety standards. Every one is a deterministic admissibility check at an execution boundary — deterministic, fails safe, unreachable by the thing it governs, small enough to read — and not one of the engineers who built them had read a word about AI governance. They converged anyway.

And the authority is already compiled: nobody approved any individual snow route, but somebody approved the rules, in an office, over weeks, with a version number. Authority does not distribute. It is declared centrally, compiled, and carried — a scoped, expiring, revocable carrier of one permission, to one place, for one period.

The one thing nothing has is the account. Every segment enforces. Not one produces an account somebody else can rely on. And the witness must never gate anything — a witness that can halt production is a new single point of failure, and the first time it stops a line somebody disconnects it. The only witness that survives contact with an operations team is one that cannot cause any. When a contractor unplugs something in the wrong cabinet, the plant keeps treating water, and the record acquires two hours it does not cover. The gap is the output.

None of the three layers works alone. A kernel without a witness is enforcement nobody can verify — the surface exactly as it stands today. A witness without a kernel is a log of things that already happened. Either without compiled policy has nothing to operate on. They are a minimum set, and removing any one collapses the other two.

What the capacity is worth, how latency and jurisdiction would price it, and whether an exchange clears are the questions the companion paper takes up — because metering is not a second system bolted onto the governance layer. It is the governance layer, read for a different purpose.

## Infrastructure or property

Nobody is behaving foolishly. The store owner who will not open his node to strangers is correct. The buyer who will not run production on an unverified box is correct. The underwriter who declines to price the unquantifiable is correct. And the collective outcome is that a genuinely useful capability sits unused. A common interface is worth more than it costs to build, and it still does not get built, because whoever goes first pays for something the rest use free.

Two mechanisms have broken that deadlock historically. The container: worthless unless everyone uses the same one — it broke when Sea-Land released the patented corner casting royalty-free, making the fitting a standard rather than an owned one. The classification society: a party with pricing power refusing to do business with anything unlisted. This surface needs both, and only the format can be published.

The honest caveat: the fragmentation may not be transitional. The mechanism that gets the hardware deployed — vendors building purpose-specific appliances for specific verticals — is also the mechanism that guarantees the result is incompatible. Persistent fragmentation is not an exotic outcome. It is the normal one.

The fork: the surface gets built either way — the silicon arrives on cycles already funded, for reasons already sufficient. What is open is who can use it. Without a way to check execution at an unverified location, every organisation large enough to buy its own hardware will have a machine-speed economy, and everyone else will rent human-speed access to somebody else's. With it, the same hardware becomes something closer to a utility. The difference is not more silicon, faster networks, better models, or larger capital programmes. It is whether a stranger can check what happened.
