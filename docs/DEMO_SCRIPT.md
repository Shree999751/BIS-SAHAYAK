# Demo script — Round 1

Target: **4 minutes** of demo, then questions. Panels get bored. Show, don't
narrate the architecture unless asked.

## Before you walk in

- [ ] `python3 backend/app.py` already running, browser already open at
      localhost:8000, page already loaded
- [ ] Wifi off. Run it offline on purpose — then say you did.
- [ ] Screen brightness up, browser zoom at 125% so the panel can read it
- [ ] Second laptop with the same thing running, in case of a crash
- [ ] Repo zipped on a pen drive

## The run

**Opening line (15 seconds).** Say this, then stop talking and start typing:

> An MSME owner in Agra who wants to sell a product has to figure out which
> Indian Standard applies, whether certification is compulsory, which BIS
> scheme, and where to test. Today that means searching several BIS portals
> and PDFs. This does it in one question. I'm running it with the wifi off.

**1. Product to standard.** Click the chip:
`I manufacture helmets in Agra. What do I need?`

Point at the answer, then at the source slip. Say: every answer carries the
BIS source it came from, and you can click through to it.

**2. Scheme comparison.** Type:
`What is the difference between ISI mark and CRS?`

Say: it pulls both scheme entries, not just the closest one.

**3. Consumer side.** Type:
`How do I check if my gold jewellery is really hallmarked?`

This is the one the panel personally cares about. Let the next-steps list sit
on screen for a beat.

**4. Hindi.** Click हिंदी, then the chip:
`सोने के आभूषण का हॉलमार्क कैसे जाँचें?`

Say: language is detected from the script, so a user can just type. No
separate mode to select.

**5. The refusal.** This is the moment that wins the round. Type something
deliberately outside the loaded sources, for example:
`Which standard applies to aircraft landing gear?`

Say:

> It says it doesn't know instead of inventing an IS number. For a BIS tool
> that matters more than the answers do. A confident wrong standard number
> costs a manufacturer a rejected licence application.

**6. The amber slip.** Point at any unverified source slip. Say:

> Amber means a human on our team hasn't yet opened that source and confirmed
> it. We show that to the user rather than hide it. Green means verified.

**Close (10 seconds).**

> Retrieval decides what is true. The language model only decides how it's
> worded, and it's locked to the retrieved sources. That's why it can't
> hallucinate a standard number.

## If something breaks

| What breaks | What you do |
|---|---|
| Server won't start | Second laptop. Keep talking while you switch. |
| Page says "server not running" | Check the terminal, restart, keep talking. |
| Answer is wrong | Say so. "That's a retrieval ranking issue, here's the tuning." Do not pretend. |
| Panel asks for a standard we don't have | Show the refusal. That's the feature. |

## Questions you will get

**"Isn't this just ChatGPT with extra steps?"**
Open the laptop's wifi indicator. It's off. Nothing left this machine. The
facts come from a curated BIS source set, not model memory, and every answer
shows which source. Then type the refusal query again.

**"How many standards can it handle?"**
Twenty curated entries today. The schema is the ingestion target — the same
retrieval works over 20 or 20,000 entries, and `docs/ARCHITECTURE.md` has the
ingestion plan for the BIS catalogue and Quality Control Orders.

**"How accurate is it?"**
Every entry is traceable to a source URL and carries a verification flag. We
would rather show you that a source is unchecked than have you find out later.

**"What about other languages?"**
The answer text is stored per language in the entry, so adding a language is
adding a field, not retraining anything. Hindi is in. The next ones are the
languages BIS already publishes consumer material in.

**"What's next if you qualify?"**
Ingest the BIS standards catalogue and the Quality Control Orders, add
embedding-based retrieval alongside BM25, and add a lab finder keyed to the
recognised laboratory list.
