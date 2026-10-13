---
title: "The Execution Surface"
subtitle: "Why Distributed Compute Cannot Be Shared"
paper_number: 5
version: "1.1"
author: "Jonathan M. Watson"
date: "2026-10"
series: "The Machine Speed Papers"
canonical_pdf: "paper.pdf"
license: "CC-BY-4.0"
---

# The Execution Surface

*Why Distributed Compute Cannot Be Shared*

**Jonathan M. Watson** — The Machine Speed Papers, No. 5 — Version 1.1 — 2026-10

---

*Machine-readable text derived from the canonical PDF (`paper.pdf`). In case of any discrepancy, the PDF governs.*

## Abstract

Compute is moving outward. That argument is over, and this paper does not make it.
It starts from the condition itself and asks what kind of thing is being built.
The answer is a planetary execution surface: a continuous layer of local compute running from gigawatt campuses down to milliwatt endpoints, thickest wherever consequences occur. It is being assembled now, segment by segment, by thousands of unrelated parties — municipalities meeting statutory duties, retailers avoiding bandwidth
costs, manufacturers preventing downtime, remote operators with no alternative, and
professionals who cannot send confidential work to somebody else’s model.
Four findings follow from describing it rather than arguing for it.
First, nobody deploys any of this hardware in order to sell compute. Every box is paid
for by a cost avoided or an obligation met, so the capital is not speculative and the
surface cannot crash the way the fibre build-out crashed. Spare capacity is a byproduct,
and there is an enormous amount of it, because every node is sized for its owner’s peak
and peaks are brief.
Second, distributed execution does not fail — markets for distributed execution fail. A
decade of well-funded attempts splits on one question: did the arrangement require
somebody to rely on work done inside a stranger’s machine? Every failure did. Every
success had a single owner holding both the hardware and the workload.
Third, two experiments have already tested this at scale, from opposite directions. Carrier edge computing had the best-sited facilities, trusted operators and no counterparty
risk, and no market formed. Decentralised compute marketplaces had auctions, enormous supply and discounts of fifty to eighty percent, and production work stayed away.
Each diagnosed a different missing piece and each built it. Neither could tell a buyer
what had happened inside the machine.
Fourth, the surface becomes a mesh only when three layers are present — the three the
earlier papers in this series derived independently. People compile policy upstream.
A deterministic Executable Governance Kernel sits at the boundary. An independent
witness runs alongside it. The relationship between the last two is specific and easy to
invert: the kernel decides whether an action may proceed, the witness records what
it can observe, and the witness never gates anything. Without all three, density is not
connection, and what remains is a very large number of capable machines each serving
one party.
The paper stops at that gap. What closing it would be worth, how such capacity would
be priced, and whether a market for it clears are the subject of the companion paper on
machine economics.

Preliminaries
Vocabulary note. This paper uses the terminology established across Papers 1–4 of this
series: execution boundary, Executable Governance Kernel (EGK), admissibility, independent witness, policy compilation, Compiled Region. It names no implementation of
any of them. An EGK is an architectural category in the way a firewall or a hypervisor
is a category; the paper argues the category is necessary and says nothing about which
one.
Prior papers in this series. All four are posted and publicly available.
   1. Watson, J. M. (2026).       Execution-Boundary Governance: A Runtime Control Model for Autonomous Systems.        SSRN Working Paper No. 7034678.
      https://ssrn.com/abstract=7034678
   2. Watson, J. M. (2026). Constitutional Compression: The Emergence of Minimal Governance at Machine Speed. SSRN Working Paper No. 7199200. https://ssrn.com/abstract=7199200
   3. Watson, J. M. (2026). Evidence Systems: Why Independent Witnesses Emerge at Machine Speed. SSRN Working Paper No. 7207219. https://ssrn.com/abstract=7207219
   4. Watson, J. M. (2026). Upstream: Where Human-in-the-Loop Goes at Machine Speed.
      SSRN Working Paper No. 7211100. https://ssrn.com/abstract=7211100

PART ONE — 2035

## Chapter 1 — A Day on the Surface

It is a Tuesday in March, in a city of about four hundred thousand people. Nothing
unusual happens.
Watch the silicon rather than the people.

04:50. In a municipal depot on the west side, a 2U short-depth box in a wall-mount cabinet finishes assigning the night’s snow routes. Two accelerators, about seven hundred
watts, bought on a capital line that also covered the salt shed roof.
It has been working since one in the morning. A model runs on it — a few billion parameters, compressed to fit — reading plough positions, salt inventory at three depots,
road temperature from sixty sensors, a gradient where the surface is refreezing, and a
list of school zones that have to be clear by seven. It has proposed and revised the plan
eleven times as conditions moved.
Each time it settles, something else happens. A different part of the same box takes the
plan and does something with it: opens a connection to the fleet system, writes twentythree route assignments, waits for acknowledgement, retries two that failed, and updates a record.
Nobody approved any individual decision. Somebody approved the rules in October
— and whether tonight’s plan came from that version or the amendment in January is
not something the depot can now establish.

05:40. A tram leaves the depot. Behind the driver’s cab there is a sealed fanless module
on an anti-vibration mount, conduction-cooled, rated for the temperature range the
tram sees in February.
Over nineteen hours that module will make several million decisions. A small vision
model watches the doorways and estimates crowd density, and the dwell time at each
stop stretches or shortens accordingly. Another model watches wheel slip on a wet
grade and adjusts traction. A third handles the door interlock — and when it says the
door may open, the actual opening is a signal on a wire, sent by an ordinary processor,
in microseconds.

At 06:02 the tram requests priority at a junction. The request goes to a cabinet at the
intersection, eleven metres away, where another box is weighing it against an ambulance eleven blocks out and a pedestrian phase that a sensor says is occupied. That box
decides in four milliseconds and changes the light.
None of these decisions is interesting. Every one of them commits before a person could
read a sentence describing it.

06:15. At a water treatment plant on the east side, a valve closes.
Chlorine residual in the north distribution zone drifted 0.1 mg/L low overnight. A
model on a 4U in the control room has been watching the trend for two hours against
flow, temperature and the pattern of the last nine Tuesdays. It concludes the dosing
should come up four percent.
That conclusion is a number. Closing the valve is eleven instructions to a controller
down the corridor, executed by a CPU with no model in it.
The plant’s recorder was offline for two hours that morning. A contractor had unplugged something in the wrong cabinet. The dosing change is in the record; the two
hours before it are not, and never will be. Nobody tried to fill them in.
The operator on shift sees a line on a screen turn from amber to green. He did not decide
anything. He is there in case something happens the rules do not cover.

07:15. A coffee chain’s morning peak starts.
In each store there is a 2U short-depth server in the comms cupboard behind the counter
— two accelerators, four hundred watts, air-cooled by a cupboard fan that somebody
has to clean twice a year. On it, a model watches the drive-thru queue through two
cameras and predicts order composition four minutes ahead — more hot drinks than
yesterday, the weather is worse — and the brewing schedule moves ahead of the queue
rather than behind it. The same box watches a refrigeration unit whose temperature
curve is drifting, and flags it. It applies an eligibility rule to a promotional discount
and declines it.
At 07:40 it revises the afternoon labour schedule down by one shift. Footfall is tracking
eight percent below the same Tuesday last month.
At 07:50 it buys things.
This is the moment worth slowing down for, because it is where the two halves of the
machine become visible.

The model decides what to order. More oat milk, less whole, an extra case of the seasonal syrup because this store is selling through faster than the regional forecast assumed. That is thinking. It runs on the part of the chip built for models, takes about
two hundred milliseconds, and produces a list.
Then the agent places the order, and placing it is nothing like thinking. It authenticates
against the supplier’s system. It fetches the current catalogue. It checks three items
against contracted prices. It discovers one is on allocation and substitutes. It assembles
a purchase order. It validates the total against its own spending limit. It submits. It
handles a timeout and resubmits. It confirms. It writes the result to the store’s inventory
record and to the regional ledger.
Notice what went wrong in the middle of that, twice. An item was on allocation, so
the agent picked something else. A submission timed out, so the agent sent it again.
Neither of those was in the plan, and both were checked before they went out — a
substitution is a different purchase, and a resend is a new attempt.
What nobody can now say for certain is whether the store bought one case of syrup or
two. The order system says one. The supplier’s system may say two. The record shows
two attempts and one confirmation, which is exactly as much as anything local could
honestly establish. It will be settled next month, by a person, from invoices.
Eleven calls, each one a few microseconds of work on an ordinary processor — the
same kind of chip that has been in every computer for forty years. No model involved
in any of them. And eleven separate moments where something irreversible could have
happened for the wrong reason.
The thinking is the expensive part. The doing is the consequential part. They run
on different chips.
Eleven thousand stores. The decisions are made in the store because sending forty camera streams to a distant data centre and back costs more than the hardware did, and
because a supply decision made three hours later is a supply decision about yesterday.

09:00. An insurer’s claims system approves a payout.
A model reads the claim, the policy, the adjuster’s photographs and the repair estimate,
and proposes approval.
Then the determination. Not an evaluation of the policy — that was done months ago,
upstream, by people. What happens here is a handful of structural checks against the
instrument the agent is carrying: is this authority valid, is this action inside its scope,
has it expired, is this the version in force. Four hundred microseconds. The same checks,
in the same order, as every other claim that morning.
Then the commit: a row is written, a payment instruction is queued, a file is closed.
What was determined, and what was attempted, go to a recorder under separate authority from the claims platform — different keys, different storage, and no path back
in.

The claimant will see the money on Thursday. She will never know that the part which
could have been wrong was already over before she refreshed the page, or that if this
is ever disputed, the dispute will be about those few lines.

10:20. On a factory floor two hundred kilometres north, a robot arm reaches a decision
point.
A vision model on an industrial computer at the cell has classified a part as within
tolerance. It ran in six milliseconds on hardware in a cabinet four metres from the arm.
Then the arm’s controller commits. Current flows to the servo. The gripper closes. The
part goes to the line rather than the reject bin.
That commit takes microseconds and it is the moment authority actually lands — not
when the model classified the part, but when the motor moved. Before that instant
everything was a proposal and could be revoked for free. After it, a physical object is
somewhere else and the world has changed.
The cell’s safety logic sits in a separate cabinet, on a different network, with its own
power supply, and the control system cannot write to it. That separation is not a design
choice. A certification body required it, decades before anyone put a model in a factory.
Four hundred metres away, a valve on a coolant loop opens on the same kind of decision.
Nobody is in the building. The plant runs itself until eleven, when a maintenance crew
arrives.

11:20. A sprayer moves down a field at working speed.
On the boom there are twelve cameras and a compute module rated for vibration and
dust. A model classifies each plant as crop or weed. Then a solenoid fires, or does not
— a signal on a wire, from a microcontroller, in microseconds.
The whole loop takes about a quarter of a second, because that is the time available
before the plant is behind the machine. Thousands of decisions a minute, each one
committing chemical or withholding it.
Nothing records which sensitivity setting was in force this morning. Eight months from
now, somebody will want to know.

11:20, six hundred kilometres north. At a mining camp with no road in for five months
of the year, a rack in a heated shipping container runs the site.

Half a dozen models share the hardware. Haul truck routing. Ventilation on demand
from air quality and crew positions. Pump scheduling. Ore grade classification from a
conveyor camera. Crew rostering against a helicopter window.
And in between all of them, thousands of ordinary calls a minute: read a sensor, write
a setpoint, log a state change, acknowledge a controller, update a manifest. The models
decide. The processor beside them acts.
The camp has a satellite link and it is genuinely good — enough for email, telemetry,
and model updates. It is not good enough to run any of the above, and nobody involved
pretends otherwise.
The rack decides. The link reports.
The recorder in the corner has been writing since the link last cleared, eleven days ago,
and will keep writing whether or not it clears again this week. Nothing it holds is for
the camp. It is for the insurer, and for the arbitration in four years that nobody expects
and everybody budgets for.

16:00. A distribution agent commits a purchase against a supplier it has never dealt
with.
The reasoning took four seconds across nine model calls, and most of it was not about
price. Is this supplier real. Do the terms match what was quoted. Is the lead time
plausible for this part in this season. The model formed a view and the view was a
judgment, not a lookup.
The commitment took thirty-one tool calls and about two milliseconds of processor
time. Six of those calls were consequential enough to be checked — the spend, the
commitment, the ledger write, three others. Each check took under ten microseconds,
because the agent was not asking anyone’s permission. It was carrying it.
The authority had been granted three weeks earlier by a person now asleep in another
time zone, and compiled into the instrument the agent holds: scoped to a category,
capped at an amount, expiring on the thirtieth, version stamped. The boundary reads
it and answers. Nothing leaves the building to find out.
Which is the only reason any of this fits in two milliseconds. Ask a central service six
times and the task spends half a second waiting on a network, on a machine that had
the answer the whole time.

17:45. A lawyer in a converted bedroom asks a question about a client file.
The model answering runs on a box on the shelf behind her, about the size of two hardcover books. She bought it eighteen months ago for two reasons. The work is privileged

and it cannot go to somebody else’s model. And she was spending four hundred dollars
a month on tokens for work a small local model handles adequately.
The box is busy for ninety seconds. It will be idle for the rest of the evening, as it was
for most of the day.

22:40. A fault appears on a distribution feeder.
There is no model in this one. A gateway at the substation runs a detection algorithm
that has been in service for a decade. It recognises the signature and trips a breaker in
milliseconds, because the alternative is a local surge propagating into something larger.
Nobody is consulted. Nobody could have been.
It is also the only decision in this entire day that anyone could fully defend afterwards.
The rule was written by engineers, certified before it was allowed near the grid, and
has not changed since. Ask what it did and why, and there is an answer — not a reconstruction, an answer.
The claim and the purchase can each establish what they were authorised to do, and
what they attempted. Neither can establish whether the judgment behind it was sound.
The supply order cannot establish what actually happened at the supplier’s end at all.
And the snow routes and the sprayer cannot establish anything.
Four different kinds of not-knowing, and only one of them is solved.

23:55. In driveways and parking structures across the city, a few thousand vehicles sit
charging.
Each one carries more processing power than the city’s entire municipal IT estate did
in 2020. They have been parked, on average, for nineteen of the last twenty-four hours.
They are doing nothing at all.

By midnight the city has executed somewhere on the order of a billion consequential
decisions.
Almost all of them were thought about within a few kilometres of where they landed.
Almost all of them were committed within metres.
A small fraction of them left behind something a stranger could read.

## Chapter 2 — What You Just Looked At

Nothing in that day requires an invention.
Every component of it exists now, in production, somewhere. The tram module, the
junction cabinet, the store server, the sprayer boom, the substation gateway, the camp
rack, the vehicle, the box on the shelf. What 2035 adds is density and ordinariness, not
novelty. The trend lines are measurable today; the claim is only that they do not stop.
One caveat about the numbers. The timings — four hundred microseconds for a determination, under ten microseconds for a carried check, two milliseconds for thirty-one
calls — are architectural targets consistent with what deterministic logic on ordinary
processors can do. They are not benchmarks of a deployed system, because no such
system has been benchmarked. They describe the envelope the design has to fit, not a
measurement taken.

