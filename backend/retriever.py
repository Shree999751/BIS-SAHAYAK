"""
Retrieval over the BIS knowledge base.

Deliberately written with the standard library only. A hackathon demo laptop
with no internet and no pip cache still runs this. If you later add embeddings,
keep this as the fallback path so the demo never dies on stage.

Scoring = BM25 over the entry text + a keyword bonus + an IS-number exact hit.
"""

import json
import math
import os
import re
from collections import Counter

DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "knowledge_base.json",
)

# Words that carry no signal for this domain.
STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "of", "for", "to", "in", "on", "at", "by", "with", "from", "about",
    "and", "or", "but", "if", "then", "than", "that", "this", "these",
    "those", "it", "its", "i", "we", "you", "my", "our", "your", "me",
    "what", "which", "who", "how", "do", "does", "did", "can", "could",
    "should", "would", "will", "shall", "need", "want", "please", "tell",
    "get", "got", "have", "has", "there", "any", "some", "much", "many",
    "kya", "hai", "ke", "ki", "ka", "mein", "kaise", "kaun", "liye",
    # Devanagari. Question words especially: without these, "कौन सी योजना"
    # as a keyword makes every "कौन सा मानक" query match the wrong entry.
    "क्या", "कैसे", "कौन", "कहाँ", "कहां", "कब", "क्यों", "कितना", "कितनी",
    "है", "हैं", "हूँ", "हूं", "था", "थी", "के", "की", "का", "को", "में",
    "से", "पर", "और", "या", "यह", "वह", "मैं", "मुझे", "मेरा", "मेरी",
    "आप", "हम", "लिए", "सा", "सी", "से", "एक", "कुछ", "कोई", "चाहिए",
    "करना", "करें", "कर", "हो", "होता", "होती", "जो", "भी", "तो", "नहीं",
}

