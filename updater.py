import os
import requests
import json
import shutil

# Senin istediğin sitelerin kaynak kodları (Kekik ve Nikstream'den referans)
SOURCES = {
    "DiziPal": "https://raw.githubusercontent.com/sarapcanagii/Pitipitii/main/DiziPal/src/main/kotlin/com/pitipitii/DiziPal.kt",
    "InatBox": "https://raw.githubusercontent.com/sarapcanagii/Pitipitii/main/InatBox/src/main/kotlin/com/pitipitii/InatBox.kt"
}

with open('linkler.json', 'r') as f:
    target_sites = json.load(f)

for site, url in target_sites.items():
    print(f"🚀 {site} hazırlanıyor...")
    
    # 1. Klasör yapısını otomatik kur (Sen uğraşma diye)
    path = f"{site}/src/main/kotlin/com/emin"
    os.makedirs(path, exist_ok=True)
    
    # 2. Kaynak kodu internetten çek
    if site in SOURCES:
        source_code = requests.get(SOURCES[site]).text
        # Linki senin verdiğinle değiştir
        updated_code = source_code.replace('mainUrl = "', f'mainUrl = "{url}')
        
        # 3. Senin repona yaz
        with open(f"{path}/{site}.kt", "w") as f:
            f.write(updated_code)
        print(f"✅ {site} klasörü ve linki otomatik oluşturuldu.")