What that day describes
A planetary execution surface — a continuous layer of compute running from gigawatt
campuses down to milliwatt endpoints, thickest wherever consequences happen. Being
built now, by thousands of unrelated parties, for thousands of unrelated reasons, and
almost nobody involved thinks of themselves as building it.
This paper does three things.
It describes that surface, segment by segment: what each part does, what speed it has
to do it at, and who paid for it.
It explains how it gets built, which turns out to be the most interesting mechanical fact
about it. Nobody deploys any of this hardware in order to sell compute. Every box in
Chapter 1 was bought to avoid a cost or meet an obligation. The spare capacity is a
byproduct.
And it names what is missing — because the surface, as it is currently arriving, has
a property nobody planned and nobody wants. Every node serves exactly one party:
whoever installed it.
The paper does not argue that compute is moving outward. That argument is over and
everyone has accepted it. It takes that as the starting condition and asks what kind of
thing is actually being built.
One boundary, stated up front. This paper stops at the description and the gap. What
the missing pieces would be worth, how such capacity would be priced, and how a
market for it might clear are the subject of the companion paper on machine economics.
Here the missing pieces are named, not filled.

The rule the day depends on
One thing that day quietly assumes, and it is worth stating once rather than fourteen
times.
In that world, nothing consequential crosses a boundary unless something local has
determined it admissible first. Reasoning can continue without that. Commitment cannot.
What records the event is a separate matter, and separate in a specific way. It observes; it
does not authorise. When the water plant’s recorder went down, the plant kept treating
water — because a recorder that can halt a treatment plant is a recorder somebody
eventually disables. Execution continued, and the record shows a gap that will still be
a gap in ten years.
Which is the honest arrangement. Something has to say whether an action may proceed. Something else has to say what happened. Confusing the two produces either
a system that stops for the wrong reasons, or a record nobody should believe.
Chapter 12 returns to this, because getting the relationship backwards is the most common error in this area and it has consequences in both directions.

PART TWO — WHY IT HAS TO BE LOCAL

## Chapter 3 — c

Compute is moving outward for many reasons — cost, bandwidth, privacy, sovereignty,
resilience. Most of them are negotiable. One is not, and it explains the shape of everything in Part Three.
Light moves through fibre optic glass at about 200,000 kilometres per second.1 Call
it 200 kilometres per millisecond. A signal going out and coming back covers twice
the distance, so a round trip costs roughly one millisecond per hundred kilometres of
separation.
That is before anything else happens — before the request is queued, before a router
looks at it, before a model runs. It is the floor. It is what you pay for the two ends being
where they are.

                                       Separation      Round trip
                                       5 km            0.05 ms
                                       50 km           0.5 ms
                                       500 km          5 ms
                                       3,000 km        30 ms

Real networks are worse. Switching, queuing and the fact that fibre does not run in
straight lines typically double or triple the theoretical minimum. A 500-kilometre round
trip that should cost 5 milliseconds usually costs 15 to 20.2
Here is why this deserves its own chapter rather than a footnote.
Every other constraint in computing has been beaten. Storage got cheaper by orders
of magnitude. Bandwidth got cheaper by orders of magnitude. Compute per watt
improved relentlessly for fifty years. When something in this field is expensive, the
reliable historical response has been to wait.
Distance does not do this. There is no process node, no architecture, no roadmap that
reduces it. The only variable anyone controls is how far apart the two ends are.
       Corning Incorporated. Corning® SMF-28® Ultra Optical Fiber. Product information PI1424, March
2013. Specifies an effective group index of refraction of 1.4676 at 1310 nm, giving a group velocity of
c/1.4676 ≈ 204,300 km/s; rounded to 200,000 km/s throughout for arithmetic convenience.
       Bozkurt, I. N., Aqeel, W., Bhattacherjee, D., Chandrasekaran, B., Godfrey, P. B., Laughlin, G., Maggs,
B. M., and Singla, A. Dissecting Latency in the Internet’s Fiber Infrastructure. arXiv:1811.10737, November
2018. The standard estimate multiplies line-of-sight distance by approximately 2.1 before converting to
time, to account for the circuitousness of real conduit routes; the authors find shortest-path routing over
the mapped US long-haul conduit network could reduce the median factor to 1.3 using fewer than half
the links. The 2.1 factor is propagation only — it takes a 500 km round trip to roughly 10 ms. The balance
to 15–20 ms is switching, queuing and peering.

An agent is not one decision
All of that would be a minor engineering note if a system made one call and stopped.
Twenty milliseconds on a two-second task is one percent.
But that is not how agents work.
An agent given a goal does not answer it. It works on it. A realistic sequence for something as ordinary as reconciling a delivery discrepancy runs: read the goal, retrieve
the order, look up the shipping record, compare, notice a mismatch, query the carrier,
fetch contract terms, check the terms against the mismatch, decide the discrepancy is
chargeable, look up the supplier account, check the credit limit, draft an adjustment,
validate it against a schedule, check whether the amount exceeds its own authority, log
the reasoning, commit, notify, update, verify the update took.
Nineteen steps, and that is a modest example.3 Complex tasks run to fifty or a hundred.
Each step is sequential, because each depends on the last. The agent cannot check the
credit limit before it knows which supplier.
Now the arithmetic changes. Twenty milliseconds on one call is a rounding error.
Twenty milliseconds on each of twenty sequential calls is four hundred milliseconds
of pure waiting, and if some steps take two round trips — many do — it is worse. The
agent is not slow because it is thinking. It is slow because it keeps stopping to ask.
Latency in an agent does not add. It accumulates in series. That is the difference
between a footnote and a design constraint.

And the authority checks accumulate too
There is a second version of this that almost nobody accounts for, and it is the one that
decides where the checking has to live.
Several steps in that nineteen-step chain are consequential. Drafting an adjustment is
not; committing it is. Looking up a credit limit is not; exceeding it is. Realistically, a task
of that size contains somewhere between three and ten moments where something has
to establish that the agent is permitted to do what it is about to do.
If each of those is a call to a central policy service, each one costs a round trip. Six
checks at twenty milliseconds is a hundred and twenty milliseconds of an agent sitting
still, waiting to be told something about its own authority — and that is on a good
network to a nearby service. On a worse one it is half a second, and on a congested one
it is unbounded.
So the cost of remote authorisation scales with the number of consequential steps, not
with the number of tasks. The busier and more capable the agent, the worse it gets.
There is only one arrangement that escapes this. The agent carries its authority rather
than asking for it. If the permission has already been compiled into an instrument
the agent holds — scoped, capped, dated, versioned — then each check is a local read
     † Empirical evaluations of production agentic frameworks indicate that realistic multi-step autonomous tasks require 15 to 30 sequential tool interactions. No single primary benchmark is cited; the
figure reflects aggregated reporting across production frameworks.

against something already in memory. Microseconds, six times, and nothing leaves the
building.
That is the 16:00 entry in Chapter 1, and it is the reason a purchase involving thirty-one
tool calls can finish in two milliseconds rather than half a second. Chapter 12 returns
to how the instrument gets there.

Improvement everywhere else makes distance worse
There is a consequence of this that points the opposite way from what you would expect.
If a step takes 200 milliseconds of which 20 is network, the network is ten percent of
the problem and nobody thinks about it. If the same step is optimised until it takes 21
milliseconds of which 20 is network, the network is ninety-five percent of the problem.
Nothing about the network changed. Everything else got better, and the fixed term
became the whole answer.
That is precisely what is happening. The industry is compressing every part of the
response except the one part that cannot be compressed: faster interconnects, faster
memory, wider decode, better batching, processors purpose-built for agent workloads.
Each of these is real, and each one makes the geography matter more.

From latency to geography
Because distance is fixed, a latency requirement converts directly into a maximum radius.
A step that must complete a network round trip within 10 milliseconds, allowing for
real-world overhead, cannot be served from more than roughly 300 to 500 kilometres
away. Not expensively. Not with diﬀiculty. It cannot be served at all, at any price, by
any vendor, ever.
And because agents run many steps in series, the radius that matters is not the radius
for one call. It is the radius that keeps the whole chain inside its budget. Tighten the
total and the permitted distance per step collapses.
That is how a question about performance becomes a question about where buildings
are.

“Edge” is a distance, not a place
The word has been used loosely for a decade, almost always to mean “not the cloud.”
That is a definition by exclusion and it explains nothing, which is part of why the category has been so easy to sell and so hard to buy.
Define it by the decision instead. The edge is however close you have to be to the thing
that commits. The distance is set by the action, not by an architectural preference, and
across this paper it varies by six orders of magnitude.
A sprayer nozzle opens or stays shut in the quarter-second before the plant is behind
the machine. The edge is on the boom. Centimetres.

A car braking for a stop sign has to close perception to actuation inside ten milliseconds, because that is what stopping distance allows. The edge is behind the dashboard.
Metres.
A junction arbitrates a tram’s priority request against an ambulance eleven blocks out,
in four milliseconds. The edge is the cabinet across the intersection. Tens of metres.
An emergency department needs an answer while the patient is still on the table, and
the imaging that informs it cannot leave the building. The edge is the hospital. Hundreds of metres.
And an insurer’s claims system writes a row, queues a payment instruction and closes
a file. That commit happens in a rack. So the edge for that decision is the rack beside it
— inside a hyperscale facility, on the same floor, two aisles over.
That last case matters more than the others, because it dissolves the argument this paper
is routinely mistaken for. A hyperscale data centre is not the opposite of the edge.
When the consequential action is a ledger write happening in the next rack, the next
rack is the edge. The surface does not stop at the campus fence. It runs straight through
it, and some of the densest execution on earth is inside buildings this paper is otherwise
contrasting itself against.
What makes something edge is not distance from a data centre. It is distance from a
commit.

## Chapter 4 — Thinking, Checking, Doing

The industry talks about AI as one thing. For understanding the execution surface it is
three, and they behave completely differently.
Inference proposes. A model takes a situation and returns a suggestion: approve this
claim, spray this plant, grant this priority, order this stock. It arrives as text, or a structured object, or a number. By itself it changes nothing. It is probabilistic by design —
the same input can produce a different answer, and that is what makes it useful on
problems nobody specified in advance.
The admissibility check permits or refuses. Before anything commits, something has
to establish that this action is of a permitted kind, that whatever proposed it was authorised to, that it falls inside the limits attached to that authority, and that the rule being
applied is the rule in force.
That is not a model. It is a small fixed set of structural checks against whatever the actor
is carrying, and it has to give the same answer every time. Critically, its size does not
depend on how complicated the organisation’s policy is. Complexity lives upstream, in
the compilation. The gate stays the same shape whether the rulebook has ten rules or
ten thousand.

A gate that grows with the ruleset is a policy engine that has been moved to the wrong
place. It fits in the window today and stops fitting the moment the business gets interesting.
The act commits. A system call. A write to a socket. A signed transaction. A pulse to
a motor. This is the moment the world changes, and it happens at whatever physical
place the action lands.
Five things follow.

They run on different clocks
Inference is slow — tens to hundreds of milliseconds, longer for anything complex. The
act is fast: microseconds, a handful of instructions. The check has to fit alongside the act
rather than alongside the thinking, which means it is operating in a budget a thousand
times smaller than the one the model enjoys.
Anything designed on the assumption that checking can happen while the model is
running has confused two of the three.

Only one of them can be examined
This is the deeper split and it does not depend on hardware.
A deterministic check can be read, tested against every case, and reasoned about. Somebody who was not present can look at it and know what it did. A model cannot be
examined that way, now or later, whatever tooling arrives.
So the reason enforcement sits apart from intelligence is not performance and not tidiness. It is that one of the two can be trusted by a stranger and the other cannot, and
mixing them means neither can.
The hardware follows from that rather than the other way round. Deterministic work
is small, serial and exact, so it lands on an ordinary processor — not because a CPU
cannot run a model, it can, but because nothing about the job calls for one.

Inference can be remote. The check and the act cannot.
There is no physical objection to a model running in a distant data centre. The agent is
already thinking in hundreds of milliseconds, so a network round trip is an acceptable
overhead on any single step.
The act has no such tolerance, and the check has to be wherever the act is, because being
late is the same as being absent.
Reasoning is location-indifferent. Enforcement is not.

And the act is not deterministic
The check is deterministic by requirement. The act is not, and conflating the two is the
most common error in this area.
The instruction is issued identically every time; what happens next is the world’s business. Swinging a hammer is perfectly deterministic; hitting the nail is not. A request
times out and gets resent, and nobody knows whether it landed once or twice. A write
half-commits. A gripper slips. None of that is a failure of the gate — the gate said yes,
correctly, and the world did something else.
Both of these are in Chapter 1, and better pointed at than left for a careful reader to find.
At 07:50 the agent substitutes an item that turned out to be on allocation, then resubmits
a request that timed out. Both went through the gate. Neither was stopped, because
neither was inadmissible — a substitution is a legitimate purchase and a resend is a
legitimate attempt.
Which means knowing what was permitted is not the same as knowing what happened — and anything that claims to account for a system’s behaviour has to carry
both. Chapter 11 is about why the second is so much harder than the first.

And most work is not affected at all
The overwhelming majority of what AI systems do tolerates hundreds of milliseconds
without diﬀiculty — summarisation, drafting, code assistance, customer service, analysis, search. All of that is fine in a central facility and will stay there. Training stays there
permanently, as do batch analytics and deep reasoning.
The surface described in this paper is not a replacement for any of that. It is the layer that
handles the subset of work where something commits, quickly, in a specific physical
place. That subset is small as a share of tokens. It is most of what happens in a city.

The industry has already split this way
NVIDIA has built silicon around this split and named it accordingly.
On 31 May 2026, at GTC Taipei, the company announced Vera — “the first CPU built
for AI agents” — eighty-eight custom Olympus cores, in full production, shipping from
system builders this autumn.4 The argument in the announcement is the one above.
Agents do not merely answer; they take actions, run code, call tools and evaluate what
comes back, and that work is CPU-bound. Sandboxed execution and orchestration run
on the host processor, not the accelerator, so the host is what caps agent throughput.
NVIDIA frames the economics as a shift from cores per dollar to tokens per dollar.
So the largest supplier of AI silicon in the world now sells a GPU for the thinking and
a CPU for the doing, and says so on the box.
       NVIDIA Corporation. NVIDIA Unveils Vera, the CPU for Agents. Press release, 31 May 2026, GTC
Taipei. 88 custom Olympus cores; in full production; systems available from builders and cloud partners
from autumn 2026. NVIDIA’s stated argument is that agent workloads are CPU-bound on sandboxed code
execution, tool calling and orchestration, and that AI factory economics are shifting from cores per dollar
to tokens per dollar. Cited as an architectural position, not as a benchmark result.