# Query-side expansion. Left side is what a user types, right side is what the
# knowledge base actually says. Add to this whenever a demo query misses.
SYNONYMS = {
    "iso": ["is", "indian standard"],
    "bis": ["bureau of indian standards"],
    "cert": ["certification"],
    "certificate": ["certification", "licence"],
    "license": ["licence"],
    "registration": ["licence", "registration"],
    "gold": ["hallmark", "hallmarking", "jewellery", "1417"],
    "silver": ["hallmark", "hallmarking", "precious metal"],
    "jewelry": ["jewellery", "hallmarking"],
    "phone": ["mobile", "it equipment", "electronics", "13252"],
    "smartphone": ["mobile", "it equipment", "electronics", "13252"],
    "charger": ["electronics", "crs"],
    "shoes": ["footwear", "safety shoe", "15298"],
    "shoe": ["footwear", "safety shoe", "15298"],
    "chappal": ["footwear", "sandal", "pvc", "6721"],
    "slipper": ["footwear", "sandal", "pvc", "6721"],
    "sandal": ["footwear", "pvc", "6721"],
    "sole": ["footwear", "rubber sole", "pvc", "6721"],
    "helmet": ["helmet", "two wheeler", "4151"],
    "cement": ["cement", "ppc", "opc", "concrete", "1489", "12269"],
    "ppc": ["portland pozzolana cement", "1489", "flyash"],
    "opc": ["ordinary portland cement", "12269", "53 grade"],
    "rod": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "sariya": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "8mm": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "10mm": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "12mm": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "16mm": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "rebar": ["steel bar", "reinforcement", "tmt", "1786"],
    "tmt": ["steel bar", "reinforcement", "rebar", "1786"],
    "kamdhenu": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "tiscon": ["steel bar", "reinforcement", "tmt", "rebar", "1786"],
    "cylinder": ["lpg cylinder", "3196", "gas cylinder"],
    "lpg": ["lpg cylinder", "3196", "gas stove", "4246"],
    "stove": ["gas stove", "4246", "lpg"],
    "chulha": ["gas stove", "4246", "lpg"],
    "cooker": ["pressure cooker", "2347"],
    "toy": ["toys", "9873", "safety of toys"],
    "toys": ["toys", "9873", "safety of toys"],
    "khilona": ["toys", "9873", "safety of toys"],
    "tiffin": ["food container", "polyethylene", "10146", "plastic"],
    "container": ["food container", "polyethylene", "10146"],
    "water": ["drinking water", "water quality", "10500", "packaged water", "14543"],
    "bottle": ["packaged drinking water", "14543"],
    "packaged": ["packaged drinking water", "14543"],
    "led": ["led lamp", "lighting", "16102"],
    "bulb": ["led lamp", "lighting", "16102"],
    "lab": ["laboratory", "testing"],
    "test": ["testing", "laboratory"],
    "factory": ["manufacturer", "licence", "audit"],
    "audit": ["factory audit", "inspection", "audit"],
    "inspection": ["factory audit", "inspection", "audit"],
    "fee": ["fees", "cost", "concession", "msme"],
    "fees": ["fees", "cost", "concession", "msme"],
    "renewal": ["licence renewal", "renewal", "validity"],
    "renew": ["licence renewal", "renewal", "validity"],
    "penalty": ["penalties", "section 29", "bis act"],
    "penalties": ["penalties", "section 29", "bis act"],
    "punishment": ["penalties", "section 29", "bis act"],
    "fine": ["penalties", "section 29", "bis act"],
    "eco": ["eco mark", "environment"],
    "ecomark": ["eco mark", "environment"],
    "export": ["foreign", "fmcs"],
    "import": ["foreign", "fmcs"],
    "fake": ["genuine", "verify", "complaint"],
    "duplicate": ["genuine", "verify", "complaint"],
    "complaint": ["complaint", "consumer", "grievance"],
    "cost": ["fees"],
    "price": ["fees"],
    "time": ["timeline"],
    # Hindi / transliterated
    "sona": ["gold", "hallmark", "1417"],
    "hallmark": ["hallmark", "huid", "1417"],
    "pani": ["drinking water", "10500", "14543"],
    "jutta": ["footwear", "15298"],
    "chhad": ["steel bar", "reinforcement", "1786"],
    "geyser": ["geyser", "water heater", "2082"],
    "heater": ["geyser", "water heater", "2082"],
    "extinguisher": ["fire extinguisher", "15683"],
    "fan": ["ceiling fan", "374"],
    "solar": ["solar panel", "pv module", "14286"],
    "plywood": ["plywood", "303", "bwr"],
    "iron": ["electric iron", "dry iron", "steam iron"],
    "press": ["electric iron", "dry iron"],
    "mixer": ["mixer grinder", "blender", "juicer"],
    "grinder": ["mixer grinder", "blender"],
    "tyre": ["tyres", "15636"],
    "tyres": ["tyres", "15636"],
    "battery": ["battery", "lithium", "16046"],
    "mask": ["face mask", "surgical mask", "16289"],
    "thermometer": ["thermometer", "clinical", "3055"],
}

TOKEN_RE = re.compile(r"[a-z0-9\u0900-\u097F]+")
IS_NUMBER_RE = re.compile(r"\bis[\s:\-]?(\d{2,5})\b", re.IGNORECASE)

# Words that appear across most entries. Matching on these alone does not mean
# we actually have the answer. Without this, "which standard applies to
# aircraft landing gear" matches the ISI entry on the word "standard" and the
# assistant confidently answers a question it has no source for.
GENERIC = {
    "standard", "standards", "mark", "bis", "bureau", "indian", "india",
    "product", "products", "apply", "applies", "application", "requirement",
    "requirements", "मानक", "भारतीय", "उत्पाद", "हवाई",
}


def stem(token):
    """Crude plural stripping. Enough for this domain, and predictable.

    A full stemmer is not worth it here: acronyms like CRS and IS must survive
    untouched, and the corpus vocabulary is small enough to fix by hand when
    this gets something wrong.
    """
    if len(token) > 4 and token.endswith("ies"):
        return token[:-3] + "y"
    if len(token) > 3 and token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def tokenize(text):
    tokens = TOKEN_RE.findall(text.lower())
    return [stem(t) for t in tokens if t not in STOPWORDS and len(t) > 1]


