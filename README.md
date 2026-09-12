# BIS Sahayak

A conversational assistant for Indian Standards and BIS services.

Smart India Hackathon — problem statement **26107**, Department of Consumer Affairs.
Team **SUTRADHAR**.

Ask a question in plain English or Hindi. The assistant finds the relevant BIS
material, answers from it, and shows the source behind every answer. When the
loaded sources do not cover the question, it says so rather than inventing an
IS number.

## Run it

No installs needed. Python 3.9 or newer.

```bash
git clone <this-repo>
cd bis-sahayak
python3 backend/app.py
```

Open http://localhost:8000

That's the whole setup. The retrieval engine uses the standard library only,
so it runs on a laptop with no internet and no pip cache.

### Dynamic Answering with Groq API & Local Dataset Fallback

By default, BIS Sahayak runs dynamically using **Groq's ultra-fast LPU API** (`llama-3.3-70b-versatile` or `llama-3.1-8b-instant`) to answer queries spanning thousands of Indian Standards in milliseconds, with an automatic, seamless fallback to the local verified BIS dataset whenever offline or without an API key.

1. **Via Environment Variable or `.env`**:
   ```bash
   # Copy example template
   cp .env.example .env
   # Set your Groq key in .env or shell (from https://console.groq.com/):
   export GROQ_API_KEY=gsk_...
   python3 backend/app.py
   ```

2. **Via Web UI**:
   You can also click **⚙️ Settings** in the top navigation bar at `http://localhost:8000` to enter or update your Groq API key directly from the browser (persisted safely in localStorage).

3. **Fallback System**:
   - If Groq is available, queries are answered dynamically with comprehensive BIS domain knowledge, scheme details (ISI, CRS, Hallmarking), and auto-linked IS standard citations.
   - If `GROQ_API_KEY` is missing, network is down, or an error occurs, it instantly falls back to the local BM25 verified dataset (`data/knowledge_base.json`).


## How it works

```
question
   |
   v
language detect (Devanagari -> hi)
   |
   v
tokenise + domain synonym expansion       backend/retriever.py
   |                                      ("sariya" -> steel bar,
   v                                       "sona"   -> hallmark)
BM25 over knowledge base
 + curated-keyword bonus
 + exact IS-number boost
   |
   v
top 3 entries above threshold
   |
   +--> nothing above threshold -> "not in my sources" reply
   |
   v
compose answer                            backend/answer.py
 grounded  = stored summary + next steps
 assisted  = LLM phrasing, context-locked
   |
   v
answer + source slips                     frontend/index.html
```

Retrieval decides what is true. Generation only decides how it is worded.
That separation is why a wrong phrasing can never produce a wrong source link.

## API

| Method | Path | Body / returns |
|---|---|---|
| GET | `/api/health` | `{status, entries}` |
| GET | `/api/topics` | entry counts by topic, unverified count |
| POST | `/api/ask` | `{question, lang?, mode?}` → `{answer, citations[], mode, lang}` |

## Knowledge base

`data/knowledge_base.json` holds the BIS material the assistant can answer
from. Each entry carries a `source_url` and a `verified` flag.

**`verified` is false until a human has opened the source URL and confirmed the
text.** Unverified entries show an amber slip in the UI. This is deliberate:
a BIS assistant that quietly presents unchecked material is worse than useless.

Adding an entry:

```json
{
  "id": "IS-9873",
  "topic": "standard",
  "is_number": "IS 9873",
  "title": "IS 9873 - ...",
  "summary": "Two to four sentences, your own words.",
  "summary_hi": "वही बात हिंदी में।",
  "keywords": ["words a real user would type", "including Hindi"],
  "next_steps": ["Actionable step", "Another step"],
  "source_title": "BIS Standards Catalogue",
  "source_url": "https://...",
  "verified": true
}
```

Restart the server after editing. No rebuild step.

## Repo layout

```
backend/retriever.py   BM25 + synonym expansion, stdlib only
backend/answer.py      answer composition, citation building, LLM path
backend/app.py         HTTP server (stdlib) + optional FastAPI app
data/knowledge_base.json
frontend/index.html    single file, no CDN, works offline
docs/TASKS.md          who is doing what
docs/DEMO_SCRIPT.md    what we say and click on demo day
docs/ARCHITECTURE.md   design decisions and what comes next
tests/test_demo_queries.py
```

## Before every push

```bash
python3 tests/test_demo_queries.py
```

Checks that the knowledge base still parses, that every entry has its required
fields, and that each demo query answers or refuses the way it should. Add a
case whenever you add entries.

## Scope right now

Working: plain-language questions, English and Hindi, standard lookup by IS
number, product-to-standard suggestion, scheme guidance (ISI, CRS, FMCS),
hallmarking and HUID, consumer verification and complaints, laboratory
guidance, citations on every answer, graceful "I don't know".

Not yet: full-text ingestion of BIS PDFs, embedding-based retrieval, languages
beyond English and Hindi, live lookup against the BIS licence database,
conversation memory across turns.