The difference is what each side concludes about where. NVIDIA’s answer is to put
the fast processor next to the accelerator, inside the rack, so the agent’s tool calls do not
wait — correct for the tool calls they have in mind: sandboxes, code execution, database
lookups, memory retrieval. All of those are the agent thinking with props. None of
them commits anything to the world.
None of that is the execution boundary. The boundary is at the servo, the valve, the
ledger and the nozzle — and by Chapter 3’s definition, sometimes that is two aisles
away in the same building and far more often it is a field, a junction box or a shop. The
rest of this paper is a tour of where those actually are.

PART THREE — THE SURFACE

## Chapter 5 — What Is Already Built

Four segments, four unrelated industries, four different stated reasons, and the same
structure underneath. None of these is a pilot. All of them are in production now.

The vehicle
A modern car is a data centre that drives.
Tesla designs its own silicon. The AI4 computer has been in production since 2023 —
two Tesla-designed SoCs on a Samsung 7nm process, delivering roughly 100 to 150 trillion INT8 operations per second on an estimated 80 to 100 watts. That is the hardware
running Full Self-Driving. Every perception decision, every path plan, every intervention, computed on a board behind the dashboard with no network anywhere in the
loop.5
NVIDIA sells the alternative to everyone else. DRIVE Thor entered production in 2025
at 1,000 INT8 TOPS per chip, configurable between 40 and 130 watts, and has been
adopted by BYD, Zeekr, Lucid, Xiaomi, XPeng and GAC.6 NVIDIA’s headline figure
of 2,000 is FP4 floating point rather than INT8 — worth separating, because the two
numbers get quoted interchangeably and they are not the same measurement.
Underneath both sits the volume deployment that nobody counts as edge AI. Mobileye
had shipped over 100 million EyeQ chips by the end of 2021, across more than 300
vehicle models and 30 manufacturers.7 Lane keeping, emergency braking, adaptive
cruise. Every one of those is a model running locally and committing to a brake actuator.
Inside the car, consolidation is correct, for exactly the reason Chapter 3 gives. Distances
are metres. Propagation delay is nanoseconds. Manufacturers are collapsing dozens
of separate controllers into one central core, with zonal aggregators that route sensor
traﬀic and actuator commands but run no control logic themselves. When distance is
trivial, centralise.
Step out one level and the same manufacturer will not send a single driving decision to
a data centre. At five hundred kilometres the identical logic produces an unacceptable
      Tesla AI4 (Hardware 4) FSD Computer: two Tesla-designed SoCs fabricated by Samsung on a 7 nm
process, in production since 2023, approximately 100–150 INT8 TOPS combined at an estimated 80–100 W
system power. Tesla moved from third-party silicon to in-house design in 2019. † The power envelope is
an estimate; Tesla does not publish it.
      NVIDIA DRIVE Thor: 1,000 INT8 TOPS per chip, configurable 40–130 W, in production since 2025.
Announced adopters include BYD, Zeekr, Lucid, Xiaomi, XPeng and GAC. NVIDIA’s headline figure of
2,000 is FP4 floating point, not INT8; the two are routinely quoted interchangeably in trade coverage and
are not the same measurement.
      Mobileye Global Inc. Celebrating 100 Million EyeQ®s on the Road. 13 December 2021. Over 100 million
EyeQ chips shipped, across more than 300 vehicle models and more than 30 automakers. The figure is a
floor; the current cumulative total is higher.

answer. Perception to actuation has to close in under ten milliseconds because that is
what stopping distance allows, and the vehicle generates terabytes a day that could not
be moved in time even if the latency were free.
One company, one product, two opposite architectural decisions, both derived from
the same equation.
There is a second, smaller demonstration in the same vehicle. Several manufacturers
now ship a conversational assistant in the cabin. It is a cloud service, and without a
connection it does not work — in a tunnel, in a dead zone, on a rural highway, the
assistant is simply absent while the car continues to drive itself perfectly well. Nobody
designed that contrast as a lesson. The thinking went remote because it could. The
doing stayed because it had to.
Note the scale, because it cuts against the assumption that serious inference needs serious iron. Tesla is doing the most consequential local inference anyone does at volume
— a two-tonne object moving at speed among people — on about a hundred watts and
roughly the compute of a high-end workstation. Not a rack. Not a region. A board
behind the dashboard.
Vehicles are the largest deployment of mission-critical local inference in existence, on
a replacement cycle measured in years. They are also parked something like ninetyfive percent of their lives8 , and for a meaningful fraction of that they are plugged into
power. So a large and growing share of the world’s local compute is going to be sitting
in driveways and charging depots, doing nothing, on mains power, within a kilometre
or two of a very large number of people.

The junction box and the tram
Municipal infrastructure is the least glamorous segment and the most instructive, because the motivation is so clean.
A city runs traﬀic signals because it is obliged to. It runs transit because it is obliged to.
When it puts a processing unit in a junction cabinet, the justification is a line in a capital
programme: signal timing, transit priority, pedestrian safety, incident detection. There
is no business case involving compute markets and there never was.
The latency requirement is real but modest — tens to hundreds of milliseconds for signal arbitration, faster for safety interlocks. What actually forces the compute local is a
different pair of constraints.
The loop cannot fail. A junction that stops arbitrating when a link degrades has to
fall back to a fixed timing plan, which is a real and visible cost — congestion, missed
priority, a slower ambulance. So the cabinet decides locally and reports upward, rather
than asking upward and waiting.
The volume is unreasonable to backhaul. A camera at every approach, a sensor in
every phase, across thousands of intersections, continuously — an enormous recurring
cost for information that is interesting for a few seconds and only at that junction.
     RAC Foundation. Spaced Out: Perspectives on Parking Policy. 2012; and Shoup, D. The High Cost of Free
Parking. 2005. Both find the average passenger car is parked approximately 95% of its operational life.

The tram carries the same logic in a moving box. Door interlocks, dwell time, traction,
priority requests. Nineteen hours a day, several million decisions, on hardware specified as part of the vehicle.

The store
Retail is where the surface is thickest per square kilometre, and where the motivation
is most obviously financial.
The founding case is bandwidth. A large store runs dozens of cameras. Backhauling
those streams continuously costs more in egress than the local hardware costs outright,
and the analysis produces a few kilobytes of useful output from terabytes of input. So
the processing moves to where the cameras are, and only the conclusions travel.
But loss prevention turned out to be the smallest of the jobs.
A coffee chain runs a node in each of eleven thousand stores. It predicts order composition from the drive-thru queue and moves the brewing schedule ahead of it. It watches
refrigeration units for tolerance drift, preventing both spoilage and an emergency callout. It applies eligibility rules to promotions at the till. It revises the afternoon labour
schedule when footfall tracks below forecast — a decision with real money in it, made
hundreds of times a day across the estate. And it commits supply orders against local
sell-through rather than a regional average, because the store two blocks from a university and the store in an oﬀice district are not the same store and never were.
That last group is the important one. Scheduling and supply buying are not latencybound in the physics sense; a labour decision could tolerate a second, or ten. What
makes them local is that they depend on local state that nobody else has — this queue,
this shelf, this morning’s footfall, this unit’s temperature curve — and moving all of
that upstream to decide centrally costs more than deciding where the state already is.
Data gravity does the same work as latency, by a different route. When the information is local, voluminous and perishable, the decision goes to the information rather
than the other way round.
A retail node is a few hundred watts to a couple of kilowatts, in a back room, on a
commercial premises with an occupant, a fixed address, staffed hours and an existing
insurance relationship. Load follows footfall: peaks at morning and lunch, a long afternoon trough, nothing overnight. Sized for the peak, which means idle most of the time.
And there are a great many of them, in every high street, in every town.

The factory floor
On a factory floor you can put your hand on the execution boundary. It is worth being
exact about where it sits, because almost everyone points at the wrong thing.
A robot arm is about to move a box. Upstream of that, a vision model has classified the
box. Upstream of that, a scheduler decided this box goes to this line. Upstream of that,
an order system decided the line runs today.
None of those is the execution boundary.

The boundary is the servo. It is the moment current flows to the motor and the arm
moves — when the gripper closes, when the valve opens, when the conveyor indexes.
Before that instant everything is a proposal and can be revoked at no cost. After it, a
physical object is somewhere else and the world has changed.
That instant is microseconds wide. Whatever governs it has to be inside it.
This is the clearest available answer to a question that otherwise floats: where exactly
does authority land in an autonomous system? Not in the model. Not in the orchestrator. Not in the policy document. At the servo, in the microsecond when the motor
turns, on the controller that turns it.
Industrial vendors have been embedding inference into operational technology for
years — accelerator tiles in programmable logic controllers, vision systems on industrial PCs at the cell, motion controllers with model inference in the loop. Latency
windows between one and ten milliseconds, deterministic9 , meaning not just fast
but predictably fast, because a control loop with variable timing is a control loop that
oscillates.
The justification is blunt: a line stoppage costs more per minute than the compute costs
per year, and a defect that escapes the cell costs more than either. There is no cloud in
this picture and there never was. A network round trip does not fit in a one-millisecond
deterministic window, and a plant that stops when its connection degrades is not a plant
anyone will operate.
What is changing is the character of what crosses the boundary. Historically everything
the servo did was specified in advance — fixed at commissioning, certified, frozen. A
threshold is not a judgment, and nobody needs to govern a threshold. What is arriving
now is discretion at that same boundary: a model, not a threshold, decides whether the
part passes; a scheduler with real latitude decides which cell runs what; an agent with
authority over a maintenance budget decides to order a part.
The boundary has not moved. What crosses it has changed character — from a rule
someone wrote to a decision something made. That is the transition this whole paper
is about, and the factory floor is where it is easiest to see, because the boundary is a
piece of metal that moves.
Of all the segments here, this is the one best prepared to be trusted by an outsider —
ruggedised hardware in an operational network, physically secured, inside an environment already audited because safety regulation requires it. It is also the one with the
fewest units. And a great deal of certified, secured, capable compute sits in the dark
from six in the evening until six in the morning.

      † Industrial Ethernet protocols (PROFINET IRT, EtherCAT) enforce deterministic bus cycle times of 1
to 10 ms; machine-vision inference deployed inside these control loops must complete within that window
or trigger a real-time fault. Drawn from protocol specifications rather than a single consolidated source.

The high street
If execution has to happen near the action, the obvious question is where to put the
boxes. The question was answered before anyone asked it.
Retail catchments settled at roughly one to three kilometres, because that is how far
a person will travel for a low-value routine purchase — milk, a prescription, a coffee.
It was optimised over centuries against human convenience and transport, and it produced the high street. That distance is a round trip of hundredths of a millisecond in
fibre: comfortably inside any latency budget in this paper.
There is a sharper version of the observation.
Data centres go where land, power and water are cheap. Those conditions correlate
with low population. Data centres therefore go away from people.
The execution surface goes where actions commit. Actions commit where activity is.
It therefore goes toward activity.
Same physics, opposite geography. One flees consequence and the other is defined
by proximity to it. That is empirically checkable rather than rhetorical: put a map of
hyperscale campuses beside a map of population density and the divergence should be
visible. If it is not, this section is wrong.
One qualification, because the neat version overstates it. The surface follows economic activity, which correlates with population but is not the same thing. Retail, transit, clinics
and warehouses cluster with people. Substations, pipelines, ports, mines and farms do
not, and two of the strongest examples in this paper are in places nobody lives. The accurate claim is that execution goes where consequences happen. Usually that is where
people are. Sometimes it emphatically is not.
What the high street adds is the commercial fabric. Every unit on it already has power,
an occupant with a reason to compute locally, and a fixed address. It is the densest
concentration of premises satisfying all three conditions, and it exists in every town,
without anyone having to build it.

## Chapter 6 — The Hard Cases

Three segments where the constraints are worse, and where each one teaches something
the easy cases do not.

The field
The strongest argument that the edge is not a forecast is that agriculture and remote
industry already finished building it.
A boom moves down a field at working speed. Cameras look at the ground. A model
classifies each plant as crop or weed. A single nozzle fires or does not. The whole loop
completes in around a quarter of a second, because that is the time available before

the plant is behind the machine. Field trials put herbicide reduction between forty and
ninety percent depending on the system and the setting10 — a large, measured saving
in a commodity input.
There is no version of this that involves a network. The machine is in a field, connectivity
is unreliable, and even with a perfect link the round trip would not fit. Local inference
is not an optimisation here. It is the entire product. The same architecture is now in
drones — smaller, cheaper, and multiplying.
And the failure mode here is the one that should worry people. The sprayer has a
sensitivity setting. Set it low and you spray less, which looks like a saving and reads
well on a cost report. But the weeds the system misses survive, set seed, and return.
In trials, populations rose by a factor of nearly three per year under low-sensitivity
settings11 , and later passes could no longer control what the first had let through.
Nobody made a bad decision. Somebody chose a parameter months earlier, for a reason that looked sound. The machine then applied it faithfully, thousands of times a
minute, across seasons, with nobody present at any individual decision. The damage
compounded silently and became visible only when it was expensive.
That is the characteristic shape of machine-speed failure. Not a dramatic error — a
small wrong setting, applied perfectly, at volume.
And note what would and would not have helped. A record of which setting was in
force, each pass, would have let somebody establish in month three what took until
month eight to notice. It would not have made the setting correct. Nothing at a boundary can establish agronomic judgment; it can only establish what was applied, under
what parameters, on whose authority. That is a smaller claim than people want from
these systems and it is the one they can actually keep.

The camp
Six hundred kilometres north, a mining camp with no road access for five months of
the year runs on a rack in a heated container. Haul truck routing, ventilation on demand, pump scheduling, ore grade classification from a conveyor camera, crew rostering against a helicopter window. It runs the site.
There is a satellite link. It is genuinely good — enough for communications, telemetry,
and model updates. It is not enough to run operations and nobody involved imagines
that it is. The round trip is tens of milliseconds at best, the link degrades in weather,
and an operation that halts when a link degrades is an operation that halts.
       Peer-reviewed field evaluations of camera-based targeted spraying report 40–90% reductions in
post-emergence herbicide volume versus conventional broadcast application. The range is conditiondependent: savings reach 80–90% in fallow conditions with weed ground cover below 5%, and compress
to 30–50% in standing crops under dense canopy closure. † Synthesised from the agronomy field-trial
literature rather than a single study.
      † In weed-science demographic models for high-fecundity species, conservative detection thresholds
that permit 5–10% of weeds to escape allow the local soil seedbank to expand by a factor of 2.5 to 3.8 per
season, compounding annually until secondary post-emergence applications become ineffective through
weed height and canopy shielding. This is a seedbank population-dynamics model observed under highfecundity pressure, not an invariant constant across all targeted-spraying deployments. Drawn from weedscience demographic modelling rather than a single trial.

