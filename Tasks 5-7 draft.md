# Lumen / Ivy: Tasks 5 to 7 (draft)

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
