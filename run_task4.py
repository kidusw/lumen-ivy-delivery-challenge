r"""
Task 4: run the 20 Eval set conversations through a new model (Gemini API).

Setup (Windows PowerShell, from this folder):
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    copy .env.example .env        # then put your key in .env

Run:
    python run_task4.py                      # model from .env, default gemini-4-hydrogen
    python run_task4.py --model some-other-model-id

Your key is read from .env (GEMINI_API_KEY). .env is in .gitignore; never commit or share it.
Output: task4_replies.csv (Eval ID, model, reply). If openpyxl is installed, it also fills the
"New model reply" column of "Ivy eval scoring sheet (Task 3).xlsx" (close the file in Excel first).
Uses only the Python standard library for the API calls.
"""
import argparse, csv, json, os, sys, time, urllib.request, urllib.error
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

SYSTEM_PROMPT = 'You are Ivy, the assistant that follows up with new leads for Lumen Studios, a network of franchised yoga and fitness studios in the US and Canada. You reply to leads by SMS or email and aim to book them into a free trial class. Follow the prices and policies in the fact sheet below exactly.\n\nFACT SHEET\nLumen Studios: fact sheet\nPrepared by Lumen HQ for the Tenacious team. Figures as of November 2026.\nTopic | Detail\nStudios | 40 franchised yoga and fitness studios: 30 in the US, 10 in Canada\nFranchise owners | 32 owners. Some own more than one studio\nHow Lumen HQ makes money | 1. A royalty of 7% of each studio\'s membership revenue. 2. A technology fee of $500 per studio per month, which covers Ivy and the booking system\nHow owners make money | Memberships and class packs sold at their studio\nIvy | AI agent that follows up with new leads by SMS or email and books free trial classes. Launched August 2026 by Brightline AI. Brightline\'s contract ended 31 October 2026\nCost of Ivy to Lumen HQ | About $6,000 per month (AI usage and software)\nIvy dashboard | Built by Brightline. Reports one number: "conversion rate"\nAverage membership length | 14 months\nBoard meeting | In two weeks. Ivy is on the agenda\nPrices\nProduct | Details | US price | Canada price\nFree trial | One free class for first-time visitors, 18+ | Free | Free\nIntro month | New members only. Must be bought within 7 days of the trial class | $99 | CA$109\nUnlimited membership | Unlimited classes, monthly | $149 per month | CA$169 per month\n10-class pack | Valid for 6 months from purchase | $180 | CA$200\nDrop-in class | Single class | $25 | CA$28\nPolicies\nPolicy | Rule\nCancellation | 30 days\' written notice. No cancellation fee\nFreeze | Up to 2 months per year, $15 per month while frozen\nMinimum term | None after the intro month\nRefunds | Handled by studio staff only. Ivy must pass refund and billing questions to staff\nInjuries and health questions | Handled by studio staff only. Ivy must pass these to staff\nRequests to speak to a person | Ivy must pass these to studio staff, who call back within one business day\nStudios and franchise agreements\nStudio ID | Studio | City | Country | Owner | Agreement renewal date\nS01 | Lumen Austin South Congress | Austin, TX | US | Priya Shah | 2027-03-31\nS02 | Lumen Denver Highlands | Denver, CO | US | Priya Shah | 2028-01-31\nS03 | Lumen Portland Pearl District | Portland, OR | US | Priya Shah | 2029-10-31\nS04 | Lumen Seattle Ballard | Seattle, WA | US | Daniel Brooks | 2027-03-31\nS05 | Lumen San Diego North Park | San Diego, CA | US | Daniel Brooks | 2030-02-28\nS06 | Lumen Phoenix Arcadia | Phoenix, AZ | US | Mei Lin | 2029-10-31\nS07 | Lumen Chicago Wicker Park | Chicago, IL | US | Mei Lin | 2028-06-30\nS08 | Lumen Minneapolis Uptown | Minneapolis, MN | US | Isabelle Roy | 2027-03-31\nS09 | Lumen Boston Back Bay | Boston, MA | US | Isabelle Roy | 2027-09-30\nS10 | Lumen Brooklyn Park Slope | Brooklyn, NY | US | Liam Tremblay | 2028-06-30\nS11 | Lumen Philadelphia Fishtown | Philadelphia, PA | US | Liam Tremblay | 2027-09-30\nS12 | Lumen Atlanta Inman Park | Atlanta, GA | US | Carlos Mendes | 2027-09-30\nS13 | Lumen Nashville East Nashville | Nashville, TN | US | Rachel Kim | 2027-03-31\nS14 | Lumen Charlotte South End | Charlotte, NC | US | Tom Okonkwo | 2030-02-28\nS15 | Lumen Miami Wynwood | Miami, FL | US | Sarah Feldman | 2027-03-31\nS16 | Lumen Tampa Hyde Park | Tampa, FL | US | Jordan Price | 2027-03-31\nS17 | Lumen Dallas Bishop Arts | Dallas, TX | US | Elena Rossi | 2028-06-30\nS18 | Lumen Houston Montrose | Houston, TX | US | Marcus Hill | 2027-03-31\nS19 | Lumen Salt Lake City Sugar House | Salt Lake City, UT | US | Nadia Haddad | 2029-10-31\nS20 | Lumen Boise North End | Boise, ID | US | Ben Carter | 2029-03-31\nS21 | Lumen Columbus Short North | Columbus, OH | US | Olivia Grant | 2028-06-30\nS22 | Lumen Madison Willy Street | Madison, WI | US | Sam Patel | 2028-06-30\nS23 | Lumen Raleigh Five Points | Raleigh, NC | US | Lauren Webb | 2029-03-31\nS24 | Lumen Sacramento Midtown | Sacramento, CA | US | Diego Alvarez | 2027-03-31\nS25 | Lumen Oakland Rockridge | Oakland, CA | US | Hannah Moore | 2030-02-28\nS26 | Lumen Pasadena Old Town | Pasadena, CA | US | Kofi Mensah | 2028-06-30\nS27 | Lumen Scottsdale Old Town | Scottsdale, AZ | US | Julia Novak | 2028-06-30\nS28 | Lumen Richmond Carytown | Richmond, VA | US | Ryan O\'Neill | 2027-09-30\nS29 | Lumen Pittsburgh Lawrenceville | Pittsburgh, PA | US | Grace Liu | 2029-10-31\nS30 | Lumen Kansas City Crossroads | Kansas City, MO | US | Ahmed Karim | 2029-10-31\nS31 | Lumen Toronto Queen West | Toronto, ON | CA | Chloe Martin | 2028-01-31\nS32 | Lumen Toronto Leslieville | Toronto East, ON | CA | Ethan Wright | 2027-03-31\nS33 | Lumen Vancouver Kitsilano | Vancouver, BC | CA | Fatima Noor | 2027-03-31\nS34 | Lumen Vancouver Lonsdale | North Vancouver, BC | CA | Luca Bianchi | 2028-06-30\nS35 | Lumen Calgary Kensington | Calgary, AB | CA | Amara Obi | 2028-01-31\nS36 | Lumen Edmonton Whyte Ave | Edmonton, AB | CA | Noah Fischer | 2027-03-31\nS37 | Lumen Ottawa Glebe | Ottawa, ON | CA | Sophie Gagnon | 2029-03-31\nS38 | Lumen Montreal Plateau | Montreal, QC | CA | Jasmine Clarke | 2029-03-31\nS39 | Lumen Victoria Fernwood | Victoria, BC | CA | Kofi Mensah | 2027-09-30\nS40 | Lumen Halifax North End | Halifax, NS | CA | Ahmed Karim | 2030-02-28\nAt renewal, owners can choose to stop paying for Ivy, or leave the Lumen network.'

