# Lumen Studios and Ivy: TRP2 Week 0 Delivery Challenge

This repo holds my work on the TRP2 Week 0 Delivery Challenge. Lumen Studios is a network of 40 franchised fitness studios. Ivy is the AI agent it uses to follow up with new leads. The task was to work out what the business needs, find out what is really happening with Ivy, build an eval, test a newer model, and recommend what to do before the board meets.

- **Submission (Google Doc):** https://docs.google.com/document/d/1-E2fRh-nuzVzBBW0dkErKmsDM7tSOoi812QDvfqPdCE/edit
- **Scoring sheet (Google Sheet, Tasks 3 and 4):** https://docs.google.com/spreadsheets/d/1lKSXelr2JLTVitRUuPab9uEbaOF2YoRoqcUobUsESfs/edit

## Main findings

- The dashboard's 31% "conversion rate" counts leads who replied, complaints included. Only 8 of 250 leads (3.2%) bought a membership.
- Ivy handed 0 of 20 refund, injury and "speak to a person" messages to staff.
- 52 of 150 SMS leads got their reply by email. Only 7.7% of them replied, against 34% of leads answered on the right channel.
- On a 20-case eval with four pass/fail criteria, Ivy passes 9 of 20 (45%). Gemini 4 Hydrogen passes 16 of 20 (80%), but it still cannot fix routing or duplicate messages. So the recommendation is to fix those first and retest the model after the board meeting.

## What is in this repo

| File | What it is |
|---|---|
| `Lumen Ivy - Delivery Challenge submission.md` / `.docx` / `(preview).pdf` | The full submission (Tasks 1 to 7) |
| `Ivy eval scoring sheet (Task 3).xlsx` | Eval criteria, per-reply scoring, evidence counts and the Task 4 model comparison |
| `run_task4.py` | Sends the 20 eval conversations to a Gemini model with Ivy's prompt and fact sheet |
| `task4_replies.csv` | The 20 replies from Gemini 4 Hydrogen used in Task 4 |
| `task4_cache_gemini-4-hydrogen.json` | Cached API responses, so the run can resume without spending quota again |
| `Task 4 prompt pack.md` | The system prompt and the 20 eval messages, for a manual run |
| `Tasks 1-2 draft.md`, `Task 4 draft.md`, `Tasks 5-7 draft.md` | Working drafts of each section |

## Re-running the Task 4 model test

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env   # then add your own GEMINI_API_KEY to .env
python run_task4.py
```

The script reads the key from `.env`, which is git-ignored. It waits between requests and stops cleanly if the free-tier daily quota runs out. Cached replies are reused on the next run.
