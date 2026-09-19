"""
Bureau of Indian Standards (BIS) - Complete Standards Catalog Extractor
Target: https://standardsbis.bsbedge.com/
Extracts the complete official Indian Standards database from BSB Edge / BIS portal.
"""

import os
import json
import csv
import re
import time
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "https://standardsbis.bsbedge.com/popupextender.aspx/GetStdNo_Bis"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://standardsbis.bsbedge.com/"
}

def fetch_prefix(prefix):
    payload = {
        "prefixText": str(prefix),
        "count": 500,
        "contextKey": ""
    }
    try:
        resp = requests.post(URL, json=payload, headers=HEADERS, timeout=12)
        if resp.status_code == 200:
            return resp.json().get("d", [])
    except Exception:
        pass
    return []

def extract_all():
    print("[*] Starting complete BIS standards extraction from standardsbis.bsbedge.com...")
    t0 = time.time()
    
    # 1. Build rich query list covering all standard number sequences
    prefixes = []
    
    # All 3-digit prefixes from 001 to 250 (captures virtually every standard due to wildcard substring matching)
    for i in range(1, 260):
        prefixes.append(str(i).zfill(3))
        
    # Additional high-density ranges and popular civil/mechanical/safety prefixes
    special_prefixes = [
        "456", "800", "875", "1893", "10500", "1200", "13920", "383", "2062", 
        "1904", "1905", "2911", "3370", "4998", "6403", "8009", "1343", "10262",
        "14458", "16700", "15658", "15498", "1608", "732", "3043", "5216", "1293",
        "6192", "8392", "8470", "13108", "4326", "15060", "15778", "1592", "3938",
        "SP ", "SP 1", "SP 2", "SP 3", "SP 4", "SP 6", "SP 7", "SP 16", "SP 23", "SP 34"
    ]
    for sp in special_prefixes:
        if sp not in prefixes:
            prefixes.append(sp)
            
    print(f"[*] Total query prefixes to probe: {len(prefixes)} using parallel workers...")
    
    raw_entries = set()
    total_queries = len(prefixes)
    completed_queries = 0
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_prefix = {executor.submit(fetch_prefix, p): p for p in prefixes}
        for future in as_completed(future_to_prefix):
            completed_queries += 1
            res = future.result()
            if res:
                raw_entries.update(res)
            if completed_queries % 50 == 0 or completed_queries == total_queries:
                print(f"    Progress: {completed_queries}/{total_queries} queries completed | Current unique standards: {len(raw_entries)}")
                
    print(f"\n[+] Raw unique entries collected: {len(raw_entries)} in {round(time.time() - t0, 2)}s")
    print("[*] Parsing and structuring standard records...")
    
    parsed_standards = {}
    
    for item_str in raw_entries:
        try:
            obj = json.loads(item_str)
            raw_first = obj.get("First", "").strip()
            raw_second = obj.get("Second", "").strip()
            
            # Clean display title (remove "BIS -- " prefix)
            clean_title = raw_first.replace("BIS -- ", "").strip()
            
            std_no = ""
            std_id = ""
            if "Standard_Number=" in raw_second:
                params = urllib.parse.parse_qs(raw_second)
                std_no = params.get("Standard_Number", [""])[0]
                std_id = params.get("id", [""])[0]
                
            # If standard_number is still empty, parse from title
            if not std_no and clean_title:
                std_no = clean_title.split(":")[0].strip()
                
            # Extract Year if available in title (e.g. "IS 456 : 2000" -> "2000")
            year_match = re.search(r':\s*(\d{4})\b', clean_title)
            year = year_match.group(1) if year_match else ""
            
            key = (std_no, std_id)
            if key not in parsed_standards or len(clean_title) > len(parsed_standards[key]["title"]):
                parsed_standards[key] = {
                    "standard_number": std_no,
                    "title": clean_title,
                    "year": year,
                    "id": std_id,
                    "source": "Bureau of Indian Standards - e-Sale (standardsbis.bsbedge.com)",
                    "detail_url": f"https://standardsbis.bsbedge.com/BIS_SearchStandard.aspx?{raw_second}"
                }
        except Exception:
            continue
            
    catalog = sorted(parsed_standards.values(), key=lambda x: x["standard_number"])
    print(f"[+] Successfully structured {len(catalog)} unique Indian Standards!")
    
    # Define output filepaths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "bis_standards_catalog.json")
    csv_path = os.path.join(current_dir, "bis_standards_catalog.csv")
    
    # Save JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved JSON catalog to: {json_path} ({os.path.getsize(json_path) / 1024:.1f} KB)")
    
    # Save CSV
    fieldnames = ["standard_number", "title", "year", "id", "source", "detail_url"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in catalog:
            writer.writerow(row)
    print(f"[+] Saved CSV catalog to: {csv_path} ({os.path.getsize(csv_path) / 1024:.1f} KB)")
    
    return catalog

if __name__ == "__main__":
    extract_all()
