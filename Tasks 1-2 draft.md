# Lumen / Ivy: Tasks 1 and 2 (draft)

Source for every number: *TRP2 W0 Delivery Challenge – Lumen Data Extract* (fact sheet, email thread, Conversations: 429 messages from 19 Oct to 19 Nov 2026, Leads: 250 leads, Owner complaints). How each number was counted is on the Evidence tab of the Task 3 scoring sheet.

---

## Task 1: Understand what the business wants

### 1a. Business priorities

| Rank | What the business needs | Who wants it | Why it matters (use a number if you can) |
|---|---|---|---|
| 1 | **Turn more new leads into paying members** | Franchise owners (Priya), Dana, Lumen HQ | Owners earn their money from memberships, and Lumen takes a 7% royalty. One unlimited member is worth about $2,086 to a studio ($149 × 14 months on average) and about $146 to Lumen. Today only 8 of 250 leads (3.2%) bought a membership. |
| 2 | **Keep franchise owners in the network and paying for Ivy** | Priya and the owners, Dana | 11 of the 40 studios renew on 31 Mar 2027, and 5 of the 6 owners who complained are among them. Those 11 studios pay $66,000 a year in technology fees, and two owners are talking about leaving the network, which would also end their royalties. |
| 3 | **Handle every lead safely and correctly**: pass refunds, billing, injuries and requests for a person to staff, and quote the right prices | Owners, their front-desk staff, Lumen policy | It is written policy. Mishandled leads walk into studios angry and leave one-star reviews, which hurts both #1 and #2. |
| 4 | **Give the board an honest answer it can defend** | Dana, the board | The board meets in two weeks. Dana has already given the CEO a 31% figure that counts replies, not sales. |
| 5 | **Fix things with the budget and tools Lumen already has** | Finance (Tom) | No new spending, contracts or vendor changes before the board meets. Ivy already costs about $6,000 a month. |

*Not a business priority:* switching to a new AI model (Marcus). That is a proposed solution, and its value has to be shown against priorities 1–3.

**Where the goals conflict and how I'd resolve it** (≈150-word limit)

