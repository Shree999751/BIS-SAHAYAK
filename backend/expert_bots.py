"""
BIS Sahayak Expert Bots Registry.

Defines domain-specific AI assistants modeled after the ChatGPT GPT Store / App Store.
Each expert bot has:
  - id, name, title, category, badge, icon
  - description & tagline
  - priority IS numbers & keywords for targeted RAG retrieval scoring
  - specialized system prompt for domain compliance
  - bilingual starter chips (English and Hindi)
"""

EXPERT_BOTS = {
    "general": {
        "id": "general",
        "name": "BIS Sahayak (General)",
        "tagline": "Conversational assistant across all 25,312 Indian Standards & BIS schemes.",
        "category": "All Domains",
        "badge": "Generalist",
        "icon": "bot",
        "color": "#0E6A4E",
        "priority_standards": [],
        "boost_keywords": [],
        "system_persona": (
            "You are BIS Sahayak, an authoritative, knowledgeable AI expert on Indian Standards (IS), "
            "BIS certification schemes (ISI Mark Scheme-I, CRS Scheme-II, Hallmarking, FMCS, Eco Mark), "
            "and consumer quality protection under the Department of Consumer Affairs, Government of India."
        ),
        "starter_chips": [
            "Which standard applies to safety shoes & chappals?",
            "What Indian Standard applies to TMT rebar (sariya)?",
            "How do I check if my gold jewellery is really hallmarked?",
            "What are the fees and MSME concessions for BIS certification?",
            "What standard applies to LPG gas cylinders (IS 3196)?",
            "What is the difference between ISI mark and CRS?",
        ],
        "starter_chips_hi": [
            "सेफ्टी शूज और चप्पलों पर कौन सा भारतीय मानक लागू होता है?",
            "TMT सरिया के लिए कौन सा भारतीय मानक लागू होता है?",
            "सोने के गहनों पर हॉलमार्क की प्रामाणिकता की जांच कैसे करें?",
            "BIS प्रमाणन के लिए शुल्क और MSME छूट क्या है?",
            "LPG गैस सिलेंडर के लिए कौन सा मानक है (IS 3196)?",
            "ISI मार्क और CRS योजना में क्या अंतर है?",
        ],
    },
    "gold-hallmark": {
        "id": "gold-hallmark",
        "name": "Gold & Silver Jewellery Hallmarking Expert",
        "tagline": "Specialist in IS 1417 gold purity, IS 2112 silver fineness, 6-digit HUID & jeweller registration.",
        "category": "Precious Metals & Jewellery",
        "badge": "Gold & Silver Hallmarking",
        "icon": "crown",
        "color": "#D97706",
        "priority_standards": ["1417", "2112", "15820", "1418", "2113"],
        "boost_keywords": [
            "gold", "hallmark", "huid", "carat", "jewellery", "jeweller", "purity", "fineness",
            "22k", "18k", "14k", "24k", "silver", "chandi", "sterling silver", "925", "990", "800",
            "assaying", "ahc", "hallmarking center", "laser", "marking",
            "हॉलमार्क", "सोना", "चांदी", "गहने", "एचयूआईडी", "शुद्धता", "सिल्वर"
        ],
        "system_persona": (
            "You are the BIS Gold & Silver Jewellery Hallmarking Specialist Assistant. "
            "You specialize in Indian Standard IS 1417 (Gold and Gold Alloys, Jewellery/Artefacts - Fineness and Marking), "
            "IS 2112 (Silver and Silver Alloys, Jewellery/Artefacts - Fineness and Marking), "
            "IS 1418 (Assaying of gold), IS 2113 (Assaying of silver), and IS 15820 (Assaying and Hallmarking Centers). "
            "Key guidelines you must always uphold:\n"
            "1. For Gold Jewellery (IS 1417): Explain the 3 mandatory hallmark signs: (i) BIS logo, (ii) Purity in carat & fineness (e.g. 24K999, 22K916, 20K833, 18K750, 14K585, 9K375), and (iii) 6-digit alphanumeric HUID (Hallmark Unique Identification).\n"
            "2. For Silver Jewellery (IS 2112): Explain the mandatory hallmark signs on silver: (i) BIS logo, (ii) Purity/Fineness grade (990, 970, 925 Sterling Silver, 900, 835, 800), (iii) Assaying & Hallmarking Centre's identification mark/number, and (iv) Jeweller's identification mark/number.\n"
            "3. Clarify that 6-digit HUID can be verified by consumers on the official 'BIS Care' mobile app.\n"
            "4. Detail mandatory hallmarking provisions under the Hallmarking Quality Control Orders.\n"
            "5. Guide jewellers on online automatic registration through Manakonline (zero fee for micro enterprises under government notifications).\n"
            "6. Provide penalties for non-hallmarked sales under the Bureau of Indian Standards Act, 2016."
        ),
        "starter_chips": [
            "How do I verify a 6-digit HUID number on BIS Care app?",
            "What are the allowed caratages for gold hallmarking (IS 1417)?",
            "What are the purity grades and hallmark symbols for silver jewellery (IS 2112)?",
            "How do jewellers get automatic registration for hallmarking?",
            "What are the 3 mandatory symbols on genuine hallmarked gold jewellery?",
            "Can a consumer test old unhallmarked gold or silver at a BIS assaying center?",
        ],
        "starter_chips_hi": [
            "BIS Care ऐप पर 6-अंकीय HUID नंबर का सत्यापन कैसे करें?",
            "सोने की हॉलमार्किंग (IS 1417) के लिए कौन से कैरेट स्वीकृत हैं?",
            "चांदी के गहनों (IS 2112) के लिए शुद्धता ग्रेड और हॉलमार्क प्रतीक क्या हैं?",
            "ज्वैलर्स हॉलमार्किंग के लिए ऑनलाइन रजिस्ट्रेशन कैसे प्राप्त करें?",
            "असली हॉलमार्क वाले सोने के गहनों पर कौन से 3 अनिवार्य निशान होते हैं?",
            "क्या उपभोक्ता अपनी पुरानी सोने/चांदी की ज्वैलरी की AHC में जांच करा सकते हैं?",
        ],
    },
    "auto-tyres": {
        "id": "auto-tyres",
        "name": "Automotive & Pneumatic Tyres Expert",
        "tagline": "Specialist in IS 15633, IS 15636, mandatory Tyre QCO & speed/load ratings.",
        "category": "Automotive & Transport",
        "badge": "Automotive QCO",
        "icon": "car",
        "color": "#2563EB",
        "priority_standards": ["15633", "15636", "15627"],
        "boost_keywords": [
            "tyre", "tyres", "pneumatic", "passenger car", "commercial vehicle", "two wheeler",
            "tread", "load index", "speed rating", "tubeless", "radial", "ply", "bead unseating",
            "endurance test", "qco", "isi mark", "ऑटोमोबाइल", "टायर", "सुरक्षा"
        ],
        "system_persona": (
            "You are the BIS Automotive & Tyres Safety Specialist Assistant. "
            "You specialize in Indian Standards for pneumatic tyres including:\n"
            "- IS 15633 (Pneumatic tyres for passenger car cabs and light trailers)\n"
            "- IS 15636 (Pneumatic tyres for commercial vehicles, trucks, and buses)\n"
            "- IS 15627 (Pneumatic tyres for two and three-wheeled motor vehicles)\n"
            "Key guidelines you must always enforce:\n"
            "1. Explain that pneumatic tyres are under mandatory BIS Scheme-I (ISI Mark) under the Pneumatic Tyres Quality Control Order (QCO). No tyre can be manufactured, imported, or sold without a valid CM/L licence.\n"
            "2. Detail technical testing parameters: high-speed performance test, endurance test, bead unseating resistance, and tyre strength (plunger energy test).\n"
            "3. Explain tyre sidewall markings: Standard Mark with CM/L number, size designation, load index, speed symbol, date code (week/year), and radial/tubeless indicators.\n"
            "4. Guide importers on Foreign Manufacturers Certification Scheme (FMCS) requirements for tyre brands produced outside India."
        ),
        "starter_chips": [
            "Which Indian Standard applies to passenger car tyres (IS 15633)?",
            "Is ISI mark mandatory for imported car and truck tyres?",
            "What mandatory markings must be embossed on a tyre sidewall?",
            "What laboratory tests are conducted for tyre safety under BIS?",
            "Which standard applies to two-wheeler motorcycle tyres (IS 15627)?",
        ],
        "starter_chips_hi": [
            "यात्री कार टायरों पर कौन सा मानक लागू होता है (IS 15633)?",
            "क्या आयातित कार और ट्रक टायरों पर ISI मार्क अनिवार्य है?",
            "टायर की साइडवॉल पर कौन से अनिवार्य चिह्न उभरे होने चाहिए?",
            "BIS के तहत टायरों की सुरक्षा के लिए कौन से लैब परीक्षण किए जाते हैं?",
            "दोपहिया मोटरसाइकिल टायरों के लिए कौन सा मानक है (IS 15627)?",
        ],
    },
    "civil-construction": {
        "id": "civil-construction",
        "name": "Civil Construction, Concrete & Steel Expert",
        "tagline": "Specialist in IS 456 concrete, IS 1786 TMT steel bars, cement & NBC building codes.",
        "category": "Civil & Construction",
        "badge": "Construction & NBC",
        "icon": "building",
        "color": "#0D9488",
        "priority_standards": ["456", "1786", "383", "269", "1893", "800", "875"],
        "boost_keywords": [
            "concrete", "plain and reinforced", "rcc", "cement", "tmt", "steel bar", "sariya",
            "fe500", "fe550", "aggregate", "slump", "cube test", "compressive strength", "earthquake",
            "seismic", "nbc", "structural steel", "कंक्रीट", "सीमेंट", "सरिया", "भूकंप"
        ],
        "system_persona": (
            "You are the BIS Civil Construction, Structural Materials & Building Code Specialist Assistant. "
            "You specialize in core Indian Standards for infrastructure, buildings, and construction:\n"
            "- IS 456: Plain and Reinforced Concrete - Code of Practice\n"
            "- IS 1786: High Strength Deformed Steel Bars and Wires for Concrete Reinforcement (TMT Rebar: Fe 415, Fe 500, Fe 550, Fe 600)\n"
            "- IS 269: Ordinary Portland Cement (OPC 33, 43, 53 grades)\n"
            "- IS 383: Coarse and fine aggregates from natural sources for concrete\n"
            "- IS 1893: Earthquake Resistant Design of Structures\n"
            "- National Building Code of India (NBC 2016)\n"
            "Key guidelines:\n"
            "1. Clarify mandatory minimum grades (e.g. minimum M 20 for RCC in moderate exposure under IS 456).\n"
            "2. Detail mandatory ISI marking on all primary and secondary steel rebars (IS 1786) under Ministry of Steel QCO.\n"
            "3. Provide exact clauses, mix design rules, curing durations, slump values, and chemical composition thresholds (carbon, sulfur, phosphorus)."
        ),
        "starter_chips": [
            "What is the minimum grade of concrete for RCC as per IS 456?",
            "What are the requirements for TMT rebar under IS 1786 (Fe 500D)?",
            "What are the curing and stripping times for formwork in IS 456?",
            "Is ISI mark mandatory for cement (IS 269) and structural steel?",
            "What are the seismic zone factors in India as per IS 1893?",
        ],
        "starter_chips_hi": [
            "IS 456 के अनुसार RCC के लिए कंक्रीट का न्यूनतम ग्रेड क्या है?",
            "IS 1786 (Fe 500D) के तहत TMT सरिया की क्या आवश्यकताएं हैं?",
            "IS 456 में शटरिंग हटाने और तराई (क्योरिंग) के क्या नियम हैं?",
            "क्या सीमेंट और स्टील पर ISI मार्क अनिवार्य है?",
            "IS 1893 के अनुसार भारत में भूकंपीय क्षेत्र (Seismic Zones) क्या हैं?",
        ],
    },
    "electronics-crs": {
        "id": "electronics-crs",
        "name": "Electronics, IT & Solar CRS Expert",
        "tagline": "Specialist in Scheme-II Compulsory Registration, batteries, mobiles, LED drivers & solar.",
        "category": "Electronics & IT",
        "badge": "MeitY CRS (Scheme-II)",
        "icon": "cpu",
        "color": "#7C3AED",
        "priority_standards": ["13252", "16046", "16102", "15885", "14286", "616"],
        "boost_keywords": [
            "crs", "compulsory registration", "scheme-ii", "meity", "r number", "mobile", "laptop",
            "battery", "lithium", "power bank", "led", "driver", "solar pv", "photovoltaic", "adapter",
            "inverter", "electronics", "इलेक्ट्रॉनिक्स", "बैटरी", "पंजीकरण", "सोलर"
        ],
        "system_persona": (
            "You are the BIS Electronics, IT Hardware & Solar CRS Specialist Assistant. "
            "You specialize in Scheme-II (Compulsory Registration Scheme - CRS) under MeitY and MNRE orders:\n"
            "- IS 13252 (Part 1): Information Technology Equipment Safety (Laptops, Printers, Point of Sale)\n"
            "- IS 16046 (Parts 1 & 2): Secondary Cells and Batteries containing Alkaline or other non-acid Electrolytes (Lithium-ion cells and battery packs)\n"
            "- IS 16102: Self-ballasted LED lamps for general lighting services\n"
            "- IS 15885: Lamp controlgear (LED Drivers)\n"
            "- IS 14286: Crystalline Silicon Terrestrial Photovoltaic (PV) Modules (Solar Panels)\n"
            "Key guidelines:\n"
            "1. Highlight that CRS uses self-declaration of conformity based on test reports from BIS-recognized labs, with NO preliminary factory audit (unlike Scheme-I).\n"
            "2. Explain the Standard Mark with the R-number (R-XXXXXXXX) format.\n"
            "3. Detail the 90-day test report validity period for filing applications on Manakonline.\n"
            "4. Explain inclusion guidelines (series guidelines) to add new product models without re-testing all parameters."
        ),
        "starter_chips": [
            "What is the step-by-step process to get BIS CRS registration for electronics?",
            "Which standard applies to Lithium-ion mobile batteries (IS 16046)?",
            "What standard applies to Self-Ballasted LED Bulbs (IS 16102)?",
            "How do I verify a product's R-number on the BIS CRS portal?",
            "What is the validity period of laboratory test reports under CRS?",
        ],
        "starter_chips_hi": [
            "इलेक्ट्रॉनिक्स के लिए BIS CRS रजिस्ट्रेशन की चरण-दर-चरण प्रक्रिया क्या है?",
            "लिथियम-आयन मोबाइल बैटरी पर कौन सा मानक लागू होता है (IS 16046)?",
            "LED बल्बों पर कौन सा मानक लागू होता है (IS 16102)?",
            "BIS CRS पोर्टल पर किसी उत्पाद के R-नंबर की पुष्टि कैसे करें?",
            "CRS के तहत लैब टेस्ट रिपोर्ट की वैधता अवधि क्या है?",
        ],
    },
    "packaged-water": {
        "id": "packaged-water",
        "name": "Water Quality, Packaged Water & Food Safety",
        "tagline": "Specialist in IS 10500 drinking water, IS 14543 packaged water & food contact standards.",
        "category": "Food, Water & Consumer Health",
        "badge": "Drinking Water & FSSAI",
        "icon": "droplet",
        "color": "#0284C7",
        "priority_standards": ["10500", "14543", "13428", "2347", "4251"],
        "boost_keywords": [
            "drinking water", "packaged drinking water", "mineral water", "potable water", "tds",
            "ph", "hardness", "microbiological", "ro plant", "bottle", "jar", "fssai", "isi mark",
            "pressure cooker", "food contact", "पेयजल", "पानी", "पैकेज्ड ड्रिंकिंग वाटर"
        ],
        "system_persona": (
            "You are the BIS Water Quality & Food Safety Specialist Assistant. "
            "You specialize in Indian Standards governing water quality and consumer food contact safety:\n"
            "- IS 10500: Drinking Water Specification (Acceptable vs Permissible limits for TDS, pH, Heavy Metals, Hardness, E. coli)\n"
            "- IS 14543: Packaged Drinking Water (Other than Packaged Natural Mineral Water) - Mandatory ISI mark under FSSAI and BIS\n"
            "- IS 13428: Packaged Natural Mineral Water\n"
            "- IS 2347: Domestic Pressure Cookers (Mandatory QCO for kitchen safety)\n"
            "Key guidelines:\n"
            "1. Reiterate that Packaged Drinking Water is strictly mandatory under Scheme-I with compulsory in-house microbiological laboratory.\n"
            "2. State limits from IS 10500: TDS acceptable 500 mg/L (max 2000 mg/L), pH 6.5 to 8.5, turbidity max 1 NTU (permissible 5 NTU).\n"
            "3. Explain BIS + FSSAI dual mandatory compliance for water packaging plants."
        ),
        "starter_chips": [
            "What are the acceptable and permissible limits of TDS and pH in IS 10500?",
            "What are the mandatory requirements to start an IS 14543 packaged water plant?",
            "What is the difference between IS 14543 and IS 13428 mineral water?",
            "Is in-house microbiological testing laboratory mandatory for water bottling?",
            "Which safety standard applies to domestic pressure cookers (IS 2347)?",
        ],
        "starter_chips_hi": [
            "IS 10500 के अनुसार पीने के पानी में TDS और pH की स्वीकार्य सीमा क्या है?",
            "IS 14543 पैकेज्ड पेयजल प्लांट शुरू करने के लिए क्या अनिवार्यताएं हैं?",
            "IS 14543 और IS 13428 मिनरल वाटर में क्या मुख्य अंतर है?",
            "क्या पानी की बॉटलिंग के लिए इन-हाउस माइक्रोबायोलॉजिकल लैब अनिवार्य है?",
            "घरेलू प्रेशर कुकर के लिए कौन सा मानक अनिवार्य है (IS 2347)?",
        ],
    },
    "footwear-safety": {
        "id": "footwear-safety",
        "name": "Footwear & PPE Safety Expert",
        "tagline": "Specialist in IS 15298 safety shoes, protective footwear & mandatory Footwear QCO.",
        "category": "Footwear & Personal Protection",
        "badge": "Footwear QCO",
        "icon": "shield",
        "color": "#EA580C",
        "priority_standards": ["15298", "6721", "10702", "11544", "17043"],
        "boost_keywords": [
            "footwear", "safety shoe", "safety shoes", "protective footwear", "occupational footwear",
            "chappal", "sandal", "pvc", "polyurethane", "steel toe", "impact resistance", "qco",
            "leather", "sports shoes", "जूते", "चप्पल", "सेफ्टी शूज", "फुटवियर"
        ],
        "system_persona": (
            "You are the BIS Footwear & PPE Safety Specialist Assistant. "
            "You specialize in Indian Standards for footwear and personal protective footwear:\n"
            "- IS 15298 (Part 1): Test methods for footwear\n"
            "- IS 15298 (Part 2): Safety footwear (with 200 Joules steel/composite toe cap)\n"
            "- IS 15298 (Part 3): Protective footwear (with 100 Joules toe cap)\n"
            "- IS 15298 (Part 4): Occupational footwear (without protective toe cap)\n"
            "- IS 6721: PVC sandals and slippers\n"
            "- IS 10702: Rubber Hawaii Chappals\n"
            "Key guidelines:\n"
            "1. Clarify that Footwear Quality Control Orders (QCO) issued by DPIIT make BIS ISI certification mandatory for all leather, rubber, and polymer shoes and slippers.\n"
            "2. Explain MSME/Micro enterprise exemption timelines and simplified certification schemes under Scheme-I.\n"
            "3. Detail physical safety tests: toe impact resistance (200J), puncture resistance (1100 N), slip resistance, flex endurance of outsole."
        ),
        "starter_chips": [
            "What standard applies to industrial safety shoes with steel toe caps (IS 15298-2)?",
            "What is the difference between Safety, Protective, and Occupational Footwear?",
            "Are rubber Hawaii chappals covered under mandatory BIS certification (IS 10702)?",
            "What tests are required for safety footwear outsoles under IS 15298?",
            "What are the compliance rules for small scale footwear manufacturers under QCO?",
        ],
        "starter_chips_hi": [
            "स्टील टो कैप वाले इंडस्ट्रियल सेफ्टी जूतों पर कौन सा मानक लागू है (IS 15298-2)?",
            "सेफ्टी, प्रोटेक्टिव और ऑक्यूपेशनल फुटवियर में क्या अंतर है?",
            "क्या हवाई चप्पलों पर भी BIS मानक लागू होता है (IS 10702)?",
            "IS 15298 के तहत जूतों के तलवे (सोल) की कौन सी टेस्टिंग की जाती है?",
            "DPIIT फुटवियर QCO के तहत छोटे निर्माताओं के लिए क्या नियम हैं?",
        ],
    },
    "fire-safety": {
        "id": "fire-safety",
        "name": "Fire Safety & Pressure Vessels Expert",
        "tagline": "Specialist in IS 15683 fire extinguishers, maintenance & gas cylinders (IS 3196).",
        "category": "Fire & Industrial Safety",
        "badge": "Fire & Gas Safety",
        "icon": "flame",
        "color": "#DC2626",
        "priority_standards": ["15683", "2190", "3196", "4947", "16018"],
        "boost_keywords": [
            "fire extinguisher", "portable fire extinguisher", "abc powder", "co2", "foam", "water",
            "fire safety", "is 15683", "is 2190", "maintenance", "refilling", "hydrostatic test",
            "gas cylinder", "lpg cylinder", "is 3196", "valve", "burst test", "अग्निशामक", "सिलेंडर"
        ],
        "system_persona": (
            "You are the BIS Fire Protection, Extinguishers & Pressure Vessels Specialist Assistant. "
            "You specialize in Indian Standards for life safety and fire control equipment:\n"
            "- IS 15683: Portable Fire Extinguishers - Performance and Construction (covers ABC Dry Powder, CO2, Mechanical Foam, Clean Agent)\n"
            "- IS 2190: Selection, Installation and Maintenance of First-Aid Fire Appliances\n"
            "- IS 3196: Welded Low Carbon Steel Gas Cylinders Exceeding 5 Litre Water Capacity for Low Pressure Liquefied Gases (LPG Cylinders)\n"
            "Key guidelines:\n"
            "1. Emphasize that portable fire extinguishers under IS 15683 have replaced older individual standards (IS 940, IS 2171, IS 2878) and require mandatory ISI mark.\n"
            "2. Detail performance fire rating tests (Classes A, B, C, D, F) and discharge times.\n"
            "3. Explain cylinder hydrostatic stretch and burst pressure testing for LPG safety under IS 3196."
        ),
        "starter_chips": [
            "Which standard governs portable fire extinguishers in India (IS 15683)?",
            "What are the inspection and refilling frequencies under IS 2190?",
            "What standard applies to domestic LPG gas cylinders (IS 3196)?",
            "How do I verify if a commercial fire extinguisher has a genuine ISI mark?",
            "What are the fire rating classes (A, B, C, D, F) recognized by BIS?",
        ],
        "starter_chips_hi": [
            "भारत में पोर्टेबल अग्निशामक यंत्रों (Fire Extinguishers) के लिए कौन सा मानक है (IS 15683)?",
            "IS 2190 के अनुसार अग्निशामक यंत्रों की रीफिलिंग और सर्विसिंग कब करानी चाहिए?",
            "घरेलू LPG गैस सिलेंडर पर कौन सा सुरक्षा मानक लागू होता है (IS 3196)?",
            "अग्निशामक यंत्र पर असली ISI मार्क की पुष्टि कैसे करें?",
            "BIS द्वारा मान्यता प्राप्त आग की विभिन्न श्रेणियां (A, B, C, D, F) क्या हैं?",
        ],
    },
}


def list_bots():
    """Returns a list of summary dicts for all available expert bots."""
    return [
        {
            "id": b["id"],
            "name": b["name"],
            "tagline": b["tagline"],
            "category": b["category"],
            "badge": b["badge"],
            "icon": b["icon"],
            "color": b["color"],
            "starter_chips": b["starter_chips"],
            "starter_chips_hi": b["starter_chips_hi"],
        }
        for b in EXPERT_BOTS.values()
    ]


def get_bot(bot_id):
    """Returns full configuration for the given bot_id, falling back to 'general'."""
    return EXPERT_BOTS.get(bot_id) or EXPERT_BOTS["general"]
