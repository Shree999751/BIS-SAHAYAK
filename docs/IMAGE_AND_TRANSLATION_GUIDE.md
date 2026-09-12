# BIS Sahayak: Technical Architecture & Implementation Guide
## Computer Vision Image Recognition, Indic Regional Translation, and Multi-Key Failover

This document provides a comprehensive technical breakdown of how **Image Recognition**, **Indic Regional Translation**, and the **Multi-Key Groq Failover & Offline Database System** operate within BIS Sahayak (Smart India Hackathon Problem Statement 26107).

---

## 1. System Architecture Overview

```
                         +-----------------------------------+
                         |       User Web Interface          |
                         |      (frontend/index.html)        |
                         +-----------------+-----------------+
                                           |
             +-----------------------------+-----------------------------+
             |                                                           |
             v                                                           v
  [ IMAGE UPLOAD & VISION ]                                   [ TEXT QUERY INPUT ]
  - FileReader Base64 Loading                                 - Freeform or Keyword Query
  - In-Browser Neural Vision (MobileNet)                      - Voice or Preset Chips
  - Pixel Classification & Scores                             - Product Description
  - BIS Taxonomy Mapping (IS 4151, IS 15683, etc.)                       |
  - Candidate Tags & Interactive Chips                                   |
             |                                                           |
             +-----------------------------+-----------------------------+
                                           |
                                           v
                       POST /api/ask (or POST /api/translate)
                                           |
                                           v
                         +-----------------------------------+
                         |      Backend Orchestrator         |
                         |      (backend/app.py & answer.py) |
                         +-----------------+-----------------+
                                           |
                   +-----------------------+-----------------------+
                   |                                               |
                   v                                               v
        [ MULTI-KEY GROQ POOL ]                         [ BM25 RETRIEVER ]
        - Key #1 (Primary)                             - Local Verified DB
        - Key #2 (Secondary Failover)                  - data/knowledge_base.json
        - Key #3 ... N (Backup Pool)                   - Standard Spec & Next Steps
        - Model Fallbacks (120B -> 70B)                            |
                   |                                               |
       (All Keys Failed or 429) ---------------------------------->+
                   |                                               |
                   +-----------------------+-----------------------+
                                           |
                                           v
                         +-----------------------------------+
                         |    Structured Standard Card       |
                         |  + Citations + Markdown Response  |
                         +-----------------+-----------------+
                                           |
                                           v
                         +-----------------------------------+
                         |    Indic Translation Engine       |
                         | (5 Languages: hi, ta, te, bn, mr) |
                         |   - Context Preservation Prompt   |
                         |   - Multi-Key Translation Pool    |
                         |   - Instant Client-Side Cache     |
                         +-----------------------------------+
```

---

## 2. How Image Recognition Works

The Image Recognition system enables users to upload or capture photos of physical products (such as motorcycle helmets, water bottles, fire extinguishers, electrical appliances, cables, gold jewellery, toys, and safety shoes) to automatically discover the applicable Indian Standard (IS), mandatory certification scheme, and compliance rules.

### A. Client-Side In-Browser Neural Vision
Rather than transferring high-bandwidth raw images to a heavy external server or third-party vision API, BIS Sahayak utilizes **client-side neural computer vision** via MobileNet and TensorFlow.js:
1. **Instant Pixel Ingestion**:
   When the user selects an image via `#file-input`, the file is converted to an in-memory DataURL via `FileReader`.
   ```javascript
   const pixelImg = new Image();
   pixelImg.src = dataUrl;
   ```
2. **On-Device Hardware Acceleration**:
   The image is fed into MobileNet running on the client machine using WebGL / WebGPU acceleration:
   ```javascript
   const predictions = await net.classify(pixelImg);
   ```
3. **Probability & Confidence Scoring**:
   MobileNet returns top classifications along with confidence percentages:
   ```javascript
   const top = predictions[0];
   const pct = Math.round(top.probability * 100);
   // Example: "Crash Helmet (94% Visual Match)"
   ```

### B. Domain Taxonomy Mapping (`VISUAL_MAPPINGS`)
Raw computer vision classifications (ImageNet categories) are mapped into the official Bureau of Indian Standards (BIS) domain catalog:

| Visual Classification Matches | Identified BIS Domain | Associated Indian Standard |
| :--- | :--- | :--- |
| `crash helmet`, `helmet`, `hard hat`, `visor` | Motorcycle Helmet | **IS 4151** (Mandatory ISI Mark) |
| `fire extinguisher`, `sprayer`, `cylinder` | Portable Fire Extinguisher | **IS 15683** (Mandatory ISI Mark) |
| `sandal`, `shoe`, `boot`, `running shoe`, `slipper` | Footwear / Safety Shoes & Casuals | **IS 15298 (Part 2)** (Industrial) / **IS 6721** |
| `water bottle`, `bottle`, `jug`, `flask` | Packaged Drinking Water | **IS 14543** & **IS 10500** |
| `necklace`, `chain`, `ring`, `bracelet`, `gold` | Gold Jewellery & Hallmarking | **IS 1417** & 6-digit HUID |
| `power cord`, `cord`, `wire`, `cable`, `conduit` | PVC Electric Cable & Wire | **IS 694** (Mandatory ISI Mark) |
| `electric iron`, `iron`, `smoothing iron` | Electric Clothes Iron | **IS 302 (Part 2)** |
| `blender`, `mixer`, `food processor`, `juicer` | Food Mixer & Grinder | **IS 302 (Part 2)** |
| `gas stove`, `stove`, `cooker`, `range` | Domestic LPG Gas Stove | **IS 4246** (Mandatory ISI Mark) |
| `teddy`, `doll`, `toy`, `plush`, `puppet` | Children Toys (Safety of Toys) | **IS 9873 (Part 1)** |
| `cellphone`, `cellular telephone`, `mobile phone` | Mobile Phone & IT Goods | **IS 13252 (Part 1)** (CRS Scheme) |
| `pressure cooker` | Domestic Pressure Cooker | **IS 2347** (Mandatory ISI Mark) |
| `cement`, `stone wall`, `brick` | Portland Cement & Concrete | **IS 1489** (PPC) / **IS 456** |

### C. Dynamic Query Synthesis & Inspection Execution
Once an item is identified:
1. The UI displays the detected category badge, thumbnail preview, and top 4 candidate confidence chips.
2. A formal inquiry is synthesized:
   ```
   "What Indian Standard and BIS certification applies to [Identified Item]?
    What is the IS number, definition, and for which things is it given to?"
   ```
3. The inquiry is sent to `POST /api/ask` along with `identified_item`, `visual_predictions`, and `image_data`.
4. The backend processes the query through both the verified knowledge base and Groq AI reasoning, outputting a structured **BIS Standard Card** with definition, scope, scheme, and status.

---

## 3. How Indic Regional Translation Works

BIS Sahayak provides on-the-fly, high-fidelity translation into **5 major Indian regional languages**:
- **Hindi (हिन्दी - `hi`)**
- **Tamil (தமிழ் - `ta`)**
- **Telugu (తెలుగు - `te`)**
- **Bengali (বাংলা - `bn`)**
- **Marathi (मराठी - `mr`)**
- *(Also supports Gujarati `gu` and Kannada `kn`)*

### A. Regulatory Context-Preservation Rules
Standard generic machine translation often corrupts critical legal specifications, altering standard numbers like "IS 1786" into untraceable translated words or mistranslating scheme names. 

BIS Sahayak enforces 4 strict preservation directives in its translation engine:
```python
system_prompt = (
    f"You are an expert official translator for the Government of India and the Bureau of Indian Standards (BIS).\n"
    f"Translate the following Indian Standards information into {lang_name} ({native_name}).\n"
    f"CRITICAL TRANSLATION RULES:\n"
    f"1. PRESERVE exact Indian Standard numbers (e.g. IS 1786, IS 456, IS 15298, IS 10500, IS 4151, IS 1417, IS 3196, IS 1489).\n"
    f"2. PRESERVE official scheme designations (Scheme-I, Scheme-II, Scheme-IV, Scheme-X, ISI Mark, CRS, CM/L, HUID, BIS Care, Manakonline).\n"
    f"3. PRESERVE all Markdown formatting: tables, bullet points, numbered lists, bolding, and headers.\n"
    f"4. If a [STANDARD_CARD] block is present, translate TITLE, DEFINITION, GIVEN_TO, and NOT_GIVEN_TO values into {lang_name}, while keeping the tag names and keys in English.\n"
    f"5. Maintain an authoritative, professional, and clear public advisory tone.\n"
    f"6. Output ONLY the translated content without preamble or extra conversational remarks."
)
```