Dana wants one number to settle "keep or switch off". Owners care only about paid memberships. Marcus wants a model switch live before the board, but Finance has frozen new spending, and a rushed change would add risk two weeks before renewal talks. Pushing every lead hard toward a sale (#1) clashes with handing upset or injured leads to staff (#3). I would resolve it in this order. First, safety and trust (#3), because broken rules drive the owner anger behind #2. Then conversion fixes that cost nothing (#1). Then report memberships, not replies, to the board (#4). The model question waits until those fixes ship and can be tested with the same eval, using existing budget (#5). The board gets "keep Ivy, fix these three things, judge it on memberships", with a fallback of staff approving every Ivy message at the renewing studios until fixes ship.

*Word count: 147*

### 1b. Discovery questions (first call with Dana and Priya)

| # | Question | Who you would ask | What answer would change your plan, and how |
|---|---|---|---|
| 1 | Before Ivy launched, what share of new leads became paying members, and how quickly did staff reply to them? | Dana (and Priya for her studios) | If it was above today's 3.2%, Ivy may be hurting sales, and pausing it at the worst studios becomes a serious option for the board. If it was lower, the case is to fix Ivy, not remove it. |
| 2 | Priya mentioned two owners who may leave and others who won't pay for Ivy again. Which studios are they, and for each one, is the deal-breaker the ignored call-backs and refunds, or the duplicate texts? | Priya | Her note gives numbers but no names or causes. If it is mainly ignored call-backs, the staff-handoff fix goes first. If it is duplicates, that goes first. Either way, I would roll the fixes out at their studios first and show them results before March. |
| 3 | When Ivy "passes something to staff", where does it actually go (inbox, booking system, phone), and who checks it? | Dana | If nobody owns that queue, fixing Ivy's routing alone won't help. We would need a named owner and a daily check at each studio, which is process work, not code. |
| 4 | Is the channel Ivy replies on decided by Ivy, the booking system, or the lead form, and can we change it without the old vendor? | Dana (or whoever holds the system access) | If it is a setting we can change, it is the cheapest conversion fix and goes first. If it needs vendor code we don't have, I would move it later and start with the handoff fix. |
| 5 | Can membership sales in the booking system be linked back to the lead ID, and how long does a lead usually take to buy? | Dana | If sales can't be linked, the board number has to be "trials attended" until we add that link. If leads take more than 4 weeks to buy, today's 3.2% understates Ivy, and I would say so. |

---

## Task 2: Find out what is really going on

Ranked by business impact, not by how often each happens.

| # | Issue | Evidence (numbers from the data) | Business priority it affects (from Task 1) | Impact | Confidence |
|---|---|---|---|---|---|
| 1 | **Ivy never hands sensitive messages to staff.** It answers refunds, billing, injuries and requests for a person with a sales pitch. | 0 of 20 such messages were handed to staff (11 complaints, 9 asked for a person). That includes the knee injury, the double charges and the manager call-back that owners raised. 10 of the 20 came from the 11 studios renewing in March. Staff edited only 2 of them. On the eval set, 0 of 4 escalation drafts were safe. | #3 safety; #2 owner retention | Highest owner anger. 7 of the 8 owner complaints trace to this issue or to duplicates. Risk of losing studios at the March renewal. | High |
| 2 | **Ivy replies on the wrong channel.** Leads who text get their reply by email. | 52 of 150 SMS leads (35%) were answered by email. Only 4 of those 52 (7.7%) ever replied and none bought, compared with 33 of 98 (34%) replying and 8 memberships for leads answered on the right channel. Email leads were always answered correctly. | #1 memberships | About a third of SMS leads are effectively lost. If they replied like correctly-routed leads, about 13 more of them would reply. | High that it happens; medium that it causes the drop (correlation, no A/B test) |
| 3 | **The 31% "conversion rate" counts replies, not sales.** | 78 of 250 leads "replied or further" = 31.2%. Only 23 (9.2%) booked a trial and 8 (3.2%) bought a membership. 19 of the 78 "conversions" were complaints or requests for a human, such as "Stop sending me the same message." | #4 honest board answer; #1 | The board could keep or cut Ivy based on the wrong number. Dana has already quoted it to the CEO. | High |
| 4 | **Duplicate messages.** The same text is sent twice, seconds apart. | 34 of 250 leads (14%) got an identical message twice, 2–6 seconds apart, at 26 studios and in every week. 6 of the 8 owner complaints mention duplicates. | #2 owner retention; #3 | Looks like spam, and front-desk staff spend time apologising. Visible to every owner. | High |
| 5 | **Ivy gives wrong prices and policies.** | All 23 Canadian messages that mention the intro month quote US $99 instead of CA$109. On the eval set, 5 of 20 drafts misstated a price or policy (unlimited $129, intro $79, packs "never expire", "cancel with no notice", "free unlimited freezes"). Staff currently fix 71% of pricing and cancellation replies by hand. | #3 correctness; #1 | Broken promises lead to refund disputes, and staff time is spent correcting Ivy. | High (Canada); medium (how often it happens across all traffic) |
| 6 | **The vendor's 92% did not test the hard cases, and Ivy reuses fixed templates.** | The vendor tested 50 self-written questions (only 25 distinct), on class schedules and locations only, with no fact check. Those topics are 28% of real traffic. 8 fixed templates produce 358 of 429 messages, often ignoring the question asked (for example, "sign-up fees?" gets the unlimited price). On harder cases Ivy scores 9 of 20 (45%). | #4; #1 | The "robotic" feel comes from the templates and logic, not the model's language. A model switch alone would not fix issues 1–5. | Medium–High |

*Not ranked (low confidence):* 36 of 176 SMS messages went out between 9 pm and 8 am. The timezone of the timestamps is unknown, so this needs checking before anyone relies on it.