So the rack decides, and the link reports. Connectivity is a reporting channel, not a
decision channel. That distinction is obvious in a mining camp and quietly true everywhere else.
That arrangement has a ceiling, and the camp already knows where it is. The rack runs
on generator power in a heated container. It cannot be much bigger, because bigger
means another container and more diesel. And when something fails, somebody flies
in. So the camp runs the models it can fit and does without the ones it cannot. The ore
classification is small because it has to be. The scheduling is cruder than it would be
with real capacity behind it. It is not ideal. It is what fits.
Which makes this the one place in the paper where the interesting question points upward rather than outward, and the sidebar takes it up.
This is also the purest instance of the argument in this paper, and it required no argument. Remote industry arrived at it because there was no alternative, decades before
anyone wrote the word “edge” in a marketing document. Mines, ships, rigs, pipelines,
forestry, remote construction — all of them have been running autonomous local operations under intermittent connectivity for a long time. The remote edge is not emerging.
It is mature, and everyone else is converging on what it already knew.

National infrastructure
The factory floor argument does not stop at the factory gate. Run it outward and it
covers most of what a country’s operational infrastructure actually does.
Electricity. A fault appears on a distribution feeder. A gateway detects it and trips a
breaker in milliseconds, because a local surge that is not isolated becomes a regional
event. There is no version of this that consults anything.
Underneath that headline case is a quieter and larger one. Distributed energy resources
— rooftop solar, batteries, local generation — are now numerous enough to destabilise
distribution networks if they behave unpredictably. So utilities require them to behave
predictably, and the requirement is explicit: when the link between an inverter and
its controller drops, the system executes a pre-configured fail-safe12 . An automated
shutdown, or a ramp down to a safe pre-approved output.
Utilities state the reason plainly. Predictable, automated local fallback is what gives
them the confidence to admit distributed assets to high-stakes grid programmes at all.
That is worth sitting with. Deterministic local behaviour is the precondition for admission. Power engineers arrived at the central requirement of this series from a completely different direction, and wrote it into their interconnection standards.
Water. A treatment plant adjusts dosing against residual measurements, manages pressure across zones, schedules backwash, and isolates a main when a pressure signature
      IEEE Std 1547-2018, Standard for Interconnection and Interoperability of Distributed Energy Resources with
Associated Electric Power Systems Interfaces, Clause 10.7. On loss of communication with the Area EPS operator, the DER maintains current operating parameters or reverts to pre-configured default control settings
within a defined time window. Reinforced by California Public Utilities Commission Rule 21 and Hawaiian Electric Rule 14H, which require distributed inverter systems to maintain autonomous local fallback
logic as an explicit precondition of grid interconnection.

suggests a break. The timescales are seconds to minutes rather than microseconds —
water is slow — but the same two constraints apply. The state is local and voluminous,
and the plant cannot stop deciding when a connection drops.
And everything else. Snow clearing. Transit fleet management, signal priority, level
crossings, tunnel ventilation. Traﬀic incident detection, variable speed limits, ramp metering. Police and emergency dispatch, where unit assignment against call volume and
shift boundaries is already automated in many services. Port operations, rail yards, airport ground movement, waste collection, building management across public estates.
Each of these is being made agentic, sector by sector, by different vendors on different
procurement cycles with different certification regimes. Each one is a decision loop
that touches physical infrastructure, runs continuously, cannot depend on a link, and
increasingly involves judgment rather than a fixed rule.
A country’s operational infrastructure is becoming a distributed autonomous system, and nobody is assembling it as one. There is no national programme and no architecture. There is a water utility buying one thing, a transit authority buying another,
a police service buying a third — each solving their own problem competently, none
of them interoperable, all of them ending up with local compute making consequential
decisions in unattended places.

The home
The home node is the segment most people get wrong, including — for a long time —
the author.
The intuitive model is that people buy hardware to earn money from it: a box in the
basement, spare cycles sold to a market, revenue against the electricity bill. That model
has been attempted repeatedly and it does not work, for reasons Part Four covers.
What is actually happening is simpler and much more durable. People are buying local
inference for their own reasons, and those reasons are getting stronger.
The work cannot leave. A lawyer works from a converted bedroom. Her work is privileged. Client material cannot go to a third party’s model under terms she does not control, and her professional obligations are not satisfied by a vendor’s assurance about
data handling. She is not unusual — the same constraint binds accountants, doctors
in private practice, therapists, financial advisers, HR consultants, anyone handling personnel files, and a significant share of corporate legal and compliance work. For all of
these, a small model on hardware they physically control is not a compromise. It is the
only configuration that satisfies the obligation.
The tokens add up. Somebody using AI seriously for routine work can spend hundreds
of dollars a month on API calls for work a small local model handles adequately. Pertoken prices keep falling and total bills keep rising, because consumption grows faster
than price declines. A capable local box costs one to three thousand dollars and draws
less power than a gaming PC. The arithmetic gets more obvious every time a workflow
gets chattier.

And it is a nice object. A real consumer category is forming around a small, quiet,
well-designed appliance that sits on a shelf and does useful things for the household
— sited by furniture placement, bought on a consumer replacement cycle, funded from
discretionary spending.
What that produces is a very large number of capable machines, in residences, on mains
power, bought for personal or professional reasons, with no relationship to any compute market. And idle almost always. The lawyer’s box works for ninety seconds and
then sits for the rest of the evening. Utilisation is not low because the hardware is badly
matched — it is low because the hardware is correctly sized for a burst and the bursts
are short.
By unit count this will be the largest segment of the entire surface. By underwriting
diﬀiculty it is by far the worst: no operator, no site certification, no uptime obligation,
no physical security, and a person who may unplug it to plug in a lamp.

## Chapter 7 — The Telco

One segment of the surface was built deliberately, by well-capitalised operators, in the
best possible locations, specifically to sell local execution.
It did not sell.
The facilities are genuinely excellent. Telecom central oﬀices are five-nines environments — dedicated power, redundant networking, physical security, staffed operations
— and they are close to users by design, because that is what a telephone network is. Carriers are licensed, regulated, creditworthy and permanent. Nobody thinks a national
telecom operator is a stranger.
The hardware went in. By late 2025, seventy-one mobile operators across thirty-nine
countries had deployed standalone cores capable of sub-ten-millisecond response.13
Major carriers on every continent partnered with equipment vendors and cloud
providers to place servers at central oﬀices and base stations. Hardware accounted for
the majority of mobile edge computing spend.
Then almost nobody bought it.
The clearest case: one national carrier announced a multi-million-pound investment
in early 2023 and opened an edge site covering a hundred-kilometre radius, stating it
would roll out to business customers more broadly. Nearly three years later it still had
that one site. An executive described the original approach candidly — build it and
they will come.
Three reasons are usually given.
      Global mobile Suppliers Association (GSA), 5G Standalone Global Status Update. 61 operators across
39 countries had commercially launched 5G SA networks as of end-2024; tracking through late 2025 puts
the total deploying or commercially operating public 5G SA cores at 71 operators across 39 to 42 countries.
‡ The figure moves with each GSA release.

Fragmented contracting. An application needing national coverage has to contract
with each operator separately, in each jurisdiction, with separate billing and separate
terms. Making a workload span operators required a purpose-built discovery interface,
demonstrated as a novelty rather than used as routine.
The carrier became a landlord. In the dominant model, the operator supplied the
building, the power and the network, and a cloud provider supplied the compute and
kept the customer. The carrier monetised rent. It never monetised execution.
And the guarantee covered the wrong thing. A carrier can commit to uptime, power,
physical security and data residency. That is a facility guarantee and it is genuinely
valuable. But a buyer running consequential automation needs something else entirely:
what was decided here, under whose authority, against which rule, and can I show that
to a regulator.
No carrier could offer that, because nothing in the rack produced it.
So enterprises priced carrier edge as premium colocation and bought their own equipment instead. Private on-premises deployment won — not because it was cheaper or
closer, but because the buyer owned the box and therefore did not need to be convinced
of anything.
It would be easy to file this as a failure and move on. It is more useful as a segment,
because the infrastructure is real and it is still there. Carrier facilities are the best-sited,
best-powered, best-secured tier of the entire surface below hyperscale. They sit in every
metro area, inside the radius that matters, with staffed operations and audit posture
that no shop or junction box will ever have.
Everything about that tier works except the part where somebody buys it.
Hold that thought, because it is the cleanest evidence available for what Part Four is
about. Proximity was solved. Power was solved. Security was solved. Uptime was
solved. Counterparty risk did not exist. The market still did not form.
Whatever is missing, it is none of those things.

## Chapter 8 — What the Segments Have in Common

Eight segments, eight unrelated industries, eight different stated reasons. Underneath
them there is one structure.

Four roles, not one device
Chip counts are the wrong unit, because one device plays several roles at once and the
same part plays different roles in different buildings.

Role                       Produces                    Bound by                    Can it be remote?
Data source                An observation              Sampling rate               Yes
Thinking                   A proposal                  Reasoning budget,           Yes
                                                       hundreds of ms
Deciding                   An admissibility            Commit window,              No
                           verdict                     microseconds
Recording                  An account of what          Must bracket the            No
                           happened                    commit

Two of the four must be local. Two need not be. A neural processing unit on a datasheet
tells you nothing about which role the device plays once it is installed — which is why
the edge AI silicon forecasts are counting something other than what this paper is about.

Two populations that fail in opposite ways
Almost everyone shares the same picture of the near future and almost nobody examines it: compute becomes ambient, everything gets a chip, the world turns responsive.
Most of that is right. The error is assuming it adds up to one connected fabric. It does
not, because two different populations are being described and neither can do what the
picture needs.
The first decides but cannot be reached. On the order of thirty billion microcontrollers
ship every year14 — anti-lock braking modules, elevator controllers, safety relays, pump
governors. They make real decisions with real physical consequences, continuously, at
microsecond scale, and are overwhelmingly not networked. The rule is real, deterministic and enforced at the boundary, and it was frozen at manufacture by someone who has
since left the company. You cannot update it, ask what it decided, or verify it applied.
Most of that population is executing control laws rather than exercising judgment, and
nobody needs to govern a thermostat; the fraction that matters is where a policy could
have been set differently and someone bears the consequence. That fraction is small
today and growing, because models are replacing fixed logic.
The second can be reached but mostly doesn’t decide. Connected devices number
roughly twenty-one billion and are forecast to pass fifty billion within a decade.15 Meters, trackers, sensors, cameras streaming upstream. Their rules can be updated any

       World Semiconductor Trade Statistics (WSTS) product-line data, via Semiconductor Industry Association Factbook. Worldwide annual microcontroller shipments have stabilised in the range of 28 to 32
billion units, date-stamped to the 2024–2025 shipment cycle. This figure must not be conflated with total
integrated-circuit shipments (approximately 400 billion units) or total discrete and optoelectronic shipments (exceeding 1 trillion units).
       IoT Analytics, State of IoT active device database. Active enterprise and consumer IoT installed base
reached 18.5–18.8 billion connected units at year-end 2024 and approximately 21.1–21.9 billion during
2025–2026, under a methodology that counts operational end-nodes and gateways communicating bidirectionally over IP or short-range wireless and excludes smartphones, laptops and tablets. The 50 billion
threshold is an unweighted industry trendline projection, not a measurement, and is presented in the text
as a forecast.

time, because the rules live on a server — which means the decision is not at the boundary. It is a round trip away, and by Chapter 4’s definitions it is reporting on an action,
not governing one.
So the population that decides cannot be audited or amended. The population that can
be audited and amended does not decide. The industry assumes the second absorbs
the first: connect everything, decide centrally, problem dissolves. Chapter 3 is why it
does not. Connectivity solves telemetry. It does not solve commitment.
What is actually emerging is a third population, growing from both directions — devices that decide acquiring connectivity, and connected devices acquiring local inference. Every segment in Part Three lives here, and satisfies two of three requirements.
Reachable. Deciding. Not evidenced.

Obligated, unattended, idle
Across all eight segments, three properties recur with almost no variation.
The deployment is obligated or economically forced — a duty to perform, a cost to
avoid, a physical constraint that leaves no alternative. Nobody in Part Three is speculating.
The location is unattended or lightly attended — a cabinet, a back room, a container,
a shelf, a parked vehicle. The factory is the exception and it is the smallest segment by
unit count.
And the capacity is idle most of the time, structurally, because every one of these boxes
is correctly sized for a peak and peaks are brief.
Obligated, unattended, idle. Those three words are the rest of this paper.

Sidebar — The Node That Leaves
An exploration. This sits outside the argument; it is here because the paper’s own logic goes
somewhere uncomfortable when you follow it up instead of out.
While compute is running toward the places where actions happen, it is also running
somewhere else entirely. Up.
And the camp from Chapter 6 is the first plausible customer, because of an arithmetic
that applies to almost nobody else.
When the camp sends something to a model it cannot run locally, the request goes up
to a satellite, across the constellation, down to a ground station, and then overland to a
data centre — and the answer comes back the same way. Every leg of that except the
first exists because the compute is on the ground.
Put the compute on the satellite and all of it disappears. The camp’s round trip becomes up and down: a few milliseconds, to hardware with solar power, no water bill,
no cooling constraint, no diesel, and nobody who has to fly in to replace a fan.

For a city this is uninteresting — a city has fibre, and orbital compute would be an
extra hop to reach something already close. For a site with no road, it deletes the entire
terrestrial leg. Mines, ships, rigs, pipelines, remote survey, disaster response, anywhere
military. The places where local compute is mandatory are exactly the places where a
data centre overhead is worth more than a data centre anywhere.
Several companies are now building data centres in low Earth orbit. Google’s first Suncatcher satellite went up on 1 October 2026 carrying four of its own AI accelerators, and
its early runs are capped at roughly fifteen-minute bursts by what the radiators and
batteries can take — which is the whole problem in one number.16 Starcloud trained
a model in orbit on a single accelerator in late 2025 and has filed for a constellation
of eighty-eight thousand.17 Blue Origin has filed for fifty-one thousand six hundred.18
The merged SpaceX and xAI entity has filed for a million.19
The stated reason has nothing to do with latency. In the right orbit a solar panel produces up to eight times what it would on the ground, almost continuously.20 There is
no water bill, no zoning hearing, no interconnection queue and no neighbours. Every
siting constraint in Chapter 9 simply disappears.
And the latency is better than people expect. Light moves faster in vacuum than in
glass, by half again. Straight up to a satellite at 550 kilometres and back is about 3.7
milliseconds; even near the horizon, past eleven hundred kilometres of path, about 7.5.
A fibre round trip from Toronto to Ohio, routed the way fibre actually runs, is also about
7.5. So on physics alone, a data centre overhead beats a data centre on the ground once
the ground one is more than about two hundred and twenty kilometres away — which
is to say almost all of them, from almost anywhere.
Real systems do not achieve this, because traﬀic routes through ground stations and
the satellite you can see is rarely the one you want. Measured latency on consumer
satellite links runs twenty to forty milliseconds, not four.21 The floor is physics; the rest
is architecture. Availability, handover, usable accelerator capacity and service reliability
      ‡ Google LLC / Planet Labs. Project Suncatcher prototype satellite, launched 1 October 2026 aboard
the SpaceX Transporter-18 rideshare mission from Vandenberg Space Force Base, carrying four Google
Tensor Processing Units. Radiator and battery constraints limit initial TPU execution to operational bursts
of approximately 15 minutes. A follow-up paired mission scheduled for 2027 will test inter-satellite freespace optical links.
      ‡ Starcloud Inc. Starcloud-1 launched 2 November 2025 aboard the SpaceX Bandwagon-4 mission, operating an NVIDIA H100 GPU; completed demonstration inference in orbit during December 2025. FCC
