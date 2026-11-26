# TRP2 Week 0 Delivery Challenge: Lumen Studios and Ivy

Prepared by Kidus · 26 November 2026

**Scoring sheet for Tasks 3 and 4:** [Ivy eval scoring sheet](https://docs.google.com/spreadsheets/d/1lKSXelr2JLTVitRUuPab9uEbaOF2YoRoqcUobUsESfs/edit)

**Code and data (GitHub):** [github.com/kidusw/lumen-ivy-delivery-challenge](https://github.com/kidusw/lumen-ivy-delivery-challenge)

**Data used:** the Lumen Data Extract, including the fact sheet, the email thread, Conversations (429 Ivy messages, 19 Oct to 19 Nov 2026), Leads (250 leads), Owner complaints, Vendor eval and the Eval set. The "Evidence" tab of the scoring sheet shows how each number was counted.

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

**Where the goals conflict and how I would resolve it**

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


---

## Task 3: Build an eval

Scoring sheet: [Ivy eval scoring sheet](https://docs.google.com/spreadsheets/d/1lKSXelr2JLTVitRUuPab9uEbaOF2YoRoqcUobUsESfs/edit) (tabs "Criteria", "Scoring", and "Evidence" for the live-traffic counts behind Task 2). A reply passes overall only if it passes all four criteria. The reference for each reply is the fact sheet and the reply staff actually sent.

| Criterion | Business priority it protects | Pass or fail rule | Ivy pass rate (out of 20) |
|---|---|---|---|
| C1 Safe handoff | #2 owner retention, #3 safe handling | If the lead raises a refund or billing issue, an injury or health question, asks for a person, or asks Ivy to stop: pass only if the reply passes it to staff (or stops) and does not sell. Other messages pass. | 16/20 (80%). All 4 cases that needed a handoff failed |
| C2 Correct facts | #1 memberships, #3 correctness | Pass only if every price and policy stated matches the fact sheet for the lead's country. | 15/20 (75%) |
| C3 Right channel | #1 memberships | Pass only if the reply goes out on the channel the lead used. | 18/20 (90%) |
| C4 Answers what was asked | #1 memberships | Pass only if the reply addresses the lead's actual question or request. A generic pitch fails. | 16/20 (80%) |
| **Overall (passes all four)** | | | **9/20 (45%)** |

Ivy's overall score is 9 of 20 (45%). It differs from the vendor's 92% because the vendor measured something else. Brightline wrote its own 50 test questions before launch, all about class times and studio locations, with only 25 distinct questions. A reply passed if it was friendly, grammatical and answered the question, and nobody checked whether the answer was true. No test covered prices, policies, refunds, injuries, requests for a person, Canada or channel, which is where every one of Ivy's 11 failures falls. My 20 cases are deliberately hard, so 45% is not Ivy's live rate.

*Word count: 98*

---

## Task 4: Test a new AI model


Scoring sheet: [Ivy eval scoring sheet](https://docs.google.com/spreadsheets/d/1lKSXelr2JLTVitRUuPab9uEbaOF2YoRoqcUobUsESfs/edit), tab "Task 4 new model" (all 20 replies, pass or fail per criterion, with reasons).
How it was run: a script sent the same system prompt (Ivy's role plus the full fact sheet) and the same 20 lead messages, one request each, to Gemini 4 Hydrogen on Google's free API tier on 25 Nov 2026. No extra instructions were added, so the test measures the model, not our prompt fixes.

| Criterion | Ivy pass rate | New model pass rate (Gemini 4 Hydrogen) |
|---|---|---|
| C1 Safe handoff | 16/20 (80%) | 19/20 (95%) |
| C2 Correct facts | 15/20 (75%) | 20/20 (100%) |
| C3 Right channel | 18/20 (90%) | 18/20 (90%)* |
| C4 Answers what was asked | 16/20 (80%) | 18/20 (90%) |
| **Overall (passes all 4)** | **9/20 (45%)** | **16/20 (80%)** |

(*) Ivy's routing system picks the reply channel, not the model, so E10 and E11 still go to the wrong channel after a model swap.

Model: Gemini 4 Hydrogen (Google, released 12 November 2026), tested on its free tier with the same fact sheet and 20 messages. Better: every price and policy was correct (Ivy got 5 wrong), and it passed injury, refund and call-back requests to staff instead of pitching. Worse: with no booking or schedule data it asked which studio instead of booking or answering (E11, E18), its emails ran long, and on a complaint it told the lead to reply STOP instead of stopping. What I caught: it told Theo, Jade and Kai "I've passed this to staff", but nothing in Ivy actually sends that hand-off, so staff would never hear: the exact failure behind Maria and Kevin. A new model also leaves wrong-channel and duplicate texts untouched. My answer to Marcus: not yet. Fix routing first with existing tools, then re-run this eval and price the model after the board.

*Word count: 149*

---


## Task 5: Spec for one fix: reply on the channel the lead used

**Problem, with evidence from the data**
Ivy answered 52 of 150 SMS leads (35%) by email. Only 4 of them (7.7%) replied and none bought a membership, against 33 of 98 (34%) answered by SMS. Email leads were always answered correctly.

**Business priority it serves**
Priority 1: turn new leads into paying members.

**What will change**
Every Ivy message, including follow-ups and staff-edited drafts, is sent on the lead's "Channel the lead used". If an SMS fails, Ivy sends one email and logs why. Existing tools only.

**Acceptance criteria**
1. Given an SMS lead, when Ivy sends any message, then it goes by SMS.
2. Given an email lead, when Ivy sends any message, then it goes by email.
3. Given an SMS send fails, when Ivy retries, then it sends one email and logs "SMS failed" with the lead ID.
4. Given staff edit a draft for an SMS lead, when they send it, then it goes by SMS.
5. Given the last 4 weeks replayed in testing, when the fix is applied, then 0 of 429 messages use the wrong channel, apart from logged fallbacks.

**Out of scope**
Duplicates, staff handoffs, Canadian prices, wording, model changes (separate tickets).

**How we will know it worked after launch**
Weekly report: wrong-channel messages at 0% (logged fallbacks under 2%). Within 4 weeks, SMS-lead replies rise from 25% (37 of 150) toward 34%, with trials and memberships compared against the previous 4 weeks.

*Word count: 241*

---

## Task 6: Email to Dana

**Subject: Ivy: my recommendation for the board**

Hi Dana,

**My recommendation: keep Ivy, but judge it on memberships, not the 31%, and give us two weeks to fix three specific faults. None of them needs new spending.**

**What is really going on**

The 31% counts every lead who replied, complaints included. What pays the owners is far lower:

| Last 4 weeks, 250 leads | Count | Rate |
|---|---|---|
| Replied, or went further (the dashboard's 31%) | 78 | 31% |
| Booked a trial | 23 | 9% |
| Bought a membership | 8 | 3% |

Three faults explain most of the owners' anger:

1. **Ivy never hands people to staff.** 20 people asked about refunds or injuries, or asked for a call back. Ivy passed none on and sent each a sales pitch. Half were at the 11 studios renewing in March.
2. **Wrong channel.** A third of leads who texted got Ivy's answer by email. Only 8% of them replied, against 34% answered by text.
3. **Duplicate texts.** 34 leads (14%) got the same message twice, seconds apart.

7 of the owners' 8 complaints match these records.

**Next two weeks**
- Week 1: route refunds, injuries and requests for a person to studio staff, and stop the duplicate texts.
- Week 2: reply on the lead's own channel and fix the Canadian intro price (Ivy quotes $99 instead of CA$109).
- Weekly membership reports to you and Priya.

**Fallback:** if a fix is not live before the board meets, staff approve every Ivy message at the 11 renewing studios before it is sent, using the draft review step they already use.

**What I'm sure of, and what I'm not yet**
I'm sure of the counts above. I don't yet know how many leads became members before Ivy, or whether the wrong channel causes the low replies. Four weeks may also be too short for some leads to buy. Booking records from before launch, and results after the fix, will answer this.

**Marcus's model idea**
I tested a model Google released on 12 November on 20 hard cases. It scored 80% against Ivy's 45%, with every price right. But it told upset customers "I've passed this to staff" when nothing would reach staff, and it cannot fix the channel or duplicates. My answer is not yet: fix these first, then retest after the board.

**Priya and the owners**
They were right. Their studios get the fixes first, with weekly numbers before March.

Selam

*Word count: 399*

---

## Task 7: Reflection and reuse

**1. What I changed my mind about.** I expected the new model to fix handoffs, since it answered injury and refund requests politely. Its replies changed my mind: it told three people "I've passed this to staff" when nothing in Ivy sends that message. A better-sounding model would hide the failure. The problem is plumbing, not wording.

**2. What I would hand to the next engineer.** A first-week kit for any new client:
- **Check the numbers:** trace every quoted metric to what the business is paid for.
- **Check the behaviour:** test real logs against the client's rules before judging wording.
- **Reuse the tools:** an eval template tied to business priorities and a model-test harness.
- **Listen before solving:** ask each stakeholder what success means and what they fear; treat proposed fixes as hypotheses.
- **Ask questions whose answers change the plan**; say "I don't know yet, here's how I'll find out."

*Word count: 149*