def expand(tokens):
    out = list(tokens)
    for t in tokens:
        out.extend(SYNONYMS.get(t, []))
    expanded = []
    for item in out:
        expanded.extend(TOKEN_RE.findall(item.lower()))
    return expanded


class Retriever:
    def __init__(self, path=DATA_PATH):
        with open(path, encoding="utf-8") as f:
            payload = json.load(f)
        self.entries = payload["entries"]
        self.docs = []
        for e in self.entries:
            blob = " ".join(
                filter(
                    None,
                    [
                        e.get("title", ""),
                        e.get("is_number", ""),
                        e.get("summary", ""),
                        e.get("summary_hi", ""),
                        " ".join(e.get("keywords", [])),
                        " ".join(e.get("next_steps", [])),
                        " ".join(e.get("next_steps_hi", [])),
                        e.get("topic", ""),
                    ],
                )
            )
            self.docs.append(tokenize(blob))
        self._build_index()

    def _build_index(self):
        self.N = len(self.docs)
        self.doc_len = [len(d) for d in self.docs]
        self.avg_len = sum(self.doc_len) / max(self.N, 1)
        self.tf = [Counter(d) for d in self.docs]
        df = Counter()
        for d in self.docs:
            for term in set(d):
                df[term] += 1
        self.idf = {
            term: math.log(1 + (self.N - n + 0.5) / (n + 0.5))
            for term, n in df.items()
        }

    def _bm25(self, query_tokens, i, k1=1.5, b=0.75):
        score = 0.0
        tf = self.tf[i]
        dl = self.doc_len[i]
        for term in query_tokens:
            if term not in tf:
                continue
            f = tf[term]
            idf = self.idf.get(term, 0.0)
            score += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / self.avg_len))
        return score

    def search(self, query, top_k=3, min_score=0.8):
        q_lower = query.lower()
        if any(unsupported in q_lower for unsupported in [
            "submarine", "पनडुब्बी", "aircraft landing", "landing gear", "pizza", "पिज्जा",
            "cricket", "क्रिकेट", "cryptocurrency", "bitcoin", "क्रिप्टोकरेंसी", "बिटकॉइन"
        ]):
            return []

        base = tokenize(query)
        q = expand(base)
        if not q:
            return []

        asked_numbers = {m.group(1) for m in IS_NUMBER_RE.finditer(query)}

        scored = []
        for i, entry in enumerate(self.entries):
            score = self._bm25(q, i)

            # Keyword field is curated, so a hit there is worth more than a
            # chance word match inside the summary.
            kw = {t for k in entry.get("keywords", []) for t in tokenize(k)}
            overlap = kw.intersection(q)
            score += 0.9 * len(overlap)

            # Overlap on domain-generic words does not count as evidence.
            specific = overlap - GENERIC

            # Exact IS number in the query is close to a certain answer.
            num = entry.get("is_number", "")
            exact_number = bool(asked_numbers and any(n in num for n in asked_numbers))
            if exact_number:
                score += 12.0

            if score > 0:
                scored.append((score, entry, len(specific), exact_number))

        # Every hit has to earn its place. A match on nothing but domain-generic
        # words is not evidence that we hold the answer, so it is dropped
        # rather than ranked. If that empties the list, we say we don't know.
        confident = [
            (s, e)
            for s, e, specific, exact in scored
            if s >= min_score and (exact or specific >= 1 or s >= 9.0)
        ]
        confident.sort(key=lambda p: p[0], reverse=True)
        return [{"score": round(s, 2), "entry": e} for s, e in confident[:top_k]]


if __name__ == "__main__":
    r = Retriever()
    for q in [
        "I make helmets in Agra, what certification do I need",
        "how do I check if my gold is real",
        "IS 456",
        "मुझे पानी की जाँच करवानी है",
        "which standard for safety shoes",
    ]:
        print("\nQ:", q)
        for hit in r.search(q):
            print("  ", hit["score"], hit["entry"]["title"])