application ICFS File No. SAT-LOA-20260202-00073, filed 4 February 2026, seeking authority for a constellation of up to 88,000 satellites.
      ‡ Blue Origin. FCC application for Project Sunrise, filed 20–21 March 2026, requesting authorisation
for up to 51,600 satellites in sun-synchronous orbits between 500 and 1,800 km. See FCC Public Notice
DOC-420864A1.
      ‡ SpaceX. FCC non-geostationary spectrum application (2026) requesting authorisation for up to
1,000,000 orbital data centre satellites.
       Derived from extraterrestrial solar irradiance physics. The solar constant at Air Mass Zero is 𝑆0
≈ 1,361 W/m²; terrestrial peak clear-sky irradiance at AM1.5 is approximately 1,000 W/m², and global
terrestrial horizontal insolation averages 150–200 W/m² across a 24-hour period (3.6–4.8 kWh/m²/day).
A sun-synchronous dawn-dusk orbit at 600–800 km avoids Earth’s shadow and receives near-continuous
illumination, yielding approximately 32.6 kWh/m²/day — a multiplier of approximately 8.15×.
      ‡ Physical two-way propagation floor to a satellite at 550 km directly overhead is approximately 3.67
ms; a four-leg bent-pipe path via a ground gateway is approximately 7.33 ms; slant ranges at low elevation
extend the per-leg distance to approximately 1,200 km. Measured consumer LEO round-trip latency runs

are all open, and heat rejection is the largest unsolved engineering problem, because
there is no air to carry it away. No orbital operator has reported commercial revenue
from inference.22 Treat it as an emerging possibility rather than a solution.
And none of it helps with the thing this paper is about. Three milliseconds is a superb
number for a video call and an eternity for a servo. Orbital compute relieves power,
water and permits. It does not relieve Chapter 3. It substitutes for hyperscale, not for
the execution boundary.
Which gives the camp a clean split, and it is the same split as everywhere else in this paper. The thinking can go up. The doing stays in the box next to the outdoor kitchen.

But it does something stranger
A satellite at 550 kilometres crosses the sky in minutes — about four and a half horizon
to horizon, and rather less if you want it high enough for the good latency.
The node you are using is never the node you were using. A session lasting an hour
hands off fifteen or twenty times. At constellation scale that is manageable as engineering: eighty-eight thousand satellites puts roughly four hundred above the horizon at
any moment, so there is always another one.
Peculiar as governance, though. The vehicle is a node that moves, and the problem
there is that it crosses cells and tunnels. The orbital case inverts it. The user stands still.
The infrastructure travels past.
The same assumption breaks either way: that the node which reasoned about an action
is still reachable, still identifiable, and still in existence when somebody comes to ask
what it did.
Here it is not reachable four minutes later. It is over the horizon, and its replacement
has no memory of what it concluded. Whatever account exists had to be produced on
a machine that was present for a moment and then physically left.
That is the problem of Chapter 11 in an unusually literal form, and the industry is filing
for these constellations by the tens of thousands while the answer is not obvious to
anyone.

25–45 ms, median approximately 33 ms. The difference is medium-access scheduling, framing overhead,
beam switching, transponder queuing, ground-station IP routing and terrestrial backhaul. † Measured
figures are drawn from aggregated performance reporting rather than operator disclosure.
      ‡ Negative claim, verified as of October 2026: no orbital operator has disclosed audited commercial
revenue derived from third-party machine learning inference services. All orbital AI workloads conducted
to date are unmonetised technology demonstrations, grant-funded research or internal proof-of-concept
tests.

PART FOUR — WHY IT IS STUCK

## Chapter 9 — Nobody Builds This to Sell Compute

Here is the mechanical fact that explains everything in Part Three, and it runs against
the intuition of everyone who has ever tried to build a compute marketplace.
Nobody deploys this hardware in order to sell capacity.
Go back through the segments and look only at the justification.

                                                                     How hard to
Segment                 What paid for it       Idle profile          underwrite
Vehicle                 Bill of materials on   Parked ~95% of life   Hard — mobile,
                        a unit being sold;                           crosses
                        safety certification                         jurisdictions
Municipal               Statutory duty,        Continuous trickle,   Moderate — public
                        capital programme      event spikes          accountability,
                                                                     unattended site
Retail                  Egress avoided,        Diurnal peaks,        Moderate —
                        shrinkage              dark overnight        commercial
                        recovered, spoilage                          occupant, no
                        prevented                                    attestation
Factory                 Downtime               Dark between          Easiest — already
                        prevented, defects     shifts                audited
                        caught, safety                               environment
                        certified
Field / remote          No alternative         Seasonal,             Hard — remote,
                        exists                 campaign-driven       intermittent link
Utility / public        Regulatory             Continuous low,       Moderate —
works                   mandate, cascade       event-driven          regulated but
                        prevention                                   unattended
Home                    Confidentiality        Idle almost always    Worst — no
                        obligation, token                            operator, no
                        cost, consumer                               security, no
                        spend                                        obligation
Carrier                 Built to sell, and     Very low tenant       Best facilities, no
                        did not sell           utilisation           product

The justification column never says revenue. Not once, except in the one segment that
tried it and failed.

Three things this explains
Infrastructure precedes the economy that runs on it — not as analogy, as literal sequence. Rail was laid for freight the builders already had. The grid was strung for
lighting. The execution surface is being built for loss prevention, signal timing, uptime,
confidentiality and safety. Whatever it eventually carries is not what paid for it.
Idle capacity is structural, not transitional. Retail load follows footfall. Factory load
follows shifts. A vehicle spends most of its life parked. A box on a shelf does nothing for
twenty-three hours. These are not underperforming assets — they are correctly sized
for their owners’ peaks, and anything correctly sized for a peak is idle most of the time.
Scale does not fix this. Scale multiplies it.
Which dissolves the objection that normally ends arguments for distributed compute. Utilisation is fatal only when third-party utilisation has to repay the capital. Here
it never did. The hardware is paid for before any external workload exists, so the economics of a byproduct are not the economics of a product.

The order of returns
Where an owner does get value from outside workloads, it arrives third, and the order
is not negotiable.
First is avoided cost — the egress not paid, the stoppage not suffered, the loss not taken,
the tokens not bought. This is what bought the hardware.
Second is the owner’s own accountability. A node that produces an account of its decisions produces an account of the owner’s decisions: the price applied, the claim flagged,
the priority granted, the part rejected, the valve opened. For a regulated operator that
may be worth more than any rental income, because it is an asset they would otherwise
have to construct separately.
Third, and only third, is anything earned on spare capacity.
Any account that reverses this order is describing a different business — one that asks
an owner to speculate on demand rather than instrument a process they were already
running. That business has been attempted repeatedly and has failed for reasons that
are not accidental.
The order matters because it determines who deploys. Reverse it and the supply side
is speculators. Keep it and the supply side is every commercial premises, every public
works department, every factory and every spare room in the country.

Why this cannot crash the way fibre crashed
The financing shape of this build-out is the most underrated fact about it, and the clearest way to see it is against the one that went wrong.
In the five years after the 1996 Telecommunications Act, telecom companies put over
five hundred billion dollars — mostly borrowed — into laying fibre.23 More than eighty
     † Between 1996 and 2001, following the US Telecommunications Act of 1996, telecommunications
carriers deployed over $500 billion in capital expenditure — heavily financed through high-yield corporate

million miles of cable went into the ground, and capacity increased by a factor estimates
put in the hundreds of thousands.
Demand did not arrive on schedule. Four years after the crash, roughly eighty-five
percent of the fibre laid was still dark and bandwidth prices had fallen ninety percent.24
Corning went from near a hundred dollars a share to about one.25 Global Crossing lost
3.4 billion on 793 million of revenue in a single quarter and filed for bankruptcy weeks
later.26
And then, years later, the same fibre carried broadband, cloud computing, video
streaming and the mobile internet. The substrate was fine. It was laid, written off,
repriced, and eventually used for applications nobody had imagined when it went in
the ground.
Two lessons, pointing in different directions. Infrastructure genuinely does precede
its applications — the people who laid that fibre could not have described streaming
video. But the financing shape destroyed the builders. This was speculative capital,
raised on debt, against projected third-party demand, by firms whose own operations
needed none of it. The substrate survived. The companies did not.
Every segment in Part Three is funded the opposite way. The store node is paid for
by egress and shrinkage. The junction cabinet is a line in a capital programme. The
factory controller is paid for by downtime it prevents. The vehicle computer is a bill-ofmaterials item on a car being sold. The lawyer’s box is paid for by her token bill and her
professional obligation. The camp rack is paid for by the fact that there is no alternative.
Not one of these depends on a market existing. There is nothing to write down, because nothing was financed against revenue that has not appeared. The capital arrives
as operating expense and bill of materials and capital programmes, spread across millions of unrelated balance sheets, each one justified locally.
It also explains why the build-out is hard to see in the statistics. The edge data centre
market is around seventeen billion dollars in 2026 against hyperscale capital expenditure of roughly seven hundred billion — a ratio of more than forty to one, routinely
quoted as evidence that distributed execution is not happening.27

debt and vendor financing — installing over 80 million route miles of fibre-optic cable across the United
States. Figures are consolidated from FCC industry analysis and telecommunications capital audits.
      † By 2003, approximately 85% of long-haul fibre strands remained dark, and long-haul IP transit
and wavelength prices had fallen by over 90% across primary domestic corridors. See Odlyzko backbone
utilisation studies and contemporaneous FCC market surveys.
       NYSE historical trading record, Corning Incorporated (GLW), 2000–2002. Split-adjusted share price
fell from approximately $113 in September 2000 to an intraday low of $1.10 in October 2002.
       Global Crossing Ltd. SEC Form 10-Q for the quarter ended 30 September 2001: net loss of $3.409
billion on consolidated revenue of $793 million. Voluntary Chapter 11 petition filed in the US Bankruptcy
Court for the Southern District of New York, 28 January 2002.
       The approximately $17 billion edge data centre market figure for 2026 is an analyst consensus estimate, not an audited financial statistic: no public cloud provider or colocation REIT reports an isolated
GAAP segment under that heading, and the figure is modelled by combining micro-modular facilities,
regional colocation and telco central-oﬀice conversions. The hyperscale comparison is drawn from company capital expenditure guidance for the five largest US cloud and AI infrastructure providers (Amazon
≈ $200bn, Alphabet $175–185bn, Meta $115–135bn, Microsoft $120bn+, Oracle ≈ $50bn), totalling approximately $660–690 billion for 2026. ‡ Both figures are moving targets.

But almost nothing in Part Three is a data centre. It is a node in a shop, a controller
on a line, a computer in a car, a rack in a container, a box on a shelf — bought from
operational and product budgets, appearing in nobody’s edge infrastructure statistics.
Whether that hidden spending is larger than the visible number is not currently measurable by anyone, and that is an honest weakness in this paper rather than a rhetorical
escape. What can be said is that the forty-to-one ratio is measuring two different things
and treating them as one.

And none of the hyperscale constraints apply
Most papers about AI infrastructure open with how hard it is getting to build a data
centre. The constraints are real, and the interesting thing about them is that none of
them apply to anything in Part Three.
Power. Availability has replaced land as the primary determinant of where a campus
can go. Grid connection queues in major hubs run to five years. A hundred-megawatt
facility draws the electricity of seventy-five thousand households28 , and operators are
building their own generation behind the meter specifically to avoid the interconnection
queue. A node in a shop draws less than a kilowatt from a supply that already exists.
Water. Cooling concentrated heat takes enormous quantities of water; large facilities
can consume millions of gallons a day in regions already in drought. It is the single
most effective argument available to local opposition, and a fair one. A node in a shop
is air-cooled by a system that was already there.
Permits and opposition. Roughly sixty-four billion dollars of US projects delayed or
cancelled over two years. Construction costs up from about six hundred and thirty dollars a square foot to over nine hundred and sixty.29 Community resistance that crosses
political lines, because the local costs are concentrated and the benefits are not. Nobody
objects to a box in a building that already has power — there is no concentrated local
cost to organise against.
Stating the asymmetry carefully. This does not mean the surface substitutes for hyperscale. It cannot absorb training or batch analytics, and those are the workloads consuming the gigawatts. The pressure on campuses is not relieved by anything in this paper.
What it means is narrower and still significant: the two build-outs serve different workloads and face different constraints. One is running into physical and political limits
that are getting worse. The other grows by occupying buildings that already exist.

       Lawrence Berkeley National Laboratory, Queued Up interconnection queue reports: average interconnection queue delays across major Regional Transmission Organizations extend from four to over five
years. A 100 MW continuous facility at an 85–90% annual load factor consumes approximately 745,000–
788,000 MWh per year; against US Energy Information Administration average residential consumption
of approximately 10,500 kWh per year, this is equivalent to 71,000–75,000 households.
      † Turner & Townsend Data Centre Cost Index, 2024–2025: base construction costs across primary
North American data centre hubs advanced from historical averages of $600–650 per square foot to over
$950–1,050 per square foot, driven by dual-loop direct-to-chip liquid cooling, high-density power distribution and structural reinforcement for multi-hundred-megawatt campuses. The approximately $64 billion
of delayed or cancelled US projects over a trailing 24-month period derives from Dodge Construction Network project pipeline tracking — a commercial audit, not an oﬀicial statistic.

The argument nobody is making
There is one further consequence, strange by its absence from public debate.
In March 2026, Iranian drones struck commercial data centres in the UAE and Bahrain
— the first time a state deliberately targeted commercial data centres in wartime.30 Military doctrine already treats civilian computing facilities carrying intelligence, defence
or sovereign logistics workloads as lawful dual-use targets, and analysts expect governments to fold data centres into critical-infrastructure planning alongside energy, water
and transport.
Concentration created a targetable object where none existed before. A hundred
megawatts of compute in one place is a point on a map.
What is odd is that this is precisely the argument that produced the architecture of the
internet in the first place — and nobody is making it. The record needs care, because the
popular version is a myth: ARPANET was built for resource sharing among research
computers, not to survive a nuclear exchange.31 But Paul Baran’s work at RAND in the
early 1960s was explicitly about communications that could survive an attack on any
particular node, and the conclusion was a distributed mesh with redundant paths and
no critical centre.32 The architecture was justified by survivability and then built for
convenience. Sixty years later the same thing is happening in reverse: a distributed
execution surface is being built for convenience, while the survivability argument that
would justify it is not being made by anyone.
The honest version has a cost. Dispersal does not make a system safer; it makes it differently exposed. Ten thousand nodes across ten thousand buildings means ten thousand
locations with variable security and ten thousand software estates to patch — an attack
surface enormously larger than one hardened facility with guards and a security operations centre. What it buys is the removal of single-point catastrophic loss: one strike,
one grid failure, one flooded basement cannot take the whole capability. That is the
benefit that matters when the threat is kinetic.
But it trades that for a much harder monitoring problem, and this is where the paper’s
argument reappears from an unexpected direction. A dispersed surface is defensible

      † Contemporaneous reporting, late March 2026: regional drone and missile attacks targeted commercial infrastructure in the Persian Gulf, including sites in the United Arab Emirates and Bahrain, with
