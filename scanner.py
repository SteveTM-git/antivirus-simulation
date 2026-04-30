import sys
from hasher import calculate_sha256
from utils import get_all_files, load_signatures, move_to_quarantine
from logger import log

def scan_directory(path):
    print("DEBUG: scan started")

    files = get_all_files(path)
    print(f"DEBUG: Found {len(files)} files")

    signatures = load_signatures()
    for file in files:
        file_hash = calculate_sha256(file)

        if not file_hash:
            continue

        print(f"[FILE] {file}")
        print(f"       SHA256: {file_hash}")

        log(f"Scanned: {file} | Hash: {file_hash}")

        if file_hash in signatures:
            print("MALICIOUS FILE DETECTED!")
            log(f"ALERT: Malicious file detected → {file}")

            move_to_quarantine(file)
            log(f"ACTION: Moved to quarantine → {file}")

            print()
        else:
            print("Safe\n")
            log(f"SAFE: {file}")



if __name__ == "__main__":
    print("DEBUG: script started")

    if len(sys.argv) != 2:
        print("Usage: python scanner.py <directory_path>")
        sys.exit(1)

    target_path = sys.argv[1]
    scan_directory(target_path)