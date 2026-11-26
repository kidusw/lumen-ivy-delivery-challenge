# Task 4: Test a new AI model (draft)

Scoring sheet: *Ivy eval scoring sheet (Task 3).xlsx*, tab "Task 4 new model" (all 20 replies, pass/fail per criterion, reasons).
How it was run: `run_task4.py` sent the same system prompt (Ivy's role plus the full fact sheet) and the same 20 lead messages, one request each, to `gemini-4-hydrogen` on the free Gemini API tier on 25 Nov 2026. Raw replies are in `task4_replies.csv`.

| Criterion | Ivy pass rate | New model pass rate (Gemini 4 Hydrogen) |
|---|---|---|
| C1 Safe handoff | 16/20 (80%) | 19/20 (95%) |
| C2 Correct facts | 15/20 (75%) | 20/20 (100%) |
| C3 Right channel | 18/20 (90%) | 18/20 (90%)* |
| C4 Answers what was asked | 16/20 (80%) | 18/20 (90%) |
| **Overall (passes all 4)** | **9/20 (45%)** | **16/20 (80%)** |

*Ivy's routing system picks the reply channel, not the model, so E10 and E11 still go to the wrong channel after a model swap.

Model: Gemini 4 Hydrogen (Google, released 12 November 2026), tested on its free tier with the same fact sheet and 20 messages. Better: every price and policy was correct (Ivy got 5 wrong), and it passed injury, refund and call-back requests to staff instead of pitching. Worse: with no booking or schedule data it asked which studio instead of booking or answering (E11, E18), its emails ran long, and on a complaint it told the lead to reply STOP instead of stopping. What I caught: it told Theo, Jade and Kai "I've passed this to staff", but nothing in Ivy actually sends that hand-off, so staff would never hear: the exact failure behind Maria and Kevin. A new model also leaves wrong-channel and duplicate texts untouched. My answer to Marcus: not yet. Fix routing first with existing tools, then re-run this eval and price the model after the board.

*Word count: 149*

---
Notes for you (not part of the submission):
- Test limits worth one line if you have room: the model got the fact sheet only, with no studio, schedule or booking access (this explains E11 and E18). The free tier allows 20 requests a day per project, and busy errors count toward it, so the run took three API projects. That is also a sign it isn't production-ready on free terms.
- Possible Task 7 material: I expected the model's handoff answers to be the big win, but they turned out to be the riskiest part, because the replies promise a handoff that nothing performs.
