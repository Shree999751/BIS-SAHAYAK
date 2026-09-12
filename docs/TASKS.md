# Work split — Round 1 (12 September)

Round 1 is judged on the working prototype only. No PPT. So the only thing
that matters tonight is: it runs, it answers, it cites, it doesn't crash.

Everyone: clone the repo and get `python3 backend/app.py` running on your own
laptop **first**, before you start your task. If it doesn't run on your
machine, say so in the group immediately.

---

## Harsh Pathak — team lead, demo driver

You run the laptop in front of the panel and you answer the questions.

- Own the master branch. Every merge goes through you.
- Rehearse `docs/DEMO_SCRIPT.md` out loud at least three times.
- Keep a **known-good commit tagged**. If someone breaks main at 11pm, you
  check out the tag and demo that.
- Prepare answers to the three questions a panel always asks:
  1. "How is this different from ChatGPT?" — retrieval decides facts, the
     model only phrases them; every claim carries a clickable BIS source; it
     refuses when the sources don't cover the question. Demo the refusal.
  2. "Where does the data come from?" — curated BIS entries with source URLs
     and a verification flag; show an amber unverified slip and explain why
     we chose to expose it rather than hide it.
  3. "How does this scale to thousands of standards?" — the entry schema is
     the ingestion target; show `docs/ARCHITECTURE.md` roadmap section.
- Carry the backup: repo zipped on a pen drive plus one on your phone.

## Hanswarup Talwar — knowledge base, certification and schemes

Biggest single lever on demo quality. Bad data = bad demo.

- Open `data/knowledge_base.json`. Take every entry with `topic` of
  `certification`, `process` or `testing`.
- For each: open the `source_url`, confirm the summary is actually right,
  correct it in your own words, then set `"verified": true`.
- Add at least **6 new entries**: fee structure, licence validity and renewal,
  what happens in a factory audit, Scheme-X if it applies, ECO mark,
  penalties under the BIS Act for using the mark without a licence.
- Do not copy paragraphs out of BIS PDFs. Summarise in two to four sentences
  and link.

## Araz Bhatia — standards coverage and product-to-standard matching

- Add at least **10 more `topic: "standard"` entries** across categories the
  panel might probe: electrical goods, cement, LPG cylinders and regulators,
  food containers, packaged drinking water, toys, steel.
- For each entry, write `keywords` the way a real user types, not the way the
  standard is titled. "sariya", "TMT bar", "8mm rod" all need to reach
  IS 1786.
- After each addition, test: `python3 backend/retriever.py` runs a set of
  sample queries and prints the ranking. Add your own queries to that list at
  the bottom of the file.
- Report to Harsh any query that returns the wrong entry first.

## Yukti Suman — hallmarking, consumer queries and the refusal path

- Verify and expand the `hallmarking` and `consumer` entries. Add: what a
  consumer can claim if purity is found short, how to file a complaint, what
  the BIS Care app does, what marks appear on silver.
- Own the **"I don't know" behaviour**. This is a scoring feature, not a bug.
  Find five questions that should be refused (out of scope, unrelated
  product, a standard we have not loaded) and confirm the assistant refuses
  cleanly in both languages.
- If the refusal threshold is too loose or too tight, tune `min_score` in
  `retriever.py` and tell Araz so his ranking tests stay valid.

## Mudit Vij — Hindi and retrieval tuning

- Every entry needs a `summary_hi`. Right now most do not. Fill them in.
- `next_steps` are still English even in Hindi mode. Add a `next_steps_hi`
  array to the entry schema and read it in `backend/answer.py`
  (`grounded_answer`, where `steps` is picked up).
- Known bug to fix: the query "मुझे पानी की जाँच करवानी है" ranks the
  hallmark-verification entry above the drinking water standard, because
  "जाँच" is a keyword on both. Fix by weighting multi-word keyword matches
  higher than single-word ones in `Retriever.search`.
- Grow the `SYNONYMS` map in `retriever.py` with the Hinglish a real MSME
  owner in Agra would type.

## Shreyansh Jain — footwear, leather, and demo QA

- You are the domain person for footwear. Add the footwear and leather
  standards properly: the IS 15298 parts, rubber and moulded soles, sports
  and school footwear, leather test methods. Verify each against BIS.
- Then switch to QA. Run **every chip on the home screen** in both languages
  on the actual demo laptop. Log anything that looks wrong, slow, or ugly.
- Check the frontend on a phone-width window. The panel may ask.
- Write down the exact five questions we will type live and confirm all five
  give a good answer on the demo machine. Hand that list to Harsh.

---

## Rules for tonight

1. Branch per person: `kb-hanswarup`, `kb-araz`, `hi-mudit`, and so on.
   Everyone edits the same JSON file, so **pull before you push** or you will
   spend an hour on merge conflicts.
2. Run `python3 tests/test_demo_queries.py` before every push. It catches a
   trailing comma in the JSON, a missing field, and any demo query you just
   broke. Do not push on a red result.
3. **Freeze at 11:00 pm.** After that, no new features. Only: run it, find
   crashes, fix crashes.
4. Nobody adds a new library. The demo runs on stdlib and that is the point.
