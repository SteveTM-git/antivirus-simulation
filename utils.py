import os

def get_all_files(directory):
    file_list = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    
    return file_list

import json

def load_signatures(file_path="signatures.json"):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return set(data.get("malware_signatures", []))
    except Exception as e:
        print(f"[ERROR] Failed to load signatures: {e}")
        return set()
import shutil
import os

def move_to_quarantine(file_path, quarantine_dir="quarantine"):
    try:
        if not os.path.exists(quarantine_dir):
            os.makedirs(quarantine_dir)

        file_name = os.path.basename(file_path)
        destination = os.path.join(quarantine_dir, file_name)

        shutil.move(file_path, destination)

        print(f"Moved to quarantine: {destination}")

    except Exception as e:
        print(f"[ERROR] Failed to quarantine {file_path}: {e}")