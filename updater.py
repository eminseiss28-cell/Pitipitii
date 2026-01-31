import os
import requests
import json

# Ana kaynakların kök adresleri
KEKIK_BASE = "https://raw.githubusercontent.com/keyiflerolsun/Kekik-cloudstream/master"
NIK_BASE = "https://raw.githubusercontent.com/sarapcanagii/Pitipitii/main"

with open('linkler.json', 'r') as f:
    target_sites = json.load(f)

for site, url in target_sites.items():
    print(f"🛠️ {site} kontrol ediliyor...")
    path = f"{site}/src/main/kotlin/com/emin"
    os.makedirs(path, exist_ok=True)

    # Bot önce Kekik'te, bulamazsa Nikstream'de arar
    sources_to_try = [
        f"{KEKIK_BASE}/{site}/src/main/kotlin/com/kekik/{site}.kt",
        f"{KEKIK_BASE}/{site}/src/main/kotlin/com/kekik/{site}Provider.kt",
        f"{NIK_BASE}/{site}/src/main/kotlin/com/pitipitii/{site}.kt",
        f"{NIK_BASE}/{site}/src/main/kotlin/com/pitipitii/{site}Provider.kt"
    ]

    success = False
    for src_url in sources_to_try:
        try:
            response = requests.get(src_url)
            if response.status_code == 200:
                code = response.text
                # Link Montajı
                code = code.replace('mainUrl = "', f'mainUrl = "{url}')
                code = code.replace('baseUrl = "', f'baseUrl = "{url}')
                # Paket İsmi Revizyonu
                code = code.replace('package com.pitipitii', 'package com.emin')
                code = code.replace('package com.kekik', 'package com.emin')
                
                with open(f"{path}/{site}Provider.kt", "w", encoding='utf-8') as f:
                    f.write(code)
                print(f"✅ {site} başarıyla çekildi ve güncellendi.")
                success = True
                break
        except:
            continue
    
    if not success:
        print(f"⚠️ {site} hiçbir kaynakta bulunamadı. Klasör yapısını kontrol et.")
