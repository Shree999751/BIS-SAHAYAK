"""
Script to expand BIS knowledge_base.json with 25 new production-grade entries.
Covers civil, electrical, fire safety, consumer goods, hallmarking, automotive,
medical devices, solar energy, food/water standards, and QCO legal mandates.
"""
import json
import os
import sys

DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "knowledge_base.json",
)

NEW_ENTRIES = [
    {
        "id": "STD-FIRE-EXT-001",
        "topic": "standard",
        "is_number": "IS 15683",
        "title": "IS 15683 - Portable Fire Extinguishers Performance and Construction",
        "title_hi": "IS 15683 - वहनीय अग्निशामक यंत्र (पोर्टेबल फायर एक्सटिंग्विशर) विनिर्देश",
        "summary": "IS 15683 governs the construction, performance, and testing of portable fire extinguishers in India (Water, Foam, Dry Powder, Carbon Dioxide CO2, and Clean Agent). Mandatory ISI certification is required under the Fire Extinguishers Quality Control Order (QCO). Extinguishers must withstand hydrostatic pressure burst tests, discharge duration tests, and fire rating tests (Class A, B, C, D, F).",
        "summary_hi": "IS 15683 भारत में पोर्टेबल अग्निशामक यंत्रों (फायर एक्सटिंग्विशर - पानी, फोम, सूखा पाउडर, CO2 और क्लीन एजेंट) के निर्माण और परीक्षण को नियंत्रित करता है। अग्नि सुरक्षा QCO के तहत ISI मार्क अनिवार्य है। इसमें हाइड्रोस्टैटिक दबाव परीक्षण, डिस्चार्ज अवधि और विभिन्न अग्नि श्रेणियों (A, B, C, D, F) की रेटिंग अनिवार्य है।",
        "keywords": [
            "fire extinguisher", "fire safety", "is 15683", "co2 cylinder", "dry powder",
            "foam extinguisher", "fire cylinder", "portable extinguisher", "isi fire extinguisher",
            "अग्निशामक", "फायर एक्सटिंग्विशर", "आग बुझाने का सिलेंडर", "अग्नि सुरक्षा", "आईएस 15683"
        ],
        "next_steps": [
            "Obtain BIS Product Certification Scheme-I licence with factory hydrostatic testing facilities",
            "Ensure pressure gauge, discharge nozzle, and safety relief valve comply with SIT guidelines",
            "Apply online at manakonline.in for ISI mark licence under IS 15683",
            "Verify ISI mark and CM/L number on the cylinder body using BIS Care App"
        ],
        "next_steps_hi": [
            "कारखाने में हाइड्रोस्टैटिक प्रेशर टेस्टिंग लैब के साथ योजना-I लाइसेंस प्राप्त करें",
            "दबाव गेज और डिस्चार्ज नोजल का एसआईटी दिशानिर्देशों के अनुसार परीक्षण सुनिश्चित करें",
            "मानकॉनलाइन (manakonline.in) पोर्टल पर IS 15683 के तहत ISI मार्क हेतु आवेदन करें",
            "सिलेंडर पर मुद्रित ISI मार्क और सीएम/एल नंबर की बीआईएस केयर ऐप से जांच करें"
        ],
        "source_title": "BIS Indian Standard IS 15683 - Portable Fire Extinguishers",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-GOLD-HALLMARK-001",
        "topic": "hallmarking",
        "is_number": "IS 1417",
        "title": "IS 1417 - Gold and Gold Alloys, Jewellery/Artefacts - Fineness and Hallmarking",
        "title_hi": "IS 1417 - स्वर्ण आभूषण एवं कलाकृतियां - शुद्धता एवं हॉलमार्किंग विनिर्देश",
        "summary": "IS 1417 is the cornerstone standard governing gold purity, fineness grades, and mandatory hallmarking in India. Permissible karats are 14K (585), 18K (750), 20K (833), 22K (916), 23K (958), and 24K (995). Since 2021, hallmarking is compulsory across notified districts under Scheme-IV. A valid hallmark requires 3 marks: the BIS Triangular Logo, Karat & Fineness mark, and a unique 6-digit alphanumeric HUID.",
        "summary_hi": "IS 1417 भारत में सोने की शुद्धता (कैरेट/फाइननेस) और अनिवार्य हॉलमार्किंग का प्रमुख मानक है। इसमें 14K (585), 18K (750), 20K (833), 22K (916), 23K (958) और 24K (995) शुद्धता शामिल है। अधिसूचित जिलों में योजना-IV के तहत हॉलमार्किंग अनिवार्य है। इसमें बीआईएस त्रिकोण चिह्न, शुद्धता और 6 अंकों का यूनिक HUID कोड शामिल होता है।",
        "keywords": [
            "gold hallmark", "is 1417", "22k 916", "18k 750", "huid", "gold jewellery",
            "gold purity", "bis hallmark gold", "sona hallmark", "hallmarked gold",
            "सोना हॉलमार्क", "आईएस 1417", "916 सोना", "22 कैरेट सोना", "एचयूआईडी", "सोने की शुद्धता"
        ],
        "next_steps": [
            "Jewellers must register on manakonline.in for a hallmarking registration certificate",
            "Send gold articles to a BIS-recognized Assaying and Hallmarking Centre (AHC) for XRF & fire assay testing",
            "Consumers must verify the 6-digit HUID code using the 'Verify HUID' feature on the BIS Care App",
            "Always insist on an itemized invoice stating gross weight, net weight, karatage, and hallmarking charges"
        ],
        "next_steps_hi": [
            "ज्वैलर्स मानकॉनलाइन (manakonline.in) पर हॉलमार्किंग पंजीकरण प्रमाण पत्र प्राप्त करें",
            "सोने के आभूषणों को परीक्षण और लेजर मार्किंग हेतु बीआईएस मान्यता प्राप्त एएचसी (AHC) केंद्र भेजें",
            "उपभोक्ता बीआईएस केयर ऐप में 'Verify HUID' विकल्प से 6 अंकों के कोड का सत्यापन करें",
            "हमेशा बिल में सकल वजन, शुद्ध वजन, कैरेट शुद्धता और हॉलमार्किंग शुल्क का उल्लेख करवाएं"
        ],
        "source_title": "BIS Hallmarking Scheme - IS 1417 Gold Specifications",
        "source_url": "https://www.bis.gov.in/hallmarking-overview/",
        "verified": True
    },
    {
        "id": "STD-SILVER-HALLMARK-001",
        "topic": "hallmarking",
        "is_number": "IS 2112",
        "title": "IS 2112 - Silver and Silver Alloys, Jewellery/Artefacts - Hallmarking",
        "title_hi": "IS 2112 - चांदी के आभूषण एवं बर्तन - शुद्धता एवं हॉलमार्किंग विनिर्देश",
        "summary": "IS 2112 specifies purity requirements and hallmarking for silver jewellery, utensils, and artefacts in India. Recognized fineness grades include 999 (Fine Silver), 970, 925 (Sterling Silver), 900, 835, and 800 parts per thousand. Silver hallmarking is currently voluntary and features the BIS triangular mark, purity grade (e.g. 925), and the AHC center identification mark.",
        "summary_hi": "IS 2112 भारत में चांदी के आभूषणों, बर्तनों और सिक्कों की शुद्धता और हॉलमार्किंग को परिभाषित करता है। इसमें 999 (फाइन सिल्वर), 970, 925 (स्टर्लिंग सिल्वर), 900, 835 और 800 शुद्धता स्तर मान्यता प्राप्त हैं। चांदी पर हॉलमार्किंग स्वैच्छिक है और इसमें बीआईएस त्रिकोण चिह्न, शुद्धता ग्रेड (जैसे 925) और केंद्र का चिह्न होता है।",
        "keywords": [
            "silver hallmark", "is 2112", "sterling silver 925", "chandi hallmark", "silver jewellery",
            "silver utensils", "999 silver", "chandi ke bartan", "चांदी हॉलमार्क", "आईएस 2112", "925 चांदी"
        ],
        "next_steps": [
            "Verify silver purity grade stamped on the article (e.g., 925 for sterling silver)",
            "Jewellers can get silver artefacts certified at BIS recognized Assaying & Hallmarking Centres",
            "Check jeweller registration status on the official BIS portal",
            "Request hallmarking verification details on tax invoices"
        ],
        "next_steps_hi": [
            "चांदी के बर्तन या आभूषण पर मुद्रित शुद्धता ग्रेड (जैसे 925) की जांच करें",
            "ज्वैलर्स बीआईएस मान्यता प्राप्त एएचसी केंद्रों से चांदी का परीक्षण और प्रमाणन करवा सकते हैं",
            "आधिकारिक पोर्टल पर ज्वैलर के पंजीकरण का सत्यापन करें",
            "खरीद चालान (बिल) पर हॉलमार्क विवरण अवश्य दर्ज करवाएं"
        ],
        "source_title": "BIS Silver Hallmarking Scheme - IS 2112",
        "source_url": "https://www.bis.gov.in/hallmarking-overview/",
        "verified": True
    },
    {
        "id": "STD-STEEL-STRUCT-001",
        "topic": "standard",
        "is_number": "IS 2062",
        "title": "IS 2062 - Hot Rolled Medium and High Tensile Structural Steel",
        "title_hi": "IS 2062 - गर्म रोल्ड मध्यम एवं उच्च तन्यता संरचनात्मक स्टील (गर्डर, चैनल, एंगल)",
        "summary": "IS 2062 covers hot rolled structural steel sections (beams, channels, angles, joists, flats, and plates) widely used in bridges, heavy buildings, industrial sheds, and civil infrastructure. Grades include E250, E300, E350, E410, and E450 with sub-qualities (A, BR, B0, C) testing impact toughness at sub-zero temperatures. Mandatory ISI mark applies under the Ministry of Steel QCO.",
        "summary_hi": "IS 2062 गर्म रोल्ड संरचनात्मक स्टील (बीम, चैनल, एंगल, प्लेट, गर्डर) का मानक है, जिसका उपयोग पुलों, बहुमंजिला इमारतों और भारी निर्माण में होता है। इसमें E250, E300, E350, E410 और E450 ग्रेड शामिल हैं। इस्पात मंत्रालय के QCO के तहत संरचनात्मक स्टील पर अनिवार्य ISI मार्क होना आवश्यक है।",
        "keywords": [
            "is 2062", "structural steel", "steel beam", "steel angle", "girder", "channel",
            "e250 steel", "e350 steel", "heavy steel plates", "संरचनात्मक स्टील", "आईएस 2062", "गर्डर", "एंगल", "चैनल"
        ],
        "next_steps": [
            "Ensure raw billets and slabs meet chemical limits for Carbon, Sulphur, and Phosphorus",
            "Conduct tensile, bend, and Charpy V-notch impact tests as per SIT norms",
            "Apply on manakonline.in for Scheme-I certification under IS 2062",
            "Verify mill test certificates (MTC) and embossed ISI brand marks before structural fabrication"
        ],
        "next_steps_hi": [
            "कच्चे बिलेट और स्लैब में कार्बन, सल्फर और फॉस्फोरस की रासायनिक सीमा सुनिश्चित करें",
            "एसआईटी नियमों के अनुसार तन्यता, बेंड और चार्पी इम्पैक्ट परीक्षण करवाएं",
            "मानकॉनलाइन पोर्टल पर IS 2062 के अंतर्गत योजना-I लाइसेंस हेतु आवेदन करें",
            "संरचनात्मक निर्माण से पहले मिल टेस्ट सर्टिफिकेट (MTC) और उभरे हुए ISI मार्क की जांच करें"
        ],
        "source_title": "BIS Indian Standard IS 2062 - Structural Steel",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-PLYWOOD-001",
        "topic": "standard",
        "is_number": "IS 303",
        "title": "IS 303 - Plywood for General Purposes (MR and BWR Grades)",
        "title_hi": "IS 303 - सामान्य उपयोग हेतु प्लाईवुड (MR एवं BWR ग्रेड) विनिर्देश",
        "summary": "IS 303 specifies requirements for general-purpose plywood manufactured from timber veneers, bonded with synthetic resin adhesives. Covers two main grades: Moisture Resistant (MR Grade - commercial interior use) and Boiling Water Resistant (BWR Grade - exterior and moisture-prone areas). Mandatory ISI certification applies under the Plywood and Wooden Products Quality Control Order (QCO).",
        "summary_hi": "IS 303 सामान्य उपयोग के प्लाईवुड के विनिर्देश तय करता है। इसमें दो मुख्य ग्रेड शामिल हैं: मॉइस्चर रेजिस्टेंट (MR ग्रेड - आंतरिक उपयोग) और बॉयलिंग वाटर रेजिस्टेंट (BWR ग्रेड - बाहरी और नमी वाले स्थान)। प्लाईवुड QCO के तहत निर्माण और बिक्री हेतु अनिवार्य ISI मार्क आवश्यक है।",
        "keywords": [
            "is 303", "plywood", "mr grade plywood", "bwr plywood", "commercial ply", "timber board",
            "plywood qco", "plywood isi mark", "प्लाईवुड", "आईएस 303", "बी डब्ल्यू आर प्लाई", "लकड़ी बोर्ड"
        ],
        "next_steps": [
            "Equip manufacturing unit with moisture meter, glue adhesion test, and Mycological test apparatus",
            "Ensure thickness tolerance, density, and modulus of rupture meet IS 303 limits",
            "Submit licence application on manakonline.in under Scheme-I",
            "Inspect stamp on plywood sheet for ISI logo, CM/L licence number, and grade"
        ],
        "next_steps_hi": [
            "कारखाने में नमी मापक, ग्लू एडहेसन और पानी में उबालने के परीक्षण उपकरण स्थापित करें",
            "प्लाईवुड की मोटाई और मजबूती का IS 303 के अनुसार सत्यापन करें",
            "मानकॉनलाइन पोर्टल पर योजना-I के तहत आवेदन करें",
            "प्लाईवुड शीट पर मुद्रित ISI मार्क, सीएम/एल लाइसेंस नंबर और ग्रेड (MR/BWR) की जांच करें"
        ],
        "source_title": "BIS Indian Standard IS 303 - General Purpose Plywood",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-FAN-001",
        "topic": "standard",
        "is_number": "IS 374",
        "title": "IS 374 - Electric Ceiling Type Fans and Regulators",
        "title_hi": "IS 374 - इलेक्ट्रिक सीलिंग पंखे एवं रेगुलेटर विनिर्देश",
        "summary": "IS 374 covers AC electric ceiling fans and their speed regulators intended for domestic and general commercial applications. Specifies air delivery (cubic meters per minute), service value (efficiency), electrical insulation, blade balancing, and silent operation. Mandatory ISI certification is coupled with BEE star-labelling energy efficiency standards.",
        "summary_hi": "IS 374 घरेलू और व्यावसायिक उपयोग के सीलिंग पंखों और रेगुलेटरों का मानक है। इसमें वायु प्रवाह (एयर डिलीवरी), ऊर्जा दक्षता (सर्विस वैल्यू), इन्सुलेशन और शोर रहित संचालन के नियम निर्धारित हैं। सीलिंग पंखों पर अनिवार्य ISI मार्क के साथ बीईई (BEE) स्टार रेटिंग लागू होती है।",
        "keywords": [
            "is 374", "ceiling fan", "electric fan", "fan regulator", "bldc fan", "air delivery",
            "fan isi mark", "pankha", "सीलिंग पंखा", "आईएस 374", "बिजली का पंखा", "पंखे का मानक"
        ],
        "next_steps": [
            "Install wind tunnel air delivery chamber and power analyzer in factory quality lab",
            "Meet minimum service value and insulation resistance requirements",
            "Apply on manakonline.in for BIS licence under IS 374",
            "Coordinate with Bureau of Energy Efficiency (BEE) for mandatory energy star rating"
        ],
        "next_steps_hi": [
            "कारखाने की लैब में एयर डिलीवरी चैंबर और पावर एनालाइजर परीक्षण उपकरण लगाएं",
            "न्यूनतम सर्विस वैल्यू और इंसुलेशन रेजिस्टेंस मानकों को पूरा करें",
            "मानकॉनलाइन पर IS 374 के अंतर्गत बीआईएस लाइसेंस हेतु आवेदन करें",
            "ऊर्जा बचत हेतु बीईई (BEE) स्टार रेटिंग का अनुपालन भी सुनिश्चित करें"
        ],
        "source_title": "BIS Indian Standard IS 374 - Ceiling Fans",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-GEYSER-001",
        "topic": "standard",
        "is_number": "IS 2082",
        "title": "IS 2082 - Stationary Storage Type Electric Water Heaters (Geysers)",
        "title_hi": "IS 2082 - स्टोरेज इलेक्ट्रिक वाटर हीटर (गीजर) विनिर्देश",
        "summary": "IS 2082 applies to stationary electric storage water heaters (geysers) of capacities up to 200 litres for household and commercial use. Specifies pressure vessel safety, thermostat cut-off, thermal insulation (standing loss), pressure relief valve, and earthing continuity. Mandatory ISI mark is required under the Electrical Appliances QCO.",
        "summary_hi": "IS 2082 घरेलू एवं व्यावसायिक उपयोग के 200 लीटर तक की क्षमता वाले स्टोरेज इलेक्ट्रिक वाटर हीटर (गीजर) का मानक है। इसमें इनर टैंक का दबाव परीक्षण, थर्मोस्टेट कट-ऑफ, थर्मल इंसुलेशन और प्रेशर रिलीफ वाल्व की सुरक्षा अनिवार्य है। गीजर पर ISI मार्क अनिवार्य है।",
        "keywords": [
            "is 2082", "geyser", "water heater", "electric geyser", "storage water heater",
            "geyser isi mark", "गीजर", "आईएस 2082", "वाटर हीटर", "पानी गर्म करने का गीजर"
        ],
        "next_steps": [
            "Implement high-pressure hydrostatic burst testing and earth leakage test equipment",
            "Verify thermostat and thermal cut-out redundancy to prevent dry boiling",
            "Apply online via manakonline.in under Scheme-I Product Certification",
            "Ensure BEE 5-star or 4-star energy label is obtained in conjunction with ISI mark"
        ],
        "next_steps_hi": [
            "कारखाने में हाई-प्रेशर हाइड्रोस्टैटिक परीक्षण और अर्थ लीकेज उपकरण स्थापित करें",
            "थर्मोस्टेट और थर्मल कट-आउट सुरक्षा की दोहरी जांच सुनिश्चित करें",
            "मानकॉनलाइन पोर्टल पर योजना-I के अंतर्गत उत्पाद लाइसेंस के लिए आवेदन करें",
            "ISI मार्क के साथ बीईई स्टार लेबलिंग ऊर्जा नियमों का भी अनुपालन करें"
        ],
        "source_title": "BIS Indian Standard IS 2082 - Storage Water Heaters",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-SOLAR-001",
        "topic": "standard",
        "is_number": "IS 14286",
        "title": "IS 14286 - Crystalline Silicon Terrestrial Photovoltaic (PV) Modules",
        "title_hi": "IS 14286 - सौर पीवी मॉड्यूल (सोलर पैनल) डिजाइन एवं प्रकार अनुमोदन",
        "summary": "IS 14286 (harmonized with IEC 61215) governs design qualification and type approval for crystalline silicon photovoltaic (solar PV) modules in India. Specifies tests for thermal cycling, humidity freeze, damp heat, mechanical load, hail impact, and UV exposure. Compulsory certification applies under the Ministry of New and Renewable Energy (MNRE) Order via the Compulsory Registration Scheme (CRS - Scheme-II).",
        "summary_hi": "IS 14286 भारत में सौर पीवी मॉड्यूल (सोलर पैनल) के डिजाइन और विश्वसनीयता का मानक है। इसमें थर्मल साइकिलिंग, डैम्प हीट, ओले के प्रभाव और तेज हवा के दबाव का परीक्षण शामिल है। नवीन और नवीकरणीय ऊर्जा मंत्रालय (MNRE) के तहत योजना-II (CRS) में इसका अनिवार्य पंजीकरण आवश्यक है।",
        "keywords": [
            "is 14286", "solar panel", "pv module", "solar pv", "solar cell", "crs solar",
            "mnre solar", "solar panel bis", "सोलर पैनल", "आईएस 14286", "सौर ऊर्जा मॉड्यूल", "सीआरएस सोलर"
        ],
        "next_steps": [
            "Send solar module test samples to a BIS-recognized solar testing laboratory (NISE, SECI, or accredited private labs)",
            "Obtain passing test reports covering IS 14286, IS/IEC 61730-1, and IS/IEC 61730-2",
            "Register online on the BIS CRS portal (crsbis.in) to receive an R-number (Registration Number)",
            "Label each module with standard CRS Mark and valid R-XXXXXXXX code"
        ],
        "next_steps_hi": [
            "सोलर पैनल नमूनों को बीआईएस मान्यता प्राप्त राष्ट्रीय सौर लैब (जैसे NISE) में परीक्षण हेतु भेजें",
            "IS 14286 और IS/IEC 61730 सुरक्षा मानकों की परीक्षण रिपोर्ट प्राप्त करें",
            "बीआईएस सीआरएस पोर्टल (crsbis.in) पर ऑनलाइन आवेदन कर 8 अंकों का R-नंबर प्राप्त करें",
            "प्रत्येक सोलर पैनल पर अनिवार्य मानक चिह्न और R-नंबर अंकित करें"
        ],
        "source_title": "BIS Compulsory Registration Scheme - Solar PV Modules IS 14286",
        "source_url": "https://www.crsbis.in/BIS/",
        "verified": True
    },
    {
        "id": "STD-ELEC-TOYS-001",
        "topic": "standard",
        "is_number": "IS 15644",
        "title": "IS 15644 - Safety of Electric Toys",
        "title_hi": "IS 15644 - बिजली एवं बैटरी चालित खिलौनों की सुरक्षा विनिर्देश",
        "summary": "IS 15644 specifies electrical and thermal safety requirements for electric and battery-operated toys intended for children up to 14 years. It ensures toys do not exceed maximum safe voltage (24V DC), prevent battery leakage, avoid hazardous heating, and eliminate risk of electric shock or radiation. Mandatory ISI Mark certification applies under the Toys Quality Control Order.",
        "summary_hi": "IS 15644 चौदह वर्ष तक के बच्चों के लिए बैटरी और बिजली से चलने वाले खिलौनों की विद्युत एवं थर्मल सुरक्षा तय करता है। इसमें 24 वोल्ट से कम सुरक्षित वोल्टेज, बैटरी लीकेज रोकथाम और जलने या करंट से सुरक्षा शामिल है। खिलौना QCO के अंतर्गत इस पर अनिवार्य ISI मार्क आवश्यक है।",
        "keywords": [
            "is 15644", "electric toys", "battery toys", "remote car", "kids electric toys",
            "toys safety", "toy qco", "खिलौने", "आईएस 15644", "इलेक्ट्रिक खिलौने", "बैटरी वाले खिलौने"
        ],
        "next_steps": [
            "Test battery compartments for screw enclosure and short-circuit protection",
            "Subject electric toy samples to thermal endurance and drop impact tests in a BIS recognized lab",
            "Apply for Scheme-I ISI Mark certification on manakonline.in",
            "Ensure age recommendation (e.g., 3+) and ISI mark with CM/L number are clearly printed on packaging"
        ],
        "next_steps_hi": [
            "बैटरी कम्पार्टमेंट में स्क्रू लॉक और शॉर्ट-सर्किट सुरक्षा का सत्यापन करें",
            "मान्यता प्राप्त लैब में थर्मल परीक्षण और ड्रॉप इम्पैक्ट टेस्ट करवाएं",
            "मानकॉनलाइन पोर्टल पर योजना-I के अंतर्गत ISI मार्क लाइसेंस हेतु आवेदन करें",
            "पैकेट पर बच्चों की उपयुक्त आयु और सीएम/एल नंबर सहित ISI चिह्न मुद्रित करें"
        ],
        "source_title": "BIS Indian Standard IS 15644 - Electric Toys Safety",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-MILK-POWDER-001",
        "topic": "standard",
        "is_number": "IS 1165",
        "title": "IS 1165 - Milk Powder Specification (Whole and Skimmed)",
        "title_hi": "IS 1165 - दुग्ध चूर्ण (मिल्क पाउडर) विनिर्देश",
        "summary": "IS 1165 governs composition, microbiological purity, and hygienic packaging for milk powder (whole milk powder and skimmed milk powder) in India. Specifies moisture limits, milk fat, milk protein, titratable acidity, insolubility index, and strict absence of pathogenic bacteria (Salmonella, Coliforms). Mandatory ISI Mark is enforced under Section 16 of the BIS Act and FSSAI regulations.",
        "summary_hi": "IS 1165 भारत में दूध के पाउडर (होल एवं स्किम्ड मिल्क पाउडर) की संरचना और सूक्ष्मजीव स्वच्छता का मानक है। इसमें नमी, वसा, प्रोटीन, घुलनशीलता और हानिकारक जीवाणुओं की पूर्ण अनुपस्थिति के कड़े नियम हैं। बीआईएस अधिनियम और FSSAI नियमों के तहत मिल्क पाउडर पर ISI मार्क अनिवार्य है।",
        "keywords": [
            "is 1165", "milk powder", "skimmed milk powder", "dairy standard", "infant milk",
            "doodh powder", "milk powder isi mark", "मिल्क पाउडर", "आईएस 1165", "दूध का पाउडर", "डेयरी मानक"
        ],
        "next_steps": [
            "Establish a clean-room microbiological laboratory for daily batch plate counts and pathogen checks",
            "Verify hermetic sealing and food-grade packaging material conforming to BIS food contact standards",
            "Apply on manakonline.in for Scheme-I certification with FSSAI manufacturing license",
            "Check that ISI Mark and licence number are printed on every commercial pouch and tin"
        ],
        "next_steps_hi": [
            "कारखाने में दैनिक बैक्टीरिया और रोगजनक परीक्षण हेतु साफ सुथरी लैब बनाएं",
            "पैकेजिंग सामग्री का बीआईएस फूड-ग्रेड मानकों के अनुसार होना सुनिश्चित करें",
            "मानकॉनलाइन पर FSSAI लाइसेंस के साथ योजना-I ISI मार्क के लिए आवेदन करें",
            "प्रत्येक पैकेट या टिन पर अनिवार्य ISI मार्क और सीएम/एल नंबर मुद्रित करें"
        ],
        "source_title": "BIS Indian Standard IS 1165 - Milk Powder",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-TYRES-001",
        "topic": "standard",
        "is_number": "IS 15636",
        "title": "IS 15636 - Automotive Vehicles - Pneumatic Tyres for Passenger Cars",
        "title_hi": "IS 15636 - ऑटोमोटिव वाहन - यात्री कारों हेतु न्यूमेटिक टायर विनिर्देश",
        "summary": "IS 15636 specifies dimensions, load rating, high-speed endurance, strength, and bead unseating resistance for pneumatic tyres fitted to passenger vehicles. Mandatory ISI Mark certification is enforced under the Pneumatic Tyres Quality Control Order (QCO) and Central Motor Vehicles Rules (CMVR). No tyre may be imported or sold without an active BIS CM/L licence.",
        "summary_hi": "IS 15636 कारों के न्यूमेटिक टायरों की मजबूती, भार क्षमता, हाई-स्पीड सहनशक्ति और सुरक्षा का मानक है। केंद्रीय मोटर वाहन नियमावली (CMVR) और टायर QCO के तहत टायरों पर ISI मार्क अनिवार्य है। बिना बीआईएस लाइसेंस के कोई भी नया टायर बेचा या आयात नहीं किया जा सकता।",
        "keywords": [
            "is 15636", "car tyres", "automobile tyre", "pneumatic tyre", "tyre qco", "tyre isi mark",
            "radial tyre", "गाड़ी का टायर", "आईएस 15636", "कार टायर", "टायर प्रमाणन"
        ],
        "next_steps": [
            "Install drum endurance test machines, bead unseating rigs, and plunger energy test equipment",
            "Submit test tyres to a recognized automotive test agency (ARAI, ICAT, or CIRT)",
            "Apply on manakonline.in for domestic or FMCS certification",
            "Ensure the ISI mark and CM/L number are molded directly onto the tyre sidewall"
        ],
        "next_steps_hi": [
            "कारखाने में ड्रम एंड्योरेंस और प्लंजर एनर्जी टेस्टिंग मशीनें स्थापित करें",
            "टायर नमूनों को एआरएआई (ARAI) या आईसीएटी (ICAT) ऑटोमोटिव लैब में परीक्षण हेतु भेजें",
            "मानकॉनलाइन पोर्टल पर योजना-I (या विदेशी कंपनियों हेतु FMCS) के तहत आवेदन करें",
            "टायर की साइडवॉल पर उभरा हुआ ISI मार्क और सीएम/एल नंबर मोल्ड होना आवश्यक है"
        ],
        "source_title": "BIS Indian Standard IS 15636 - Passenger Car Tyres",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-THERMO-001",
        "topic": "standard",
        "is_number": "IS 3055 (Part 1)",
        "title": "IS 3055 (Part 1) - Clinical Thermometers (Mercury-in-Glass and Solid-Stem)",
        "title_hi": "IS 3055 (भाग 1) - क्लिनिकल थर्मामीटर (बुखार नापने का थर्मामीटर) विनिर्देश",
        "summary": "IS 3055 (Part 1) covers clinical thermometers used for measuring human body temperature. Specifies scale accuracy (+/- 0.1°C), constriction reliability, mercury thread retreat, and thermal shock resistance. Mandatory ISI Mark applies to ensure medical measurement integrity in clinics, hospitals, and homes.",
        "summary_hi": "IS 3055 (भाग 1) मानव शरीर का तापमान मापने वाले क्लिनिकल थर्मामीटर का मानक है। इसमें तापमान पैमाने की शुद्धता (+/- 0.1°C), पारे की गति और थर्मल शॉक की विश्वसनीयता सुनिश्चित की जाती है। चिकित्सा शुद्धता के लिए इस पर अनिवार्य ISI मार्क आवश्यक है।",
        "keywords": [
            "is 3055", "thermometer", "clinical thermometer", "mercury thermometer", "fever thermometer",
            "medical devices", "थर्मामीटर", "आईएस 3055", "बुखार नापने का यंत्र", "क्लिनिकल थर्मामीटर"
        ],
        "next_steps": [
            "Calibrate temperature bath standards against National Physical Laboratory (NPL) references",
            "Perform water bath comparative tests for scale accuracy and constrictor safety",
            "Apply via manakonline.in for Scheme-I product licence",
            "Ensure the ISI logo, CM/L number, and Celsius scale are etched legibly on the glass tube"
        ],
        "next_steps_hi": [
            "राष्ट्रीय भौतिक प्रयोगशाला (NPL) के मानकों के अनुसार परीक्षण उपकरणों का अंशांकन करें",
            "जल-कुंड में तुलनात्मक पैमाने की सटीकता (+/- 0.1°C) का सत्यापन करें",
            "मानकॉनलाइन पोर्टल पर योजना-I लाइसेंस के लिए आवेदन करें",
            "कांच की नली पर मुद्रित ISI मार्क, सीएम/एल नंबर और सेल्सियस पैमाने की जांच करें"
        ],
        "source_title": "BIS Indian Standard IS 3055 - Clinical Thermometers",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-MASKS-001",
        "topic": "standard",
        "is_number": "IS 16289",
        "title": "IS 16289 - Medical Face Masks (Surgical 3-Ply Masks)",
        "title_hi": "IS 16289 - मेडिकल फेस मास्क (सर्जिकल 3-प्लाई मास्क) विनिर्देश",
        "summary": "IS 16289 specifies construction and performance for surgical and medical face masks intended to protect healthcare workers and patients. Categorizes masks into Class 1, Class 2, and Class 3 based on Bacterial Filtration Efficiency (BFE >= 95% to 98%), Differential Pressure (breathability), Splash Resistance against synthetic blood, and microbial cleanliness.",
        "summary_hi": "IS 16289 सर्जिकल और मेडिकल फेस मास्क (3-प्लाई मास्क) का आधिकारिक मानक है। इसमें बैक्टीरियल फिल्ट्रेशन क्षमता (BFE 95% से 98%), सांस लेने में सुगमता (डिफरेंशियल प्रेशर) और रक्त छींटों के प्रतिरोध के आधार पर क्लास 1, 2 और 3 निर्धारित हैं।",
        "keywords": [
            "is 16289", "face mask", "surgical mask", "3 ply mask", "medical mask", "bfe 98",
            "ppe mask", "मास्क", "आईएस 16289", "सर्जिकल मास्क", "3 प्लाई मास्क", "मेडिकल मास्क"
        ],
        "next_steps": [
            "Equip manufacturing clean room with meltblown filtration media verification tests",
            "Send samples to BIS-approved textile and biological labs for BFE and synthetic blood splash testing",
            "Apply for BIS Product Certification on manakonline.in",
            "Print ISI mark, classification (Class 1/2/3), and manufacturer batch details on the box"
        ],
        "next_steps_hi": [
            "कारखाने में मेल्टब्लाउन फिल्टर कपड़े की गुणवत्ता और स्वच्छता का परीक्षण करें",
            "मान्यता प्राप्त लैब में BFE और ब्लड स्प्लैश प्रतिरोध की जांच करवाएं",
            "मानकॉनलाइन पर योजना-I के तहत ISI मार्क हेतु आवेदन करें",
            "मास्क के बॉक्स पर ISI मार्क, क्लास (Class 1/2/3) और बैच नंबर स्पष्ट रूप से लिखें"
        ],
        "source_title": "BIS Indian Standard IS 16289 - Medical Face Masks",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-HAWAII-CHAPPAL-001",
        "topic": "standard",
        "is_number": "IS 10702",
        "title": "IS 10702 - Rubber Hawaii Chappals Specifications",
        "title_hi": "IS 10702 - रबर हवाई चप्पल एवं घरेलू स्लीपर्स विनिर्देश",
        "summary": "IS 10702 specifies requirements for rubber Hawaii chappals and flip-flops composed of microcellular rubber soles and rubber straps. Details hardness, relative density, split tear strength, tensile strength, and strap attachment pull test. Note: Hawaii chappals fall under voluntary BIS certification, unlike heavy industrial protective footwear which is strictly mandatory.",
        "summary_hi": "IS 10702 रबर की हवाई चप्पलों और घरेलू स्लीपर्स का मानक है, जिसमें सोल और स्ट्रैप की मजबूती, लचीलापन, वजन और घिसाव प्रतिरोध शामिल है। ध्यान दें: सामान्य हवाई चप्पलें स्वैच्छिक बीआईएस प्रमाणन के अंतर्गत आती हैं, जबकि कारखानों के भारी सेफ्टी जूते अनिवार्य ISI मार्क में आते हैं।",
        "keywords": [
            "is 10702", "hawaii chappal", "rubber slippers", "flip flops", "casual slippers",
            "chappal standard", "चप्पल", "हवाई चप्पल", "आईएस 10702", "रबर चप्पल", "स्लीपर"
        ],
        "next_steps": [
            "Verify tensile strength of rubber compound and strap attachment retention",
            "Manufacturers may voluntarily obtain the ISI Mark under Scheme-I for brand quality trust",
            "Distinguish general consumer chappals from industrial safety footwear governed by IS 15298",
            "Apply online at manakonline.in if voluntary certification is sought"
        ],
        "next_steps_hi": [
            "रबर सोल के लचीलेपन और स्ट्रैप की मजबूती की जांच करें",
            "निर्माता ब्रांड विश्वसनीयता हेतु स्वेच्छा से योजना-I के तहत ISI मार्क ले सकते हैं",
            "सामान्य चप्पलों को औद्योगिक सुरक्षा जूतों (IS 15298) से अलग समझें",
            "यदि स्वैच्छिक प्रमाणन चाहिए तो मानकॉनलाइन पर आवेदन करें"
        ],
        "source_title": "BIS Indian Standard IS 10702 - Rubber Hawaii Chappals",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-PLUG-SOCKET-001",
        "topic": "standard",
        "is_number": "IS 1293",
        "title": "IS 1293 - Plugs and Socket-Outlets of Rated Voltage up to 250 Volts",
        "title_hi": "IS 1293 - प्लग एवं सॉकेट-आउटलेट (250 वोल्ट तक) विनिर्देश",
        "summary": "IS 1293 governs safety, dimensions, and endurance of household plugs and socket-outlets (6A, 10A, 16A) in India. Specifies shutter safety (child-proof shutters), temperature rise, mechanical endurance, insulation resistance, and non-accessibility to live pins during insertion. Mandatory ISI Mark applies under the Electrical Accessories Quality Control Order.",
        "summary_hi": "IS 1293 भारत में घरेलू प्लग और सॉकेट (6A, 10A, 16A) की सुरक्षा और आयामों का मानक है। इसमें बच्चों की सुरक्षा हेतु शटर, पिन की मजबूती, तापमान वृद्धि और करंट से सुरक्षा अनिवार्य है। इलेक्ट्रिकल एक्सेसरीज QCO के तहत प्लग और सॉकेट पर ISI मार्क अनिवार्य है।",
        "keywords": [
            "is 1293", "plug and socket", "electric plug", "socket outlet", "16a socket", "6a plug",
            "power plug", "switch socket", "प्लग और सॉकेट", "आईएस 1293", "बिजली का प्लग", "सॉकेट"
        ],
        "next_steps": [
            "Set up test gauges for pin dimensions, withdrawal force, and temperature rise testing",
            "Ensure shutters prevent single-pin insertion and child tampering",
            "Apply for Scheme-I ISI Mark certification on manakonline.in",
            "Ensure the ISI emblem and CM/L number are molded onto the plastic housing of the plug and socket"
        ],
        "next_steps_hi": [
            "प्लग पिन के आकार, तापमान वृद्धि और मजबूती के गेज परीक्षण उपकरण स्थापित करें",
            "सुनिश्चित करें कि सॉकेट में चाइल्ड-प्रूफ शटर ठीक से काम कर रहे हैं",
            "मानकॉनलाइन पोर्टल पर योजना-I लाइसेंस हेतु आवेदन करें",
            "प्लग और सॉकेट की बॉडी पर उभरा हुआ ISI मार्क और सीएम/एल नंबर अवश्य अंकित करें"
        ],
        "source_title": "BIS Indian Standard IS 1293 - Plugs and Sockets",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-WELDING-001",
        "topic": "standard",
        "is_number": "IS 814",
        "title": "IS 814 - Covered Electrodes for Manual Metal Arc Welding",
        "title_hi": "IS 814 - वेल्डिंग इलेक्ट्रोड (कवर्ड इलेक्ट्रोड) विनिर्देश",
        "summary": "IS 814 specifies requirements for covered carbon and carbon-manganese steel electrodes used for manual metal arc welding of structural and pressure vessel steels. Details tensile strength, elongation, Charpy V-notch impact value, radiographic sound quality, and coating concentricity. Mandatory ISI Mark is enforced under the Steel Products QCO.",
        "summary_hi": "IS 814 मेटल आर्क वेल्डिंग में उपयोग होने वाले कवर्ड स्टील वेल्डिंग इलेक्ट्रोड का आधिकारिक मानक है। इसमें वेल्ड मेटल की तन्यता, लचीलापन, इम्पैक्ट मजबूती और रेडियोग्राफिक शुद्धता के नियम शामिल हैं। इस्पात मंत्रालय के QCO के तहत वेल्डिंग इलेक्ट्रोड पर ISI मार्क अनिवार्य है।",
        "keywords": [
            "is 814", "welding electrode", "welding rod", "arc welding", "welding steel",
            "welding qco", "वेल्डिंग रॉड", "आईएस 814", "वेल्डिंग इलेक्ट्रोड", "वेल्डिंग का मानक"
        ],
        "next_steps": [
            "Conduct chemical analysis of core wire and flux coating materials",
            "Fabricate all-weld metal test assemblies and test for tensile and Charpy V-notch impact properties",
            "Submit online application on manakonline.in for Scheme-I certification",
            "Check that the ISI Mark, electrode classification (e.g., E6013), and batch are printed on the package"
        ],
        "next_steps_hi": [
            "कोर वायर और फ्लक्स कोटिंग सामग्री का रासायनिक विश्लेषण करें",
            "वेल्ड मेटल के नमूनों का तन्यता और चार्पी इम्पैक्ट परीक्षण करवाएं",
            "मानकॉनलाइन पर योजना-I ISI मार्क हेतु आवेदन करें",
            "पैकेट पर इलेक्ट्रोड वर्गीकरण (जैसे E6013) और ISI मार्क की जांच करें"
        ],
        "source_title": "BIS Indian Standard IS 814 - Welding Electrodes",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-MINERAL-WATER-001",
        "topic": "standard",
        "is_number": "IS 13428",
        "title": "IS 13428 - Packaged Natural Mineral Water",
        "title_hi": "IS 13428 - पैकेज्ड प्राकृतिक खनिज जल (नेचुरल मिनरल वाटर) विनिर्देश",
        "summary": "IS 13428 applies exclusively to natural mineral water obtained directly from natural underground sources (springs, artesian wells) without altering its essential mineral composition. Distinct from packaged drinking water (IS 14543): chemical treatment is strictly prohibited (only filtration and aeration allowed). Mandatory ISI Mark is enforced by law across India.",
        "summary_hi": "IS 13428 प्राकृतिक स्रोतों (जैसे पहाड़ों या भूमिगत झरनों) से सीधे प्राप्त प्राकृतिक खनिज जल (नेचुरल मिनरल वाटर) का मानक है। यह सामान्य पैकेज्ड पानी (IS 14543) से अलग है क्योंकि इसमें रासायनिक परिवर्तन वर्जित है। इस पर अनिवार्य ISI मार्क लागू होता है।",
        "keywords": [
            "is 13428", "natural mineral water", "spring water", "mineral water bottle", "packaged mineral water",
            "mineral water isi mark", "प्राकृतिक खनिज जल", "आईएस 13428", "मिनरल वाटर", "नेचुरल मिनरल वाटर"
        ],
        "next_steps": [
            "Prove geographical authenticity and continuous hygienic source protection at the natural source",
            "Establish on-site microbiological and chemical testing labs for heavy metals and pesticides",
            "Apply for BIS Scheme-I licence with mandatory factory audit and independent sampling",
            "Verify ISI mark, CM/L number, and source location printed on the sealed bottle"
        ],
        "next_steps_hi": [
            "प्राकृतिक स्रोत के संरक्षण और निरंतर स्वच्छता का भूगर्भीय प्रमाण प्रस्तुत करें",
            "कारखाने में भारी धातुओं और कीटनाशक अवशेषों की जांच हेतु लैब स्थापित करें",
            "योजना-I के तहत कारखाना निरीक्षण और पानी की सैंपलिंग करवाएं",
            "बोतल पर स्रोत का नाम, अनिवार्य ISI मार्क और सीएम/एल नंबर मुद्रित होना आवश्यक है"
        ],
        "source_title": "BIS Indian Standard IS 13428 - Natural Mineral Water",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-ELEC-IRON-001",
        "topic": "standard",
        "is_number": "IS 302 (Part 2/Sec 3)",
        "title": "IS 302 (Part 2/Sec 3) - Safety of Electric Dry and Steam Irons",
        "title_hi": "IS 302 (भाग 2/अनुभाग 3) - बिजली की स्त्री (इलेक्ट्रिक प्रेस / आयरन) विनिर्देश",
        "summary": "IS 302 (Part 2/Sec 3) specifies safety and endurance requirements for electric dry irons and steam irons used in homes. Details thermostat precision, heating element insulation, earthing continuity, cord flex testing, and prevention of thermal fire hazards. Mandatory ISI Mark is required under the Electrical Appliances QCO.",
        "summary_hi": "IS 302 (भाग 2/अनुभाग 3) घरेलू कपड़ों की बिजली वाली प्रेस (ड्राय और स्टीम आयरन) की सुरक्षा का मानक है। इसमें थर्मोस्टेट की सटीकता, अर्थिंग की मजबूती, केबल के मुड़ने की क्षमता और आग के खतरों से सुरक्षा शामिल है। बिजली की प्रेस पर अनिवार्य ISI मार्क होना आवश्यक है।",
        "keywords": [
            "electric iron", "is 302 2 3", "steam iron", "dry iron", "press standard",
            "iron isi mark", "बिजली की प्रेस", "आयरन", "आईएस 302", "स्त्री", "स्टीम आयरन"
        ],
        "next_steps": [
            "Test thermostat cycling life (over 10,000 cycles) and thermal fuse safety cut-off",
            "Conduct high-voltage breakdown test (1500V) and cord flex endurance test in-house",
            "Submit licence application on manakonline.in under Scheme-I",
            "Verify ISI mark and CM/L licence number embossed on the iron rating plate"
        ],
        "next_steps_hi": [
            "थर्मोस्टेट की लाइफ साइकिल (10,000 से अधिक बार) और थर्मल फ्यूज कट-ऑफ का परीक्षण करें",
            "कारखाने में 1500V हाई-वोल्टेज और केबल फ्लेक्सिंग का परीक्षण करें",
            "मानकॉनलाइन पोर्टल पर योजना-I के तहत लाइसेंस के लिए आवेदन करें",
            "आयरन की नेमप्लेट पर मुद्रित ISI मार्क और सीएम/एल नंबर की जांच करें"
        ],
        "source_title": "BIS Indian Standard IS 302-2-3 - Electric Irons",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-MIXER-GRINDER-001",
        "topic": "standard",
        "is_number": "IS 302 (Part 2/Sec 14)",
        "title": "IS 302 (Part 2/Sec 14) - Electric Kitchen Machines, Mixers, Grinders & Blenders",
        "title_hi": "IS 302 (भाग 2/अनुभाग 14) - मिक्सर, ग्राइंडर एवं ब्लेंडर विनिर्देश",
        "summary": "IS 302 (Part 2/Sec 14) governs the safety of electric food mixers, juicers, grinders, blenders, and food processors. Covers overload protection, electrical shock insulation, blade locking safety, thermal motor protection, and ingress of water into motor housing. Mandatory ISI Mark is enforced under the Electrical Appliances QCO.",
        "summary_hi": "IS 302 (भाग 2/अनुभाग 14) घरेलू मिक्सर, ग्राइंडर, जूसर और फूड प्रोसेसर की सुरक्षा का मानक है। इसमें ओवरलोड प्रोटेक्शन, करंट से सुरक्षा, ब्लेड लॉक सुरक्षा और मोटर में पानी जाने से बचाव के नियम तय किए गए हैं। मिक्सर-ग्राइंडर पर ISI मार्क अनिवार्य है।",
        "keywords": [
            "mixer grinder", "is 302 2 14", "food processor", "blender", "juicer mixer",
            "mixer isi mark", "मिक्सर ग्राइंडर", "आईएस 302", "मिक्सी", "जूसर मिक्सर"
        ],
        "next_steps": [
            "Equip testing laboratory with locked-rotor test rig and overload trip measurement instruments",
            "Perform mechanical stability, moisture ingress, and blade impact tests",
            "Apply online on manakonline.in for BIS Scheme-I licence",
            "Ensure the ISI emblem and CM/L number are molded on the mixer base rating plate"
        ],
        "next_steps_hi": [
            "कारखाने में लॉक्ड-रोटर परीक्षण और ओवरलोड ट्रिप उपकरण लगाएं",
            "मोटर की स्थिरता, नमी प्रतिरोध और ब्लेड की मजबूती की जांच करें",
            "मानकॉनलाइन पर योजना-I के अंतर्गत लाइसेंस आवेदन करें",
            "मिक्सर की बेस प्लेट पर उभरा हुआ ISI मार्क और सीएम/एल नंबर अवश्य मुद्रित करें"
        ],
        "source_title": "BIS Indian Standard IS 302-2-14 - Kitchen Machines",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-CEMENT-OPC43-001",
        "topic": "standard",
        "is_number": "IS 269",
        "title": "IS 269 - Ordinary Portland Cement (33, 43, and 53 Grades)",
        "title_hi": "IS 269 - साधारण पोर्टलैंड सीमेंट (33, 43 एवं 53 ग्रेड) विनिर्देश",
        "summary": "IS 269 is the comprehensive revised standard covering Ordinary Portland Cement across 33 Grade, 43 Grade, and 53 Grade. Specifies chemical modulus limits, fineness (specific surface by Blaine air permeability), initial and final setting times, soundness (Le Chatelier & Autoclave), and compressive strength (43 MPa at 28 days for 43 Grade). Mandatory ISI Mark applies by statutory order.",
        "summary_hi": "IS 269 साधारण पोर्टलैंड सीमेंट (33 ग्रेड, 43 ग्रेड और 53 ग्रेड) का एकीकृत आधिकारिक मानक है। इसमें रासायनिक अनुपात, महीनता (ब्लेन टेस्ट), जमने का समय (सेटिंग टाइम), साउंडनेस और 28 दिनों की कंप्रेसिव मजबूती (43 ग्रेड हेतु 43 MPa) निर्धारित है। सीमेंट पर अनिवार्य ISI मार्क कानूनन लागू है।",
        "keywords": [
            "is 269", "opc 43", "opc cement", "ordinary portland cement", "43 grade cement",
            "cement standard", "cement isi mark", "ओपीसी सीमेंट", "आईएस 269", "43 ग्रेड सीमेंट", "सीमेंट का मानक"
        ],
        "next_steps": [
            "Set up complete in-house chemical wet lab and compressive strength compression testing machine",
            "Ensure raw clinker and gypsum ratios comply with IS 269 chemical limits",
            "Submit Scheme-I application on manakonline.in with verified factory layout",
            "Ensure cement bags bear the ISI logo, Grade (43 Grade), week and year of manufacture, and net weight"
        ],
        "next_steps_hi": [
            "कारखाने में पूर्ण रासायनिक लैब और 28-दिवसीय मजबूती परीक्षण मशीन स्थापित करें",
            "क्लिंकर और जिप्सम के अनुपात को IS 269 के रासायनिक नियमों के अनुसार बनाए रखें",
            "मानकॉनलाइन पर योजना-I के अंतर्गत कारखाना निरीक्षण हेतु आवेदन करें",
            "बोरी पर स्पष्ट रूप से ISI मार्क, ग्रेड (43 ग्रेड), निर्माण का सप्ताह/वर्ष और शुद्ध वजन लिखें"
        ],
        "source_title": "BIS Indian Standard IS 269 - Ordinary Portland Cement",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "STD-BATTERY-001",
        "topic": "standard",
        "is_number": "IS 16046 (Part 1 & 2)",
        "title": "IS 16046 - Secondary Cells and Batteries (Lithium-ion Batteries for Portables)",
        "title_hi": "IS 16046 - लिथियम-आयन बैटरी एवं पोर्टेबल सेल्स विनिर्देश (CRS योजना)",
        "summary": "IS 16046 (Part 1 for nickel systems, Part 2 for lithium systems) specifies safety requirements for portable secondary sealed cells and batteries containing non-acid electrolytes (Lithium-ion / Li-polymer batteries used in mobile phones, power banks, and laptops). Governs continuous charging, short circuit, overcharging, thermal abuse, and crush resistance under Compulsory Registration Scheme (CRS).",
        "summary_hi": "IS 16046 पोर्टेबल लिथियम-आयन बैटरियों (मोबाइल, पावर बैंक, लैपटॉप में प्रयुक्त) की सुरक्षा का मानक है। इसमें ओवरचार्जिंग, शॉर्ट सर्किट, अत्यधिक तापमान और आग से सुरक्षा के परीक्षण शामिल हैं। इलेक्ट्रॉनिक्स मंत्रालय (MeitY) के तहत योजना-II (CRS) में इसका अनिवार्य पंजीकरण आवश्यक है।",
        "keywords": [
            "is 16046", "lithium battery", "li-ion battery", "power bank battery", "mobile battery",
            "battery safety", "crs battery", "बैटरी", "आईएस 16046", "लिथियम बैटरी", "पावर बैंक बैटरी"
        ],
        "next_steps": [
            "Submit battery cell and pack samples to a BIS-recognized testing laboratory for safety evaluation",
            "Obtain passing test reports covering thermal abuse, free fall, and mechanical crush tests",
            "Register on the BIS CRS portal (crsbis.in) to receive an assigned R-number",
            "Affix the standard CRS mark and R-number (e.g., R-XXXXXXXX) on every battery label"
        ],
        "next_steps_hi": [
            "बैटरी पैक नमूनों को बीआईएस मान्यता प्राप्त परीक्षण लैब में जांच हेतु भेजें",
            "शॉर्ट सर्किट और थर्मल सुरक्षा की अधिकृत लैब रिपोर्ट प्राप्त करें",
            "crsbis.in पोर्टल पर पंजीकरण कर R-नंबर (रजिस्ट्रेशन नंबर) प्राप्त करें",
            "प्रत्येक बैटरी लेबल पर अनिवार्य मानक चिह्न और R-नंबर अंकित करें"
        ],
        "source_title": "BIS Compulsory Registration Scheme - Batteries IS 16046",
        "source_url": "https://www.crsbis.in/BIS/",
        "verified": True
    },
    {
        "id": "STD-HELMET-IND-001",
        "topic": "standard",
        "is_number": "IS 2925",
        "title": "IS 2925 - Industrial Safety Helmets (Construction Hard Hats)",
        "title_hi": "IS 2925 - औद्योगिक सुरक्षा हेलमेट (कंस्ट्रक्शन हार्ड हैट) विनिर्देश",
        "summary": "IS 2925 covers industrial safety helmets (hard hats) designed for head protection against falling objects and electrical hazards in construction sites, mines, refineries, and manufacturing plants. Tests include impact shock absorption (50 Joules), penetration resistance, flammability, and electrical insulation up to 2000V. Mandatory ISI Mark applies.",
        "summary_hi": "IS 2925 निर्माण स्थलों, खदानों और कारखानों में सिर की सुरक्षा हेतु औद्योगिक सेफ्टी हेलमेट (हार्ड हैट) का मानक है। इसमें 50 जूल का शॉक एब्जॉर्प्शन, नुकीली वस्तु प्रतिरोध, आग प्रतिरोध और 2000 वोल्ट तक विद्युत इंसुलेशन का परीक्षण होता है। इस पर अनिवार्य ISI मार्क लागू होता है।",
        "keywords": [
            "is 2925", "hard hat", "industrial helmet", "safety helmet", "construction helmet",
            "head protection", "सेफ्टी हेलमेट", "आईएस 2925", "हार्ड हैट", "कंस्ट्रक्शन हेलमेट"
        ],
        "next_steps": [
            "Establish drop tower impact absorption rig and electrical insulation test tank in-house",
            "Ensure shell polymer (HDPE/ABS) and harness cradle meet shock absorption criteria",
            "Apply for Scheme-I Product Certification on manakonline.in",
            "Verify molded ISI mark, CM/L number, and manufacturing month/year inside the helmet peak"
        ],
        "next_steps_hi": [
            "कारखाने में ड्रॉप इम्पैक्ट शॉक एब्जॉर्प्शन और इलेक्ट्रिकल इंसुलेशन टेस्टिंग उपकरण लगाएं",
            "हेलमेट के शेल (HDPE/ABS) और हार्नेस के लचीलेपन की जांच करें",
            "मानकॉनलाइन पोर्टल पर योजना-I के तहत आवेदन करें",
            "हेलमेट के अंदर मोल्ड किए गए ISI मार्क और सीएम/एल नंबर की जांच करें"
        ],
        "source_title": "BIS Indian Standard IS 2925 - Industrial Helmets",
        "source_url": "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/isdetails",
        "verified": True
    },
    {
        "id": "PROC-MANAKONLINE-001",
        "topic": "process",
        "title": "Manakonline Portal - Digital e-Services for BIS Licences and Applications",
        "title_hi": "मानकॉनलाइन पोर्टल (manakonline.in) - बीआईएस डिजिटल ई-सेवाएं एवं आवेदन प्रक्रिया",
        "summary": "Manakonline (manakonline.in) is the unified official digital portal for all Bureau of Indian Standards e-services. It facilitates online application for Product Certification (Scheme-I, Scheme-X), licence renewals, fee payments, factory audit scheduling, testing requests under the Laboratory Information Management System (LIMS), and Hallmarking center registrations. All domestic and international filings are processed paperlessly.",
        "summary_hi": "मानकॉनलाइन (manakonline.in) बीआईएस की सभी ई-सेवाओं का एकीकृत आधिकारिक पोर्टल है। इसके माध्यम से नए लाइसेंस (योजना-I, योजना-X), लाइसेंस नवीनीकरण, सरकारी शुल्क भुगतान, कारखाना ऑडिट शेड्यूलिंग, लैब परीक्षण (LIMS) और हॉलमार्किंग पंजीकरण पूरी तरह डिजिटल और पेपरलेस तरीके से किए जाते हैं।",
        "keywords": [
            "manakonline", "bis portal", "online licence application", "lims bis", "manakonline portal",
            "cml application", "renew online bis", "मानकॉनलाइन", "बीआईएस पोर्टल", "ऑनलाइन आवेदन", "लाइसेंस पोर्टल"
        ],
        "next_steps": [
            "Register an enterprise account on manakonline.in using official GSTIN and PAN details",
            "Select 'Product Certification' or 'Hallmarking' module based on your business requirement",
            "Upload factory layout, list of in-house testing equipment, and manufacturing process flowcharts",
            "Track application status, scrutiny queries, and inspection dates in the interactive applicant dashboard"
        ],
        "next_steps_hi": [
            "कंपनी के पैन और जीएसटी विवरण के साथ manakonline.in पर उद्यम खाता बनाएं",
            "अपनी आवश्यकतानुसार 'उत्पाद प्रमाणन' या 'हॉलमार्किंग' मॉड्यूल का चयन करें",
            "कारखाने का नक्शा, इन-हाउस लैब उपकरणों की सूची और निर्माण प्रक्रिया अपलोड करें",
            "डैशबोर्ड में आवेदन की प्रगति, ऑडिट तिथि और अधिकारियों के प्रश्नों का उत्तर ट्रैक करें"
        ],
        "source_title": "Manakonline - BIS Official e-Services Portal",
        "source_url": "https://www.manakonline.in/",
        "verified": True
    },
    {
        "id": "LAW-QCO-LIST-001",
        "topic": "certification",
        "title": "Quality Control Orders (QCO) Master Guide - Mandatory Certification in India",
        "title_hi": "गुणवत्ता नियंत्रण आदेश (QCO) मास्टर गाइड - भारत में अनिवार्य बीआईएस प्रमाणन",
        "summary": "Quality Control Orders (QCOs) are statutory executive notifications issued by Central Government Ministries (under Section 16 of the BIS Act, 2016) making BIS certification and standard marks legally compulsory for specified goods. Once a QCO is enforced, no person or entity may manufacture, import, store, sell, or distribute non-certified goods. Violation is a criminal offense under Section 29, punishable by imprisonment and heavy financial fines.",
        "summary_hi": "गुणवत्ता नियंत्रण आदेश (QCO) बीआईएस अधिनियम 2016 की धारा 16 के तहत केंद्र सरकार के मंत्रालयों द्वारा जारी अनिवार्य आदेश हैं। QCO लागू होने के बाद बिना बीआईएस प्रमाणन और मानक चिह्न (ISI मार्क/CRS) के सामान बनाना, बेचना, आयात या स्टोर करना गैर-कानूनी है। इसका उल्लंघन धारा 29 के तहत दंडनीय अपराध है जिसमें जेल और भारी जुर्माना हो सकता है।",
        "keywords": [
            "qco", "quality control order", "mandatory bis list", "compulsory bis products",
            "section 16 bis act", "qco compliance", "qco notification", "क्यूसीओ", "गुणवत्ता नियंत्रण आदेश", "अनिवार्य बीआईएस"
        ],
        "next_steps": [
            "Consult the latest QCO gazette notifications on bis.gov.in to check enforcement dates for your product",
            "Apply for BIS certification at least 3-4 months prior to the QCO implementation deadline",
            "Verify whether small/micro enterprises (MSME) are granted transitional extension periods",
            "Report non-certified sale of QCO goods to BIS enforcement officers or via the BIS Care Mobile App"
        ],
        "next_steps_hi": [
            "अपने उत्पाद की QCO लागू होने की तिथि जानने हेतु bis.gov.in पर नवीनतम अधिसूचनाएं देखें",
            "QCO लागू होने की अंतिम तिथि से कम से कम 3-4 महीने पहले बीआईएस लाइसेंस हेतु आवेदन करें",
            "जांचें कि क्या एमएसएमई (MSME) इकाइयों को अतिरिक्त समय दिया गया है",
            "QCO का उल्लंघन करने वाले अवैध उत्पादों की बीआईएस केयर ऐप से शिकायत दर्ज करें"
        ],
        "source_title": "BIS Quality Control Orders (QCO) Directory",
        "source_url": "https://www.bis.gov.in/product-certification/products-under-compulsory-certification/",
        "verified": True
    }
]


def expand():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {e["id"] for e in data["entries"]}
    added = 0

    for new_e in NEW_ENTRIES:
        if new_e["id"] in existing_ids:
            print(f"Skipping already existing ID: {new_e['id']}")
            continue
        data["entries"].append(new_e)
        existing_ids.add(new_e["id"])
        added += 1

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully added {added} new entries. Total entries now: {len(data['entries'])}")


if __name__ == "__main__":
    expand()
