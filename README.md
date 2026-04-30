# 🛡️ Basic Antivirus Simulation (Signature-Based Scanner)

A Python-based antivirus simulation that detects malicious files using SHA-256 hash comparison and isolates them using a quarantine mechanism.

---

## 🚀 Features

- 🔍 Recursive file scanning
- 🔐 SHA-256 hashing for file fingerprinting
- 🚨 Signature-based malware detection
- 📦 Automatic quarantine of infected files
- 📜 Logging system for audit and traceability

---

## 📸 Photo

<img width="528" height="440" alt="image" src="https://github.com/user-attachments/assets/fb690e28-2468-4d8c-a86a-102774f5d307" />

---

## 🧠 How It Works

1. The scanner traverses a directory recursively.
2. Each file is hashed using SHA-256.
3. The hash is compared against a database of known malware signatures.
4. If a match is found:
   - The file is flagged as malicious
   - It is moved to a quarantine folder
   - The event is logged

---

## 📂 Project Structure
antivirus_sim/
│── scanner.py # Main scanning engine
│── hasher.py # SHA-256 hashing
│── utils.py # File handling & quarantine logic
│── logger.py # Logging system
│── signatures.json # Malware signature database
│── quarantine/ # Isolated malicious files
---

## ▶️ Usage

```bash
python scanner.py <directory_path>
Example:
python scanner.py .
📄 Sample Output
[FILE] ./test.txt
SHA256: 2cf24dba5...
MALICIOUS FILE DETECTED!
Moved to quarantine: quarantine/test.txt
Disclaimer
This project is for educational purposes only.
It demonstrates signature-based detection and does not replace real antivirus software.
🛠️ Tech Stack
Python
File System Handling
Cryptographic Hashing (SHA-256)
🚀 Future Improvements
Real-time file monitoring
Heuristic-based detection
GUI dashboard
Integration with threat intelligence APIs

---

