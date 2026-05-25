import os
import json
import hashlib
import requests
import zipfile
from datetime import date, datetime, timezone
import io
import gzip
from pathlib import Path

# Configurazione
GTFS_URL = "https://www.gtt.to.it/open_data/gtt_gtfs.zip"
OUTPUT_DIR = Path("public_data")
VERSIONS_FILE =  OUTPUT_DIR / "versions.json"

def get_file_hash(file_bytes):
    """Calcola l'hash MD5 del contenuto scompattato."""
    return hashlib.md5(file_bytes).hexdigest()

def main(compress:bool=True):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if VERSIONS_FILE.exists():
        with open(VERSIONS_FILE, 'r', encoding='utf-8') as f:
            versions = json.load(f)
    else:
        versions = {}

    print(f"Scaricando GTFS da {GTFS_URL}...")
    response = requests.get(GTFS_URL)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        for filename in z.namelist():
            if not filename.endswith('.txt'): 
                continue

            print(f"Elaborando {filename}...")
            file_bytes = z.read(filename)
            
            # L'hash viene calcolato sui byte RAW (scompattati)
            current_hash = get_file_hash(file_bytes)

            file_info = versions.get(filename, {})
            changed = False
            timenow = datetime.now(timezone.utc).replace(microsecond=0)
            version_num = int(file_info.get("version_int", -1))
            if file_info.get("hash") != current_hash:
                print(f" -> [AGGIORNATO] {filename} è cambiato.")
                file_info["hash"] = current_hash
                file_info["last_modified"] = timenow.isoformat()
                file_info["version_int"] = version_num+1
                versions[filename] = file_info
                changed = True
            else:
                print(f" -> [INVARIATO] {filename}.")

            # Gestione speciale per la tabella molto grande
            #if filename == "connections.txt":
            if(compress):
                output_filename = filename + ".gz"
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                
                print(f" -> Comprimo {filename} in formato Gzip...")
                with gzip.open(output_path, 'wb', compresslevel=6) as f_out:
                    f_out.write(file_bytes)
                
            else:
                # Tutti gli altri file standard rimangono in formato testo libero
                output_path = os.path.join(OUTPUT_DIR, filename)
                with open(output_path, 'wb') as f:
                    f.write(file_bytes)
            

    # Salva il file delle versioni
    with open(VERSIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(versions, f, indent=4)
        
    print("Elaborazione e compressione completate.")

if __name__ == "__main__":
    main(True)