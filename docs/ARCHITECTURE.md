# Architecture

## The one decision that matters

Retrieval decides what is true. Generation decides how it is worded.

A general chatbot asked "which IS covers safety footwear" will produce a
number. Sometimes the right one. A manufacturer who files a licence
application against a wrong number loses months. So the system is built so
that the model is structurally unable to supply a standard number:

- Facts live in `data/knowledge_base.json`, each with a source URL.
- Retrieval picks entries. If nothing scores above threshold, the answer is
  "not in my sources" and no model is called at all.
- Citations are built from the retrieved entries, never from model output.
- When the LLM path is on, the prompt carries only the retrieved entries and
  forbids stating any IS number outside them.

Worst case with the model on: awkward phrasing. Never a wrong source link.

## Why BM25 and not embeddings, for now

An embedding model means a download, a pip install, a few hundred MB and a
warm-up. On a hackathon laptop that is three ways to fail on stage. BM25 over
a curated keyword field, plus a domain synonym map, handles this corpus well
because the vocabulary is narrow and the user's word ("sariya", "TMT rod") can
be mapped to the standard's word explicitly.

At catalogue scale this stops being enough. The plan is hybrid: BM25 for exact
IS-number and code matching, dense retrieval for descriptive product queries,
reciprocal rank fusion over both. BM25 stays as the offline fallback.

## Components

| File | Does |
|---|---|
| `backend/retriever.py` | tokenise, expand synonyms, BM25 score, keyword bonus, IS-number boost |
| `backend/answer.py` | compose grounded or assisted answer, build citations |
| `backend/app.py` | HTTP layer, language detection, stdlib server + optional FastAPI |
| `data/knowledge_base.json` | the source of truth |
| `frontend/index.html` | ask box, chips, answer, source slips, language toggle |

No database, no vector store, no build step. Everything loads at start.

## Language

Script detection, not a language classifier: Devanagari in the query means the
Hindi fields are used. The user does not pick a mode. Translations are stored
per entry rather than machine-translated at request time, because a wrong
translation of a certification requirement is a real cost and the entry count
is small enough to translate once, properly.

## Source verification

Every entry has `verified: true|false`. False means no human on the team has
opened the source URL and confirmed the summary. The UI shows unverified
sources in amber.

Showing this rather than hiding it is a product decision. The failure mode for
a government-facing tool is a confident answer nobody checked. Making that
state visible means a user can weigh it, and means the team can see at a glance
how much of the corpus is still unchecked (`GET /api/topics` returns the count).

## Roadmap

**Ingestion.** The entry schema is the target format. Three sources: the BIS
standards catalogue for titles, numbers and scope; Quality Control Orders for
what is compulsory and from when; the recognised-laboratory list for the lab
finder. Extraction produces draft entries with `verified: false`; a reviewer
promotes them.

**Retrieval.** Hybrid dense plus BM25 with rank fusion. Clause-level chunks for
standards where a user asks about a specific requirement rather than the scope.

**Product to standard.** Today this is keyword overlap. Next is a structured
product profile — category, material, intended use, voltage or size class —
matched against standard scope fields, so an answer can say why a standard
applies rather than only that it does.

**Lab finder.** Keyed to the recognised laboratory list, filtered by the IS the
user's product needs and by state, so the answer is a shortlist rather than a
link to a list.

**Conversation.** Multi-turn memory so a user can say "and what does that cost"
without repeating the product. Deliberately not in the Round 1 build; a
stateless demo is a demo that cannot get confused on stage.

**Languages.** Adding one is adding fields to entries, not retraining. Order
should follow whatever BIS already publishes consumer material in.
