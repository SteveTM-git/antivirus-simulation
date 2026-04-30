import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    except Exception as e:
        print(f"[ERROR] Cannot read file: {file_path} | {e}")
        return None