open-source defence reporting and corporate risk notices indicating that commercial data centres hosting dual-use cloud services sustained structural and electrical damage. Drawn from contemporaneous
reporting rather than oﬀicial confirmation. Note: an earlier draft asserted that eighteen named technology companies were designated as legitimate military targets; no primary gazette, decree or communiqué
supports that claim and it has been removed.
       Taylor, R. W. (Director, ARPA Information Processing Techniques Oﬀice) has stated on the record
that ARPANET was conceived to link heterogeneous research computers at distant academic institutions,
eliminating the need to procure redundant mainframes at each contractor site, and that packet switching
was selected for bandwidth eﬀiciency and interactive remote terminal access rather than nuclear resilience.
See also ARPA IPTO programme charters.
       Baran, P. On Distributed Communications. RAND Corporation memoranda RM-3420-PR through RM-
3430-PR, eleven volumes, August 1964. Volume I, RM-3420-PR, Introduction to Distributed Communications Networks, analyses centralised, decentralised and distributed topologies under nuclear attack scenarios and concludes in favour of a distributed mesh using digital message blocks and dynamic store-andforward routing.

only if each node can be checked — not inspected physically, which is impossible at
that scale, but checked. What has this node been doing, under what authority, against
which rules.
Same capability. One gap, two problems.

## Chapter 10 — Edge Has Been Tried

By now a particular objection has been building, and Chapter 7 will have brought it to
the surface.
This has all been tried. Repeatedly. By people with more money and better distribution than anyone reading this. Edge computing has been announced as the next wave
roughly every three years since 2014, and the announcements have a consistent quality: enormous vendor enthusiasm, a consortium, a reference architecture, a handful of
lighthouse deployments, and then silence.
A reader who has been in the industry for a decade has watched this cycle two or three
times. The scepticism deserves a proper answer rather than a paragraph.

The graveyard
Fog computing. The most complete example, because it had everything an architectural movement is supposed to have. Cisco coined the term in 2012, and on 19
November 2015 founded the OpenFog Consortium with ARM, Dell, Intel, Microsoft
and Princeton, which produced a reference architecture, a testbed programme, working groups and a substantial body of specification.33 The proposition was precisely
this paper’s: computation distributed between the cloud and the endpoint, closer to
where data originates. By December 2018 it announced a merger into the Industrial
Internet Consortium.34 Nobody says “fog” any more, and the architecture it specified
was not adopted at scale.
Carrier mobile edge computing. Chapter 7 covers it. Excellent facilities. Almost nobody bought.
Industrial IoT platforms. The most expensive failure in the list. One major industrial
conglomerate built a platform intended to be the operating system for connected machinery across its own enormous installed base and everyone else’s, with very large
capital commitments and a dedicated business unit. It is now a case study in how these
things go wrong, and the business was restructured and largely divested. Comparable
platforms from several other industrial vendors followed similar trajectories. [Writedown figures circulate in secondary coverage and require primary sourcing before citation.]
      OpenFog Consortium founding announcement, 19 November 2015: Cisco Systems, ARM, Dell, Intel,
Microsoft and Princeton University. Cisco coined the term “fog computing” in 2012.
      OpenFog Consortium / Industrial Internet Consortium joint merger announcement, 18 December
2018; integration completed early 2019.

Smart city platforms. A decade of pilots and very few production systems. The most
prominent example in this paper’s own city — a comprehensively planned, sensorinstrumented district — was cancelled in 2020 after sustained public objection, having
produced a great deal of documentation and no district.35
Decentralised compute marketplaces. Treated separately below, because they failed
from the opposite direction.
That is a genuine graveyard and none of it should be minimised. An honest assessment
has to concede that the proposition “build distributed compute infrastructure and a
market will form” has been tested many times and failed every time.
One thing was constant across every entry, and it is about to be constant again: the
hardware vendors were enthusiastic every single time. Cisco coined the term and convened the consortium. GE built the platform. Carrier edge had equipment vendors,
hyperscalers and national operators pushing in the same direction at once.
They are doing it again now, harder and with far better products. NVIDIA ships IGX
Thor into the industrial and medical edge — up to 2,070 FP4 TFLOPS on a system-onmodule, 128 GB of memory, extended temperature range, shock and vibration compliance, ECC, CAN and PCIe Gen5 industrial I/O, and a ten-year support lifecycle.36
AMD sells Versal AI Edge and Kria modules into the same sockets. Supermicro builds
short-depth edge servers around both.
Two details in that product line are worth pausing on. NVIDIA’s stated target applications are factory automation cells, surgical rooms, smart retail checkout, industrial
safety and mobile robots — which is, almost line for line, Part Three of this paper. And
the platform ships compliant with ISO 26262 and IEC 61508, targeting ASIL D and SIL
2.37
That second point matters more than the teraflops. The functional safety standards
Chapter 12 argues the boundary requires are now arriving pre-certified, from the vendor, as a product feature. The separation between what computes and what is allowed
to act is being built into commodity silicon by people who are not thinking about AI
governance at all.
None of which tells you anything about adoption, because vendor enthusiasm was
equally high in 2015. What it does tell you is that the hardware will be available, cheap,
well supported and ordinary. Whatever stops the surface becoming shareable, it will
not be that the silicon does not exist.

       Sidewalk Labs. Oﬀicial statement terminating the Quayside project, Toronto, 7 May 2020, citing economic uncertainty alongside protracted public opposition concerning data governance, intellectual property rights and civic privacy protections.
       NVIDIA Corporation. NVIDIA IGX Thor Powers Industrial, Medical, and Robotics Edge AI Applications.
Developer technical brief. IGX T5000 system-on-module: up to 2,070 FP4 TFLOPS, 2,560-core Blackwell
iGPU, 128 GB LPDDR5x at 273 GB/s. Extended temperature range, shock and vibration compliance, ECC
memory, real-time Linux kernel, CAN and PCIe Gen5 industrial I/O, 10-year support lifecycle. Note that
NVIDIA’s documentation uses TFLOPS and TOPS interchangeably for the same FP4 figures.
       Ibid. IGX Thor is stated to comply with ISO 26262 and IEC 61508, targeting ASIL D/SC3 and ASIL/SIL
2. Final certification is not issued by NVIDIA: the NVIDIA Halos AI Systems Inspection Lab issues inspection reports for customers to submit to certification agencies.

The auction that didn’t clear
If carrier edge lacked a market mechanism, decentralised compute marketplaces had
nothing but market mechanism. Platforms emerged that aggregate third-party hardware and sell it through real-time bidding, reverse auctions and spot pricing. One operates seventeen thousand accelerators across fourteen hundred providers in five hundred locations.38 Another claims to have aggregated over a million from independent
data centres and former cryptocurrency miners.39
The price advantage is real and large — routinely fifty to eighty percent below major
cloud on-demand rates.40
Enterprises did not move.
The market cleared, but only for a particular kind of work: research, experiments, finetuning, rendering, batch jobs that can be restarted if a machine disappears. It did not
cross into production systems or regulated data, and the reasons given by the platforms’
own users read like a summary of this paper. Reliability depends entirely on which
provider you land on. There is no compliance certification for regulated workloads.
There is no security isolation guarantee on unverified hosts. Actual costs run twenty to
forty percent above listed prices once variable performance, interruptions and restarts
are accounted for.41
Read that against the discount. A sixty percent price advantage was not enough to
move production workloads onto hardware nobody had verified. That is a measured
price for trust, and it is a high one.
Three observations make this the more interesting of the two failures.
The industry has identified what is missing and is building it. Several platforms
have developed verification protocols specifically to prove that untrusted hardware executed a task correctly; others are implementing cryptographic proof schemes. The
same requirement, arrived at independently, by people trying to sell capacity rather
than govern it.
Decentralisation reverses under commercial pressure. One of the most credible
decentralised networks saw active providers fall to their lowest level in its history,
with capacity contracting sharply quarter on quarter, while new entrants introduced
protocol-owned compute in enterprise data centres with vetted operators. The market

      Vast.ai public marketplace status page: approximately 17,000 active accelerators distributed across
approximately 1,400 independent host providers spanning over 500 geographical locations. Platformreported telemetry, reflecting verifiable capacity available on the public marketplace.
     † io.net claims access to over 1,000,000 aggregated accelerators. This figure originates in platform marketing, tokenomics documentation and promotional roadmaps and is an unverified platformreported target, incorporating community worker registrations, consumer-grade hardware and partnership pipelines. Independent audits of network state indicate active enterprise-grade accelerators typically
number between 2,700 and 20,000.
     † Decentralised compute broker spot rates run 50–80% below hyperscale on-demand list rates. Requires citation to dated marketplace telemetry.
     † Realised compute expenditure on decentralised brokers runs 20–40% above listed base rates once
node preemption, variable egress, container re-initialisation latency and lost training progress from uncoordinated host restarts are accounted for. Drawn from operator reporting rather than audited disclosure.

demanded verification. Nobody could supply it, so the answer was to re-centralise
and inspect.
A verified tier emerged as a product. Platforms now split their offering: a community
tier of independent providers at lower rates, and a secure tier of vetted infrastructure
at higher rates. Verification is already being sold at a premium, by people who did not
set out to sell it.

And yet
Here is what the graveyard omits.
Content delivery edge compute is one of the largest distributed computing deployments ever built, and almost nobody counts it as edge. The major content delivery
networks began running customer code at their points of presence in the late 2010s. It
is now routine — request routing, authentication, personalisation, bot filtering, image
transformation — executing within tens of milliseconds of the user, across hundreds
of locations globally, at enormous volume.42 Nobody wrote a consortium specification
for it. No reference architecture, no working group, no standards body. It simply got
built and sold.
Private on-premises deployment won the enterprise, decisively. Enterprises did not
reject local execution. They rejected renting local execution from a carrier. The same
companies that would not buy carrier edge instances bought hyperconverged appliances, private cellular networks, and their own racks, in very large numbers.
And every segment in Part Three is a success. The store node, the junction cabinet, the
factory cell, the sprayer, the camp rack, the vehicle, the substation gateway, the lawyer’s
box. None is a pilot. All in production, at scale, paying for themselves.
So the record is not a graveyard. It is a graveyard next to a thriving industrial estate,
and the interesting question is what divides them.

What actually separates them
Sort every item above by a single question: does the thing require two parties who do
not know each other to trust an execution?
The failures all say yes. Fog computing proposed a general substrate on which anybody’s workload might run on anybody’s hardware. Carrier edge asked enterprises to
run production systems in a telco’s rack. Industrial IoT platforms asked manufacturers
to route operational data through a vendor’s cloud and accept that vendor’s analytics
as authoritative about their own machinery. Smart city platforms asked municipalities,
vendors, utilities and citizens to share an instrumented environment on terms none of
them could independently verify. Decentralised marketplaces asked enterprises to run
workloads on hardware owned by strangers.
      Content delivery edge compute general availability: AWS Lambda@Edge, July 2017; Cloudflare
Workers, September 2017; Fastly Compute@Edge, late 2021. Note that edge compute revenue is not separable in provider SEC filings — receipts are bundled within overall subscription, network security and
CDN revenue lines — so no claim about its profitability is made in the text.

Every one required a trust relationship that did not previously exist and could not be
constructed.
The successes all say no. Content delivery edge works because the customer already
had a commercial relationship with the network, the network owns every machine involved, and — this matters — almost nothing consequential commits. It is transforming
a request in flight. If a worker misbehaves, a page renders wrong and somebody fixes it.
Nobody needs to prove afterwards what rule was applied, because nothing irreversible
happened.
Private on-premises deployment works because there is only one party. The buyer owns
the box, the workload, the network and the risk. Verification is unnecessary when the
person who needs convincing is the person who installed it.
And every segment in Part Three works for the same reason. The store’s node runs the
store’s workload. The factory’s cell runs the factory’s line. The camp’s rack runs the
camp. One party owns both ends, and the question of whether a stranger could check
what happened never arises, because no stranger is involved.

The finding
Distributed execution does not fail. Markets for distributed execution fail.
That is a considerably narrower claim than “edge has been tried,” and it changes what
the record means. The technology works. The economics work. The physics forces it.
Deployment is happening at scale right now and has been for years, quietly, without
consortia, in every segment this paper describes.
What has never worked, in more than a decade of well-funded attempts, is getting one
party to rely on execution that happened on another party’s hardware, in a place they
cannot inspect, under conditions they cannot verify.
Which means the objection is not evidence against this paper. It is the paper’s central
evidence, gathered by other people at considerable expense.
Three caveats, because the pattern is a little too clean. Some of these failed for ordinary
reasons too — fog computing’s specifications were complex and arrived before there
were workloads that needed them; industrial IoT platforms suffered organisational
problems unrelated to architecture; smart city projects failed on politics and privacy
more than engineering. So the verification gap is a hypothesis, not a demonstrated
cause. What the record supports is that it was present in every failure and absent from
every success, which makes it worth investigating rather than proven. And content
delivery edge is a success with an asterisk — the workloads are low-consequence, so
it does not actually test the hypothesis.
If anything, that asterisk sharpens the point. The one form of shared distributed execution that succeeded is the one where nothing important commits. The moment something does — a payment, a dispatch, a shutdown, a purchase — the entire record goes
the other way.

Why nobody buys compute from a stranger’s shop
So why do the markets fail? The answer is not technical.
A hyperscale region sells compute on the strength of a compliance estate. Certifications.
Audit posture. Key custody. Administrative separation. Physical security. A company
large enough to sue and likely to exist next year. When an enterprise buys capacity
from a major cloud provider, most of what they are buying is not the silicon. It is the
institution wrapped around the silicon, and the institution is the expensive part.
A tram has none of that. Neither does a shop, a junction box, a mining camp or a shelf
in a house. Which produces a three-link chain.
Uninsurable. No underwriter will write cover for automated decision-making at an
unattended location they cannot inspect, on hardware they cannot certify, run by an
operator with no relevant history, producing no account of what was decided. Not
because the risk is large — because it is unquantifiable. An underwriter prices exposure.
There is nothing here to price.
Unfinanceable. Large infrastructure is not funded from cash. Hyperscale is financed
through securitised credit — asset-backed and mortgage-backed instruments — which
requires assets that can be insured, valued and pledged.43 Distributed capacity is
funded from operating expense and managed service contracts, because it has no
financing vehicle, because it has no underwriting story.
Unusable by anyone else. So capacity that is physically installed, technically capable
and sitting idle cannot be sold, because the buyer cannot verify it and nobody will stand
behind it.
That chain reframes the forty-to-one capital ratio from Chapter 9. It is usually read as
the market’s verdict on where compute belongs. It is better read as a measurement of
where insurance exists.

