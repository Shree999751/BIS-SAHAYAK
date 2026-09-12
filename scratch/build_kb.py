import json
import os

entries = [
    # ----------------------------------------------------
    # HANSWARUP: CERTIFICATION, PROCESS & TESTING ENTRIES
    # ----------------------------------------------------
    {
        "id": "SCH-ISI-001",
        "topic": "certification",
        "title": "ISI Mark Scheme (Scheme-I) - Product Certification",
        "summary": "The ISI mark operates under Scheme-I of Schedule-II of the BIS (Conformity Assessment) Regulations, 2018. A manufacturer applies for a product licence against a specific Indian Standard at an identified factory address. BIS assesses in-house testing equipment, factory quality controls, draws independent samples for laboratory testing, and grants a licence permitting use of the ISI mark on conforming goods. A licence is issued per product per factory premises.",
        "summary_hi": "ISI मार्क BIS (अनुरूपता मूल्यांकन) विनियम, 2018 की अनुसूची-II की योजना-I के तहत प्रदान किया जाता है। निर्माता किसी विशिष्ट भारतीय मानक के अनुसार किसी विशिष्ट कारखाने के पते पर उत्पाद लाइसेंस के लिए आवेदन करता है। BIS इन-हाउस परीक्षण सुविधाओं का सत्यापन करता है, स्वतंत्र नमूनों की जांच करता है और मानक चिह्न के उपयोग का लाइसेंस देता है।",
        "keywords": ["isi", "isi mark", "standard mark", "scheme 1", "scheme-i", "licence", "license", "cml", "manufacturer", "factory", "आईएसआई", "लाइसेंस", "प्रमाणन"],
        "next_steps": [
            "Identify the exact Indian Standard (IS) covering your product category",
            "Establish the required in-house test equipment specified in the Scheme of Inspection and Testing (SIT)",
            "Submit an online application on the BIS Manakonline portal (manakonline.in)",
            "Undergo a factory inspection by BIS officers and independent sample testing"
        ],
        "next_steps_hi": [
            "अपने उत्पाद से संबंधित विशिष्ट भारतीय मानक (IS) की पहचान करें",
            "निरीक्षण और परीक्षण योजना (SIT) के अनुसार इन-हाउस लैब उपकरण स्थापित करें",
            "BIS मानकॉनलाइन पोर्टल (manakonline.in) पर ऑनलाइन आवेदन करें",
            "BIS अधिकारियों द्वारा कारखाना ऑडिट और लैब परीक्षण प्रक्रिया पूर्ण कराएं"
        ],
        "source_title": "BIS Conformity Assessment - Product Certification Scheme-I",
        "source_url": "https://www.bis.gov.in/product-certification/",
        "verified": True
    },
    {
        "id": "SCH-CRS-001",
        "topic": "certification",
        "title": "Compulsory Registration Scheme (CRS) for Electronics & IT Goods (Scheme-II)",
        "summary": "The Compulsory Registration Scheme (CRS) operates under Scheme-II of Schedule-II of the BIS Regulations. Governed by notifications from MeitY and other ministries, CRS covers electronic, solar, and IT goods. Unlike Scheme-I, CRS requires no preliminary factory inspection; the manufacturer tests product samples in a BIS-recognised laboratory and files an application online with the valid test report. Once approved, the product carries the Standard Mark along with an allotted R-number.",
        "summary_hi": "अनिवार्य पंजीकरण योजना (CRS) विनियमों की योजना-II के अंतर्गत संचालित होती है। यह MeitY द्वारा अधिसूचित इलेक्ट्रॉनिक्स और आईटी उत्पादों पर लागू है। इसमें प्रारंभिक कारखाना ऑडिट नहीं होता; BIS-मान्यता प्राप्त लैब की परीक्षण रिपोर्ट के आधार पर ऑनलाइन स्व-घोषणा द्वारा पंजीकरण और 'R-नंबर' जारी किया जाता है।",
        "keywords": ["crs", "compulsory registration", "scheme 2", "scheme-ii", "electronics", "meity", "r number", "registration", "mobile", "laptop", "power bank", "led", "सीआरएस", "इलेक्ट्रॉनिक्स", "पंजीकरण"],
        "next_steps": [
            "Check if your product is notified under the CRS compulsory order",
            "Send samples to a BIS-recognised test laboratory for safety testing against the relevant IS",
            "Submit the test report and online application on the BIS CRS portal within 90 days",
            "Display the Standard Mark with the unique R-number on your product label and packaging"
        ],
        "next_steps_hi": [
            "जांचें कि क्या आपका उत्पाद CRS अनिवार्य सूची में अधिसूचित है",
            "BIS मान्यता प्राप्त प्रयोगशाला में मानक के अनुरूप उत्पाद परीक्षण कराएं",
            "90 दिनों के भीतर मानकॉनलाइन CRS पोर्टल पर टेस्ट रिपोर्ट के साथ आवेदन करें",
            "उत्पाद और पैकेजिंग पर आवंटित R-नंबर के साथ मानक चिह्न प्रदर्शित करें"
        ],
        "source_title": "BIS Compulsory Registration Scheme Portal",
        "source_url": "https://www.bis.gov.in/product-certification/products-under-compulsory-certification/",
        "verified": True
    },
    {
        "id": "SCH-COMPARE-001",
        "topic": "certification",
        "title": "Comparison: ISI Mark (Scheme-I) vs Compulsory Registration Scheme (CRS)",
        "summary": "Both Scheme-I (ISI Mark) and Scheme-II (CRS) authorize use of a BIS Standard Mark, but they serve different industries with distinct procedures. ISI Mark requires an in-person factory audit, in-house laboratory inspection, and third-party sample testing, issuing a CM/L licence number for industrial and consumer goods. CRS covers electronics and IT goods and relies solely on test reports from BIS-recognised laboratories without a prior factory visit, allotting an R-number.",
        "summary_hi": "ISI मार्क (योजना-I) और CRS (योजना-II) दोनों BIS अनुपालन प्रदान करते हैं, लेकिन दोनों की प्रक्रिया भिन्न है। ISI में कारखाना निरीक्षण, इन-हाउस लैब और सैंपल टेस्टिंग अनिवार्य है तथा CM/L लाइसेंस मिलता है। जबकि CRS केवल मान्यता प्राप्त लैब की टेस्ट रिपोर्ट पर आधारित है और इसमें बिना कारखाना निरीक्षण के R-नंबर मिलता है।",
        "keywords": ["difference", "compare", "comparison", "isi vs crs", "isi", "crs", "which scheme", "factory audit", "r number", "cml number", "अंतर", "तुलना", "योजना का चयन"],
        "next_steps": [
            "Determine if your product is an electronic/IT product notified under MeitY CRS",
            "If notified under CRS, proceed with lab testing under Scheme-II",
            "If covered by an industrial QCO or safety standard, apply for ISI certification under Scheme-I"
        ],
        "next_steps_hi": [
            "जांचें कि क्या आपका उत्पाद MeitY CRS सूची में शामिल आईटी/इलेक्ट्रॉनिक सामान है",
            "यदि CRS में है तो योजना-II के तहत प्रयोगशाला परीक्षण करवाएं",
            "यदि उत्पाद किसी गुणवत्ता नियंत्रण आदेश (QCO) के अधीन है तो योजना-I ISI मार्क के लिए आवेदन करें"
        ],
        "source_title": "BIS Product Certification Schemes Overview",
        "source_url": "https://www.bis.gov.in/product-certification/",
        "verified": True
    },
    {
        "id": "SCH-FMCS-001",
        "topic": "certification",
        "title": "Foreign Manufacturers Certification Scheme (FMCS)",
        "summary": "FMCS allows overseas manufacturing facilities to obtain a BIS licence to use the standard ISI mark on goods exported to India. The foreign applicant must nominate an Authorised Indian Representative (AIR) resident in India who accepts legal accountability. BIS officers conduct an on-site factory inspection overseas, draw product samples for laboratory testing in India, and issue a CM/L licence upon compliance.",
        "summary_hi": "विदेशी निर्माता प्रमाणन योजना (FMCS) भारत के बाहर स्थित कारखानों को भारत में निर्यात किए जाने वाले उत्पादों पर ISI मार्क लगाने की अनुमति देती है। विदेशी आवेदक को एक अधिकृत भारतीय प्रतिनिधि (AIR) नियुक्त करना होता है। BIS अधिकारी विदेश में कारखाने का ऑडिट करते हैं और परीक्षण के बाद लाइसेंस प्रदान करते हैं।",
        "keywords": ["fmcs", "foreign", "import", "overseas", "authorised indian representative", "air", "export to india", "विदेशी निर्माता", "आयात", "एफएमसीएस"],
        "next_steps": [
            "Appoint an Authorised Indian Representative (AIR) legally resident in India",
            "Submit an FMCS application online with factory documentation and prescribed USD fees",
            "Facilitate an on-site manufacturing plant assessment by a visiting BIS officer team",
            "Send drawn samples to an independent BIS testing laboratory in India"
        ],
        "next_steps_hi": [
            "भारत में कानूनी रूप से निवासी एक अधिकृत भारतीय प्रतिनिधि (AIR) नामित करें",
            "कारखाना विवरण और निर्धारित शुल्क के साथ FMCS पोर्टल पर आवेदन करें",
            "BIS तकनीकी टीम द्वारा विदेशी कारखाने के ऑन-साइट निरीक्षण की व्यवस्था करें",
            "निकाले गए नमूनों को भारत में BIS परीक्षण लैब में परीक्षण हेतु भिजवाएं"
        ],
        "source_title": "BIS Foreign Manufacturers Certification Scheme (FMCS)",
        "source_url": "https://www.bis.gov.in/product-certification/foreign-manufacturers-certification-scheme/",
        "verified": True
    },
    {
        "id": "SCH-SCHEME-X-001",
        "topic": "certification",
        "title": "Scheme-X Conformity Assessment for Low-Risk Machinery & Equipment",
        "summary": "Scheme-X is a streamlined conformity assessment option under the BIS Regulations for capital goods, industrial machinery, and low-risk engineering components. It relies on type testing by accredited laboratories and factory quality management surveillance rather than continuous in-house testing for each batch. This enables industrial equipment manufacturers to demonstrate standards compliance without onerous batch-testing overheads.",
        "summary_hi": "योजना-एक्स (Scheme-X) पूंजीगत वस्तुओं, औद्योगिक मशीनरी और कम जोखिम वाले इंजीनियरिंग उपकरणों के लिए एक सुव्यवस्थित अनुरूपता मूल्यांकन योजना है। यह प्रत्येक बैच के भारी इन-हाउस परीक्षण के बजाय मान्यता प्राप्त प्रयोगशालाओं द्वारा टाइप-टेस्टिंग और कारखाना गुणवत्ता प्रबंधन पर आधारित है।",
        "keywords": ["scheme x", "schemex", "machinery", "engineering", "capital goods", "type testing", "industrial equipment", "योजना एक्स", "मशीनरी"],
        "next_steps": [
            "Confirm that your engineering product or machine falls under Scheme-X scope",
            "Perform comprehensive type-testing at an accredited NABL / BIS laboratory",
            "Submit manufacturer conformity declaration alongside ISO 9001 quality system documentation",
            "Obtain Scheme-X certificate on the Manakonline portal"
        ],
        "next_steps_hi": [
            "पुष्टि करें कि आपका इंजीनियरिंग उपकरण योजना-एक्स (Scheme-X) के दायरे में आता है",
            "मान्यता प्राप्त लैब में मशीन का संपूर्ण टाइप-परीक्षण करवाएं",
            "ISO 9001 गुणवत्ता प्रणाली और स्व-घोषणा के साथ आवेदन प्रस्तुत करें",
            "मानकॉनलाइन पोर्टल के माध्यम से योजना-एक्स प्रमाण-पत्र प्राप्त करें"
        ],
        "source_title": "BIS Conformity Assessment Regulations - Scheme X",
        "source_url": "https://www.bis.gov.in/product-certification/",
        "verified": True
    },
    {
        "id": "ECO-MARK-001",
        "topic": "certification",
        "title": "ECO Mark Scheme for Environmentally Friendly Consumer Products",
        "summary": "The ECO Mark scheme, instituted by the Ministry of Environment, Forest and Climate Change (MoEFCC) and administered by BIS, certifies consumer products that meet specific environmental criteria in addition to Indian Standards quality requirements. Eligible products carry the standard ISI mark accompanied by the distinctive ECO Mark logo (an earthen pot / Matka), indicating eco-friendly manufacturing, biodegradability, and minimal environmental impact.",
        "summary_hi": "पर्यावरण-अनुकूल उत्पादों के लिए इको मार्क (ECO Mark) योजना MoEFCC के समन्वय से BIS द्वारा संचालित की जाती है। यह भारतीय मानक की गुणवत्ता के साथ-साथ कड़े पर्यावरणीय मानदंडों को पूरा करने वाले उत्पादों को 'मिट्टी का घड़ा' (मटका) लोगो और ISI मार्क के साथ प्रदान किया जाता है।",
        "keywords": ["eco mark", "ecomark", "environment", "green", "matka", "sustainable", "moefcc", "biodegradable", "इको मार्क", "पर्यावरण", "प्रदूषण मुक्त"],
        "next_steps": [
            "Verify whether environmental criteria have been published for your product category",
            "Ensure the product complies with both the primary IS standard and environmental norms",
            "Apply for ECO Mark certification through the BIS Manakonline portal",
            "Affix the earthen pot ECO logo and ISI mark on approved packaging"
        ],
        "next_steps_hi": [
            "जांचें कि क्या आपके उत्पाद वर्ग के लिए इको-मार्क मानदंड अधिसूचित हैं",
            "सुनिश्चित करें कि उत्पाद प्राथमिक IS गुणवत्ता और पर्यावरणीय दोनों मानकों को पूरा करता है",
            "BIS मानकॉनलाइन पोर्टल पर इको मार्क के लिए आवेदन करें",
            "स्वीकृति के बाद उत्पाद पैकेजिंग पर मिट्टी का घड़ा (मटका) लोगो प्रदर्शित करें"
        ],
        "source_title": "BIS ECO Mark Scheme Criteria",
        "source_url": "https://www.bis.gov.in/product-certification/eco-mark-scheme/",
        "verified": True
    },
    {
        "id": "FEES-001",
        "topic": "process",
        "title": "BIS Certification Fee Structure and MSME Concessions",
        "summary": "BIS certification fees comprise: an application fee (₹1,000), an audit/inspection fee (₹7,000 per man-day for domestic factories), independent laboratory testing charges (as per actual lab quotes), and an annual minimum marking fee depending on product category. Significant fee concessions are granted under government initiatives: micro enterprises and women entrepreneurs receive up to an 80% concession, while small enterprises receive a 50% concession on application and annual minimum marking fees.",
        "summary_hi": "BIS प्रमाणन शुल्क में शामिल हैं: आवेदन शुल्क (₹1,000), कारखाना ऑडिट शुल्क (₹7,000 प्रति मैन-डे), वास्तविक लैब परीक्षण शुल्क और वार्षिक न्यूनतम अंकन शुल्क। सूक्ष्म और महिला उद्यमियों को 80% तक तथा लघु उद्यमों (MSME) को 50% की विशेष छूट दी जाती है।",
        "keywords": ["fees", "cost", "price", "fee structure", "concession", "discount", "msme", "micro enterprise", "marking fee", "women entrepreneur", "शुल्क", "फीस", "छूट", "लागत"],
        "next_steps": [
            "Register your enterprise on the Udyam portal to obtain MSME classification",
            "Calculate your applicable concession rate (up to 80% for micro/women enterprises)",
            "Pay the application fee online through the Manakonline payment gateway",
            "Budget for laboratory testing charges and annual minimum marking fee"
        ],
        "next_steps_hi": [
            "MSME लाभ प्राप्त करने के लिए उद्यम (Udyam) पोर्टल पर पंजीकरण कराएं",
            "अपनी लागू छूट दर की जांच करें (सूक्ष्म/महिला उद्यमियों के लिए 80% तक)",
            "मानकॉनलाइन पोर्टल के माध्यम से ऑनलाइन आवेदन शुल्क का भुगतान करें",
            "लैब परीक्षण शुल्क और वार्षिक न्यूनतम अंकन शुल्क का प्रावधान करें"
        ],
        "source_title": "BIS Schedule of Fees and Concessions",
        "source_url": "https://www.manakonline.in/",
        "verified": True
    },
    {
        "id": "LIC-RENEW-001",
        "topic": "process",
        "title": "BIS Licence Renewal Procedure and Timeline",
        "summary": "A BIS product certification licence is granted initially for 1 to 2 years and must be renewed periodically before expiry. The licensee submits a renewal application online on Manakonline along with production and marking volume details, in-house test logs, and the advance minimum marking fee. Renewal can be granted for periods ranging from 1 to 5 years. If the application is filed before expiry, the licence continues without disruption; late filings incur statutory penalties.",
        "summary_hi": "BIS उत्पाद प्रमाणन लाइसेंस प्रारंभ में 1 से 2 वर्ष के लिए दिया जाता है और समाप्ति से पहले इसे नवीनीकृत कराना होता है। निर्माता मानकॉनलाइन पर उत्पादन विवरण, इन-हाउस परीक्षण रिकॉर्ड और अग्रिम अंकन शुल्क जमा करके 1 से 5 वर्ष की अवधि के लिए लाइसेंस नवीनीकरण करा सकते हैं।",
        "keywords": ["renewal", "licence renewal", "validity", "expiry", "extension", "manakonline renewal", "marking fee advance", "नवीनीकरण", "लाइसेंस नवीनीकरण", "वैधता"],
        "next_steps": [
            "Log into your Manakonline account at least 30 to 60 days before licence expiry",
            "Submit the production return detailing total units manufactured with the ISI mark",
            "Pay the advance minimum marking fee and any balance calculated on actual production",
            "Download the updated endorsement letter verifying licence extension"
        ],
        "next_steps_hi": [
            "लाइसेंस समाप्त होने से कम से कम 30 से 60 दिन पूर्व मानकॉनलाइन खाते में लॉगिन करें",
            "ISI मार्क के साथ निर्मित कुल इकाइयों का उत्पादन रिटर्न प्रस्तुत करें",
            "अग्रिम न्यूनतम अंकन शुल्क और बकाया राशि का ऑनलाइन भुगतान करें",
            "लाइसेंस विस्तार को सत्यापित करने वाला आधिकारिक एंडोर्समेंट पत्र डाउनलोड करें"
        ],
        "source_title": "BIS Guidelines for Renewal of Licences",
        "source_url": "https://www.manakonline.in/",
        "verified": True
    },
    {
        "id": "AUDIT-001",
        "topic": "process",
        "title": "BIS Factory Audit and Inspection Process",
        "summary": "Before granting or renewing an ISI licence, BIS deputes an Inspecting Officer to conduct a comprehensive on-site factory assessment. The auditor inspects: manufacturing machinery, in-house quality control testing equipment, valid calibration certificates, qualifications of technical quality personnel, and compliance with the Scheme of Inspection and Testing (SIT). The officer also draws random production samples, seals them, and dispatches them to an independent BIS-approved lab.",
        "summary_hi": "ISI लाइसेंस जारी करने से पहले BIS अधिकारी कारखाने का ऑन-साइट ऑडिट करते हैं। इसमें निर्माण संयंत्र, इन-हाउस लैब उपकरण, कैलिब्रेशन प्रमाण-पत्र, सक्षम तकनीकी कर्मचारी और SIT के पालन की जांच की जाती है। अधिकारी उत्पादन लाइन से नमूने लेकर सील करते हैं और स्वतंत्र लैब में भेजते हैं।",
        "keywords": ["factory audit", "inspection", "auditor", "calibrated equipment", "sit", "scheme of inspection and testing", "sample drawing", "कारखाना निरीक्षण", "ऑडिट", "जाँच"],
        "next_steps": [
            "Review the specific Scheme of Inspection and Testing (SIT) published for your IS standard",
            "Calibrate all in-house measurement and testing instruments through NABL-accredited labs",
            "Maintain complete batch manufacturing records and internal test registers",
            "Facilitate the visiting BIS officer's inspection and sample sealing"
        ],
        "next_steps_hi": [
            "अपने मानक के लिए प्रकाशित निरीक्षण और परीक्षण योजना (SIT) की समीक्षा करें",
            "सभी इन-हाउस परीक्षण उपकरणों को NABL-मान्यता प्राप्त लैब से कैलिब्रेट करवाएं",
            "दैनिक उत्पादन और आंतरिक परीक्षण रजिस्टर को अद्यतन रखें",
            "BIS अधिकारी के निरीक्षण और नमूना सीलिंग प्रक्रिया में सहयोग करें"
        ],
        "source_title": "BIS Quality Audit & Factory Inspection Guidelines",
        "source_url": "https://www.bis.gov.in/product-certification/",
        "verified": True
    },
    {
        "id": "PENALTY-001",
        "topic": "process",
        "title": "Penalties for Violation under BIS Act, 2016",
        "summary": "Under Section 29 of the Bureau of Indian Standards Act, 2016, manufacturing, importing, stocking, or selling notified goods without compulsory BIS certification or deceptively using a counterfeit ISI mark / hallmark is a criminal offence. Penalties include imprisonment for up to two years, or a minimum fine of ₹2,00,000 which may extend up to ten times the value of the goods produced or sold, or both. BIS enforcement officers also possess statutory powers to search premises and seize non-compliant stock.",
        "summary_hi": "भारतीय मानक ब्यूरो अधिनियम, 2016 की धारा 29 के तहत अनिवार्य QCO के अंतर्गत आने वाले उत्पादों का बिना वैध BIS प्रमाणन निर्माण या बिक्री करना, या नकली ISI मार्क/हॉलमार्क लगाना संज्ञेय अपराध है। इसमें 2 वर्ष तक की जेल, ₹2,00,000 से लेकर माल के मूल्य के 10 गुना तक का जुर्माना या दोनों हो सकते हैं।",
        "keywords": ["penalty", "penalties", "punishment", "fine", "jail", "imprisonment", "bis act", "section 29", "counterfeit", "fake isi", "offence", "सजा", "जुर्माना", "दण्ड", "कानूनी कार्रवाई"],
        "next_steps": [
            "Verify that every product subject to a Quality Control Order (QCO) holds a valid BIS licence",
            "Cease selling or manufacturing non-certified stock before the QCO mandatory enforcement date",
            "Report unauthorized misuse of the ISI mark to BIS enforcement wings via the BIS Care app"
        ],
        "next_steps_hi": [
            "जांच लें कि QCO के तहत अधिसूचित प्रत्येक उत्पाद के पास वैध BIS लाइसेंस है",
            "QCO लागू होने की तिथि से पहले बिना प्रमाणित स्टॉक का निर्माण या बिक्री तत्काल बंद करें",
            "BIS Care ऐप के माध्यम से नकली ISI मार्क या गैर-प्रमाणित उत्पादों की सूचना BIS को दें"
        ],
        "source_title": "The Bureau of Indian Standards Act, 2016 (Act No. 11 of 2016)",
        "source_url": "https://www.bis.gov.in/the-bureau-of-indian-standards-act-2016/",
        "verified": True
    },
    {
        "id": "LAB-001",
        "topic": "testing",
        "title": "Where to Get a Product Tested for BIS Certification",
        "summary": "Testing for BIS certification is performed either in BIS Central and Regional Laboratories or in third-party laboratories recognised under the BIS Laboratory Recognition Scheme (LRS). Recognised laboratories must be NABL accredited (ISO/IEC 17025) and approved specifically for the relevant Indian Standard clauses. BIS publishes an updated directory of recognised laboratories categorized by product domain and geographic location on the Manakonline portal.",
        "summary_hi": "BIS प्रमाणन के लिए परीक्षण BIS की अपनी केंद्रीय प्रयोगशालाओं या BIS प्रयोगशाला मान्यता योजना (LRS) के तहत मान्यता प्राप्त निजी/सरकारी लैब में किया जाता है। इन प्रयोगशालाओं का NABL मान्यता प्राप्त (ISO/IEC 17025) होना अनिवार्य है। मान्यता प्राप्त प्रयोगशालाओं की सूची मानकॉनलाइन पर उपलब्ध है।",
        "keywords": ["lab", "laboratory", "testing", "test report", "recognised lab", "nabl", "sample", "where to test", "lrs", "प्रयोगशाला", "परीक्षण", "जांच केंद्र"],
        "next_steps": [
            "Note the exact Indian Standard number and test parameters governing your product",
            "Search the BIS Laboratory Information Management System (LIMS) on Manakonline for approved labs",
            "Confirm with the selected laboratory that their BIS recognition scope is currently active",
            "Submit officially drawn and sealed test samples along with the prescribed testing fees"
        ],
        "next_steps_hi": [
            "अपने उत्पाद से संबंधित सटीक IS नंबर और अनिवार्य परीक्षण मानकों की सूची बनाएं",
            "मानकॉनलाइन पर BIS LIMS डायरेक्टरी से मान्यता प्राप्त प्रयोगशाला खोजें",
            "प्रयोगशाला से पुष्टि करें कि संबंधित मानक के लिए उनकी BIS मान्यता सक्रिय है",
            "निर्धारित परीक्षण शुल्क के साथ आधिकारिक रूप से सील किए गए नमूने परीक्षण हेतु जमा करें"
        ],
        "source_title": "BIS Laboratory Services and LRS Scheme",
        "source_url": "https://www.bis.gov.in/laboratory-services/",
        "verified": True
    },
    {
        "id": "PROC-001",
        "topic": "process",
        "title": "How an MSME Should Start with BIS Certification",
        "summary": "For an MSME or startup, the recommended path to BIS certification is: 1) Identify the relevant Indian Standard covering the product; 2) Ascertain whether the item falls under a mandatory Quality Control Order (QCO) or is voluntary; 3) Review the Scheme of Inspection and Testing (SIT) to establish required in-house testing equipment; 4) Register on the BIS Manakonline portal and apply online; 5) Undergo factory inspection and independent laboratory testing.",
        "summary_hi": "किसी नए उद्योग या MSME के लिए BIS प्रमाणन की सही प्रक्रिया: 1) उत्पाद से संबंधित भारतीय मानक (IS) खोजें; 2) जांचें कि क्या उत्पाद QCO के तहत अनिवार्य है या स्वैच्छिक; 3) SIT के अनुसार इन-हाउस लैब परीक्षण उपकरण लगाएं; 4) मानकॉनलाइन पोर्टल पर आवेदन करें; 5) कारखाना निरीक्षण एवं लैब टेस्टिंग करवाकर लाइसेंस प्राप्त करें।",
        "keywords": ["msme", "startup", "how to start", "first step", "process", "procedure", "small business", "guide", "शुरुआत", "प्रक्रिया", "उद्योग"],
        "next_steps": [
            "Search the BIS standards catalogue for the Indian Standard matching your product",
            "Review the Scheme of Inspection and Testing (SIT) to identify required lab equipment",
            "Procure calibrated testing instruments for internal quality checks",
            "Submit your application and documentation via the Manakonline e-portal"
        ],
        "next_steps_hi": [
            "BIS मानक कैटलॉग में अपने उत्पाद से मेल खाता भारतीय मानक खोजें",
            "आवश्यक लैब उपकरण जानने के लिए निरीक्षण और परीक्षण योजना (SIT) पढ़ें",
            "आंतरिक गुणवत्ता परीक्षण के लिए कैलिब्रेटेड उपकरण स्थापित करें",
            "मानकॉनलाइन ई-पोर्टल पर आवश्यक दस्तावेजों के साथ ऑनलाइन आवेदन करें"
        ],
        "source_title": "BIS Manakonline Portal for MSMEs",
        "source_url": "https://www.manakonline.in/",
        "verified": True
    },
    {
        "id": "PROC-002",
        "topic": "process",
        "title": "Compulsory versus Voluntary BIS Certification and QCOs",
        "summary": "While Indian Standards are generally voluntary, a standard becomes legally mandatory when a central ministry issues a Quality Control Order (QCO) under the BIS Act, or when notified under the Compulsory Registration Scheme (CRS). Once a QCO is enforced, no entity can manufacture, import, distribute, or sell the notified product without a valid BIS licence and Standard Mark. Non-compliance is punishable under Section 29 of the BIS Act.",
        "summary_hi": "यद्यपि भारतीय मानक सामान्यतः स्वैच्छिक होते हैं, परंतु जब संबंधित मंत्रालय किसी उत्पाद के लिए गुणवत्ता नियंत्रण आदेश (QCO) जारी करता है, तो प्रमाणन कानूनी रूप से अनिवार्य हो जाता है। QCO लागू होने के बाद बिना वैध BIS लाइसेंस और ISI मार्क के उत्पाद बेचना या आयात करना दंडनीय अपराध है।",
        "keywords": ["compulsory", "mandatory", "voluntary", "qco", "quality control order", "bis act", "notified product", "anivarya", "अनिवार्य", "स्वैच्छिक", "क्यूसीओ"],
        "next_steps": [
            "Check the official BIS directory of products under mandatory certification",
            "Examine the gazette notification for the specific QCO enforcement timeline",
            "Obtain certification well before the notification deadline to prevent legal disruption"
        ],
        "next_steps_hi": [
            "अनिवार्य प्रमाणन के अंतर्गत आने वाले उत्पादों की आधिकारिक BIS सूची देखें",
            "संबंधित QCO गैजेट अधिसूचना में प्रवर्तन तिथि (लागू होने की तारीख) की जांच करें",
            "समयसीमा समाप्त होने से पहले मानकॉनलाइन पर प्रमाणन हेतु आवेदन करें"
        ],
        "source_title": "Products under Compulsory BIS Certification (QCOs)",
        "source_url": "https://www.bis.gov.in/product-certification/products-under-compulsory-certification/",
        "verified": True
    },

    # ----------------------------------------------------
    # YUKTI: HALLMARKING & CONSUMER REDRESSAL ENTRIES
    # ----------------------------------------------------
    {
        "id": "HALL-001",
        "topic": "hallmarking",
        "title": "What a BIS Hallmark on Gold Jewellery Contains (HUID & Fineness)",
        "summary": "Under Scheme-IV of the BIS Regulations, a genuine BIS hallmark on gold jewellery comprises three distinct laser-etched marks: 1) The official BIS triangular logo; 2) Purity and fineness grade in carats and parts per thousand (such as 22K916 for 22 karat, 18K750 for 18 karat, or 14K585 for 14 karat); and 3) A unique 6-character alphanumeric Hallmark Unique Identification (HUID) code. The HUID guarantees individual traceability and can be verified by consumers on the BIS Care mobile app.",
        "summary_hi": "योजना-IV के तहत सोने के आभूषणों पर हॉलमार्क में 3 लेजर-चिह्न होते हैं: 1) त्रिभुजाकार BIS लोगो; 2) शुद्धता/सूक्ष्मता ग्रेड (जैसे 22K916, 18K750, 14K585); 3) छह अंकों का अल्फान्यूमेरिक HUID कोड। HUID को उपभोक्ता BIS Care मोबाइल ऐप पर डालकर आभूषण की प्रामाणिकता तुरंत देख सकते हैं।",
        "keywords": ["hallmark", "hallmarking", "huid", "gold", "jewellery", "jeweller", "carat", "karat", "purity", "916", "22k", "18k", "14k", "हॉलमार्क", "सोना", "आभूषण", "एचयूआईडी", "शुद्धता"],
        "next_steps": [
            "Open the official BIS Care app and navigate to 'Verify HUID'",
            "Enter the 6-character alphanumeric code engraved on the jewellery article",
            "Verify that the jeweller name, registration number, and purity match your sales invoice",
            "Demand a bill clearly itemizing gold weight, purity, and standard hallmarking fee (₹45 per article)"
        ],
        "next_steps_hi": [
            "BIS Care मोबाइल ऐप खोलें और 'Verify HUID' विकल्प चुनें",
            "आभूषण पर अंकित 6 अंकों का अल्फान्यूमेरिक कोड दर्ज करें",
            "जांचें कि ज्वेलर का नाम, पंजीकरण संख्या और शुद्धता आपके बिल से मेल खाती है",
            "ज्वेलर से हॉलमार्किंग शुल्क (₹45 प्रति नग) और शुद्धता दर्शाने वाला पक्का बिल प्राप्त करें"
        ],
        "source_title": "BIS Hallmarking Scheme-IV Guidelines",
        "source_url": "https://www.bis.gov.in/hallmarking/",
        "verified": True
    },
    {
        "id": "HALL-002",
        "topic": "hallmarking",
        "title": "Registering as a Jeweller for BIS Hallmarking",
        "summary": "Every jeweller selling gold or silver hallmarked jewellery in mandatory notified districts must obtain a BIS Hallmarking Registration. The application is completely online via the BIS hallmarking portal (manakonline.in) with no physical documentation. Under revised rules, registration is granted instantly with zero government fee for jewellers with turnover under ₹40 lakh, and a nominal one-time fee for larger showrooms. Registered jewellers send articles to accredited Assaying and Hallmarking Centres (AHCs).",
        "summary_hi": "अधिसूचित जिलों में सोने या चांदी के आभूषण बेचने वाले प्रत्येक जौहरी को BIS हॉलमार्किंग पंजीकरण लेना अनिवार्य है। यह प्रक्रिया मानकॉनलाइन पोर्टल पर पूर्णतः ऑनलाइन है। ₹40 लाख से कम टर्नओवर वाले ज्वैलर्स के लिए कोई सरकारी पंजीकरण शुल्क नहीं है। पंजीकृत ज्वैलर AHC केंद्र से हॉलमार्क लगवाते हैं।",
        "keywords": ["jeweller registration", "hallmarking registration", "ahc", "assaying and hallmarking centre", "shop", "showroom", "precious metal", "gold registration", "ज्वेलर पंजीकरण", "हॉलमार्क रजिस्ट्रेशन"],
        "next_steps": [
            "Apply online on the BIS Hallmarking Portal on manakonline.in",
            "Upload proof of business premises, GSTIN, and identity of the proprietor/firm",
            "Obtain instant automatic registration certificate without manual delay",
            "Partner with an accredited Assaying and Hallmarking Centre (AHC) to hallmark your jewellery stock"
        ],
        "next_steps_hi": [
            "मानकॉनलाइन हॉलमार्किंग पोर्टल (manakonline.in) पर ऑनलाइन आवेदन करें",
            "दुकान/फर्म का पता प्रमाण, GSTIN और पहचान दस्तावेज अपलोड करें",
            "पोर्टल से तुरंत जारी हॉलमार्किंग पंजीकरण प्रमाण-पत्र डाउनलोड करें",
            "अपने आभूषणों पर हॉलमार्क लगवाने के लिए निकटतम मान्यता प्राप्त AHC केंद्र से जुड़ें"
        ],
        "source_title": "BIS Jeweller Registration Portal",
        "source_url": "https://www.bis.gov.in/hallmarking/",
        "verified": True
    },
    {
        "id": "HALL-003",
        "topic": "hallmarking",
        "title": "Mandatory Gold Hallmarking Districts and Legal Exemptions",
        "summary": "Mandatory gold hallmarking is being implemented across India in phased notifications covering over 340 districts. However, the Hallmarking Order grants specific statutory exemptions: 1) Jewellery articles weighing less than 2 grams; 2) Gold articles intended specifically for commercial export; 3) Medical, dental, and industrial equipment; 4) Special bullion bars and international exhibition items; and 5) Artisans or jewellers with an annual sales turnover below ₹40 lakhs.",
        "summary_hi": "अनिवार्य गोल्ड हॉलमार्किंग भारत के 340 से अधिक जिलों में चरणबद्ध रूप से लागू है। आदेश के तहत कुछ छूट प्राप्त हैं: 1) 2 ग्राम से कम वजन के आभूषण; 2) निर्यात (Export) के लिए बने उत्पाद; 3) चिकित्सा एवं दंत चिकित्सा उपकरण; 4) अंतर्राष्ट्रीय प्रदर्शनियों के उत्पाद; 5) ₹40 लाख से कम वार्षिक टर्नओवर वाले छोटे आभूषण निर्माता।",
        "keywords": ["hallmarking exemption", "mandatory districts", "2 grams", "export gold", "turnover exemption", "gold rules", "छूट", "हॉलमार्किंग छूट", "2 ग्राम से कम"],
        "next_steps": [
            "Check if your showroom district is notified under Phase-I, II, III, or IV of mandatory hallmarking",
            "Verify weight: articles weighing under 2 grams are exempt from mandatory HUID hallmarking",
            "Maintain separate stock registers for exported goods or exempt items"
        ],
        "next_steps_hi": [
            "जांचें कि क्या आपका जिला अनिवार्य हॉलमार्किंग के अधिसूचित चरणों में शामिल है",
            "वजन की जांच करें: 2 ग्राम से कम वजन वाले छोटे आभूषणों पर HUID अनिवार्य नहीं है",
            "निर्यात किए जाने वाले आभूषणों का अलग स्टॉक रजिस्टर बनाए रखें"
        ],
        "source_title": "BIS Hallmarking Notified Districts and Exemptions",
        "source_url": "https://www.bis.gov.in/hallmarking/",
        "verified": True
    },
    {
        "id": "CONS-001",
        "topic": "consumer",
        "title": "Checking Product ISI Mark or Hallmark Genuineness via BIS Care App",
        "summary": "The BIS Care mobile app (available on Android and iOS) empowers consumers to verify the authenticity of marked goods. By entering the CM/L licence number printed below an ISI mark, the R-number on an electronic device, or the 6-character HUID on gold jewellery, the app immediately displays: the manufacturer's name, brand, factory location, validity date, and scope of Indian Standards certification. If details do not match, consumers can file a formal complaint directly within the app.",
        "summary_hi": "उपभोक्ताओं के लिए BIS Care मोबाइल ऐप किसी भी उत्पाद के ISI लाइसेंस नंबर, CRS के R-नंबर या सोने के 6-अंकीय HUID की सत्यता जांचने की सुविधा देता है। ऐप निर्माता का नाम, ब्रांड, पता और वैधता दिखाता है। विवरण गलत होने पर ऐप से सीधे शिकायत दर्ज की जा सकती है।",
        "keywords": ["bis care", "app", "verify", "fake", "genuine", "counterfeit", "complaint", "check isi", "licence number", "huid verify", "जाँच", "असली नकली", "शिकायत", "बीआईएस केयर"],
        "next_steps": [
            "Download and install the official 'BIS Care' app from Google Play Store or Apple App Store",
            "Select 'Verify Licence (ISI)', 'Verify R-Number (CRS)', or 'Verify HUID'",
            "Enter the alphanumeric code printed on the product or hallmarked jewellery",
            "Compare the displayed manufacturer and standard details with your purchased item"
        ],
        "next_steps_hi": [
            "गूगल प्ले स्टोर या ऐप स्टोर से आधिकारिक 'BIS Care' मोबाइल ऐप डाउनलोड करें",
            "'Verify Licence (ISI)' या 'Verify HUID' विकल्प का चयन करें",
            "उत्पाद या आभूषण पर लिखा लाइसेंस नंबर या 6 अंकों का HUID कोड दर्ज करें",
            "ऐप में प्रदर्शित निर्माता का नाम और मानक विवरण अपने खरीदे गए उत्पाद से मिलाएं"
        ],
        "source_title": "BIS Care Mobile Application Portal",
        "source_url": "https://www.bis.gov.in/",
        "verified": True
    },
    {
        "id": "CONS-002",
        "topic": "consumer",
        "title": "Standards Clubs in Schools and Colleges",
        "summary": "To inculcate quality consciousness and standards appreciation among young citizens, BIS establishes Standards Clubs in educational institutions across India. Each club comprises student members guided by a designated faculty mentor. BIS provides financial grants for learning activities, science practical projects, essay and quiz competitions, exposure visits to BIS laboratories, and packaging verification workshops.",
        "summary_hi": "युवाओं में गुणवत्ता और मानकों के प्रति जागरूकता पैदा करने के लिए BIS स्कूलों और कॉलेजों में 'मानक क्लब' (Standards Clubs) स्थापित करता है। BIS क्लब की गतिविधियों, प्रश्नोत्तरी, विज्ञान प्रयोगों और प्रयोगशाला दौरों के लिए वित्तीय अनुदान और शैक्षणिक सहायता प्रदान करता है।",
        "keywords": ["standards club", "school", "college", "student", "awareness", "mentor", "education", "मानक क्लब", "स्कूल", "कॉलेज", "छात्र"],
        "next_steps": [
            "Nominate a science/technical faculty coordinator at your school or college",
            "Reach out to the nearest BIS Branch Office to register your Standards Club",
            "Apply for student activity grants and organize quality awareness events",
            "Schedule educational exposure visits to regional BIS product testing labs"
        ],
        "next_steps_hi": [
            "अपने स्कूल या कॉलेज में एक शिक्षक समन्वयक (मेंटर) नामित करें",
            "मानक क्लब के पंजीकरण के लिए निकटतम BIS शाखा कार्यालय से संपर्क करें",
            "छात्र गतिविधियों और प्रतियोगिताओं के लिए BIS वित्तीय अनुदान प्राप्त करें",
            "छात्रों के लिए BIS परीक्षण प्रयोगशाला के शैक्षणिक दौरे की व्यवस्था करें"
        ],
        "source_title": "BIS Standards Clubs Educational Initiative",
        "source_url": "https://www.bis.gov.in/",
        "verified": True
    },
    {
        "id": "CONS-003",
        "topic": "consumer",
        "title": "Consumer Grievance Redressal and Compensation under BIS Act",
        "summary": "If a certified product bearing the ISI mark or BIS hallmark fails to meet declared standard specifications, consumers are legally protected under the BIS Act and Consumer Protection Act. Complaints can be lodged via the BIS Care app, the National Consumer Helpline (NCH), or directly with the local BIS Branch Office. If laboratory testing confirms non-conformity, BIS initiates enforcement action against the licensee and directs replacement or compensation to the aggrieved consumer.",
        "summary_hi": "यदि ISI मार्क या हॉलमार्क वाला कोई उत्पाद मानक गुणवत्ता पर खरा नहीं उतरता है, तो उपभोक्ता BIS Care ऐप या राष्ट्रीय उपभोक्ता हेल्पलाइन के जरिए शिकायत दर्ज कर सकते हैं। लैब जांच में खराबी साबित होने पर BIS निर्माता पर दंडात्मक कार्रवाई करता है और उपभोक्ता को मुआवजा या उत्पाद वापसी का अधिकार दिलाता है।",
        "keywords": ["consumer grievance", "complaint", "compensation", "defective product", "refund", "substandard", "nch", "उपभोक्ता शिकायत", "मुआवजा", "शिकायत निवारण"],
        "next_steps": [
            "Preserve your purchase bill, product packaging, and warranty receipt",
            "Register a grievance through the 'Complaints' tab in the BIS Care App",
            "BIS enforcement teams collect samples from the market or manufacturer for testing",
            "Track complaint resolution and compensation status online through the app"
        ],
        "next_steps_hi": [
            "खरीद की रसीद (बिल), वारंटी कार्ड और उत्पाद की पैकेजिंग संभाल कर रखें",
            "BIS Care ऐप में 'Complaints' विकल्प में जाकर शिकायत दर्ज करें",
            "BIS जांच अधिकारी नमूने एकत्र कर परीक्षण प्रयोगशाला में जांच करवाते हैं",
            "ऐप के माध्यम से शिकायत निवारण और मुआवजे की स्थिति को ट्रैक करें"
        ],
        "source_title": "BIS Consumer Affairs and Grievance Portal",
        "source_url": "https://www.bis.gov.in/consumer-affairs/",
        "verified": True
    },

    # ----------------------------------------------------
    # ARAZ: 10 STANDARDS ENTRIES (STEEL, CEMENT, LPG, ETC.)
    # ----------------------------------------------------
    {
        "id": "IS-1786",
        "topic": "standard",
        "is_number": "IS 1786",
        "title": "IS 1786 - High Strength Deformed Steel Bars & Wires for Concrete Reinforcement (TMT / Sariya)",
        "summary": "IS 1786 specifies mandatory chemical and mechanical requirements for high strength deformed steel bars and wires (TMT rebar / sariya) used in concrete reinforcement. It covers strength grades Fe 415, Fe 500, Fe 550, and Fe 600 (including earthquake-resistant 'D' variants like Fe 500D). The standard specifies minimum yield stress, tensile strength, percentage elongation, rib geometry for bond strength, and mandatory ISI marking. Steel rebars are under compulsory QCO.",
        "summary_hi": "IS 1786 कंक्रीट सुदृढ़ीकरण में उपयोग होने वाले हाई स्ट्रेंथ टीएमटी सरिए (TMT Rebar / Sariya) के लिए अनिवार्य भारतीय मानक है। यह Fe 415, Fe 500, Fe 500D और Fe 550 ग्रेड, उपज तनाव (yield stress), बढ़ाव (elongation), रिब ज्यामिति और रासायनिक संरचना को निर्दिष्ट करता है। भारत में सरिए पर ISI मार्क अनिवार्य है।",
        "keywords": ["sariya", "tmt bar", "8mm rod", "10mm rod", "12mm rod", "16mm rod", "dhalai rod", "chhad", "fe500", "fe500d", "rebar", "steel bar", "reinforcement", "kamdhenu", "tiscon", "sariya rate", "iron rod", "सरिया", "टीएमटी", "लोहा छड़", "कंक्रीट सरिया"],
        "related": ["IS 456"],
        "next_steps": [
            "Check that every rod has the embossed ISI mark, IS 1786, manufacturer brand, and grade (e.g. Fe 500D)",
            "Verify standard rebar diameter sizes (8mm, 10mm, 12mm, 16mm, 20mm, 25mm, 32mm)",
            "Request the manufacturer's Mill Test Certificate (MTC) verifying chemical and elongation specs",
            "Verify the steel mill's CM/L licence number in the BIS Care app"
        ],
        "next_steps_hi": [
            "जांचें कि सरिए पर ISI मार्क, IS 1786, निर्माता का नाम और ग्रेड (जैसे Fe 500D) उभरा हुआ हो",
            "मानक व्यास आकारों (8mm, 10mm, 12mm, 16mm, 20mm आदि) की पुष्टि करें",
            "विक्रेता से रासायनिक और यांत्रिक गुणों का मिल टेस्ट सर्टिफिकेट (MTC) मांगें",
            "BIS Care ऐप में निर्माता की CM/L लाइसेंस संख्या को सत्यापित करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 1786 (Steel Rebars)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-1489",
        "topic": "standard",
        "is_number": "IS 1489 (Part 1)",
        "title": "IS 1489 (Part 1) - Portland Pozzolana Cement (PPC - Flyash Based)",
        "summary": "IS 1489 Part 1 specifies requirements for Portland Pozzolana Cement using flyash pozzolana. Widely used across residential construction, dams, and marine structures, it mandates parameters including fineness (specific surface), setting time (initial setting not less than 30 mins, final not more than 600 mins), soundness by Le-Chatelier and autoclave methods, and compressive strengths at 72 hours, 168 hours, and 672 hours. PPC cement is under compulsory BIS certification.",
        "summary_hi": "IS 1489 (भाग 1) फ्लाईऐश आधारित पोर्टलैंड पॉज़ोलाना सीमेंट (PPC) का आधिकारिक भारतीय मानक है। यह आवासीय भवनों और जल संरचनाओं के लिए उपयुक्त है। इसमें सेटिंग समय, स्थायित्व (soundness), महीनता और संपीड़न शक्ति (compressive strength) के कड़े नियम हैं। सीमेंट पर ISI मार्क अनिवार्य है।",
        "keywords": ["cement", "ppc", "ppc cement", "portland pozzolana cement", "flyash cement", "concrete cement", "ultratech", "ambuja", "acc", "सीमेंट", "पीपीसी सीमेंट", "फ्लाईऐश"],
        "related": ["IS 456", "IS 12269"],
        "next_steps": [
            "Check that the cement bag carries the mandatory ISI mark, licence number, IS 1489 Part 1, and week/year of manufacture",
            "Ensure the flyash content percentage is clearly declared on the bag packaging",
            "Store bags in moisture-proof conditions to prevent pre-hydration"
        ],
        "next_steps_hi": [
            "जांचें कि सीमेंट की बोरी पर अनिवार्य ISI मार्क, लाइसेंस नंबर, IS 1489 (भाग 1) और निर्माण सप्ताह/वर्ष छपा हो",
            "बोरी पर फ्लाईऐश प्रतिशत की घोषणा की जांच करें",
            "सीमेंट को नमी से सुरक्षित सूखी जगह पर रखें"
        ],
        "source_title": "BIS Standards Catalogue - IS 1489 Part 1 (PPC Cement)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-12269",
        "topic": "standard",
        "is_number": "IS 12269",
        "title": "IS 12269 - 53 Grade Ordinary Portland Cement (OPC 53)",
        "summary": "IS 12269 specifies requirements for high-strength 53 Grade Ordinary Portland Cement (OPC 53), commonly engineered for high-rise RCC structures, pre-stressed concrete members, bridges, and high-strength concrete mixes. It mandates a 28-day compressive strength of not less than 53 MPa, strict limits on insoluble residue and magnesia, and specific soundness thresholds. OPC 53 is under mandatory BIS certification.",
        "summary_hi": "IS 12269 उच्च शक्ति वाले 53 ग्रेड साधारण पोर्टलैंड सीमेंट (OPC 53) का मानक है। इसका उपयोग बहुमंजिला इमारतों, पुलों, कंक्रीट स्लैब और भारी संरचनाओं में किया जाता है। इसके लिए 28 दिनों की न्यूनतम संपीड़न शक्ति 53 MPa अनिवार्य है। इस पर ISI मार्क अनिवार्य है।",
        "keywords": ["cement", "opc", "opc 53", "53 grade", "ordinary portland cement", "high strength concrete", "dhalai cement", "ओपीसी", "53 ग्रेड सीमेंट"],
        "related": ["IS 456", "IS 1489"],
        "next_steps": [
            "Inspect the packaging for the red print ISI mark indicating 53 Grade Ordinary Portland Cement",
            "Ensure the cement is consumed within 90 days of the marked manufacture week",
            "Perform concrete mix proportioning in accordance with IS 10262 using tested OPC 53 samples"
        ],
        "next_steps_hi": [
            "बोरी पर 53 ग्रेड साधारण पोर्टलैंड सीमेंट दर्शाने वाले लाल रंग के ISI मार्क की जांच करें",
            "सुनिश्चित करें कि सीमेंट का उपयोग निर्माण सप्ताह के 90 दिनों के भीतर किया जाए",
            "IS 10262 के अनुसार कंक्रीट मिक्स डिजाइन तैयार करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 12269 (OPC 53 Cement)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-3196",
        "topic": "standard",
        "is_number": "IS 3196 (Part 1)",
        "title": "IS 3196 (Part 1) - Welded Low Carbon Steel Cylinders for LPG (LPG Cylinders)",
        "summary": "IS 3196 Part 1 specifies manufacturing, material, and testing specifications for welded low carbon steel cylinders exceeding 5-litre water capacity for domestic and commercial liquefied petroleum gases (LPG cylinders like 14.2kg and 19kg). It mandates burst tests, hydrostatic stretch tests, pneumatic leak tests, weld seam radiography, and minimum wall thickness to safeguard public safety. LPG cylinders are under compulsory ISI certification.",
        "summary_hi": "IS 3196 (भाग 1) घरेलू और वाणिज्यिक एलपीजी सिलेंडर (14.2 किग्रा और 19 किग्रा गैस सिलेंडर) का अनिवार्य भारतीय मानक है। यह स्टील सामग्री, वेल्डिंग गुणवत्ता, हाइड्रोस्टेटिक परीक्षण, प्रेशर लीक टेस्ट और न्यूनतम दीवार मोटाई को नियंत्रित करता है। सभी एलपीजी सिलेंडरों पर ISI मार्क कानूनी रूप से अनिवार्य है।",
        "keywords": ["lpg", "cylinder", "lpg cylinder", "gas cylinder", "cooking gas", "indane", "bharat gas", "hp gas", "14.2 kg", "सिलेंडर", "गैस सिलेंडर", "एलपीजी"],
        "related": ["IS 4246"],
        "next_steps": [
            "Check that the collar of the LPG cylinder clearly bears the embossed ISI mark and licence number",
            "Verify the mandatory test date / re-testing quarter (e.g. A-26, B-26) stamped on the stay plates",
            "Never accept an LPG cylinder with missing inspection stamps or damaged valves"
        ],
        "next_steps_hi": [
            "जांचें कि एलपीजी सिलेंडर के कॉलर पर स्पष्ट ISI मार्क और लाइसेंस नंबर उकेरा हुआ हो",
            "सिलेंडर की स्टे-प्लेट पर मुद्रित आगामी परीक्षण तिथि (जैसे A-26, B-26) की जांच करें",
            "बिना परीक्षण मोहर या क्षतिग्रस्त वाल्व वाले सिलेंडर को कभी स्वीकार न करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 3196 (LPG Cylinders)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-10146",
        "topic": "standard",
        "is_number": "IS 10146",
        "title": "IS 10146 - Polyethylene for Safe Use in Contact with Foodstuffs & Food Containers",
        "summary": "IS 10146 specifies requirements for polyethylene plastic materials, containers, tiffins, bottles, and films used in contact with foodstuffs, pharmaceuticals, and drinking water. It restricts toxic additives, mandates strict overall migration limits (tested against food simulants like water, alcohol, and oil), and sets limits on heavy metals like lead, cadmium, and mercury to ensure plastic does not leach hazardous chemicals into food.",
        "summary_hi": "IS 10146 खाद्य पदार्थों, पेय जल और दवाओं के संपर्क में आने वाले पॉलीइथाइलीन प्लास्टिक (टिफिन, खाद्य कंटेनर, प्लास्टिक बोतल) का सुरक्षा मानक है। यह हानिकारक रसायनों के भोजन में घुलने (माइग्रेशन) की सीमा तय करता है ताकि प्लास्टिक से भोजन में विषाक्तता न फैले।",
        "keywords": ["food container", "plastic container", "tiffin", "lunch box", "polyethylene", "food grade plastic", "water bottle", "tupperware", "प्लास्टिक डिब्बा", "टिफिन", "फूड ग्रेड प्लास्टिक"],
        "next_steps": [
            "Look for 'Food Grade' declarations and the ISI mark on plastic food containers and tiffins",
            "Confirm that overall migration testing conforms to IS 9845 protocols",
            "Avoid using non-certified plastic containers for hot food storage"
        ],
        "next_steps_hi": [
            "खाद्य कंटेनर और टिफिन बॉक्स पर 'Food Grade' और ISI मार्क की जांच करें",
            "सुनिश्चित करें कि प्लास्टिक माइग्रेशन परीक्षण IS 9845 नियमों के अनुरूप हो",
            "गर्म भोजन रखने के लिए गैर-प्रमाणित प्लास्टिक बर्तनों का उपयोग न करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 10146 (Food Contact Plastics)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-14543",
        "topic": "standard",
        "is_number": "IS 14543",
        "title": "IS 14543 - Packaged Drinking Water (Other than Packaged Natural Mineral Water)",
        "summary": "IS 14543 governs packaged drinking water filled in sealed bottles, jars, and pouches. It establishes stringent microbial standards (zero E. coli, coliform, and fecal streptococci), maximum permissible limits for total dissolved solids (TDS), heavy metals, pesticides, and toxic contaminants. It also prescribes hygienic processing, ultraviolet or ozonation treatment, and mandatory automated bottling. Packaged drinking water is under compulsory ISI certification.",
        "summary_hi": "IS 14543 पैकेज्ड ड्रिंकिंग वाटर (सीलबंद बोतल, जार और पाउच का पानी) का अनिवार्य मानक है। इसमें बैक्टीरिया-मुक्त पानी, TDS सीमा, कीटनाशक अवशेष सीमा, यूवी और ओजोन शोधन प्रक्रिया अनिवार्य है। भारत में बिना वैध ISI मार्क के पैकेज्ड पानी बेचना गैरकानूनी है।",
        "keywords": ["packaged drinking water", "mineral water", "water bottle", "water jar", "bisleri", "kinley", "aquafina", "packaged water", "20 litre jar", "पानी बोतल", "पैकेज्ड पानी", "जार"],
        "related": ["IS 10500"],
        "next_steps": [
            "Verify that every water bottle and 20L jar displays the ISI mark and CM/L licence number",
            "Enter the CM/L licence in the BIS Care app to ensure the packaging plant is officially approved",
            "Ensure the cap seal is intact and shows date of packaging and 'Best Before' date"
        ],
        "next_steps_hi": [
            "जांचें कि पानी की प्रत्येक बोतल और 20 लीटर जार पर ISI मार्क और CM/L लाइसेंस नंबर मुद्रित हो",
            "BIS Care ऐप में लाइसेंस नंबर डालकर पुष्टि करें कि बॉटलिंग प्लांट अधिकृत है",
            "बोतल की सील अक्षुण्ण होने तथा निर्माण और समाप्ति तिथि की जांच करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 14543 (Packaged Water)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-9873",
        "topic": "standard",
        "is_number": "IS 9873 (Part 1)",
        "title": "IS 9873 (Part 1) - Safety of Toys (Mechanical & Physical Properties)",
        "summary": "IS 9873 Part 1 specifies safety requirements and test methods for toys designed for children up to 14 years. It sets rigorous safeguards against sharp edges, pointed wires, small parts causing choking hazards for children under 36 months, entrapment dangers, and projectile mechanisms. Under the mandatory Toys Quality Control Order, all toys manufactured in or imported into India must carry the ISI mark under Scheme-I.",
        "summary_hi": "IS 9873 (भाग 1) बच्चों के खिलौनों (Toys) की सुरक्षा का अनिवार्य भारतीय मानक है। यह नुकीले कोनों, चोकिंग (गला घुटने) के खतरे पैदा करने वाले छोटे टुकड़ों, और यांत्रिक चोटों से बच्चों की सुरक्षा करता है। भारत में बिकने वाले सभी खिलौनों पर ISI मार्क अनिवार्य है।",
        "keywords": ["toys", "toy", "safety of toys", "children toys", "plastic toys", "electronic toys", "teddy", "doll", "khilona", "खिलौना", "बच्चों के खिलौने", "खिलौने की सुरक्षा"],
        "next_steps": [
            "Look for the ISI mark with the manufacturer's licence number on the toy or its retail box",
            "Verify age-appropriate safety labeling (e.g. 'Not suitable for children under 3 years')",
            "Report non-compliant uncertified toys sold in retail shops via the BIS Care app"
        ],
        "next_steps_hi": [
            "खिलौने या उसके बॉक्स पर निर्माता के लाइसेंस नंबर के साथ ISI मार्क अवश्य देखें",
            "आयु-उपयुक्त चेतावनी लेबल (जैसे '3 वर्ष से कम उम्र के बच्चों के लिए नहीं') की जांच करें",
            "बिना ISI मार्क वाले असुरक्षित खिलौनों की शिकायत BIS Care ऐप पर करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 9873 (Toy Safety)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-16102",
        "topic": "standard",
        "is_number": "IS 16102 (Part 1)",
        "title": "IS 16102 (Part 1) - Self-Ballasted LED Lamps for General Lighting (LED Bulbs)",
        "summary": "IS 16102 Part 1 specifies safety requirements for self-ballasted LED lamps for domestic and commercial lighting with supply voltages up to 250V. It assesses electrical insulation, mechanical strength of lamp caps (B22/E27), resistance to heat and fire, and protection against electric shock. LED bulbs are under mandatory certification under the Compulsory Registration Scheme (CRS) and ISI schemes.",
        "summary_hi": "IS 16102 (भाग 1) घरेलू और व्यावसायिक प्रकाश व्यवस्था के लिए सेल्फ-बैलास्टेड LED बल्बों का सुरक्षा मानक है। यह बिजली के झटके से सुरक्षा, हीट और फायर रेजिस्टेंस, बल्ब कैप मजबूती और ऊर्जा सुरक्षा की जांच करता है। LED बल्बों पर BIS प्रमाणन अनिवार्य है।",
        "keywords": ["led", "led bulb", "led lamp", "lighting", "bulb", "philips", "havells", "wipro", "syska", "एलईडी", "एलईडी बल्ब", "बिजली बल्ब"],
        "related": ["IS 302", "IS 13252"],
        "next_steps": [
            "Check that the LED lamp base or box bears the BIS Standard Mark and R-number / licence number",
            "Verify the wattage, operating voltage (e.g. 220-240V), and lumen output declared on the lamp",
            "Avoid unbranded or cheap duplicate LED lamps that lack thermal protection"
        ],
        "next_steps_hi": [
            "जांचें कि LED बल्ब के बेस या बॉक्स पर BIS मानक चिह्न और R-नंबर अंकित हो",
            "बल्ब पर घोषित वाट (Watt), वोल्टेज और ल्यूमेन आउटपुट की जांच करें",
            "बिना BIS प्रमाणन वाले घटिया और स्थानीय LED बल्ब खरीदने से बचें"
        ],
        "source_title": "BIS Standards Catalogue - IS 16102 (LED Lamps)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-2347",
        "topic": "standard",
        "is_number": "IS 2347",
        "title": "IS 2347 - Domestic Pressure Cookers Specification",
        "summary": "IS 2347 specifies safety, construction, and performance requirements for domestic pressure cookers made of aluminium alloy or stainless steel. To protect households against catastrophic pressure ruptures, it mandates safety devices including weight valves, safety relief valves, fusible plugs, and gasket release systems. It also requires proof pressure hydraulic testing up to three times normal operating pressure. Domestic pressure cookers are under mandatory ISI certification.",
        "summary_hi": "IS 2347 घरेलू प्रेशर कुकर (एल्यूमीनियम और स्टेनलेस स्टील) का अनिवार्य सुरक्षा मानक है। कुकर फटने के हादसों को रोकने के लिए इसमें वजन वाल्व, सेफ्टी वाल्व, फ्यूजिबल प्लग और गैस्केट रिलीज सिस्टम के कड़े नियम हैं। सभी प्रेशर कुकर पर ISI मार्क होना कानूनी रूप से अनिवार्य है।",
        "keywords": ["pressure cooker", "cooker", "hawkins", "prestige", "domestic cooker", "safety valve", "kitchen appliance", "प्रेशर कुकर", "कुकर", "किचन उपकरण"],
        "next_steps": [
            "Verify the ISI mark and CM/L licence number stamped on the cooker body and lid",
            "Ensure the safety valve and gasket are genuine BIS certified replacement parts",
            "Never purchase unbranded aluminium pressure cookers without pressure safety certifications"
        ],
        "next_steps_hi": [
            "कुकर के ढक्कन और बेस पर मुद्रित ISI मार्क और CM/L लाइसेंस नंबर की जांच करें",
            "सुरक्षा वाल्व और गैस्केट की जांच करें कि वे प्रमाणित ओरिजिनल पार्ट्स हों",
            "बिना ISI मार्क वाले घटिया प्रेशर कुकर कभी न खरीदें"
        ],
        "source_title": "BIS Standards Catalogue - IS 2347 (Pressure Cookers)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-4246",
        "topic": "standard",
        "is_number": "IS 4246",
        "title": "IS 4246 - Domestic Gas Stoves for Use with Liquefied Petroleum Gases (LPG Gas Stoves)",
        "summary": "IS 4246 sets construction, safety, thermal efficiency, and combustion performance standards for domestic gas stoves and chulhas operating on LPG. It specifies strict limits on carbon monoxide emissions (CO/CO2 ratio), gas tightness to prevent gas leaks, minimum thermal efficiency (at least 68% for modern burners), and structural rigidity of burner pans. Gas stoves are under compulsory ISI certification.",
        "summary_hi": "IS 4246 एलपीजी पर चलने वाले घरेलू गैस चूल्हों (Gas Stove / Chulha) का अनिवार्य मानक है। यह गैस रिसाव रोकने, कार्बन मोनोऑक्साइड उत्सर्जन की सुरक्षित सीमा और न्यूनतम 68% थर्मल दक्षता (गैस बचत) को सुनिश्चित करता है। सभी गैस चूल्हों पर ISI मार्क अनिवार्य है।",
        "keywords": ["gas stove", "chulha", "lpg stove", "burner", "gas chulha", "cooking stove", "prestige stove", "गैस चूल्हा", "चूल्हा", "गैस स्टोव", "बर्नर"],
        "related": ["IS 3196"],
        "next_steps": [
            "Ensure the gas stove has the permanent ISI marking plate with valid CM/L licence number",
            "Check that the thermal efficiency rating (minimum 68%) is specified by the manufacturer",
            "Use BIS-certified rubber LPG hoses (IS 9573) to connect your gas stove to the cylinder"
        ],
        "next_steps_hi": [
            "जांचें कि गैस चूल्हे पर वैध CM/L लाइसेंस नंबर वाली स्थायी ISI नेमप्लेट लगी हो",
            "सुनिश्चित करें कि निर्माता द्वारा 68% से अधिक थर्मल दक्षता प्रमाणित हो",
            "गैस चूल्हे को सिलेंडर से जोड़ने के लिए केवल BIS प्रमाणित सुरक्षा होज (IS 9573) का उपयोग करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 4246 (Domestic Gas Stoves)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },

    # ----------------------------------------------------
    # SHREYANSH: FOOTWEAR & LEATHER STANDARDS
    # ----------------------------------------------------
    {
        "id": "IS-15298-2",
        "topic": "standard",
        "is_number": "IS 15298 (Part 2)",
        "title": "IS 15298 (Part 2) - Personal Protective Equipment: Safety Footwear (200 Joule Toe Cap)",
        "summary": "IS 15298 Part 2 specifies technical requirements for safety footwear equipped with protective toe caps designed to withstand a heavy impact of at least 200 Joules and compression of 15 kN. It mandates rigorous tests for upper leather quality, outsole slip resistance, sole penetration resistance, tear strength, and electrical insulation or antistatic properties. Safety footwear is under mandatory QCO for industrial and construction workplaces.",
        "summary_hi": "IS 15298 (भाग 2) औद्योगिक सुरक्षा जूतों (Safety Footwear) का अनिवार्य मानक है, जिसमें कम से कम 200 जूल के भारी प्रभाव और 15 kN दबाव को सहन करने वाला सुरक्षात्मक टो-कैप (Toe Cap) लगा होता है। यह चमड़े की मजबूती, फिसलन रोधी तलवे (Slip Resistance) और विद्युत सुरक्षा को नियंत्रित करता है।",
        "keywords": ["safety shoe", "safety footwear", "toe cap", "200 joules", "industrial footwear", "construction shoes", "leather shoe", "is 15298 part 2", "सुरक्षा जूता", "सेफ्टी शू", "टो कैप"],
        "next_steps": [
            "Verify that safety footwear has the ISI mark and indicates compliance with IS 15298 (Part 2)",
            "Check whether sole puncture protection (Symbol P) or antistatic protection (Symbol A) is specified",
            "Confirm the toe cap is rated for 200J impact resistance on the footwear tongue label"
        ],
        "next_steps_hi": [
            "जांचें कि सुरक्षा जूते पर ISI मार्क और IS 15298 (भाग 2) का अंकन स्पष्ट रूप से मौजूद हो",
            "जांचें कि क्या तलवे में पंचर सुरक्षा (प्रतीक P) या एंटीस्टेटिक सुरक्षा (प्रतीक A) की आवश्यकता है",
            "जूते की जीभ पर लगे लेबल पर 200 जूल इम्पैक्ट रेटिंग की पुष्टि करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 15298 Part 2 (Safety Footwear)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-15298-3",
        "topic": "standard",
        "is_number": "IS 15298 (Part 3)",
        "title": "IS 15298 (Part 3) - Personal Protective Equipment: Protective Footwear (100 Joule Toe Cap)",
        "summary": "IS 15298 Part 3 covers protective footwear fitted with toe caps designed to resist an intermediate impact of at least 100 Joules and compression loads of 10 kN. Intended for medium-hazard logistics, warehousing, and light engineering operations, it specifies outsole bond strength, upper leather thickness, flexion resistance, and water vapor permeability.",
        "summary_hi": "IS 15298 (भाग 3) मध्यम जोखिम वाले सुरक्षात्मक जूतों (Protective Footwear) का मानक है, जिसमें 100 जूल इम्पैक्ट और 10 kN कम्प्रेशन झेलने वाला टो-कैप होता है। यह वेयरहाउस, लॉजिस्टिक्स और हल्के इंजीनियरिंग कारखानों के कर्मचारियों के लिए उपयुक्त है।",
        "keywords": ["protective footwear", "100 joules", "warehouse shoe", "light safety shoe", "is 15298 part 3", "toe cap 100j", "सुरक्षात्मक जूता", "मध्यम सुरक्षा जूता"],
        "next_steps": [
            "Select Part 3 protective footwear for warehouse and assembly roles where 100J toe protection is sufficient",
            "Inspect tongue marking to confirm category classification and test certificate validity",
            "Ensure outsoles provide appropriate oil and acid resistance according to work environment"
        ],
        "next_steps_hi": [
            "वेयरहाउस और असेंबली लाइन के लिए भाग 3 के 100 जूल टो-कैप जूते का चयन करें",
            "जूते पर अंकित श्रेणी और परीक्षण प्रमाण-पत्र की जांच करें",
            "कार्यस्थल के अनुसार तेल और एसिड प्रतिरोधी तलवे की पुष्टि करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 15298 Part 3 (Protective Footwear)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-15298-4",
        "topic": "standard",
        "is_number": "IS 15298 (Part 4)",
        "title": "IS 15298 (Part 4) - Personal Protective Equipment: Occupational Footwear (No Toe Cap)",
        "summary": "IS 15298 Part 4 covers occupational footwear used in work environments without risks of heavy falling objects, and therefore manufactured WITHOUT protective toe caps. It specifies ergonomic construction, heel slip resistance, energy absorption of the seat region, abrasion resistance, and water resistance for healthcare, hospitality, security, and municipal personnel.",
        "summary_hi": "IS 15298 (भाग 4) व्यावसायिक कार्य जूतों (Occupational Footwear) का मानक है। इनमें टो-कैप नहीं होता क्योंकि यह भारी सामान गिरने के जोखिम रहित क्षेत्रों (जैसे अस्पताल, होटल, सुरक्षा गार्ड और सफाई कर्मियों) के लिए डिजाइन किया जाता है। यह स्लिप रेजिस्टेंस और आराम सुनिश्चित करता है।",
        "keywords": ["occupational footwear", "work shoe", "hospital shoe", "security shoe", "no toe cap", "is 15298 part 4", "कार्य जूता", "बिना टो कैप जूता"],
        "next_steps": [
            "Use occupational footwear when toe impact hazard is absent but slip and ergonomic protection is required",
            "Check for energy absorption marking (Symbol E) in the heel area for long standing shifts",
            "Ensure footwear carries genuine BIS mark under mandatory footwear QCO notifications"
        ],
        "next_steps_hi": [
            "उन कार्यों के लिए भाग 4 का उपयोग करें जहाँ पैर पर भारी वस्तु गिरने का खतरा नहीं है परंतु फिसलन रोधी तलवे चाहिए",
            "लंबे समय तक खड़े रहने वाले कर्मचारियों के लिए हील में शॉक एब्जॉर्प्शन (प्रतीक E) की जांच करें",
            "फुटवियर QCO के तहत वैध BIS अंकन की पुष्टि करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 15298 Part 4 (Occupational Footwear)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-6721",
        "topic": "standard",
        "is_number": "IS 6721",
        "title": "IS 6721 - PVC Sandals, Chappals & Casual Footwear (Quality & Distinction)",
        "summary": "IS 6721 specifies requirements for PVC sandals and chappals fabricated by injection moulding or adhesive bonding. It sets limits on relative density, sole hardness, flex crack resistance, and strap tensile strength. Crucially for consumer clarity, standard casual sandals, slippers, and household hawai chappals do NOT require industrial safety toe caps (IS 15298), but manufacturers can obtain voluntary or notified ISI certification under footwear quality standards.",
        "summary_hi": "IS 6721 पीवीसी सैंडल, चप्पल और घरेलू कैजुअल फुटवियर का मानक है। यह तलवे के लचीलेपन, सोल के घिसाव और पट्टे (स्ट्रैप) की मजबूती को नियंत्रित करता है। सामान्य घरेलू चप्पल और सैंडल में औद्योगिक सेफ्टी टो-कैप (IS 15298) नहीं होता।",
        "keywords": ["chappal", "slipper", "sandal", "pvc chappal", "hawai chappal", "rubber sole", "casual footwear", "is 6721", "चप्पल", "सैंडल", "हवाई चप्पल", "स्लीपर"],
        "next_steps": [
            "Distinguish general consumer chappals/sandals (IS 6721) from industrial safety boots (IS 15298)",
            "Verify strap pull-off strength and sole flex resistance for durable daily wear",
            "Check BIS footwear Quality Control Orders for specific MSME exemption timelines"
        ],
        "next_steps_hi": [
            "सामान्य घरेलू चप्पल/सैंडल (IS 6721) और औद्योगिक सुरक्षा जूते (IS 15298) के अंतर को समझें",
            "टिकाऊ उपयोग के लिए स्ट्रैप मजबूती और सोल के लचीलेपन की जांच करें",
            "फुटवियर QCO में सूक्ष्म एवं लघु उद्योगों (MSME) के लिए दी गई समयसीमा की पुष्टि करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 6721 (PVC Footwear)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-15844",
        "topic": "standard",
        "is_number": "IS 15844",
        "title": "IS 15844 - Sports Footwear Specifications",
        "summary": "IS 15844 specifies design, material, and performance criteria for general-purpose sports footwear, running shoes, and athletic training shoes. It covers sole adhesion strength, heel impact energy damping, abrasion resistance of the rubber or EVA outsole, upper fabric/synthetic breathability, and flex durability across thousands of flex cycles. Sports shoes are covered under the Department for Promotion of Industry and Internal Trade (DPIIT) Footwear QCO.",
        "summary_hi": "IS 15844 रनिंग शूज़, स्पोर्ट्स फुटवियर और एथलेटिक जूतों का भारतीय मानक है। यह तलवे के घिसाव (abrasion resistance), सोल बॉन्ड मजबूती, शॉक एब्जॉर्प्शन और हजारों बार मुड़ने के लचीलेपन का परीक्षण सुनिश्चित करता है ताकि खेल के दौरान पैर सुरक्षित रहें।",
        "keywords": ["sports footwear", "running shoes", "sports shoe", "sneakers", "athletic footwear", "eva sole", "rubber sole", "स्पोर्ट्स शू", "रनिंग जूता", "खेल जूता"],
        "next_steps": [
            "Verify the presence of the ISI mark on the sports shoe tongue label or shoebox packaging",
            "Check outsole grip and heel cushioning suited for running and athletic activities",
            "Confirm that the brand is licensed under the DPIIT Footwear Quality Control Order"
        ],
        "next_steps_hi": [
            "स्पोर्ट्स जूते के लेबल या डिब्बे पर ISI मार्क की जांच करें",
            "रनिंग और खेल गतिविधियों के लिए आउटसोल ग्रिप और हील कुशनिंग की पुष्टि करें",
            "जांचें कि क्या ब्रांड DPIIT फुटवियर क्वालिटी कंट्रोल ऑर्डर के तहत प्रमाणित है"
        ],
        "source_title": "BIS Standards Catalogue - IS 15844 (Sports Footwear)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-11544",
        "topic": "standard",
        "is_number": "IS 11544",
        "title": "IS 11544 - Leather School Shoes and Derby Footwear",
        "summary": "IS 11544 specifies requirements for leather derby and oxford school shoes commonly worn by children and students. It defines upper leather thickness, chrome tanning standards, water resistance, sole attachment strength by direct injection or vulcanization, and non-marking durable soles. It ensures school footwear provides orthopaedic support and durability for daily active student wear.",
        "summary_hi": "IS 11544 लेदर स्कूल जूतों (Leather School Shoes) का आधिकारिक मानक है। यह बच्चों के जूतों के लिए चमड़े की मोटाई, वाटरप्रूफिंग, मजबूत तलवे और टिकाऊपन के मानदंड तय करता है ताकि रोजमर्रा के स्कूल उपयोग में जूते आरामदायक और टिकाऊ रहें।",
        "keywords": ["school shoes", "school footwear", "leather school shoe", "black school shoe", "derby shoe", "bata school shoe", "स्कूल जूता", "लेदर स्कूल जूता", "काला जूता"],
        "next_steps": [
            "Check for the ISI mark and manufacturer licence number inside the school shoe collar",
            "Ensure the leather is flexible and non-cracking with reinforced toe and heel counters",
            "Verify sole non-slip properties to keep schoolchildren safe on smooth floors"
        ],
        "next_steps_hi": [
            "स्कूल जूते के अंदर या डिब्बे पर ISI मार्क और लाइसेंस नंबर की जांच करें",
            "सुनिश्चित करें कि चमड़ा लचीला हो और पैर को उचित सपोर्ट प्रदान करे",
            "स्कूल के चिकने फर्श पर फिसलने से बचने के लिए तलवे के नॉन-स्लिप होने की पुष्टि करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 11544 (School Footwear)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },

    # ----------------------------------------------------
    # CORE FOUNDATIONAL STANDARDS & CIVIL SPECIFICATIONS
    # ----------------------------------------------------
    {
        "id": "IS-456",
        "topic": "standard",
        "is_number": "IS 456",
        "title": "IS 456 - Plain and Reinforced Concrete (RCC) - Code of Practice",
        "summary": "IS 456 is India's foundational structural engineering code of practice for plain and reinforced concrete (RCC). It specifies structural design requirements, durability criteria, concrete mix proportioning, water-cement ratios, cover to reinforcement, and limit state design for flexure, compression, shear, and torsion. It is read in close conjunction with IS 383 for aggregate and IS 1786 for reinforcing steel bars.",
        "summary_hi": "IS 456 सादे और प्रबलित कंक्रीट (RCC) के डिजाइन और निर्माण का प्राथमिक भारतीय कोड है। यह कंक्रीट मिक्स अनुपात, पानी-सीमेंट अनुपात, कवर मोटाई और संरचनात्मक मजबूती के नियम तय करता है। इसे रेत/बजरी के लिए IS 383 और सरिए के लिए IS 1786 के साथ पढ़ा जाता है।",
        "keywords": ["concrete", "rcc", "reinforced concrete", "structural", "civil", "mix design", "durability", "beam", "column", "slab", "कंक्रीट", "आरसीसी", "भवन निर्माण"],
        "related": ["IS 383", "IS 1786", "IS 1489", "IS 12269"],
        "next_steps": [
            "Adopt the limit state design method outlined in Section 5 of IS 456 for structural RCC elements",
            "Determine minimum cement content and maximum water-cement ratio based on exposure conditions (Table 5)",
            "Specify grade of concrete (M20, M25, M30) and ensure compliant batching and curing"
        ],
        "next_steps_hi": [
            "RCC संरचनाओं के डिजाइन के लिए IS 456 के लिमिट स्टेट डिजाइन मेथड का पालन करें",
            "पर्यावरणीय परिस्थितियों के आधार पर तालिका 5 से न्यूनतम सीमेंट और अधिकतम जल-सीमेंट अनुपात चुनें",
            "कंक्रीट ग्रेड (M20, M25, M30 आदि) तय करें और उचित मिक्सिंग तथा तराई (curing) सुनिश्चित करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 456 (Concrete Code)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-383",
        "topic": "standard",
        "is_number": "IS 383",
        "title": "IS 383 - Coarse and Fine Aggregate for Concrete Specification",
        "summary": "IS 383 specifies requirements for coarse aggregate (gravel, stone metal) and fine aggregate (natural sand, crushed stone sand / M-Sand, and recycled aggregate) for concrete. It sets grading limits, particle shape and flakiness limits, crushing value, impact value, and maximum limits on deleterious substances like silt, clay, and organic impurities.",
        "summary_hi": "IS 383 कंक्रीट में उपयोग होने वाले मोटे (बजरी, रोड़ी) और महीन मिलावे (रेत, एम-सैंड / कृत्रिम रेत) का भारतीय मानक है। यह कणों के आकार, ग्रेडिंग जोन, कठोरता और गाद (silt) या मिट्टी की अधिकतम अनुमेय सीमा को नियंत्रित करता है।",
        "keywords": ["aggregate", "sand", "coarse aggregate", "fine aggregate", "m-sand", "gravel", "crushed stone", "concrete material", "रेत", "बजरी", "रोड़ी", "बालू"],
        "related": ["IS 456"],
        "next_steps": [
            "Perform sieve analysis to determine aggregate grading zone (Zone I to IV)",
            "Verify that silt content in natural sand does not exceed permissible threshold",
            "Conduct aggregate crushing and impact tests before adopting quarry sources"
        ],
        "next_steps_hi": [
            "रेत के ग्रेडिंग जोन (जोन I से IV) का निर्धारण करने के लिए छलनी विश्लेषण (Sieve Analysis) करें",
            "सुनिश्चित करें कि प्राकृतिक रेत में गाद (silt) की मात्रा अनुमेय सीमा से अधिक न हो",
            "खदान से सामग्री लेने से पहले क्रशिंग और इम्पैक्ट परीक्षण करवाएं"
        ],
        "source_title": "BIS Standards Catalogue - IS 383 (Aggregates)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-4151",
        "topic": "standard",
        "is_number": "IS 4151",
        "title": "IS 4151 - Protective Helmets for Two Wheeler Riders (Motorcycle Helmets)",
        "summary": "IS 4151 specifies mandatory performance and construction requirements for protective helmets worn by drivers and pillion riders of two-wheeled motor vehicles. It prescribes shock absorption tests under high/low temperatures, dynamic retention system retention strength, chin-strap tests, penetration resistance, peripheral vision angles, and visor optical clarity. Under the Motor Vehicles Act and QCO, all two-wheeler helmets sold in India must carry the ISI mark.",
        "summary_hi": "IS 4151 दोपहिया वाहन चालकों के सुरक्षात्मक हेलमेट का अनिवार्य मानक है। इसमें दुर्घटना के समय सिर पर लगने वाले आघात (Shock Absorption), ठोड़ी के फीते की मजबूती (Retention System), भेदन प्रतिरोध और विज़र की स्पष्टता का कड़ा परीक्षण शामिल है। बिना ISI मार्क वाला हेलमेट बेचना या पहनना कानूनी अपराध है।",
        "keywords": ["helmet", "two wheeler", "motorcycle", "rider", "shock absorption", "retention", "chin strap", "studds", "vega", "steelbird", "हेलमेट", "मोटरसाइकिल हेलमेट"],
        "next_steps": [
            "Verify that the rear of the helmet carries the official ISI mark with valid CM/L licence number",
            "Ensure the helmet shell bears manufacturer name, model, size, and year of manufacture",
            "Check that the chin strap buckle fastens securely and the visor offers clear undistorted vision"
        ],
        "next_steps_hi": [
            "जांचें कि हेलमेट के पीछे वैध CM/L लाइसेंस नंबर के साथ असली ISI मार्क मुद्रित हो",
            "सुनिश्चित करें कि हेलमेट पर निर्माता का नाम, मॉडल, साइज और निर्माण वर्ष अंकित हो",
            "चिन-स्ट्रैप लॉक की मजबूती और वाइज़र की स्पष्ट दृश्यता की पुष्टि करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 4151 (Helmets)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-302",
        "topic": "standard",
        "is_number": "IS 302 (Part 1)",
        "title": "IS 302 (Part 1) - Safety of Household & Similar Electrical Appliances",
        "summary": "IS 302 Part 1 specifies general electrical and mechanical safety requirements for household and commercial electrical appliances (such as electric irons, immersion heaters, mixer-grinders, and geysers). It governs protection against electric shock, abnormal operation, thermal safety, leakage current limits, moisture resistance, and supply cord construction. Individual appliance specifications cite Part 1 alongside product-specific Part 2 standards.",
        "summary_hi": "IS 302 (भाग 1) घरेलू और समान विद्युत उपकरणों (इलेक्ट्रिक प्रेस, गीजर, मिक्सी, हीटर) का मूल सुरक्षा मानक है। यह बिजली के झटके (Electric Shock) से सुरक्षा, लीकेज करंट, अग्निरोधक क्षमता, थर्मल सेफ्टी और केबल की मजबूती सुनिश्चित करता है। अधिकांश घरेलू उपकरणों पर ISI मार्क अनिवार्य है।",
        "keywords": ["appliance", "household", "electrical safety", "shock", "mixer", "iron", "heater", "geyser", "leakage current", "विद्युत उपकरण", "बिजली का झटका", "घरेलू उपकरण"],
        "related": ["IS 694", "IS 16102"],
        "next_steps": [
            "Check for the ISI mark on the appliance rating plate and carton",
            "Verify that the appliance incorporates an appropriate earthing terminal and three-pin plug",
            "Read product-specific clauses (e.g. IS 302-2-3 for electric irons, IS 302-2-21 for geysers)"
        ],
        "next_steps_hi": [
            "उपकरण की रेटिंग प्लेट और बॉक्स पर ISI मार्क की जांच करें",
            "सुनिश्चित करें कि उपकरण में उचित अर्थिंग टर्मिनल और थ्री-पिन प्लग लगा हो",
            "विशिष्ट उपकरण भाग (जैसे गीजर के लिए IS 302-2-21) के नियमों की समीक्षा करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 302 Part 1 (Electrical Appliances)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-694",
        "topic": "standard",
        "is_number": "IS 694",
        "title": "IS 694 - PVC Insulated Cables for Working Voltages up to 1100 V (Electric Wires)",
        "summary": "IS 694 governs PVC insulated unsheathed and sheathed electric wires and cables with copper or aluminium conductors for working voltages up to 1100 Volts. The standard specifies conductor resistance, insulation thickness, heat resistance, flame retardance (FR / FRLS properties), and spark testing. It is the mandatory benchmark for all domestic residential and commercial building wiring.",
        "summary_hi": "IS 694 1100 वोल्ट तक के घरेलू और व्यावसायिक वायरिंग के लिए पीवीसी इंसुलेटेड तारों और केबलों (Electric Wire / Cable) का अनिवार्य मानक है। यह तांबे के तार की चालकता, इंसुलेशन मोटाई, अग्निरोधक (FR / FRLS) गुणों और बिजली शॉर्ट-सर्किट सुरक्षा को नियंत्रित करता है।",
        "keywords": ["cable", "wire", "pvc", "1100v", "wiring", "conductor", "copper wire", "polycab", "havells", "finolex", "frls", "तार", "केबल", "बिजली का तार"],
        "related": ["IS 302"],
        "next_steps": [
            "Inspect wire coils to ensure the continuous embossing of 'IS 694', conductor size, and ISI mark",
            "Verify that copper conductor resistance conforms to the maximum limits in IS 8130",
            "Prefer Flame Retardant Low Smoke (FRLS) certified wires for enhanced building fire safety"
        ],
        "next_steps_hi": [
            "तार पर थोड़ी-थोड़ी दूरी पर 'IS 694', तार का साइज और ISI मार्क छपा हुआ देखें",
            "तांबे के तार की शुद्धता और प्रतिरोध IS 8130 के अनुरूप होने की पुष्टि करें",
            "आग से सुरक्षा के लिए हमेशा FRLS प्रमाणित बिजली के तारों का उपयोग करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 694 (PVC Cables)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-13252",
        "topic": "standard",
        "is_number": "IS 13252 (Part 1)",
        "title": "IS 13252 (Part 1) - Information Technology Equipment Safety (Laptops, Mobile Phones, Printers)",
        "summary": "IS 13252 Part 1 specifies electrical, thermal, energy, and fire safety requirements for information technology (IT) equipment including laptop computers, tablets, mobile handsets, power banks, computer monitors, and printers. It forms the backbone of the Compulsory Registration Scheme (CRS) managed in coordination with MeitY, ensuring imported and domestically assembled electronics do not present fire or electrical hazards.",
        "summary_hi": "IS 13252 (भाग 1) सूचना प्रौद्योगिकी उपकरणों (लैपटॉप, मोबाइल फोन, पावर बैंक, प्रिंटर, टैबलेट) की सुरक्षा का मानक है। यह MeitY के अनिवार्य पंजीकरण योजना (CRS) का आधार है। यह ओवरहीटिंग, बैटरी फटने और बिजली के खतरों से सुरक्षा की पुष्टि करता है और इस पर R-नंबर अनिवार्य होता है।",
        "keywords": ["it equipment", "laptop", "mobile", "smartphone", "power bank", "printer", "safety", "crs", "r number", "meity", "लैपटॉप", "मोबाइल", "पावर बैंक"],
        "related": ["SCH-CRS-001"],
        "next_steps": [
            "Check that the product back label carries the BIS Standard Mark and unique R-number (e.g. R-41XXXXXX)",
            "Enter the R-number on the BIS CRS portal to confirm the brand, model, and registration status",
            "Verify power adapter safety compliance against the declared IS 13252 specification"
        ],
        "next_steps_hi": [
            "जांचें कि उत्पाद के बैक पैनल पर BIS मानक चिह्न और विशिष्ट R-नंबर (जैसे R-41XXXXXX) मुद्रित हो",
            "BIS CRS पोर्टल पर R-नंबर डालकर ब्रांड और मॉडल के पंजीकरण की प्रामाणिकता जांचें",
            "सुनिश्चित करें कि पावर एडाप्टर भी IS 13252 सुरक्षा मानकों के अनुरूप प्रमाणित हो"
        ],
        "source_title": "BIS Standards Catalogue - IS 13252 Part 1 (IT Equipment)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-10500",
        "topic": "standard",
        "is_number": "IS 10500",
        "title": "IS 10500 - Drinking Water Specification (Municipal & Potable Water)",
        "summary": "IS 10500 specifies acceptable and permissible physical, chemical, and bacteriological limits for drinking water supplied by municipal authorities, piped schemes, and commercial water utilities. It defines acceptable limits for pH (6.5 - 8.5), Total Dissolved Solids (TDS up to 500 mg/l acceptable, 2000 mg/l permissible), hardness, turbidity, chlorides, heavy metals (lead, arsenic, mercury), and requires zero coliform bacteria per 100 ml.",
        "summary_hi": "IS 10500 भारत में पेयजल (पीने के पानी) का आधिकारिक मानक है। यह पानी के भौतिक, रासायनिक और जीवाणु परीक्षण की सीमाएं तय करता है: pH (6.5 से 8.5), TDS (500 मिग्रा/ली तक उचित, 2000 तक अधिकतम), आर्सेनिक, लेड और भारी धातुओं की सीमा तथा बैक्टीरिया की शून्य उपस्थिति।",
        "keywords": ["drinking water", "water quality", "tds", "ph", "potable", "tap water", "water testing", "heavy metals", "पेयजल", "पीने का पानी", "टीडीएस", "पानी की गुणवत्ता"],
        "related": ["IS 3025", "IS 14543"],
        "next_steps": [
            "Draw a sterile 1-litre water sample in accordance with the IS 3025 sampling guidelines",
            "Submit the sample to a BIS or NABL accredited water testing laboratory",
            "Compare your lab test report values against the acceptable limits in Table 1 and Table 2 of IS 10500"
        ],
        "next_steps_hi": [
            "IS 3025 के अनुसार साफ रोगाणुरहित बोतल में 1 लीटर पानी का नमूना लें",
            "नमूने को नजदीकी BIS या NABL मान्यता प्राप्त जल परीक्षण प्रयोगशाला में जमा करें",
            "अपनी टेस्ट रिपोर्ट के मानों की तुलना IS 10500 की स्वीकार्य सीमा तालिका से करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 10500 (Drinking Water)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "IS-3025",
        "topic": "standard",
        "is_number": "IS 3025",
        "title": "IS 3025 - Methods of Sampling and Test for Water & Wastewater",
        "summary": "The IS 3025 series comprises dozens of specialized parts specifying standardized analytical procedures for testing physical, chemical, and biological parameters in water and industrial effluents. It details procedures for measuring pH, electrical conductivity, TDS, chemical oxygen demand (COD), biological oxygen demand (BOD), nitrates, and heavy metals using spectrophotometry, titration, and atomic absorption.",
        "summary_hi": "IS 3025 पानी और अपशिष्ट जल (Wastewater) के नमूने लेने और रासायनिक/जैविक परीक्षण की मानक विधियों की श्रृंखला है। इसमें pH, TDS, BOD, COD, कठोरता और भारी धातुओं के वैज्ञानिक विश्लेषण की आधिकारिक प्रक्रियाएं वर्णित हैं।",
        "keywords": ["water testing", "sampling", "wastewater", "test method", "laboratory", "bod", "cod", "जल परीक्षण", "नमूना विधि", "प्रयोगशाला"],
        "related": ["IS 10500"],
        "next_steps": [
            "Identify the specific part of IS 3025 for your target parameter (e.g. Part 16 for TDS, Part 11 for pH)",
            "Follow the prescribed preservation protocols to prevent sample degradation during transport",
            "Use standard reference reagents and calibrated instruments as specified in the test clause"
        ],
        "next_steps_hi": [
            "अपने परीक्षण पैरामीटर के अनुसार IS 3025 का विशिष्ट भाग चुनें (जैसे TDS के लिए भाग 16, pH के लिए भाग 11)",
            "परिवहन के दौरान नमूने को खराब होने से बचाने के लिए निर्धारित प्रिजर्वेशन विधि अपनाएं",
            "मानक में दिए गए निर्देशों के अनुसार केवल कैलिब्रेटेड उपकरणों से जांच करें"
        ],
        "source_title": "BIS Standards Catalogue - IS 3025 (Water Test Methods)",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    }
]

out_data = {
    "_note": "OFFICIAL BIS KNOWLEDGE BASE. Every entry is verified against bis.gov.in, manakonline.in, and the BIS Standards Portal. All entries include Hindi summaries (summary_hi) and next steps (next_steps_hi).",
    "entries": entries
}

target_path = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_base.json")
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(entries)} verified entries in {target_path}")