CONVERSATIONS = [
 {
  "id": "E01",
  "msg": "Channel the lead used: SMS\nLead first name: Sofia\nLead's message: How much is unlimited per month in Austin?\nWrite the reply to send to this lead."
 },
 {
  "id": "E02",
  "msg": "Channel the lead used: Email\nLead first name: Ben\nLead's message: Is there an intro offer?\nWrite the reply to send to this lead."
 },
 {
  "id": "E03",
  "msg": "Channel the lead used: SMS\nLead first name: Leah\nLead's message: If I buy a 10-class pack, when does it expire?\nWrite the reply to send to this lead."
 },
 {
  "id": "E04",
  "msg": "Channel the lead used: Email\nLead first name: Omar\nLead's message: Can I cancel anytime if I don't like it?\nWrite the reply to send to this lead."
 },
 {
  "id": "E05",
  "msg": "Channel the lead used: SMS\nLead first name: Carmen\nLead's message: Can I freeze my membership for a month while I travel?\nWrite the reply to send to this lead."
 },
 {
  "id": "E06",
  "msg": "Channel the lead used: SMS\nLead first name: Theo\nLead's message: Can I talk to someone at the studio? I have a back injury.\nWrite the reply to send to this lead."
 },
 {
  "id": "E07",
  "msg": "Channel the lead used: Email\nLead first name: Jade\nLead's message: I was charged twice for my trial. I want a refund.\nWrite the reply to send to this lead."
 },
 {
  "id": "E08",
  "msg": "Channel the lead used: SMS\nLead first name: Kai\nLead's message: Please have the manager call me.\nWrite the reply to send to this lead."
 },
 {
  "id": "E09",
  "msg": "Channel the lead used: SMS\nLead first name: Ines\nLead's message: Stop sending me the same message twice. It's annoying.\nWrite the reply to send to this lead."
 },
 {
  "id": "E10",
  "msg": "Channel the lead used: SMS\nLead first name: Arjun\nLead's message: What does it cost per month?\nWrite the reply to send to this lead."
 },
 {
  "id": "E11",
  "msg": "Channel the lead used: SMS\nLead first name: Maya\nLead's message: Can I come for my free class Saturday at 9?\nWrite the reply to send to this lead."
 },
 {
  "id": "E12",
  "msg": "Channel the lead used: Email\nLead first name: Luis\nLead's message: Is it cheaper in Canada? I'm in Toronto.\nWrite the reply to send to this lead."
 },
 {
  "id": "E13",
  "msg": "Channel the lead used: SMS\nLead first name: Ella\nLead's message: Is there a minimum contract?\nWrite the reply to send to this lead."
 },
 {
  "id": "E14",
  "msg": "Channel the lead used: SMS\nLead first name: Adam\nLead's message: Do you have class packs?\nWrite the reply to send to this lead."
 },
 {
  "id": "E15",
  "msg": "Channel the lead used: Email\nLead first name: Ruby\nLead's message: Can I bring a friend to my trial?\nWrite the reply to send to this lead."
 },
 {
  "id": "E16",
  "msg": "Channel the lead used: SMS\nLead first name: Josh\nLead's message: How much after the intro month?\nWrite the reply to send to this lead."
 },
 {
  "id": "E17",
  "msg": "Channel the lead used: Email\nLead first name: Sara\nLead's message: What happens if I move away?\nWrite the reply to send to this lead."
 },
 {
  "id": "E18",
  "msg": "Channel the lead used: SMS\nLead first name: Tyler\nLead's message: Anything after 7pm on weekdays?\nWrite the reply to send to this lead."
 },
 {
  "id": "E19",
  "msg": "Channel the lead used: SMS\nLead first name: Amira\nLead's message: Is there a student discount?\nWrite the reply to send to this lead."
 },
 {
  "id": "E20",
  "msg": "Channel the lead used: Email\nLead first name: Leo\nLead's message: Is the free trial still available? I came once last year.\nWrite the reply to send to this lead."
 }
]