The seventeenth-century version
This problem is old, and knowing that tells you what kind of problem it is.
A cargo owner in the 1700s faced the same structure. Ships sailed from ports he would
never visit, owned by merchants he had never met, in conditions he could not observe.
He could not tell a sound hull from a rotten one. So he could not insure the cargo, so
he could not risk the trade.
The solution was not better ships and it was not better shipowners. It was a classification society: surveyors inspected vessels against a common standard and published a
register. Underwriters then refused to cover cargo on unclassified ships.44
       Hyperscale data centre capacity is financed through securitised debt instruments, specifically Data
Centre Asset-Backed Securities (DC ABS) and single-asset single-borrower commercial mortgage-backed
securities (SASB CMBS), backed by bankruptcy-remote special purpose vehicles holding legal title to physical facilities and secured by long-term triple-net lease cash flows with investment-grade hyperscale tenants. See Standard & Poor’s and Morningstar DBRS presale rating reports.
       Lloyd’s Register historical records. The Society for the Registry of Shipping published the first Register
of Ships in 1764, providing underwriters and merchants with independent technical assessment of vessel

The direction of the incentive is the whole lesson. Shipowners did not submit to survey
because it improved their vessels. They submitted because unclassified ships could not
get freight.
And there is a detail that matters more than it first appears. What was certified was
not the shipowner’s reputation. It was the vessel’s condition, surveyed to a common
standard, expressed in a form an underwriter could price without inspecting it himself.
Trustworthiness of the counterparty was never the missing piece.
Which explains the most puzzling thing in Part Three. If the problem were trust in
the operator, carrier edge would have worked. The carriers are licensed, regulated,
permanent and creditworthy. Their facilities are excellent and perfectly sited. They
are not strangers by any definition.
They still could not sell execution, because nothing in the rack could say what had happened in it.
Put the two failures side by side and the shape is clear. Carrier edge had facilities,
proximity, uptime and trusted operators. No market formed. Decentralised markets
had an auction, enormous supply and a large discount. Production work stayed away.
Each proposed a different missing piece. Each built it. Neither cleared, and what they
have in common is that the buyer could not check what happened at execution.

## Chapter 11 — The Missing Pieces

The surface exists. The capacity is real, installed, powered and idle. This chapter is the
list of what is not there.
It is a list, not a design. What each of these would be worth, how it would be priced
and how it would clear is the subject of the companion paper.
Five things are missing. The first four are commercial and the fifth is underneath all of
them.

1. There is no exchange.
Compute today is sold in bundled enterprise contracts by a small number of providers.
There is no open market where capacity is bid and cleared, no price discovery, and
therefore no signal that would tell an owner whether their idle box is worth anything
to anyone.

seaworthiness; surveyors inspected hulls and rigging against standardised construction criteria, assigning
classifications such as the A1 rating. Marine underwriters at Lloyd’s conditioned the issuance of cargo and
hull policies on active listing in the Register; unclassed or poorly graded vessels were refused coverage or
assessed prohibitive premiums.

2. No node can say what it is.
This is the deepest of the four and the least discussed.
An operator schedules work onto machines he owns. He installed them, so he knows
what each one is, where it sits and what it can take. That direction is solved and the
tooling for it is mature.
Now run it the other way. State a requirement — a decision inside five milliseconds of
this junction, in this jurisdiction, producing an account a regulator will accept — and
ask the surface which machines qualify. Nothing answers, because no machine out
there has any way of announcing itself to a stranger.
Push works. Pull does not. And pull is not an orchestration problem, which matters,
because orchestration is the diagnosis the industry has already tried and built. An
orchestrator schedules against an inventory it was handed. There is no inventory here,
and no vocabulary in which one could be written.45
3. Nothing can be priced on the two things that decide whether it fits.
Latency class and jurisdiction determine whether a given node can do a given job at
all, and no commercial arrangement expresses either. Compute is sold by instance type
and by the hour. An instance type is a proxy for capability; an hour is a proxy for
consumption. Neither says where the machine is or how fast it can reach anything
from there.
4. An agent cannot pay for what it does where it does it.
Committing a consequential action costs money at the moment of the commit — compute, invocation, settlement, and whatever the counterparty charges. Fees do not disappear because the actor is software. Today those costs flow upstream and are reconciled
in batch, against an account held by a human organisation. No arrangement exists that
lets an agent carry bounded spending authority to the boundary and settle against it
there.
5. There is no way for a stranger to check what happened.
This one sits under the other four, and none of them can be built on top of it until it
exists.
Enforcement at the commit is buildable and, as Part Three shows, has been built repeatedly by people solving unrelated problems. What has not been built is the account —
what was proposed, which rule applied, which version of it, what the verdict was, and
under whose authority, produced at the moment of the commit and portable enough
that someone who was not present can rely on it.
      Negative claim, verified against governing edge standards. ETSI MEC defines application enablement APIs and platform management architectures but provides no open syntax for cross-vendor nodes to
advertise execution boundaries, verifiable state attestations or deterministic tail-latency guarantees. OPC
Unified Architecture provides extensible information modelling, role-based access security and publishsubscribe integration over Time-Sensitive Networking for industrial field devices, but does not address
heterogeneous edge compute admissibility, multi-tenant policy compilation or independent witness logging. Matter is an application-layer interoperability specification for consumer smart-home peripherals
and carries no compute governance abstractions.

The gate is the easy half
There is a version of that last requirement which sounds manageable and is not.
The manageable version: record that the check ran and what it decided. Small, fast,
cheap, and entirely within the control of the component doing the checking.
The actual version has to bracket the act, and the act is where the trouble is. It needs
five things.
What was proposed. The action, as the agent wanted to perform it.
What was permitted. The verdict, the rule applied, the version of that rule, and the
authority it was checked against.
What was attempted. Which is not always the same as what was permitted, because
an agent working through a long chain adapts — substituting an item that turned out
to be unavailable, retrying a leg that failed, splitting a request that was too large.
What came back. Success, failure, partial completion, or nothing at all.
And whether this was a new attempt or a repeat of an earlier one. This is the hardest of
the five and the one most likely to be skipped. When a request times out, the agent does
not know whether it landed. It resends. If the account cannot distinguish a retry from
a second action, then it says two purchases were authorised and the world contains one
— or says one and the world contains two.
None of this is exotic. Distributed systems engineering has wrestled with exactly-once
semantics, idempotency keys and reconciliation for decades, and the answers are partial
and well understood.46 What is new is the requirement that the resulting account be
legible to somebody outside the system — an insurer, a regulator, a counterparty —
rather than to the operator’s own reconciliation process.
Producing a record of a decision is straightforward. Producing an account of what
actually happened is not, and the second is what anyone relying on it actually needs.
And there is a ceiling on even the second one. An account produced at a boundary establishes what was proposed, permitted, attempted and returned. It does not establish
that the supplier was real, that the part was genuinely in tolerance, that the payment
reached the right account, or that the model’s judgment was sound. It attests to observation, not to truth. Anyone expecting more from it will be disappointed, and the
disappointment will be their error rather than the architecture’s.

      On exactly-once semantics, idempotency keys and reconciliation in distributed systems, the literature
is mature and the results are known to be partial. † The literature is broad; no single canonical reference
is cited.

Why this is hard even when you want it
The remaining diﬀiculties are not matters of will.
The device is not trustworthy about itself: the component producing the account shares
hardware with the thing it is accounting for. Keys have to live somewhere, on hardware
in a shop or a roadside cabinet or a vehicle, where physical access is not diﬀicult to
obtain. Ordering matters and cheap devices have bad clocks — “this check happened
before that commit” is the entire claim. And the link is unreliable, which is the reason
the node is local in the first place, so accounts have to be produced without connectivity,
buffered, and shipped opportunistically.
Every piece of that exists somewhere. Secure elements are commodity parts. Signing
is fast. Append-only logging is well understood. What does not exist is the assembly,
at this scale, in a form that means the same thing across different manufacturers, industries and countries.
And it has to be nearly free, because it attaches to every action and there will be an enormous number of actions. Anything that adds meaningful cost per action gets switched
off under load, which is the same as never having it.

## Chapter 12 — Why the Mesh Coheres, or Doesn’t

The previous chapter listed what is missing. This one says what it is.
Paper 1, Execution-Boundary Governance, argued that once an autonomous system holds
execution authority, admissibility has to be settled at the execution boundary, by a deterministic Executable Governance Kernel, inside the window the action itself occupies.
Paper 2, Constitutional Compression, showed that such a kernel compresses to a minimal
invariant core. Paper 3, Evidence Systems, showed that delegating execution forces an independent witness into existence. Paper 4, Upstream, showed that human policy has to
be compiled before a machine can apply it, and that compiling it is a standing function
rather than a project.
All four reasoned from first principles. None of them looked at a deployment.
This chapter drops them onto the surface from Part Three and asks one question: take
all three away, and what is left?
The answer is that it does not become a mesh. It becomes a very large number of capable
machines, each serving one party, with no ability to work for anyone else.

What Part Three already built
Go back through Part Three looking for one specific thing — a component that sits
between a proposal and an act and returns a verdict — and it is everywhere.
The grid gateway that ramps to a safe pre-approved output when its controller goes
quiet. The safety cabinet on the factory floor, on its own network, with its own power,

that the control system cannot write to. The protection relay at 22:40 that trips a breaker
without consulting anything. IEEE 1547, requiring every distributed energy resource
to execute a pre-configured fallback on loss of communications. And now NVIDIA,
shipping IGX Thor pre-certified to IEC 61508.
Every one of those is a deterministic admissibility check at an execution boundary. Not
one of the engineers who built them called it that, and none of them had read a word
about AI governance.
They converged anyway, on the same four properties.
Deterministic. Same action, same actor, same authority, same rule, same verdict, every time, inside a bounded window. A gate that permits on Tuesday and refuses on
Wednesday for no stated reason is not a gate — and determinism is the only reason
somebody who was not present can ever examine what it did.
Fails safe. A check that defaults to permit is decorative, because any failure removes
it silently and nobody notices. Grid operators settled this decades ago and wrote their
reasoning into the interconnection standards: predictable automated fallback is the precondition for admitting a distributed asset at all.
Unreachable by the thing it governs. Different cabinet, different network, its own
power, no path back in. That is what a certification body demanded on the factory
floor in Chapter 1, decades before anyone put a model in a plant.47
Small enough to read. Not fast enough — small enough, because the whole value
of determinism is that a person can examine the logic and know what it does in every
case. That is only achievable because the gate does not evaluate policy. If it did, it would
grow with every rule the organisation added and stop fitting the window the moment
the business got interesting. What reaches the boundary either satisfies a small fixed
set of conditions or does not, and that set is the same size whether the rulebook holds
ten rules or ten thousand.
Which raises the obvious question about the rulebook.

And the authority is already compiled
Start with the objection everything in this paper invites. If decisions commit in microseconds, and nobody is consulted, and nobody could have been — then who is in
charge?
Somebody is in charge, and they were in charge in October.
Nobody approved any individual snow route in Chapter 1. Somebody approved the
rules, in an oﬀice, over weeks, with a review process, a legal opinion, a council signoff and a version number. The salt budget. The school-zone deadline. The gradient
      IEC 61508-2, Clause 7.4.2.3: where a system executes both safety-related and non-safety-related functions, all hardware and software components shall be treated as safety-related unless adequate independence and separation between the functions can be demonstrated. The standard requires physical separation, dedicated execution memory and independent bus interfaces, such that a failure or memory corruption within the Basic Process Control System cannot prevent the Safety Instrumented System from transitioning the process to a verified safe state. ISO 13849-1 mirrors this architectural isolation for machinery,
requiring designated architecture Categories 3 and 4 and measures against Common Cause Failures.

threshold. The overtime limit. Every one a human decision, made deliberately, at human speed, months before the night it governed.
The human is in the loop. The loop is upstream. A pilot cannot bank an airliner more
steeply than the aircraft permits. There is nobody to appeal to at thirty thousand feet
and no time to appeal in. An engineer set that limit years earlier, on the ground, with
months to think about it — and the flight computer holds the pilot to it in milliseconds,
which is faster than the pilot could decide anything.
What that requires is translation. A policy as a human writes it — purchases above five
thousand dollars require a second approval, unless the supplier is pre-cleared, unless the item is
safety-critical — is prose, and prose cannot be evaluated in four hundred microseconds.
So it is compiled into a bounded instrument: explicit scope, named authority, validity
period, version. That instrument travels to the edge. Not the authority itself, which
stays where it was granted, but a scoped, expiring, revocable carrier of one permission,
to one place, for one period.
Authority does not distribute. It is declared centrally, compiled, and carried. Which
is how a system can be constitutionally unified and geographically distributed at the
same time — and it is not hypothetical. Millions of vehicles enforce rules written in one
place and updated over the air, and have for years.
Carrying it is also what makes the arithmetic work. Chapter 3 established that authority
checks accumulate like everything else: six consequential steps means six checks, and
six round trips to a central policy service is a hundred milliseconds of an agent sitting
still, waiting to be told about its own permissions. Carried authority collapses that to
six local reads. The 16:00 purchase fits in two milliseconds for that reason and no other.
One caveat carries straight into Part Three: the compilation never finishes. Every organisation on this surface runs a Compiled Region its machines enforce and an Uncompiled
Region its people still hold, and the frontier between them moves without ever closing.
So the surface already has two of the three layers. Nobody set out to build either one.
They arrived because engineers solving unrelated problems kept arriving at the same
answer.

The one thing nothing has
Which makes the absence conspicuous.
Every segment in Part Three enforces. Not one produces an account somebody else can
rely on. The grid gateway trips and the utility believes it because the utility specified it.
The safety cabinet halts a line and a certification body believes it because they certified
it. The lawyer’s box answers a question and she believes it because she owns it.
Take away the pre-existing relationship — put the device in a stranger’s building, running a stranger’s rule, on behalf of a party who has never inspected it — and there is
nothing left.

What independence means here is physical. Its own keys. Its own storage. Its own path
out. Disjoint enough that compromising the execution surface does not compromise the
account of what the execution surface did.
And it must never gate anything. This is the single most important property and the
easiest to get backwards.
       The EGK determines whether an action may proceed. The independent witness records what it can observe. If the witness becomes unavailable, authorised execution continues uninterrupted, and the resulting gap in independent evidence remains explicit and irrecoverable.