### B. Standard Card Tag Integrity
When translating, the structured Standard Card block:
```
[STANDARD_CARD]
IS_NUMBER: IS 14543
TITLE: Packaged Drinking Water (Other Than Packaged Natural Mineral Water)
DEFINITION: Specifies requirements for water filled in sealed containers intended for human consumption.
GIVEN_TO: Packaged drinking water, 20-litre water jars, 1-litre sealed bottles
NOT_GIVEN_TO: Natural mineral water (covered separately by IS 13428)
SCHEME: Scheme-I (Compulsory ISI Mark)
STATUS: Mandatory under QCO
[END_STANDARD_CARD]
```
is translated such that values are converted to the regional language while keys and tags remain strictly parseable by `extract_standard_card()`.

### C. Zero-Lag Client-Side Memory Caching
To eliminate latency and prevent redundant API calls:
1. When a user clicks a language pill (e.g. தமிழ் or मराठी), the frontend checks `translationCache[targetLang]`.
2. If already translated in this session, the card and markdown body are swapped **instantly (0 ms delay)**.
3. If not yet cached, `POST /api/translate` is invoked. Once returned, it is saved into `translationCache[targetLang]` for the duration of the query view.

---

## 4. Multi-Key Groq Failover & Offline Database System

To ensure continuous uptime during high-traffic hackathon judging, network instability, or API rate limiting, BIS Sahayak uses a **3-tier hierarchical failover system**.

### A. Key Discovery & Pooling
The application discovers and pools keys from all standard configurations:
1. **Single or Comma-Separated**:
   ```env
   GROQ_API_KEY=gsk_key1,gsk_key2,gsk_key3
   ```
2. **Plural Variable**:
   ```env
   GROQ_API_KEYS=gsk_key1,gsk_key2
   ```
3. **Numbered Variables**:
   ```env
   GROQ_API_KEY_1=gsk_primary
   GROQ_API_KEY_2=gsk_backup
   GROQ_API_KEY_3=gsk_tertiary
   ```
4. **Client-Supplied Key**:
   Passed via the UI Settings modal or `X-Groq-Api-Key` HTTP header.

### B. Failover Execution Loop
```python
# Pool of candidate keys
for key_idx, key in enumerate(all_keys, 1):
    for model in candidate_models:
        try:
            # Attempt inference on Groq LPU
            resp = make_request(key, model)
            return resp, key_info
        except HTTPError as err:
            if err.code == 429:  # Rate Limit Exceeded
                sys.stderr.write(f"[Groq Key Failover] Key #{key_idx} rate limited (HTTP 429). Switching to next key...\n")
                break  # Advance to next key in pool
            elif err.code in (401, 403):  # Invalid or revoked key
                sys.stderr.write(f"[Groq Key Failover] Key #{key_idx} auth error (HTTP {err.code}). Switching to next key...\n")
                break  # Advance to next key in pool
```

### C. Automatic Offline Database Fallback
If **all** configured keys fail (or if no keys are provided):
1. The system does **NOT** throw an error or crash.
2. In `mode="auto"`, it automatically switches to the **BIS Verified Database (Local)**:
   - Queries the local `data/knowledge_base.json` (43+ verified entries).
   - Computes BM25 relevance scores over standard numbers, titles, and bilingual keywords.
   - Extracts exact Indian Standard numbers, scope, next steps, and official portal citations.
3. The response is flagged with:
   ```json
   {
     "dynamic": false,
     "fallback": true,
     "fallback_reason": "All configured Groq API keys failed or rate-limited. Switched to offline verified BIS database.",
     "engine": "BIS Verified Database (Offline Fallback)"
   }
   ```
4. The user receives a fully verified, official answer with zero downtime.

---

## 5. Verification Commands

To test and verify each component:

1. **Run full query benchmark (all 53 tests)**:
   ```powershell
   $env:PYTHONUTF8=1; python tests/test_demo_queries.py
   ```

2. **Verify Multi-Key Failover in terminal**:
   ```powershell
   python -c "from backend.answer import compose, get_all_groq_keys; from backend.retriever import Retriever; ret = Retriever(); test_keys = 'gsk_fake_key_1,' + get_all_groq_keys()[0]; res = compose('What standard applies to packaged water?', ret.search('water', top_k=2), api_key=test_keys); print('Engine:', res['engine']); print('Failover Active:', res['key_info']['failovers'] > 0)"
   ```

3. **Verify Pure Offline Fallback**:
   ```powershell
   python -c "import os; os.environ['GROQ_API_KEY']=''; from backend.answer import compose; from backend.retriever import Retriever; res = compose('What standard applies to helmets?', Retriever().search('helmet', top_k=2), api_key='gsk_fake'); print('Engine:', res['engine']); print('Fallback:', res['fallback'])"
   ```

4. **Verify Health Endpoint**:
   ```powershell
   Invoke-RestMethod -Uri "http://localhost:8000/api/health"
   ```