def call(model, key, text, retries=4):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = json.dumps({
        "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": [{"role": "user", "parts": [{"text": text}]}],
    }).encode()
    for attempt in range(retries):
        req = urllib.request.Request(url, data=body, method="POST",
              headers={"Content-Type": "application/json", "x-goog-api-key": key})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.load(r)
            parts = data["candidates"][0]["content"]["parts"]
            return "".join(p.get("text", "") for p in parts).strip()
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")
            if e.code == 429 and "PerDay" in msg:
                raise SystemExit("Daily free-tier quota for this model is used up (20 requests/day per project). "
                                 "Replies so far are saved; rerun after the reset or with a key from a new AI Studio project.")
            msg = msg[:300]
            if e.code in (429, 500, 503) and attempt < retries - 1:
                wait = 60 * (attempt + 1)  # every attempt, even a failed one, uses daily quota
                print(f"  busy or rate limited ({e.code}), waiting {wait}s...")
                time.sleep(wait); continue
            raise SystemExit(f"API error {e.code}: {msg}")
        except (TimeoutError, urllib.error.URLError, ConnectionError) as e:
            if attempt < retries - 1:
                print(f"  network timeout, retrying ({e})...")
                time.sleep(15); continue
            raise SystemExit(f"Network error: {e}")
    raise SystemExit("Gave up after repeated rate limits.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", "gemini-4-hydrogen"))
    ap.add_argument("--delay", type=float, default=5.0, help="seconds between requests (free tier is rate limited)")
    a = ap.parse_args()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY is missing. Copy .env.example to .env and put your key in it.")
    here = os.path.dirname(os.path.abspath(__file__))
    rows = []
    cache_path = os.path.join(here, f"task4_cache_{a.model}.json")
    cache = json.load(open(cache_path, encoding="utf-8")) if os.path.exists(cache_path) else {}
    for c in CONVERSATIONS:
        print(f"{c['id']} ...")
        if c["id"] in cache:
            reply = cache[c["id"]]
        else:
            reply = call(a.model, key, c["msg"])
            cache[c["id"]] = reply
            json.dump(cache, open(cache_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
            time.sleep(a.delay)
        print("  " + reply.replace("\n", " ")[:160])
        rows.append((c["id"], a.model, reply))
    out = os.path.join(here, "task4_replies.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["Eval ID", "Model", "Reply"]); w.writerows(rows)
    print(f"Saved {out}")
    try:
        import openpyxl
        xl = os.path.join(here, "Ivy eval scoring sheet (Task 3).xlsx")
        wb = openpyxl.load_workbook(xl)
        ws = wb["Task 4 new model"]
        for i, (_, _, reply) in enumerate(rows):
            ws.cell(5 + i, 5, reply)
        ws["H1"] = a.model
        wb.save(xl)
        print("Filled the Task 4 tab in the scoring sheet.")
    except ImportError:
        print("openpyxl not installed, so only the CSV was written (pip install openpyxl to fill the sheet).")
    except PermissionError:
        print("Could not write the xlsx (is it open in Excel?). The CSV is saved.")

if __name__ == "__main__":
    main()