The temptation runs the other way. If the record matters, surely no action should proceed unwitnessed — and the argument sounds responsible right up to the moment you
deploy it. A witness that can halt production is a new single point of failure sitting directly in the execution path, and the first time it stops a line during a shift somebody
disconnects it. A witness that can be blamed for downtime will be removed. The only
witness that survives contact with an operations team is one that cannot cause any.
So when a contractor unplugs something in the wrong cabinet, as at the water plant
in Chapter 1, the plant keeps treating water. The record acquires two hours it does
not cover. Nobody backfills it, nobody interpolates it, and nobody later describes that
period as witnessed.
The gap is the output. That is unusual and worth stating plainly, because every logging system most engineers have worked with treats an outage as something to smooth
over. Here it is the honest result: somebody pulled a plug, execution continued under
authority, and the evidentiary record says so permanently. An evidentiary deficiency
is not an execution failure, and conflating the two produces a system that fails for the
wrong reasons.
It also removes a special case. One might otherwise need a carve-out for protective
actions — a protection relay must trip whether or not anything is recording, because
the alternative is the physical harm the whole arrangement exists to prevent. Under failopen witnessing no carve-out is required, because the witness was never in the path. A
narrow exception that has to be defined is a narrow exception that can be abused; better
architecture that needs none.
And if witnessing is genuinely cheap, there is no reason to deploy one. An operator could run three, from three vendors, each observing the same boundary and each
producing its own stream. None of them controls execution, so adding them adds no
dependency to the execution path. That is the property that makes redundancy sensible here and would not make it sensible for an interlock. One goes down and two keep
recording; the failed stream shows a gap. All three go down and authorised execution
continues under the kernel with no independent evidence for the period, which is the
same condition as having none at all and is recorded as such.
The interesting case is disagreement. If two streams differ about what happened, the
discrepancy is preserved rather than reconciled. A single authoritative record that

silently resolves conflicts is worse than three that argue, because the argument is information and the resolution is a guess.
Two qualifications, because the idea is more attractive than it is proven. Different vendors does not mean independent — three witnesses sharing a power supply, a network
path, an administrative domain or a storage system are one witness with three logos.
And the cost claim is a design objective rather than a measurement. Whether peraction cost, power draw and unit price are genuinely low enough for triple deployment
depends on benchmarks nobody has published.

Why an EGK is the only way the claim gets approved
The insurance claim from Chapter 1 is worth walking through properly, because it is
the cleanest demonstration of why this is an architecture rather than a preference.
An insurer wants to approve claims automatically. Say ten million a year. The determination on each one is the same question: is this covered, was the thing approving it
authorised to, at this amount, under the rule in force today.
There are only four ways to answer it.
A person answers it. Accurate, reviewable, and it costs somewhere between fifteen and
forty dollars per claim in loaded labour, and takes hours or days.48 Across ten million
claims that is a labour budget larger than the book. This is what automation was built
to escape.
A model answers it. An evaluator is asked whether the proposed approval complies
with policy. This is the approach most currently-shipping AI governance takes, and it
fails twice. It costs tokens — a policy review of a few thousand tokens, run on every
claim, is tens of billions of tokens a year for a function that produces a yes or a no. And
the answer cannot be examined. Asked in court why claim 4,182,663 was approved, the
insurer can produce the model’s output and nothing else. A model judging a model is
not a control. It is a second opinion with the same epistemic status as the first.
Nothing answers it, and the work happens afterwards. Sample the approvals monthly.
Cheap, and what most organisations actually do. It is also the sprayer failure from Chapter 6: a misconfigured threshold executes across the entire book before anyone reads a
report, and the review discovers a systematic error two hundred thousand claims after
it started.
Or an EGK answers it. A handful of structural checks against the compiled instrument
the agent is carrying. Four hundred microseconds. Effectively free — the marginal cost
is a few microseconds of an ordinary processor that was going to be idle anyway. Identical on every claim. Examinable, because it is small and deterministic and someone can

     † CAQH Index administrative cost reporting and US Bureau of Labor Statistics loaded labour calculations: direct administrative processing cost for manually adjudicating a complex claim ranges from $15
to $40 per transaction, reflecting 20 to 45 minutes of claims-adjuster review at fully loaded hourly rates
of $45 to $65 inclusive of benefits and administrative overhead. Fully automated electronic adjudication
executes at an administrative marginal cost below $1.50 per transaction. Drawn from the CAQH Index
series and BLS wage data.

read it. And it happens before the approval commits, which means the wrong answer is
prevented rather than discovered.
Those are the only four options, and three are disqualified on cost, verifiability, or both.
Fast, cheap, and defensible is not a combination the other three can produce. It is
what an EGK is for, and it is the reason the insurer can run ten million automated determinations a year at all rather than as a pilot.
Now add the witness, because the kernel alone is not suﬀicient. Without it, the insurer
has a control they cannot prove they ran — adequate for their own risk committee,
which trusts them, and inadequate for a regulator, a reinsurer, or a claimant’s lawyer,
all of whom are being asked to accept the insurer’s word about a decision the insurer
made in its own favour. The account has to come from somewhere the claims platform
cannot reach, or it is not evidence. It is a claim about a claim.
And without the compiled instrument, neither layer has anything to work with. The
kernel needs something to check. An account saying “the check passed” is meaningless
unless you can say which rule passed, in which version, granted by whom, and trace it
to the human decision it came from.

Why none of the three works alone
Taken apart, each fails predictably.
A kernel without a witness is enforcement nobody can verify — which is the execution
surface exactly as it stands today. The grid gateway, the safety relay, the vision system,
the sprayer: all of them enforce, and not one can prove it to anyone who was not already
trusting them. It is why the carrier in Chapter 7 could not sell execution despite owning
the best-sited facilities in the country.
A witness without a kernel is a log of things that already happened. This is most of
what is currently sold as AI governance: useful, well built, and structurally incapable
of stopping anything.
Either without compiled policy has nothing to operate on — no rule in a form the gate
can process in microseconds, and no way for the record to name which rule, in which
version, under whose authority.
They are not a stack of good ideas. They are a minimum set, and removing any one
collapses the other two.

What this means for the surface
The surface in Part Three is being built regardless. Chapter 9 is explicit about why. What
is in question is whether it becomes one thing or stays several million things.
A node with a kernel and a witness can be used by somebody who did not install
it, because what it produces is an account that travels — checkable by a party who
was never there, who did not inspect the premises, and who does not need to trust the
operator. That is the difference between an insurable asset and an uninsurable one, and
Chapter 7 showed that no amount of facility quality substitutes for it.

A node without them can only ever be used by its owner. Not because of any technical
limitation — the silicon is identical — but because nothing it produces means anything
to anyone else.
That is the whole of it. The mesh in Chapter 1 is not a mesh because the hardware is
dense. Density is not connection. It is a mesh only if a decision made in a stranger’s
shop can be relied on by somebody in another city, and that requires all three layers
present at the boundary where the decision happened.
Absent them, Chapter 1 describes something that looks like infrastructure from a distance and is not. Which is, precisely, what every failure in Chapter 10 turned out to
be.

What this chapter does not claim
It does not claim anyone will build this, or that it would be adopted if they did. The
next chapter is about why that is genuinely uncertain, and the honest answer there is
that it may not happen at all.
It does not claim novelty for the components. Every one has been built in some form —
compiled policy in access control and industrial safety, deterministic gates in payments
and grid protection, independent attestation in secure hardware and financial audit.
What has not been built is the assembly, at this scale, in a form that means the same
thing across different manufacturers, industries and countries.
It does not name an implementation, and it should not. The argument is that the category is necessary. Which particular kernel, which particular witness, and whose compilation toolchain are questions this paper has no business answering.
And it does not say what any of it is worth. A kernel that permits an action creates no
revenue by itself.
What it creates is the precondition, and the shape of that is worth naming before this
paper hands off.
Look again at what the agent was carrying at 16:00 in Chapter 1. An instrument scoped
to a category, capped at an amount, expiring on a date, stamped with a version. That is
already a spending limit. The same instrument that establishes whether an action may
proceed also establishes what it may cost, and the same witness that records the action
records the charge. Metering is not a second system bolted onto the governance layer.
It is the governance layer, read for a different purpose.
Which is why the economics follow this paper rather than precede it. A market in execution needs three things that do not exist today: capacity a stranger can verify, authority
that can be carried to the place where the money is actually spent, and a record both
sides can rely on afterwards. Those are what the last two chapters have described. Today the alternative is what the market already offers — bundled enterprise contracts
from a handful of suppliers, priced by instance and by the hour, on the two dimensions
that say nothing about whether a given machine can do a given job at all.

What the capacity is worth, how latency and jurisdiction would price it, and whether
an exchange clears are the questions the companion paper takes up.

PART FIVE — CLOSE

## Chapter 13 — Infrastructure or Property

Capitalism is working correctly
It would be easy to read the last three chapters as a story about market failure. It is not,
and the distinction matters. Every individual decision here is rational.
The store owner installs a node to cut costs and does not open it to strangers, because
an open interface means untrusted code running inside a network that also handles
payments. Correct. The buyer refuses to run a production system on an unverified box
in someone else’s shop. Correct. The underwriter declines to price a risk with no data
behind it. Correct. The vendor building a traﬀic controller has no incentive to make
it interoperable with a retail node, because their customer is a municipality and their
competitor is another traﬀic controller. Correct.
Nobody is behaving foolishly. Nobody needs to be persuaded to behave better. And
the collective outcome is that a genuinely useful capability sits unused.
Nobody wants to be the first to build a fitting that nothing else fits.
That is the whole of it, and it is a well-understood failure. A common interface is worth
more than it costs to build, and it still does not get built, because whoever goes first
pays for something the rest use free. Markets do not clear this on their own. It is not
ignorance, monopoly or bad faith. It is that the value of the thing stays invisible until
enough parties are already using it, and nobody can be the one who proves it.
Two mechanisms have broken that deadlock historically.
The container. Worthless unless everyone uses the same one, and no shipper could
justify standardising alone. It broke when Sea-Land released the patented corner casting and twistlock royalty-free, which made the fitting an international standard rather
than an owned one. Its inventor concluded a universal interface was worth more to him
than a proprietary one, and he was right. It still took about two decades.49
The classification society. Surveyors inspect to a published standard and maintain a
register. Then a party with pricing power — the underwriters — refuses to do business
with anything unlisted.
The first is a format. The second is an institution. This surface needs both, and only the
format can be published.

       ISO 668:1968 and ISO 1496. Sea-Land Service released Keith Tantlinger’s patented corner casting
and twistlock designs royalty-free to the American Standards Association and the International Organization for Standardization in the mid-1960s. Full global adoption and physical logistics conversion spanned
approximately two decades, from McLean’s initial Ideal X sailing in 1956 to generalised intermodal dominance in the late 1970s. —

The fragmentation is load-bearing
There is a harder version of this problem, and it is the strongest objection to everything
in this paper.
Chapter 9 argues that the hardware gets deployed because vendors build purposespecific appliances for specific verticals — a traﬀic controller, a store server, an industrial unit, a camp rack, a home appliance — each shaped around its own problem, certified for its own environment, sold into its own procurement system.
That mechanism is the only one that gets the hardware deployed at all. It is also the
mechanism that guarantees the result is incompatible.
So the fragmentation everyone treats as a transitional annoyance may not be transitional.
It may be the direct and permanent consequence of the only process that builds the
surface in the first place.
And a serious paper should say plainly that this can fail. Some coordination problems never resolve — there are still incompatible rail gauges, competing electrical plugs,
countries driving on different sides of the road. Persistent fragmentation is not an exotic
outcome. It is the normal one.
Three things would have to be true for this to resolve. Someone with pricing power
makes verified execution a condition of doing business — an insurer, a regulator, a
franchisor, or a dominant buyer. The interface is free, because a toll on a universal gate
guarantees that a competing gate gets built. And early adopters get some advantage
that does not depend on everyone else moving.
The third is the weakest, and it is where this argument is most vulnerable. Container
shipping had it: the ships were cheaper on day one, standard or not. Whether a node
that can prove its execution has any advantage before a market exists is an open question, and the honest answer today is that it mostly does not — except in the one place
where it already does, which is the owner’s own accountability. That was the second
item in the order of returns in Chapter 9, and it may turn out to be the thing that carries
the whole transition.

The argument in one pass
A planetary execution surface is being built now, continuously, from gigawatt campuses
down to milliwatt endpoints, thickest where consequences happen. It is being built by
thousands of unrelated parties who each need local execution for their own reasons
and would buy it if no market ever existed.
It is correctly sized for its owners’ peaks, which means it is idle most of the time. That
is structural and scale will not fix it.
And almost none of it can be used by anyone else, because nothing at these locations
produces an account a stranger can rely on.
Two things this does not mean. It does not mean a machine-speed economy is impossible without shared infrastructure — every organisation large enough to buy its own

silicon can run agents on its own hardware, under its own governance. The islands
work. They are simply islands. And it does not mean central computing is in decline.
Training, batch and deep reasoning stay central, permanently, and so do most tokens.
This is not a forecast of displacement.

What it does claim
Two things, different in kind.
The first is unconditional. High-consequence agentic action requires admissibility determined at the execution boundary and an account of what happened there, whether
or not anything is ever shared with anyone. An operator running entirely on their own
hardware, selling nothing, still needs both — for their regulator, their insurer, and their
own defence when a systematic error runs across an entire book before anyone reads a
report. That follows from the speed of the action and the liability of the owner. It does
not depend on markets existing.
The second is open. Whether that account can also be checked by a stranger determines
whether the surface is infrastructure or private property.

Where we actually are
Almost all high-consequence local execution today is non-discretionary. The grid gateway ramps to a pre-approved output. The safety relay trips at a threshold. The sprayer
classifies against a fixed model. The rule was set at commissioning by a person, certified,
and frozen.
What does not yet exist at scale is discretion at the boundary — agents holding real
authority over consequential physical and financial actions, choosing between options,
committing on behalf of a principal who is not watching. The retail supply order is
close. The maintenance budget is close. Almost nothing else is.
The threshold is discretion, not speed. A fast system following a fixed rule is an engineering problem and engineering has handled it for a century. A fast system exercising
judgment is a governance problem, and nothing currently deployed addresses it.
That is the transition, and it has not happened yet. The hardware is arriving first —
which is, on the evidence of every previous infrastructure cycle, exactly the order in
which these things happen.

The fork
The surface gets built either way. The silicon arrives on cycles already funded, for reasons already suﬀicient. Nothing in this paper is a prediction about whether it appears.
What is open is who can use it.
Without a way to check execution at an unverified location, every organisation large
enough to buy its own hardware will have a machine-speed economy, and everyone else
will rent human-speed access to somebody else’s. The capacity will exist — densely, in

every high street, every vehicle, every plant and every spare room — and it will serve
one party each.
With it, the same hardware becomes something closer to a utility.
The difference between those outcomes is not more silicon. It is not faster networks,
better models, or larger capital programmes. All of those are coming regardless and
none of them changes the answer.
It is whether a stranger can check what happened.

Author interest statement
The author is the founder of HyperEdgeX.ai, a company working on executionboundary governance and verification infrastructure for autonomous systems. This
paper names no implementation of any component it describes and argues only
that the architectural categories are necessary, not which instance of them should be
adopted. The analysis stands or falls on the evidence presented; readers should weigh
it accordingly.

A note on the references
Footnotes marked † rest on aggregated, secondary or industry-reported sources rather
than a single primary document, and are identified as such so the reader can weigh
them. Footnotes marked ‡ record figures that were accurate at the time of writing but
are expected to move — regulatory filings, deployment counts, market sizes and launch
schedules. Several claims in this paper are negative — that no standard does a given
thing, that no operator has reported a given revenue — and negative claims cannot be
proved by citation. Each is scoped as narrowly as the evidence allows and dated.
